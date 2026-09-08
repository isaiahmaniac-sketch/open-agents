"""Persistent-ledger interface for idempotent consequential operations."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ExecutionState(str, Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CONFLICT = "CONFLICT"


@dataclass(frozen=True)
class ExecutionRecord:
    idempotency_key: str
    request_fingerprint: str
    state: ExecutionState
    result_reference: str | None = None


class ExecutionLedger:
    """Minimal interface; production implementations must persist atomically."""

    def reserve(self, record: ExecutionRecord) -> ExecutionRecord:
        raise NotImplementedError

    def get(self, idempotency_key: str) -> ExecutionRecord | None:
        raise NotImplementedError
