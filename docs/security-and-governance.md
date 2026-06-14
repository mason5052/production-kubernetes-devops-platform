# Security And Governance

The security model focused on practical controls that improve production safety without blocking engineering velocity.

## Control Areas

| Area | Public-safe implementation summary |
|------|------------------------------------|
| IAM | Reduced broad cloud permissions and moved toward scoped, least-privilege policies. |
| Kubernetes RBAC | Used role-based access patterns to limit who and what could change cluster resources. |
| Vulnerability management | Supported remediation through image scanning, dependency visibility, and prioritized fixes. |
| CI/CD guardrails | Added build, validation, scan, and rollout checks before production deployment. |
| WAF and edge security | Tuned web application firewall controls to reduce malicious traffic exposure. |
| Audit support | Improved evidence retrieval for infrastructure, deployment, access, and operational controls. |
| Secrets hygiene | Avoided committing secrets and excluded sensitive files from public and source-controlled artifacts. |

## IAM Hardening Pattern

The public-safe IAM hardening pattern is:

1. Identify broad managed policies and broad inline permissions.
2. Map required actions to real platform responsibilities.
3. Separate infrastructure roles by workload category where possible.
4. Scope permissions by tags, resource prefixes, and read-only discovery needs.
5. Validate that unrelated resource actions are denied.
6. Keep operational permissions for monitoring and managed instance access where needed.

## Kubernetes Security Pattern

The public-safe Kubernetes security pattern is:

- Use namespaces to separate workload ownership.
- Apply RBAC for operational boundaries.
- Use readiness and liveness checks for safer rollouts.
- Use network policy where service-to-service boundaries are required.
- Use image scanning before deployment.
- Keep secrets out of manifests and repositories.

## WAF And Threat Reduction

Production security work included AWS WAF and related security improvements that reduced malicious traffic exposure by more than 90% at a public-safe summary level.

## Governance Outcomes

- Faster audit response through standardized infrastructure and deployment evidence.
- Clearer ownership boundaries for cloud and Kubernetes changes.
- Better vulnerability remediation support through scanning and operational tracking.
- Safer CI/CD releases through repeatable gates and rollout checks.

