# Portfolio Roadmap

This roadmap separates what this repository already covers from what is intentionally tracked as future engineering work.

## Complete Now

| Production area | Current artifact |
|-----------------|------------------|
| Production Kubernetes operating model | `README.md`, `docs/architecture.md`, `examples/kubernetes/` |
| CI/CD with validation and scan gates | `docs/cicd.md`, `examples/github-actions/ci-cd.yml` |
| GitOps-style delivery | `examples/argocd/application.yaml` |
| Observability and incident response | `docs/observability.md`, `examples/monitoring/prometheus-rule.yaml` |
| Terraform-based cloud foundation | `examples/terraform/` |
| Security and governance narrative | `docs/security-and-governance.md` |
| Policy-as-code guardrails with tests | `examples/policy-as-code/` (Kyverno policies plus `kyverno test` coverage) |

## 2026 Portfolio Evidence

Goal: make cloud and platform security ownership visible, not only DevOps execution.

Tracked work:

- Add Terraform IAM least-privilege guardrail examples.
- Build secure CI supply chain template with SBOM and signing.

Completed: production-grade Kyverno policy test coverage (`examples/policy-as-code/`).

## 2027 Security Automation

Goal: show that security automation can be designed as a reusable platform capability.

Tracked work:

- Add vulnerability triage automation with risk scoring.
- Add audit evidence bundle generator example.
- Add cloud security posture checklist mapped to CNAPP/CSPM concepts.
- Add secrets management pattern with rotation and CI/CD boundaries.
- Add Kubernetes platform threat model.
- Add GitOps promotion and rollback evidence flow.
- Add incident/on-call runbook library.
- Add SLO and dashboard examples for platform reliability.

## 2028 Platform Security Architecture

Goal: move from implementation evidence to architecture judgment.

Tracked work:

- Add SOC 2, PCI, or HIPAA-style generic control mapping.
- Add secure AI-assisted SDLC reference architecture.
- Add LLM/tool boundary policy examples.
- Add architecture decision records for security tradeoffs.
- Add commerce abuse defense operational write-up from WAF and bot-defense work.

## 2029 Staff-Level Ownership

Goal: document governance, metrics, and multi-team platform ownership.

Tracked work:

- Add platform governance metrics model.
- Add validation workflow for YAML, Terraform, Markdown, and examples.

## 2030-2031 Leverage Track

Goal: grow the repository into a reusable production engineering reference.

Possible directions:

- Package the guardrail examples as a reusable starter kit.
- Publish architecture decision records as writing samples.
- Add talks, diagrams, and release notes if the repo begins receiving external attention.
- Keep the repo focused on cloud security, platform security, DevSecOps, and AI SDLC governance work.

## Maintenance Rule

Each new artifact should answer three questions:

1. What production responsibility does this cover?
2. What engineering judgment does it make visible?
3. How does it stay focused on DevOps platform work?
