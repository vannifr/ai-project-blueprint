---
versie: '1.0'
type: technical
layer: 3
roles: [Tech Lead]
tags: [governance, security, mlops]
---

# 1. Agentic AI Engineering

## 1. Doel

Deze module beschrijft de engineering-praktijken voor het bouwen, testen en beheren van agentische AI-systemen (Samenwerkingsmodus 4-5). Waar de [AI Architectuur](05-ai-architectuur.md) het strategische patroon definieert, biedt dit document de operationele handleiding: orkestratie, protocollen, tool-ontwerp, faalpatronen, observeerbaarheid en kostenbeheersing.

!!! warning "Voorwaarde"
    Lees eerst [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md) en de [acceptatiecriteria voor Modus 4-5](../00-strategisch-kader/06-has-h-niveaus.md#4b-acceptatiecriteria-voor-modus-4-5-agentisch). Elke technische keuze in dit document wordt bepaald door de modus en het risicoprofiel.

______________________________________________________________________

## 2. Orkestratiepatronen

Een agent-systeem kiest een orkestratiepatroon op basis van taakcomplexiteit en risico. Begin altijd met het eenvoudigste patroon dat werkt.

### Enkele Agent

```
[Gebruiker/Trigger] → [Agent + Tools] → [Resultaat]
```

Eén LLM met directe toegang tot een set tools. Geschikt voor afgebakende taken met beperkte actieradius.

**Wanneer gebruiken:** Taken met helder doel, beperkte tool-set, lage tot gemiddelde complexiteit.

### Multi-Agent (Supervisor)

```
[Trigger] → [Supervisor Agent] → [Specialist Agent A] → [Resultaat A]
                                → [Specialist Agent B] → [Resultaat B]
                                → [Samenvoegen] → [Eindresultaat]
```

Een supervisor-agent verdeelt werk over gespecialiseerde sub-agents. Elke sub-agent heeft een afgebakende scope en eigen tool-set.

**Wanneer gebruiken:** Complexe taken die meerdere expertisegebieden vereisen, of taken die parallelliseerbaar zijn.

### Handoff-patroon

```
[Agent A] → [Overdrachtsmoment] → [Agent B] → [Overdrachtsmoment] → [Agent C]
```

Verantwoordelijkheid wordt overgedragen tussen agents naarmate de context evolueert. Elke agent verwerkt een specifieke fase.

**Wanneer gebruiken:** Sequentiële workflows met duidelijke fasegrenzen (bijv. analyse → plan → uitvoering → review).

### Keuzematrix

| Patroon      | Complexiteit | Risico         | Kosten    | Aanbevolen bij                   |
| :----------- | :----------- | :------------- | :-------- | :------------------------------- |
| Enkele Agent | Laag         | Laag-Gemiddeld | Laagst    | Afgebakende taken, Modus 4       |
| Supervisor   | Hoog         | Gemiddeld-Hoog | Hoger     | Parallelle expertises, Modus 4-5 |
| Handoff      | Gemiddeld    | Gemiddeld      | Gemiddeld | Sequentiële workflows, Modus 4   |

______________________________________________________________________

## 3. Protocollen en Standaarden

### Model Context Protocol (MCP)

MCP is een open standaard (Anthropic, 2024) die definieert hoe agents verbinding maken met externe tools, databronnen en API's. MCP biedt:

- **Gestandaardiseerde tool-beschrijvingen:** Tools worden beschreven in een uniform schema zodat elke MCP-compatibele agent ze kan aanroepen.
- **Transportlagen:** Stdio (lokaal) en Streamable HTTP (netwerk).
- **Beveiligingsmodel:** Server-identiteit, capability-registratie en toestemmingsbeheer.

**Aanbeveling:** Ontwerp nieuwe interne API's met MCP-compatibiliteit. Dit voorkomt vendor lock-in en maakt tools herbruikbaar over agent-frameworks heen.

### Agent-to-Agent (A2A) Protocol

A2A (Google, 2025; Linux Foundation) is een open standaard voor communicatie tussen agents van verschillende frameworks of leveranciers. Agents publiceren hun capaciteiten en onderhandelen over interactiemodaliteiten.

**Wanneer relevant:** Bij multi-agent systemen die agents van verschillende teams of leveranciers combineren.

______________________________________________________________________

## 4. Tool-Ontwerp voor Agents

### Ontwerpprincipes

1. **Allowlist-eerst:** Alleen expliciet toegestane tools zijn beschikbaar. Deny-by-default.
1. **Progressieve ontsluiting:** Geef de agent een korte tool-index; laat uitgebreide beschrijvingen pas laden wanneer nodig. Dit beperkt token-verbruik.
1. **Atomaire acties:** Elke tool doet exact één ding. Combineer niet "lezen en schrijven" in één tool.
1. **Idempotent waar mogelijk:** Herhaald aanroepen van dezelfde tool met dezelfde input mag geen bijwerkingen hebben.
1. **Sandbox-uitvoering:** Tools draaien in een geïsoleerde omgeving zonder directe toegang tot productiedata (zie [Technische Controls](05-ai-architectuur.md#technisch-afdwingbare-controls-verplicht-bij-samenwerkingsmodus-4-5)).

### Code Execution Pattern

In plaats van directe tool-aanroepen kan een agent code schrijven die tools aanroept. Dit biedt:

- On-demand laden van tools (lagere baseline token-kosten)
- Complexe logica in één stap (filtering, transformatie)
- Betere traceerbaarheid (code is inspectieerbaar)

**Risico:** Vereist strikte sandboxing. Gebruik uitsluitend met Modus 5-governance.

______________________________________________________________________

## 5. Agent Memory

Agents die langlopende taken uitvoeren of over meerdere sessies werken, hebben geheugen nodig. Wij onderscheiden vier typen:

| Type              | Beschrijving                                                                         | Opslagmedium         | Voorbeeld                                          |
| :---------------- | :----------------------------------------------------------------------------------- | :------------------- | :------------------------------------------------- |
| **Tokengeheugen** | Inhoud van het contextvenster (systeemprompt, gespreksgeschiedenis, tool-resultaten) | In-context           | Lopende conversatie                                |
| **Episodisch**    | Specifieke gebeurtenissen: wat gebeurde er, wanneer, met welk resultaat              | Database/bestand     | "Vorige ingebruikname faalde door schema-mismatch" |
| **Semantisch**    | Algemene kennis, feiten, relaties                                                    | Kennisbank/RAG       | Bedrijfsbeleid, productdocumentatie                |
| **Procedureel**   | Geleerde vaardigheden en operationele kennis                                         | Configuratie/prompts | Optimale volgorde van ingebruikname-stappen        |

**Aanbeveling:** Begin met tokengeheugen + RAG (semantisch). Voeg episodisch geheugen pas toe wanneer de agent terugkerende taken uitvoert en van eerdere resultaten moet leren.

______________________________________________________________________

## 6. Faalpatronen en Mitigatie

Agentische systemen falen kwalitatief anders dan traditionele software. De onderstaande patronen vereisen specifieke mitigatie.

| Faalpatroon                | Beschrijving                                                               | Impact                                      | Mitigatie                                                                       |
| :------------------------- | :------------------------------------------------------------------------- | :------------------------------------------ | :------------------------------------------------------------------------------ |
| **Oneindige lus**          | Agent genereert continu subtaken of herhaalt dezelfde actie                | Kostenexplosie, systeembelasting            | Harde iteratielimiet per taak; Circuit Breaker op token-budget                  |
| **Hallucinatie-escalatie** | Hallucinate output wordt input voor volgende stap, fouten stapelen zich op | Onbetrouwbare resultaten die correct lijken | Multi-staps validatie; tussentijdse factchecks; cross-validatie tussen modellen |
| **Scope creep**            | Agent interpreteert mandaat breder dan bedoeld                             | Ongeautoriseerde acties                     | Expliciete scopegrenzen in systeemprompt + tool-allowlist                       |
| **Tool-misbruik**          | Agent roept tools aan in onbedoelde combinaties of volgorde                | Data-corruptie, ongewenste bijwerkingen     | Tool-aanroepen loggen en valideren tegen toegestane sequenties                  |
| **Cascade-falen**          | Fout in sub-agent propageert door het hele systeem                         | Systeembrede storing                        | Isolatie per agent; foutgrenzen (error boundaries); graceful degradation        |
| **Stille degradatie**      | Kwaliteit daalt geleidelijk zonder zichtbare foutmelding                   | Onopgemerkt slechte output                  | Periodieke Golden Set validatie; acceptance rate monitoring                     |

!!! tip "Vuistregel"
    Elk faalpatroon moet een corresponderende alert hebben in het [monitoringdashboard](../10-doorlopende-verbetering/03-metrics-dashboards.md). Geen mitigatie zonder meetbaar signaal.

______________________________________________________________________

## 7. Observeerbaarheid

### Waarom agent-observeerbaarheid anders is

Traditionele monitoring meet **wat** er gebeurt (latency, errors, throughput). Agent-observeerbaarheid moet ook meten **waarom** iets gebeurt: welke beslissingen nam de agent, welke tools riep hij aan, en wat was de redenering?

### Minimale Telemetrie

| Datapunt             | Beschrijving                                                 | Doel                        |
| :------------------- | :----------------------------------------------------------- | :-------------------------- |
| **Beslissingsspoor** | Per stap: input, redenering, gekozen actie, vertrouwensscore | Audit, debugging            |
| **Tool-aanroepen**   | Welke tool, met welke parameters, resultaat, duur            | Kostenanalyse, foutdetectie |
| **Escalatie-events** | Wanneer en waarom de agent escaleerde naar een mens          | Scopevalidatie              |
| **Token-verbruik**   | Per stap en per sessie                                       | Kostenbeheersing            |
| **Sessie-uitkomst**  | Succes/faal, doorlooptijd, aantal stappen                    | Kwaliteitsmonitoring        |

### OpenTelemetry

OpenTelemetry heeft gestandaardiseerde semantische conventies voor AI-agent observeerbaarheid. Gebruik deze conventies om vendor-onafhankelijke tracing te implementeren. Dit maakt het mogelijk om agent-gedrag te analyseren ongeacht het onderliggende framework.

______________________________________________________________________

## 8. Kostenbeheersing

Agentische systemen hebben een fundamenteel ander kostenmodel dan traditionele AI-applicaties. Inferentiekosten zijn slechts circa 20% van de totale eigendomskosten.

### TCO-structuur

| Kostencategorie                  | Aandeel | Beheersmaatregel                          |
| :------------------------------- | :------ | :---------------------------------------- |
| Inferentie (API-tokens)          | ~20%    | Prompt caching, model tiering             |
| Data-voorbereiding en integratie | ~25%    | Gestandaardiseerde pipelines              |
| Governance en compliance         | ~20%    | Proportionele governance per risiconiveau |
| Monitoring en tuning             | ~15%    | Geautomatiseerde alerts, SLO-bewaking     |
| Training en onboarding           | ~20%    | Herbruikbare patronen en documentatie     |

### Optimalisatietechnieken

- **Prompt caching:** Als een agent steeds dezelfde systeemprompt gebruikt, kan de provider deze tokens cachen. Reduceert invoerkosten tot ~90% en latentie tot ~75%.
- **Model tiering:** Routeer eenvoudige taken naar een goedkoper model; complexe taken naar een capabeler model.
- **Dynamische iteratielimieten:** Stel het maximaal aantal stappen in op basis van taakcomplexiteit, niet als vast getal.
- **Harde budgetcap:** Technische limiet per taak/sessie/dag (zie [Technische Controls](05-ai-architectuur.md#technisch-afdwingbare-controls-verplicht-bij-samenwerkingsmodus-4-5)).

______________________________________________________________________

## 9. Agent-testen

### Teststrategie

Agent-testen gaat verder dan functionele tests. Wij testen op vier dimensies:

| Dimensie       | Wat testen                                                   | Methode                        |
| :------------- | :----------------------------------------------------------- | :----------------------------- |
| **Kwaliteit**  | Taakcompletering, juiste tool-selectie, redeneringskwaliteit | Golden Set scenario's          |
| **Prestaties** | Latentie, doorvoer, resource-gebruik                         | Belastingtests                 |
| **Veiligheid** | Prompt injection, scope-overschrijding, tool-misbruik        | Adversarial tests, red teaming |
| **Kosten**     | Token-verbruik per taak, kosten per succesvol resultaat      | Kostenbenchmarks               |

### Adversarial Scenario's (verplicht voor Modus 4-5)

- **Scope-test:** Geef de agent een opdracht buiten zijn mandaat. Verwacht: weigering of escalatie.
- **Lus-test:** Creëer een situatie die tot eindeloos herhalen kan leiden. Verwacht: stop na iteratielimiet.
- **Conflicterende instructies:** Geef tegenstrijdige context. Verwacht: escalatie, niet raden.
- **Tool-misbruik:** Bied tools aan die de agent niet mag gebruiken. Verwacht: geen aanroep.

______________________________________________________________________

## 10. Checklist Agentic AI Engineering

!!! check "10. Checklist Agentic AI Engineering"
    - [ ] Orkestratiepatroon is gekozen en gedocumenteerd
    - [ ] Tool-allowlist is gedefinieerd en afgedwongen
    - [ ] Sandbox-omgeving is ingericht voor tool-executie
    - [ ] Iteratielimieten en budgetcaps zijn geconfigureerd
    - [ ] Faalpatronen zijn geïdentificeerd met corresponderende alerts
    - [ ] Beslissingsspoor (audit trail) is actief per agent-stap
    - [ ] Escalatiepad naar mens is gedefinieerd en getest
    - [ ] Adversarial tests zijn uitgevoerd en gedocumenteerd
    - [ ] Kostenmodel is opgesteld (TCO, niet alleen inferentie)
    - [ ] OpenTelemetry of gelijkwaardige tracing is geïmplementeerd

______________________________________________________________________

## 11. Gerelateerde Modules

- [AI Architectuur — Patroon C: Agentic AI](05-ai-architectuur.md)
- [AI-Samenwerkingsmodi (Modus 4-5)](../00-strategisch-kader/06-has-h-niveaus.md)
- [AI Safety Checklist](../07-compliance-hub/08-ai-safety-checklist.md)
- [Red Teaming](../07-compliance-hub/07-red-teaming.md)
- [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
- [Kostenoptimalisatie](07-kostenoptimalisatie.md)

______________________________________________________________________
