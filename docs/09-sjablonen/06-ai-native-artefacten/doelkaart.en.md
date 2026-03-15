---
versie: '1.0'
type: template
layer: 3
phase: [1, 2, 3]
tags: [template]
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

- **Primary Sources:** \[Company information/Manuals for the **RAG** knowledge base.\]
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

### E. Assumptions

*What assumptions underlie this project? Document the key assumptions and their validation status. Test the riskiest assumption first.*

| Category       | Assumption                                           | Impact if wrong     | Evidence                  | Status                             |
| :------------- | :--------------------------------------------------- | :------------------ | :------------------------ | :--------------------------------- |
| **Data**       | \[E.g. Sufficient representative data is available\] | \[High/Medium/Low\] | \[What evidence exists?\] | \[Open / Validated / Invalidated\] |
| **Model**      | \[E.g. Model generalises to production data\]        | \[High/Medium/Low\] | \[What evidence exists?\] | \[Open / Validated / Invalidated\] |
| **Adoption**   | \[E.g. Users trust and use the output correctly\]    | \[High/Medium/Low\] | \[What evidence exists?\] | \[Open / Validated / Invalidated\] |
| **Cost**       | \[E.g. Usage costs remain manageable at scale\]      | \[High/Medium/Low\] | \[What evidence exists?\] | \[Open / Validated / Invalidated\] |
| **Ethics**     | \[E.g. Training data contains no systematic bias\]   | \[High/Medium/Low\] | \[What evidence exists?\] | \[Open / Validated / Invalidated\] |
| **Regulatory** | \[E.g. Approach remains EU AI Act compliant\]        | \[High/Medium/Low\] | \[What evidence exists?\] | \[Open / Validated / Invalidated\] |

- **Riskiest assumption:** \[Which assumption kills the project if it turns out to be wrong?\]
- **Validation approach:** \[How will we test this? Reference an Experiment Ticket if applicable.\]
- **Owner:** \[Who is responsible for validating the critical assumptions?\]
- **Re-assessment date:** \[When will assumptions be re-evaluated?\]

______________________________________________________________________

### F. Green AI & Sustainability

*How do we limit the ecological footprint of this system?*

- **Is AI proportionate?** Does the value creation outweigh the energy cost? \[Yes / No / Explanation\]
- **Smaller model possible?** Can a smaller, specialised model perform the task? \[Yes / No / Motivation\]
- **Green infrastructure?** Does the system run on a cloud provider using renewable energy? \[Provider + certification\]
- **E-waste plan?** Is there a plan for hardware lifecycle and replacement? \[Yes / No / Reference\]

See: [Green AI & Sustainability](../../08-technische-standaarden/08-green-ai.en.md)

______________________________________________________________________

### Approval by Guardian

**Name:** \[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\]

______________________________________________________________________
