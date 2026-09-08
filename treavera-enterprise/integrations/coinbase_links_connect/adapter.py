"""Governed Coinbase adapter for Henry APEX.

The adapter deliberately separates data normalization from transaction execution.
A live Coinbase/AgentKit client is injected at runtime; credentials are never
accepted as persisted configuration.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from decimal import Decimal
from hashlib import sha256
import json
from typing import Any, Literal, Protocol

Operation = Literal[
    "get_wallet_details",
    "get_balance",
    "native_transfer",
]


class CoinbaseClient(Protocol):
    """Minimal runtime contract implemented by the Coinbase AgentKit adapter."""

    def get_wallet_details(self) -> Any: ...
    def get_balance(self, asset_id: str | None = None) -> Any: ...
    def native_transfer(self, amount: str, asset_id: str, destination: str) -> Any: ...


@dataclass(frozen=True)
class Authority:
    operation: Operation
    mode: Literal["read", "prepare", "execute"] = "read"
    human_approval: bool = False
    max_amount: Decimal | None = None
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
    """Normalize provider output without assuming a single Coinbase response shape."""
    if hasattr(wallet, "model_dump"):
        wallet = wallet.model_dump()
    elif hasattr(wallet, "__dict__"):
        wallet = vars(wallet)
    if not isinstance(wallet, dict):
        return {"raw": str(wallet)}
    return {
        "provider": "coinbase",
        "wallet_id": wallet.get("id") or wallet.get("wallet_id"),
        "address": wallet.get("address") or wallet.get("default_address"),
        "network": wallet.get("network"),
        "raw": wallet,
    }


class CoinbaseLinksConnectAdapter:
    """Henry APEX policy boundary around Coinbase AgentKit capabilities."""

    provider = "coinbase"

    def __init__(self, client: CoinbaseClient):
        self.client = client

    def wallet_details(self, authority: Authority) -> tuple[dict[str, Any], AuditEvent]:
        self._allow(authority, "get_wallet_details")
        result = normalize_wallet(self.client.get_wallet_details())
        return result, self._audit(authority, {"operation": "get_wallet_details"}, "ok")

    def balance(self, authority: Authority, asset_id: str | None = None) -> tuple[Any, AuditEvent]:
        self._allow(authority, "get_balance")
        payload = {"operation": "get_balance", "asset_id": asset_id}
        result = self.client.get_balance(asset_id)
        return result, self._audit(authority, payload, "ok")

    def native_transfer(
        self,
        authority: Authority,
        amount: Decimal,
        asset_id: str,
        destination: str,
    ) -> tuple[Any, AuditEvent]:
        self._allow(authority, "native_transfer")
        if authority.mode != "execute":
            raise PolicyDenied("native_transfer must use execute mode after policy approval")
        if not authority.human_approval:
            raise PolicyDenied("human approval is required for native transfers")
        if authority.max_amount is not None and amount > authority.max_amount:
            raise PolicyDenied("transfer exceeds the APEX authority limit")

        payload = {
            "operation": "native_transfer",
            "amount": str(amount),
            "asset_id": asset_id,
            "destination": destination,
            "network": authority.network,
        }
        result = self.client.native_transfer(str(amount), asset_id, destination)
        return result, self._audit(authority, payload, "ok")

    def _allow(self, authority: Authority, operation: Operation) -> None:
        if authority.operation != operation:
            raise PolicyDenied(f"authority permits {authority.operation}, not {operation}")
        if authority.mode not in {"read", "prepare", "execute"}:
            raise PolicyDenied("invalid authority mode")

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
