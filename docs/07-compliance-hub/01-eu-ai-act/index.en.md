---
versie: '1.1'
description: 'EU AI Act compliance guide: risk classification, obligations per AI system category, and practical steps to align your AI project with the European AI regulation.'
type: index
layer: 3
roles: [Guardian]
tags: [eu-ai-act]
---

# 1. EU AI Act

!!! abstract "Purpose"
    Practical guide to EU AI Act requirements and how to apply them within your AI project.

## 1. Purpose

This document describes the specific requirements of the European AI Regulation (EU AI Act) and how they are applied within the project. The EU AI Act is the world's first comprehensive AI regulation and applies to all organisations that offer or use AI systems within the EU.

______________________________________________________________________

## 2. Risk Classification under the EU AI Act

The EU AI Act categorises systems based on the risk they pose to safety and fundamental rights.

### Unacceptable Risk (Art. 5)

- **Definition:** Systems that pose a clear threat to fundamental rights.
- **Action:** Absolutely prohibited.

**Prohibited applications (Art. 5):**

| Category                          | Description                                                          |
| --------------------------------- | -------------------------------------------------------------------- |
| Manipulation                      | Subliminal techniques that influence behaviour                       |
| Exploitation of vulnerable groups | Abuse of age, disability or social situation                         |
| Social scoring                    | Government assessment of citizens based on behaviour                 |
| Real-time biometrics              | Facial recognition in public spaces (exceptions for law enforcement) |
| Emotion recognition               | In the workplace or in education (limited exceptions)                |
| Biometric categorisation          | Based on sensitive characteristics (race, religion, etc.)            |

### High Risk (Art. 6, Annex III)

- **Definition:** Systems in critical domains with significant impact on fundamental rights.
- **Requirements:** Strict rules for data governance, documentation, transparency and human oversight.
- **Documentation:** Mandatory technical dossier and CE marking.

### Transparency Obligations (EU AI Act Art. 50)

- **Scope:** Transparency obligations apply to certain AI systems, including systems that interact with persons (e.g. chatbots) and systems that generate or publish synthetic or manipulated content in contexts where labelling/disclosure is required.
- **Requirements:** Disclosure/labelling where legally required, including (a) notifying that one is interacting with AI (unless evident from context), and (b) marking/labelling artificially generated or manipulated content where applicable.

> **Clarification:** "Limited risk" is an internal working category within this blueprint. The EU AI Act does not work with an explicit "limited risk" level, but with concrete obligations per system type (Art. 50).

Sources: \[so-27\], \[so-36\]

### Minimal Risk

- **Definition:** Most AI systems (spam filters, AI in games).
- **Requirements:** No legal obligations, but voluntary codes of conduct recommended.

______________________________________________________________________

## 3. Annex III: High-Risk Domains

AI systems fall under High Risk if they are deployed in the following domains:

| Domain                          | Examples                                          | Playbook Mapping           |
| ------------------------------- | ------------------------------------------------- | -------------------------- |
| **Biometrics (1)**              | Facial recognition, fingerprint analysis          | Risk Classification > High |
| **Critical infrastructure (2)** | Traffic, water, gas, electricity                  | Risk Classification > High |
| **Education (3)**               | Admission, assessment, surveillance               | Risk Classification > High |
| **Employment (4)**              | Recruitment, CV screening, performance assessment | Risk Classification > High |
| **Essential services (5)**      | Creditworthiness, insurance, social benefits      | Risk Classification > High |
| **Law enforcement (6)**         | Risk assessment, evidence analysis                | Risk Classification > High |
| **Migration & asylum (7)**      | Visa applications, border control                 | Risk Classification > High |
| **Justice (8)**                 | Investigation of facts and law                    | Risk Classification > High |

______________________________________________________________________

## 4. Article References: Core Obligations

### Art. 9: Risk Management System

**Requirement:** A continuous risk management system throughout the full lifecycle.

**Playbook Implementation:**

- [Risk Pre-Scan](../../09-sjablonen/03-risicoanalyse/pre-scan.md) at project start
- Periodic risk updates at every Gate
- Guardian review on Hard Boundaries
- Incident process for new risks

**Checklist:**

- [ ] Risks are identified and documented
- [ ] Mitigation measures are implemented
- [ ] Residual risks are accepted by the Guardian
- [ ] Risk register is periodically reviewed

### Art. 10: Data Governance

**Requirement:** Use of high-quality datasets with appropriate measures against bias.

