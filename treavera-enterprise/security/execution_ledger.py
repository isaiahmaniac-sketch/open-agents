"""Durable idempotency ledger for Henry APEX consequential operations."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import sqlite3
from threading import RLock


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
    """Interface for an atomically persistent execution ledger."""

    def reserve(self, record: ExecutionRecord) -> ExecutionRecord:
        raise NotImplementedError

    def get(self, idempotency_key: str) -> ExecutionRecord | None:
        raise NotImplementedError


class SQLiteExecutionLedger(ExecutionLedger):
    """Small durable implementation for development/staging.

    Production deployments should place the same contract behind a managed,
    access-controlled database with durable backups and immutable audit policy.
    """

    def __init__(self, path: str = "apex_execution_ledger.sqlite3") -> None:
        self._db = sqlite3.connect(path, check_same_thread=False)
        self._db.execute("PRAGMA journal_mode=WAL")
        self._db.execute(
            """CREATE TABLE IF NOT EXISTS execution_ledger (
                idempotency_key TEXT PRIMARY KEY,
                request_fingerprint TEXT NOT NULL,
                state TEXT NOT NULL,
                result_reference TEXT
            )"""
        )
        self._db.commit()
        self._lock = RLock()

    def reserve(self, record: ExecutionRecord) -> ExecutionRecord:
        with self._lock:
            existing = self.get(record.idempotency_key)
            if existing is not None:
                if existing.request_fingerprint != record.request_fingerprint:
                    return ExecutionRecord(
                        record.idempotency_key,
                        record.request_fingerprint,
                        ExecutionState.CONFLICT,
                    )
                return existing
            self._db.execute(
                "INSERT INTO execution_ledger VALUES (?, ?, ?, ?)",
                (record.idempotency_key, record.request_fingerprint, record.state.value, record.result_reference),
            )
            self._db.commit()
            return record

    def get(self, idempotency_key: str) -> ExecutionRecord | None:
        row = self._db.execute(
            "SELECT idempotency_key, request_fingerprint, state, result_reference "
            "FROM execution_ledger WHERE idempotency_key = ?",
            (idempotency_key,),
        ).fetchone()
        if row is None:
            return None
        return ExecutionRecord(row[0], row[1], ExecutionState(row[2]), row[3])

    def close(self) -> None:
        self._db.close()
