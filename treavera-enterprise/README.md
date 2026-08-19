# Treavera Enterprise

Enterprise agent platform foundation: AI control plane, governed domain agents, shared contracts, skills, evidence, change control, archive, and continuous drift detection.

## Architecture

```text
Executive Dashboard / Customer Portal / Admin Console
                         |
                    API Gateway
                         |
                  AI Control Plane
     +-------------------+-------------------+
     |                   |                   |
 Workflow Engine    Policy Gateway     Agent Registry
     |                   |                   |
 Memory / Knowledge  Identity / RBAC   Skill Runtime
                         |
          +--------------+--------------+
          |              |              |
      Treasury       Compliance     Automotive
       Agent           Agent          Agent
          |              |              |
          +--------------+--------------+
                         |
                Evidence + Audit Log
                         |
             Change Control / Archive
                         |
                 Drift Detection
```

## Domain agents

- **Treasury** — liquidity forecasting, cash position, risk monitoring, yield optimisation.
- **Compliance** — policy evaluation, AML/KYC workflows, audit trail and reporting.
- **Automotive** — inventory, customer delivery, finance and vehicle handover.

## Governance principle

Documentation is a governed operational interface, not a passive knowledge store. Every material claim should be traceable to implementation, verification evidence, and the change that introduced it. Archived state preserves historical truth; agent context provides the current operational view; drift detection closes the control loop.

## Initial scope

This directory is intentionally a foundation layer. Domain implementations should be independently deployable and communicate through versioned contracts/events rather than sharing internal state.
