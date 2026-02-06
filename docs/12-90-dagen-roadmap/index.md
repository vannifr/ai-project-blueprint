---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# 1. Snelstart: AI-Project in 90 Dagen

## 1. Vooraf (Definition of Ready)

- Kernteam benoemd: **AI Product Manager**, **Tech Lead**, **Guardian**
- Toegang tot relevante data geregeld (minimaal leesrechten)
- Werkruimte klaar: repo/wiki + plek voor sjablonen + beslislogboek
- Eén gebruikscasus geselecteerd (max 1) met duidelijke eigenaar

______________________________________________________________________

## 2. Planning (week-voor-week)

| Week | Doel                            | Opleveringen (verplicht)                                                                                                                     | Primaire eigenaar    | Gate/Output                                |
| ---: | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------ |
|    1 | Gebruikscasus scherp + scope    | [Project Charter](../09-sjablonen/01-project-charter/template.md) (concept)                                                                  | AI PM                | Go/no-go op probleemdefinitie              |
|    2 | Risico + data haalbaarheid      | [Risico Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md), Data-Evaluatie samenvatting                                                 | Guardian + Tech Lead | Gate 1 (Go/No-Go Ontdekking): doorgaan?    |
|    3 | Doel + Rode Lijnen              | [Business Case](../09-sjablonen/02-business-case/template.md) (v1)                                                                           | AI PM + Guardian     | Rode Lijnen akkoord                        |
|    4 | Testbasis opzetten              | [Gouden Set Test](../09-sjablonen/07-validatie-bewijs/template.md) + Gouden Set v1                                                           | AI PM + QA/Tech      | Testplan gereed                            |
|    5 | Prototype (pilot)               | Prototype + [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md) (concept)                                                  | Tech Lead            | Interne demo                               |
|    6 | Pilot meten                     | [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md) (pilot)                                                          | Tech Lead + AI PM    | Gate 2 (Investering PoV): naar Realisatie? |
|    7 | Realisatie: integratiepad       | Integratieplan + loggingplan                                                                                                                 | Tech Lead            | Ready for RC                               |
|    8 | Privacy & security checks       | [Data & Privacyblad](../09-sjablonen/11-privacy-data/privacyblad.md)                                                                         | Guardian + Privacy   | "OK to proceed"                            |
|    9 | Release Candidate bouwen        | RC build + [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md) (v1); *Batch size policy gedefinieerd en gecommuniceerd*    | Tech Lead            | RC gereed                                  |
|   10 | RC testen & bewijs              | [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md) (RC); *CI feedback SLO's vastgesteld (afgesproken tijdsvenster)* | QA + Guardian        | Gate 3 (Productie-klaar): Live?            |
|   11 | Live pilot + monitoring         | Monitoring + incidentproces actief; *AI-assisted development guardrails geïmplementeerd (verplichte review, test coverage)*                  | Tech Lead            | 1e productie-evaluatie                     |
|   12 | Optimaliseren + overdracht      | Beheerplan + nulmeting drift; *Regressie op Gouden Set vóór RC afgedwongen* — Bron: \[so-28\]                                                | Tech Lead + AI PM    | Overdracht Beheer & Optimalisatie          |
|   13 | Retrospective + standaardiseren | Lessons learned + gids updates                                                                                                               | AI CC                | v2.3 backlog                               |

______________________________________________________________________

## 3. Minimale beslismomenten (Gates)

- **Gate 1 (Go/No-Go Ontdekking) (einde week 2):** risico + data haalbaarheid bevestigd
- **Gate 2 (Investering PoV) (einde week 6):** pilotresultaat ([Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)) voldoet aan [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- **Gate 3 (Productie-klaar) (einde week 10):** RC voldoet aan [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md) + logging/privacy geregeld
- **Gate 4 (Livegang) (week 12):** overdracht naar beheer incl. nulmeting prestatieverloop

______________________________________________________________________

## 4. Tijdlijn per Risiconiveau

De standaard 13-weken planning is geschikt voor **Beperkt Risico** toepassingen. Pas de tijdlijn aan op basis van uw risicoklassificatie:

### Minimaal Risico (Fast Lane): 6-8 weken

| Fase         | Weken | Focus                                     |
| ------------ | ----: | ----------------------------------------- |
| Verkenning   |   1-2 | Charter + Risico Pre-Scan + Doelkaart     |
| Validatie    |   3-4 | Prototype + Gouden Set (20 cases) + Pilot |
| Livegang     |   5-6 | Validatierapport + Monitoring basis       |
| Stabilisatie |   7-8 | Optimalisatie + Overdracht                |

Zie [Fast Lane](../02-fase-ontdekking/06-fast-lane.md) voor toelatingscriteria.

### Beperkt Risico: 13 weken (standaard)

Volg de week-voor-week planning in sectie 1 hierboven.

### Hoog Risico: 18-24 weken

| Fase                    | Weken | Extra activiteiten t.o.v. standaard                         |
| ----------------------- | ----: | ----------------------------------------------------------- |
| Verkenning              |   1-3 | Uitgebreide DPIA, juridische review, Guardian goedkeuring   |
| Data Governance         |   4-6 | Data lineage, uitgebreide kwaliteitscontroles, bias-analyse |
| Validatie               |  7-12 | Gouden Set (150+ cases), Eerlijkheidstoets, externe audit   |
| Realisatie              | 13-18 | Uitgebreid technisch dossier, CE-voorbereiding              |
| Livegang & Stabilisatie | 19-24 | Gefaseerde uitrol, intensieve monitoring, Guardian reviews  |

**Extra vereisten Hoog Risico:**

- Volledige EU AI Act compliance documentatie
- Onafhankelijke Guardian review bij elke Gate
- Kwantitatieve Eerlijkheidstoets met mitigatieplan
- 100% input/output logging met 12 maanden retentie
