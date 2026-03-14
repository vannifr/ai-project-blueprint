---
versie: '1.0'
---

# 1. Sources & Inspiration

## 1. Overview

This project was created through the synthesis of international industry standards, academic research and practical experience in AI project management. Below is an overview of the most important sources that have served as the foundation and inspiration.

______________________________________________________________________

## 2. Primary Sources (Audit)

The following sources form the legal and technical backbone of this blueprint and are suitable for audit purposes.

| Ref ID        | Source                                                          | Description                                                                                               | Status       |
| :------------ | :-------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----------- |
| **\[so-27\]** | EU AI Act (Official Text)                                       | Official legislative text & Regulation (EU) 2024/1689                                                     | Final        |
| **\[so-36\]** | EU AI Act (Implementation)                                      | Phased entry into force & deadlines                                                                       | Active       |
| **\[so-28\]** | DORA GenAI Report v2025.2                                       | DevOps Research & Assessment report on GenAI impact                                                       | Published    |
| **\[so-1\]**  | NIST IR 8605 (Draft)                                            | A Framework for Managing Risks of Generative AI                                                           | Public Draft |
| **\[so-10\]** | arXiv:2505.10924                                                | Man-in-the-Middle Attacks on LLM-based Agents                                                             | Preprint     |
| **\[so-40\]** | EC — Withdrawal of AILD (OJ EU, Oct 2025)                       | Official withdrawal of AI Liability Directive; implications for EU liability law                          | Final        |
| **\[so-41\]** | Directive (EU) 2024/2853 — Revised PLD                          | Product Liability Directive including software & AI; entry into force 8 Dec 2024                          | Final        |
| **\[so-42\]** | OWASP Top 10 for LLM Applications (2025)                        | Most critical security risks for LLM applications, 2025 edition                                           | Published    |
| **\[so-43\]** | OWASP / Security Research — Deceptive Delight & HashJack (2025) | New attack patterns: multi-turn manipulation and URL-fragment prompt injection                            | Published    |
| **\[so-44\]** | Context Engineering — Industry Analysis (2025)                  | Shift from prompt engineering to context engineering; the Context Builder role                            | Published    |
| **\[so-45\]** | ISACA — AAISM Certification (Aug 2025)                          | Advanced in AI Security Management: world's first AI-centred security management qualification            | Final        |
| **\[so-46\]** | Workday — AI Productivity Research (2025)                       | AI Productivity Paradox: rework pitfall, organisational vs. individual productivity; GAINS™ ROI framework | Published    |
| **\[so-47\]** | Cornell University — Carbon-Aware AI (2025)                     | Smart siting and grid decarbonisation reduce AI carbon footprint by 73%, water by 86%                     | Published    |
| **\[so-48\]** | IEA / Datacenter Energy Reports (2025)                          | Data centre energy consumption, water usage and projections to 2030                                       | Published    |
| **\[so-49\]** | Regulation (EU) 2016/679 — GDPR                                 | General Data Protection Regulation; directly applicable in all EU member states                           | Final        |
| **\[so-50\]** | NIST AI 100-1 — AI Risk Management Framework (RMF) 1.0          | NIST AI RMF: framework for managing AI system risks; four core functions: Govern, Map, Measure, Manage    | Final        |

______________________________________________________________________

## 3. External Standards & Methodologies

The process design of this Blueprint has been tested against and inspired by the following international frameworks:

### Project Management Institute (PMI)

- **CPMAI (Certified Project Manager in Artificial Intelligence):** For the 7-step methodology and the data-centric approach to projects.
- **PMBOK Guide:** For general project management standards and process groups.

### Agile & Software Development

- **Agile Manifesto & Scrum Guide:** For the iterative approach in the **Realisation** and **Delivery** phases.
- **DevOps & MLOps Principles:** For the setup of automated pipelines (CI/CD/CT) and technical robustness.

### Risk Management

- **NIST AI Risk Management Framework (AI RMF 1.0):** For the classification and management of AI-specific risks.
- **ISO/IEC 42001:** The international standard for Artificial Intelligence Management Systems.

