# Architecture

This platform is a self-managed cloud and Kubernetes operating model for production
applications, scheduled automation, GPU inference, and shared platform services. It was built
to be repeatable, observable, and recoverable, and to remove dependence on manual server
operations.

## Design Goals

- Provide a repeatable, reviewable deployment platform for production services and automation.
- Run a real, self-managed control plane with high availability rather than relying on a
  managed cluster service.
- Standardize cloud infrastructure with Terraform so changes are planned, reviewed, and audited.
- Make production health visible and make incidents recoverable.
- Keep least-privilege access and tenant isolation as first-class concerns.
- Reduce cost while keeping full operational control.

## Platform Layers

Six layers, from cloud foundation up to observability, with security cutting across all of them.

```mermaid
flowchart TB
    subgraph l1["Cloud Foundation"]
        direction TB
        c1["Multi-AZ VPC, subnets, security groups"]
        c2["EC2 compute, EBS, S3 object storage"]
        c3["Network Load Balancer, IAM roles"]
    end
    subgraph l2["Kubernetes Foundation"]
        direction TB
        k1["HA control plane (kubeadm 1.29) + etcd quorum"]
        k2["containerd runtime + Flannel CNI"]
        k3["Worker node pools, namespaces, RBAC"]
    end
    subgraph l3["Delivery"]
        direction TB
        d1["GitHub Actions self-hosted runners"]
        d2["Multi-arch image build + vulnerability scan"]
        d3["Private registry + kubectl rollout"]
    end
    subgraph l4["Runtime"]
        direction TB
        r1["Deployments and Services"]
        r2["Jobs and CronJobs (automation)"]
        r3["GPU inference (vLLM)"]
    end
    subgraph l5["Observability"]
        direction TB
        o1["Prometheus + Alertmanager"]
        o2["Grafana dashboards"]
        o3["Centralized logs (Seq) + runbooks"]
    end
    subgraph l6["Security and Governance (cross-cutting)"]
        direction TB
        s1["IAM least-privilege, RBAC, NetworkPolicy, image scanning"]
    end

    l1 --> l2
    l2 --> l3
    l3 --> l4
    l4 --> l5
    l6 -.governs.-> l1
    l6 -.governs.-> l3
    l6 -.governs.-> l5

    classDef cloud fill:#1a73e8,stroke:#0b3d91,color:#ffffff;
    classDef k8s fill:#f59e0b,stroke:#b45309,color:#1a1a1a;
    classDef del fill:#9334e6,stroke:#6b21a8,color:#ffffff;
    classDef run fill:#34a853,stroke:#1e7e34,color:#ffffff;
    classDef obs fill:#0097a7,stroke:#006064,color:#ffffff;
    classDef sec fill:#d93025,stroke:#a50e0e,color:#ffffff;

    class c1,c2,c3 cloud;
    class k1,k2,k3 k8s;
    class d1,d2,d3 del;
    class r1,r2,r3 run;
    class o1,o2,o3 obs;
    class s1 sec;
```

| Layer | Responsibility |
|-------|----------------|
| Cloud foundation | Compute, network, object storage, load balancing, IAM, and environment boundaries. |
| Kubernetes foundation | Control-plane HA, etcd, runtime, CNI, worker capacity, namespaces, RBAC, scheduling. |
| Delivery | Self-hosted CI/CD, image build and scan, registry, controlled rollout. |
| Runtime | Deployments, Services, Jobs, CronJobs, and GPU inference workloads. |
| Observability | Metrics, dashboards, alerts, logs, incident review, runbooks. |
| Security | IAM least-privilege, RBAC, network policy, secrets hygiene, scanning, audit evidence. |

## High-Availability Cluster Topology

The control plane runs three nodes across two Availability Zones with a 3-member etcd quorum,
fronted by an AWS Network Load Balancer for a single, highly available API endpoint. The quorum
tolerates the loss of one control-plane node; failover has been tested.

```mermaid
flowchart TB
    subgraph ingress["API Access - HA"]
        direction TB
        api["kubectl and API clients"]
        nlb["AWS Network Load Balancer - TCP 6443"]
        api --> nlb
    end

    subgraph cplane["Control Plane - multi-AZ, HA"]
        direction TB
        cp1["control-plane-1 (AZ-a)"]
        cp2["control-plane-2 (AZ-a)"]
        cp3["control-plane-3 (AZ-c)"]
        eq["etcd quorum - 3 members, tolerates 1 loss"]
        cp1 --- eq
        cp2 --- eq
        cp3 --- eq
    end

    subgraph wpools["Worker Node Pools"]
        direction TB
        wrpa["RPA pool - Linux CPU"]
        wwin["Windows Server node"]
        wgpu["GPU node - NVIDIA L40S 48GB"]
        warm["ARM64 edge node - on-prem"]
    end

    ingress -->|"load-balanced apiserver"| cplane
    cplane -->|"schedules pods"| wpools

    classDef lb fill:#1a73e8,stroke:#0b3d91,color:#ffffff;
    classDef ctl fill:#f59e0b,stroke:#b45309,color:#1a1a1a;
    classDef etcd fill:#b45309,stroke:#7c2d12,color:#ffffff;
    classDef wrk fill:#34a853,stroke:#1e7e34,color:#ffffff;

    class api,nlb lb;
    class cp1,cp2,cp3 ctl;
    class eq etcd;
    class wrpa,wwin,wgpu,warm wrk;
```

## Multi-AZ Network Model

Public subnets carry only edge entry points and per-AZ NAT egress. Control-plane and worker
nodes live in private subnets spread across two Availability Zones. No node is directly
reachable from the public internet.

```mermaid
flowchart TB
    subgraph net0["Public Internet"]
        direction TB
        ext["External clients (HTTPS / WSS)"]
    end

    subgraph vpc["AWS VPC - multi-AZ, private address space"]
        direction TB
        subgraph public["Public Subnets"]
            direction TB
            elb["Edge load balancer - TLS termination"]
            nat["NAT gateways - per-AZ egress"]
        end
        subgraph aza["Private Subnet - Availability Zone A"]
            direction TB
            a_cp["control-plane-1, control-plane-2"]
            a_wk["workers: RPA, GPU, dashboard"]
        end
        subgraph azc["Private Subnet - Availability Zone C"]
            direction TB
            c_cp["control-plane-3"]
            c_wk["worker: RPA"]
        end
    end

    net0 --> public
    public --> aza
    public --> azc

    classDef extc fill:#455a64,stroke:#263238,color:#ffffff;
    classDef pub fill:#1a73e8,stroke:#0b3d91,color:#ffffff;
    classDef priv fill:#34a853,stroke:#1e7e34,color:#ffffff;

    class ext extc;
    class elb,nat pub;
    class a_cp,a_wk,c_cp,c_wk priv;
```

## Workload Types

| Workload type | Description |
|---------------|-------------|
| Web and platform services | Containerized services deployed through controlled rollouts with health checks. |
| Automation jobs | Scheduled browser and data automation running as CronJobs, one task per node. |
| GPU inference | LLM serving on a dedicated GPU node with an OpenAI-compatible API. |
| Shared platform services | Observability, registry, and operational tooling supporting the rest of the platform. |
