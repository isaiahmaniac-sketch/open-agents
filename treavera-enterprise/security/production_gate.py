"""Fail-closed production authorization state machine."""
from __future__ import annotations

from enum import StrEnum


class ReleaseState(StrEnum):
    DEVELOPMENT = "DEVELOPMENT"
    TEST = "TEST"
    SECURITY_REVIEW = "SECURITY_REVIEW"
    STAGING = "STAGING"
    HUMAN_ACCEPTANCE = "HUMAN_ACCEPTANCE"
    PRODUCTION_APPROVAL = "PRODUCTION_APPROVAL"
    RELEASED = "RELEASED"
    BLOCKED = "BLOCKED"


_ALLOWED = {
    ReleaseState.DEVELOPMENT: {ReleaseState.TEST, ReleaseState.BLOCKED},
    ReleaseState.TEST: {ReleaseState.SECURITY_REVIEW, ReleaseState.BLOCKED},
    ReleaseState.SECURITY_REVIEW: {ReleaseState.STAGING, ReleaseState.BLOCKED},
    ReleaseState.STAGING: {ReleaseState.HUMAN_ACCEPTANCE, ReleaseState.BLOCKED},
    ReleaseState.HUMAN_ACCEPTANCE: {ReleaseState.PRODUCTION_APPROVAL, ReleaseState.BLOCKED},
    ReleaseState.PRODUCTION_APPROVAL: {ReleaseState.RELEASED, ReleaseState.BLOCKED},
    ReleaseState.RELEASED: {ReleaseState.BLOCKED},
    ReleaseState.BLOCKED: {ReleaseState.DEVELOPMENT},
}


def transition(current: ReleaseState, target: ReleaseState, *, human_authorized: bool = False) -> ReleaseState:
    if target not in _ALLOWED[current]:
        raise PermissionError(f"invalid release transition: {current} -> {target}")
    if target in {ReleaseState.PRODUCTION_APPROVAL, ReleaseState.RELEASED} and not human_authorized:
        raise PermissionError("human authorization is required for production promotion")
    return target
