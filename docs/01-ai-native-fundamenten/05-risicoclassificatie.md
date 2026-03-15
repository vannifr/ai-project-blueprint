---
versie: '1.0'
type: foundation
layer: 1
roles: [Guardian]
tags: [risk]
---

# 1. Risicoclassificatie

## 1. Validatie Diepgang

Niet elke wijziging vereist dezelfde diepgang van validatie. We classificeren wijzigingen op basis van de impact op de **Rode Lijnen**.

| Niveau       | Trigger (Voorbeeld)                                    | Validatie Diepgang                              | EU AI Act Mapping   |
| :----------- | :----------------------------------------------------- | :---------------------------------------------- | :------------------ |
| **Kritiek**  | Beveiliging, Financiële transacties, Gezondheidsadvies | Volledige Validatie + **Rode Lijn** Verificatie | **Hoog Risico**     |
| **Verhoogd** | Persoonsgegevens (PII), Externe API-koppelingen        | Uitgebreide Gedrags- + Doelgerichtheidtoets     | **Beperkt Risico**  |
| **Matig**    | Schrijfstijl (Tone of Voice), UX-wijzigingen           | Minimale Gedrags- + Doelgerichtheidtoets        | **Beperkt Risico**  |
| **Laag**     | Geen **Rode Lijnen** geraakt                           | Syntactische + Minimale Gedragscheck            | **Minimaal Risico** |

______________________________________________________________________

## 2. Gerelateerde Modules

- [Validatie Model](04-validatie-model.md)
- [Bewijsstandaarden](07-bewijsstandaarden.md)
- [Valkuilencatalogus](../17-bijlagen/valkuilen-catalogus.md)
- [EU AI Act](../07-compliance-hub/01-eu-ai-act/index.md)

______________________________________________________________________
