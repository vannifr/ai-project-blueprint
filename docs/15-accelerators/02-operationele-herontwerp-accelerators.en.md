---
versie: '1.0'
type: strategic
layer: 2
answers: [What does Operational Redesign Accelerators entail?]
---

# 2. Operational Redesign Accelerators

## 1. Purpose

These accelerators speed up the execution of the [Operational Redesign](../14-drie-tracks/02-operationele-herontwerp.md) track. They provide ready-to-use frameworks for process analysis, prioritisation and implementation planning.

______________________________________________________________________

## 2. Accelerator: Process Scorecard

Use this format to evaluate processes on AI suitability. Score each criterion from 1 (low) to 3 (high).

| Criterion            | Score (1–3) | Notes                                             |
| :------------------- | :---------- | :------------------------------------------------ |
| **Repeatability**    |             | How often is this process executed?               |
| **Data richness**    |             | Is sufficient historical data available?          |
| **Rule-based**       |             | Are decisions based on clear rules?               |
| **Error-proneness**  |             | How often do errors occur in the current process? |
| **Time-intensity**   |             | How many hours per week does this process cost?   |
| **Low error impact** |             | Are AI errors recoverable without major damage?   |

**Total score:** Sum of all scores (max. 18). Processes with score ≥ 12 are strong candidates.

______________________________________________________________________

## 3. Accelerator: AI Process Redesign Template

Use this format for each selected process before implementation:

### Current State ('As-Is')

- **Process name:** \[name\]
- **Process owner:** \[name + role\]
- **Frequency:** \[daily / weekly / per request\]
- **Steps:** \[list the steps as a numbered list\]
- **Current KPI:** \[e.g. 45 min/document, 8% error rate\]
- **Bottlenecks:** \[what costs the most time or causes the most errors?\]

### Desired State ('To-Be')

- **Role of AI:** \[which steps does AI take over or support?\]
- **Role of human:** \[what does the employee still do?\]
- **Collaboration mode:** \[Mode 2 / 3 / 4 — see [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)\]
- **KPI target value:** \[e.g. 10 min/document, \<2% error rate\]
- **Hard Boundaries:** \[which decisions may AI never make independently?\]

### Baseline Measurement

| KPI       | Current value | Target value | Measurement method |
| :-------- | :------------ | :----------- | :----------------- |
| \[KPI 1\] |               |              |                    |
| \[KPI 2\] |               |              |                    |

______________________________________________________________________

## 4. Accelerator: Implementation Sprint Plan

Divide the implementation into four two-week sprints:

| Sprint   | Week | Goal                     | Deliverables                                               |
| :------- | :--- | :----------------------- | :--------------------------------------------------------- |
| Sprint 1 | 1–2  | Build & internal testing | Working basic version + internal test report               |
| Sprint 2 | 3–4  | User pilot (small group) | Pilot feedback + first measurements                        |
| Sprint 3 | 5–6  | Adjust & expand          | Improved version + broader pilot group                     |
| Sprint 4 | 7–8  | Scale & embed            | Production version + process description + monitoring live |

**Go/No-Go after Sprint 2:** If pilot results are not moving towards target values, stop and analyse the cause before Sprint 3.

______________________________________________________________________

## 5. Accelerator: Adoption Plan

Technology alone is not enough — adoption determines success.

| Phase       | Activity                                                       | Owner              |
| :---------- | :------------------------------------------------------------- | :----------------- |
| Awareness   | Communication about the 'why' of the change                    | AI PM + Management |
| Training    | Hands-on session in the new way of working (not just the tool) | Tech Lead + HR     |
| Guidance    | Buddy system: experienced users help new users                 | Process owner      |
| Measurement | Weekly check-in: how is usage going?                           | AI PM              |
| Embedding   | Include KPIs in regular performance conversations              | Management         |

______________________________________________________________________

## 6. Related Modules

- [Accelerators — Overview](index.md)
- [Operational Redesign](../14-drie-tracks/02-operationele-herontwerp.md)
- [Quick Start: AI Project in 90 Days](../12-90-dagen-roadmap/index.md)
- [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
- [Benefits Realisation — Operational](../10-doorlopende-verbetering/04-batenrealisatie.md)
