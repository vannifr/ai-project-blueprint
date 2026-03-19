---
versie: '1.0'
type: template
layer: 1
tags: [stakeholder, template]
---

# RACI Matrix — Rollen per Fase

!!! abstract "Doel"
    RACI-overzicht dat per kernactiviteit en fase vastlegt wie verantwoordelijk, eindverantwoordelijk, geraadpleegd of geinformeerd is.

Centraal overzicht van wie **Responsible**, **Accountable**, **Consulted** en **Informed** is per kernactiviteit, over alle fasen van de AI-lifecycle.

**Legenda:** R = Responsible (uitvoerder) · A = Accountable (eindverantwoordelijke) · C = Consulted (geraadpleegd) · I = Informed (geïnformeerd) · — = Niet betrokken

!!! info "Eén A per activiteit"
    Elke activiteit heeft precies één **A** (eindverantwoordelijke). Meerdere R's zijn mogelijk, maar nooit meerdere A's.

______________________________________________________________________

## Fase 1 — Verkenning & Strategie

| Kernactiviteit                             | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :----------------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Use case selectie & prioritering           |   A   |     C     |       C        |    C     |  I   |       —       |      —       |        —        |          —          |
| Stakeholder interviews & probleemdefinitie |   R   |     C     |       —        |    I     |  I   |       —       |      C       |        —        |          —          |
| Moduskeuze beoordeling (autonomieniveau)   |   R   |     C     |       —        |    C     |  I   |       —       |      —       |        —        |          C          |
| Risk Pre-Scan                              |   R   |     C     |       C        |    A     |  I   |       —       |      —       |        —        |          C          |
| Doelkaart (goal card) opstellen            |   A   |     C     |       —        |    R     |  I   |       —       |      —       |        —        |          —          |
| Harde Grenzen definiëren                   |   R   |     C     |       —        |    A     |  I   |       —       |      —       |        —        |          C          |
| Fast Lane beslissing                       |   A   |     R     |       —        |    C     |  C   |       —       |      —       |        —        |          —          |

______________________________________________________________________

## Fase 2 — Validatie (PoV)

| Kernactiviteit                             | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :----------------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| PoV-scope en opzet                         |   A   |     R     |       R        |    C     |  I   |       C       |      —       |        C        |          —          |
| Dataset verkenning & kwaliteitsbeoordeling |   C   |     C     |       A        |    C     |  —   |       R       |      —       |        C        |          —          |
| Golden Set samenstellen                    |   C   |     C     |       A        |    C     |  —   |       R       |      —       |        C        |          —          |
| Business Case opstellen                    |   A   |     C     |       C        |    C     |  C   |       —       |      —       |        —        |          —          |
| Gate 2 Review                              |   A   |     C     |       C        |    R     |  C   |       —       |      —       |        —        |          C          |
| Guardian goedkeuring Gate 2                |   —   |     —     |       —        |    A     |  —   |       —       |      —       |        —        |          —          |

______________________________________________________________________

## Fase 3 — Realisatie

| Kernactiviteit                           | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :--------------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Sprint planning & backlog beheer         |   A   |     C     |       C        |    —     |  I   |       —       |      —       |        —        |          —          |
| Modelontwikkeling (SDD-patroon)          |   C   |     A     |       R        |    —     |  —   |       R       |      —       |        C        |          —          |
| Prompt engineering & versioning          |   R   |     A     |       C        |    C     |  —   |       —       |      —       |        R        |          —          |
| Data pipeline bouwen                     |   C   |     C     |       R        |    —     |  —   |       A       |      —       |        C        |          —          |
| RAG-architectuur (indien van toepassing) |   C   |     A     |       R        |    —     |  —   |       R       |      —       |        R        |          —          |
| Technische Model Card                    |   C   |     A     |       R        |    C     |  —   |       —       |      —       |        —        |          —          |
| Red Teaming coördineren                  |   R   |     C     |       C        |    A     |  —   |       —       |      —       |        —        |          R          |
| Gate 3 Review                            |   A   |     R     |       C        |    C     |  C   |       —       |      —       |        —        |          C          |

______________________________________________________________________

## Fase 4 — Levering

| Kernactiviteit                      | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :---------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Go-live planning & coördinatie      |   A   |     R     |       —        |    C     |  I   |       C       |      C       |        —        |          C          |
| Technische implementatie (livegang) |   C   |     A     |       —        |    —     |  —   |       R       |      —       |        C        |          C          |
| Traceerbaarheidsrapport             |   A   |     C     |       R        |    C     |  —   |       —       |      —       |        —        |          —          |
| Gebruikerstraining & adoptie        |   C   |     —     |       —        |    —     |  I   |       —       |      A       |        C        |          —          |
| Overdracht aan beheerorganisatie    |   A   |     R     |       C        |    C     |  C   |       C       |      C       |        C        |          C          |

______________________________________________________________________

## Fase 5 — Beheer & Optimalisatie

| Kernactiviteit                     | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :--------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Drift detectie & monitoring        |   C   |     C     |       R        |    C     |  —   |       A       |      —       |        C        |          —          |
| Performance rapportage             |   A   |     C     |       R        |    C     |  I   |       —       |      —       |        —        |          —          |
| Ethisch toezicht & bias monitoring |   C   |     —     |       R        |    A     |  I   |       —       |      —       |        —        |          C          |
| Modelaanpassing of retraining      |   C   |     A     |       R        |    C     |  I   |       R       |      —       |        C        |          —          |
| Incident response (uitvoering)     |   R   |     R     |       C        |    C     |  A   |       C       |      —       |        —        |          R          |
| Decommissioning beslissing         |   C   |     C     |       —        |    C     |  A   |       —       |      —       |        —        |          C          |

______________________________________________________________________

## Fase 6 — Doorlopende Verbetering

| Kernactiviteit               | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :--------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Retrospective faciliteren    |   A   |     C     |       C        |    C     |  I   |       —       |      R       |        —        |          —          |
| Kaizen Log bijhouden         |   R   |     C     |       C        |    A     |  I   |       —       |      —       |        —        |          —          |
| GAINS™ batenrealisatie meten |   A   |     —     |       R        |    C     |  C   |       —       |      —       |        —        |          —          |
| KPI-dashboard beheren        |   R   |     C     |       A        |    —     |  I   |       —       |      —       |        —        |          —          |

______________________________________________________________________

## Fase 7 — Project Afsluiting

| Kernactiviteit                 | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :----------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Lessons Learned sessie         |   A   |     R     |       R        |    C     |  C   |       C       |      R       |        C        |          C          |
| Eindrapportage batenrealisatie |   A   |     —     |       R        |    C     |  C   |       —       |      —       |        —        |          —          |
| Decommissioning uitvoeren      |   R   |     A     |       C        |    C     |  I   |       R       |      —       |        C        |          C          |
| Archivering & kennisoverdracht |   A   |     R     |       C        |    C     |  I   |       R       |      —       |        R        |          C          |

______________________________________________________________________

**Gerelateerde modules:**

- [Rollen & Verantwoordelijkheden — Overzicht](index.md)
- [Guardian Review Checklist](../09-sjablonen/15-guardian-review/template.md)
- [Fase-overzichten per fase](../02-fase-ontdekking/02-activiteiten.md)
