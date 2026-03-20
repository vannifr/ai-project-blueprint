---
versie: '1.0'
type: guide
layer: 2
roles: [AI Product Manager]
tags: [onboarding]
answers: [How does Project Charter Light work?]
---

# Project Charter Light

## Instructions

This is a **simplified 1-page project framework** for your first AI initiative. Complete it with your team during the kick-off session on days 1–2. The full version is available in the [Project Charter](../09-sjablonen/01-project-charter/template.md).

!!! tip "Do it in 60 minutes"
    Schedule a structured session of 60 minutes. Treat each section in 10 minutes. Decision points that take longer than 10 minutes: note them as open items and move on.

______________________________________________________________________

**Project:** \[Project name\]
**Date:** \[Date\]
**AI PM:** \[Name\]
**Sponsor:** \[Name of client / executive sponsor\]
**Version:** 1.0

______________________________________________________________________

## Section 1 — The Problem (The Why)

*Describe the pain point you want to solve. Focus on the problem, not the technology.*

**What is the pain point?**

\[E.g. Customer service answers e-mails manually and takes on average 3 days, leading to complaints.\]

**What is the impact of this problem?**

\[E.g. 40 complaints per month; 2 FTEs spend 30% of their time on repetitive replies.\]

**What is the current way of working?**

\[E.g. Staff read e-mails in Outlook and manually type replies based on a FAQ document.\]

______________________________________________________________________

## Section 2 — The Solution (The What)

*Describe in one sentence what you are going to build.*

**Solution concept (1 sentence):**

\[E.g. An AI assistant that summarises incoming e-mails and drafts a reply, which a staff member approves before sending.\]

**Collaboration Mode** (choose one):

- [ ] **Mode 1 — Instrumental:** AI as a tool (e.g. automatic sorting), no interaction with end users
- [x] **Mode 2 — Advisory:** AI makes a suggestion, human decides and approves *(recommended for Explorers)*
- [ ] **Mode 3 — Collaborative:** Human and AI work together as equal partners
- [ ] **Mode 4 — Delegated:** AI executes autonomously, human monitors exceptions

!!! warning "Start low"
    When in doubt: choose one level lower. Mode 2 is the safest starting point for a first prototype.

______________________________________________________________________

## Section 3 — Team & Roles

| Role                       | Name              | Time commitment  |
| :------------------------- | :---------------- | :--------------- |
| AI Project Manager (AI PM) | \[Name\]          | \[e.g. 50%\]     |
| Developer / Tech Lead      | \[Name\]          | \[e.g. 80%\]     |
| Domain Expert              | \[Name\]          | \[e.g. 20%\]     |
| AI Guardian (optional)     | \[Name or "N/A"\] | \[e.g. 10%\]     |
| Sponsor                    | \[Name\]          | Review on day 21 |

______________________________________________________________________

## Section 4 — Scope

**In scope (what we do):**

- \[E.g. Prototype processes incoming e-mails from the mailbox "customerservice@org.com"\]
- \[E.g. Prototype generates draft replies in English\]
- \[E.g. Prototype is tested on 20 historical e-mails\]

**Out of scope (what we do NOT do in these 30 days):**

- Automatic sending of e-mails (human always approves)
- Integration with CRM system
- Multi-language support
- GDPR compliance audit report (follows in the Builder phase)

______________________________________________________________________

## Section 5 — Risk & Compliance (Summary)

*Based on the [Quick Risk Pre-Scan](03-risk-prescan-quick.md). Complete this after days 3–4.*

**Risk score Pre-Scan:** \[ \] Green    \[ \] Amber    \[ \] Red

**EU AI Act category:** \[ \] None/Minimal    \[ \] Transparency obligation    \[ \] High Risk

**Contains personal data:** \[ \] Yes — privacy measures: \[describe\]    \[ \] No

**Hard Boundaries (what the system NEVER does):**

- \[E.g. The system never automatically sends communications without human approval.\]
- \[E.g. The system never provides financial or legal advice.\]

______________________________________________________________________

## Section 6 — Success & Planning

**Definition of success on day 21:**

\[E.g. Prototype processes 20 historical e-mails with ≥ 80% quality score on domain-expert-reviewed draft replies.\]

**Gate 1 Review date:** \[Date, approximately day 21 from start\]

**Go/No-Go criteria:**

| Criterion                | Threshold             | Measured on day |
| :----------------------- | :-------------------- | :-------------- |
| Quality score Golden Set | ≥ 80%                 | Day 16–17       |
| Prototype runs stably    | 0 crashes on 20 cases | Day 16–17       |
| Sponsor is convinced     | Subjective judgement  | Day 21          |

______________________________________________________________________

## Approval

| Role    | Name     | Date     | Signature / E-mail confirmation |
| :------ | :------- | :------- | :------------------------------ |
| AI PM   | \[Name\] | \[Date\] |                                 |
| Sponsor | \[Name\] | \[Date\] |                                 |

______________________________________________________________________

## Next Steps

- [30-Day Plan](01-30-dagen-plan.md) — day-by-day execution
- [Quick Risk Pre-Scan](03-risk-prescan-quick.md) — for section 5 of this charter
- [Full Project Charter](../09-sjablonen/01-project-charter/template.md) — for the Builder phase
