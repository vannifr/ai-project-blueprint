---
versie: '1.0'
type: technical
layer: 3
roles: [Tech Lead]
---

# 1. AI Architectuur

!!! abstract "Doel"
    Overzicht van de meest voorkomende architectuurpatronen voor AI-systemen en de overwegingen bij het kiezen van de juiste aanpak.

## 1. Doel

Deze module beschrijft de meest voorkomende architectuurpatronen voor AI-systemen en de overwegingen bij het kiezen van de juiste aanpak. Een goede architectuur balanceert functionaliteit, schaalbaarheid, kosten en veiligheid.

______________________________________________________________________

## 2. Basisarchitectuur: De AI-Stack

Elke AI-oplossing bestaat uit een aantal lagen die samenwerken:

```
┌─────────────────────────────────────────┐
│ Gebruikersinterface │ Web, App, API, Chat
├─────────────────────────────────────────┤
│ Orkestratie-laag │ Routing, workflow, caching
├─────────────────────────────────────────┤
│ AI-Kern (Model) │ LLM, classifier, etc.
├─────────────────────────────────────────┤
│ RAG │ Vectorstore, documenten
├─────────────────────────────────────────┤
│ Data-laag │ Databases, logging, storage
└─────────────────────────────────────────┘
```

______________________________________________________________________

## 3. Referentiearchitecturen

### Patroon A: Directe LLM-integratie

**Omschrijving:** Gebruiker communiceert direct met een LLM via een simpele interface.

```
[Gebruiker] → [API Gateway] → [LLM Provider] → [Response]
```

**Kenmerken:**

| Aspect        | Waarde                                     |
| ------------- | ------------------------------------------ |
| Complexiteit  | Laag                                       |
| Kosten        | Variabel (per API-call)                    |
| Latency       | Afhankelijk van provider                   |
| Data-isolatie | Data gaat naar externe provider            |
| Geschikt voor | Prototypes, interne tools, Minimaal risico |

**Aandachtspunten:**

