# HPG Acquisition Lifecycle

## Stage 0 — Intent

Capture vehicle/asset, target budget, intended family use, proposed ownership entity, timing and acquisition rationale.

## Stage 1 — Identity and authority

Verify the acquiring person/entity, authority to act, beneficial ownership and relationship to the family structure.

## Stage 2 — Portfolio snapshot

Import read-only positions and cash balances from approved sources. Timestamp every source and reconcile duplicates.

Example connector classes:

- Sharesight
- Delta portfolio tracker
- Finary
- Snowball Analytics
- bank/cash accounts
- broker/custodian feeds

Connector names are adapters, not endorsements or live integrations in this demo.

## Stage 3 — Liquidity and affordability

Calculate available liquidity, committed liquidity, concentration, financing needs and post-acquisition liquidity buffer. Keep calculations separate from regulated financial advice.

## Stage 4 — Source of funds / wealth

Collect evidence appropriate to the risk profile. Do not infer source of funds solely from portfolio balances.

## Stage 5 — Asset due diligence

For vehicles:

- VIN / chassis identity
- registered person
- PPSR / security-interest check where applicable
- ownership/provenance evidence
- odometer and condition
- compliance/registration/WOF/COF as applicable
- purchase price and market evidence
- insurance
- warranty
- import history where relevant

## Stage 6 — Compliance gate

Run policy checks and escalate exceptions. No settlement is available while a mandatory control is unresolved.

## Stage 7 — Family approval

Require the configured authorised approver(s). The decision record includes rationale, evidence and policy version.

## Stage 8 — Settlement

Sandbox only. Real payment execution requires separately authorised payment infrastructure and appropriate controls.

## Stage 9 — Registration and asset register

Record the NZTA registered-person workflow separately from legal ownership. The NZTA Motor Vehicle Register does not itself establish legal ownership.

## Stage 10 — Lifecycle monitoring

Track insurance, maintenance, registration, valuation, portfolio concentration, custody/location, provenance and eventual disposition.
