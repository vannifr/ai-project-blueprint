---
versie: '1.1'
type: foundation
layer: 1
roles: [Data Scientist]
tags: [governance]
summary: Overzicht van de beheer-artefacten (Doeldefinitie, Harde Grenzen, Prompts, Validatierapport en Traceerbaarheid) die grip geven op AI-systeemgedrag.
answers: [Wat houdt Artefact Model in?, Hoeveel validatie is voldoende?]
---

# 1. Artefact Model

!!! abstract "Doel"
    Overzicht van de beheer-artefacten (Doeldefinitie, Harde Grenzen, Prompts, Validatierapport en Traceerbaarheid) die grip geven op AI-systeemgedrag.

## 1. Beheer-Artefacten

Om AI-systemen beheersbaar te maken, beheren we specifieke artefacten die grip geven op het gedrag.

| Artefact             | Doel                                                                 | Eigenaar            | Formaat                                                                                      |
| :------------------- | :------------------------------------------------------------------- | :------------------ | :------------------------------------------------------------------------------------------- |
| **Doeldefinitie**    | **Business hypothese:** Welke uitkomst wordt nagestreefd? (*Intent*) | AI Product Manager  | Gestructureerde statement ("Gegeven X, als Y, dan Z")                                        |
| **Harde Grenzen**    | **Harde grenzen:** Wat mag NOOIT gebeuren? (*Constraints*)           | Guardian (Ethicist) | IF/THEN regels ("ALS PII, DAN blokkeren")                                                    |
| **Prompts**          | **Sturing:** De configuratie die de AI stuurt (prompts, RAG).        | AI Engineer / Team  | Versiebeheerde config (bijvoorbeeld YAML, JSON, Markdown of andere gestructureerde formaten) |
| **Validatierapport** | **Bewijs:** Resultaten van testen en metingen (*Evidence*).          | QA Engineer         | Gestructureerd rapport met metrics                                                           |
| **Traceerbaarheid**  | **Verbinding:** Koppeling tussen Doel Instructie Bewijs.             | ML Engineer         | Referenties (ID's / Git SHAs)                                                                |

Prompts omvatten niet alleen prompts, maar alle informatie en configuraties die het gedrag van het systeem beïnvloeden, waaronder gekoppelde kennisbronnen, toegestane acties, technische beperkingen, bewaartermijnen en regels voor gebruik en escalatie.

______________________________________________________________________
