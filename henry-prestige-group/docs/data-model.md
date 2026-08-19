# Canonical Data Model

## Family

- family_id
- governance_policy_id
- jurisdiction = NZ
- authorised_roles

## Person / Entity

- subject_id
- type: individual | company | trust | partnership
- identity_status
- beneficial_ownership_status
- risk_rating

## Portfolio Account

- account_id
- provider
- account_type
- jurisdiction
- currency
- as_of
- connector_status
- reconciliation_status

## Position

- position_id
- account_id
- instrument_id
- quantity
- valuation
- currency
- source_timestamp
- data_confidence

## Acquisition

- acquisition_id
- target_asset_id
- acquiring_subject_id
- intended_use
- price
- currency
- funding_source_ids
- liquidity_snapshot_id
- compliance_case_id
- approval_state
- settlement_state

## Vehicle Asset

- VIN
- make
- model
- variant
- build_year
- registration_status
- registered_person
- provenance
- security_interest_status
- insurance_status
- warranty_status

## Evidence

- evidence_id
- evidence_type
- source
- hash
- collected_at
- collector
- policy_version
- verification_status

## Decision

- decision_id
- subject
- actor
- action
- rationale
- evidence_ids
- policy_version
- ai_assist_metadata
- human_approval
- timestamp
