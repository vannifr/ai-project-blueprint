# ?? Artefact Model

## ?? Beheer-Artefacten
Om AI-systemen beheersbaar te maken, beheren we specifieke artefacten die grip geven op het gedrag.

| Artefact | Doel | Eigenaar | Formaat |
| :--- | :--- | :--- | :--- |
| **Doeldefinitie** | **Business hypothese:** Welke uitkomst wordt nagestreefd? (*Intent*) | AI Product Manager | Gestructureerde statement ("Gegeven X, als Y, dan Z") |
| **Rode Lijnen** | **Harde grenzen:** Wat mag NOOIT gebeuren? (*Constraints*) | Guardian (Ethicist) | IF/THEN regels ("ALS PII, DAN blokkeren") |
| **Sturingsinstructies** | **Sturing:** De configuratie die de AI stuurt (prompts, RAG). | ML Engineer | Versiebeheerde config (JSON/YAML/Markdown) |
| **Validatierapport** | **Bewijs:** Resultaten van testen en metingen (*Evidence*). | QA Engineer | Gestructureerd rapport met metrics |
| **Traceerbaarheid** | **Verbinding:** Koppeling tussen Doel ? Instructie ? Bewijs. | ML Engineer | Referenties (ID's / Git SHAs) |

---
**Versie:** 2.0
**Datum:** 31 januari 2026
**Status:** Definitief

---
© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
