# Private Governance Model

## Separation of concerns

Hinui Prestige Group Auto Group should distinguish four logical classes of assets:

1. **Family assets** — assets acquired or held for family purposes.
2. **Operating assets** — assets held by the automotive operating business.
3. **Customer/third-party assets** — assets held or handled on behalf of customers.
4. **Restricted/proposed assets** — assets under evaluation or subject to unresolved approval/compliance conditions.

These classes must never be silently merged in reporting, custody, accounting or authorization workflows.

## Acquisition state machine

```text
PROPOSED
  -> DUE_DILIGENCE
  -> APPROVED
  -> FUNDED
  -> SETTLED
  -> IN_CUSTODY
  -> ACTIVE
  -> EXIT_PROPOSED
  -> DISPOSED / TRANSFERRED
```

Every transition requires an actor, timestamp, policy decision and evidence reference.

## Family authorization

The platform should support configurable approval tiers rather than hard-coding a single family hierarchy. Examples include:

- ordinary operating expenditure
- vehicle acquisition
- high-value acquisition
- financing or leverage
- asset transfer
- sale/disposal
- related-party transaction
- estate/succession transfer

Actual thresholds should be configured by the governing family/legal structure.

## Privacy model

Family identity, financial information, private addresses, asset locations and sensitive documents should be treated as restricted data. Public dealer workflows should receive only the minimum information required to perform their function.

## Evidence

Material actions should reference evidence rather than relying on narrative notes:

- acquisition proposal
- approval record
- invoice/contract
- settlement confirmation
- registration/title record
- insurance
- inspection
- maintenance record
- valuation
- disposition/transfer record
