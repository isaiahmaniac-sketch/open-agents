# Henry APEX — NZ Compliance-by-Design Standard

**Status:** Architecture baseline
**Jurisdiction:** New Zealand only
**Production principle:** Fail closed when mandatory controls, evidence or human authority are missing.

## Constitutional rules

1. Compliance is an executable control, not a document-only claim.
2. Agents may recommend, analyse and prepare; they cannot create or expand their own authority.
3. Consequential actions require deterministic policy enforcement outside the model and appropriate human oversight.
4. Production promotion requires human acceptance and explicit production approval.
5. Personal-information workflows require privacy-by-design assessment and evidence.
6. Indirect collection requires an IPP3A applicability and notification assessment where applicable.
7. Provider/API terms are part of the integration control boundary.
8. Audit, provenance and evidence are mandatory for consequential workflows.
9. Missing or stale controls fail closed to REVIEW or DENY.
10. International standards may inform engineering controls, but NZ law, applicable NZ requirements and provider terms are the authoritative compliance boundary.

## Assurance loop

NZ obligations → applicability → risk → controls → build → test → evidence → human acceptance → controlled release → monitoring → drift detection → reassessment.

## Required control-plane registries

- obligations
- applicability decisions
- controls
- AI systems / models / agents
- data provenance
- permissions and authority
- human approvals
- evidence
- exceptions
- incidents
- releases
- compliance drift

## Privacy-by-design minimum

For workflows involving personal information, APEX must be able to record the information source, collection method, purpose, recipients, retention, access/correction handling and relevant notification assessment. A Privacy Impact Assessment is required before personal-information use with AI, with periodic review.

## Release gate

`IDENTITY → JURISDICTION → APPLICABILITY → RISK → CONTROLS → SECURITY TESTS → AI EVALUATION → EVIDENCE → HUMAN ACCEPTANCE → PRODUCTION APPROVAL → CONTROLLED RELEASE → MONITORING`

No bypass path is permitted for agents.

## Current implementation scope

The Coinbase/Links Connect integration is deliberately READ + PREPARE ONLY. Live transaction execution is disabled. The integration must not be treated as production-ready until the central APEX execution firewall, persistent execution ledger, structured human approval, emergency stop, policy engine, evidence pipeline and deployment gates are implemented and independently tested.
