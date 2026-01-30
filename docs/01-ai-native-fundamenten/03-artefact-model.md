# Artefact Model

In *AI-Native* projecten beheren we specifieke artefacten om grip te houden op het onvoorspelbare karakter van AI.

| Artefact | Doel | Eigenaar | Formaat |
| :--- | :--- | :--- | :--- |
| **Intent Record** | **Business hypothese:** Welke uitkomst wordt nagestreefd? | Intent Owner | Gestructureerde statement ("Gegeven X, als Y, dan Z") |
| **Constraints Record** | **Harde grenzen:** Wat mag NOOIT gebeuren? | Risk Officer | IF/THEN regels ("ALS PII, DAN blokkeren") |
| **Context Artifacts** | **Sturing:** De executabele configuratie (prompts, tools). | Context Steward | Versiebeheerde config (JSON/YAML) |
| **Change Set** | **Implementatie:** De wijziging zelf. | Delivery Lead | Git commit diff |
| **Validation Evidence** | **Bewijs:** Resultaten van testen. | Delivery Lead | Gestructureerd log |
| **Trace Links** | **Verbinding:** Intent â†” Change â†” Evidence. | Delivery Lead | Referenties (ID's) |

---

Â© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.

