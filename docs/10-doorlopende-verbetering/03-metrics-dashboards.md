---
versie: '1.0'
type: guide
layer: 2
phase: [1, 2, 3, 4, 5]
---

# 3. Metrics & Dashboards

## 1. Doelstelling

Wij maken de gezondheid van het AI-systeem continu zichtbaar via gelaagde dashboards en eenduidige KPI's, zodat het beheerteam tijdig kan ingrijpen bij afwijkingen.

______________________________________________________________________

## 2. Intrede Criteria

- Systeem is in productie (Gate 4 goedgekeurd).
- SLO's zijn schriftelijk overeengekomen.
- Logging en telemetrie zijn actief ingericht.

______________________________________________________________________

## 3. Kernactiviteiten

### De vier KPI-categorieën

Wij meten op vier niveaus. Elke categorie heeft een vaste eigenaar en rapportagecadans:

| Categorie           | Voorbeeldmetrics                                                      | Eigenaar       | Cadans      |
| :------------------ | :-------------------------------------------------------------------- | :------------- | :---------- |
| **Modelprestaties** | Nauwkeurigheid, F1-score, afwijking t.o.v. Golden Set                 | Data Scientist | Dagelijks   |
| **Operationeel**    | Latentie P95, foutpercentage, uptime, doorvoer (requests/min)         | MLOps Engineer | Real-time   |
| **Gebruikskosten**  | Kosten per aanroep, maandelijkse rekenkosten                          | AI PM          | Maandelijks |
| **Governance**      | Aantal overschreden Rode Lijnen, Guardian-interventies, bias-signalen | Guardian       | Wekelijks   |

### Dashboardlagen

Wij onderscheiden drie lagen. Elk dashboard heeft een ander publiek en een andere granulariteit:

**Laag 1 — Operationeel (real-time):** Zichtbaar voor MLOps en tech team. Toont systeemgezondheid, alerts en actieve incidenten.

**Laag 2 — Modelkwaliteit (dagelijks/wekelijks):** Zichtbaar voor Data Scientist en AI PM. Toont nauwkeurigheidstrends, Drift-signalen en vergelijking met de Golden Set.

**Laag 3 — Strategisch (maandelijks/kwartaal):** Zichtbaar voor CAIO en management. Toont ROI-realisatie, kostentrends en compliance-status.

### Drempelwaarden en alerts

Voor elk kritisch metric definiëren wij drie niveaus:

| Niveau                 | Actie                                                                              |
| :--------------------- | :--------------------------------------------------------------------------------- |
| 🟡 **Waarschuwing**    | Notificatie naar het beheerteam; onderzoek vereist binnen 48 uur                   |
| 🟠 **Kritiek**         | Directe interventie vereist; Guardian wordt geïnformeerd                           |
| 🔴 **Circuit Breaker** | Automatische blokkering of escalatie; menselijke goedkeuring vereist voor herstart |

**Voorbeeld:** Als de nauwkeurigheid daalt onder 85% (Waarschuwing), onder 80% (Kritiek) of onder 70% (Circuit Breaker).

### SLO-definitie en bewaking

Een SLO (Service Level Objective) is een intern bindend streefdoel. Wij definiëren minimaal:

- **Beschikbaarheid:** bijv. ≥ 99,5% uptime per maand.
- **Latentie:** bijv. P95 responstijd ≤ 2 seconden.
- **Nauwkeurigheidsbodem:** bijv. F1-score ≥ 0,80 op de Golden Set.

SLO's worden vastgesteld vóór Gate 4 en opgenomen in de overdrachts­documentatie.

______________________________________________________________________

## 4. Team & Rollen

| Rol                | Verantwoordelijkheid                                  | R/A/C/I |
| :----------------- | :---------------------------------------------------- | :------ |
| MLOps Engineer     | Beheert operationeel dashboard, configureert alerts   | R       |
| Data Scientist     | Beheert modelkwaliteitsdashboard, analyseert trends   | R       |
| AI Product Manager | Beheert strategisch dashboard, bewaakt ROI en SLO's   | A       |
| Guardian           | Bewaakt governance-dashboard, rapporteert afwijkingen | C       |
| CAIO               | Ontvangt maandelijks strategisch rapport              | I       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] Alle vier KPI-categorieën zijn zichtbaar in het juiste dashboard.
- [ ] Drempelwaarden en alertregels zijn gedocumenteerd en getest.
- [ ] SLO's zijn vastgesteld en gedeeld met de beheerorganisatie.
- [ ] Eerste maandrapport is opgeleverd aan de CAIO.

______________________________________________________________________

## 6. Deliverables

| Deliverable              | Beschrijving                                      | Eigenaar       |
| :----------------------- | :------------------------------------------------ | :------------- |
| Operationeel dashboard   | Real-time gezondheids­bewaking                    | MLOps Engineer |
| Modelkwaliteitsrapport   | Wekelijkse samenvatting prestaties vs. Golden Set | Data Scientist |
| Maandrapport Strategisch | ROI, kosten, compliance-status                    | AI PM          |
| SLO-document             | Vastgestelde servicenormen en drempelwaarden      | AI PM          |

______________________________________________________________________

**Gerelateerde modules:**

- [Doorlopende Verbetering — Overzicht](index.md)
- [Retrospectives](01-retrospectives.md)
- [Waarderealisatie (benefits realization)](04-batenrealisatie.md)
- [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md)
- [Beheer & Optimalisatie — Activiteiten](../06-fase-monitoring/02-activiteiten.md)

______________________________________________________________________

**Volgende stap:** [Meet de gerealiseerde baten via Waarderealisatie](04-batenrealisatie.md)
→ Zie ook: [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md)
