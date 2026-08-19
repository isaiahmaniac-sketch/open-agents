# Treavera Enterprise Skill Governance

## Purpose
Define how skills are authored, verified, versioned, consumed by agents, and retired.

## Required skill lifecycle

1. **Specify** — define purpose, inputs, outputs, authority boundaries, failure modes and acceptance criteria.
2. **Implement** — keep executable logic and adapters version controlled.
3. **Verify** — test documented claims against implementation and runtime behaviour.
4. **Evidence** — record source files, tests, commits and verification results.
5. **Change control** — associate material changes with an issue/PR and decision record.
6. **Archive** — preserve superseded specifications and evidence rather than deleting history.
7. **Agent context** — publish the current governed operational interface for agents.
8. **Drift detection** — continuously compare governed claims with implementation and evidence.

## Authority rules

- Skills may recommend actions but must respect policy, identity, RBAC and approval gates.
- High-impact financial, legal, compliance or ownership actions require explicit policy evaluation and an auditable decision record.
- Agents must not silently mutate governance records.
- Evidence must identify the implementation version used for a conclusion.
