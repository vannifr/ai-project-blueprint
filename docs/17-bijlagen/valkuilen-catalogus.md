---
versie: '1.0'
type: reference
layer: 3
answers: [Wat is Valkuilencatalogus voor AI-Projecten?]
---

# 1. Valkuilencatalogus voor AI-Projecten

## 1. Doel

Deze catalogus bundelt de meest voorkomende valkuilen bij AI-projecten, gegroepeerd per thema. Elke valkuil bevat een beschrijving, het risico en een verwijzing naar de Blueprint-module die de mitigatie beschrijft.

______________________________________________________________________

## 2. Governance & Organisatie

| #    | Valkuil                                                                                                   | Risico                                              | Mitigatie (Blueprint-verwijzing)                                           |
| :--- | :-------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- | :------------------------------------------------------------------------- |
| G-01 | **Geen governance-kader** — AI-projecten starten zonder duidelijke rollen, gates of verantwoordelijkheden | Oncontroleerbare uitkomsten, compliance-risico      | [Governance Model](../00-strategisch-kader/03-governance-model.md)         |
| G-02 | **Rubber stamping** — Menselijke reviewer keurt AI-output blind goed                                      | Fouten passeren onopgemerkt                         | [Samenwerkingsmodi — Modus 2](../00-strategisch-kader/06-has-h-niveaus.md) |
| G-03 | **Wildgroei van AI-tools** — Teams gebruiken ongekeurde AI-diensten                                       | Data-lekken, vendor lock-in, compliance-schendingen | [Approved Tools](../07-compliance-hub/08-ai-safety-checklist.md)           |
| G-04 | **Ontbrekende escalatiepaden** — Geen duidelijke procedure wanneer AI faalt                               | Vertraagde respons bij incidenten                   | [Incident Playbooks](../07-compliance-hub/06-incidentrespons-playbooks.md) |
| G-05 | **Governance als blokkade** — Te zware governance voor laag-risico toepassingen                           | Vertraagde time-to-value, frustratie bij teams      | [Fast Lane](../02-fase-ontdekking/06-fast-lane.md)                         |

______________________________________________________________________

## 3. Technisch & Engineering

| #    | Valkuil                                                                             | Risico                                               | Mitigatie (Blueprint-verwijzing)                                                           |
| :--- | :---------------------------------------------------------------------------------- | :--------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| T-01 | **Blind copy-paste** — AI-code accepteren zonder begrip                             | Verborgen bugs, veiligheidslekken, technische schuld | [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)                 |
| T-02 | **Prompt-perfectionisme** — Meer tijd aan de prompt dan aan de oplossing            | Vertraagde oplevering                                | [Engineering Patterns — Anti-patterns](../04-fase-ontwikkeling/06-engineering-patterns.md) |
| T-03 | **Ongevalideerde keten** — Meerdere AI-stappen zonder tussentijdse controle         | Hallucinatie-escalatie                               | [Validatiemodel](../01-ai-native-fundamenten/04-validatie-model.md)                        |
| T-04 | **Technische schuld door AI** — AI genereert code sneller dan het team kan reviewen | Schuld accumuleert exponentieel                      | [SDD Patroon](../04-fase-ontwikkeling/05-sdd-patroon.md)                                   |
| T-05 | **Context-vervuiling** — Te veel of irrelevante context aangeboden aan AI           | Lagere kwaliteit, hogere kosten                      | [Context Builder](../08-rollen-en-verantwoordelijkheden/index.md)                          |
| T-06 | **Oneindige agent-lus** — Agent herhaalt stappen zonder voortgang                   | Kostenexplosie                                       | [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)        |
| T-07 | **Scope creep bij agents** — Agent interpreteert mandaat breder dan bedoeld         | Ongeautoriseerde acties                              | [Acceptatiecriteria Modus 4-5](../00-strategisch-kader/06-has-h-niveaus.md)                |

______________________________________________________________________

## 4. Data & Kwaliteit

