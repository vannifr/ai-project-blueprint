---
versie: '1.0'
type: template
layer: 3
phase: [2]
roles: [AI Product Manager, Business Sponsor, Data Scientist]
tags: [governance, template]
answers: [How do I use the Technical Model Card template?]
---

# 1. Technical Model Card

## 1. Purpose

This template is intended for developers and auditors. It documents the technical specifications, training data and performance of the model and travels from **Development** to **Management & Optimisation**.

______________________________________________________________________

**Model Name:** \[E.g. Customer-Service-Bot-v2\]
**Type:** \[E.g. LLM (GPT-4o) with RAG\]

______________________________________________________________________

### Purpose & Limitations

- **Primary Use:** \[What is this model intended for?\]
- **Out of Scope:** \[What must this model NOT be used for?\]
- **Collaboration Mode:** \[E.g. Mode 3: Collaborative\]

______________________________________________________________________

### Technical Specifications

- **Base Model (Foundation):** \[E.g. Azure OpenAI GPT-4\]
- **Parameters:** \[E.g. Temperature: 0.7, TopP: 0.9\]
- **Knowledge Coupling (RAG):**
- **Source:** \[E.g. SharePoint folder 'Knowledge Management'\]
- **Update frequency:** \[Weekly / Real-time\]

______________________________________________________________________

### Training & Data

- *Only complete if fine-tuning or own training is involved.*
- **Training data:** \[Dataset description\]
- **Period:** \[Data from YYYY to YYYY\]
- **Data Evaluation:** \[Reference to quality report\]

______________________________________________________________________

### Performance & Validation

*Results extracted from the **Validation Report** (Phase 3).*

- **Metrics:**
- **Accuracy:** \[X%\]
- **Hallucination rate:** \[\< X%\]
- **Test set:** \[Description of the questions or scenarios used\]

______________________________________________________________________

### Ethical Considerations

- **Known Limitations:** \[E.g. "Model struggles with jargon in language X".\]
- **Bias Mitigation:** \[What steps have been taken to reduce bias?\]

______________________________________________________________________

### Management & Maintenance

- **Owner (Tech):** \[Name Tech Lead\]
- **Owner (Business):** \[Name Product Owner\]
- **Performance Degradation Monitoring:** \[Which tool measures the **Performance Degradation**?\]

______________________________________________________________________

### Version Control

- **v1.0:** Initial Release (Name Developer)
- **v1.1:** Prompt update after feedback (Name Developer)

______________________________________________________________________
