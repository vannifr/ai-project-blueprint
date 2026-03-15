---
versie: '1.0'
type: guide
layer: 2
phase: [5]
roles: [AI Product Manager, Data Scientist]
tags: [monitoring]
---

# 1. Drift Detectie (Drift Detection)

## 1. Doel

Drift (drift) is het fenomeen waarbij de kwaliteit van een AI-systeem over tijd verslechtert. Deze module beschrijft hoe wij drift detecteren, meten en hierop reageren.

______________________________________________________________________

## 2. Typen Drift

### Data Drift

**Wat:** De input die het systeem ontvangt verandert t.o.v. de data waarop het getraind/getest is.

**Voorbeelden:**

- Nieuwe productcategorieën die niet in de kennisbank staan
- Veranderd taalgebruik door klanten
- Seizoensgebonden vraagpatronen

**Signalen:**

- Toename van "weet ik niet" antwoorden
- Vragen over onbekende onderwerpen
- Veranderende vraagverdeling

### Concept Drift

**Wat:** De relatie tussen input en gewenste output verandert, ook al blijft de input vergelijkbaar.

**Voorbeelden:**

- Prijswijzigingen die niet in kennisbank zijn bijgewerkt
- Nieuw beleid dat andere antwoorden vereist
- Veranderende klantverwachtingen

**Signalen:**

- Correcte antwoorden worden als incorrect beoordeeld
- Toename van klachten ondanks gelijke testresultaten
- Gap tussen validatie en productie-feedback

### Drift

**Wat:** Het model zelf verandert (bij updates door provider) of degradeert.

**Voorbeelden:**

- Provider update naar nieuw model
- Veranderingen in API-gedrag
- Fine-tuned model verliest kwaliteit

**Signalen:**

- Plotselinge verandering in outputstijl
- Veranderde latency of tokengebruik
- Regressie op eerder werkende scenario's

### Aanname-drift

**Wat:** De aannames waarop het AI-systeem is gebouwd kloppen niet meer door veranderingen in de omgeving, het gebruik of de regelgeving.

**Voorbeelden:**

- Gebruikersvolume groeit voorbij de aangenomen capaciteit
- Datadistributie verschuift t.o.v. de oorspronkelijke aanname
- Nieuwe regelgeving (bijv. EU AI Act-handhaving) maakt de huidige aanpak non-compliant
- Kosten schalen anders dan aangenomen

**Signalen:**

- Discrepantie tussen aangenomen en werkelijk gebruikersprofiel
- Kostenoverschrijding zonder verandering in functionaliteit
- Compliance-bevindingen bij audits

**Actie:** Herbeoordeel de aannames in de [Doelkaart (sectie E)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) bij elke kwartaalreview of na significante wijzigingen in het operationele landschap.

______________________________________________________________________

## 3. Detectiemethoden

### Periodieke Golden Set Testing

**Aanpak:** Voer de Golden Set regelmatig uit op productie.

| Risiconiveau | Frequentie         | Omvang                |
| ------------ | ------------------ | --------------------- |
| Minimaal     | Maandelijks        | Steekproef (25%)      |
| Beperkt      | Wekelijks          | Volledige set         |
| Hoog         | Dagelijks/Continue | Volledige set + extra |

**Wat meten we:**

- Feitelijkheid (% correct)
- Relevantie (gemiddelde score)
- Weigeringsgraad (adversarial)
- Vergelijking met nulmeting

### Real-time Monitoring

**Aanpak:** Monitor productie-interacties op signalen van drift.

**Metrics om te monitoren:**

| Metric                 | Drempel voor alert                |
| ---------------------- | --------------------------------- |
| Foutpercentage         | > 1.5x baseline                   |
| "Weet niet" antwoorden | > 2x baseline                     |
| Latency                | > 2x baseline                     |
| Tokengebruik           | > 1.5x baseline (kostenindicator) |
| Negatieve feedback     | > 2x baseline                     |

### Gebruikersfeedback Analyse

**Aanpak:** Verzamel en analyseer feedback systematisch.

**Feedbackkanalen:**

- Thumbs up/down in interface
- Escalaties naar menselijke medewerkers
- Klachten via andere kanalen
- Correcties door gebruikers

______________________________________________________________________

## 4. Drempelwaarden

Gebaseerd op [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md) sectie 3.2:

**Significant drift treedt op als:**

| Criterium        | Drempel                                  |
| ---------------- | ---------------------------------------- |
| Feitelijkheid    | Daalt ≥ 2 procentpunten t.o.v. nulmeting |
| Relevantie (1-5) | Daalt ≥ 0.3 t.o.v. nulmeting             |
| Major fouten     | Stijgt ≥ 50% over 2 meetperioden         |
| Kritieke fouten  | > 0 = direct actie                       |

