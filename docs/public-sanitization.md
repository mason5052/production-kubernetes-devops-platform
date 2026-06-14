# Public Sanitization Notes

This repository is based on real production DevOps and platform engineering work, but every artifact has been rewritten for public release.

## Removed From Public Version

- Real employer, customer, product, and project names
- Real domains, DNS records, IP addresses, VPN details, subnet ranges, instance IDs, and account identifiers
- Private repository URLs and private registry URLs
- Secrets, tokens, SSH keys, kubeconfigs, access key exports, Terraform state, and variable files
- Internal application manifests, dashboards, alert channels, and incident records
- Any operational detail that could reveal attack surface or private infrastructure design

## Preserved In Public Version

- High-level architecture patterns
- Technology choices
- Operating responsibilities
- Sanitized CI/CD flow
- Sanitized Kubernetes deployment patterns
- Sanitized Terraform module patterns
- Monitoring and alerting model
- Security and governance practices
- Public-safe business outcomes

## Intended Audience

The intended reader is a hiring manager, recruiter, DevOps lead, platform engineering manager, security engineering manager, or SRE interviewer who wants to understand the type of production systems I have built and operated.

This repository is not intended to be a drop-in infrastructure template.

