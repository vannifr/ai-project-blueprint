---
versie: '1.0'
type: guide
layer: 2
phase: [1, 2, 3, 4, 5]
tags: [agile]
summary: Structured evaluation of the AI system and the team to identify improvement areas and embed them in the next cycle.
answers: [How does Retrospectives work?, What roles do I need?]
---

# 1. Retrospectives

!!! abstract "Purpose"
    Structured evaluation of the AI system and the team to identify improvement areas and embed them in the next cycle.

## 1. Objective

We evaluate the functioning of the AI system and the team in a structured and periodic manner to identify improvement points, make adjustments and embed them in the next cycle.

______________________________________________________________________

## 2. Entry Criteria

- The system is in production (Gate 4 approved).
- Monitoring is active and delivering measurable data.
- The management team is assembled and has agreed a fixed cadence.

______________________________________________________________________

## 3. Core Activities

### Sprint Retrospective (Bi-weekly)

The sprint retrospective evaluates the functioning of the team and the system over the past sprint. Use the **Start / Stop / Continue** format as a basis, supplemented with AI-specific questions:

- What data quality problems have emerged?
- What outputs surprised us (positively or negatively)?
- Have any Hard Boundaries been approached or crossed?
- How did the collaboration with the Guardian go?

#### Root Cause Analysis

For each significant problem the team conducts a **thorough root cause analysis**. Use one of these methods:

- **5× Why:** Ask "why?" five times to move from symptom to root cause.
- **Fishbone diagram (Ishikawa):** Categorise causes along dimensions: Data, Model, Process, People, Tooling.
- **Timeline analysis:** Reconstruct the timeline of events that led to the problem.

#### Change Experiments

Each retrospective results in at least one concrete **change experiment** — a bounded adjustment in working method, process or tooling that the team tests in the next sprint:

| Element         | Description                                                                     |
| :-------------- | :------------------------------------------------------------------------------ |
| **Hypothesis**  | "If we change X, we expect Y improvement."                                      |
| **Measurement** | How do we measure whether the experiment succeeds? (KPI, observation, feedback) |
| **Duration**    | One sprint — then evaluate and decide: keep, adjust or stop.                    |
| **Owner**       | One team member who drives the experiment.                                      |

**Duration:** 60 minutes. **Owner:** AI Product Manager. **Output:** Action list + change experiment in the backlog.

### Quarterly Model Retrospective

Every quarter we evaluate the model itself — not just the team:

- Evolution of accuracy compared to the baseline.
- Signals of Performance Degradation: has the distribution of input data changed?
- Comparison with the original Business Case: are we still delivering the promised value?
- Assessment of the Golden Set: are the test cases still representative?

**Duration:** 3 hours. **Owner:** Data Scientist + AI PM. **Output:** Quarterly Model Health Report.

### AI-Specific Retrospective Questions

In addition to the usual team insights, we also ask at every AI project:

| Dimension     | Question                                                               |
| :------------ | :--------------------------------------------------------------------- |
| Data quality  | Are our training data and production data still aligned?               |
| Governance    | Have we complied with all Hard Boundaries this sprint?                 |
| Transparency  | Can we explain to the Guardian why the system made specific decisions? |
| Team capacity | Does the team have sufficient AI knowledge to manage the system?       |
| User feedback | What are end users saying about the quality of the output?             |

______________________________________________________________________

## 4. Team & Roles

| Role               | Responsibility                                           | R/A/C/I |
| :----------------- | :------------------------------------------------------- | :------ |
| AI Product Manager | Facilitates the retrospective, guards action list        | A       |
| Data Scientist     | Reports on model performance and Performance Degradation | R       |
| MLOps Engineer     | Reports on infrastructure and monitoring                 | R       |
| Guardian           | Evaluates compliance with Hard Boundaries and ethics     | C       |
| End users          | Provide feedback on quality of outputs                   | C       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] Action list is documented in the backlog with owner and deadline.
- [ ] Model Health Report (quarterly) has been shared with the CAIO.
- [ ] Significant findings have been passed on to the project Lessons Learned.
- [ ] Decision on retraining or adjustment is documented.

______________________________________________________________________

## 6. Deliverables

| Deliverable                   | Description                                                    | Owner          |
| :---------------------------- | :------------------------------------------------------------- | :------------- |
| Sprint action list            | Concrete improvement points with deadline                      | AI PM          |
| Quarterly Model Health Report | Performance, Performance Degradation, Business Case comparison | Data Scientist |
| Retrospective Minutes         | Decisions and discussion points                                | AI PM          |

______________________________________________________________________

**Related modules:**

- [Continuous Improvement — Overview](index.md)
- [Kaizen Logs](02-kaizen-logs.md)
- [Metrics & Dashboards](03-metrics-dashboards.md)
- [Performance Degradation Detection](../06-fase-monitoring/05-drift-detectie.md)
- [Lessons Learned](../11-project-afsluiting/01-lessons-learned.md)

______________________________________________________________________

**Next step:** [Record improvements in the Kaizen Log](02-kaizen-logs.md)
→ See also: [Metrics & Dashboards](03-metrics-dashboards.md)
