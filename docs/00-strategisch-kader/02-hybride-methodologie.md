---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# 1. Hybride Methodologie

## 1. Doel

Dit document beschrijft de hybride aanpak van de AI Project Gids, waarbij voorspelbare planning (Waterfall) wordt gecombineerd met iteratieve uitvoering (Agile) voor een optimale balans tussen structuur en flexibiliteit.

______________________________________________________________________

## 2. Concept

De hybride methodologie erkent dat AI-projecten enerzijds strikte mijlpalen vereisen voor budgettering en compliance, en anderzijds extreme flexibiliteit nodig hebben tijdens de modelontwikkeling.

### Voorspelbare Elementen (Waterfall)

- Strategische planning en **Het Kostenoverzicht**.
- Compliance en governance checkpoints.
- Risico-inventarisatie.
- Mijlpaal planning (**Gates**).

### Iteratieve Elementen (Agile)

- **Afstellen van het model** en tuning.
- User feedback loops.
- *Experiment-driven development*.
- Continue verbetering (*Kaizen*).

______________________________________________________________________

## 3. Praktische Implementatie

```mermaid
gantt
    title Hybride Methodologie
    dateFormat  YYYY-MM-DD
    section Voorspelbaar
    Verkenning & Strategie     :p1, 2024-01-01, 2w
    Het Kostenoverzicht          :p2, after p1, 1w
    section Iteratief
    Realisatie Sprints 1-4     :s1, after p2, 4w
    section Voorspelbaar
    Gate 3 (Productie-klaar) Review              :m1, after s1, 1w
    section Iteratief
    Realisatie Sprints 5-8     :s2, after m1, 4w
```

______________________________________________________________________

## 4. Voordelen

- **Structuur:** Duidelijke planning en governance voor management.
- **Flexibiliteit:** Snelle aanpassing aan nieuwe data-inzichten voor het team.
- **Risicobeheer:** Proactieve risico-identificatie en mitigatie.
- **Compliance:** Geïntegreerde EU AI Act compliance reviews.

______________________________________________________________________