______________________________________________________________________

## 4. Legislation & Regulation

The governance and compliance sections (such as **Risk Management & Compliance**) are directly derived from:

### European Union

- **The EU AI Act (2024):** For risk classification (Unacceptable, High, Limited, Minimal) and the obligations around transparency and the technical dossier.
- **General Data Protection Regulation (GDPR):** For privacy safeguards and data minimisation.

______________________________________________________________________

## 5. Academic & Research

- **Stanford Digital Economy Lab - Future of Work:** Research into the impact of AI on work and the economy.
- **MIT NANDA - The GenAI Divide (2025):** Report on the gap in AI execution within the business world.
- **Writer — AI Governance & Communication (2025):** Practical guidelines for stakeholder communication in AI projects and expectation management.

______________________________________________________________________

## 6. Secondary Interpretation (Optional)

The following sources provide additional context and interpretation, but do not serve as primary audit sources.

- MayerBrown — EU AI Act analysis and commentary
- Other secondary interpretation only after review by Guardian

______________________________________________________________________

## Practical References

### EU AI Act — Article Level

| Reference           | Content                                                                  | Relevant for                      |
| :------------------ | :----------------------------------------------------------------------- | :-------------------------------- |
| EU AI Act Annex III | Classification of high-risk AI systems (14 categories)                   | Risk classification, Gate 1       |
| EU AI Act Art. 9    | Risk management system — mandatory for high-risk systems                 | Compliance Hub, Phase 1–3         |
| EU AI Act Art. 13   | Transparency requirements — logging, explainability                      | Operations, Mode 3–4              |
| EU AI Act Art. 17   | Quality management system — procedures and documentation                 | Governance Model, Gate 3          |
| EU AI Act Art. 61   | Post-market monitoring — mandatory drift and incident reporting          | Phase 5, Operations               |
| EU AI Act Art. 72   | Incident reporting to national supervisory authority (serious incidents) | Compliance Hub, Incident Response |

### Data Governance & Privacy

| Reference                                    | Content                                                 | Relevant for                       |
| :------------------------------------------- | :------------------------------------------------------ | :--------------------------------- |
| ISO/IEC 27701:2019                           | Privacy Information Management — extension to ISO 27001 | Privacy-by-Design, Guardian Review |
| EDPB Guidelines 02/2022                      | GDPR application to LLM systems (ChatGPT and similar)   | Compliance Hub, Phase 1            |
| NIST Privacy Framework v1.0                  | Framework for privacy risk management                   | Risk Pre-Scan, Phase 1             |
| DPIA Model (Dutch Data Protection Authority) | Dutch-language DPIA model for high-risk processing      | Phase 2, Guardian Review           |

### MLOps & Monitoring

| Reference                               | Content                                                     | Relevant for                     |
| :-------------------------------------- | :---------------------------------------------------------- | :------------------------------- |
| Google MLOps Whitepaper (2021)          | MLOps maturity model: levels 0, 1, 2                        | Technical Standards, Phase 5     |
| Microsoft MLOps Maturity Model          | Practical framework for CI/CD in ML systems                 | Technical Standards              |
| Monte Carlo — ML Observability (2024)   | Data observability and model health monitoring framework    | Model Health Review, Phase 5     |
| OECD AI Principles (2019, revised 2024) | Five principles for responsible AI (including monitoring)   | Governance Model, Compliance Hub |
| NIST AI RMF 1.0 (2023)                  | AI Risk Management Framework — Govern, Map, Measure, Manage | Risk Pre-Scan, Gate Reviews      |

### Sustainability

| Reference                            | Content                                                     | Relevant for                           |
| :----------------------------------- | :---------------------------------------------------------- | :------------------------------------- |
| Green Software Foundation — SCI Spec | Software Carbon Intensity — CO₂ per software unit           | Green AI, Business Case                |
| IEA Energy & AI Report (2024)        | Energy consumption of AI data centres worldwide             | Business Case, Environmental footprint |
| EU Green Deal Digital Strategy       | European sustainability goals for the digital sector (2030) | Governance Model, Operations           |
