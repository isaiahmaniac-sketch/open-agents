# Private Family Structure — Reference Only

This document describes a technology architecture, not a recommendation for a legal structure.

A possible production separation is:

```text
Family / Family Governance
        │
        ▼
Family Holding / Trust Structure
        │
        ├── Investment Portfolio(s)
        ├── Cash / Treasury Relationships
        └── HPG Acquisition Entity
                    │
                    ├── Vehicle Inventory
                    ├── Acquisition Contracts
                    └── Asset Register
```

The exact use of a company, trust, partnership, SPV or other entity must be determined by New Zealand legal, tax and estate-planning advisers.

The software therefore models `ownership_structure` as configuration rather than hard-coding a trust or company arrangement.

## Separation of duties

- Family principal: defines mandate
- Director/trustee/authorised representative: exercises legal authority
- Compliance role: reviews AML/CFT/privacy controls where applicable
- Acquisition operator: executes approved workflow
- AI: assists and records evidence, but has no legal authority

## Privacy principle

Private does not mean invisible. Statutory registers, tax obligations, AML/CFT obligations, consumer protections and other lawful disclosure obligations remain applicable where relevant.
