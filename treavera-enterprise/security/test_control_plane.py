from __future__ import annotations

import pytest

from drift_control import DriftSeverity, assert_release_safe, compare_baseline
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