- Zorg voor rate limiting en kostenbewaking
- Log alle interacties conform [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- Implementeer Harde Grenzen via system prompts

### Patroon B: RAG

**Omschrijving:** LLM wordt verrijkt met bedrijfsspecifieke informatie uit een kennisbank.

```
[Gebruiker] → [Orkestratie] → [Vectorstore Query] → [Context + Prompt] → [LLM] → [Response]
```

**Kenmerken:**

| Aspect        | Waarde                                   |
| ------------- | ---------------------------------------- |
| Complexiteit  | Midden                                   |
| Kosten        | Vectorstore + LLM API                    |
| Latency       | Hoger (extra query-stap)                 |
| Data-isolatie | Kennisbank blijft intern mogelijk        |
| Geschikt voor | Klantenservice, documentatie-assistenten |

**Componenten:**

- **Document Processor:** Splitst documenten in chunks
- **Embedding Model:** Converteert tekst naar vectoren
- **Vectorstore:** Slaat en doorzoekt vectoren (Pinecone, Weaviate, pgvector)
- **Retriever:** Haalt relevante context op basis van query
- **LLM:** Genereert antwoord met context

**Aandachtspunten:**

- Chunk-grootte beïnvloedt kwaliteit en kosten
- Embedding-model moet passen bij taal en domein
- Log bronverwijzingen voor traceerbaarheid

### Patroon C: Agentic AI (Autonome Systemen)

**Omschrijving:** AI-systeem dat zelfstandig taken uitvoert, tools aanroept en beslissingen neemt.

```
[Gebruiker/Trigger] → [Agent Orchestrator] → [Beslissen] → [Tool Aanroepen] → [Evalueren] → [Volgende Stap of Response]
```

**Kenmerken:**

| Aspect        | Waarde                                       |
| ------------- | -------------------------------------------- |
| Complexiteit  | Hoog                                         |
| Kosten        | Variabel, kan snel oplopen                   |
| Latency       | Variabel (meerdere stappen)                  |
| Data-isolatie | Afhankelijk van tools                        |
| Geschikt voor | Automatisering, research, complexe workflows |

**Vereisten (Samenwerkingsmodus 4-5):**

- **Actieradius beperking:** Definieer welke tools beschikbaar zijn
- **Budget limieten:** Maximale kosten per taak
- **Circuit Breaker:** Automatische stop bij afwijkend gedrag
- **Menselijke escalatie:** Definieer wanneer mens moet ingrijpen
- **Uitgebreide logging:** Elke beslissing en actie vastleggen

**Aandachtspunten:**

- Begin met beperkte actieradius, breid geleidelijk uit
- Test uitgebreid met adversarial scenario's
- Guardian review verplicht voor Hoog Risico

#### Technisch afdwingbare controls (verplicht bij Samenwerkingsmodus 4–5)

Voor agentic AI-systemen die autonoom acties uitvoeren, zijn de volgende technische controls verplicht.

| Control                                | Beschrijving                                                                                                                     |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Tool allowlist                         | Expliciete lijst van toegestane tools; niet-geautoriseerde tools worden geblokkeerd.                                             |
| Capability-based access control (CBAC) | Toegangsrechten worden toegekend op basis van capabilities (wat mag), eventueel bovenop RBAC (wie is het).                       |
| Sandboxed tool execution               | Tools worden uitgevoerd in een geïsoleerde omgeving zonder directe toegang tot productiesystemen.                                |
| Just-in-time permissies                | Rechten worden enkel verleend op het moment van uitvoering en voor de minimaal benodigde scope.                                  |
| Per-taak budget/spend limit            | Maximale kosten of resources per individuele taak of sessie.                                                                     |
| Deny-by-default network egress         | Uitgaand netwerkverkeer is standaard geblokkeerd; enkel expliciete bestemmingen worden toegestaan.                               |
| Harde Budget Cap (Cost Guardrail)      | Technische limiet op API-kosten per dag/maand (via API-gateway of provider). Voorkomt "bill shock" door oneindige loops of DDOS. |
| Rate Limiting                          | Maximaal aantal requests per gebruiker per minuut. Beschermt tegen misbruik en kostenexplosie.                                   |

Bron: \[so-1\]

______________________________________________________________________

## 4. Architectuurbeslissingen

### Cloud vs On-Premise

| Factor              | Cloud (API)                   | On-Premise / Private Cloud   |
| ------------------- | ----------------------------- | ---------------------------- |
| Opstartkosten       | Laag                          | Hoog                         |
| Operationele kosten | Variabel per gebruik          | Vast (infra + onderhoud)     |
| Schaalbaarheid      | Automatisch                   | Handmatig                    |
| Data-soevereiniteit | Data naar provider            | Data blijft intern           |
| Latency             | Afhankelijk van netwerk       | Potentieel lager             |
| Geschikt voor       | Prototypes, variabele volumes | Strenge privacy, hoog volume |

### Modelkeuze

| Overweging       | Foundation Model (GPT, Claude) | Fine-tuned / Custom Model            |
| ---------------- | ------------------------------ | ------------------------------------ |
| Tijd tot live    | Snel (dagen)                   | Langzaam (weken-maanden)             |
| Flexibiliteit    | Hoog, breed inzetbaar          | Geoptimaliseerd voor specifieke taak |
| Kosten per query | Hoger                          | Potentieel lager                     |
| Onderhoud        | Provider verantwoordelijk      | Team verantwoordelijk                |
| Geschikt voor    | Generieke taken, prototypes    | Hoog volume, specialistische taken   |

______________________________________________________________________

## 5. Beveiligingsarchitectuur

### Minimale Beveiligingslagen

| Laag             | Maatregel                             |
| ---------------- | ------------------------------------- |
| Netwerk          | HTTPS, API gateway, firewall          |
| Authenticatie    | API keys, OAuth, service accounts     |
| Autorisatie      | Role-based access (wie mag wat?)      |
| Input validatie  | Sanitization, length limits           |
| Output filtering | PII detectie, content filtering       |
| Logging          | Audit trail conform Bewijsstandaarden |

### Specifiek voor AI

- **Prompt injection bescherming:** Scheiding system/user prompts
- **Rate limiting:** Per gebruiker en totaal
- **Kostenbewaking:** Alerts bij onverwacht hoog gebruik
- **Model toegang:** Beperkte toegang tot productiemodellen

______________________________________________________________________

## 6. Schaalbaarheid

### Typische Bottlenecks

| Component   | Bottleneck                        | Oplossing                  |
| ----------- | --------------------------------- | -------------------------- |
| LLM API     | Rate limits, kosten               | Caching, batching, queuing |
| Vectorstore | Query latency bij veel documenten | Indexing, sharding         |
| Orkestratie | Complexe workflows                | Async processing, workers  |

### Schaalstrategieën

| Strategie        | Wanneer toepassen                    |
| ---------------- | ------------------------------------ |
| Response caching | Herhalende vragen, statische content |
| Semantic caching | Vergelijkbare vragen                 |
| Batching         | Veel gelijktijdige requests          |
| Model tiering    | Simpele vragen naar goedkoper model  |

______________________________________________________________________

## 7. Checklist Architectuur

!!! check "7. Checklist Architectuur"
    - [ ] Architectuurpatroon is gekozen en gedocumenteerd
    - [ ] Beveiligingslagen zijn geïmplementeerd
    - [ ] Schaalbaarheid is overwogen
    - [ ] Kosteninschatting is gemaakt
    - [ ] Logging en monitoring zijn ingericht
    - [ ] Harde Grenzen zijn geïmplementeerd in de architectuur
    - [ ] Rollback-strategie is gedefinieerd

______________________________________________________________________

## 8. Gerelateerde Modules

- [Technische Standaarden & Leveringscriteria](01-mloops-standaarden.md)
- [Model Governance](03-model-governance.md)
- [Risicobeheersing & Compliance](../07-compliance-hub/index.md)
- [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)
- [Agentic AI Engineering](09-agentic-ai-engineering.md)
