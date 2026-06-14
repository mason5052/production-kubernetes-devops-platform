# Policy-as-Code Guardrails

Kyverno `ClusterPolicy` examples that enforce a small, opinionated platform baseline on
Kubernetes workloads, plus executable tests that prove each policy passes compliant
workloads and blocks non-compliant ones.

These are portfolio examples, not a hardened production baseline. Adapt the label keys,
severities, and `validationFailureAction` values to your own platform before use.

## Policies

| File | Policy | Action | What it enforces |
|------|--------|--------|------------------|
| `required-metadata-policy.yaml` | `require-platform-metadata` | Enforce | Every Pod must carry `owner`, `service`, and `data-classification` platform labels so ownership and data sensitivity are always attributable. |
| `require-probes-and-resources.yaml` | `require-probes-and-resources` | Audit | Containers must define readiness and liveness probes (with `periodSeconds`) and CPU and memory requests so rollout health and scheduling are predictable. |
| `disallow-privileged-pods.yaml` | `disallow-privileged-pods` | Enforce | Containers (and init containers, if present) must not run privileged, removing a common container-escape path. |

`kustomization.yaml` assembles the three policies for a single `kubectl apply -k .` rollout.

## Tests

`tests/kyverno-test.yaml` runs all three policies against four fixtures and asserts the
expected pass/fail outcome for each policy-resource pair (12 assertions total):

| Fixture | metadata | probes/resources | privileged |
|---------|----------|------------------|------------|
| `good-pod` | pass | pass | pass |
| `privileged-pod` | pass | pass | fail |
| `missing-metadata-pod` | fail | pass | pass |
| `missing-probes-pod` | pass | fail | pass |

### Run the tests

Install the Kyverno CLI (see the
[Kyverno CLI install guide](https://kyverno.io/docs/kyverno-cli/install/)), then from the
repository root:

```bash
kyverno test examples/policy-as-code/tests
```

Expected output:

```
Test Summary: 12 tests passed and 0 tests failed
```

Run this command locally, or wire it into CI, to keep the policies verifiably correct.
