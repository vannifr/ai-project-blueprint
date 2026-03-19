---
versie: '1.1'
type: foundation
layer: 1
---

# 1. Specification-First Method

!!! abstract "Purpose"
    Description of the Specification-First Method (Spec-Driven Development) where expectations are formally recorded before building begins.

## 1. Shift-Left Validation

The **Specification-First Method** (also known as *Spec-Driven Development*) ensures that we record expectations before we build.

Instead of writing prompts directly, we follow this cycle:

1. **AI Product Manager** defines the **Goal Definition**.
1. **The team** (AI Engineer, Developer or prompt specialist) drafts the initial **Steering Instructions**.
1. The system generates a detailed **specification** of the expected behaviour.
1. **Human Review** of the specification: We validate the intent before spending resources on training or test runs.
1. The approved specification drives further development and automated validation.

For systems with a higher degree of autonomy, behaviour changes are implemented in small, bounded steps. The intent of the change, applicable boundaries and how to verify the change works correctly are all recorded upfront before it is permanently applied.

______________________________________________________________________

## 2. Related Templates

- [Goal Definition Template](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
