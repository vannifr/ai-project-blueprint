---
versie: '1.0'
---

# 1. Risk Classification in Validation

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
