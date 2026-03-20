---
versie: '1.0'
type: template
layer: 3
phase: [1, 2]
roles: [Guardian]
tags: [risk, template]
answers: [How do I use the Risk Pre-Scan (Gate 1 Checklist) template?]
---

# 1. Risk Pre-Scan (Gate 1 Checklist)

## 1. Purpose

This template serves the initial risk inventory in **Discovery & Strategy** (Phase 1). It helps to identify blockers in the area of legislation (EU AI Act), privacy and ethics at an early stage.

______________________________________________________________________

!!! note "Download this template"
    [Download as Markdown](https://github.com/vannifr/ai-project-blueprint/raw/main/docs/09-sjablonen/03-risicoanalyse/pre-scan.en.md){ .md-button } — Open in your editor or AI assistant and fill in the fields.

**Project:** \[Project Name\]
**Completed by:** \[Name\]

______________________________________________________________________

### Section A: EU AI Act Classification

*Tick what applies. If one of these is 'Yes', that determines the risk category.*

!!! check "Prohibited Practices (UNACCEPTABLE)"

- [ ] Does the system use subliminal techniques to manipulate behaviour?
- [ ] Is biometric categorisation used (race, politics, religion)?
- [ ] Is real-time biometric identification applied in public spaces?

**If YES to any of the above: STOP PROJECT IMMEDIATELY.**

!!! check "High Risk Systems (HIGH RISK)"

- [ ] Is it used in critical infrastructure (water, energy, traffic)?
- [ ] Does it decide on access to education or assessment of students?
- [ ] Does it decide on recruitment, selection or promotion of employees?
- [ ] Does it decide on access to services (credit, benefits, insurance)?

**If YES: Full compliance mandatory (Technical Dossier, CE marking).**

!!! check "Transparency Obligations (Art. 50)"

- [ ] Is there direct interaction with people (chatbot, virtual assistant)?
- [ ] Does the system generate synthetic or manipulated content (text, image, audio)?

**If YES: Transparency obligation (User must know it is AI, content must be labelled where required).**

______________________________________________________________________

### Section A.2: GPAI & Role Determination

!!! check "Role Determination & Obligations"

- [ ] Are we using a GPAI/foundation model from a third party?
- [ ] Are we a deployer or (partial) provider (e.g. through fine-tuning or own distribution)?
- [ ] Does this system fall under Art. 50 transparency obligations (chatbot, synthetic content, or content with manipulative potential)?
- [ ] Is there an AI literacy plan for involved roles (mandatory from 2 February 2025)?

**If one or more questions are answered with "Yes":**
Consult the extended guidance in [EU AI Act Compliance](../../07-compliance-hub/01-eu-ai-act/index.md).

______________________________________________________________________

### Section B: Privacy & Data (GDPR)

- **Are personal data being processed?** \[Yes/No\]
- **Is there a legal basis for this use?** \[Yes/No\]
- **Is data shared with external parties (e.g. OpenAI, Azure)?** \[Yes/No\]

#### B.4 DPIA Triggers (if one "Yes": start DPIA or consult DPO)

!!! check "DPIA Triggers"

- [ ] Large-scale processing of personal data
- [ ] Systematic monitoring of behaviour (e.g. profiling)
- [ ] Use of special categories of personal data
- [ ] Automated assessment with significant impact on persons
- [ ] New technology + high risk context (doubt = involve DPO)

______________________________________________________________________

### Section C: Ethical Quick Scan

- **Can the system discriminate or exclude groups (Bias)?** \[Yes/No\]
- **Is the operation explainable to a layperson?** \[Yes/No\]
- **Is a human 'emergency stop' or override possible?** \[Yes/No\]

______________________________________________________________________

### Conclusion & Guardian Advice

- **Final Risk Level:** \[Low / Limited / High / Prohibited\]
- **Required Actions:** \[E.g. "Conduct DPIA", "Prepare Validation Report", "Add disclaimer"\]
