---
versie: '1.0'
---

# 1. The Objective Card (Intent Map)

## 1. Purpose

The Objective Card formalises the **Objective Definition** of the AI project. This document connects human intent to the technical **System Prompts** and serves as the source from which the AI solution is generated.

______________________________________________________________________

**Project:** \[Project Name\]

______________________________________________________________________

### A. The Intent (Human Intent)

*What is the user trying to achieve and how should the AI behave?*

- **The User (Persona):** Who are they? \[E.g. A junior legal employee.\]
- **The Goal:** What do they want to achieve? \[Quickly find the risks in a contract.\]
- **The AI (System Persona):**
- **Role:** \[E.g. An experienced senior lawyer and mentor.\]
- **Tone:** \[Professional, sharp, but helpful. No jargon without explanation.\]
- **The Task:** \[Describe exactly what the AI must do. E.g: "Scan the uploaded PDF document for liability clauses and summarise them."\]

______________________________________________________________________

### B. System Prompts (Context)

*What knowledge does the AI need to do this?*

- **Primary Sources:** \[Company information/Manuals for the **Knowledge Coupling**.\]
- **Examples (Few-Shot):**
- **Input:** \[Example of a vague clause.\]
- **Desired Output:** \[How the AI should have interpreted/improved it.\]
- *(Add at least 3 good examples to guide the behaviour).*

______________________________________________________________________

### C. Hard Boundaries (Constraints)

*What must the AI absolutely not do? These are the hard safety rules.*

- **Safety:** \[E.g. Never give legal advice on criminal law.\]
- **Format:** \[E.g. Response may never be longer than 2 paragraphs.\]
- **Behaviour / Conviction:** \[E.g. Do not fabricate facts. If it is not in the sources, say: "I don't know".\]

______________________________________________________________________

### D. Assessment (Evidence)

*How do we prove that the Objective Card works? This is the input for the **Validation Report**.*

- **Test prompt 1 (Success case):** \[Question the AI must answer correctly.\]
- **Test prompt 2 (Adversarial):** \[Question that tries to make the AI hallucinate or cross the **Hard Boundaries**.\]
- **Acceptance score:** \[Minimum score (e.g. 8 on relevance) or percentage.\]

______________________________________________________________________

### Approval by Guardian

**Name:** \[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\]

______________________________________________________________________
