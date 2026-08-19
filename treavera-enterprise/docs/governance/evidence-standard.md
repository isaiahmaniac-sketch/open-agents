# Evidence Standard

Every governed conclusion should expose enough evidence for another engineer or agent to reproduce the reasoning.

## Evidence record

```yaml
id: evidence-<timestamp>-<slug>
subject: <claim-or-decision>
implementation:
  commit: <sha>
  files: []
verification:
  tests: []
  results: []
change_control:
  issue: <number>
  pull_request: <number>
  decision_record: <path>
status: verified | failed | superseded
```

Evidence is immutable in meaning: corrections create a new record and reference the superseded record.
