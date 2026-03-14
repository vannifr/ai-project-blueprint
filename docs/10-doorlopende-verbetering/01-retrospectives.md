---
versie: '1.0'
---

# 1. Retrospectives

## 1. Doelstelling

Wij evalueren gestructureerd en periodiek het functioneren van het AI-systeem én het team om verbeterpunten te identificeren, bij te sturen en te borgen in de volgende cyclus.

______________________________________________________________________

## 2. Intrede Criteria

- Het systeem is in productie (Gate 4 goedgekeurd).
- Monitoring is actief en levert meetbare data.
- Het beheerteam is samengesteld en heeft een vaste cadans afgesproken.

______________________________________________________________________

## 3. Kernactiviteiten

### Sprint Retrospective (tweewekelijks)

De sprint retrospective evalueert de werking van het team en het systeem over de afgelopen sprint. Gebruik het **Start / Stop / Doorgaan**-format als basis, aangevuld met AI-specifieke vragen:

- Welke datakwaliteitsproblemen zijn opgedoken?
- Welke outputs verrasten ons (positief of negatief)?
- Zijn er Rode Lijnen benaderd of overschreden?
- Hoe verliep de samenwerking met de Guardian?

**Duur:** 60 minuten. **Eigenaar:** AI Product Manager. **Output:** Actielijst in de backlog.

### Kwartaal Modelretrospective

Elk kwartaal evalueren wij het model zelf — niet enkel het team:

- Evolutie van de nauwkeurigheid ten opzichte van de nulmeting.
- Signalen van Drift: is de verdeling van invoerdata veranderd?
- Vergelijking met de oorspronkelijke Business Case: leveren we nog de beloofde waarde?
- Beoordeling van de Golden Set: zijn de testcases nog representatief?

**Duur:** 3 uur. **Eigenaar:** Data Scientist + AI PM. **Output:** Kwartaalrapport Modelgezondheid.

### AI-Specifieke Retrospective Vragen

Naast de gebruikelijke teaminzichten stellen wij bij elk AI-project ook:

| Dimensie           | Vraag                                                                                |
| :----------------- | :----------------------------------------------------------------------------------- |
| Datakwaliteit      | Zijn onze trainingsdata en productiedata nog in lijn?                                |
| Governance         | Hebben wij alle Rode Lijnen nageleefd deze sprint?                                   |
| Transparantie      | Kunnen wij aan de Guardian uitleggen waarom het systeem specifieke beslissingen nam? |
| Teamcapaciteit     | Heeft het team voldoende AI-kennis om het systeem te beheren?                        |
| Gebruikersfeedback | Wat zeggen eindgebruikers over de kwaliteit van de output?                           |

______________________________________________________________________

## 4. Team & Rollen

| Rol                | Verantwoordelijkheid                                    | R/A/C/I |
| :----------------- | :------------------------------------------------------ | :------ |
| AI Product Manager | Faciliteert de retrospective, bewaakt actielijst        | A       |
| Data Scientist     | Rapporteert over modelprestaties en Drift               | R       |
| MLOps Engineer     | Rapporteert over infrastructuur en monitoring           | R       |
| Guardian           | Evalueert naleving van Rode Lijnen en ethische aspecten | C       |
| Eindgebruikers     | Leveren feedback over kwaliteit van outputs             | C       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] Actielijst is gedocumenteerd in de backlog met eigenaar en deadline.
- [ ] Modelgezondheidsrapport (kwartaal) is gedeeld met de CAIO.
- [ ] Significante bevindingen zijn doorgegeven aan de Lessons Learned van het project.
- [ ] Beslissing over hertraining of aanpassing is gedocumenteerd.

______________________________________________________________________

## 6. Deliverables

| Deliverable                     | Beschrijving                                  | Eigenaar       |
| :------------------------------ | :-------------------------------------------- | :------------- |
| Actielijst sprint               | Concrete verbeterpunten met deadline          | AI PM          |
| Kwartaalrapport Modelgezondheid | Prestaties, Drift, Business Case-vergelijking | Data Scientist |
| Retrospective Notulen           | Beslissingen en discussiepunten               | AI PM          |

______________________________________________________________________

**Gerelateerde modules:**

- [Doorlopende Verbetering — Overzicht](index.md)
- [Kaizen Logs](02-kaizen-logs.md)
- [Metrics & Dashboards](03-metrics-dashboards.md)
- [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md)
- [Lessons Learned](../11-project-afsluiting/01-lessons-learned.md)

______________________________________________________________________

**Volgende stap:** [Registreer verbeteringen in het Kaizen Log](02-kaizen-logs.md)
→ Zie ook: [Metrics & Dashboards](03-metrics-dashboards.md)
