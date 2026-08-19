# Open-Source Security Standard

The code may be open source while operational data remains private.

## Public repository may contain

- source code
- architecture
- schemas without real PII
- policy templates
- synthetic demo data
- tests
- threat models
- documentation

## Never commit

- private keys
- API tokens
- bank credentials
- portfolio credentials
- identity documents
- real source-of-funds evidence
- family member PII
- real account numbers
- production customer data

## Security baseline

- least privilege
- deny-by-default access
- MFA for operators
- secrets manager rather than repository secrets in code
- encryption in transit and at rest
- append-only audit trail
- dependency scanning
- SBOM generation
- signed releases where practical
- reproducible CI checks
- branch protection and required reviews
- security disclosure process

## NZ operational restriction

Application-level controls must be backed by infrastructure-level controls. A UI checkbox saying `NZ_ONLY` is insufficient. Production must use network, identity, hosting-region and data-store controls to enforce the jurisdiction boundary.

## Demo mode

All external integrations are disabled until explicitly configured. Demo mode uses synthetic accounts, vehicles, balances and identities.
