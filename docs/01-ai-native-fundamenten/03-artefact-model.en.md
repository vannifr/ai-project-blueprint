---
versie: '1.0'
---

# 1. Artefact Model

## 1. Management Artefacts

To make AI systems governable, we manage specific artefacts that give control over behaviour.

| Artefact                  | Purpose                                                                           | Owner               | Format                                                                            |
| :------------------------ | :-------------------------------------------------------------------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| **Goal Definition**       | **Business hypothesis:** Which outcome is being pursued? (*Intent*)               | AI Product Manager  | Structured statement ("Given X, when Y, then Z")                                  |
| **Hard Boundaries**       | **Hard limits:** What must NEVER happen? (*Constraints*)                          | Guardian (Ethicist) | IF/THEN rules ("IF PII, THEN block")                                              |
| **Steering Instructions** | **Steering:** The configuration that steers the AI (prompts, knowledge coupling). | ML Engineer         | Version-controlled config (e.g. YAML, JSON, Markdown or other structured formats) |
| **Validation Report**     | **Evidence:** Results of tests and measurements (*Evidence*).                     | QA Engineer         | Structured report with metrics                                                    |
| **Traceability**          | **Connection:** Linking Goal → Instruction → Evidence.                            | ML Engineer         | References (IDs / Git SHAs)                                                       |

Steering Instructions encompass not only prompts, but all information and configurations that influence the system's behaviour, including linked knowledge sources, permitted actions, technical constraints, retention periods and rules for use and escalation.

______________________________________________________________________
