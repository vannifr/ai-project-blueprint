---
versie: '1.0'
pdf: false
---

# Cheatsheet — Red Lines

**Source:** [AI Safety Checklist](../../07-compliance-hub/08-ai-safety-checklist.md) | [Red Teaming](../../07-compliance-hub/07-red-teaming.md)

______________________________________________________________________

## What are Red Lines?

**Red Lines** are behaviours that the AI system must **never** exhibit, regardless of user instruction. They are technically enforced — not merely described in documentation.

______________________________________________________________________

## Universal Red Lines (for every system)

| Category                | Prohibited behaviour                                        |
| :---------------------- | :---------------------------------------------------------- |
| **Harmful content**     | Instructions for physical harm, illegal activities, weapons |
| **Deception**           | Claiming to be human when asked                             |
| **Privacy**             | Generating or inferring personal data about third parties   |
| **System instructions** | Revealing or overwriting own system prompt                  |
| **Scope violation**     | Performing actions outside the defined task scope           |

______________________________________________________________________

## Domain-specific Red Lines (examples)

| Domain           | Red Line example                               |
| :--------------- | :--------------------------------------------- |
| Legal            | No concrete legal advice without qualification |
| Medical          | No diagnoses or medication recommendations     |
| Financial        | No investment advice without disclaimer        |
| HR               | No selection decisions without human review    |
| Customer service | No commitments outside the approved offering   |

______________________________________________________________________

## Defining Red Lines — Template

```
RED LINE #[n]
Category: [Harmful content / Privacy / Scope / Deception / Domain]
Prohibited behaviour: [Exact description]
Technical enforcement: [Input filter / Output filter / Guardrail / Prompt]
Tested via: [Red Teaming exercise #]
Approved by: [Guardian] on [date]
```

______________________________________________________________________

## Gate Review Check

- [ ] All Red Lines are documented in writing
- [ ] Each Red Line is technically enforced (not merely described)
- [ ] Red Teaming has tested Red Lines (see [Red Teaming Playbook](../../07-compliance-hub/07-red-teaming.md))
- [ ] Guardian has approved Red Lines
- [ ] Procedure for violations is documented

**Source:** [Red Teaming Playbook](../../07-compliance-hub/07-red-teaming.md) | [Deployment Safety](../../07-compliance-hub/08-ai-safety-checklist.md)
