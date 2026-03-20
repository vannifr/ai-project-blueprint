---
versie: '1.1'
type: foundation
layer: 1
roles: [Guardian]
tags: [risk]
summary: Classificatie van wijzigingen op basis van impact, zodat de juiste validatiediepgang wordt toegepast in lijn met de EU AI Act.
answers: [Wat houdt Risicoclassificatie in?, Hoe classificeer ik het risico van mijn AI-project?]
---

# 1. Risicoclassificatie

!!! abstract "Doel"
    Classificatie van wijzigingen op basis van impact, zodat de juiste validatiediepgang wordt toegepast in lijn met de EU AI Act.

## 1. Validatie Diepgang

Niet elke wijziging vereist dezelfde diepgang van validatie. We classificeren wijzigingen op basis van de impact op de **Harde Grenzen**.

| Niveau       | Trigger (Voorbeeld)                                    | Validatie Diepgang                              | EU AI Act Mapping   |
| :----------- | :----------------------------------------------------- | :---------------------------------------------- | :------------------ |
| **Kritiek**  | Beveiliging, Financiële transacties, Gezondheidsadvies | Volledige Validatie + **Rode Lijn** Verificatie | **Hoog Risico**     |
| **Verhoogd** | Persoonsgegevens (PII), Externe API-koppelingen        | Uitgebreide Gedrags- + Doelgerichtheidtoets     | **Beperkt Risico**  |
| **Matig**    | Schrijfstijl (Tone of Voice), UX-wijzigingen           | Minimale Gedrags- + Doelgerichtheidtoets        | **Beperkt Risico**  |
| **Laag**     | Geen **Harde Grenzen** geraakt                         | Syntactische + Minimale Gedragscheck            | **Minimaal Risico** |

______________________________________________________________________

## 2. Gerelateerde Modules

- [Validatie Model](04-validatie-model.md)
- [Bewijsstandaarden](07-bewijsstandaarden.md)
- [Valkuilencatalogus](../17-bijlagen/valkuilen-catalogus.md)
- [EU AI Act](../07-compliance-hub/01-eu-ai-act/index.md)

______________________________________________________________________
