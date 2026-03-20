---
versie: '1.0'
type: template
layer: 3
phase: [2, 3]
roles: [Data Scientist]
tags: [template, validation]
answers: ['How do I use the Template: Validation Report template?']
---

# 1. Template: Validation Report

!!! warning "Outdated template"
    This is the **old** template for validation reporting. For new projects use the updated **[Validation Report](validatierapport.md)**.

## 1. Purpose

This template serves to record the test results of the **Validation Pilot**. It forms the objective evidence that the AI solution meets the established criteria and safety boundaries.

______________________________________________________________________

!!! note "Download this template"
    [Download as Markdown](https://github.com/vannifr/ai-project-blueprint/raw/main/docs/09-sjablonen/07-validatie-bewijs/template.en.md){ .md-button } — Open in your editor or AI assistant and fill in the fields.

### Test Setup

- **Date of the pilot:** \[DD-MM-YYYY\]
- **Model version:** \[E.g. GPT-4o with specific system prompts v1.2\]
- **Test set:** \[Description of the dataset or scenarios used\]

______________________________________________________________________

### Results (Metrics)

- **Accuracy / Relevance:** \[E.g. 92% of answers were correct according to the expert.\]
- **Hard Boundaries Check:**

1. Privacy: \[No PII detected in output\].
1. Safety: \[System successfully refused harmful prompts\].

- **User experience:** \[Feedback from the testers\].

______________________________________________________________________

### Conclusion

!!! check "Conclusion"
    - [ ] **Meets** the success criteria (>90%).
    - [ ] **Does not meet**. Adjustment of **System Prompts** required.

______________________________________________________________________
