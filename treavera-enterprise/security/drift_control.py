"""Deterministic drift controls for Henry APEX.

This module treats policy, authority, control manifests and approved artifacts as
versioned state. A material mismatch blocks promotion rather than silently
accepting drift.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
from typing import Mapping


class DriftSeverity(str, Enum):
    NONE = "NONE"
    REVIEW = "REVIEW"
    BLOCK = "BLOCK"


@dataclass(frozen=True)
class DriftFinding:
    control: str
    expected: str
    actual: str
    severity: DriftSeverity
    reason: str


@dataclass(frozen=True)
class DriftReport:
    status: DriftSeverity
    findings: tuple[DriftFinding, ...]
    baseline_fingerprint: str
    observed_fingerprint: str


def fingerprint(state: Mapping[str, object]) -> str:
    canonical = json.dumps(state, sort_keys=True, separators=(",", ":"), default=str)
    return sha256(canonical.encode("utf-8")).hexdigest()


def compare_baseline(
    baseline: Mapping[str, object],
    observed: Mapping[str, object],
    *,
    blocked_controls: frozenset[str] = frozenset(),
) -> DriftReport:
    """Compare security/compliance state and fail closed on material drift."""
    findings: list[DriftFinding] = []
    for key in sorted(set(baseline) | set(observed)):
        expected = baseline.get(key)
        actual = observed.get(key)
        if expected == actual:
            continue
        severity = DriftSeverity.BLOCK if key in blocked_controls else DriftSeverity.REVIEW
        findings.append(
            DriftFinding(
                control=key,
                expected=str(expected),
                actual=str(actual),
                severity=severity,
                reason="approved baseline differs from observed state",
            )
        )

    status = DriftSeverity.NONE
    if findings:
        status = DriftSeverity.BLOCK if any(f.severity == DriftSeverity.BLOCK for f in findings) else DriftSeverity.REVIEW
    return DriftReport(status, tuple(findings), fingerprint(baseline), fingerprint(observed))


def assert_release_safe(report: DriftReport) -> None:
    """Block production when any material drift is present."""
    if report.status != DriftSeverity.NONE:
        raise RuntimeError(f"APEX release blocked: drift status={report.status.value}")
