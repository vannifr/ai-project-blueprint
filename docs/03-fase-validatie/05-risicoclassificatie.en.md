---
versie: '1.1'
type: guide
layer: 2
phase: [2]
roles: [AI Product Manager, Data Scientist, Guardian]
tags: [risk, validation]
---

# 1. Risk Classification in Validation

!!! abstract "Purpose"
    Refinement of the risk profile during the Validation phase based on the reality of the prototype.

During the Validation phase, the initial risk classification from Discovery is tested against the reality of the prototype.

## 1. Refining the Risk Profile

Based on the PoC results, the project must be classified according to the frameworks in [Risk Classification](../01-ai-native-fundamenten/05-risicoclassificatie.md).

### Key considerations:

- **Data Impact:** Does the AI process more sensitive data in practice than originally anticipated?
- **Decision Impact:** How significant is the actual influence of the AI on the end user? (Crucial for EU AI Act *High Risk* determination).
- **Technical Stability:** How often do hallucinations or errors occur that could pose a risk?

## 2. Mapping to the EU AI Act

Verify whether the *use case* still falls within the same category after the PoC:

- **Unacceptable Risk:** Stop the project immediately.
- **High Risk:** Start the full conformity process (see Compliance Hub).
- **Limited/Minimal Risk:** Continue with standard quality assurance.

______________________________________________________________________

**Next step:** Refine the risk profile and document it in the [Risk Analysis](../09-sjablonen/03-risicoanalyse/template.md)
→ See also: [EU AI Act classification](../07-compliance-hub/01-eu-ai-act/index.md)
