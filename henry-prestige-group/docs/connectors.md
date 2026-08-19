# Portfolio Connector Governance

All portfolio and cash-account connectors are **read-only by default**.

## Connector contract

Every connector must declare:

```yaml
name:
provider:
data_classes:
read_capabilities:
write_capabilities: []
processing_countries:
storage_countries:
retention:
encryption:
privacy_assessment:
last_verified:
owner:
status:
```

## Examples

The sandbox can model adapters for Delta, Finary, Snowball Analytics, Sharesight and cash/broker accounts. Exact APIs, commercial terms and permissions must be verified independently before implementation.

## Reconciliation

A portfolio balance is not treated as settlement-ready cash until:

- source is authenticated
- timestamp is known
- account ownership is reconciled
- currency is known
- duplicate feeds are resolved
- data freshness meets policy
- connector residency is approved

## No transaction authority

Portfolio connectors cannot:

- execute trades
- withdraw funds
- transfer assets
- change beneficiaries
- approve an acquisition

Those capabilities belong outside the read-only aggregation boundary and require separate authorisation.
