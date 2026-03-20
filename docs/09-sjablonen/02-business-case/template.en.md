---
versie: '1.0'
type: template
layer: 3
phase: [2]
roles: [AI Product Manager, Business Sponsor]
tags: [template]
answers: ['How do I use the Template: Business Case & The Cost Overview template?']
---

# 1. Template: Business Case & The Cost Overview

## 1. Purpose

This template helps to quantify the business value and map the total operating costs of an AI solution.

______________________________________________________________________

!!! note "Download this template"
    [Download as Markdown](https://github.com/vannifr/ai-project-blueprint/raw/main/docs/09-sjablonen/02-business-case/template.en.md){ .md-button } — Open in your editor or AI assistant and fill in the fields.

### Value Hypothesis

*What is the expected gain?*

- **Efficiency gain:** \[E.g. Number of hours saved per month.\]
- **Quality improvement:** \[E.g. Reduction in error rate.\]
- **Revenue growth:** \[E.g. Higher conversion through personalisation.\]

______________________________________________________________________

### The Cost Overview (TCO)

*What are the total costs for development and management?*

- **Investment (Capex):**
- Team hours (Project Management, Data Science, Engineering).
- Initial data acquisition or tooling.
- **Usage Costs (Opex):**
- API / Token costs per month.
- Compute / Hosting (Cloud).
- Maintenance & Monitoring by team.

______________________________________________________________________

### ROI & Payback Period

- **Net return:** \[Value - Costs\].
- **Payback period:** \[Months to break-even\].

______________________________________________________________________

## Environmental Footprint

> **Mandatory field** for all systems with continuous inference or scalable rollout.

| Aspect                         | Estimate / Notes                                      |
| :----------------------------- | :---------------------------------------------------- |
| Inference intensity            | \[Low / Medium / High — calls/day + model type\]      |
| CO₂ estimate (inference)       | \[kg CO₂eq/month — use provider dashboard or tool\]   |
| Training costs (if applicable) | \[Not applicable / kg CO₂eq one-time\]                |
| Comparison with baseline       | \[Current process vs. AI system — net impact\]        |
| Optimisation measures          | \[E.g. model quantisation, batch inference, caching\] |

!!! info "Green AI Guideline"
    Refer to the [Green AI standard](../../08-technische-standaarden/index.md) for calculation tools and thresholds. For systems with >1,000 calls/day, a detailed calculation is required.

______________________________________________________________________
