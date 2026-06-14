# Security Policy

This repository is a public portfolio artifact for production DevOps and platform engineering experience.

## Public-Safe Boundary

The repository must not include:

- Employer source code
- Internal project names
- Customer or employee data
- Hostnames, domains, IP addresses, VPC IDs, subnet IDs, account IDs, AMI IDs, or instance IDs
- Credentials, tokens, access keys, private keys, SSH keys, kubeconfigs, or Terraform state
- Internal dashboards, alert routes, runbook links, Jira links, Slack channels, or service ownership data

## Example Data

All examples use placeholders such as:

- `example-org`
- `example.com`
- `registry.example.internal`
- `platform-service`
- `us-east-1`

These are not real production identifiers.

Example files are design patterns and portfolio evidence. They are not hardened production baselines and should not be copied into a live environment without threat modeling, testing, access review, and organization-specific policy review.

## Reporting Issues

If a sensitive value is ever found in this repository, remove it immediately, rotate the affected credential if applicable, and rewrite history before publishing or republishing.

