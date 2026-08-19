# Henry Prestige Group Auto Group

**Private New Zealand family-asset acquisition sandbox demo**

Henry Prestige Group Auto Group (HPG) is a reference architecture for a privately controlled, New Zealand-only digital acquisition environment for high-value vehicles and related family assets.

It is designed to bridge:

- family/private acquisition governance
- luxury vehicle inventory and allocation
- portfolio aggregation
- cash-position visibility
- acquisition readiness
- provenance and asset records
- AML/CFT and customer due diligence controls
- transparent human approval
- optional future RWA/tokenisation interfaces

## Non-negotiable design boundary

This repository is a **sandbox/demo**, not a licensed dealer, financial adviser, custodial service, exchange, trustee, bank, or securities platform. No live customer funds, securities, tokens, or regulated financial advice should be enabled by this reference implementation.

The system is designed to fail closed when a regulated activity, missing approval, unresolved identity, source-of-funds issue, sanctions/PEP concern, privacy issue, or jurisdiction violation is detected.

## New Zealand-only operating model

Production deployment should enforce:

1. NZ-only user access and approved NZ operational roles.
2. NZ-region hosting and storage wherever commercially and technically available.
3. No overseas disclosure of personal information without a documented Privacy Act 2020 / IPP 12 decision.
4. Connector allowlisting and data minimisation.
5. Audit logging of every acquisition decision and material data access.
6. Human approval before commitment, settlement, transfer, or regulated advice.

## Portfolio bridge

The architecture uses a **read-only portfolio aggregation boundary**. External portfolio providers such as Delta, Finary, Snowball Analytics, Sharesight and bank/cash-account sources are treated as data sources, not as authorities for acquisition approval.

Each imported position is normalised into a canonical asset model with source, timestamp, confidence, ownership context, and reconciliation state.

## Acquisition lifecycle

`Intent → Identity → Ownership Structure → Portfolio Snapshot → Liquidity Test → Source of Funds → Asset Due Diligence → Compliance Gate → Human Approval → Settlement → Registration → Asset Register → Ongoing Monitoring`

## Governance

`Specification → Implementation → Verification → Evidence → Change Control → Archive → Agent Context → Drift Detection`

## Regulatory design references

The compliance model is aligned to the current New Zealand regulatory source material captured in `docs/compliance/nz-gold-standard.md`. It must be reviewed by qualified New Zealand legal/compliance professionals before any production use.
