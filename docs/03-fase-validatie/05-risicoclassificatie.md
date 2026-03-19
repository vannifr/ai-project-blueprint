---
versie: '1.0'
type: guide
layer: 2
phase: [2]
roles: [AI Product Manager, Data Scientist, Guardian]
tags: [risk, validation]
---

# 1. Risicoclassificatie in Validatie

!!! abstract "Doel"
    Verfijning van het risicoprofiel tijdens de Validatiefase op basis van de werkelijkheid van het prototype.

Tijdens de Validatiefase wordt de initiële risicoclassificatie uit Discovery getoetst aan de werkelijkheid van het prototype.

## 1. Verfijning van het Risicoprofiel

Op basis van de PoC resultaten moet het project worden ingedeeld volgens de kaders in [Risicoclassificatie](../01-ai-native-fundamenten/05-risicoclassificatie.md).

### Aandachtspunten:

- **Data Impact:** Verwerkt de AI in de praktijk meer gevoelige data dan voorzien?
- **Beslissingsimpact:** Hoe groot is de werkelijke invloed van de AI op de eindgebruiker? (Cruciaal voor EU AI Act *High Risk* bepaling).
- **Technische Stabiliteit:** Hoe vaak treden hallucinaties of fouten op die een risico kunnen vormen?

## 2. Mapping op EU AI Act

Controleer of de *gebruikscasus* na de PoC nog steeds in dezelfde categorie valt:

- **Unacceptable Risk:** Stop het project onmiddellijk.
- **High Risk:** Start het volledige conformiteitstraject (zie Compliance Hub).
- **Limited/Minimal Risk:** Ga door met standaard kwaliteitsborging.

______________________________________________________________________

**Volgende stap:** Verfijn het risicoprofiel en documenteer het in de [Risicoanalyse](../09-sjablonen/03-risicoanalyse/template.md)
→ Zie ook: [EU AI Act classificatie](../07-compliance-hub/01-eu-ai-act/index.md)
