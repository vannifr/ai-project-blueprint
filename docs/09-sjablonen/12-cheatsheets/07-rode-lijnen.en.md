---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [Guardian]
tags: [ethics, quick-reference]
---

# Cheatsheet — Hard Boundaries

**Source:** [AI Safety Checklist](../../07-compliance-hub/08-ai-safety-checklist.md) | [Red Teaming](../../07-compliance-hub/07-red-teaming.md)

______________________________________________________________________

## What are Hard Boundaries?

**Hard Boundaries** are behaviours that the AI system must **never** exhibit, regardless of user instruction. They are technically enforced — not merely described in documentation.

______________________________________________________________________

## Universal Hard Boundaries (for every system)

| Category                | Prohibited behaviour                                        |
| :---------------------- | :---------------------------------------------------------- |
| **Harmful content**     | Instructions for physical harm, illegal activities, weapons |
| **Deception**           | Claiming to be human when asked                             |
| **Privacy**             | Generating or inferring personal data about third parties   |
| **System instructions** | Revealing or overwriting own system prompt                  |
| **Scope violation**     | Performing actions outside the defined task scope           |

______________________________________________________________________

## Domain-specific Hard Boundaries (examples)

| Domain           | Red Line example                               |
| :--------------- | :--------------------------------------------- |
| Legal            | No concrete legal advice without qualification |
| Medical          | No diagnoses or medication recommendations     |
| Financial        | No investment advice without disclaimer        |
| HR               | No selection decisions without human review    |
| Customer service | No commitments outside the approved offering   |

______________________________________________________________________

## Defining Hard Boundaries — Template

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

- [ ] All Hard Boundaries are documented in writing
- [ ] Each Red Line is technically enforced (not merely described)
- [ ] Red Teaming has tested Hard Boundaries (see [Red Teaming Playbook](../../07-compliance-hub/07-red-teaming.md))
- [ ] Guardian has approved Hard Boundaries
- [ ] Procedure for violations is documented

**Source:** [Red Teaming Playbook](../../07-compliance-hub/07-red-teaming.md) | [Deployment Safety](../../07-compliance-hub/08-ai-safety-checklist.md)
