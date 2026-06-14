# AI-Assisted Delivery Approval Boundary

This example describes a public-safe control boundary for AI-assisted software delivery. It is a portfolio artifact, not a production policy engine.

## Allowed Without Human Approval

- Summarize logs, metrics, and pull request context.
- Draft runbook updates using sanitized incident notes.
- Suggest Kubernetes, Terraform, or CI/CD changes in a branch.
- Generate test cases or policy checks for reviewer approval.

## Requires Human Approval

- Merging production-impacting code.
- Changing Terraform resources.
- Changing Kubernetes manifests that affect runtime permissions, network exposure, or scaling.
- Accepting vulnerability risk.
- Updating secrets, identity, or deployment credentials.
- Disabling alerts, scans, admission controls, or rollback checks.

## Never Allowed For An Agent

- Access production credentials directly.
- Run `kubectl` against production without an approved human-controlled session.
- Apply Terraform to production.
- Bypass CI/CD gates.
- Override an active security exception without owner approval.

## Audit Evidence

- Prompt or task summary.
- Generated diff or command plan.
- Reviewer decision and timestamp.
- Policy checks and scan results.
- Deployment event, image digest, and rollback reference.
