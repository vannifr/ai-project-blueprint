# Huisstijl & Schrijfwijzer (Styleguide v2.3)

Deze blauwdruk borgt dat alle modules in het Playbook consistent, begrijpelijk en uniform blijven. Versie 2.3 integreert lessen uit de redactionele audit van maart 2026: scherpere regels rond redundantie, verplichte koppeling van Samenwerkingsmodi bij gates, CTA-structuur per module, en uitbreiding van de terminologietabel.

**Taal:** De Blauwdruk is beschikbaar in **Nederlands (standaard)** en **Engels**. Geen andere talen.

______________________________________________________________________

## Toon & Stem (Tone of Voice)

Wij schrijven voor professionals die actie willen ondernemen. Onze taal is direct, activerend en zelfverzekerd.

- **Formele aanspreekvorm (Vlaamse standaard):** Gebruik consequent **"u"** en **"uw"**. Vermijd de informele "je/jou"-vorm voor een zakelijke uitstraling.
- **Actief boven Passief:**
    - ❌ Fout: "Door het team zal worden beoordeeld of de data geschikt is."
    - ✅ Goed: "Het team evalueert de data."
- **De "Wij"-vorm:** We schrijven vanuit het perspectief van het projectteam. "Wij bouwen", "Wij toetsen".
- **Geen Academisch Jargon:** Vermijd onduidelijke of te theoretische taal. We schrijven een praktische handleiding.
- **Instructief register per laag:**
    - Laag 1 (Strategie): overtuigend, beknopt, directieniveau — geen stappenlijsten
    - Laag 2 (Fasen): stapsgewijs, instructief, teamgericht — gebruik imperatief ("Stel vast", "Beoordeel")
    - Laag 3 (Toolkit): functioneel, scanbaar, zonder proza — tabellen en checklists boven doorlopende tekst

______________________________________________________________________

## Single Source of Truth — de anti-redundantieregel

> **Kernregel: één concept, één thuis. Alle andere verwijzingen linken daarnaar.**

De AI-levenscyclus, de vijf samenwerkingsmodi, de vier kernartefacten en de risicoclassificatie worden **één keer volledig uitgelegd** — in hun canoniek thuis-document. Alle andere modules verwijzen ernaar; ze herhalen de uitleg **niet**.

| Concept                                                         | Canoniek thuis-document                                   |
| :-------------------------------------------------------------- | :-------------------------------------------------------- |
| AI-levenscyclus (5 fasen)                                       | `docs/00-strategisch-kader/01-ai-levenscyclus.md`         |
| Samenwerkingsmodi (Modus 1–5)                                   | `docs/00-strategisch-kader/06-has-h-niveaus.md`           |
| Kernartefacten (doeldefinitie, rode lijnen, prompts, validatie) | `docs/01-ai-native-fundamenten/01-definitie.md`           |
| Risicoclassificatie (piramide)                                  | `docs/01-ai-native-fundamenten/05-risicoclassificatie.md` |
| Bewijsstandaarden per risicoklasse                              | `docs/01-ai-native-fundamenten/07-bewijsstandaarden.md`   |
| Gate-criteria (4 gates)                                         | `docs/09-sjablonen/08-gate-reviews/template.md`           |

**Praktische toets:** Staat hetzelfde in meer dan één document? Behoud de versie in het canoniek thuis-document. Vervang alle andere instanties door een verwijzing in de stijl: `→ Zie [Samenwerkingsmodi](../../00-strategisch-kader/06-has-h-niveaus.md) voor de volledige uitleg.`

______________________________________________________________________

## Samenwerkingsmodi — verplichte koppeling bij gates

Elke fase-gate en elk sjabloon dat een go/no-go bevat, **vermeldt expliciet de relevante samenwerkingsmodus (Modus 1–5)** als ontwerpbeperking.

**Vaste formulering bij gates:**

```markdown
**Samenwerkingsmodus:** [Modus X — Naam]
Vereiste validatie voor deze modus: [verwijzing naar 01.07 Bewijsstandaarden]
```

**Richtlijn per fase:**

| Fase            | Gebruikelijke modi | Wat te vermelden                                               |
| :-------------- | :----------------- | :------------------------------------------------------------- |
| Verkenning (02) | 1–3                | Beoogde modus benoemen als ontwerpkeuze in Project Charter     |
| Validatie (03)  | 1–3                | Modus toetsen in Gate 2 (klopt de modus bij het risiconiveau?) |
| Realisatie (04) | 1–4                | SDD-specificatie vermeldt de modus als constraint              |
| Levering (05)   | 1–4                | Overdrachtsprotocol specificeert menselijk toezicht per modus  |
| Beheer (06)     | alle               | Driftdrempels en menselijk controlepunt afhankelijk van modus  |

