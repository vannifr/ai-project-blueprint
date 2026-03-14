---
versie: '1.0'
---

# 3. Metrics & Dashboards

## 1. Objective

We make the health of the AI system continuously visible via layered dashboards and unambiguous KPIs, so that the management team can intervene in a timely manner when deviations occur.

______________________________________________________________________

## 2. Entry Criteria

- System is in production (Gate 4 approved).
- SLOs are agreed in writing.
- Logging and telemetry are actively set up.

______________________________________________________________________

## 3. Core Activities

### The Four KPI Categories

We measure at four levels. Each category has a fixed owner and reporting cadence:

| Category              | Example metrics                                                          | Owner          | Cadence   |
| :-------------------- | :----------------------------------------------------------------------- | :------------- | :-------- |
| **Model performance** | Accuracy, F1-score, deviation vs Golden Set                              | Data Scientist | Daily     |
| **Operational**       | Latency P95, error rate, uptime, throughput (requests/min)               | MLOps Engineer | Real-time |
| **Usage costs**       | Cost per call, monthly compute costs                                     | AI PM          | Monthly   |
| **Governance**        | Number of Hard Boundary violations, Guardian interventions, bias signals | Guardian       | Weekly    |

### Dashboard Layers

We distinguish three layers. Each dashboard has a different audience and granularity:

**Layer 1 — Operational (real-time):** Visible to MLOps and tech team. Shows system health, alerts and active incidents.

**Layer 2 — Model quality (daily/weekly):** Visible to Data Scientist and AI PM. Shows accuracy trends, Performance Degradation signals and comparison with the Golden Set.

**Layer 3 — Strategic (monthly/quarterly):** Visible to CAIO and management. Shows ROI realisation, cost trends and compliance status.

### Thresholds and Alerts

For each critical metric we define three levels:

| Level                  | Action                                                                   |
| :--------------------- | :----------------------------------------------------------------------- |
| 🟡 **Warning**         | Notification to management team; investigation required within 48 hours  |
| 🟠 **Critical**        | Immediate intervention required; Guardian is informed                    |
| 🔴 **Circuit Breaker** | Automatic blocking or escalation; human approval required before restart |

**Example:** If accuracy drops below 85% (Warning), below 80% (Critical) or below 70% (Circuit Breaker).

### SLO Definition and Monitoring

An SLO (Service Level Objective) is an internally binding target. We define at a minimum:

- **Availability:** e.g. ≥ 99.5% uptime per month.
- **Latency:** e.g. P95 response time ≤ 2 seconds.
- **Accuracy floor:** e.g. F1-score ≥ 0.80 on the Golden Set.

SLOs are established before Gate 4 and included in the handover documentation.

______________________________________________________________________

## 4. Team & Roles

| Role               | Responsibility                                   | R/A/C/I |
| :----------------- | :----------------------------------------------- | :------ |
| MLOps Engineer     | Manages operational dashboard, configures alerts | R       |
| Data Scientist     | Manages model quality dashboard, analyses trends | R       |
| AI Product Manager | Manages strategic dashboard, guards ROI and SLOs | A       |
| Guardian           | Guards governance dashboard, reports deviations  | C       |
| CAIO               | Receives monthly strategic report                | I       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] All four KPI categories are visible in the right dashboard.
- [ ] Thresholds and alert rules are documented and tested.
- [ ] SLOs are established and shared with the management organisation.
- [ ] First monthly report has been delivered to the CAIO.

______________________________________________________________________

## 6. Deliverables

| Deliverable              | Description                                  | Owner          |
| :----------------------- | :------------------------------------------- | :------------- |
| Operational dashboard    | Real-time health monitoring                  | MLOps Engineer |
| Model quality report     | Weekly summary of performance vs Golden Set  | Data Scientist |
| Monthly Strategic Report | ROI, cost, compliance status                 | AI PM          |
| SLO document             | Established service standards and thresholds | AI PM          |

______________________________________________________________________

**Related modules:**

- [Continuous Improvement — Overview](index.md)
- [Retrospectives](01-retrospectives.md)
- [Benefits Realisation](04-batenrealisatie.md)
- [Performance Degradation Detection](../06-fase-monitoring/05-drift-detectie.md)
- [Management & Optimisation — Activities](../06-fase-monitoring/02-activiteiten.md)

______________________________________________________________________

**Next step:** [Measure realised benefits via Benefits Realisation](04-batenrealisatie.md)
→ See also: [Performance Degradation Detection](../06-fase-monitoring/05-drift-detectie.md)
