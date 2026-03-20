---
versie: '1.0'
type: guide
layer: 2
phase: [1, 2, 3, 4, 5]
roles: [Business Sponsor]
summary: Kwartaalmeting of het AI-systeem de beloofde baten daadwerkelijk realiseert, met bijsturing wanneer de realisatie achterblijft.
answers: [Hoe werkt Waarderealisatie (Operationeel)?]
---

# 4. Waarderealisatie (Operationeel)

!!! abstract "Doel"
    Kwartaalmeting of het AI-systeem de beloofde baten daadwerkelijk realiseert, met bijsturing wanneer de realisatie achterblijft.

## 1. Doelstelling

Wij meten kwartaal na kwartaal of het AI-systeem de in de Business Case beloofde baten daadwerkelijk realiseert, en sturen bij als de realisatie achterblijft.

______________________________________________________________________

## 2. Intrede Criteria

- Systeem is in productie en nulmeting is vastgelegd (zie [Overdracht Checklist](../05-fase-levering/04-sjablonen/overdracht-checklist.md)).
- De originele Business Case met baten-KPI's is beschikbaar.
- Het waarderealisatieplan is overgedragen aan de eigenaar in de beheerorganisatie.

______________________________________________________________________

## 3. Kernactiviteiten

### De AI Productiviteitsparadox — Waarschuwing

!!! warning "Rework-valkuil"
    Onderzoek (Workday, 2025) toont aan dat gemiddeld **40% van de tijdwinst door AI** verloren gaat aan *rework*: het corrigeren van fouten, herschrijven van AI-gegenereerde content en dubbelchecken van outputs. Op organisatieniveau bedraagt de werkelijke productiviteitsboost **5–15%**, tegenover de gepercipieerde 50–100% op individueel niveau.

    Aanvullend: in specifieke case studies vergrootten AI-codingassistenten pull requests met tot **154%** (GitHub Copilot), wat nieuwe knelpunten in de reviewfase creëert.

    **Conclusie:** meet realisatie op organisatieniveau, niet op individueel gevoel. Splits AI-gegenereerd werk op in kleinere brokken. Investeer in platformvolwassenheid en centrale sturing — louter bottom-up experimenteren leidt tot wildgroei en inconsistentie.

Bron: \[so-46\]

______________________________________________________________________

### GAINS™ Raamwerk voor ROI-meting

Het GAINS™-raamwerk koppelt AI-uitgaven aan concrete zakelijke uitkomsten in plaats van louter te kijken naar kostenposten. Gebruik de vijf dimensies als structuur voor uw kwartaalrapportage.

| Dimensie                            | Wat meten                                               | Streefwaarde (richtlijn)           |
| :---------------------------------- | :------------------------------------------------------ | :--------------------------------- |
| **G — Usage & Engagement**          | Actieve dagelijkse gebruikers (DAU) en interactiediepte | DAU > 60% van doelgroep            |
| **A — Task Completion Time**        | Versnelling t.o.v. handmatige baseline per taaktype     | Definieer per use case             |
| **I — Error Reduction**             | Foutpercentage en vermeden herstelkosten                | Koppel aan Batenregister           |
| **N — Revenue/Output Correlation**  | Directe bijdrage aan omzet of outputvolume              | Koppel aan Business Case           |
| **S — Cost per Productive Outcome** | Kosten per nuttig resultaat (CFO-metriek)               | Dalende trend kwartaal-op-kwartaal |

Bron: \[so-46\]

______________________________________________________________________

### Kwartaalreview Waarderealisatie

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
1. Bijstuurplan voorleggen aan Guardian (raken aanpassingen aan Harde Grenzen?).
1. Beslissing documenteren in het Kaizen Log.

______________________________________________________________________

## 4. Team & Rollen

| Rol                | Verantwoordelijkheid                               | R/A/C/I |
| :----------------- | :------------------------------------------------- | :------ |
| AI Product Manager | Beheert Batenregister, coördineert kwartaalreview  | A       |
| Data Scientist     | Levert datagedreven analyse van batentekorten      | R       |
| CAIO / Stuurgroep  | Ontvangt kwartaalrapport, keurt bijsturing goed    | C       |
| Guardian           | Beoordeelt of bijsturing de Harde Grenzen raakt    | C       |
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
- [Project Afsluiting — Waarderealisatie](../11-project-afsluiting/03-batenrealisatie.md)
- [Business Case sjabloon](../09-sjablonen/02-business-case/template.md)

______________________________________________________________________

**Volgende stap:** [Sluit het project formeel af via Project Afsluiting](../11-project-afsluiting/index.md)
→ Zie ook: [Lessons Learned](../11-project-afsluiting/01-lessons-learned.md)