______________________________________________________________________

## Terminologie & Lexicon (De Vertaallijst)

Wij slaan de brug tussen techniek en business. Gebruik de onderstaande tabel voor een consistente woordkeuze die zowel technisch accuraat als grammaticaal correct is voor een Vlaams publiek.

> **Opmerking v2.3:** De tabel reflecteert de **huidige documentstandaard**. Termen zijn bewust afgestemd op internationaal gangbaar vakjargon dat door de doelgroep herkend wordt.

| ❌ Vermijd (NL-Nederlands / Jargon)             | ✅ Gebruik (Huidige Standaard)              | Toelichting                                                                                           |
| :---------------------------------------------- | :------------------------------------------ | :---------------------------------------------------------------------------------------------------- |
| Het Kostenplaatje                               | **Het Kostenoverzicht**                     | Zakelijker en formeler                                                                                |
| Inregelen                                       | **Instellen / Configureren**                | Standaard IT-taal                                                                                     |
| U pakt                                          | **U raadpleegt**                            | Correcter taalgebruik                                                                                 |
| Gereedschapskist                                | **Toolkit**                                 | Gangbare term in de sector                                                                            |
| Intent Record                                   | **Doeldefinitie**                           | Het 'Waarom'                                                                                          |
| Context Artifacts / Sturingsinstructies         | **Prompts**                                 | Internationaal gangbaar; schrijf als "Prompts"                                                        |
| Guardrails                                      | **Rode Lijnen**                             | De harde grenzen                                                                                      |
| Proof of Value (PoV) / Praktijkproef            | **Proof of Value (PoV)**                    | PoV is de standaard; voeg bij eerste gebruik voluit toe                                               |
| Model Drift / Prestatieverloop                  | **Drift**                                   | Schrijf als "Drift" — internationaal herkend; voeg bij eerste gebruik toe: "Drift (prestatieverloop)" |
| Retrieval Augmented Gen / Kenniskoppeling       | **RAG**                                     | Schrijf als "RAG"; geen Nederlandse vertaling verplicht                                               |
| Hyperparameter Tuning / Afstellen van het model | **Fine-tunen**                              | Fine-tunen is de gestandaardiseerde term in dit playbook                                              |
| Shadow AI                                       | **Wildgroei**                               | Ongecontroleerd gebruik                                                                               |
| Deployment                                      | **Ingebruikname / Livegang**                |                                                                                                       |
| Fairness audit / Eerlijkheidstoets              | **Fairness audit (bias audit)**             | Gebruik beide termen bij eerste vermelding                                                            |
| Batenrealisatie                                 | **Waarderealisatie (benefits realization)** | Gebruik volledige term bij eerste vermelding per document                                             |
| Doelkaart                                       | **Doelkaart (goal card)**                   | Gebruik altijd met EN-equivalent bij eerste vermelding                                                |

______________________________________________________________________

## Agentische AI — terminologie

| ❌ Vermijd                         | ✅ Gebruik (Blauwdruk-standaard) | Toelichting                                                                                                                   |
| ---------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| AI-agent / bot                     | **Agent**                        | Schrijf zonder lidwoord-koppeling; "de agent" is correct                                                                      |
| Multi-agent systeem                | **Multi-agentsysteem**           | Aaneengeschreven; gebruik bij eerste vermelding: "multi-agentsysteem (meerdere samenwerkende agents)"                         |
| Orchestrator / dirigent            | **Orchestrator**                 | Internationaal gangbaar; geen vertaling                                                                                       |
| Tool calls / gereedschapsaanroepen | **Tool-aanroepen**               | Met koppelteken; enkelvoud: "tool-aanroep"                                                                                    |
| Memory / geheugen                  | **Agent-geheugen**               | Specificeer altijd type bij eerste vermelding: korte-termijngeheugen (contextvenster) of lange-termijngeheugen (vectoropslag) |
| ReAct / Reason + Act               | **ReAct-patroon**                | Met koppelteken; voeg bij eerste gebruik toe: "ReAct-patroon (redeneren en handelen in afwisselende stappen)"                 |
| Human-in-the-loop                  | **Mens-in-de-lus**               | Alternatief: "menselijk controlepunt" bij niet-technische tekst                                                               |
| Human-on-the-loop                  | **Mens-op-de-lus**               | Gebruik uitsluitend bij Modus 4 (Gedelegeerd) context                                                                         |
| Agentic workflow                   | **Agentische workflow**          | Met -ische suffix; "agentisch" als bijvoeglijk naamwoord                                                                      |
| Tool allowlist / whitelist         | **Toegestane toollijst**         | Vermijd "whitelist" — gebruik "toegestane toollijst" of "toolallowlist"                                                       |
| Circuit breaker                    | **Noodrem**                      | Bij eerste gebruik: "noodrem (circuit breaker)"                                                                               |
| Excessive Agency (OWASP LLM06)     | **Buitensporige autonomie**      | Bij eerste gebruik volledige OWASP-referentie opnemen                                                                         |
| Sandboxed execution                | **Geïsoleerde uitvoering**       | Alternatief: "sandbox-uitvoering" bij technische context                                                                      |
| Task decomposition                 | **Taakverdeling**                | Specifiek voor agentische planning; niet verwarren met werkpakketten                                                          |

