---
versie: '1.0'
description: Three anonymised case studies of AI projects at different risk levels — from an internal knowledge bot to high-risk credit assessment.
type: reference
layer: 3
---

# Case Studies

The examples below illustrate how the Blueprint is applied in practice. All organisation names and persons are anonymised.

______________________________________________________________________

## Example 1 — Minimal Risk: Internal Knowledge Bot (Government)

**Sector:** Government — municipal services
**Risk class:** Minimal Risk (Mode 2 — Advisory)
**Blueprint components used:** Explorer Kit, Project Charter, Goal card, Validation report

### Situation

A mid-sized municipality wanted to help employees quickly find answers in internal policy documents and process descriptions. The call centre needed an average of 40 minutes per complex query; much time was lost searching for information in an outdated intranet.

### Approach

The project team used the **Fast Lane** (6 weeks) because the risk class was Minimal: no personal data, no external decisions, fully internal use. The Goal card defined the intent as "employee finds the correct policy document within 2 minutes". Red Lines restricted the system to internal documents and prohibited answers to legal or medical questions.

The PoV lasted 2 weeks and tested 50 representative questions (the Golden Set). After validation (89% correct references) the system was rolled out to 3 pilot departments.

### Result

Average search time fell from 40 to 6 minutes. Adoption after 8 weeks: 74% of employees use the system daily. No incidents reported. The system operates in **Mode 2**: each employee evaluates the answer themselves before using it.

*Sector: Government — Names anonymised.*

______________________________________________________________________

## Example 2 — Limited Risk: Customer Service Automation (Financial Services)

**Sector:** Financial services — insurer
**Risk class:** Limited Risk (Mode 3 — Collaborative)
**Blueprint components used:** Full lifecycle (13 weeks), Business Case, Fairness audit (bias audit), Guardian Review, Validation report

### Situation

A mid-sized insurer received 12,000 customer queries per month by email, of which 60% were routine (policy status, payment confirmations, address changes). The processing team of 8 employees consistently worked with a backlog.

### Approach

The Guardian classified the system as Limited Risk: customers communicate with an AI but take the action themselves (no automatic decisions). Transparency obligation: customers are informed that they are communicating with an AI assistant.

The **Fairness audit (bias audit)** tested whether customer queries in simpler language (lower literacy level, non-native speakers) received equivalent response quality. An initial problem with formal language use was corrected in the prompt revision of week 8.

The Business Case demonstrated an ROI of 340% over 18 months. Gate 2 (investment decision) was made based on the Validation report after the PoV: 91% correct routing, 0 privacy incidents.

### Result

Processing time for routine queries fell from 4 hours to 12 minutes per batch. The team of 8 was redeployed to handle complex complaints. Customer satisfaction (NPS) rose by 12 points. The system operates in **Mode 3**: the AI drafts a response, an employee approves before sending.

*Sector: Financial services — Names anonymised.*

______________________________________________________________________

## Example 3 — High Risk: Credit Risk Assessment (Finance)

**Sector:** Financial services — credit provider
**Risk class:** High Risk (EU AI Act Annex III — Mode 4 Delegated)
**Blueprint components used:** Full lifecycle (22 weeks), DPIA, Fairness audit (bias audit, extended), Guardian Review, Evidence Standards High Risk, CE-marking preparation

### Situation

A credit provider wanted to partially automate the acceptance process for small business loans (\< €50,000). The manual process took an average of 5 working days; commercial pressure was high to reduce this to 24 hours.

### Approach

The Guardian immediately classified the system as **High Risk** (EU AI Act Annex III, point 5b: AI systems for creditworthiness assessments). This activated the full compliance trajectory: DPIA, extended Fairness audit (bias audit), human oversight at every decision, logging for 5 years, and preparation for the EU AI Act declaration of conformity.

The **Fairness audit (bias audit)** revealed that the initial model rejected applications from sole traders in certain postal code areas 23% more often than comparable applications. Analysis showed this was a proxy for demographic characteristics — an unacceptable Red Line. The model was revised with corrected training data.

Gate 3 (production go) was delayed by 3 weeks for additional validation by an external auditor. The system was deployed in **Mode 4**: the AI makes a recommendation with a confidence score; a credit analyst makes the final decision and documents the rationale.

### Result

Turnaround time fell from 5 to 1.5 working days. The Fairness correction improved the representativeness of the portfolio. First external audit after 6 months of production: no violations. The incident involving the proxy variable is documented as a learning point in the Lessons Learned and has led to a tightening of the Fairness audit procedure in the Blueprint.

*Sector: Financial services — Names anonymised.*

______________________________________________________________________

**Related modules:**

- [Risk Classification](../01-ai-native-fundamenten/05-risicoclassificatie.md)
- [Compliance Hub](../07-compliance-hub/index.md)
- [90-Day Roadmap](../12-90-dagen-roadmap/index.md)

______________________________________________________________________

**Version:** 1.0
**Date:** 13 March 2026
**Status:** Final
