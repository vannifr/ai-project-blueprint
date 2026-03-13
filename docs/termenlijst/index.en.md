---
versie: '1.0'
pdf: false
description: 'Glossary of AI project management terms: clear definitions bridging technology and business — from golden set and concept drift to agentic AI, RAG, and HAS-H collaboration modes.'
---

# 1. Glossary

This document contains the definitions of the most important terms and abbreviations used in the AI Project Blueprint. We bridge the gap between technology and business by consistently using clear terminology.

______________________________________________________________________

## 1. A

- **AI Collaboration Modes:** A five-level model that defines the relationship and division of tasks between human and AI (Instrumental through Autonomous). → [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)
- **Model fine-tuning:** The fine-tuning of parameters and configurations to optimise the performance of an AI model for a specific task (*Hyperparameter Tuning*).

## 2. B

- **Bias:** Prejudices in data or models that lead to unfair results. See also **Fairness Check**.
- **Business Case:** The financial justification document describing the investment, expected returns (ROI) and cost-benefit analysis. Supplemented by the **Objective Card** for AI-specific goal definitions and Hard Boundaries.

## 3. C

- **CI/CD (Continuous Integration / Continuous Delivery):** An automatic pipeline that builds, tests and deploys code changes. In AI projects, the CI/CD pipeline also monitors model quality via automated gates (e.g. accuracy > 85% before go-live).
- **Circuit Breaker:** An automatic stop mechanism in agentic AI systems that blocks actions or requires human approval when the system exhibits deviant behaviour or exceeds configured thresholds.
- **Constitutional AI:** A technique in which AI systems are trained with explicit ethical principles as an anchored set of rules, so that the system consistently exhibits safe and fair behaviour.

## 4. D

- **Data Assessment:** The process of evaluating whether data is suitable for an AI solution based on Access, Quality and Relevance.
- **DPIA (Data Protection Impact Assessment):** Mandatory risk analysis under GDPR for AI systems that process personal data and pose a high risk to data subjects. → [Data & Privacy Sheet](../09-sjablonen/11-privacy-data/privacyblad.md)

## 5. E

- **EU AI Act:** The European regulation that sets rules for the safety and ethics of AI systems. → [EU AI Act](../07-compliance-hub/01-eu-ai-act/index.md)
- **Evidence Standards:** The minimum criteria that test results and documentation must meet to pass a Gate. Defines standards per risk level for factuality, relevance, safety and fairness. → [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)

## 6. F

- **Fairness Check:** A check or audit to detect undesired bias or discrimination in the output of an AI system. Measures differences in performance between groups (*Bias Audit*).
- **Fast Lane:** An accelerated project route for AI applications with Minimal risk and Collaboration Mode 1-2. Requires less documentation but retains core governance. → [Fast Lane](../02-fase-ontdekking/06-fast-lane.md)

## 7. G

- **Gate:** A formal decision point in the AI lifecycle where a Go/No-Go decision is made on the basis of evidence. The blueprint defines 4 gates (Gate 1 through Gate 4). → [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)
- **Golden Set:** A representative collection of test cases used to measure AI performance. Contains standard cases, edge cases and adversarial scenarios. Size varies by risk level (20–150 cases).
- **GPU (Graphics Processing Unit):** Specialised processor widely used for training and running AI models, due to its high parallelisation capacity.
- **Guardian:** The independent role within the project team that safeguards ethical and legal frameworks. Has veto rights when Hard Boundaries are exceeded. → [Roles & Responsibilities](../08-rollen-en-verantwoordelijkheden/index.md)

## 8. H

- **Hard Boundaries:** The strict limits and safety frameworks that an AI system must never exceed (*Constraints / Guardrails*).
- **Human-in-the-loop:** A working method in which a human supervises or plays a decisive role in an AI-driven process.

## 9. K