______________________________________________________________________

## AI-Projectmanagement als discipline — terminologie

| ❌ Vermijd             | ✅ Gebruik (Blauwdruk-standaard)             | Toelichting                                                                                                                  |
| ---------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Onzekerheid managen    | **Productieve onzekerheid**                  | De kern van AI-PM: weten wanneer door te gaan en wanneer te stoppen                                                          |
| Experiment mislukt     | **Experiment zonder convergerend resultaat** | Neutraler; voorkomt blame-cultuur rondom iteraties                                                                           |
| Model werkt niet       | **Model haalt de succescriteria niet**       | Koppelt altijd terug aan de Golden Set; vermijd vage negatieve uitspraken                                                    |
| Sprint velocity        | **Iteratiesnelheid**                         | In AI-context; koppel altijd aan experimentbudget, niet alleen aan story points                                              |
| Stakeholder management | **Verwachtingsbeheer**                       | In AI-PM context specifieker dan generiek stakeholder management                                                             |
| Model accuracy         | **Modelnauwkeurigheid**                      | Schrijf voluit; voeg bij eerste gebruik de gebruikte metriek toe (bijv. F1, precision@K)                                     |
| Retraining             | **Hertraining**                              | Schrijf als één woord; bij eerste gebruik: "hertraining (het opnieuw trainen van het model op nieuwe of gecorrigeerde data)" |
| Concept drift          | **Conceptdrift**                             | Aaneengeschreven; onderscheid van datadrift en modeldrift                                                                    |
| Cone of uncertainty    | **Onzekerheidskegel**                        | Bij eerste gebruik: "onzekerheidskegel (de toenemende onzekerheid naarmate de planningshorizon verder weg ligt)"             |
| Build vs. buy          | **Bouwen of inkopen**                        | Schrijf voluit in lopende tekst                                                                                              |
| Foundation model       | **Basismodel**                               | Alternatief: gebruik "LLM" als het specifiek over taalmodellen gaat                                                          |

______________________________________________________________________

## Bronvermeldingen `[so-XX]`

Externe claims, statistieken, wetgeving en onderzoeksresultaten **vereisen altijd** een bronverwijzing in het formaat `[so-XX]`.

**Wanneer verplicht:**

- Statistieken en kwantitatieve claims ("40% van de tijdwinst gaat verloren aan rework")
- Verwijzingen naar wetgeving (EU AI Act, GDPR, PLD)
- Externe raamwerken (NIST, OWASP, ISACA)
- Onderzoeksresultaten (universiteiten, consultancies, standaardinstellingen)

**Wanneer niet verplicht:**

- Interne blauwdruk-concepten (Rode Lijnen, Golden Set, Doelkaart)
- Procesbeschrijvingen die eigen methodologie beschrijven
- Algemeen gangbare definities zonder specifieke bron

**Formaat:** Plaats `Bron: \[so-XX\]` of `Bronnen: \[so-XX\], \[so-YY\]` op een aparte regel na de relevante paragraaf of tabel. Zie `docs/16-bronnen/index.md` voor de volledige bronnenlijst.

______________________________________________________________________

## Admonitions (Informatieblokken)

Gebruik MkDocs Material admonitions spaarzaam en consequent. Elk type heeft een specifiek doel:

