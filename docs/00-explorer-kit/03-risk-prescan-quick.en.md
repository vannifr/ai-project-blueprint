---
versie: '1.0'
type: guide
layer: 2
tags: [onboarding, risk]
---

# Quick Risk Pre-Scan

## 1. Purpose

This shortened risk scan identifies the most critical blockers for your AI prototype in **20–30 minutes**. Conduct it on days 3–4 of the [30-Day Explorer Kit](01-30-dagen-plan.md).

!!! info "Relationship to the full Pre-Scan"
    This is a simplified version of the [full Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md). If the result is amber or red, or if in doubt, always complete the full version.

______________________________________________________________________

**Project:** \[Name\]
**Completed by:** \[Name + role\]
**Date:** \[Date\]

______________________________________________________________________

## 2. Part A — Hard Blockers (Stop Questions)

*If you answer "Yes" to any of these questions: **STOP this project immediately** and consult the [Compliance Hub](../07-compliance-hub/index.md).*

!!! danger "Prohibited practices (EU AI Act Art. 5)"

- [ ] Does the system use subliminal or manipulative techniques to influence human behaviour without the person's knowledge?
- [ ] Does the system apply biometric categorisation based on sensitive characteristics (race, political opinions, religion)?
- [ ] Does the system perform real-time biometric identification in public spaces?
- [ ] Does the system evaluate individuals based on social behaviour ("social scoring")?

**→ If one or more "Yes": PROJECT BLOCKED. Consult [EU AI Act](../07-compliance-hub/01-eu-ai-act/index.md).**

______________________________________________________________________

## 3. Part B — High-Risk Indicators

*Score each question: 0 = No / 1 = Partially / 2 = Yes*

### B1 — Application Domain

| Question                                                                      | Score (0/1/2) |
| :---------------------------------------------------------------------------- | :------------ |
| Is the system deployed in critical infrastructure (energy, water, transport)? |               |
| Does it decide on access to education, employment or social services?         |               |
| Does it decide on credit, insurance or financial services?                    |               |
| Is it deployed in law enforcement, migration or the justice system?           |               |
| Does the system affect safety (physical harm possible)?                       |               |

**Subtotal B1:** \_\_\_/10

### B2 — Data & Privacy

| Question                                                                                       | Score (0/1/2) |
| :--------------------------------------------------------------------------------------------- | :------------ |
| Does the system process personal data (GDPR)?                                                  |               |
| Does the training or inference data contain special categories (health, political, biometric)? |               |
| Is data from minors being processed?                                                           |               |
| Is the data source external/unknown (e.g. web scraping)?                                       |               |
| Are user interactions stored without explicit consent?                                         |               |

**Subtotal B2:** \_\_\_/10

### B3 — Autonomy & Impact

| Question                                                                            | Score (0/1/2) |
| :---------------------------------------------------------------------------------- | :------------ |
| Does the system make decisions without human intervention that impact individuals?  |               |
| Are the consequences of an error difficult to reverse?                              |               |
| Are there no alternative control measures if the system fails?                      |               |
| Does the system interact directly with end users who do not know it is AI?          |               |
| Does the system affect labour-related decisions (evaluation, selection, dismissal)? |               |

**Subtotal B3:** \_\_\_/10

______________________________________________________________________

## 4. Score Calculation

**Total score Part B:** Subtotal B1 + B2 + B3 = \_\_\_/30

| Total score | Colour code  | Interpretation                               | Action                                                                                              |
| :---------- | :----------- | :------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| 0–6         | 🟢 **Green** | Low risk — proceed                           | Document and move to day 5                                                                          |
| 7–15        | 🟡 **Amber** | Elevated risk — additional measures required | Complete the full Pre-Scan; schedule a risk session with a stakeholder                              |
| 16–30       | 🔴 **Red**   | High risk — stop or redefine                 | Complete the [full Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md); consult a legal adviser |

______________________________________________________________________

## 5. Part C — Transparency & Governance (Baseline Checks)

*Always complete, regardless of Part B score.*

!!! check "Minimum requirements for prototype"

- [ ] **Transparency:** End users know they are interacting with an AI system (no hidden AI)
- [ ] **Human oversight:** There is always a human who can review and correct the AI output
- [ ] **Hard Boundaries:** We have defined at least 2 concrete boundaries on what the system NEVER does
- [ ] **Logging:** We log inputs and outputs of the prototype (also for troubleshooting)
- [ ] **Accountable person:** One individual bears ultimate responsibility for this system

______________________________________________________________________

## 6. Conclusion & Next Step

**Risk score:** \[ \] Green    \[ \] Amber    \[ \] Red

**Remarks:**

\[Note any specific risks that deserve extra attention, even if the total score is green.\]

**Established Hard Boundaries:**

1. \[E.g. The system never automatically sends communications without human approval.\]
1. \[E.g. The system never processes personal data outside the EU without explicit consent.\]

**Next step:**

- [ ] Green: Document in [Project Charter Light](02-project-charter-light.md), section 5, and proceed
- [ ] Amber: Schedule risk session and complete [full Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md) before day 9
- [ ] Red: Discuss with Sponsor. Consider redefining the use case

______________________________________________________________________

## 7. Related Modules

- [Full Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)
- [EU AI Act Overview](../07-compliance-hub/01-eu-ai-act/index.md)
- [Risk Classification Framework](../01-ai-native-fundamenten/05-risicoclassificatie.md)
- [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)
- [Privacy & Data Sheet](../09-sjablonen/11-privacy-data/privacyblad.md)
