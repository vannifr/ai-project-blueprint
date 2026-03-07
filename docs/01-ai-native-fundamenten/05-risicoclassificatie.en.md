---
versie: '1.0'
---

# 1. Risk Classification

## 1. Validation Depth

Not every change requires the same depth of validation. We classify changes based on their impact on the **Hard Boundaries**.

| Level        | Trigger (Example)                               | Validation Depth                                 | EU AI Act Mapping |
| :----------- | :---------------------------------------------- | :----------------------------------------------- | :---------------- |
| **Critical** | Security, Financial transactions, Health advice | Full Validation + **Hard Boundary** Verification | **High Risk**     |
| **Elevated** | Personal data (PII), External API connections   | Extended Behavioural + Goal Alignment check      | **Limited Risk**  |
| **Moderate** | Writing style (Tone of Voice), UX changes       | Minimal Behavioural + Goal Alignment check       | **Limited Risk**  |
| **Low**      | No **Hard Boundaries** affected                 | Syntactic + Minimal Behavioural check            | **Minimal Risk**  |

______________________________________________________________________
