---
versie: '1.0'
---

# 4. Benefits Realisation (Operational)

## 1. Objective

We measure quarter by quarter whether the AI system is actually realising the benefits promised in the Business Case, and make adjustments when realisation falls short.

______________________________________________________________________

## 2. Entry Criteria

- System is in production and baseline measurement is recorded (see [Handover Checklist](../05-fase-levering/04-sjablonen/overdracht-checklist.md)).
- The original Business Case with benefit KPIs is available.
- The benefits realisation plan has been handed over to the owner in the management organisation.

______________________________________________________________________

## 3. Core Activities

### The AI Productivity Paradox — Warning

!!! warning "Rework Pitfall"
    Research (Workday, 2025) shows that on average **40% of time savings from AI** are lost to *rework*: correcting errors, rewriting AI-generated content and double-checking outputs. At organisational level the actual productivity gain is **5–15%**, compared to the perceived 50–100% at individual level.

    Additionally: AI coding assistants increase pull requests by an average of **154%**, creating new bottlenecks in the review phase.

    **Conclusion:** measure realisation at organisational level, not on individual perception. Split AI-generated work into smaller chunks. Invest in platform maturity and central governance — purely bottom-up experimentation leads to Shadow AI and inconsistency.

Source: \[so-46\]

______________________________________________________________________

### GAINS™ Framework for ROI Measurement

The GAINS™ framework links AI expenditure to concrete business outcomes rather than simply looking at cost items. Use the five dimensions as the structure for your quarterly reporting.

| Dimension                           | What to measure                                 | Target value (guideline)           |
| :---------------------------------- | :---------------------------------------------- | :--------------------------------- |
| **G — Usage & Engagement**          | Active daily users (DAU) and interaction depth  | DAU > 60% of target group          |
| **A — Task Completion Time**        | Acceleration vs. manual baseline per task type  | Define per use case                |
| **I — Error Reduction**             | Error rate and avoided remediation costs        | Link to Benefits Register          |
| **N — Revenue/Output Correlation**  | Direct contribution to revenue or output volume | Link to Business Case              |
| **S — Cost per Productive Outcome** | Cost per useful result (CFO metric)             | Declining trend quarter-on-quarter |

Source: \[so-46\]

______________________________________________________________________

### Quarterly Benefits Realisation Review

Every three months the AI PM compares the actual benefits with the Business Case. The review includes:

1. **Measurement:** Collecting current values for all benefit KPIs.
1. **Comparison:** Actual value vs. target value vs. baseline.
1. **Analysis:** Explain deviations. Is the deviation structural or temporary?
1. **Adjustment:** Propose changes (better adoption, retraining, different approach).
1. **Reporting:** Present findings to the CAIO or steering committee.

### Benefits Register

We maintain a living Benefits Register per AI system:

| Benefit                             | Target  | Baseline | Q1     | Q2     | Q3  | Q4  | Trend       |
| :---------------------------------- | :------ | :------- | :----- | :----- | :-- | :-- | :---------- |
| Processing time saving (hours/week) | -20 hrs | 48 hrs   | 35 hrs | 31 hrs | —   | —   | ↓ on track  |
| Error rate in output                | \< 5%   | 12%      | 8%     | 6%     | —   | —   | ↓ declining |
| User satisfaction (NPS)             | ≥ 30    | 12       | 18     | 24     | —   | —   | ↑ rising    |

### Adjustment Protocol

If a benefit remains more than 20% below the target after two quarters:

1. Root cause analysis by Data Scientist + AI PM.
1. Draw up an adjustment plan (retraining, process redesign, additional user training).
1. Submit adjustment plan to Guardian (do adjustments affect Hard Boundaries?).
1. Document decision in the Kaizen Log.

______________________________________________________________________

## 4. Team & Roles

| Role                      | Responsibility                                      | R/A/C/I |
| :------------------------ | :-------------------------------------------------- | :------ |
| AI Product Manager        | Manages Benefits Register, coordinates review       | A       |
| Data Scientist            | Delivers data-driven analysis of benefit shortfalls | R       |
| CAIO / Steering Committee | Receives quarterly report, approves adjustments     | C       |
| Guardian                  | Assesses whether adjustments affect Hard Boundaries | C       |
| Management organisation   | Provides operational data (actual measurements)     | R       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] Quarterly report has been delivered to the CAIO.
- [ ] All benefit KPIs have been measured and documented in the Benefits Register.
- [ ] Structural shortfalls have a documented adjustment plan.

______________________________________________________________________

## 6. Deliverables

| Deliverable               | Description                                                      | Owner                  |
| :------------------------ | :--------------------------------------------------------------- | :--------------------- |
| Benefits Register         | Living overview of targets, baseline and realisation per quarter | AI PM                  |
| Quarterly Benefits Report | Analysis and adjustment recommendations for CAIO                 | AI PM                  |
| Adjustment Plan           | Concrete actions for structural benefit shortfall                | AI PM + Data Scientist |

______________________________________________________________________

**Related modules:**

- [Continuous Improvement — Overview](index.md)
- [Metrics & Dashboards](03-metrics-dashboards.md)
- [Project Closure — Benefits Realisation](../11-project-afsluiting/03-batenrealisatie.md)
- [Business Case template](../09-sjablonen/02-business-case/template.md)
