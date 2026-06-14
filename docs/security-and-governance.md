# Security And Governance

The security model focused on practical controls that improve production safety without blocking engineering velocity.

## Control Areas

| Area | Implementation summary |
|------|------------------------------------|
| IAM | Reduced broad cloud permissions and moved toward scoped, least-privilege policies. |
| Kubernetes RBAC | Used role-based access patterns to limit who and what could change cluster resources. |
| Vulnerability management | Supported remediation through image scanning, dependency visibility, and prioritized fixes. |
| CI/CD guardrails | Added build, validation, scan, and rollout checks before production deployment. |
| WAF and edge security | Tuned web application firewall controls to reduce malicious traffic exposure. |
| Audit support | Improved evidence retrieval for infrastructure, deployment, access, and operational controls. |
| Secrets hygiene | Avoided committing secrets and excluded sensitive files from public and source-controlled artifacts. |
| Change control | Connected source review, rollout evidence, rollback paths, and risk decisions. |
| Policy-as-code | Used repeatable policy patterns to reduce manual review drift across Kubernetes and CI/CD. |
| AI SDLC guardrails | Kept AI-assisted delivery bounded by approval, audit logging, and tool access controls. |

## IAM Hardening Pattern

The IAM hardening pattern is:

1. Identify broad managed policies and broad inline permissions.
2. Map required actions to real platform responsibilities.
3. Separate infrastructure roles by workload category where possible.
4. Scope permissions by tags, resource prefixes, and read-only discovery needs.
5. Validate that unrelated resource actions are denied.
6. Keep operational permissions for monitoring and managed instance access where needed.

## Kubernetes Security Pattern

The Kubernetes security pattern is:

- Use namespaces to separate workload ownership.
- Apply RBAC for operational boundaries.
- Use readiness and liveness checks for safer rollouts.
- Use network policy where service-to-service boundaries are required.
- Use image scanning before deployment.
- Keep secrets out of manifests and repositories.
- Require labels, probes, resource requests, and non-privileged runtime defaults through admission policy where possible.
- Treat exceptions as temporary risk decisions with owner, reason, expiration, and evidence.

## Vulnerability Management Pattern

The market analysis showed vulnerability management as one of the strongest DevSecOps signals. The operating pattern is:

1. Collect findings from image, dependency, IaC, and configuration scans.
2. Normalize severity, affected component, fixed version, exploitability, and workload exposure.
3. Prioritize internet-facing, privileged, regulated, or high-blast-radius workloads first.
4. Deduplicate repeated findings so teams see one actionable remediation path.
5. Track accepted risk with an owner, expiration date, and compensating controls.
6. Preserve remediation evidence for audit and post-incident review.

See `examples/vulnerability-triage/` for a small sample input and output pattern.

## Change Control And Risk Acceptance

The platform model treats change control as an engineering workflow, not a separate paperwork step.

| Control | Evidence to retain |
|---------|--------------------|
| Source review | Pull request, reviewer, scope, test signal, and approval context. |
| Infrastructure change | Terraform plan, affected resources, rollback or mitigation path, and change window. |
| Application release | Image digest, deployment event, rollout result, and post-deploy health. |
| Security exception | Finding, reason, owner, expiration, compensating control, and revalidation date. |
| Incident follow-up | Timeline, impact, mitigation, root cause, and prevention work item. |

## Policy-As-Code Direction

Manual review does not scale across many teams and workloads. The public examples show how platform rules can become executable controls:

- Admission policies for required metadata, non-privileged pods, probes, and resource controls.
- CI/CD checks that block obvious policy violations before a deployment reaches the cluster.
- Terraform guardrails that make least privilege and tagging reviewable.
- Exception records that keep velocity while making risk visible.

## WAF And Threat Reduction

Production security work included AWS WAF and related security improvements that reduced malicious traffic exposure by more than 90%.

## AI-Assisted Delivery Governance

AI-assisted development changes delivery speed, but it does not remove the need for control. The platform pattern is:

- Human approval for production-impacting changes.
- Tool and secret boundaries for agents and automation.
- Audit logging for prompts, generated changes, reviewer decisions, and deployment actions.
- Policy checks before generated manifests, Terraform, or scripts are merged.
- Explicit rollback and incident response paths for AI-assisted changes.

## Governance Outcomes

- Faster audit response through standardized infrastructure and deployment evidence.
- Clearer ownership boundaries for cloud and Kubernetes changes.
- Better vulnerability remediation support through scanning and operational tracking.
- Safer CI/CD releases through repeatable gates and rollout checks.
- Better public proof of cloud security, platform security, and DevSecOps ownership.

