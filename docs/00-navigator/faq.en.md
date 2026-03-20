---
versie: '1.0'
description: Frequently asked questions about AI project management with the Blueprint.
type: faq
layer: 1
answers: [What is Frequently Asked Questions (FAQ)?]
---

# Frequently Asked Questions (FAQ)

## 1. Which metrics should I track to measure success?

The Blueprint uses phase-specific metrics. Use the table below as a starting point and adapt to your project context.

| Phase                     | Key Metrics                                                                                                             | Source                                                                                                                               |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| Discovery & Strategy      | Data quality score, feasibility outcome                                                                                 | [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)                                                            |
| Validation (PoV)          | Accuracy vs. baseline, latency (p95 = 95th percentile; 95% of requests are faster than this value), cost per prediction | [Experiment Ticket](../09-sjablonen/17-experiment-ticket/template.md), [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)  |
| Development               | Test coverage, integration score, Red Line compliance                                                                   | [SDD Pattern](../04-fase-ontwikkeling/05-sdd-patroon.md)                                                                             |
| Delivery                  | Adoption rate, user satisfaction (CSAT/NPS), go-live readiness                                                          | [Handover Checklist](../05-fase-levering/04-sjablonen/overdracht-checklist.md)                                                       |
| Monitoring & Optimisation | Drift indicators, business impact, hallucination rate                                                                   | [Drift Detection](../06-fase-monitoring/05-drift-detectie.md), [Model Health Review](../09-sjablonen/18-modelgezondheid/template.md) |
| Continuous Improvement    | Kaizen velocity, benefits realisation vs. business case                                                                 | [Metrics Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)                                                         |

!!! tip "Start with three"
    Choose a maximum of three key metrics per phase. Too many metrics create reporting overhead without insight. Only add metrics when existing ones leave questions unanswered.

______________________________________________________________________

## 2. What kind of estimates do we need in AI projects?

**Short answer:** Story points remain useful for coordination but lose their predictive value for AI-specific experiment work.

**Why?** AI experiments are non-deterministic: outcomes depend on data quality, model behaviour and unexpected edge cases. Traditional estimation assumes known complexity — with AI, the complexity often only becomes clear in hindsight.

**Recommendation:**

- **Time-boxing instead of estimation** for AI experiment work. Use the [Experiment Ticket](../09-sjablonen/17-experiment-ticket/template.md) to scope spikes with a fixed end date and decision point (Continue / Pivot / Stop).
- **Keep story points** for infrastructure, integration and UI work within the same sprint — relative estimation remains valuable there.
- **Avoid the trap** of retroactively assigning higher points to failed experiments. A failed experiment with valuable insights is not a "bigger ticket" — it is a learned outcome.

See also: [Agile Anti-patterns](../00-strategisch-kader/04-agile-antipatronen-niet-toegestaan.md) for common pitfalls in AI projects.

______________________________________________________________________

**Next step:** Define your phase-specific metrics and record them in the [Project Charter](../09-sjablonen/01-project-charter/template.md).
→ See also: [Experiment Ticket](../09-sjablonen/17-experiment-ticket/template.md) | [Metrics Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
