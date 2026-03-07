---
versie: '1.0'
---

# 2. Kaizen Logs

## 1. Objective

We record every small, targeted improvement to the AI system in a continuous Kaizen Log so that improvements are traceable, repeatable and aggregately visible.

______________________________________________________________________

## 2. Entry Criteria

- The system is in production and actively in use.
- The retrospective cadence is operational.
- A shared document or backlog is available for the team.

______________________________________________________________________

## 3. Core Activities

### Recording a Kaizen Entry

Every improvement — however small — is logged with a fixed structure:

| Field       | Description                                                    |
| :---------- | :------------------------------------------------------------- |
| **ID**      | Unique sequence number (e.g. KZ-2026-001)                      |
| **Date**    | Date on which the problem was identified                       |
| **Owner**   | Who is responsible for implementation?                         |
| **Problem** | What is not working well or could be better? (max 2 sentences) |
| **Measure** | What is the concrete improvement?                              |
| **Result**  | What is the measured effect after implementation?              |
| **Status**  | Open / In progress / Closed                                    |

**Example:**

> KZ-2026-007 · 15-03-2026 · Data Scientist · Accuracy in category X drops structurally 3% per month. · Supplement Golden Set with 20 new edge cases and retrain. · Accuracy restored to baseline +1.2%. · Closed.

### Monitoring the Kaizen Cycle

- **Weekly:** Discuss status of open entries in the stand-up.
- **Monthly:** Overview of closed entries and measured effects to the team.
- **Quarterly:** Aggregated Kaizen analysis as input for the Model Retrospective.

### Distinction Kaizen Log vs. Incident Log

| Kaizen Log                     | Incident Log                       |
| :----------------------------- | :--------------------------------- |
| Proactive improvements         | Reactive outages and incidents     |
| Focused on quality improvement | Focused on recovery and root cause |
| No time pressure               | SLO-bound response times           |
| Owner: AI PM / Data Scientist  | Owner: MLOps Engineer              |

______________________________________________________________________

## 4. Team & Roles

| Role               | Responsibility                                       | R/A/C/I |
| :----------------- | :--------------------------------------------------- | :------ |
| AI Product Manager | Manages the Kaizen Log, prioritises entries          | A       |
| Data Scientist     | Records and analyses model-related improvements      | R       |
| MLOps Engineer     | Records infrastructure and pipeline improvements     | R       |
| Guardian           | Assesses whether improvements affect Hard Boundaries | C       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] All open entries older than 30 days have a status update or have been escalated.
- [ ] Monthly overview has been shared with the team.
- [ ] Quarterly analysis has been included in the Model Health Report.

______________________________________________________________________

## 6. Deliverables

| Deliverable        | Description                                | Owner          |
| :----------------- | :----------------------------------------- | :------------- |
| Kaizen Log         | Living overview of all improvements        | AI PM          |
| Monthly overview   | Summary of closed entries and effects      | AI PM          |
| Quarterly analysis | Aggregated insight into improvement trends | Data Scientist |

______________________________________________________________________

**Related modules:**

- [Continuous Improvement — Overview](index.md)
- [Retrospectives](01-retrospectives.md)
- [Metrics & Dashboards](03-metrics-dashboards.md)
- [Management & Optimisation — Activities](../06-fase-monitoring/02-activiteiten.md)
