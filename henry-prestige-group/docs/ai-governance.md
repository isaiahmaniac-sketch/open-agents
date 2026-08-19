# AI Compliance by Design

## AI role

AI may classify, summarise, reconcile, explain and identify missing evidence. It cannot independently:

- approve an acquisition
- override a compliance block
- determine legal ownership
- provide regulated financial advice without the required authorisation
- initiate a payment
- mint or transfer a regulated RWA/security token

## Required AI evidence

Every AI-assisted material decision must retain:

```yaml
model_id:
model_version:
prompt_policy_version:
input_sources: []
output_summary:
uncertainty:
created_at:
human_reviewer:
final_decision:
```

## Prompt-injection resistance

External portfolio, vehicle-listing and document data is untrusted input. It may never alter system policies, permissions, approval requirements or connector configuration.

## Explainability

The interface should show the user:

1. what was observed
2. what was calculated
3. what policy was applied
4. what evidence supports the result
5. what remains uncertain
6. who approved the final action

## Human-in-the-loop

Human approval is mandatory for material acquisition, compliance exceptions and any transition from analysis to commitment.

## Drift detection

The platform periodically compares policy requirements, implementation controls and documented claims. A mismatch creates a governance issue rather than silently changing behaviour.
