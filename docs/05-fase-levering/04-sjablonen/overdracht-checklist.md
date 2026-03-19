---
versie: '1.0'
type: guide
layer: 2
phase: [4]
roles: [AI Product Manager]
tags: [gate-review]
---

# 1. Checklist: Operationele Overdracht

!!! abstract "Doel"
    Afvinkbare checklist voor de formele overdracht van het AI-systeem van het projectteam aan de beheerorganisatie bij Gate 4.

Gebruik deze checklist bij de formele overdracht van het AI-systeem van het projectteam aan de beheerorganisatie (Gate 4 — Livegang). Alle items moeten zijn afgevinkt én gedocumenteerd vóór de overdracht officieel is.

______________________________________________________________________

## 1. Technische Gereedheid

- [ ] **Modeldocumentatie volledig:** Technische Modelkaart is ingevuld en goedgekeurd door de Guardian.
- [ ] **Coderepository opgeleverd:** Alle broncode, configuraties en modeldefinities staan in een door de beheerorganisatie toegankelijke repository (versiebeheer).
- [ ] **Omgevingsdocumentatie aanwezig:** Infrastructuurvereisten (rekenkracht, opslag, netwerk, toegangsrechten) zijn gedocumenteerd.
- [ ] **Runbook beschikbaar:** Stap-voor-stap handleiding voor dagelijkse bediening, herstartprocedures en schaling is geschreven en getest door de beheerorganisatie.
- [ ] **Monitoring actief:** Dashboards, alerts en drempelwaarden zijn ingericht en zichtbaar voor het beheerteam.
- [ ] **Logging geconfigureerd:** Input/output-logging is actief conform de vereisten van het risiconiveau (minimaal 30 dagen retentie voor Beperkt Risico, 12 maanden voor Hoog Risico).

______________________________________________________________________

## 2. Operationele Gereedheid

- [ ] **Beheerteam aangewezen:** Er is een benoemde eigenaar (Accountable) voor het systeem in de beheerorganisatie.
- [ ] **Escalatiepad gedefinieerd:** Procedures voor incidenten zijn gedocumenteerd: wie contacteren, wanneer, hoe? → [Incident Respons](../../07-compliance-hub/05-incidentrespons.md)
- [ ] **SLO's vastgesteld:** Servicenormen (latentie, beschikbaarheid, nauwkeurigheidsdrempel) zijn schriftelijk overeengekomen tussen projectteam en beheerorganisatie.
- [ ] **Retraining-protocol gedocumenteerd:** Wanneer en hoe wordt het model opnieuw afgestemd? Wie mag dit initiëren?
- [ ] **Nulmeting vastgelegd:** Baseline-prestaties (nauwkeurigheid, latentie, gebruikskosten) zijn gemeten en gedocumenteerd als referentie voor toekomstig Drift.

______________________________________________________________________

## 3. Governance & Compliance

- [ ] **Guardian overgedragen:** De Guardian-rol is formeel overgedragen aan een persoon binnen de beheerorganisatie of een onafhankelijke partij.
- [ ] **Harde Grenzen gecommuniceerd:** De beheerorganisatie kent en begrijpt de Harde Grenzen van het systeem. Schriftelijke bevestiging aanwezig.
- [ ] **EU AI Act dossier compleet:** Voor Hoog Risico-systemen is het Technisch Dossier volledig en goedgekeurd door de Guardian. → [EU AI Act](../../07-compliance-hub/01-eu-ai-act/index.md)
- [ ] **Privacy & Data compliant:** Data & Privacyblad (AVG/DPIA) is goedgekeurd en opgenomen in het dossier.
- [ ] **Licenties en contracten geregeld:** Alle externe API-contracten, datalicenties en leveranciersovereenkomsten zijn overgedragen aan de beheerorganisatie.

______________________________________________________________________

## 4. Kennisoverdracht

- [ ] **Gebruikerstraining afgerond:** Eindgebruikers zijn opgeleid. Trainingsmateriaal is beschikbaar en up-to-date.
- [ ] **Beheerderstraining afgerond:** Technisch beheerteam heeft een hands-on sessie gehad met de MLOps-engineer van het projectteam.
- [ ] **Lessons Learned overgedragen:** Inzichten uit het project zijn gedocumenteerd en beschikbaar voor toekomstige projecten. → [Lessons Learned](../../11-project-afsluiting/01-lessons-learned.md)
- [ ] **Contactpersonenlijst opgeleverd:** Namen en contactgegevens van dataproviders, modelleveranciers en technische contacten zijn overgedragen.

______________________________________________________________________

## 5. Formele Afsluiting

- [ ] **Overdrachtsacceptatie ondertekend:** Projectteam én beheerorganisatie hebben het overdrachtsformulier ondertekend.
- [ ] **Gate 4 (Livegang) goedgekeurd:** Alle Gate Review-criteria zijn afgevinkt en gedocumenteerd. → [Gate Reviews](../../09-sjablonen/04-gate-reviews/checklist.md)
- [ ] **Waarderealisatieplan geactiveerd:** Het plan voor het meten van de gerealiseerde baten is overgedragen aan de eigenaar in de beheerorganisatie. → [Waarderealisatie](../../11-project-afsluiting/03-batenrealisatie.md)
- [ ] **Projectarchief afgesloten:** Alle projectdocumenten zijn gearchiveerd op de afgesproken locatie.

______________________________________________________________________

## Ondertekening

| Rol                        | Naam | Datum | Handtekening |
| :------------------------- | :--- | :---- | :----------- |
| Projectleider (AI PM)      |      |       |              |
| Tech Lead                  |      |       |              |
| Guardian                   |      |       |              |
| Eigenaar Beheerorganisatie |      |       |              |

______________________________________________________________________

**Gerelateerde modules:**

- [Fase 4: Levering — Overzicht](../01-doelstellingen.md)
- [Gate Reviews Checklist](../../09-sjablonen/04-gate-reviews/checklist.md)
- [Lessons Learned](../../11-project-afsluiting/01-lessons-learned.md)
- [Incident Respons](../../07-compliance-hub/05-incidentrespons.md)

______________________________________________________________________

**Volgende stap:** Vul deze checklist in samen met het beheerteam vóór de formele overdracht
→ Zie ook: [Gate 4](../../09-sjablonen/04-gate-reviews/checklist.md) | [Fase 5 Monitoring](../../06-fase-monitoring/01-doelstellingen.md)
