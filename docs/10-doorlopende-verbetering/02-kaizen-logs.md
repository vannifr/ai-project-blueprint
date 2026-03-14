---
versie: '1.0'
---

# 2. Kaizen Logs

## 1. Doelstelling

Wij registreren elke kleine, gerichte verbetering aan het AI-systeem in een doorlopend Kaizen Log zodat verbeteringen traceerbaar, herhaalbaar en geaggregeerd zichtbaar zijn.

______________________________________________________________________

## 2. Intrede Criteria

- Het systeem is in productie en actief in gebruik.
- De retrospective-cadans is operationeel.
- Er is een gedeeld document of backlog beschikbaar voor het team.

______________________________________________________________________

## 3. Kernactiviteiten

### Kaizen-entry registreren

Elke verbetering — hoe klein ook — wordt gelogd met een vaste structuur:

| Veld          | Beschrijving                                      |
| :------------ | :------------------------------------------------ |
| **ID**        | Uniek volgnummer (bijv. KZ-2026-001)              |
| **Datum**     | Datum waarop het probleem werd geïdentificeerd    |
| **Eigenaar**  | Wie is verantwoordelijk voor de uitvoering?       |
| **Probleem**  | Wat werkt niet goed of kan beter? (max. 2 zinnen) |
| **Maatregel** | Wat is de concrete verbetering?                   |
| **Resultaat** | Wat is het gemeten effect na implementatie?       |
| **Status**    | Open / In uitvoering / Gesloten                   |

**Voorbeeld:**

> KZ-2026-007 · 15-03-2026 · Data Scientist · De nauwkeurigheid van categorie X daalt structureel 3% per maand. · Aanvulling Golden Set met 20 nieuwe randgevallen en hertraining. · Nauwkeurigheid hersteld naar baseline +1,2%. · Gesloten.

### Kaizen-cyclus bewaken

- **Wekelijks:** Status van open entries bespreken in het stand-up.
- **Maandelijks:** Overzicht van gesloten entries en gemeten effecten naar het team.
- **Kwartaal:** Geaggregeerde Kaizen-analyse als input voor de Modelretrospective.

### Onderscheid Kaizen Log vs. Incidentlog

| Kaizen Log                       | Incidentlog                         |
| :------------------------------- | :---------------------------------- |
| Proactieve verbeteringen         | Reactieve storingen en incidenten   |
| Gericht op kwaliteitsverhoging   | Gericht op herstel en worteloorzaak |
| Geen tijdsdruk                   | SLO-gebonden responstijden          |
| Eigenaar: AI PM / Data Scientist | Eigenaar: MLOps Engineer            |

______________________________________________________________________

## 4. Team & Rollen

| Rol                | Verantwoordelijkheid                                      | R/A/C/I |
| :----------------- | :-------------------------------------------------------- | :------ |
| AI Product Manager | Beheert het Kaizen Log, prioriteert entries               | A       |
| Data Scientist     | Registreert en analyseert modelgerelateerde verbeteringen | R       |
| MLOps Engineer     | Registreert infrastructuur- en pijplijnverbeteringen      | R       |
| Guardian           | Beoordeelt of verbeteringen de Rode Lijnen raken          | C       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] Alle open entries ouder dan 30 dagen hebben een status-update of zijn geëscaleerd.
- [ ] Maandelijks overzicht is gedeeld met het team.
- [ ] Kwartaalanalyse is opgenomen in het Modelgezondheidsrapport.

______________________________________________________________________

## 6. Deliverables

| Deliverable     | Beschrijving                                  | Eigenaar       |
| :-------------- | :-------------------------------------------- | :------------- |
| Kaizen Log      | Levend overzicht van alle verbeteringen       | AI PM          |
| Maandoverzicht  | Samenvatting van gesloten entries en effecten | AI PM          |
| Kwartaalanalyse | Geaggregeerd inzicht in verbetertrends        | Data Scientist |

______________________________________________________________________

**Gerelateerde modules:**

- [Doorlopende Verbetering — Overzicht](index.md)
- [Retrospectives](01-retrospectives.md)
- [Metrics & Dashboards](03-metrics-dashboards.md)
- [Beheer & Optimalisatie — Activiteiten](../06-fase-monitoring/02-activiteiten.md)

______________________________________________________________________

**Volgende stap:** [Stel KPI's en dashboards in via Metrics & Dashboards](03-metrics-dashboards.md)
→ Zie ook: [Retrospectives](01-retrospectives.md)
