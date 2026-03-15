---
versie: '1.0'
description: 'Roles and responsibilities in AI projects: AI Project Manager, Data Scientist, Domain Expert, Guardian, and more — with RACI matrix and accountability per lifecycle phase.'
type: index
layer: 1
---

# 1. Roles & Responsibilities

## 1. Who Does What in an AI Project?

In AI projects the boundaries between business and IT blur. That is why we define roles based on responsibility, not job title.

______________________________________________________________________

## 2. The Core Team (The Squad)

These people work on the project daily and are the engine of innovation.

### The AI Product Manager (Business Lead)

Not just a Product Owner. The AI PM understands not only the customer need, but also what is technically feasible with AI (and what is not).

- **Responsibility:** The **Objective Card**.
- **Task:** Translates vague business wishes into sharp AI instructions. Manages the backlog and prioritises on value.
- **Focus:** "Are we solving the right problem?"

### The Tech Lead (Technical Lead)

The architect of the solution. Ensures that the separate components (data, model, interface) work together seamlessly.

- **Responsibility:** The **Technical Model Card**.
- **Task:** Selects the right model, builds the pipelines and safeguards technical stability.
- **Focus:** "Is it robust and scalable?"

### The Guardian (Role & Responsibilities)

The 'Guardian' is not a single job title, but a role with veto rights that guards the ethical and legal frameworks. Given the complexity, this role is in practice often fulfilled by a duo ("Two-man rule"):

- **Privacy & Legal Officer:** Tests against GDPR, EU AI Act and legal risks. Focus: *Is this legally permitted?*
- **AI Quality Ethicist (or QA Lead):** Tests for bias in the dataset, quality of the Golden Set and output safety. Focus: *Is this fair and safe?*

For projects with a **High Risk** classification, explicit approval from both is required at Gate Reviews. For small projects one person can carry the role, provided sufficient mandate.

- **Responsibility:** The **Risk Pre-Scan**.
- **Focus:** "Is it safe and fair?"

______________________________________________________________________

## 3. Supporting Roles

These specialists are brought in when the specific phase requires them.

| Role                    | Focus          | Task                                                                                    |
| :---------------------- | :------------- | :-------------------------------------------------------------------------------------- |
| **Data Engineer**       | Data quality   | The backbone of the data. Ensures data arrives clean at the model.                      |
| **AI Tester (QA)**      | Reliability    | Specialist in 'breaking' AI via *Adversarial Testing*.                                  |
| **Adoption Manager**    | Change         | Ensures people actually use the tool (ADKAR model).                                     |
| **Context Builder**     | Knowledge mgmt | Manages what the model sees at every moment — see extension below.                      |
| **AI Security Officer** | Security       | Focuses on LLM vulnerabilities, data poisoning and AI governance — see extension below. |

______________________________________________________________________

### Context Builder

The industry is shifting from *prompt engineering* (writing instructions) to **context engineering** (managing what the model sees at every moment). The Context Builder acts as a digital librarian: gathering relevant information from hundreds of files and real-time data streams, summarising it, and archiving it in a hierarchical knowledge base that transcends the LLM's context limits.

**Core responsibilities:**

- Designing and maintaining the RAG architecture (Retrieval-Augmented Generation)
- Preventing *context pollution* — more context is not always better; irrelevant information degrades model performance
- Reducing usage costs through targeted information retrieval (significantly cheaper than sending full context to the model)
- Guarding the Context Development Lifecycle: which information is current, which is outdated?

**When to deploy:** mandatory for RAG systems or when the model has access to more than one knowledge source. Can be a human role or an automated agentic component.

Source: \[so-44\]

______________________________________________________________________

### AI Security Officer

As AI systems become more critical, traditional security roles are no longer sufficient. The AI Security Officer focuses specifically on threats unique to ML systems.

**Core responsibilities:**

- Threat modelling based on the [OWASP Top 10 for LLMs](../07-compliance-hub/07-red-teaming.md)
- Executing or coordinating Red Teaming sessions
- Managing AI governance frameworks (EU AI Act Art. 9, NIST AI RMF \[so-50\])
- Responding to AI-specific incidents: model poisoning, prompt injection, bias escalations

**Certification:** ISACA introduced the **AAISM** (Advanced in AI Security Management) in August 2025 — the world's first AI-centred security management qualification, specifically focused on LLM vulnerabilities and AI governance.

Source: \[so-45\]

______________________________________________________________________

## 4. Strategic Level (Steering Committee)

### Chief AI Officer (CAIO)

Programme sponsor. Determines the overarching strategy and allocates budget.

- **Task:** Decides at the **Gates** whether a project continues or stops.
- **Ownership:** Guards the entire portfolio and the AI maturity of the organisation.
