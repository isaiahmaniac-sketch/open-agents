# Agent Context Contract

Agent context is the governed operational interface to Treavera knowledge.

## Context layers

1. **Identity** — actor, tenant, role and delegated authority.
2. **Policy** — applicable rules and approval requirements.
3. **Knowledge** — current approved domain facts.
4. **Skills** — executable procedures and constraints.
5. **Evidence** — supporting implementation and verification references.
6. **History** — relevant prior decisions and superseded state.

Agents should consume the current context layer rather than copying whole documentation sets into prompts. Context must be scoped to the task and authority of the requesting actor.
