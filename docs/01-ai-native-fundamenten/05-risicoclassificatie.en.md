---
versie: '1.1'
type: foundation
layer: 1
roles: [Guardian]
tags: [risk]
summary: Classification of changes based on impact so that the appropriate validation depth is applied in line with the EU AI Act.
answers: [What does Risk Classification entail?, How do I classify the risk of my AI project?]
---

# 1. Risk Classification

!!! abstract "Purpose"
    Classification of changes based on impact so that the appropriate validation depth is applied in line with the EU AI Act.

## 1. Validation Depth

Not every change requires the same depth of validation. We classify changes based on their impact on the **Hard Boundaries**.

| Level        | Trigger (Example)                               | Validation Depth                                 | EU AI Act Mapping |
| :----------- | :---------------------------------------------- | :----------------------------------------------- | :---------------- |
| **Critical** | Security, Financial transactions, Health advice | Full Validation + **Hard Boundary** Verification | **High Risk**     |
| **Elevated** | Personal data (PII), External API connections   | Extended Behavioural + Goal Alignment check      | **Limited Risk**  |
| **Moderate** | Writing style (Tone of Voice), UX changes       | Minimal Behavioural + Goal Alignment check       | **Limited Risk**  |
| **Low**      | No **Hard Boundaries** affected                 | Syntactic + Minimal Behavioural check            | **Minimal Risk**  |

______________________________________________________________________

## 2. Related Modules

- [Validation Model](04-validatie-model.md)
- [Evidence Standards](07-bewijsstandaarden.md)
- [Pitfalls Catalogue](../17-bijlagen/valkuilen-catalogus.md)
- [EU AI Act](../07-compliance-hub/01-eu-ai-act/index.md)

______________________________________________________________________
