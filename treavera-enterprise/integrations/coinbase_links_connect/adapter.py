"""Read/prepare-only Coinbase boundary for Henry APEX.

There is deliberately NO transaction execution method here. Any future
execution capability must be implemented behind the central APEX execution
firewall, durable ledger, structured human approval, deterministic policy and
independently controlled emergency stop.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import sys
from typing import Any, Literal, Protocol

# The repository's top-level directory contains a hyphen, so add the security
# package directory explicitly rather than pretending the parent is importable.
_SECURITY_DIR = Path(__file__).resolve().parents[2] / "security"
if str(_SECURITY_DIR) not in sys.path:
    sys.path.insert(0, str(_SECURITY_DIR))

from authority import AuthorityDenied, EmergencyStop  # noqa: E402

Operation = Literal["get_wallet_details", "get_balance", "prepare_native_transfer"]
Mode = Literal["read", "prepare"]


class CoinbaseClient(Protocol):
    def get_wallet_details(self) -> Any: ...
    def get_balance(self, asset_id: str | None = None) -> Any: ...


@dataclass(frozen=True)
class Authority:
    operation: Operation
    mode: Mode = "read"
    network: str | None = None


@dataclass(frozen=True)
class AuditEvent:
    provider: str
    operation: str
    mode: str
    request_hash: str
    timestamp: str
    result: str


class PolicyDenied(PermissionError):
    pass


def idempotency_key(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    return sha256(canonical.encode("utf-8")).hexdigest()


def normalize_wallet(wallet: Any) -> dict[str, Any]:
    """Return an allowlisted projection; never propagate the raw provider object."""
    if hasattr(wallet, "model_dump"):
        wallet = wallet.model_dump()
    elif hasattr(wallet, "__dict__"):
        wallet = vars(wallet)
    if not isinstance(wallet, dict):
        return {"provider": "coinbase", "wallet_id": None, "address": None, "network": None}
    return {
        "provider": "coinbase",
        "wallet_id": wallet.get("id") or wallet.get("wallet_id"),
        "address": wallet.get("address") or wallet.get("default_address"),
        "network": wallet.get("network"),
    }


class CoinbaseLinksConnectAdapter:
    provider = "coinbase"

    def __init__(self, client: CoinbaseClient, emergency_stop: EmergencyStop | None = None):
        self.client = client
        # The default is now the central APEX security primitive, not a
        # connector-owned implementation. Tests may inject the same primitive.
        self.emergency_stop = emergency_stop or EmergencyStop()

    def wallet_details(self, authority: Authority) -> tuple[dict[str, Any], AuditEvent]:
        self._allow(authority, "get_wallet_details", "read")
        result = normalize_wallet(self.client.get_wallet_details())
        return result, self._audit(authority, {"operation": "get_wallet_details"}, "ok")

    def balance(self, authority: Authority, asset_id: str | None = None) -> tuple[Any, AuditEvent]:
        self._allow(authority, "get_balance", "read")
        payload = {"operation": "get_balance", "asset_id": asset_id}
        result = self.client.get_balance(asset_id)
        return result, self._audit(authority, payload, "ok")

    def prepare_native_transfer(
        self,
        authority: Authority,
        amount: str,
        asset_id: str,
        destination: str,
    ) -> tuple[dict[str, Any], AuditEvent]:
        """Create a non-executable intent. This method cannot move funds."""
        self._allow(authority, "prepare_native_transfer", "prepare")
        if not amount or not asset_id or not destination:
            raise PolicyDenied("transfer intent requires amount, asset and destination")
        payload = {
            "operation": "prepare_native_transfer",
            "amount": amount,
            "asset_id": asset_id,
            "destination": destination,
            "network": authority.network,
        }
        intent = {
            "status": "PREPARED_ONLY",
            "executable": False,
            "request_fingerprint": idempotency_key(payload),
            **payload,
        }
        return intent, self._audit(authority, payload, "prepared")

    def _allow(self, authority: Authority, operation: Operation, mode: Mode) -> None:
        try:
            self.emergency_stop.assert_running()
        except AuthorityDenied as exc:
            raise PolicyDenied(str(exc)) from exc
        if authority.operation != operation or authority.mode != mode:
            raise PolicyDenied("authority does not exactly match the requested operation")

    @staticmethod
    def _audit(authority: Authority, payload: dict[str, Any], result: str) -> AuditEvent:
        return AuditEvent(
            provider="coinbase",
            operation=authority.operation,
            mode=authority.mode,
            request_hash=idempotency_key(payload),
            timestamp=datetime.now(timezone.utc).isoformat(),
            result=result,
        )


def audit_dict(event: AuditEvent) -> dict[str, Any]:
    return asdict(event)
