---
versie: '1.1'
---

# 1. Core Activities & Roles (Monitoring & Optimisation)

## 1. Core Activities

### Operational Monitoring & MLOps

We monitor the 'heartbeat' of the system.

- **Real-time Performance Tracking:** Dashboarding of critical metrics: Latency (speed), Error rates, Uptime, Throughput.
- **Performance Degradation Monitoring:** Statistically monitoring whether production input data deviates from training data (*Data Drift*) or whether the relationship between data and outcomes changes (*Concept Drift*).
- **Data Loop Integration:** Feeding production data and outcomes back into the development environment for analysis (Feedback Loop).
- **Automated Triggers:** Setting alerts for drops below thresholds (e.g. accuracy \< 85%).

### Continuous Improvement & Retraining

Standing still means falling behind.

- **Retraining Strategy:** When do we retrain? (Periodically? On drift alert? On new data?).
- **Experiment Loops:** Use production insights to test new hypotheses in short sprints (A/B testing, Canary releases).
- **Backlog Management:** Maintain a living list of bugs, improvements and feature requests from users.

### Cost Control & Energy Efficiency

Sustainability in euros and CO2.

- **Cloud & API Optimisation (Cost Overview):** Monthly review of compute (GPU/CPU) and token costs. Optimise through model compression (*quantisation*) or caching.
- **Sustainability Measurement (ESG):** Monitoring energy consumption (*inference footprint*) and reporting for ESG goals.
- **Resource Allocation:** Set up autoscaling to adjust infrastructure to actual demand.

### Ethical Oversight & Compliance Monitoring

Ongoing legal conformity.

- **Post-Market Surveillance:** (EU AI Act requirement) Continuously scanning for unforeseen bias, discrimination or safety risks.
- **Audit-ready Logging:** Retaining logs of decisions and human interventions for auditors.
- **Transparency Reports:** Periodic reporting to stakeholders and CAIO on safety and performance.
- **Fairness Audit (Bias Audit):** Regular sampling by the Ethicist of the 'tone' and quality of outputs.

### Decommissioning

An AI system has a finite lifespan. Define in advance when shutdown is justified.

**Decommissioning triggers:**

| Category          | Trigger                                                                          | Action                                    |
| :---------------- | :------------------------------------------------------------------------------- | :---------------------------------------- |
| **Technical**     | Drift exceeds threshold and retraining does not improve performance              | System offline, root cause analysis       |
| **Economic**      | Cost per Productive Outcome rises > 50% above baseline after 2 quarters          | CAIO review: stop or re-architect         |
| **Ethical/Legal** | Critical fairness audit finding or new legislation renders system non-compliant  | Immediate stop, Guardian review mandatory |
| **Strategic**     | Use case disappears due to organisational change or better alternative available | Controlled wind-down per handover plan    |

**Decommissioning process:**

1. **Announcement:** Inform users and stakeholders in advance (minimum 4 weeks).
1. **Archiving:** Retain the technical dossier, validation reports and Kaizen Log per retention policy.
1. **Knowledge transfer:** Document lessons learned in the [Lessons Learned](../11-project-afsluiting/01-lessons-learned.md) register.
1. **Data deletion:** Delete or anonymise production data in accordance with GDPR \[so-49\].
1. **Infrastructure:** Shut down compute, API keys and monitoring pipelines.
1. **Guardian sign-off:** Guardian confirms all Red Lines obligations have been fulfilled.

## 2. Team & Roles

| Role                        | Responsibility in Monitoring & Optimisation                                                     |
| :-------------------------- | :---------------------------------------------------------------------------------------------- |
| **MLOps Engineer**          | **R**esponsible: Owner of monitoring pipelines, infrastructure and stability.                   |
| **AI Product Manager**      | **A**ccountable: Guards Business KPIs, manages backlog and user feedback.                       |
| **Chief AI Officer (CAIO)** | **C**onsulted: Evaluates long-term ROI and strategic impact.                                    |
| **Data Scientist**          | **R**esponsible: Analyses **Performance Degradation**, performs retraining and improves models. |
| **Guardian (Ethicist)**     | **C**onsulted: Performs ethical reviews and post-market surveillance.                           |

______________________________________________________________________

## 5. Related Modules

**Further reading:**

- [Performance Degradation Detection](05-drift-detectie.md)
- [MLOps Standards](../08-technische-standaarden/01-mloops-standaarden.md)
- [EU AI Act compliance](../07-compliance-hub/01-eu-ai-act/index.md)

**See also:** [Phase 5 Overview](01-doelstellingen.md) · [Deliverables](03-afleveringen.md)
