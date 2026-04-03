---
versie: '1.1'
type: compliance
layer: 3
roles: [Data Scientist, Guardian]
tags: [eu-ai-act, validation]
summary: Specificatie van de eisen waaraan een Validatierapport moet voldoen voor formeel akkoord op ingebruikname vanuit wettelijk en ethisch perspectief.
answers: [Wat zijn de compliance-eisen voor Validatie Eisen (Compliance)?, Hoeveel validatie is voldoende?]
sources:
  - id: eu-ai-act
    ref: Verordening (EU) 2024/1689 — EU AI Act (Art. 9, 10, 17)
    url: https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32024R1689
    date_verified: '2025-03-20'
    next_review: '2026-01-01'
  - id: iso-42001
    ref: ISO/IEC 42001:2023 — AI Management System Standard (sectie 9)
    url: https://www.iso.org/standard/81230.html
    date_verified: '2025-03-20'
    next_review: '2027-01-01'
    notes: ISO-normen worden doorgaans elke 5 jaar herzien.
---

# 1. Validatie Eisen (Compliance)

!!! abstract "Doel"
    Specificatie van de eisen waaraan een Validatierapport moet voldoen voor formeel akkoord op ingebruikname vanuit wettelijk en ethisch perspectief.

## 1. Doel

Vaststellen waaraan een **Validatierapport** moet voldoen om formeel akkoord te krijgen voor ingebruikname, specifiek gericht op wettelijke en ethische kaders.

______________________________________________________________________

## 2. Vereisten voor het Validatierapport

1. **Objectiviteit:** Gebruik van meetbare metrics en onafhankelijke testsets.
1. **Dekking:** Bewijs van toetsing op alle gedefinieerde **Harde Grenzen**.
1. **Traceerbaarheid:** Directe koppeling tussen de **Doeldefinitie**, de gebruikte data en de testresultaten.
1. **Eerlijkheid:** Rapportage over de uitgevoerde **Fairness audit (bias audit)**.
1. **Stabiliteit:** Bewijs van robuustheid tegen afwijkende invoer of pogingen tot manipulatie.

## 3. Gerelateerde sjablonen

- [Validatierapport sjabloon](../09-sjablonen/07-validatie-bewijs/validatierapport.md) — Gebruik dit sjabloon om het Validatierapport op te stellen.
- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md) — Welke bewijslast per risiconiveau?
