---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
tags: [quick-reference, validation]
---

# Cheatsheet — Evidence Standards

**Source:** [Evidence Standards](../../01-ai-native-fundamenten/07-bewijsstandaarden.md)

______________________________________________________________________

## Evidence Levels

| Level                    | Description                                  | Example                              |
| :----------------------- | :------------------------------------------- | :----------------------------------- |
| **L1 — Claim**           | Assertion without substantiation             | "The model is accurate"              |
| **L2 — Indication**      | Single measurement or anecdote               | One test result                      |
| **L3 — Evidence**        | Repeatable measurement on representative set | Golden Set score on 200 items        |
| **L4 — Strong Evidence** | Multiple methods, independently validated    | Golden Set + human review + A/B test |

**Minimum requirement for Gate 2:** level L3 or higher.

______________________________________________________________________

## Required Evidence per Artefact

| Artefact           | Minimum level | Method                                                                                        |
| :----------------- | :------------ | :-------------------------------------------------------------------------------------------- |
| Output quality     | L3            | Golden Set + automated metric                                                                 |
| Fairness           | L3            | Segmented analysis per group                                                                  |
| Safety (High Risk) | L4            | Red Teaming + independent review                                                              |
| Latency            | L3            | Load test (p95, p99) (p95 = 95th percentile — 95% of all requests are faster than this value) |
| Cost projection    | L2            | Calculator + documented assumptions                                                           |
| Traceability       | L3            | Audit trail demonstrated                                                                      |

______________________________________________________________________

## Evidence Documentation

Each piece of evidence must include at minimum:

- **What** was measured (metric, definition)
- **How** measured (method, tool)
- **When** measured (date, version)
- **By whom** assessed (reviewer, independence)
- **Result** (number + comparison with threshold)

______________________________________________________________________

## Common Mistakes

!!! warning "Insufficient evidence"
    - Metric measured on training data instead of independent test set
    - No baseline defined ("better than before" is not evidence)
    - Only positive results reported (cherry picking)
    - Evaluation performed by the development team itself (no independence)

**Source:** [Evidence Standards](../../01-ai-native-fundamenten/07-bewijsstandaarden.md) | [Validation Report](../07-validatie-bewijs/validatierapport.md)