| #    | Valkuil                                                                                    | Risico                                                     | Mitigatie (Blueprint-verwijzing)                                               |
| :--- | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------- | :----------------------------------------------------------------------------- |
| D-01 | **Data-bias niet gedetecteerd** — Trainings- of RAG-data bevat systematische vertekeningen | Discriminerende output                                     | [Ethische Richtlijnen](../07-compliance-hub/03-ethische-richtlijnen.md)        |
| D-02 | **Geen baseline** — Geen meting van huidige prestaties voor AI-inzet                       | Onmogelijk om verbetering aan te tonen                     | [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md) |
| D-03 | **Stille degradatie** — Modelkwaliteit daalt geleidelijk zonder alarm                      | Gebruikers krijgen steeds slechtere output                 | [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md)                   |
| D-04 | **Hallucinaties niet gemitigeerd** — AI genereert plausibele maar onjuiste feiten          | Juridisch risico, reputatieschade                          | [Red Teaming](../07-compliance-hub/07-red-teaming.md)                          |
| D-05 | **Verouderde kennisbank** — RAG-bronnen worden niet bijgewerkt                             | Incorrecte antwoorden op basis van achterhaalde informatie | [Beheer & Optimalisatie](../06-fase-monitoring/02-activiteiten.md)             |

______________________________________________________________________

## 5. Organisatie & Mensen

| #    | Valkuil                                                                                   | Risico                                                  | Mitigatie (Blueprint-verwijzing)                                                  |
| :--- | :---------------------------------------------------------------------------------------- | :------------------------------------------------------ | :-------------------------------------------------------------------------------- |
| O-01 | **Expertise-erosie** — Team verliest vakkennis omdat AI het werk overneemt                | Niemand kan AI-output meer beoordelen                   | [Samenwerkingsmodi — Modus 4 risico](../00-strategisch-kader/06-has-h-niveaus.md) |
| O-02 | **AI-theater** — Pilots zonder meetbare business-waarde                                   | Budget verspild, stakeholder-vermoeidheid               | [Batenrealisatie](../10-doorlopende-verbetering/04-batenrealisatie.md)            |
| O-03 | **Geen adoptiestrategie** — AI-tools beschikbaar maar niet gebruikt                       | Licentiekosten zonder waarde                            | [Adoptie Manager](../08-rollen-en-verantwoordelijkheden/index.md)                 |
| O-04 | **Oversprong naar autonomie** — Direct naar Modus 4-5 zonder leerfases                    | Onbeheersbare systemen                                  | [Begin laag, schaal op](../00-strategisch-kader/06-has-h-niveaus.md)              |
| O-05 | **Ontbrekende eigenaar** — Geen duidelijke verantwoordelijke voor AI-systeem in productie | Drift wordt niet opgemerkt, incidenten niet afgehandeld | [Rollen & Verantwoordelijkheden](../08-rollen-en-verantwoordelijkheden/index.md)  |

______________________________________________________________________

## 6. Kosten & ROI

| #    | Valkuil                                                                            | Risico                                         | Mitigatie (Blueprint-verwijzing)                                                                       |
| :--- | :--------------------------------------------------------------------------------- | :--------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| K-01 | **Alleen inferentiekosten berekend** — TCO mist governance, monitoring, integratie | Budget-overschrijding                          | [Kostenoptimalisatie](../08-technische-standaarden/07-kostenoptimalisatie.md)                          |
| K-02 | **Geen kostenlimiet per agent-taak** — Agent draait onbeperkt                      | Bill shock door oneindige loops                | [Agentic AI Engineering — Kostenbeheersing](../08-technische-standaarden/09-agentic-ai-engineering.md) |
| K-03 | **ROI te vroeg gemeten** — Na 4-6 weken conclusies trekken over waarde             | Voortijdige annulering van kansrijke projecten | [Batenrealisatie](../10-doorlopende-verbetering/04-batenrealisatie.md)                                 |
| K-04 | **Rework niet gemeten** — Tijdswinst door AI wordt tenietgedaan door correctiewerk | Vals productiviteitsbeeld                      | [Engineering Patterns — Rework](../04-fase-ontwikkeling/06-engineering-patterns.md)                    |

______________________________________________________________________

## 7. Gebruik van deze Catalogus

- **Bij projectstart:** Loop de categorieën door die relevant zijn voor het risicoprofiel.
- **Bij gate reviews:** Controleer of de geïdentificeerde valkuilen zijn gemitigeerd.
- **Bij retrospectives:** Gebruik de catalogus als checklist voor lessen geleerd.

______________________________________________________________________

## 8. Gerelateerde Modules

- [Governance Model](../00-strategisch-kader/03-governance-model.md)
- [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)
- [Risicobeheer](../07-compliance-hub/02-risicobeheer/index.md)

______________________________________________________________________
