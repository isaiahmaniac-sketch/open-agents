# New Zealand Gold-Standard Compliance Baseline

> This is an engineering control baseline, not legal advice. Production deployment requires confirmation by New Zealand legal/compliance professionals and the applicable regulators.

## 1. Motor vehicle trading

If HPG conducts business as a motor vehicle trader, the implementation must support Motor Vehicle Traders Register requirements and NZTA transaction controls. The system must record trader status, vehicle identity, seller/buyer identity, acquisition and disposal events, and required transaction evidence.

## 2. AML/CFT

High-value vehicle activity must be assessed against the AML/CFT Act 2009 and current DIA guidance. The control plane therefore supports:

- customer and beneficial-owner identification
- risk rating
- enhanced due diligence escalation
- source-of-funds / source-of-wealth evidence
- transaction monitoring
- suspicious activity escalation
- prohibited cash transaction controls
- record retention
- compliance-officer review
- regulator/reporting workflow placeholders

**Hard control:** the sandbox must reject cash settlement paths at or above the statutory prohibited threshold for specified high-value goods and must not permit transaction splitting to evade a threshold.

## 3. Privacy

The platform adopts the Privacy Act 2020 principles, including IPP 3A for indirect collection and IPP 12 for overseas disclosure. Personal information is minimised, purpose-bound, encrypted, access-controlled and auditable.

A connector cannot be enabled merely because an API exists. It requires a data-residency and privacy assessment first.

## 4. Financial advice boundary

Portfolio aggregation may provide factual information and calculations in the sandbox. It must not present personalised recommendations concerning regulated financial products unless the appropriate New Zealand Financial Advice Provider/licensing structure exists.

The UI must clearly distinguish:

- factual portfolio data
- arithmetic / scenario analysis
- acquisition workflow decisions
- regulated financial advice

## 5. RWA boundary

RWA functionality is modelled as a future legal/technical boundary. A token representing a vehicle, equity, debt, beneficial interest or other financial right must not be minted, marketed, transferred or traded by this sandbox.

The demo may model provenance and entitlement records without representing them as legally effective ownership or securities.

## 6. AI governance

AI is an assistant, not the legal decision-maker. Every material compliance conclusion must have:

- source evidence
- policy version
- model/version identifier
- timestamp
- confidence/uncertainty
- human reviewer where required
- final disposition

AI must not override a compliance block.

## 7. Fail-closed rules

`UNKNOWN → REVIEW`

`CONFLICT → REVIEW`

`MISSING EVIDENCE → BLOCK`

`JURISDICTION NOT NZ → BLOCK`

`REGULATED ACTIVITY WITHOUT LICENCE/APPROVAL → BLOCK`

`SANCTIONS/AML ALERT → BLOCK + ESCALATE`

`PRIVACY RESIDENCY UNRESOLVED → BLOCK CONNECTOR`
