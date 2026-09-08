"""NZ compliance-by-design primitives for Henry APEX.

This module is intentionally deterministic and independent of any LLM. It is a
control-plane primitive: missing controls fail closed and consequential actions
can be routed to human review.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable


class Decision(str, Enum):
    ALLOW = "ALLOW"
    REVIEW = "REVIEW"
    DENY = "DENY"


@dataclass(frozen=True)
class ComplianceContext:
    jurisdiction: str = "NZ"
    personal_information: bool = False
    indirect_collection: bool = False
    consequential_action: bool = False
    human_review_complete: bool = False
    privacy_impact_assessment_complete: bool = False
    evidence_complete: bool = False
    provider_terms_accepted: bool = True
    production_approved: bool = False
    controls: frozenset[str] = field(default_factory=frozenset)


@dataclass(frozen=True)
class ComplianceDecision:
    decision: Decision
    reasons: tuple[str, ...]
    required_controls: tuple[str, ...]


class NZComplianceEngine:
    """Fail-closed NZ compliance gate for APEX workflows."""

    BASE_CONTROLS = frozenset({"NZ-JURISDICTION", "AUDIT", "PROVENANCE"})

    def evaluate(self, context: ComplianceContext) -> ComplianceDecision:
        reasons: list[str] = []
        required = set(self.BASE_CONTROLS)

        if context.jurisdiction != "NZ":
            return ComplianceDecision(Decision.DENY, ("APEX is NZ-only",), tuple(sorted(required)))

        if context.personal_information:
            required.add("PRIVACY-ACT-2020")
            if not context.privacy_impact_assessment_complete:
                reasons.append("privacy impact assessment is incomplete")

        if context.indirect_collection:
            required.add("IPP3A")
            reasons.append("IPP3A notification applicability must be resolved")

        if context.consequential_action and not context.human_review_complete:
            required.add("HUMAN-OVERSIGHT")
            reasons.append("human review is required before consequential action")

        if not context.provider_terms_accepted:
            reasons.append("provider terms have not been accepted")

        if not context.evidence_complete:
            reasons.append("required evidence is incomplete")

        missing = required - set(context.controls)
        if missing:
            reasons.append("required controls missing: " + ", ".join(sorted(missing)))

        if reasons:
            return ComplianceDecision(Decision.REVIEW, tuple(reasons), tuple(sorted(required)))

        if not context.production_approved:
            return ComplianceDecision(Decision.REVIEW, ("production approval is missing",), tuple(sorted(required)))

        return ComplianceDecision(Decision.ALLOW, (), tuple(sorted(required)))


def controls(*names: str) -> frozenset[str]:
    return frozenset(names)