**Playbook Implementation:**

- [Data Evaluation](../../02-fase-ontdekking/02-activiteiten.md) in Phase 1
- [Data Pipelines](../../08-technische-standaarden/02-data-pipelines.md) standards
- [Fairness Check](../../07-compliance-hub/03-ethische-richtlijnen.md) for bias detection

**Checklist:**

- [ ] Data sources are documented
- [ ] Data quality has been evaluated
- [ ] Bias analysis has been performed
- [ ] Representativeness has been validated

### Art. 11-12: Technical Documentation

**Requirement:** Comprehensive technical documentation demonstrating compliance.

**Playbook Implementation:**

- [Technical Model Card](../../09-sjablonen/02-business-case/modelkaart.md)
- [Objective Card](../../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Validation Report](../../09-sjablonen/07-validatie-bewijs/validatierapport.md)

**Required Content of Technical Dossier:**

| Element                   | Playbook Document                |
| ------------------------- | -------------------------------- |
| System description        | Technical Model Card             |
| Design and development    | Specification (SDD Pattern)      |
| Operation and limitations | Objective Card + Hard Boundaries |
| Risk management system    | Risk Pre-Scan + updates          |
| Change log                | Git history + release notes      |
| Test results              | Validation Report + Golden Set   |

### Art. 13: Transparency

**Requirement:** Sufficient transparency so that users can interpret the output.

**Playbook Implementation:**

- Transparency obligation in [Hard Boundaries](../../07-compliance-hub/index.md)
- AI disclaimer in user interface (Limited/High Risk)
- Source attribution with Knowledge Coupling (RAG)

**Checklist:**

- [ ] Users know they are communicating with AI
- [ ] Limitations have been communicated
- [ ] Sources are shown where relevant

### Art. 14: Human Oversight

**Requirement:** Measures to enable effective human oversight.

**Playbook Implementation:**

- [AI Collaboration Modes](../../00-strategisch-kader/06-has-h-niveaus.md) determine oversight level
- Guardian role with veto rights
- Human-in-the-loop for Mode 1-3
- Circuit Breaker for Mode 4-5

**Oversight per Collaboration Mode:**

| Mode | Oversight Form       | Implementation                                     |
| ---- | -------------------- | -------------------------------------------------- |
| 1-2  | Human-in-the-loop    | Human always decides                               |
| 3    | Human-on-the-loop    | Human monitors, intervenes on deviation            |
| 4    | Human-over-the-loop  | Human sets boundaries, AI executes                 |
| 5    | Human-above-the-loop | Human sets policy, AI autonomous within boundaries |

### Art. 15: Accuracy, Robustness & Cybersecurity

**Requirement:** Appropriate levels of accuracy, robustness and cybersecurity.

**Playbook Implementation:**

- [Evidence Standards](../../01-ai-native-fundamenten/07-bewijsstandaarden.md) for accuracy norms
- [Test Frameworks](../../08-technische-standaarden/04-test-frameworks.md) incl. adversarial testing
- [AI Architecture](../../08-technische-standaarden/05-ai-architectuur.md) security layers

**Checklist:**

- [ ] Accuracy meets norms per risk level
- [ ] Adversarial testing has been performed
- [ ] Security measures are implemented
- [ ] Robustness is tested (variation, edge cases)

### GPAI (from 2 August 2025) — Implications for Vendor Selection

When your organisation deploys a general-purpose AI (GPAI) or foundation model from a third party, specific considerations apply.

**Role determination:**

- Determine whether your organisation acts as a **deployer** (applying an existing model) or as a **(partial) provider** (fine-tuning, own distribution, or substantial modification).
- In case of substantial modification or (re)distribution of a model, the role may shift towards provider; document this explicitly in the dossier.

**Contractual requirements for vendors:**

- [ ] Model documentation available and up to date
- [ ] Update notifications for model changes
- [ ] Incident support and reporting procedures
- [ ] Contractual guarantees for data governance and security
- [ ] Capability to implement Art. 50 downstream (disclosure/labelling) where relevant

Sources: \[so-27\], \[so-36\]

______________________________________________________________________

## 5. Compliance Mapping: Playbook to EU AI Act