**Alertniveaus:**

| Niveau | Conditie                             | Actie                         |
| ------ | ------------------------------------ | ----------------------------- |
| Groen  | Binnen baseline                      | Normaal beheer                |
| Geel   | Tussen baseline en drempel           | Verhoogde monitoring          |
| Oranje | Drempel overschreden                 | Onderzoek + mitigatieplan     |
| Rood   | Kritieke fout of ernstige degradatie | Escalatie + mogelijk rollback |

______________________________________________________________________

## 5. Responsprotocol

### Bij Geel (Verhoogde Monitoring)

- [ ] Verhoog meetfrequentie
- [ ] Analyseer trend (is het stabiel of verslechterend?)
- [ ] Identificeer mogelijke oorzaken
- [ ] Documenteer bevindingen

### Bij Oranje (Onderzoek)

- [ ] Root cause analyse uitvoeren
- [ ] Bepaal type drift (data/concept/model)
- [ ] Stel mitigatieplan op
- [ ] Informeer stakeholders
- [ ] Plan correctieve actie

### Bij Rood (Escalatie)

- [ ] Escaleer naar Tech Lead en Guardian
- [ ] Overweeg rollback of tijdelijke uitschakeling
- [ ] Activeer incidentproces
- [ ] Communiceer naar gebruikers indien relevant
- [ ] Documenteer voor lessons learned

______________________________________________________________________

## 6. Mitigatiestrategieën

### Data Drift

| Oorzaak               | Mitigatie                              |
| --------------------- | -------------------------------------- |
| Kennisbank verouderd  | Update kennisbank, herindex            |
| Nieuwe onderwerpen    | Kennisbank uitbreiden                  |
| Veranderd taalgebruik | Prompts aanpassen, voorbeelden updaten |

### Concept Drift

| Oorzaak                 | Mitigatie                                          |
| ----------------------- | -------------------------------------------------- |
| Beleid gewijzigd        | Prompts updaten                                    |
| Verwachtingen veranderd | Doelkaart (goal card) herzien, specificatie update |
| Externe veranderingen   | Rode Lijnen herzien                                |

### Drift

| Oorzaak                   | Mitigatie                              |
| ------------------------- | -------------------------------------- |
| Provider update           | Regressietest, prompts aanpassen       |
| API-wijzigingen           | Integratie updaten, fallback voorzien  |
| Onverklaarbare degradatie | Contacteer provider, overweeg rollback |

______________________________________________________________________

## 7. Nulmeting en Baseline

### Nulmeting Vastleggen

Bij livegang leg je de nulmeting vast:

| Metric        | Waarde bij livegang | Drempel voor alert |
| ------------- | ------------------- | ------------------ |
| Feitelijkheid | 99.2%               | \< 97.2%           |
| Relevantie    | 4.4                 | \< 4.1             |
| Major fouten  | 2/150               | > 3/150            |
| Latency (p95) | 1.8s                | > 3.6s             |

### Baseline Updaten

- Na significante systeemwijzigingen
- Na uitbreiding van kennisbank
- Minimaal jaarlijks herzien

______________________________________________________________________

## 8. Monitoring Dashboard

Aanbevolen visualisaties:

| Visualisatie              | Doel                                 |
| ------------------------- | ------------------------------------ |
| Trendlijn metrics         | Feitelijkheid, relevantie over tijd  |
| Heatmap vraagcategorieën  | Identificeer problematische gebieden |
| Alert timeline            | Overzicht van overschrijdingen       |
| Vergelijking met baseline | Actueel vs nulmeting                 |

______________________________________________________________________

## 9. Checklist Drift Monitoring

!!! check "9. Checklist Drift Monitoring"
    - [ ] Nulmeting is vastgelegd bij livegang
    - [ ] Periodieke Golden Set testing is ingepland
    - [ ] Real-time monitoring is actief
    - [ ] Drempelwaarden zijn geconfigureerd
    - [ ] Alerting is gekoppeld aan verantwoordelijken
    - [ ] Responsprotocol is gedocumenteerd en bekend
    - [ ] Feedbackkanalen zijn ingericht

______________________________________________________________________

## 10. Gerelateerde Modules

- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Beheer & Optimalisatie](01-doelstellingen.md)
- [Incidentrespons](../07-compliance-hub/05-incidentrespons.md)
- [Metrics Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
- [Agentic AI Engineering — Stille Degradatie](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Valkuilencatalogus](../17-bijlagen/valkuilen-catalogus.md)

______________________________________________________________________

**Volgende stap:** Richt het monitoring-dashboard in en definieer drempelwaarden voor uw productie-omgeving
→ Zie ook: [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
