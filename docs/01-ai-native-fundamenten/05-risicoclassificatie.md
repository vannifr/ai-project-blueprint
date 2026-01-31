# Risicoclassificatie

Niet elke wijziging vereist dezelfde diepgang van validatie. We classificeren wijzigingen op basis van risico (impact op *Constraints*).

| Niveau | Trigger (Voorbeeld) | Validatie Diepgang | EU AI Act Mapping |
| :--- | :--- | :--- | :--- |
| **Kritiek** (*Critical*) | Beveiliging, Financiële transacties, Regelgeving | Volledige Validatie + Constraint Verificatie | **Hoog Risico** (*High Risk*) |
| **Verhoogd** (*Elevated*) | PII (Privacy), Externe API's | Uitgebreide Behavioral + Intent Alignment | **Beperkt Risico** (*Limited Risk*) |
| **Matig** (*Moderate*) | Merkstem (Tone of Voice), UX SLA's | Minimale Behavioral + Intent Alignment | **Beperkt Risico** (*Limited Risk*) |
| **Laag** (*Low*) | Geen constraints geraakt | Syntactische + Minimale Behavioral | **Minimaal Risico** (*Minimal Risk*) |

---

© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.


