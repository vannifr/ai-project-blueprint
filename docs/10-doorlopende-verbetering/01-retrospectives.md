---
versie: '1.0'
type: guide
layer: 2
phase: [1, 2, 3, 4, 5]
tags: [agile]
---

# 1. Retrospectives

!!! abstract "Doel"
    Gestructureerde evaluatie van het AI-systeem en het team om verbeterpunten te identificeren en te borgen in de volgende cyclus.

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
- Zijn er Harde Grenzen benaderd of overschreden?
- Hoe verliep de samenwerking met de Guardian?

#### Oorzaak-gevolg analyse (Root Cause Analysis)

Bij elk significant probleem voert het team een **grondige oorzaakanalyse** uit. Gebruik een van deze methoden:

- **5× Waarom:** Stel vijf keer de vraag "waarom?" om van symptoom naar grondoorzaak te komen.
- **Visgraatdiagram (Ishikawa):** Categoriseer oorzaken langs dimensies: Data, Model, Proces, Mens, Tooling.
- **Timeline-analyse:** Reconstrueer de tijdlijn van gebeurtenissen die tot het probleem leidden.

#### Veranderexperimenten

Elke retrospective resulteert in minstens één concreet **veranderexperiment** — een afgebakende aanpassing in werkwijze, proces of tooling die het team in de volgende sprint test:

| Element       | Beschrijving                                                                |
| :------------ | :-------------------------------------------------------------------------- |
| **Hypothese** | "Als we X veranderen, verwachten we Y verbetering."                         |
| **Meting**    | Hoe meten we of het experiment slaagt? (KPI, observatie, feedback)          |
| **Duur**      | Eén sprint — daarna evalueren en beslissen: behouden, aanpassen of stoppen. |
| **Eigenaar**  | Eén teamlid dat het experiment trekt.                                       |

**Duur:** 60 minuten. **Eigenaar:** AI Product Manager. **Output:** Actielijst + veranderexperiment in de backlog.

### Kwartaal Modelretrospective

Elk kwartaal evalueren wij het model zelf — niet enkel het team:

- Evolutie van de nauwkeurigheid ten opzichte van de nulmeting.
- Signalen van Drift: is de verdeling van invoerdata veranderd?
- Vergelijking met de oorspronkelijke Business Case: leveren we nog de beloofde waarde?
- Beoordeling van de Golden Set: zijn de testcases nog representatief?

**Duur:** 3 uur. **Eigenaar:** Data Scientist + AI PM. **Output:** Kwartaalrapport Model Health.

### AI-Specifieke Retrospective Vragen

Naast de gebruikelijke teaminzichten stellen wij bij elk AI-project ook:

| Dimensie           | Vraag                                                                                |
| :----------------- | :----------------------------------------------------------------------------------- |
| Datakwaliteit      | Zijn onze trainingsdata en productiedata nog in lijn?                                |
| Governance         | Hebben wij alle Harde Grenzen nageleefd deze sprint?                                 |
| Transparantie      | Kunnen wij aan de Guardian uitleggen waarom het systeem specifieke beslissingen nam? |
| Teamcapaciteit     | Heeft het team voldoende AI-kennis om het systeem te beheren?                        |
| Gebruikersfeedback | Wat zeggen eindgebruikers over de kwaliteit van de output?                           |

______________________________________________________________________

## 4. Team & Rollen

| Rol                | Verantwoordelijkheid                                      | R/A/C/I |
| :----------------- | :-------------------------------------------------------- | :------ |
| AI Product Manager | Faciliteert de retrospective, bewaakt actielijst          | A       |
| Data Scientist     | Rapporteert over modelprestaties en Drift                 | R       |
| MLOps Engineer     | Rapporteert over infrastructuur en monitoring             | R       |
| Guardian           | Evalueert naleving van Harde Grenzen en ethische aspecten | C       |
| Eindgebruikers     | Leveren feedback over kwaliteit van outputs               | C       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] Actielijst is gedocumenteerd in de backlog met eigenaar en deadline.
- [ ] Model Healthsrapport (kwartaal) is gedeeld met de CAIO.
- [ ] Significante bevindingen zijn doorgegeven aan de Lessons Learned van het project.
- [ ] Beslissing over hertraining of aanpassing is gedocumenteerd.

______________________________________________________________________

## 6. Deliverables

| Deliverable                  | Beschrijving                                  | Eigenaar       |
| :--------------------------- | :-------------------------------------------- | :------------- |
| Actielijst sprint            | Concrete verbeterpunten met deadline          | AI PM          |
| Kwartaalrapport Model Health | Prestaties, Drift, Business Case-vergelijking | Data Scientist |
| Retrospective Notulen        | Beslissingen en discussiepunten               | AI PM          |

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
