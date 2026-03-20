---
versie: '1.1'
description: 'Compliance Hub: all regulatory and ethical requirements for AI projects in one place — EU AI Act, risk management, ethical guidelines, incident response, red teaming, and safety checklists.'
type: index
layer: 3
roles: [Guardian]
tags: [eu-ai-act]
summary: Central overview of all regulatory and ethical requirements for AI projects, from EU AI Act to incident response and safety checklists.
answers: [What does the Risk Management & Compliance section contain?]
---

# 1. Risk Management & Compliance

!!! abstract "Purpose"
    Central overview of all regulatory and ethical requirements for AI projects, from EU AI Act to incident response and safety checklists.

Compliance is not a brake — it is the brakes on a car that allow you to drive fast safely. This module centralises requirements from the EU AI Act, internal values and ethical frameworks.

______________________________________________________________________

## 2. Modules in This Section

| Module                                                         | Description                                                                         |
| :------------------------------------------------------------- | :---------------------------------------------------------------------------------- |
| [EU AI Act](01-eu-ai-act/index.md)                             | Risk classification, obligations per risk level, timeline and compliance checklist  |
| [Risk Management](02-risicobeheer/index.md)                    | Risk analysis, mitigation and continuous risk monitoring                            |
| [Ethical Guidelines](03-ethische-richtlijnen.md)               | Operational ethical frameworks: fairness audit, representativeness, equal treatment |
| [Validation Requirements](04-validatie-eisen.md)               | Evidence standards per risk level for audit compliance                              |
| [Incident Response](05-incidentrespons.md)                     | Emergency stop, reporting obligation, escalation procedure                          |
| [Incident Response Playbooks](06-incidentrespons-playbooks.md) | Concrete playbooks per incident type                                                |
| [Red Teaming](07-red-teaming.md)                               | Security testing: jailbreaks, prompt injection, harmful output                      |
| [AI Safety Checklist](08-ai-safety-checklist.md)               | Safety checklist for go-live                                                        |

______________________________________________________________________

## 3. Privacy-by-Design (GDPR)

Privacy is not an afterthought, but a design choice. Minimum rules that always apply:

- **Data minimisation:** collect/process only what is necessary.
- **Purpose limitation:** do not automatically reuse data for other purposes.
- **Transparency:** user/data subject knows when AI is being used.
- **Security:** access, logging and retention are in place before go-live.

No go-live without a completed [Data & Privacy Sheet](../09-sjablonen/11-privacy-data/privacyblad.md) and documented logging and retention agreements.

______________________________________________________________________

## 4. Agentic AI & Constitutional AI

When AI systems perform actions autonomously ([Collaboration Mode](../00-strategisch-kader/06-has-h-niveaus.md) 4 & 5), the focus shifts to **Constitutional AI**: technical restriction of the action radius and real-time monitoring that blocks actions when hard boundaries are crossed.

______________________________________________________________________

**Next step:** Determine the risk class of your system via the [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md).
→ See also: [Risk Classification](../01-ai-native-fundamenten/05-risicoclassificatie.md) | [Decision Matrix](../08-rollen-en-verantwoordelijkheden/besluitvormingsmatrix.md)
