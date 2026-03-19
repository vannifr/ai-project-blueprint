---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
tags: [quick-reference, risk]
---

# Cheatsheet — Risk Pre-Scan

**Bron:** [Risk Pre-Scan Template](../03-risicoanalyse/pre-scan.md)

______________________________________________________________________

## De 5 Snelle Risikovragen

| #   | Vraag                                                         | Hoog-risico indicator     |
| :-- | :------------------------------------------------------------ | :------------------------ |
| 1   | Neemt het systeem beslissingen die mensen direct beïnvloeden? | Ja → Hoog                 |
| 2   | Verwerkt het persoons- of gezondheidsgegevens?                | Ja → minstens Beperkt     |
| 3   | Is de output zichtbaar voor externe gebruikers?               | Ja → verhoogd risico      |
| 4   | Wat is de impact als het systeem fout zit?                    | Groot/onomkeerbaar → Hoog |
| 5   | Is er menselijk toezicht op elke output?                      | Nee → risicoverhoging     |

______________________________________________________________________

## Risicomatrix (Snel Oordeel)

```
               IMPACT VAN FOUT
               Klein    Groot
KANS FOUT   ┌────────┬────────┐
Laag        │  Groen │  Geel  │
            ├────────┼────────┤
Hoog        │  Geel  │  Rood  │
            └────────┴────────┘
```

- **Groen** → Doorgaan, standaard monitoring
- **Geel** → Extra mitigatie definiëren
- **Rood** → Escaleer naar Guardian; overweeg herontwerp

______________________________________________________________________

## Top 5 AI-risico's om te Checken

| Risico              | Signaal                                 | Mitigatie                         |
| :------------------ | :-------------------------------------- | :-------------------------------- |
| **Hallucinations**  | Feitelijke output zonder bronvermelding | RAG + bronvermelding verplicht    |
| **Bias**            | Gebruikersgroepen ongelijk behandeld    | Fairness audit in testset         |
| **Privacy-lekkage** | PII in prompts of outputs               | Data-minimalisatie + filtering    |
| **Vendor lock-in**  | Afhankelijkheid één API-provider        | Abstractielaag + alternatief      |
| **Scope creep**     | Systeem doet meer dan goedgekeurd       | Harde Grenzen technisch afdwingen |

______________________________________________________________________

## Uitkomst Pre-Scan

- **≤ 2 risico's Geel, geen Rood** → Ga naar Gate 1
- **≥ 3 Geel of 1 Rood** → Volledige risicoanalyse vereist eerst
- **Hoog Risico classificatie** → EU AI Act-traject verplicht

**Bron volledige aanpak:** [Risicoanalyse](../03-risicoanalyse/template.md) | [EU AI Act](../../07-compliance-hub/01-eu-ai-act/index.md)
