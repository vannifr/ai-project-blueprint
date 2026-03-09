---
versie: '1.0'
---

# 4. Waarderealisatie (benefits realization) (Operationeel)

## 1. Doelstelling

Wij meten kwartaal na kwartaal of het AI-systeem de in de Business Case beloofde baten daadwerkelijk realiseert, en sturen bij als de realisatie achterblijft.

______________________________________________________________________

## 2. Intrede Criteria

- Systeem is in productie en nulmeting is vastgelegd (zie [Overdracht Checklist](../05-fase-levering/04-sjablonen/overdracht-checklist.md)).
- De originele Business Case met baten-KPI's is beschikbaar.
- Het waarderealisatie (benefits realization)plan is overgedragen aan de eigenaar in de beheerorganisatie.

______________________________________________________________________

## 3. Kernactiviteiten

### Kwartaalreview Waarderealisatie (benefits realization)

Elke drie maanden vergelijkt de AI PM de werkelijke baten met de Business Case. De review omvat:

1. **Meting:** Verzamelen van actuele waarden voor alle baten-KPI's.
1. **Vergelijking:** Actuele waarde vs. doelwaarde vs. nulmeting.
1. **Analyse:** Verklaar afwijkingen. Is de afwijking structureel of tijdelijk?
1. **Bijsturing:** Stel aanpassingen voor (betere adoptie, hertraining, andere aanpak).
1. **Rapportage:** Presenteer bevindingen aan de CAIO of stuurgroep.

### Batenregister

Wij houden een levend Batenregister bij per AI-systeem:

| Bat                                  | Doelwaarde | Nulmeting | Q1     | Q2     | Q3  | Q4  | Trend       |
| :----------------------------------- | :--------- | :-------- | :----- | :----- | :-- | :-- | :---------- |
| Tijdsbesparing verwerking (uur/week) | -20 uur    | 48 uur    | 35 uur | 31 uur | —   | —   | ↓ op schema |
| Foutpercentage in output             | \< 5%      | 12%       | 8%     | 6%     | —   | —   | ↓ dalend    |
| Gebruikerstevredenheid (NPS)         | ≥ 30       | 12        | 18     | 24     | —   | —   | ↑ stijgend  |

### Bijsturingsprotocol

Als een baat meer dan 20% onder de doelwaarde blijft na twee kwartalen:

1. Root cause analyse door Data Scientist + AI PM.
1. Bijstuurplan opstellen (hertraining, process redesign, extra training gebruikers).
1. Bijstuurplan voorleggen aan Guardian (raken aanpassingen aan Rode Lijnen?).
1. Beslissing documenteren in het Kaizen Log.

______________________________________________________________________

## 4. Team & Rollen

| Rol                | Verantwoordelijkheid                               | R/A/C/I |
| :----------------- | :------------------------------------------------- | :------ |
| AI Product Manager | Beheert Batenregister, coördineert kwartaalreview  | A       |
| Data Scientist     | Levert datagedreven analyse van batentekorten      | R       |
| CAIO / Stuurgroep  | Ontvangt kwartaalrapport, keurt bijsturing goed    | C       |
| Guardian           | Beoordeelt of bijsturing de Rode Lijnen raakt      | C       |
| Beheerorganisatie  | Levert operationele data aan (werkelijke metingen) | R       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] Kwartaalrapport is opgeleverd aan de CAIO.
- [ ] Alle baten-KPI's zijn gemeten en gedocumenteerd in het Batenregister.
- [ ] Structurele tekorten hebben een gedocumenteerd bijstuurplan.

______________________________________________________________________

## 6. Deliverables

| Deliverable           | Beschrijving                                                      | Eigenaar               |
| :-------------------- | :---------------------------------------------------------------- | :--------------------- |
| Batenregister         | Levend overzicht van doelen, nulmeting en realisatie per kwartaal | AI PM                  |
| Kwartaalrapport Baten | Analyse en bijsturingsaanbevelingen voor CAIO                     | AI PM                  |
| Bijstuurplan          | Concrete acties bij structurele batenachterstand                  | AI PM + Data Scientist |

______________________________________________________________________

**Gerelateerde modules:**

- [Doorlopende Verbetering — Overzicht](index.md)
- [Metrics & Dashboards](03-metrics-dashboards.md)
- [Project Afsluiting — Waarderealisatie (benefits realization)](../11-project-afsluiting/03-batenrealisatie.md)
- [Business Case sjabloon](../09-sjablonen/02-business-case/template.md)
