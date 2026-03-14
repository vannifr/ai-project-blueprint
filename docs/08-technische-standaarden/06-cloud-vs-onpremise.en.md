---
versie: '1.0'
pdf: false
type: technical
layer: 3
roles: [Tech Lead]
---

# Cloud vs. On-Premise

Decision framework for choosing between cloud deployment, on-premise infrastructure or a hybrid approach. Use this during the **Discovery & Strategy** phase before architectural choices are locked in.

______________________________________________________________________

## 1. Decision Matrix

Score each criterion based on your situation: **C** = advantage for Cloud, **O** = advantage for On-Premise, **=** = neutral.

| Criterion                                                                        | Weight | Your situation | Direction |
| :------------------------------------------------------------------------------- | :----- | :------------- | :-------- |
| **Data sovereignty** — data must remain in NL/EU                                 | High   |                | C / O     |
| **Scalability** — volumes vary significantly or are unknown                      | High   |                | C / O     |
| **Time-to-market** — quick prototype or pilot needed                             | High   |                | C / O     |
| **Cost certainty** — predictable monthly costs required                          | High   |                | C / O     |
| **Compliance** — sector regulation requires full control                         | High   |                | C / O     |
| **Latency** — real-time processing with \< 100 ms required                       | Medium |                | C / O     |
| **Existing infrastructure** — significant on-prem investment present             | Medium |                | C / O     |
| **Maintenance capacity** — internal team for infrastructure management available | Medium |                | C / O     |

### Interpretation

- **Predominantly C:** cloud-first approach recommended
- **Predominantly O:** on-premise or private cloud recommended
- **Mixed:** consider hybrid architecture

______________________________________________________________________

## 2. Decision Tree (5 questions)

```
1. Does the system process special categories of personal data (health, biometrics)?
   YES → On-premise or private cloud strongly recommended
   NO  → go to 2

2. Is the expected load unpredictable or seasonal (10× variation)?
   YES → Cloud recommended (elastic scalability)
   NO  → go to 3

3. Does the organisation have < 2 FTE available for infrastructure management?
   YES → Cloud recommended (managed services)
   NO  → go to 4

4. Does the sector require full audit control over hardware and data location?
   YES → On-premise or private cloud required
   NO  → go to 5

5. Is time-to-market < 3 months for a working system?
   YES → Cloud recommended
   NO  → both options comparable; base on TCO
```

______________________________________________________________________

## 3. Cloud Deployment

### Providers — Comparison

| Aspect                | AWS                     | Azure                 | GCP                  |
| :-------------------- | :---------------------- | :-------------------- | :------------------- |
| **LLM/AI services**   | Bedrock (Claude, Llama) | Azure OpenAI, Copilot | Vertex AI (Gemini)   |
| **EU data residency** | Frankfurt, Ireland      | West/North Europe     | Belgium, Netherlands |
| **Compliance**        | ISO 27001, SOC 2        | ISO 27001, SOC 2      | ISO 27001, SOC 2     |
| **Min. costs (dev)**  | Pay-per-use             | Pay-per-use           | Pay-per-use          |
| **MLOps platform**    | SageMaker               | Azure ML              | Vertex AI            |

### Cloud Cost Management

Primary cost drivers in cloud AI deployments:

- **Inference APIs** — cost per token/request (largest variable cost for LLM applications)
- **Compute (GPU/CPU hours)** — for training and fine-tuning
- **Storage** — model artefacts, training data, vector databases
- **Network** — data transfer and egress costs

See [Cost Optimisation](07-kostenoptimalisatie.md) for reduction techniques (caching, model tiering, batch processing).

### Cloud Security Checklist

- [ ] Data residency configured to EU region
- [ ] Encryption at rest and in transit configured
- [ ] IAM with least-privilege configured
- [ ] VPC/private endpoint for sensitive services
- [ ] Secrets management (no credentials in code)
- [ ] Logging and audit trail active
- [ ] Budget alerts configured

______________________________________________________________________

## 4. On-Premise Deployment

### Infrastructure Requirements

| Component   | Minimum (pilot)          | Production                          |
| :---------- | :----------------------- | :---------------------------------- |
| **CPU**     | 16 cores                 | 32+ cores                           |
| **RAM**     | 64 GB                    | 256 GB+                             |
| **GPU**     | Optional (CPU inference) | NVIDIA A100 / H100 for large models |
| **Storage** | 2 TB NVMe                | 20+ TB RAID                         |
| **Network** | 1 Gbps                   | 10 Gbps                             |
| **OS**      | Ubuntu 22.04 LTS         | Ubuntu 22.04 LTS / RHEL             |

### Software Stack (open source options)

| Layer             | Option                     | Licence          |
| :---------------- | :------------------------- | :--------------- |
| **Model serving** | Ollama, vLLM, TGI          | MIT / Apache 2.0 |
| **Orchestration** | Kubernetes (k3s for small) | Apache 2.0       |
| **MLOps**         | MLflow, DVC                | Apache 2.0       |
| **Monitoring**    | Prometheus + Grafana       | Apache 2.0       |
| **Vector store**  | Qdrant, Weaviate, pgvector | Apache 2.0 / BSD |

### TCO Calculation (simplified)

```
CapEx (one-off):
  Hardware:            €_______
  Installation/setup:  €_______

OpEx (annual):
  Energy:              €_______ /year
  Maintenance/admin:   €_______ /year  (1–2 FTE × rate)
  Licences:            €_______ /year

Compare with Cloud:
  Expected cloud costs:  €_______ /year
  Break-even point:      _______ years
```

______________________________________________________________________

## 5. Hybrid Architecture

The most common hybrid patterns:

| Pattern                            | Description                                                         | When                                         |
| :--------------------------------- | :------------------------------------------------------------------ | :------------------------------------------- |
| **Dev cloud / Prod on-prem**       | Develop in cloud (flexible), run in production on-prem (control)    | Strict production requirements, flexible R&D |
| **Data on-prem / Inference cloud** | Raw data stays on-prem; anonymised/processed to cloud for inference | Data sovereignty + scalability               |
| **Multi-cloud**                    | Critical workloads on two providers                                 | Avoid vendor lock-in, high availability      |
| **Edge + cloud**                   | Real-time inference on-device; heavy processing in cloud            | IoT, low latency, limited connectivity       |

______________________________________________________________________

## 6. Recommendations by Organisation Profile

| Profile                          | Recommendation                                                                  |
| :------------------------------- | :------------------------------------------------------------------------------ |
| **Explorer** (first pilot)       | Cloud-first: managed LLM API + SaaS tooling. Minimal infrastructure investment. |
| **Builder** (production systems) | Hybrid: cloud for dev/test, on-prem or private cloud for production data.       |
| **Visionary** (portfolio)        | Multi-cloud + on-prem for critical systems. Own Platform Enablement team.       |

______________________________________________________________________

## Related Modules

- [Cost Optimisation](07-kostenoptimalisatie.md)
- [AI Architecture](05-ai-architectuur.md)
- [MLOps Standards](01-mloops-standaarden.md)
- [Data Pipelines](02-data-pipelines.md)
