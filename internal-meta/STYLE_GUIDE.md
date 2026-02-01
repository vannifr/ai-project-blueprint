# 🎨 Huisstijl & Schrijfwijzer (Styleguide v2.1)

Deze gids borgt dat alle modules in het Playbook consistent, begrijpelijk en uniform blijven. Versie 2.1 integreert de **Vlaamse taalgids-audit** voor een optimale aansluiting bij Belgisch Nederlandstalige professionals.

______________________________________________________________________

## 1. Toon & Stem (Tone of Voice)

Wij schrijven voor professionals die actie willen ondernemen. Onze taal is direct, activerend en zelfverzekerd.

- **Formele aanspreekvorm (Vlaamse standaard):** Gebruik consequent **"u"** en **"uw"**. Vermijd de informele "je/jou"-vorm voor een zakelijke uitstraling.
- **Actief boven Passief:**
    - ❌ Fout: "Door het team zal worden beoordeeld of de data geschikt is."
    - ✅ Goed: "Het team evalueert de data."
- **De "Wij"-vorm:** We schrijven vanuit het perspectief van het projectteam. "Wij bouwen", "Wij toetsen".
- **Geen Academisch Jargon:** Vermijd onduidelijke of te theoretische taal. We schrijven een praktische handleiding.

______________________________________________________________________

## 2. Terminologie & Lexicon (De Vertaallijst)

Wij slaan de brug tussen techniek en business. Gebruik de onderstaande tabel voor een consistente woordkeuze die zowel technisch accuraat als grammaticaal correct is voor een Vlaams publiek.

| ❌ Vermijd (NL-Nederlands / Jargon) | ✅ Gebruik (Vlaamse IT-Standaard) | Toelichting                   |
| :---------------------------------- | :-------------------------------- | :---------------------------- |
| Het Kostenplaatje                   | **Het Kostenoverzicht**           | Zakelijker en formeler        |
| Inregelen                           | **Instellen / Configureren**      | Standaard IT-taal             |
| U pakt                              | **U raadpleegt**                  | Correcter taalgebruik         |
| Gereedschapskist                    | **Toolkit**                       | Gangbare term in de sector    |
| Wollige taal                        | **Onduidelijke taal**             | Directer                      |
| De "loodgieter"                     | **Ruggengraat van de data**       | Professionele metafoor        |
| Intent Record                       | **Doeldefinitie**                 | Het 'Waarom'                  |
| Context Artifacts                   | **Sturingsinstructies**           | Prompts/Configs               |
| Guardrails                          | **Rode Lijnen**                   | De harde grenzen              |
| Proof of Value (PoV)                | **Praktijkproef**                 | Mag PoV blijven als afkorting |
| Model Drift                         | **Prestatieverloop**              | Verslechtering over tijd      |
| Retrieval Augmented Gen (RAG)       | **Kenniskoppeling**               | Verbinden aan eigen docs      |
| Hyperparameter Tuning               | **Afstellen van het model**       | Fijn-afstelling               |
| Shadow AI                           | **Wildgroei**                     | Ongecontroleerd gebruik       |
| Deployment                          | **Ingebruikname / Livegang**      |                               |

______________________________________________________________________

## 3. Plagiaat & Originaliteit

- **Strikte Regel:** Kopieer nooit letterlijke zinnen uit bronbestanden (zoals PMI-documenten, ISO-normen of externe whitepapers).
- **Herformuleren:** Lees de bron, begrijp de kern, en schrijf het op alsof je het uitlegt aan een collega.
- **Context:** Vertaal algemene theorie altijd naar de specifieke context van onze modulaire aanpak.

______________________________________________________________________

## 4. Opmaakstandaarden (Markdown)

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

______________________________________________________________________

## 📝 Instructies voor Auteurs

Volg dit proces wanneer je een nieuwe module toevoegt of een bestaande bewerkt.

### Stap 1: Bepaal de Plaats in de Levenscyclus

Kijk naar **Module 00 (Het Strategisch Kader)**. Waar past jouw document?

- Is het strategie? -> Module 00 - 02.
- Is het uitvoering? -> Module 03 - 05.
- Is het beheer? -> Module 06.
- Is het een template? -> Module 09+.

### Stap 2: Gebruik de Vaste Structuur

Elke Proces-Module moet de volgende anatomie hebben:

1. **Doelstelling (Het Waarom):** Eén krachtige zin.
1. **Intrede Criteria (Definition of Ready):** Wat moet er af zijn voordat we mogen beginnen?
1. **Kernactiviteiten (Het Wat):** 3 tot 5 duidelijke stappen. Gebruik de termen uit het Lexicon.
1. **RACI (Het Wie):** Wie is Responsible (R) en wie is Accountable (A)?
1. **Exit Criteria (De Gate):** De checklist om de fase af te sluiten.
1. **Deliverables:** De concrete bestanden die worden opgeleverd.

### Stap 3: De 'Jip en Janneke' Check (Begrijpelijkheid)

Lees je concepttekst door met de bril van een niet-technische manager (bijv. een Financieel Directeur).

- Snapt hij/zij wat "Inference costs" zijn? -> Nee? Verander in **"Gebruikskosten"**.
- Snapt hij/zij wat "Bias audit" is? -> Nee? Verander in **"Eerlijkheidstoets"**.

### Stap 4: Versiebeheer

Eindig elk document altijd met een footer voor traceerbaarheid:

______________________________________________________________________

**Versie:** \[X.X\]
**Datum:** \[DD maand JJJJ\]
**Status:** \[Concept / Definitief\]

______________________________________________________________________

## Checklist voor Publicatie

- [ ] Heb ik alle Engelse jargon-termen vertaald naar de Playbook-standaard?
- [ ] Heb ik gecontroleerd op plagiaat (geen copy-paste)?
- [ ] Is de toon actief ("Wij doen") en niet passief ("Er wordt gedaan")?
- [ ] Staan de icoontjes bij de juiste secties?

______________________________________________________________________

© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