| Admonition    | Gebruik voor                                                        |
| :------------ | :------------------------------------------------------------------ |
| `!!! tip`     | Praktisch advies dat de lezer helpt — niet verplicht maar waardevol |
| `!!! info`    | Contextuele achtergrondinfo die het begrip verdiept                 |
| `!!! warning` | Risico of valkuil die actieve aandacht vraagt                       |
| `!!! danger`  | Kritieke grens of verbod — niet negeren                             |
| `!!! check`   | Checklists die actie vereisen (bij voorkeur in gates en sjablonen)  |

**Richtlijnen:**

- Maximaal **2 admonitions per sectie** — meer verstoort de leesstroom
- Admonition-tekst is **bondig** (max. 4 regels); langere toelichting hoort in de lopende tekst
- Gebruik de **title-syntax** voor specifieke context: `!!! warning "Titel van de waarschuwing"`

______________________________________________________________________

## Module-anatomie — vaste structuur

Elke Proces-Module (Laag 2) moet de volgende anatomie hebben:

1. **Doelstelling (Het Waarom):** Eén krachtige zin.
1. **Intrede Criteria (Definition of Ready):** Wat moet er af zijn voordat we mogen beginnen?
1. **Kernactiviteiten (Het Wat):** 3 tot 5 duidelijke stappen. Gebruik de termen uit het Lexicon.
1. **RACI (Het Wie):** Wie is Responsible (R) en wie is Accountable (A)?
1. **Exit Criteria (De Gate):** De checklist om de fase af te sluiten. Vermeld altijd de beoogde Samenwerkingsmodus.
1. **Deliverables:** De concrete bestanden die worden opgeleverd.
1. **CTA-blok (Volgende stap):** Zie "Module-CTA" hieronder.

______________________________________________________________________

## Module-CTA (Call to Action)

Elke module in Laag 2 eindigt met een **"Volgende stap"-blok**. Dit is geen optioneel element.

**Formaat:**

```markdown
______________________________________________________________________

**Volgende stap:** [Eén concrete actie die de lezer nu kan nemen]
→ Gebruik [Sjabloonnaam](relatief/pad/naar/template.md) als startpunt.
→ Zie ook: [Gerelateerde module](relatief/pad.md)
```

**Richtlijnen voor de CTA:**

- De actie is specifiek ("Vul de Doelkaart in") — geen vage aansporing ("Ga verder")
- Verwijs altijd naar het relevante sjabloon als dat bestaat
- Maximaal 3 "Zie ook"-verwijzingen — meer verstoort de focus

______________________________________________________________________

## Praktijkvoorbeelden (Case Studies)

Geanonimiseerde praktijkvoorbeelden versterken de geloofwaardigheid en maken abstracte concepten concreet. Gebruik het volgende formaat:

```markdown
!!! info "Praktijkvoorbeeld — [Sector] / [Risicoklasse]"
    **Situatie:** [2–3 zinnen: wat was het AI-project, welke uitdaging]
    **Aanpak:** [2–3 zinnen: welk onderdeel van de Blauwdruk werd ingezet]
    **Resultaat:** [1–2 zinnen: meetbaar of kwalitatief resultaat]
    *Sector: [bijv. Financiële dienstverlening] — Namen geanonimiseerd.*
```

**Plaatsingsregel:** Maximaal **1 praktijkvoorbeeld per module**. Voorkeurspositie: na de kernactiviteiten, vóór de exit-criteria. Bijlage `docs/17-bijlagen/` bevat langere cases.

**Prioriteit voor eerste reeks (zie IMPLEMENTATION_PLAN.md):**

- 1 voorbeeld per risicoklasse: Minimaal, Beperkt, Hoog Risico
- Sectoren: zorg, financiën, overheid, HR (in lijn met EU AI Act Bijlage III)

______________________________________________________________________

## Green AI — duurzaamheidsintegratie

Duurzaamheid is geen apart hoofdstuk — het is een **cross-cutting concern** dat op drie vaste plaatsen verschijnt:

1. **Business Case (Fase 2):** Verplicht veld "Ecologische voetafdruk" — schat inferentie- en trainingskosten in CO₂-equivalenten.
1. **Risk Pre-Scan (Fase 1):** Trigger: "Vereist het systeem continue inferentie op grote schaal?" → verwijs naar Green AI-standaard.
1. **Beheer & Optimalisatie (Fase 5):** Driftmeting omvat ook kostenefficiëntie; verwijs naar Green AI-benchmarks.

