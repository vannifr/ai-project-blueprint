---
versie: '1.0'
description: 'AI risk inventory template: systematically identify, classify, and mitigate technical, ethical, and compliance risks in your AI project — based on EU AI Act risk categories.'
---

# 1. Template: Risk Inventory

## 1. Purpose

Identifying and assessing risks in the areas of technology, organisation and compliance (EU AI Act).

______________________________________________________________________

### Risk Classification

*Choose the category according to the EU AI Act:*

- [ ] **Unacceptable:** (PROHIBITED)
- [ ] **High Risk:** (Requires technical dossier & human oversight)
- [ ] **Limited Risk:** (Transparency obligation)
- [ ] **Minimal Risk:** (No specific requirements)

______________________________________________________________________

### Assessment Against Hard Boundaries

*Which hard limits must not be crossed?*

1. **Privacy:** \[Risk of leaking PII\].
1. **Safety:** \[Risk of harmful outputs\].
1. **Bias:** \[Risk of unequal treatment\].

______________________________________________________________________

### Mitigation Plan

*How do we reduce risks to an acceptable level?*

- **Technical:** \[E.g. Filters on output, anonymising input\].
- **Procedural:** \[E.g. The Guardian performs spot checks\].

______________________________________________________________________

### Sustainability trigger

- [ ] **Scale trigger:** Does the system require continuous large-scale inference (>1,000 calls/day)?
    - Yes → refer to the [Green AI standard](../../08-technische-standaarden/index.md) and complete the Environmental Footprint field in the Business Case as mandatory.
    - No → no further action required.

______________________________________________________________________
