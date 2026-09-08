from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from authority import AuthorityDenied, EmergencyStop, HumanApproval, request_fingerprint
from drift_control import DriftSeverity, assert_release_safe, compare_baseline
from execution_ledger import ExecutionRecord, ExecutionState, SQLiteExecutionLedger
from production_gate import ReleaseState, transition


def test_material_blocked_drift_fails_closed():
    report = compare_baseline(
        {"execution_enabled": False, "human_approval": True},
        {"execution_enabled": True, "human_approval": True},
        blocked_controls=frozenset({"execution_enabled"}),
    )
    assert report.status == DriftSeverity.BLOCK
    with pytest.raises(RuntimeError):
        assert_release_safe(report)


def test_non_blocked_drift_requires_review():
    report = compare_baseline({"policy_version": "1"}, {"policy_version": "2"})
    assert report.status == DriftSeverity.REVIEW
    with pytest.raises(RuntimeError):
        assert_release_safe(report)


def test_structured_approval_is_bound_to_exact_request():
    payload = {"operation": "prepare_native_transfer", "amount": "1", "destination": "0xabc"}
    fingerprint = request_fingerprint(payload)
    now = datetime.now(timezone.utc)
    approval = HumanApproval(
        "human-1", "prepare_native_transfer", fingerprint,
        now.isoformat(), (now + timedelta(minutes=5)).isoformat(), "approval-1",
    )
    assert approval.valid_for("prepare_native_transfer", fingerprint, now)
    assert not approval.valid_for(
        "prepare_native_transfer",
        request_fingerprint({**payload, "amount": "2"}),
        now,
    )
    assert not approval.valid_for("get_balance", fingerprint, now)


def test_expired_approval_is_denied():
    now = datetime.now(timezone.utc)
    approval = HumanApproval(
        "human-1", "prepare_native_transfer", "fp", now.isoformat(),
        (now - timedelta(seconds=1)).isoformat(), "approval-2",
    )
    assert not approval.valid_for("prepare_native_transfer", "fp", now)


def test_emergency_stop_is_fail_closed():
    stop = EmergencyStop()
    stop.stop()
    with pytest.raises(AuthorityDenied):
        stop.assert_running()


def test_ledger_rejects_idempotency_key_reuse_with_changed_request(tmp_path):
    ledger = SQLiteExecutionLedger(str(tmp_path / "ledger.sqlite3"))
    first = ExecutionRecord("key-1", "fingerprint-a", ExecutionState.NEW)
    second = ExecutionRecord("key-1", "fingerprint-b", ExecutionState.NEW)
    assert ledger.reserve(first) == first
    conflict = ledger.reserve(second)
    assert conflict.state == ExecutionState.CONFLICT
    assert ledger.get("key-1") == first
    ledger.close()


def test_production_requires_human_authorization():
    with pytest.raises(PermissionError):
        transition(ReleaseState.HUMAN_ACCEPTANCE, ReleaseState.PRODUCTION_APPROVAL)
    assert transition(
        ReleaseState.HUMAN_ACCEPTANCE,
        ReleaseState.PRODUCTION_APPROVAL,
        human_authorized=True,
    ) == ReleaseState.PRODUCTION_APPROVAL


def test_release_requires_human_authorization():
    with pytest.raises(PermissionError):
        transition(ReleaseState.PRODUCTION_APPROVAL, ReleaseState.RELEASED)
