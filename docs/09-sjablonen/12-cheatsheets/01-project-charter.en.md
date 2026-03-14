---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [AI Product Manager]
tags: [quick-reference]
---

# Cheatsheet — Project Charter

**Source:** [Project Charter Template](../01-project-charter/template.md)

______________________________________________________________________

## Mandatory Sections

| Section               | Core question                            | Common pitfall                    |
| :-------------------- | :--------------------------------------- | :-------------------------------- |
| **Problem statement** | What concrete problem are we solving?    | Too broad or too technical        |
| **AI objective**      | What exactly does the AI system do?      | Confusing output with outcome     |
| **Success criteria**  | How will we know it worked? (measurable) | Missing baseline                  |
| **Scope**             | What is and isn't in scope?              | Scope creep from vague boundaries |
| **Risks**             | Top 3 risks + mitigation                 | Only technical risks named        |
| **Stakeholders**      | Who is responsible, who is involved?     | Guardian missing                  |
| **Budget & Timeline** | Phase budget + milestones                | No allowance for iterations       |

______________________________________________________________________

## Minimum Quality Criteria

- [ ] Success criteria are **measurable** (number + timeframe)
- [ ] Baseline is **established** (current performance)
- [ ] **Guardian** is appointed and has signed off
- [ ] Risk classification (High / Limited / Minimal) is determined
- [ ] Business Case is approved or in preparation
- [ ] Charter is signed by sponsor

______________________________________________________________________

## Red Flags

!!! danger "Stop if..."
    - No measurable success criteria have been formulated
    - The problem statement begins with a technology choice ("We're going to use ChatGPT for...")
    - No owner/Guardian has been designated
    - Budget or timeline is entirely absent

______________________________________________________________________

## Quick Reference Risk Classification

| Risk        | Characteristics                                          |
| :---------- | :------------------------------------------------------- |
| **High**    | Decisions affecting people, medical, legal, safety       |
| **Limited** | Customer contact, automated content, recommendations     |
| **Minimal** | Internal use, non-decisive, human final judgement always |

**Source:** [EU AI Act classification](../../07-compliance-hub/01-eu-ai-act/index.md)
