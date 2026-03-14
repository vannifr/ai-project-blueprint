---
versie: '1.1'
type: activities
layer: 2
phase: [2]
roles: [AI Product Manager, Data Scientist]
tags: [validation]
---

# 1. Core Activities & Roles (Validation)

## 1. Core Activities

### Validation Pilot

A small-scale experiment to test whether the AI understands the specific business context.

- **Assemble Test Set:** Collect 50–100 representative real-world examples
- **Baseline Measurement:** How do humans or existing systems perform currently?
- **AI Experiment:** Have the AI process the same examples
- **Success Criterion:** Does the AI score a sufficient result (>90%) on the test set?

### Reliability Testing

Statistical check whether the results are stable and not based on chance.

- **Reproducibility:** Does the AI give consistent answers when repeated?
- **Edge Cases:** How does the system respond to unusual or extreme input?
- **Bias Detection:** Are there systematic errors in certain categories?

### Cost Overview

A complete estimate of investment and operational costs.

#### Investment Costs

- **People:** Development, training, management (FTEs)
- **Technology:** Licences, cloud infrastructure, tools
- **Data:** Cleaning, labelling, enrichment

#### Operational Costs (per month/year)

- **Usage Costs:** Cloud/API costs per task or transaction
- **Maintenance:** Monitoring, updates, support
- **Risk:** Potential costs of errors or incidents

#### Return on Investment (ROI)

- **Time Savings:** How many hours do we save per week/month?
- **Quality Improvement:** Fewer errors, higher customer satisfaction
- **Revenue Growth:** New opportunities, faster turnaround

## 2. Team & Roles

| Role                   | Responsibility in Validation                                                     |
| :--------------------- | :------------------------------------------------------------------------------- |
| **Data Scientist**     | **R**esponsible: Performing the Validation Pilot and reliability testing.        |
| **AI Product Manager** | **A**ccountable: Owner of the business case and ROI calculation (Cost Overview). |
| **Business Sponsor**   | **C**onsulted: Validates the test set and success criteria.                      |
| **Finance**            | **C**onsulted: Reviews the cost estimate and ROI calculation.                    |
| **Stakeholders**       | **I**nformed: Receive updates on progress.                                       |

______________________________________________________________________

## 5. Related Modules

**Templates:**

- [Business Case & Model Card](../09-sjablonen/02-business-case/template.md)
- [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)

**See also:** [Phase 2 Overview](01-doelstellingen.md) · [Deliverables](03-afleveringen.md)

______________________________________________________________________

**Next step:** Run the Validation Pilot and document the results in the Validation report.
→ Use the [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md) as your starting point.
→ See also: [Business Case](../09-sjablonen/02-business-case/template.md) | [Gate 2 Checklist](../09-sjablonen/04-gate-reviews/checklist.md)
