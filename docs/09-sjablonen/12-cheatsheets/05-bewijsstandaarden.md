---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
tags: [quick-reference, validation]
---

# Cheatsheet — Bewijsstandaarden

**Bron:** [Bewijsstandaarden](../../01-ai-native-fundamenten/07-bewijsstandaarden.md)

______________________________________________________________________

## Bewijsniveaus

| Niveau                | Beschrijving                                 | Voorbeeld                                 |
| :-------------------- | :------------------------------------------- | :---------------------------------------- |
| **L1 — Claim**        | Bewering zonder onderbouwing                 | "Het model is accuraat"                   |
| **L2 — Indicatie**    | Enkelvoudige meting of anekdote              | Één testresultaat                         |
| **L3 — Bewijs**       | Herhaalbare meting op representatieve set    | Golden Set score op 200 items             |
| **L4 — Sterk Bewijs** | Meerdere methoden, onafhankelijk gevalideerd | Golden Set + menselijke review + A/B-test |

**Minimale eis voor Gate 2:** niveau L3 of hoger.

______________________________________________________________________

## Vereist Bewijs per Artefact

| Artefact                 | Minimaal niveau | Methode                                                                                         |
| :----------------------- | :-------------- | :---------------------------------------------------------------------------------------------- |
| Outputkwaliteit          | L3              | Golden Set + geautomatiseerde metric                                                            |
| Fairness                 | L3              | Gesegmenteerde analyse per groep                                                                |
| Veiligheid (Hoog Risico) | L4              | Red Teaming + onafhankelijke review                                                             |
| Latency                  | L3              | Load test (p95, p99) (p95 = 95e percentiel — 95% van alle verzoeken is sneller dan deze waarde) |
| Kostenprognose           | L2              | Calculator + aannames gedocumenteerd                                                            |
| Traceerbaarheid          | L3              | Audit trail gedemonstreerd                                                                      |

______________________________________________________________________

## Bewijsdocumentatie

Elk bewijs moet minimaal bevatten:

- **Wat** is gemeten (metric, definitie)
- **Hoe** gemeten (methode, tool)
- **Wanneer** gemeten (datum, versie)
- **Door wie** beoordeeld (beoordelaar, onafhankelijkheid)
- **Resultaat** (getal + vergelijking met drempelwaarde)

______________________________________________________________________

## Veelgemaakte Fouten

!!! warning "Onvoldoende bewijs"
    - Metric gemeten op trainingsdata i.p.v. onafhankelijke testset
    - Geen baseline gedefinieerd ("beter dan voorheen" is geen bewijs)
    - Enkel positieve resultaten gerapporteerd (cherry picking)
    - Evaluatie uitgevoerd door ontwikkelteam zelf (geen onafhankelijkheid)

**Bron:** [Bewijsstandaarden](../../01-ai-native-fundamenten/07-bewijsstandaarden.md) | [Validatierapport](../07-validatie-bewijs/validatierapport.md)
