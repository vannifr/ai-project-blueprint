---
versie: '1.1'
type: foundation
layer: 1
tags: [validation]
summary: Definition of minimum evidence standards so that Gate Reviews are based on verifiable criteria rather than intuition.
answers: [What does Evidence Standards entail?, How much validation is sufficient?]
---

# 1. Evidence Standards

!!! abstract "Purpose"
    Definition of minimum evidence standards so that Gate Reviews are based on verifiable criteria rather than intuition.

!!! tip "When to use this?"
    You are preparing a Gate Review and want to know what evidence you need to collect for your project's risk level and collaboration mode.

## 1. Objective

This module defines **minimum evidence standards** for AI solutions, so that Gate Reviews are based on **verifiable criteria** rather than intuition.

The evidence for an AI system consists of a coherent set of documents and log data that together provide insight into: what the system was supposed to do, how its behaviour was steered, how it was tested and what happened in practice. This coherence enables assessment, auditing and incident analysis.

**Core principle:**
An AI solution may only proceed to the next phase when the evidence meets the standards for the chosen **risk level** (see Risk Management & Compliance) and **Collaboration Mode** (see AI Collaboration Modes).

______________________________________________________________________

## 2. Scope (what does this apply to?)

These standards apply to:

- Generative AI (text/image/advice)
- AI performing classification/extraction
- AI supporting decisions (advisory) or executing them (agent/action)

Not intended for:

- Pure BI reporting without AI decision-making
- Simple rules/automation without a model

______________________________________________________________________

## 3. Definitions (to make terms verifiable)

### Error Classification

- **Critical:** violation of Hard Boundaries (privacy breach, prohibited advice, discriminatory output, dangerous instructions, misleading transparency).
    **Norm:** 0 permitted.
- **Major:** substantively incorrect with a real risk of harm or wrong decision.
    **Norm:** very limited (see table).
- **Minor:** style/format/minor incompleteness without decision impact.

### "Significant Performance Degradation"

Performance degradation is **significant** if any of the following occurs relative to the baseline:

- **Factual accuracy drops ≥ 2 percentage points** (e.g. from 99% to 97%)
- **Relevance score drops ≥ 0.3** on a 1–5 scale
- **Number of Major errors increases ≥ 50%** over two consecutive measurement periods

*(Note: precise thresholds may be stricter per use case, but not more lenient without explicit approval from the Guardian.)*

______________________________________________________________________

## 4. Required evidence (evidence pack)

Each Gate Review is based at minimum on these documents:

1. **[Golden Set Test & Acceptance Protocol](../09-sjablonen/07-validatie-bewijs/template.md)** (the approach)
1. **[Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)** (the results + conclusion)
1. **[Technical Model Card](../09-sjablonen/02-business-case/modelkaart.md)** (what is actually running)
1. **[Goal Definition](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)** (what it was supposed to do + Hard Boundaries)
1. **[Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)** (risk class)

______________________________________________________________________

## 5. Minimum requirements for test sets ("Golden Set")

| Risk Level  | Minimum Golden Set size | Required components                                         |
| ----------- | ----------------------: | ----------------------------------------------------------- |
| **Minimal** |                20 cases | 80% standard cases + 20% edge cases                         |
| **Limited** |                50 cases | 80% standard + 15% complex + 5% adversarial                 |
| **High**    |               150 cases | 70% standard + 20% complex + 10% adversarial + fairness set |

**Additional rules (all levels):**

- Test cases are **realistic real-world examples** (not synthetic "happy flow only").
- Each test case has: **expected outcome** or **assessment criteria**.
- Adversarial set explicitly includes: jailbreaks, prompt injection, policy circumvention, "invent a source" tricks.
- **Synthetic Data Generation:** To reduce the workload of 150+ test cases, a "red-teaming AI" may be used to generate draft test cases. **Requirement:** A human expert must validate and approve each generated test case and the "expected answer" (Ground Truth) before inclusion in the Golden Set.

______________________________________________________________________

## 6. Measurement criteria and minimum standards (per risk level)

> *If your use case has no "accuracy" (e.g. generative text), use "Factual accuracy", "Completeness" and "Relevance" as primary measures.*

### Standards Table

| Criterion                                        |            Minimal risk |                    Limited risk |                                      High risk |
| ------------------------------------------------ | ----------------------: | ------------------------------: | ---------------------------------------------: |
| **Critical errors**                              |                       0 |                               0 |                                              0 |
| **Major errors (max)**                           |         ≤ 2 in test set |                 ≤ 1 in test set |         ≤ 0–1 in test set *(Guardian decides)* |
| **Factual accuracy** *(no factual inaccuracies)* |                   ≥ 98% |                           ≥ 99% |                                        ≥ 99.5% |
| **Relevance (1–5)**                              |                   ≥ 4.0 |                           ≥ 4.2 |                                          ≥ 4.5 |
| **Safety: "must refuse" prompts**                |          100% rejection |                  100% rejection |                                 100% rejection |
| **Transparency (AI disclaimer where required)**  | n/a or 100% if external |           100% where applicable |                          100% where applicable |
| **Fairness check** *(bias)*                      |  qualitative (Guardian) |     qual + quant where possible |               required quant + mitigation plan |
| **Audit trail (logging completeness)**           |        minimal metadata | 100% metadata + output sampling |          100% input/output + traceable context |
| **Stability** *(variation across runs)*          |                 monitor |     limited variation permitted | strict: variation must be explained/acceptable |

### Fairness (bias) — minimum norm (brief and verifiable)

- **Limited:** if relevant groups can be distinguished, then: difference in **Major error rate** between groups ≤ **10%**.
- **High:** difference in **Major error rate** between groups ≤ **5%**, plus described mitigation where deviations exist.

*(If group labels are absent or privacy-sensitive: Guardian determines a qualitative check + mitigation.)*

______________________________________________________________________

## 7. Logging requirements (audit trail)

### What do we log at minimum?

- **Date/time**, user/role (hashed ID where required)
- **Use case / endpoint**
- **Model name + version**
- **Prompt/Steering Instructions version**
- **Sources used** (for Knowledge coupling: document IDs/URLs)
- **Output**
- **Human override** (yes/no + reason)

### Retention (baseline)

- **Minimal/Limited:** standard 90 days, unless otherwise required.
- **High risk:** standard 12 months (or longer if legally required).

*(Align with privacy policy; pseudonymise where possible.)*

______________________________________________________________________

## 8. Evidence per Gate (practical)

- **Gate 1 (Go/No-Go Discovery) (to Evidence):** 09.01 + 09.02 (draft) + 09.03 + Data Evaluation completed.
- **Gate 2 (PoV Investment) (to Development):** 09.06 (pilot results) + 09.04 (draft) + Guardian approval on Hard Boundaries.
- **Gate 3 (Production-Ready) (to Go-live/Delivery):** 09.06 (release candidate) meets standards from §6 + logging plan + incident procedure.
- **Gate 4 (Go-live) (to Management):** baseline recorded + monitoring/feedback loop set up.
