# Observability

The observability model was designed to make production health visible across cloud infrastructure, Kubernetes workloads, application behavior, and incident response workflows.

## Goals

- Detect service degradation before users report it.
- Reduce time to identify the failing layer.
- Provide dashboards for platform, workload, and deployment health.
- Route actionable alerts without creating excessive noise.
- Preserve enough evidence for incident review and audit support.

## Signals

| Signal | Example use |
|--------|-------------|
| Availability | Service up/down status, endpoint checks, and rollout health. |
| Latency | Request duration, slow dependency behavior, and user-facing performance. |
| Errors | Application error rate, failed jobs, crash loops, and failed deployments. |
| Saturation | CPU, memory, disk, pod capacity, node pressure, and queue depth. |
| Deployment health | Rollout status, restart count, image version, and failed readiness checks. |
| Security events | WAF activity, vulnerability remediation evidence, and suspicious traffic trends. |

## Monitoring Stack

| Component | Responsibility |
|-----------|----------------|
| Prometheus | Metrics collection and alert rule evaluation. |
| Grafana | Dashboards for workload, cluster, and service health. |
| Alertmanager | Alert grouping, routing, and escalation support. |
| CloudWatch | Cloud infrastructure telemetry and operational visibility. |
| Centralized logs | Application and platform log review during incident investigation. |

## Alert Design

Alerts should be actionable. A good alert includes:

- The affected service or workload class
- The failing signal
- Severity
- Suggested first checks
- Dashboard link or query reference
- Runbook reference

## Operational Improvements

Production outcomes:

- Improved incident visibility by connecting Kubernetes health, application signals, and cloud telemetry.
- Reduced response time by standardizing dashboards, alerts, and runbooks.
- Improved post-incident analysis by preserving deployment, log, and metric context.

## Example

See `examples/monitoring/prometheus-rule.yaml` for an alert rule example.

