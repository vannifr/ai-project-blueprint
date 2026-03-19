---
versie: '1.1'
description: 'Compliance Hub: all regulatory and ethical requirements for AI projects in one place — EU AI Act, risk management, ethical guidelines, incident response, red teaming, and safety checklists.'
type: index
layer: 3
roles: [Guardian]
tags: [eu-ai-act]
---

# 1. Risk Management & Compliance

## 1. Purpose of This Module

Compliance is not a brake — it is the brakes on a car that allow you to drive fast safely. This module defines the **Hard Boundaries**: the ethical and legal limits within which we innovate. It centralises requirements from the EU AI Act and internal values.

______________________________________________________________________

## 2. Risk Classification (The Pyramid)

Before a project starts (in **Discovery & Strategy**), it must be assigned to a risk category. This determines the intensity of oversight required.

| Risk Level       | Description                                                      | Example                                                     | Required Action                                                                                                                        |
| :--------------- | :--------------------------------------------------------------- | :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| **Unacceptable** | Systems that manipulate people or perform social scoring.        | Real-time facial recognition in public spaces.              | **PROHIBITED**. Project is stopped immediately.                                                                                        |
| **High Risk**    | AI with impact on critical infrastructure or fundamental rights. | CV scanner for job applicants, creditworthiness assessment. | Full EU AI Act Compliance ([Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md), Human oversight, CE marking). |
| **Limited Risk** | Systems that interact with users or generate content.            | Customer service chatbot, marketing text generator.         | Transparency obligation. The user must know they are interacting with AI.                                                              |
| **Minimal Risk** | Internal optimisations without personal data.                    | Spam filter, inventory forecasting, code assistant.         | No specific requirements (code of conduct recommended).                                                                                |

______________________________________________________________________

## 3. The Role of the Guardian (Ethicist)

The Guardian is the "Protector" of the organisation's values. This role is independent of the development team.

- **Mandate:** The Guardian has veto rights (via a 'Stop button') in every phase of the project if the **Hard Boundaries** are crossed.
- **Tasks:**
- Phase 1: Assesses the **Objective Definition** for ethical desirability.
- Phase 2 & 3: Performs **Fairness Checks** (Bias audits).
- Phase 5: Performs periodic 'Vibe Checks' on production systems.

______________________________________________________________________

## 4. The Fairness Check (Bias Audit)

AI learns from historical data and can therefore inherit biases. We assess every High and Limited risk system on three levels:

1. **Representativeness:** Is the data a good reflection of reality?
1. **Stereotyping:** Does the AI reinforce harmful clichés?
1. **Equal Treatment:** Does every user group receive the same quality of responses?

______________________________________________________________________

## 5. Incident Management

What if something goes wrong?

- **The Emergency Stop (Circuit Breaker):** For autonomous systems (**Collaboration Mode** 4 & 5) there must be a technical or procedural way to take the AI offline immediately.
- **Reporting Obligation:** Incidents in which people have been harmed must be reported to the internal Compliance/Legal team within 24 hours.

______________________________________________________________________

## 6. Documentation Requirements (The Dossier)

For High Risk systems a 'Technical Dossier' is mandatory. This contains:

- **System Description:** What does it do and for whom?
- **Dataset Specifications:** Where does the data come from and how was it evaluated (**Data Evaluation**)?
- **Risk Management Plan:** What risks exist and how are they mitigated?
- **Instructions for Use:** Manual for the human supervisor.
- **Logs:** Evidence of operation and decisions ([Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)).

______________________________________________________________________

## 7. Privacy-by-Design (GDPR) — Practical Guidelines

**Goal:** privacy is not an afterthought, but a design choice.

### Minimum Rules (Always)

- **Data minimisation:** collect/process only what is necessary.
- **Purpose limitation:** do not automatically reuse data for other purposes.
- **Transparency:** user/data subject knows when AI is being used (where relevant).
- **Security:** access, logging and retention are in place before go-live.

### Privacy Actions Per Phase

**Phase 1 (Discovery & Strategy):**

- Complete the [Data & Privacy Sheet](../09-sjablonen/11-privacy-data/privacyblad.md) at a high level.
- Determine whether a DPIA is required (see [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md) triggers).

**Phase 2 (Validation):**

- Test with as little personal data as possible (pseudonymise where possible).
- Document which logs you need and how you safeguard privacy.

**Phase 3 (Development):**

- Implement redaction/pseudonymisation in pipelines where possible.
- Ensure access to prompts/config is restricted (change control).

**Phase 4 (Delivery):**

- Publish transparency and usage instructions (if external/customer-facing).
- Confirm processor agreements and data location.

**Phase 5 (Management & Optimisation):**

- Monitor for data leaks/unwanted data in logs.
- Periodic review of retention and access rights.

### Go-Live Condition

No go-live without:

- [Data & Privacy Sheet](../09-sjablonen/11-privacy-data/privacyblad.md) completed and approved (Privacy/DPO if required)
- Logging and retention agreements documented (see [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md))

______________________________________________________________________

## 8. Agentic AI & Constitutional AI

When AI systems perform actions autonomously (Mode 4 & 5), the focus shifts to **Constitutional AI**:

- **Action Radius:** Technical restriction of what an agent may do (e.g. maximum budget limits).
- **Hard Boundary Monitoring:** Real-time monitoring that blocks actions if they risk crossing the **Hard Boundaries**.

When an AI system can perform actions in other systems, it is explicitly documented which systems and functions are accessible, under what conditions this may occur and how access can be immediately restricted or revoked in the event of deviations or incidents.

______________________________________________________________________

**Next step:** Determine the risk class of your system and select the corresponding compliance path.
→ Use the [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md) as your starting point.
→ See also: [Risk Classification](../01-ai-native-fundamenten/05-risicoclassificatie.md) | [Decision Matrix](../08-rollen-en-verantwoordelijkheden/besluitvormingsmatrix.en.md)

______________________________________________________________________

**Version:** 1.0 / **Date:** 13 March 2026 / **Status:** Draft