Verwijs altijd naar `docs/08-technische-standaarden/` voor de volledige Green AI-richtlijnen. Schrijf geen uitleg over Green AI opnieuw in fase-modules.

______________________________________________________________________

## Plagiaat & Originaliteit

- **Strikte Regel:** Kopieer nooit letterlijke zinnen uit bronbestanden (zoals PMI-documenten, ISO-normen of externe whitepapers).
- **Herformuleren:** Lees de bron, begrijp de kern, en schrijf het op alsof je het uitlegt aan een collega.
- **Context:** Vertaal algemene theorie altijd naar de specifieke context van onze modulaire aanpak.

______________________________________________________________________

## Opmaakstandaarden (Markdown)

Consistentie zorgt voor leesbaarheid.

- **Titels:**
    - `#` voor Modulenamen.
    - `##` voor Hoofdstukken.
    - `###` voor Activiteiten.
- **Navigatie-Icoontjes:** Gebruik emoji's spaarzaam maar functioneel:
    - 📂 = Module / Hoofdstuk
    - 🎯 = Doelstelling
    - ⚙️ = Activiteiten / Proces
    - 👥 = Rollen (RACI)
    - ✅ = Checklists / Gates
- **Lijsten:** Gebruik bullets voor opsommingen en genummerde lijsten voor stappenplannen.
- **Scheidingslijnen:** Gebruik `______________________________________________________________________` als sectie-separator tussen H2-secties. Niet tussen H3-subsecties.

______________________________________________________________________

## Instructies voor Auteurs

### Bepaal de Plaats in de Levenscyclus

Kijk naar **Module 00 (Het Strategisch Kader)**. Waar past jouw document?

- Is het strategie? → Module 00–02.
- Is het uitvoering? → Module 03–05.
- Is het beheer? → Module 06.
- Is het een template? → Module 09+.

### De 'Jip en Janneke' Check (Begrijpelijkheid)

Lees je concepttekst door met de bril van een niet-technische manager (bijv. een Financieel Directeur).

- Snapt hij/zij wat "Inference costs" zijn? → Nee? Verander in **"Gebruikskosten"**.
- Snapt hij/zij wat "Bias audit" is? → Gebruik **"Fairness audit (bias audit)"**.

### Versiebeheer

Eindig elk document altijd met een footer voor traceerbaarheid:

______________________________________________________________________

**Versie:** \[X.X\]
**Datum:** \[DD maand JJJJ\]
**Status:** \[Concept / Definitief\]

______________________________________________________________________

## Plaatsingsregels voor nieuwe content

Voordat je een nieuw document aanmaakt, raadpleeg altijd:

1. **[INFORMATION_ARCHITECTURE.md](INFORMATION_ARCHITECTURE.md)** — beslisboom voor waar nieuwe content thuishoort
1. **[AI_COPYWRITER_CONSTITUTION.md](AI_COPYWRITER_CONSTITUTION.md)** — inhoudsprincipes en eindtoets
1. **[BACKLOG.md](BACKLOG.md)** — controleer of het onderwerp al gepland staat

**Stelregel:** Eén nieuw concept = één bestaand document uitbreiden. Alleen bij een echt nieuw thema dat nergens past: een nieuw bestand aanmaken.

______________________________________________________________________

## Checklist voor Publicatie

- [ ] Heb ik alle Engelse jargon-termen vertaald naar de Playbook-standaard?
- [ ] Heb ik gecontroleerd op plagiaat (geen copy-paste)?
- [ ] Is de toon actief ("Wij doen") en niet passief ("Er wordt gedaan")?
- [ ] Staan de icoontjes bij de juiste secties?
- [ ] Zijn externe claims voorzien van een bronverwijzing `[so-XX]`?
- [ ] Heb ik de Single Source of Truth-regel getoetst — geen herhaalde uitleg van kernconcepten?
- [ ] Bevat de module een CTA-blok ("Volgende stap")?
- [ ] Vermeldt de gate de relevante Samenwerkingsmodus (Modus 1–5)?
- [ ] Is de bijbehorende EN-vertaling gesynchroniseerd (of aangemaakt)?
- [ ] Is de nieuwe bron toegevoegd aan `docs/16-bronnen/index.md`?

______________________________________________________________________

© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.

______________________________________________________________________

**Versie:** 2.3
**Datum:** 13 maart 2026
**Status:** Definitief
