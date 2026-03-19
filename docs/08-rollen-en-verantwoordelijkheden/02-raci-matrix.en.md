---
versie: '1.1'
type: template
layer: 1
tags: [stakeholder, template]
---

# RACI Matrix — Roles per Phase

!!! abstract "Purpose"
    RACI overview that records who is responsible, accountable, consulted or informed per core activity and phase.

Central overview of who is **Responsible**, **Accountable**, **Consulted** and **Informed** per core activity, across all phases of the AI lifecycle.

**Legend:** R = Responsible (executor) · A = Accountable (final responsible) · C = Consulted (consulted) · I = Informed (informed) · — = Not involved

!!! info "One A per activity"
    Each activity has exactly one **A** (final responsible). Multiple R's are possible, but never multiple A's.

______________________________________________________________________

## Phase 1 — Discovery & Strategy

| Core Activity                                  | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :--------------------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Use case selection & prioritisation            |   A   |     C     |       C        |    C     |  I   |       —       |      —       |        —        |          —          |
| Stakeholder interviews & problem definition    |   R   |     C     |       —        |    I     |  I   |       —       |      C       |        —        |          —          |
| Collaboration mode assessment (autonomy level) |   R   |     C     |       —        |    C     |  I   |       —       |      —       |        —        |          C          |
| Risk Pre-Scan                                  |   R   |     C     |       C        |    A     |  I   |       —       |      —       |        —        |          C          |
| Objective Card (goal card) creation            |   A   |     C     |       —        |    R     |  I   |       —       |      —       |        —        |          —          |
| Define Hard Boundaries                         |   R   |     C     |       —        |    A     |  I   |       —       |      —       |        —        |          C          |
| Fast Lane decision                             |   A   |     R     |       —        |    C     |  C   |       —       |      —       |        —        |          —          |

______________________________________________________________________

## Phase 2 — Validation (PoV)

| Core Activity                            | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :--------------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| PoV scope and setup                      |   A   |     R     |       R        |    C     |  I   |       C       |      —       |        C        |          —          |
| Dataset exploration & quality assessment |   C   |     C     |       A        |    C     |  —   |       R       |      —       |        C        |          —          |
| Golden Set compilation                   |   C   |     C     |       A        |    C     |  —   |       R       |      —       |        C        |          —          |
| Business Case creation                   |   A   |     C     |       C        |    C     |  C   |       —       |      —       |        —        |          —          |
| Gate 2 Review                            |   A   |     C     |       C        |    R     |  C   |       —       |      —       |        —        |          C          |
| Guardian approval Gate 2                 |   —   |     —     |       —        |    A     |  —   |       —       |      —       |        —        |          —          |

______________________________________________________________________

## Phase 3 — Development

| Core Activity                        | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :----------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Sprint planning & backlog management |   A   |     C     |       C        |    —     |  I   |       —       |      —       |        —        |          —          |
| Model development (SDD pattern)      |   C   |     A     |       R        |    —     |  —   |       R       |      —       |        C        |          —          |
| Prompt engineering & versioning      |   R   |     A     |       C        |    C     |  —   |       —       |      —       |        R        |          —          |
| Data pipeline construction           |   C   |     C     |       R        |    —     |  —   |       A       |      —       |        C        |          —          |
| RAG architecture (if applicable)     |   C   |     A     |       R        |    —     |  —   |       R       |      —       |        R        |          —          |
| Technical Model Card                 |   C   |     A     |       R        |    C     |  —   |       —       |      —       |        —        |          —          |
| Red Teaming coordination             |   R   |     C     |       C        |    A     |  —   |       —       |      —       |        —        |          R          |
| Gate 3 Review                        |   A   |     R     |       C        |    C     |  C   |       —       |      —       |        —        |          C          |

______________________________________________________________________

## Phase 4 — Delivery

| Core Activity                         | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :------------------------------------ | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Go-live planning & coordination       |   A   |     R     |       —        |    C     |  I   |       C       |      C       |        —        |          C          |
| Technical implementation (deployment) |   C   |     A     |       —        |    —     |  —   |       R       |      —       |        C        |          C          |
| Traceability report                   |   A   |     C     |       R        |    C     |  —   |       —       |      —       |        —        |          —          |
| User training & adoption              |   C   |     —     |       —        |    —     |  I   |       —       |      A       |        C        |          —          |
| Handover to management organisation   |   A   |     R     |       C        |    C     |  C   |       C       |      C       |        C        |          C          |

______________________________________________________________________

## Phase 5 — Monitoring & Optimisation

| Core Activity                       | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :---------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Drift detection & monitoring        |   C   |     C     |       R        |    C     |  —   |       A       |      —       |        C        |          —          |
| Performance reporting               |   A   |     C     |       R        |    C     |  I   |       —       |      —       |        —        |          —          |
| Ethical oversight & bias monitoring |   C   |     —     |       R        |    A     |  I   |       —       |      —       |        —        |          C          |
| Model adjustment or retraining      |   C   |     A     |       R        |    C     |  I   |       R       |      —       |        C        |          —          |
| Incident response (execution)       |   R   |     R     |       C        |    C     |  A   |       C       |      —       |        —        |          R          |
| Decommissioning decision            |   C   |     C     |       —        |    C     |  A   |       —       |      —       |        —        |          C          |

______________________________________________________________________

## Phase 6 — Continuous Improvement

| Core Activity                       | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :---------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Facilitate retrospective            |   A   |     C     |       C        |    C     |  I   |       —       |      R       |        —        |          —          |
| Maintain Kaizen Log                 |   R   |     C     |       C        |    A     |  I   |       —       |      —       |        —        |          —          |
| Measure GAINS™ benefits realisation |   A   |     —     |       R        |    C     |  C   |       —       |      —       |        —        |          —          |
| Manage KPI dashboard                |   R   |     C     |       A        |    —     |  I   |       —       |      —       |        —        |          —          |

______________________________________________________________________

## Phase 7 — Project Closure

| Core Activity                     | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr | Context Builder | AI Security Officer |
| :-------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: | :-------------: | :-----------------: |
| Lessons Learned session           |   A   |     R     |       R        |    C     |  C   |       C       |      R       |        C        |          C          |
| Final benefits realisation report |   A   |     —     |       R        |    C     |  C   |       —       |      —       |        —        |          —          |
| Execute decommissioning           |   R   |     A     |       C        |    C     |  I   |       R       |      —       |        C        |          C          |
| Archiving & knowledge transfer    |   A   |     R     |       C        |    C     |  I   |       R       |      —       |        R        |          C          |

______________________________________________________________________

**Related modules:**

- [Roles & Responsibilities — Overview](index.md)
- [Guardian Review Checklist](../09-sjablonen/15-guardian-review/template.md)
- [Phase activity pages](../02-fase-ontdekking/02-activiteiten.md)
