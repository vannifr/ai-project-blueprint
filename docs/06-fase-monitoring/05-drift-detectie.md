---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# 2.5.3 Prestatieverloop Detectie (Drift Detection)

## 2.5.3.1 Doel

Prestatieverloop (drift) is het fenomeen waarbij de kwaliteit van een AI-systeem over tijd verslechtert. Deze module beschrijft hoe wij drift detecteren, meten en hierop reageren.

______________________________________________________________________

## 2.5.3.2 Typen Prestatieverloop

### 2.5.3.2.1 Data Drift

**Wat:** De input die het systeem ontvangt verandert t.o.v. de data waarop het getraind/getest is.

**Voorbeelden:**

- Nieuwe productcategorieën die niet in de kennisbank staan
- Veranderd taalgebruik door klanten
- Seizoensgebonden vraagpatronen

**Signalen:**

- Toename van "weet ik niet" antwoorden
- Vragen over onbekende onderwerpen
- Veranderende vraagverdeling

### 2.5.3.2.2 Concept Drift

**Wat:** De relatie tussen input en gewenste output verandert, ook al blijft de input vergelijkbaar.

**Voorbeelden:**

- Prijswijzigingen die niet in kennisbank zijn bijgewerkt
- Nieuw beleid dat andere antwoorden vereist
- Veranderende klantverwachtingen

**Signalen:**

- Correcte antwoorden worden als incorrect beoordeeld
- Toename van klachten ondanks gelijke testresultaten
- Gap tussen validatie en productie-feedback

### 2.5.3.2.3 Model Drift

**Wat:** Het model zelf verandert (bij updates door provider) of degradeert.

**Voorbeelden:**

- Provider update naar nieuw model
- Veranderingen in API-gedrag
- Fine-tuned model verliest kwaliteit

**Signalen:**

- Plotselinge verandering in outputstijl
- Veranderde latency of tokengebruik
- Regressie op eerder werkende scenario's

______________________________________________________________________

## 2.5.3.3 Detectiemethoden

### 2.5.3.3.1 Periodieke Gouden Set Testing

**Aanpak:** Voer de Gouden Set regelmatig uit op productie.

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

### 2.5.3.3.2 Real-time Monitoring

**Aanpak:** Monitor productie-interacties op signalen van drift.

**Metrics om te monitoren:**

| Metric                 | Drempel voor alert                |
| ---------------------- | --------------------------------- |
| Foutpercentage         | > 1.5x baseline                   |
| "Weet niet" antwoorden | > 2x baseline                     |
| Latency                | > 2x baseline                     |
| Tokengebruik           | > 1.5x baseline (kostenindicator) |
| Negatieve feedback     | > 2x baseline                     |

### 2.5.3.3.3 Gebruikersfeedback Analyse

**Aanpak:** Verzamel en analyseer feedback systematisch.

**Feedbackkanalen:**

- Thumbs up/down in interface
- Escalaties naar menselijke medewerkers
- Klachten via andere kanalen
- Correcties door gebruikers

______________________________________________________________________

## 2.5.3.4 Drempelwaarden

Gebaseerd op [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md) sectie 3.2:

**Significant prestatieverloop treedt op als:**

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

## 2.5.3.5 Responsprotocol

### 2.5.3.5.1 Bij Geel (Verhoogde Monitoring)

- [ ] Verhoog meetfrequentie
- [ ] Analyseer trend (is het stabiel of verslechterend?)
- [ ] Identificeer mogelijke oorzaken
- [ ] Documenteer bevindingen

### 2.5.3.5.2 Bij Oranje (Onderzoek)

- [ ] Root cause analyse uitvoeren
- [ ] Bepaal type drift (data/concept/model)
- [ ] Stel mitigatieplan op
- [ ] Informeer stakeholders
- [ ] Plan correctieve actie

### 2.5.3.5.3 Bij Rood (Escalatie)

- [ ] Escaleer naar Tech Lead en Guardian
- [ ] Overweeg rollback of tijdelijke uitschakeling
- [ ] Activeer incidentproces
- [ ] Communiceer naar gebruikers indien relevant
- [ ] Documenteer voor lessons learned

______________________________________________________________________

## 2.5.3.6 Mitigatiestrategieën

### 2.5.3.6.1 Data Drift

| Oorzaak               | Mitigatie                              |
| --------------------- | -------------------------------------- |
| Kennisbank verouderd  | Update kennisbank, herindex            |
| Nieuwe onderwerpen    | Kennisbank uitbreiden                  |
| Veranderd taalgebruik | Prompts aanpassen, voorbeelden updaten |

### 2.5.3.6.2 Concept Drift

| Oorzaak                 | Mitigatie                              |
| ----------------------- | -------------------------------------- |
| Beleid gewijzigd        | Sturingsinstructies updaten            |
| Verwachtingen veranderd | Doelkaart herzien, specificatie update |
| Externe veranderingen   | Rode Lijnen herzien                    |

### 2.5.3.6.3 Model Drift

| Oorzaak                   | Mitigatie                              |
| ------------------------- | -------------------------------------- |
| Provider update           | Regressietest, prompts aanpassen       |
| API-wijzigingen           | Integratie updaten, fallback voorzien  |
| Onverklaarbare degradatie | Contacteer provider, overweeg rollback |

______________________________________________________________________

## 2.5.3.7 Nulmeting en Baseline

### 2.5.3.7.1 Nulmeting Vastleggen

Bij livegang leg je de nulmeting vast:

| Metric        | Waarde bij livegang | Drempel voor alert |
| ------------- | ------------------- | ------------------ |
| Feitelijkheid | 99.2%               | \< 97.2%           |
| Relevantie    | 4.4                 | \< 4.1             |
| Major fouten  | 2/150               | > 3/150            |
| Latency (p95) | 1.8s                | > 3.6s             |

### 2.5.3.7.2 Baseline Updaten

- Na significante systeemwijzigingen
- Na uitbreiding van kennisbank
- Minimaal jaarlijks herzien

______________________________________________________________________

## 2.5.3.8 Monitoring Dashboard

Aanbevolen visualisaties:

| Visualisatie              | Doel                                 |
| ------------------------- | ------------------------------------ |
| Trendlijn metrics         | Feitelijkheid, relevantie over tijd  |
| Heatmap vraagcategorieën  | Identificeer problematische gebieden |
| Alert timeline            | Overzicht van overschrijdingen       |
| Vergelijking met baseline | Actueel vs nulmeting                 |

______________________________________________________________________

## 2.5.3.9 Checklist Drift Monitoring

- [ ] Nulmeting is vastgelegd bij livegang
- [ ] Periodieke Gouden Set testing is ingepland
- [ ] Real-time monitoring is actief
- [ ] Drempelwaarden zijn geconfigureerd
- [ ] Alerting is gekoppeld aan verantwoordelijken
- [ ] Responsprotocol is gedocumenteerd en bekend
- [ ] Feedbackkanalen zijn ingericht

______________________________________________________________________

## 2.5.3.10 Gerelateerde Modules

- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Beheer & Optimalisatie](01-doelstellingen.md)
- [Incidentrespons](../07-compliance-hub/05-incidentrespons.md)
- [Metrics Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
