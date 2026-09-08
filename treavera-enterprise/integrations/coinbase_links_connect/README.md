# Henry APEX — Coinbase ↔ Links Connect Adapter

This module defines the governed integration boundary between Henry APEX, Links Connect, and Coinbase Developer Platform / AgentKit.

## Responsibility

- **Links Connect:** integration/data-fabric boundary.
- **Coinbase CDP / AgentKit:** wallet and onchain capabilities.
- **Henry APEX:** authority, policy, orchestration, provenance, audit.
- **Portfolio Dividend Tracker / wlthy / CloFin:** remain separate systems of record/intelligence; no blind duplication.

## Current state

The connected Links Connect connector available to the runtime currently exposes Stripe and HubSpot resources, not Coinbase. Therefore this implementation adds the Coinbase adapter contract and governed execution boundary without pretending that a live Coinbase account is connected.

## Security model

1. Read operations are the default.
2. Transactional actions require an explicit APEX policy decision.
3. High-risk actions require human approval.
4. Secrets are supplied only through runtime secret management.
5. Every action receives an idempotency key and produces an audit record.
6. No private key or Coinbase credential is stored in Links Connect records or source control.

## Coinbase alignment

AgentKit supports wallet management, onchain actions, multiple networks, and custom action providers. The adapter is intentionally provider-neutral at the APEX boundary so AgentKit can be upgraded independently of the integration fabric.

## Activation requirements

Set CDP credentials in the deployment secret store and wire the adapter to the live Coinbase AgentKit runtime. Do not commit credentials.
