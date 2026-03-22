---
versie: '1.0'
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [Data Scientist]
tags: [quick-reference]
answers: [Wat is de snelle referentie voor Cheatsheet — Golden Set?]
---

# Cheatsheet — Golden Set

**Bron:** [Validatierapport](../07-validatie-bewijs/validatierapport.md)

______________________________________________________________________

## Wat is een Golden Set?

Een **Golden Set** is een vaste verzameling van input-output-paren met bekende, correcte antwoorden. Het is de meetlat voor de kwaliteit van uw AI-systeem.

______________________________________________________________________

## Minimale Samenstelling

| Criterium                 | Minimale waarde | Aanbevolen        |
| :------------------------ | :-------------- | :---------------- |
| Aantal voorbeelden        | 50              | 200+              |
| Dekking van use cases     | 80%             | 100%              |
| Randgevallen (edge cases) | 10% van set     | 20%               |
| Beoordelaars per item     | 1               | 2–3 (inter-rater) |
| Updatefrequentie          | Bij modelwissel | Kwartaal          |

______________________________________________________________________

## Opbouw in 4 Stappen

```
1. Verzamel echte gebruikersvragen (of synthetisch indien geen data)
2. Laat domeinexperts de correcte output vaststellen
3. Categoriseer per use case + moeilijkheidsgraad
4. Vergrendel de set — wijzig alleen via formeel proces
```

______________________________________________________________________

## Kwaliteitsdrempels

| Metric                                                                           | Drempelwaarde (Go) | Actie bij mislukken                |
| :------------------------------------------------------------------------------- | :----------------- | :--------------------------------- |
| Accuracy (classificatie)                                                         | ≥ 85%              | Hertraining of promptoptimalisatie |
| F1-score                                                                         | ≥ 0.80             | Controleer klasse-imbalans         |
| Menselijke beoordeling                                                           | ≥ 4.0/5.0          | Review promptontwerp               |
| Hallucination rate                                                               | ≤ 5%               | RAG-kwaliteit verbeteren           |
| Latency p95 (95e percentiel — 95% van alle verzoeken is sneller dan deze waarde) | ≤ \[budget\] ms    | Model tiering overwegen            |

______________________________________________________________________

## Valkuilen

!!! warning "Vermijd deze fouten"
    - Golden Set gebruiken als **trainingsdata** (contamination)
    - Set niet updaten na **domeinwijziging** (concept drift)
    - Enkel happy-path-gevallen opnemen (geen edge cases)
    - Eén beoordelaar per item (geen inter-rater agreement)

**Bron volledige aanpak:** [Validatierapport template](../07-validatie-bewijs/validatierapport.md)
