---
versie: '1.0'
type: technical
layer: 3
roles: [Tech Lead]
tags: [cost]
---

# Green AI & Duurzaamheid

AI-systemen hebben een substantiële ecologische voetafdruk. De elektriciteitsvraag voor AI-rekenkracht groeit snel: verwacht wordt dat deze in 2030 **11 keer hoger** ligt dan in 2023. Voor projectmanagers is duurzaamheid daarom geen bijzaak, maar een strategische beslissing die al in de Business Understanding fase moet worden genomen.

!!! info "Waarom nu?"
    Stijgende energieprijzen maken duurzame keuzes ook financieel aantrekkelijk. Energiezuinige modellen en slimme planning zijn niet alleen goed voor het klimaat — ze verlagen direct de operationele kosten.

Bronnen: \[so-47\], \[so-48\]

______________________________________________________________________

## 1. De Ecologische Voetafdruk van AI

### Energie

- Een gemiddelde ChatGPT-query verbruikt circa **0,34 Wh** elektriciteit — 5 tot 10 keer meer dan een standaard zoekopdracht (juni 2025).
- Het trainen van een groot taalmodel stoot meer dan **493 ton CO₂** uit — vergelijkbaar met honderden vluchten.
- Datacenters zijn verantwoordelijk voor circa **2% van de wereldwijde broeikasgasuitstoot**.

### Water

- Voor elke kilowattuur die een datacenter verbruikt, is circa **2 liter water** nodig voor koeling.
- Tegen 2030 zal het waterverbruik door datacenters naar verwachting verdrievoudigen tot **664 miljard liter per jaar**.

### Hardware

- Snelle hardware-verversing leidt tot grote hoeveelheden e-waste met gespecialiseerde metalen die moeilijk te recyclen zijn.

Bronnen: \[so-47\], \[so-48\]

______________________________________________________________________

## 2. Reductiepotentieel

Onderzoek van Cornell University (2025) toont aan dat de ecologische impact van AI drastisch kan worden verminderd door twee maatregelen te combineren:

| Maatregel                                                                    | CO₂-reductie      | Waterreductie     |
| :--------------------------------------------------------------------------- | :---------------- | :---------------- |
| Smart siting (datacenters in regio's met lage waterstress en groene energie) | tot 73%           | tot 86%           |
| Grid-decarbonisatie (overstap op hernieuwbare energiebronnen)                | aanvullend effect | aanvullend effect |

Bron: \[so-47\]

______________________________________________________________________

## 3. Praktische Maatregelen per Projectfase

### Fase 1 — Verkenning & Strategie

**Modelselectie als duurzaamheidsoverweging:**

- Kies voor "lean" modellen of *knowledge distillation* (kennis overdragen van een groot naar een klein model) wanneer de taak dit toelaat. Dit kan de operationele uitstoot met **tot 80%** verlagen.
- Documenteer de keuze voor een specifiek model inclusief de motivatie voor de modelgrootte in de [Technische Modelkaart](../09-sjablonen/02-business-case/modelkaart.md).

**Vragen bij modelselectie:**

- [ ] Is een kleiner gespecialiseerd model voldoende voor deze taak?
- [ ] Biedt de vendor transparantie over energieverbruik en datacenterlocatie?
- [ ] Zijn er alternatieven met vergelijkbare prestaties op groene infrastructuur?

______________________________________________________________________

### Fase 3 — Realisatie

**Temporal Workload Shifting:**

- Plan niet-urgente trainingstaken op momenten dat er een overschot aan zonne- of windenergie beschikbaar is op het net. Dit leidt tot gemiddeld **40% minder emissies** voor dezelfde berekening.
- Overweeg carbon-aware schedulers (bijv. via de Carbon Aware SDK van de Green Software Foundation).

**Green Coding Richtlijnen:**

- [ ] Vermijd onnodige API-calls: gebruik caching voor herhaalde queries (zie ook [Kostenoptimalisatie](07-kostenoptimalisatie.md))
- [ ] Minimaliseer prompt-lengte zonder kwaliteitsverlies
- [ ] Begrens modelrespons-lengte waar mogelijk (`max_tokens`)
- [ ] Gebruik batch-processing voor niet-real-time taken

______________________________________________________________________

### Fase 5 — Beheer & Optimalisatie

**Continue monitoring van ecologische KPI's:**

| KPI                         | Meting                                  | Drempelwaarde                                                                      |
| :-------------------------- | :-------------------------------------- | :--------------------------------------------------------------------------------- |
| Energie per query (Wh)      | Monitoring via cloudprovider dashboards | Definieer bij aanvang                                                              |
| CO₂ per maand (kg)          | Via provider rapportage of externe tool | Dalende trend                                                                      |
| Cost per Productive Outcome | Zie GAINS™ raamwerk                     | Koppel aan [Waarderealisatie](../10-doorlopende-verbetering/04-batenrealisatie.md) |

______________________________________________________________________

## 4. Afwegingskader: Wanneer is AI Duurzaam Gerechtvaardigd?

Stel uzelf bij elk AI-initiatief de volgende vragen:

1. **Is het probleem groot genoeg?** Weegt de waardecreatie op tegen de energiekost?
1. **Is er een zuiniger alternatief?** Een eenvoudig regel-gebaseerd systeem of een klein gespecialiseerd model kan beter zijn dan een groot foundation model.
1. **Wordt de energie verduurzaamd?** Kiest uw cloudprovider voor hernieuwbare energie?
1. **Wordt de hardware verantwoord beheerd?** Is er een plan voor hardware-lifecycle en e-waste?

!!! tip "Governance-ankerpunt"
    Leg de antwoorden op bovenstaande vragen vast in de [Doelkaart (goal card)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) als onderdeel van de Rode Lijnen. Een AI-systeem waarvan de milieukosten niet opwegen tegen de maatschappelijke baten, voldoet niet aan de verantwoordelijke inzetcriteria van deze blauwdruk.

______________________________________________________________________

## 5. Gerelateerde Modules

- [Kostenoptimalisatie](07-kostenoptimalisatie.md)
- [AI Architectuur](05-ai-architectuur.md)
- [Doelkaart (goal card)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Waarderealisatie (benefits realization)](../10-doorlopende-verbetering/04-batenrealisatie.md)
- [Bronnen & Inspiratie](../16-bronnen/index.md)
