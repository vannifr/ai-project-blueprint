---
versie: '1.1'
---

# 1. Blueprint & Methodology Index

This page serves as the "Rosetta Stone" of the AI Project Blueprint. Here you will find the mapping between the technical codes (used for auditing and automation) and the content documents.

## 1. The Code Structure

| Code     | Meaning            | Use                                                   |
| :------- | :----------------- | :---------------------------------------------------- |
| **MOD**  | **Module**         | A process phase or knowledge domain in the blueprint. |
| **TMP**  | **Template**       | A fillable document or template.                      |
| **SDD**  | **Spec-Driven**    | Guidelines for specification-driven development.      |
| **GATE** | **Decision Point** | A formal review moment between phases.                |

______________________________________________________________________

## 2. Module Overview (MOD)

The modules form the navigation structure of the AI lifecycle.

| Code       | Phase / Domain                                                             | Description                                                     |
| :--------- | :------------------------------------------------------------------------- | :-------------------------------------------------------------- |
| **MOD-00** | [Strategic Framework](../index.md)                                         | Foundation, reading guide and summary.                          |
| **MOD-01** | [AI-Native Foundations](../01-ai-native-fundamenten/01-definitie.md)       | The 7 normative criteria for AI projects.                       |
| **MOD-02** | [Phase 1: Discovery](../02-fase-ontdekking/01-doelstellingen.md)           | Problem definition and data evaluation.                         |
| **MOD-03** | [Phase 2: Validation](../03-fase-validatie/01-doelstellingen.md)           | Validation Pilot (PoV) and Business Case.                       |
| **MOD-04** | [Phase 3: Development](../04-fase-ontwikkeling/01-doelstellingen.md)       | Development via the SDD method.                                 |
| **MOD-05** | [Phase 4: Delivery](../05-fase-levering/01-doelstellingen.md)              | Go-live and human oversight.                                    |
| **MOD-06** | [Phase 5: Monitoring](../06-fase-monitoring/01-doelstellingen.md)          | Management, performance degradation detection and optimisation. |
| **MOD-07** | [Compliance Hub](../07-compliance-hub/index.md)                            | EU AI Act, Risk Management and Ethics.                          |
| **MOD-08** | [Roles & Responsibilities](../08-rollen-en-verantwoordelijkheden/index.md) | Who does what in AI projects.                                   |
| **MOD-09** | [Toolkit & Templates](../09-sjablonen/index.md)                            | Central storage of all reusable templates.                      |

______________________________________________________________________

## 3. Template Overview (TMP)

These are the artefacts produced during a project. Together they form the **Legal Dossier**.

| Code          | Document Name                                                                         | Phase       | Mandatory? |
| :------------ | :------------------------------------------------------------------------------------ | :---------- | :--------- |
| **TMP-09-01** | [Project Charter](../09-sjablonen/01-project-charter/template.md)                     | Initiation  | ✅         |
| **TMP-09-02** | [Business Case](../09-sjablonen/02-business-case/template.md)                         | Validation  | ✅\*       |
| **TMP-09-03** | [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)                         | Initiation  | ✅         |
| **TMP-09-04** | [Technical Model Card](../09-sjablonen/02-business-case/modelkaart.md)                | Development | ✅         |
| **TMP-09-05** | [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md)                 | All         | ✅         |
| **TMP-09-06** | [Goal Definition (AI Artefact)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) | Development | ✅         |
| **TMP-09-07** | [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)          | Validation  | ✅         |
| **TMP-09-08** | [Traceability Matrix](../09-sjablonen/08-traceerbaarheid-links/template.md)           | Delivery    | ⚠️         |
| **TMP-09-09** | [Risk Analysis (Full)](../09-sjablonen/03-risicoanalyse/template.md)                  | Validation  | ⚠️         |
| **TMP-09-10** | [Prompt Template](../09-sjablonen/10-prompt-engineering/template.md)                  | Development | 💡         |
| **TMP-09-11** | [Privacy & Data Sheet](../09-sjablonen/11-privacy-data/privacyblad.md)                | Discovery   | ✅         |

*\*Optional for Fast Lane projects.*

______________________________________________________________________

## 4. Decision Points (GATES)

| Gate       | Name               | Condition for Passage                          |
| :--------- | :----------------- | :--------------------------------------------- |
| **GATE 1** | Go/No-Go Discovery | Risk Pre-Scan (TMP-03) completed.              |
| **GATE 2** | PoV Investment     | Business Case (TMP-02) approved.               |
| **GATE 3** | Production-Ready   | Validation Report (TMP-07) signed by Guardian. |
| **GATE 4** | Go-live            | Go-live audit completed.                       |
