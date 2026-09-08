# Henry APEX — Coinbase ↔ Links Connect

## Status: HOLD / READ + PREPARE ONLY

This integration is intentionally **not production-enabled**. It provides a governed NZ-only boundary for Coinbase data while preventing the adapter from executing transfers.

### Architecture

- **Coinbase / AgentKit:** provider capability and wallet data.
- **Links Connect:** integration/data-fabric boundary when a supported live connector is available.
- **Henry APEX:** authority, deterministic policy, orchestration, provenance, audit and human oversight.
- **Portfolio Dividend Tracker / wlthy / CloFin:** remain separate systems of record/intelligence; no blind duplication.

### Non-negotiable controls

1. NZ-only operating jurisdiction.
2. Read is the default authority.
3. `prepare_native_transfer` creates an intent only; it cannot move funds.
4. There is no live transfer method in this adapter.
5. Human approval must be a structured approval bound to the exact request before any future execution capability is considered.
6. Future execution requires a persistent idempotency/execution ledger, deterministic policy outside the model, destination/network validation, transaction simulation, emergency stop, audit evidence and post-execution verification.
7. Provider responses are reduced to allowlisted projections; raw responses are not propagated by default.
8. Secrets remain in runtime secret management and never in source control.
9. Missing compliance evidence fails closed to review/deny.
10. Production promotion requires human acceptance and explicit production approval.

### NZ privacy-by-design

Where personal information is involved, APEX must assess the Privacy Act 2020 requirements and complete the required privacy assessment before use. Indirect collection must trigger an IPP3A applicability/notification assessment. The Office of the Privacy Commissioner recommends a Privacy Impact Assessment before using AI with personal information and regular updates thereafter.

### Activation

Do not activate live transaction execution from this repository. Any future capability must be introduced through the central APEX execution firewall and pass security, compliance, testing and human-approval gates first.