- **Knowledge Coupling:** Connecting an AI model to specific business information or documents to make answers more relevant and accurate (*Retrieval-Augmented Generation / RAG*).

## 10. L

- **LLM (Large Language Model):** A large-scale language model trained on extensive text corpora, capable of generating, summarising and reasoning about text. Examples include models in the GPT, Claude and Gemini families.

## 11. M

- **MLOps (Machine Learning Operations):** The combination of practices, processes and tools for reliably building, testing, deploying and monitoring ML models in production. It is the ML counterpart of DevOps.
- **Model Card:** Short name for **Technical Model Card**. The technical accountability document for developers and auditors. → [Technical Model Card](../09-sjablonen/02-business-case/modelkaart.md)
- **Mode 1–5 (AI Collaboration Modes):** The five collaboration levels between human and AI: Mode 1 (Instrumental), Mode 2 (Advisory), Mode 3 (Collaborative), Mode 4 (Delegating), Mode 5 (Autonomous). → [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)
- **Monitoring & Optimisation:** The phase after go-live focused on monitoring performance, costs and compliance.

## 12. O

- **Objective Card:** The AI-specific steering document that combines the **Objective Definition** (what do we want to achieve), **Hard Boundaries** (what must never happen) and **System Prompts** (how do we steer behaviour). Core artefact for every AI solution (*Intent Map*). → [Objective Card template](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)

## 13. P

- **Performance degradation:** The phenomenon in which the accuracy or relevance of a model decreases over time due to changes in data or the world (*Model Drift / Data Drift*). → [Drift Detection](../06-fase-monitoring/05-drift-detectie.md)

## 14. R

- **RACI:** A matrix for assigning roles: **R**esponsible (executor), **A**ccountable (final responsible), **C**onsulted (consulted), **I**nformed (informed). Each activity has exactly one A.
- **Realisation:** The phase in which the AI solution is technically built and extensively tested.
- **ROI (Return on Investment):** The ratio between the return and the investment of a project or system, expressed as a percentage or absolute value.

## 15. S

- **SLO (Service Level Objective):** A measurable target for the quality or availability of a service, such as "latency P95 \< 2 seconds" or "uptime > 99.5%". Lower than an SLA but internally binding for the team.
- **Specification-Driven Development (SDD):** A method in which tests and specifications are drawn up before implementation. First define what the system must do and what it must never do, then build (*Spec-First / Test-Driven Development*). → [Spec-Driven Development](../01-ai-native-fundamenten/06-specificatie-gedreven-ontwikkeling.md)
- **System Prompts:** The collection of information, instructions and configurations that determine how the AI behaves (*Prompts / Context Artifacts*). → [Prompt Engineering template](../09-sjablonen/10-prompt-engineering/template.md)

## 16. T

- **Technical Model Card:** The technical accountability document for developers and auditors. Describes model version, architecture, data sources and configuration. → [Technical Model Card](../09-sjablonen/02-business-case/modelkaart.md)
- **Total Cost of Ownership:** An integral calculation of all costs (investment + operations) and expected returns (ROI).

## 17. U

- **Uncontrolled AI use:** The uncontrolled or unmanaged use of AI tools within an organisation (*Shadow AI*).
- **Usage costs:** The variable costs of running an AI system, such as API tokens or cloud computing time (*Inference costs*).

## 18. V

- **Validation Pilot (PoV):** A small-scale, controlled experiment to prove that an AI solution works in the intended context (*Proof of Value / PoV*). → [Phase 2: Validation](../03-fase-validatie/01-doelstellingen.md)
- **Validation Report:** The evidence document that, using objective test data, demonstrates that an AI system meets the stated objectives and the standards from the Evidence Standards. Contains test results, metrics and conclusions (*Evidence Report*). Note: this is a different document from the Data & Privacy Sheet (GDPR-related). → [Validation Report template](../09-sjablonen/07-validatie-bewijs/validatierapport.md)

______________________________________________________________________
