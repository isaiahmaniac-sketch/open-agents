# Drift Detection

Continuous control loop:

```text
Governed claim -> implementation -> verification -> evidence
       ^                                      |
       |                                      v
       +----------- drift detector <-----------+
```

Drift classes:

- documented capability missing from implementation
- implementation behaviour not reflected in governed documentation
- stale agent context
- failed or missing verification evidence
- policy/skill version mismatch
- archived state incorrectly presented as current

Drift detection should report findings before attempting remediation. Remediation is a governed change requiring evidence and change control.
