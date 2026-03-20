---
versie: '1.1'
type: activities
layer: 2
phase: [1]
roles: [AI Product Manager]
summary: Overview of the core activities and role assignments during the Discovery phase, from problem exploration to data evaluation and risk assessment.
answers: [What activities do I perform in this phase?, How do I classify the risk of my AI project?]
---

# 1. Core Activities & Roles (Discovery & Strategy)

!!! abstract "Purpose"
    Overview of the core activities and role assignments during the Discovery phase, from problem exploration to data evaluation and risk assessment.

## 1. Core Activities

### Problem Exploration

We define the challenge from the end user's perspective, not from the technology's perspective.

- **Question Articulation:** What is the real problem? What are the pain points?
- **AI Suitability:** Is AI truly the right solution here? Or can it be solved more simply?
- **Success Indicators:** How do we measure whether we have solved the problem?

### Data Evaluation

An analysis of the required information across three dimensions:

#### Access

- **Question:** Are we legally permitted and technically able to access it?
- **Check:** Legal rights, APIs, databases, security

#### Quality

- **Question:** Is the data complete and consistent?
- **Check:** Completeness, accuracy, currency, duplicates

#### Relevance

- **Question:** Does the data contain the answer to the question?
- **Check:** Correlation with the objective, representativeness

### Risk Inventory

An initial scan for legal and ethical obstacles.

- **EU AI Act Classification:** Does the system fall under the high-risk category?
- **Privacy & GDPR:** Which personal data is being processed?
- **Ethical Questions:** Can the system discriminate or cause harm?
- **Organisational Risks:** Do we have the right people and resources?

______________________________________________________________________

## 1b. Project Type Classification

!!! info "Two project types at a glance"
    - **Type A — Building with AI**: The development team uses AI tools and agentic AI as part of the development process. The end product itself does not need to contain AI.
    - **Type B — AI in the Product**: The end product integrates AI functionality for end users.

Before proceeding with the core activities, determine the type of AI project. The Blueprint distinguishes two fundamentally different project types:

| Characteristic         | Type A — Building *with* AI                                                                                                                                               | Type B — AI *in* the product                                                                                            |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| **Description**        | AI/agents are used as development tools (code assistants, test generation, documentation automation)                                                                      | The end product contains AI capabilities for end users (recommendations, classification, generation, agentic workflows) |
| **Risk profile**       | Standard software risks; AI errors affect the development process, not the end user                                                                                       | AI-specific risks; errors directly affect end users, customers or business processes                                    |
| **Collaboration Mode** | Typically Mode 1–2 (the developer reviews AI output)                                                                                                                      | Mode 2–5 depending on risk and volume (full lifecycle required)                                                         |
| **Blueprint scope**    | Selective: use [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md), [Governance Model](../00-strategisch-kader/03-governance-model.md) and relevant cheatsheets | Full: all phases, Gate Reviews, Collaboration Modes and monitoring apply                                                |

!!! warning "This Blueprint is primarily designed for Type B projects"
    Type A projects (building *with* AI) may use selected modules but do not require the full lifecycle. Classify your project deliberately — a wrong classification leads to either unnecessarily heavy governance or insufficient safeguards.

**Not sure?** If the AI system generates output that is directly seen or used by end users without human intervention, it is a Type B project.

## 2. Team & Roles

| Role                    | Responsibility in Discovery                                           |
| :---------------------- | :-------------------------------------------------------------------- |
| **AI Product Manager**  | **A**ccountable: Owner of the business case and problem articulation. |
| **Data Scientist**      | **R**esponsible: Performing the Data Evaluation.                      |
| **Business Sponsor**    | **C**onsulted: Validates the problem and the value hypothesis.        |
| **Guardian (Ethicist)** | **C**onsulted: Conducts the initial ethical and legal scan.           |
| **Stakeholders**        | **I**nformed: Are kept informed of findings.                          |

______________________________________________________________________

## 5. Related Modules

**Templates:**

- [Project Charter](../09-sjablonen/01-project-charter/template.md)
- [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)
- [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)

**See also:** [Phase 1 Overview](01-doelstellingen.md) · [Deliverables](03-afleveringen.md)

______________________________________________________________________

**Next step:** Complete the Goal card and run the Collaboration Mode Assessment.
→ Use the [Project Charter](../09-sjablonen/01-project-charter/template.md) as your starting point.
→ See also: [Collaboration Mode Assessment](05-has-h-beoordeling.md) | [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)
