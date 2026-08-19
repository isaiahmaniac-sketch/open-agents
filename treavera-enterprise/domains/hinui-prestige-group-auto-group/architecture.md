# Architecture

```text
Family Governance
       |
       v
Authorization & Policy
       |
       +-------------------+
       |                   |
       v                   v
Asset Acquisition     Treasury Interface
       |
       v
Ownership / SPV / Custody Records
       |
       v
Vehicle Asset Registry
       |
 +-----+------+----------------+
 |            |                |
 v            v                v
Utilization  Maintenance     Compliance
 |            |                |
 +------------+----------------+
              |
              v
        Valuation / Exit
              |
       +------+------+
       |             |
       v             v
    Resale      Family Transfer
```

## Core services

### Family Governance

Maintains family-level roles, mandates, authorization thresholds, delegated authorities and succession/estate workflow references.

### Asset Acquisition

Handles sourcing, due diligence, acquisition proposals, purchase method analysis, settlement readiness and acquisition approval.

### Ownership & Custody

Separates registered owner, beneficial owner, custodian, operating entity and allocated family user. Supports entity/SPV references without assuming a particular legal structure.

### Vehicle Asset Registry

Canonical record for VIN/chassis identity, specification, provenance, purchase price, valuation, location, status and lifecycle events.

### Utilization

Controls family allocation, bookings, driver/user authorization, mileage, operating expenses and return/custody events.

### Maintenance & Warranty

Tracks scheduled servicing, repairs, tyres, inspections, warranty claims and manufacturer/dealer records.

### Treasury Interface

Provides approved funding requests and asset-level cash-flow information to the Treavera Treasury Agent. It does not bypass treasury policy or authorization controls.

### Compliance & Evidence

Captures source-of-funds evidence, KYC/AML requirements where applicable, title/registration records, insurance, approvals, invoices and material decisions.

### Exit & Transfer

Supports valuation, resale, trade-in, inter-entity transfer, family transfer and estate workflows subject to the applicable legal/tax structure.
