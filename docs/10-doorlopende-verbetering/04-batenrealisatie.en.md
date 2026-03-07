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
