---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
tags: [quick-reference, risk]
---

# Cheatsheet — Risk Pre-Scan

**Source:** [Risk Pre-Scan Template](../03-risicoanalyse/pre-scan.md)

______________________________________________________________________

## The 5 Quick Risk Questions

| #   | Question                                                    | High-risk indicator       |
| :-- | :---------------------------------------------------------- | :------------------------ |
| 1   | Does the system make decisions that directly affect people? | Yes → High                |
| 2   | Does it process personal or health data?                    | Yes → at least Limited    |
| 3   | Is the output visible to external users?                    | Yes → elevated risk       |
| 4   | What is the impact if the system is wrong?                  | Large/irreversible → High |
| 5   | Is there human oversight on every output?                   | No → risk increase        |

______________________________________________________________________

## Risk Matrix (Quick Assessment)

```
               IMPACT OF ERROR
               Small    Large
ERROR PROB  ┌────────┬────────┐
Low         │  Green │ Yellow │
            ├────────┼────────┤
High        │ Yellow │  Red   │
            └────────┴────────┘
```

- **Green** → Proceed, standard monitoring
- **Yellow** → Define additional mitigation
- **Red** → Escalate to Guardian; consider redesign

______________________________________________________________________

## Top 5 AI Risks to Check

| Risk                | Signal                            | Mitigation                           |
| :------------------ | :-------------------------------- | :----------------------------------- |
| **Hallucinations**  | Factual output without source     | RAG + mandatory source attribution   |
| **Bias**            | User groups treated unequally     | Fairness audit in test set           |
| **Privacy leakage** | PII in prompts or outputs         | Data minimisation + filtering        |
| **Vendor lock-in**  | Dependency on single API provider | Abstraction layer + alternative      |
| **Scope creep**     | System does more than approved    | Hard Boundaries technically enforced |

______________________________________________________________________

## Pre-Scan Outcome

- **≤ 2 risks Yellow, no Red** → Proceed to Gate 1
- **≥ 3 Yellow or 1 Red** → Full risk analysis required first
- **High Risk classification** → EU AI Act process mandatory

**Source for full approach:** [Risk Analysis](../03-risicoanalyse/template.md) | [EU AI Act](../../07-compliance-hub/01-eu-ai-act/index.md)
