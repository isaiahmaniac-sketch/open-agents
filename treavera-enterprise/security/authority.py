"""Human authority and emergency-stop primitives for Henry APEX."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
from typing import Any


class AuthorityDenied(PermissionError):
    pass


@dataclass(frozen=True)
class HumanApproval:
    approver_id: str
    action: str
    request_fingerprint: str
    approved_at: str
    expires_at: str
    approval_id: str

    def valid_for(self, action: str, fingerprint: str, now: datetime | None = None) -> bool:
        if action != self.action or fingerprint != self.request_fingerprint:
            return False
        current = now or datetime.now(timezone.utc)
        expiry = datetime.fromisoformat(self.expires_at.replace("Z", "+00:00"))
        return current < expiry


class EmergencyStop:
    def __init__(self) -> None:
        self._stopped = False

    def stop(self) -> None:
        self._stopped = True

    def reset(self) -> None:
        self._stopped = False

    def assert_running(self) -> None:
        if self._stopped:
            raise AuthorityDenied("APEX emergency stop is active")


def request_fingerprint(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    return sha256(canonical.encode("utf-8")).hexdigest()
