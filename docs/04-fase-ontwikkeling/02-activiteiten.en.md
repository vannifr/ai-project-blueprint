---
versie: '1.1'
---

# 1. Core Activities & Roles (Development)

## 1. Core Activities

### Automating Data Flows

Setting up pipelines that automatically clean and supply data (no more manual work).

- **Data Pipelines:** Automated ETL processes (Extract, Transform, Load)
- **Quality Controls:** Automatic validation of incoming data
- **Version Control:** Tracking of data changes and lineage

### Knowledge Coupling & Fine-Tuning

Connecting the AI to internal documents and **model fine-tuning** for optimal performance.

- **Knowledge Coupling:** Connecting the AI to internal documents, FAQs, procedures. Like this whole ai-delivery.io blueprint
- **Prompt Engineering:** Optimising the **Steering Instructions**.
- **Model Fine-Tuning:** Adjusting parameters for the specific use case.

### Specification-First Method

We write the expected outcome (the test) first, then the implementation. This ensures quality.

- **Test-Driven Development for AI:** First define what the system must do.
- **Acceptance Criteria:** Clear, measurable requirements per feature.
- **Automated Tests:** Continuous validation with every change.

### Variant: SaaS & Procurement (Buy vs. Build)

Not all AI solutions are built in-house. When purchasing standard AI software (SaaS), the focus of the Development phase changes:

- **From Building to Configuring:** Focus on setting up the right system prompts, knowledge coupling sources and safety filters within the vendor environment.
- **Validation Remains Identical:** Even a purchased tool must pass the **Validation Pilot** and **Golden Set** test before going live. Do not blindly trust the vendor's "demo".
- **Model Card becomes Configuration Card:** Document which settings, plugins and data connections are active.
- **Vendor Lock-in Check:** Verify that data and logs are exportable for compliance (EU AI Act).

______________________________________________________________________

### Validation at Three Levels

Every change is tested on three dimensions:

#### Syntactic

- **Question:** Does the code work? No crashes or errors?
- **Check:** Unit tests, integration tests

#### Technical Delivery & Pipelines

- **Data Pipelines:** Setting up robust flows for training and inference.
- **Automated Gates (Governance-as-Code):** Integrate the **Hard Boundaries** and success metrics directly into the CI/CD pipeline.
- *Example:* The build automatically fails if the bias score is too high or accuracy drops below the threshold.
- **Continuous Testing (CT):** Automated evaluation of model outputs with every change to the **Steering Instructions**.

______________________________________________________________________

#### Behavioural

- **Question:** Does it do what we expect?
- **Check:** Functional tests, regression tests

#### Goal-Aligned

- **Question:** Does it help the user? Does it deliver value?
- **Check:** User acceptance testing, A/B testing

## 2. Team & Roles

| Role                   | Responsibility in Development                                         |
| ---------------------- | --------------------------------------------------------------------- |
| **Data Scientist**     | **R**esponsible: Development of AI models and **Knowledge Coupling**. |
| **ML Engineer**        | **R**esponsible: Building data pipelines and infrastructure.          |
| **AI Product Manager** | **A**ccountable: Owner of the product backlog and prioritisation.     |
| **QA Engineer**        | **R**esponsible: Performing automated tests and validation.           |
| **DevOps**             | **C**onsulted: Advises on **Go-live** and infrastructure.             |

______________________________________________________________________

## 5. Related Modules

**Templates:**

- [Goal Definition](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)

**Further reading:**

- [Spec-Driven Development](../01-ai-native-fundamenten/06-specificatie-gedreven-ontwikkeling.md)
- [SDD Pattern](05-sdd-patroon.md)

**See also:** [Phase 3 Overview](01-doelstellingen.md) · [Deliverables](03-afleveringen.md)