| EU AI Act Article  | Requirement              | Playbook Module                 | Template             |
| ------------------ | ------------------------ | ------------------------------- | -------------------- |
| Art. 5             | Prohibited practices     | Risk Pre-Scan                   | Section A            |
| Art. 6 + Annex III | High-risk classification | Compliance Hub                  | Risk Classification  |
| Art. 9             | Risk management system   | Risk Pre-Scan + Gates           | Risk Analysis        |
| Art. 10            | Data governance          | Data Pipelines + Fairness Check | Data & Privacy Sheet |
| Art. 11-12         | Technical documentation  | Technical standards             | Model Card           |
| Art. 13            | Transparency             | Hard Boundaries                 | Objective Card       |
| Art. 14            | Human oversight          | AI Collaboration Modes          | Project Charter      |
| Art. 15            | Accuracy & security      | Evidence Standards              | Validation Report    |
| Art. 50            | Transparency obligation  | Hard Boundaries                 | Objective Card       |

______________________________________________________________________

## 6. EU AI Act Timeline

The EU AI Act has a phased entry into force. The dates below are binding.

- **1 August 2024** — Regulation enters into force.
- **2 February 2025** — Prohibited practices take effect (Art. 5) + obligation for AI literacy for involved personnel.
- **2 August 2025** — GPAI rules take effect (general-purpose AI / foundation models).
- **2 August 2026** — Most obligations take effect, including Annex III high-risk systems.
- **2 August 2027** — Extended transition period for specific categories: high-risk AI in regulated products + GPAI models already on the market (legacy).

Sources: \[so-27\], \[so-36\]

______________________________________________________________________

## 7. EU AI Act Compliance Checklist (High Risk)

**Prior to development:**

- [ ] Risk classification determined (not Unacceptable)
- [ ] Annex III categorisation documented
- [ ] Risk management system established

**During development:**

- [ ] Data governance measures implemented
- [ ] Technical documentation maintained
- [ ] Human oversight built in

**Before go-live:**

- [ ] Validation Report meets Art. 15 requirements
- [ ] Transparency requirements implemented
- [ ] Conformity assessment completed (if required)
- [ ] CE marking (if applicable)

**After go-live:**

- [ ] Monitoring and logging active
- [ ] Incident reporting procedure ready
- [ ] Periodic compliance review planned

______________________________________________________________________

## 8. Additional Legislation & Belgian Context

### Withdrawal of the AI Liability Directive (AILD)

In February 2025 the European Commission announced the withdrawal of the proposal for the AI Liability Directive, officially published in October 2025. The AILD was intended to ease the burden of proof for victims of AI-related harm via a "rebuttable presumption of causality".

**Consequence for Belgian organisations:** there is currently no harmonised EU directive for AI liability. Liability falls back on:

- **General Belgian liability law** (Art. 1382 BW)
- The revised **Product Liability Directive (PLD)** — see below

Source: \[so-40\]

______________________________________________________________________

### Revised Product Liability Directive (PLD)

The revised PLD (Directive (EU) 2024/2853) entered into force on **8 December 2024** and now explicitly includes software and AI systems as products. Belgium must transpose this into national law by **9 December 2026**.

**Key points for AI projects:**

- AI software falls under the definition of "product" → product liability applies
- Damage caused by defective AI systems can be recovered from the manufacturer/provider
- Documentation obligations under the EU AI Act support the PLD defence

Source: \[so-41\]

______________________________________________________________________

### Scope per Regulation (Belgium)

| Regulation             | Applicable?                                   | Deadline              |
| :--------------------- | :-------------------------------------------- | :-------------------- |
| EU AI Act              | ✅ Yes — directly applicable as EU regulation | Phased until Aug 2027 |
| GDPR / AVG             | ✅ Yes — additionally applicable              | Ongoing               |
| PLD (revised)          | ✅ Yes — after transposition into Belgian law | Dec 2026              |
| AI Liability Directive | ❌ Withdrawn — not in force                   | N/A                   |
| Colorado AI Act (US)   | ❌ Not applicable to Belgian market           | N/A                   |

!!! warning "Legal Fragmentation"
    With the withdrawal of the AILD, organisations are now navigating a patchwork of national legislation. Document your AI systems thoroughly via the EU AI Act obligations: this also forms your PLD defence.

Sources: \[so-40\], \[so-41\]

______________________________________________________________________

## 9. Related Modules

- [Risk Management & Compliance](../index.md)
- [Risk Pre-Scan](../../09-sjablonen/03-risicoanalyse/pre-scan.md)
- [Evidence Standards](../../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Ethical Guidelines](../03-ethische-richtlijnen.md)
