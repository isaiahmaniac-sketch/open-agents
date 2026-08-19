# HPG Architecture

```text
                         ┌─────────────────────────┐
                         │ Private Family Portal   │
                         │ NZ-only access          │
                         └────────────┬────────────┘
                                      │
                         ┌────────────▼────────────┐
                         │ Acquisition Orchestrator │
                         └──────┬───────┬──────────┘
                                │       │
                 ┌──────────────┘       └──────────────┐
                 ▼                                     ▼
        ┌─────────────────┐                   ┌─────────────────┐
        │ Compliance Gate │                   │ Portfolio Bridge│
        │ AML/CFT / KYC   │                   │ read-only       │
        │ privacy / policy│                   │ normalisation   │
        └────────┬────────┘                   └────────┬────────┘
                 │                                     │
                 └────────────────┬────────────────────┘
                                  ▼
                       ┌─────────────────────┐
                       │ Acquisition Ledger  │
                       │ evidence + decisions│
                       └──────────┬──────────┘
                                  ▼
                       ┌─────────────────────┐
                       │ Human Approval Gate │
                       └──────────┬──────────┘
                                  ▼
                       ┌─────────────────────┐
                       │ Settlement Adapter  │
                       │ sandbox only        │
                       └─────────────────────┘
```

## Components

### Family Portal

Private interface for family members and authorised operators. Shows asset opportunities, portfolio context, acquisition readiness, provenance and approval status without exposing unnecessary sensitive data.

### Acquisition Orchestrator

Coordinates the workflow but does not independently authorise settlement or regulated advice.

### Compliance Gate

Policy engine implementing deny-by-default checks for identity, beneficial ownership, source of funds, sanctions/PEP screening where applicable, transaction risk, privacy, jurisdiction and required human approvals.

### Portfolio Bridge

Normalises read-only holdings and cash data from approved connectors. It does not initiate trades, move money, or infer ownership without reconciliation.

### Acquisition Ledger

Immutable-style append-only evidence model containing decisions, source records, timestamps, actor identity, policy version and verification status.

### Settlement Adapter

Sandbox adapter only. A production implementation must be separately reviewed for banking, payments, custody and financial-services licensing boundaries.

## Data sovereignty

The default architecture is NZ-resident processing. Overseas APIs are disabled by default for personal data. Every connector must declare:

- data categories
- geographic processing locations
- retention
- encryption
- contractual privacy safeguards
- deletion capability
- legal basis / purpose
- operator approval
