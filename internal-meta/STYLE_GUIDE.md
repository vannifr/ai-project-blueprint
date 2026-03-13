# Huisstijl & Schrijfwijzer (Styleguide v2.2)

Deze blauwdruk borgt dat alle modules in het Playbook consistent, begrijpelijk en uniform blijven. Versie 2.2 integreert de **Vlaamse taalgids-audit** voor een optimale aansluiting bij Belgisch Nederlandstalige professionals, en synchroniseert de terminologietabel met de huidige documentstandaard.

______________________________________________________________________

## Toon & Stem (Tone of Voice)

Wij schrijven voor professionals die actie willen ondernemen. Onze taal is direct, activerend en zelfverzekerd.

- **Formele aanspreekvorm (Vlaamse standaard):** Gebruik consequent **"u"** en **"uw"**. Vermijd de informele "je/jou"-vorm voor een zakelijke uitstraling.
- **Actief boven Passief:**
    - ❌ Fout: "Door het team zal worden beoordeeld of de data geschikt is."
    - ✅ Goed: "Het team evalueert de data."
- **De "Wij"-vorm:** We schrijven vanuit het perspectief van het projectteam. "Wij bouwen", "Wij toetsen".
- **Geen Academisch Jargon:** Vermijd onduidelijke of te theoretische taal. We schrijven een praktische handleiding.

______________________________________________________________________

## Terminologie & Lexicon (De Vertaallijst)

Wij slaan de brug tussen techniek en business. Gebruik de onderstaande tabel voor een consistente woordkeuze die zowel technisch accuraat als grammaticaal correct is voor een Vlaams publiek.

> **Opmerking v2.2:** De tabel hieronder reflecteert de **huidige documentstandaard**. Enkele termen zijn bewust aangepast ten opzichte van v2.1 om aansluiting te houden bij internationaal gangbaar vakjargon dat door de doelgroep herkend wordt.

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

Volg dit proces wanneer je een nieuwe module toevoegt of een bestaande bewerkt.

### Bepaal de Plaats in de Levenscyclus

Kijk naar **Module 00 (Het Strategisch Kader)**. Waar past jouw document?

- Is het strategie? -> Module 00 - 02.
- Is het uitvoering? -> Module 03 - 05.
- Is het beheer? -> Module 06.
- Is het een template? -> Module 09+.

### Gebruik de Vaste Structuur

Elke Proces-Module moet de volgende anatomie hebben:

1. **Doelstelling (Het Waarom):** Eén krachtige zin.
1. **Intrede Criteria (Definition of Ready):** Wat moet er af zijn voordat we mogen beginnen?
1. **Kernactiviteiten (Het Wat):** 3 tot 5 duidelijke stappen. Gebruik de termen uit het Lexicon.
1. **RACI (Het Wie):** Wie is Responsible (R) en wie is Accountable (A)?
1. **Exit Criteria (De Gate):** De checklist om de fase af te sluiten.
1. **Deliverables:** De concrete bestanden die worden opgeleverd.

### De 'Jip en Janneke' Check (Begrijpelijkheid)

Lees je concepttekst door met de bril van een niet-technische manager (bijv. een Financieel Directeur).

- Snapt hij/zij wat "Inference costs" zijn? -> Nee? Verander in **"Gebruikskosten"**.
- Snapt hij/zij wat "Bias audit" is? -> Gebruik **"Fairness audit (bias audit)"**.

### Versiebeheer

Eindig elk document altijd met een footer voor traceerbaarheid:

______________________________________________________________________

**Versie:** \[X.X\]
**Datum:** \[DD maand JJJJ\]
**Status:** \[Concept / Definitief\]

______________________________________________________________________

## Nieuwe inhoudsgebieden: uitgebreide terminologie

De Blauwdruk breidt uit naar twee nieuwe kennisdomeinen: **Agentische AI** en **AI-projectmanagement als discipline**. Gebruik de onderstaande tabellen voor consistente terminologie in alle nieuwe content.

### Agentische AI

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

### AI-Projectmanagement als discipline

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
- [ ] Is de bijbehorende EN-vertaling gesynchroniseerd (of aangemaakt)?
- [ ] Is de nieuwe bron toegevoegd aan `docs/16-bronnen/index.md`?

______________________________________________________________________

© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
