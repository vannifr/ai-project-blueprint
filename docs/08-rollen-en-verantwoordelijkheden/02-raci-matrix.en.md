---
versie: '1.0'
---

# RACI Matrix — Roles per Phase

Central overview of who is **Responsible**, **Accountable**, **Consulted** and **Informed** per core activity, across all phases of the AI lifecycle.

**Legend:** R = Responsible (executor) · A = Accountable (final responsible) · C = Consulted (consulted) · I = Informed (informed) · — = Not involved

!!! info "One A per activity"
    Each activity has exactly one **A** (final responsible). Multiple R's are possible, but never multiple A's.

______________________________________________________________________

## Phase 1 — Discovery & Strategy

| Core Activity                                  | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr |
| :--------------------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: |
| Use case selection & prioritisation            |   A   |     C     |       C        |    C     |  I   |       —       |      —       |
| Stakeholder interviews & problem definition    |   R   |     C     |       —        |    I     |  I   |       —       |      C       |
| Collaboration mode assessment (autonomy level) |   R   |     C     |       —        |    C     |  I   |       —       |      —       |
| Risk Pre-Scan                                  |   R   |     C     |       C        |    A     |  I   |       —       |      —       |
| Objective Card (goal card) creation            |   A   |     C     |       —        |    R     |  I   |       —       |      —       |
| Define Hard Boundaries                         |   R   |     C     |       —        |    A     |  I   |       —       |      —       |
| Fast Lane decision                             |   A   |     R     |       —        |    C     |  C   |       —       |      —       |

______________________________________________________________________

## Phase 2 — Validation (PoV)

| Core Activity                            | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr |
| :--------------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: |
| PoV scope and setup                      |   A   |     R     |       R        |    C     |  I   |       C       |      —       |
| Dataset exploration & quality assessment |   C   |     C     |       A        |    C     |  —   |       R       |      —       |
| Golden Set compilation                   |   C   |     C     |       A        |    C     |  —   |       R       |      —       |
| Business Case creation                   |   A   |     C     |       C        |    C     |  C   |       —       |      —       |
| Gate 2 Review                            |   A   |     C     |       C        |    R     |  C   |       —       |      —       |
| Guardian approval Gate 2                 |   —   |     —     |       —        |    A     |  —   |       —       |      —       |

______________________________________________________________________

## Phase 3 — Development

| Core Activity                        | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr |
| :----------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: |
| Sprint planning & backlog management |   A   |     C     |       C        |    —     |  I   |       —       |      —       |
| Model development (SDD pattern)      |   C   |     A     |       R        |    —     |  —   |       R       |      —       |
| Prompt engineering & versioning      |   R   |     A     |       C        |    C     |  —   |       —       |      —       |
| Data pipeline construction           |   C   |     C     |       R        |    —     |  —   |       A       |      —       |
| RAG architecture (if applicable)     |   C   |     A     |       R        |    —     |  —   |       R       |      —       |
| Technical Model Card                 |   C   |     A     |       R        |    C     |  —   |       —       |      —       |
| Red Teaming coordination             |   R   |     C     |       C        |    A     |  —   |       —       |      —       |
| Gate 3 Review                        |   A   |     R     |       C        |    C     |  C   |       —       |      —       |

______________________________________________________________________

## Phase 4 — Delivery

| Core Activity                         | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr |
| :------------------------------------ | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: |
| Go-live planning & coordination       |   A   |     R     |       —        |    C     |  I   |       C       |      C       |
| Technical implementation (deployment) |   C   |     A     |       —        |    —     |  —   |       R       |      —       |
| Traceability report                   |   A   |     C     |       R        |    C     |  —   |       —       |      —       |
| User training & adoption              |   C   |     —     |       —        |    —     |  I   |       —       |      A       |
| Handover to management organisation   |   A   |     R     |       C        |    C     |  C   |       C       |      C       |

______________________________________________________________________

## Phase 5 — Monitoring & Optimisation

| Core Activity                       | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr |
| :---------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: |
| Drift detection & monitoring        |   C   |     C     |       R        |    C     |  —   |       A       |      —       |
| Performance reporting               |   A   |     C     |       R        |    C     |  I   |       —       |      —       |
| Ethical oversight & bias monitoring |   C   |     —     |       R        |    A     |  I   |       —       |      —       |
| Model adjustment or retraining      |   C   |     A     |       R        |    C     |  I   |       R       |      —       |
| Incident response (execution)       |   R   |     R     |       C        |    C     |  A   |       C       |      —       |
| Decommissioning decision            |   C   |     C     |       —        |    C     |  A   |       —       |      —       |

______________________________________________________________________

## Phase 6 — Continuous Improvement

| Core Activity                       | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr |
| :---------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: |
| Facilitate retrospective            |   A   |     C     |       C        |    C     |  I   |       —       |      R       |
| Maintain Kaizen Log                 |   R   |     C     |       C        |    A     |  I   |       —       |      —       |
| Measure GAINS™ benefits realisation |   A   |     —     |       R        |    C     |  C   |       —       |      —       |
| Manage KPI dashboard                |   R   |     C     |       A        |    —     |  I   |       —       |      —       |

______________________________________________________________________

## Phase 7 — Project Closure

| Core Activity                     | AI PM | Tech Lead | Data Scientist | Guardian | CAIO | Data Engineer | Adoption Mgr |
| :-------------------------------- | :---: | :-------: | :------------: | :------: | :--: | :-----------: | :----------: |
| Lessons Learned session           |   A   |     R     |       R        |    C     |  C   |       C       |      R       |
| Final benefits realisation report |   A   |     —     |       R        |    C     |  C   |       —       |      —       |
| Execute decommissioning           |   R   |     A     |       C        |    C     |  I   |       R       |      —       |
| Archiving & knowledge transfer    |   A   |     R     |       C        |    C     |  I   |       R       |      —       |

______________________________________________________________________

**Related modules:**

- [Roles & Responsibilities — Overview](index.md)
- [Guardian Review Checklist](../09-sjablonen/15-guardian-review/template.md)
- [Phase activity pages](../02-fase-ontdekking/02-activiteiten.md)
