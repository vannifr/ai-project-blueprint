---
versie: '1.0'
type: guide
layer: 2
phase: [3]
roles: [AI Product Manager]
summary: Bewezen engineering patterns en veelvoorkomende anti-patterns voor teams die AI-tools inzetten, gericht op kwaliteitsborging en het voorkomen van rework.
answers: [Hoe werkt Engineering Patterns voor AI-Gedreven Ontwikkeling?, Welke rollen heb ik nodig?, Hoe gebruik ik AI als ontwikkeltool zonder dat het eindproduct zelf AI bevat (Type A)?]
---

# 1. Engineering Patterns voor AI-Gedreven Ontwikkeling

!!! abstract "Doel"
    Bewezen engineering patterns en veelvoorkomende anti-patterns voor teams die AI-tools inzetten, gericht op kwaliteitsborging en het voorkomen van rework.

!!! tip "Wanneer gebruik je dit?"
    Je team gebruikt AI-tools (zoals code-assistenten) tijdens de ontwikkelfase en je wilt weten welke werkpatronen kwaliteit borgen en welke valkuilen je moet vermijden.

## 1. Doel

Deze module beschrijft bewezen engineering patterns en veelvoorkomende anti-patterns voor teams die AI-tools inzetten tijdens de ontwikkelfase. Het doel is de kwaliteit van AI-gegenereerde output te borgen en productiviteitsverlies door rework te voorkomen.

______________________________________________________________________

## 2. Patterns

### Pattern 1: Safe Refactor

**Probleem:** AI-gegenereerde refactoring kan subtiele regressies introduceren.

**Oplossing:**

1. Schrijf of valideer tests die het huidige gedrag vastleggen.
1. Laat AI de refactoring uitvoeren.
1. Voer de bestaande tests uit om regressies te detecteren.
1. Review de diff handmatig op intentie en leesbaarheid.

```
[Tests schrijven] → [AI refactort] → [Tests draaien] → [Menselijke review]
```

**Waarom:** Tests fungeren als vangnet. Als de tests slagen maar de code onleesbaar is, weiger de wijziging.

### Pattern 2: AI als Eerste Reviewer

**Probleem:** Menselijke code review is tijdrovend en inconsistent bij stijl- en conventiecontroles.

**Oplossing:**

1. Configureer AI om code te reviewen op conventies, formatting en veelgemaakte fouten.
1. Menselijke reviewer behandelt alleen wat overblijft: architectuurbeslissingen, business-logica, veiligheid.

**Wanneer gebruiken:** Bij teams met veel pull requests en beperkte reviewcapaciteit. De AI-review is een filter, geen vervanging.

### Pattern 3: Bounded Contexts voor Agents

**Probleem:** Agents die toegang hebben tot een groot codebase produceren inconsistente of conflicterende wijzigingen.

**Oplossing:**

- Beperk de context per agent tot een afgebakend domein (module, service, bounded context).
- Gebruik machine-leesbare contextbestanden die het domein, de interfaces en de beperkingen beschrijven.
- Laat geen agent wijzigingen maken buiten zijn domeingrens zonder expliciete goedkeuring.

**Waarom:** Domein-isolatie voorkomt "emergent complexity" — onvoorziene interacties tussen parallelle wijzigingen.

### Pattern 4: Machine-Leesbare Contextbestanden

**Probleem:** AI-tools produceren generieke output omdat ze de projectcontext niet kennen.

**Oplossing:** Onderhoud gestructureerde contextbestanden die AI-tools als input kunnen gebruiken:

- **Doelkaart (goal card):** Wat het systeem moet bereiken en welke grenzen gelden ([Doelkaart](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)).
- **Architectuurbeslissingen:** Technische keuzes vastgelegd als Architecture Decision Records (ADR's).
- **API-contracten:** Interfacedefinities die de grenzen van het domein beschrijven.
- **Harde Grenzen:** Expliciete constraints die de AI nooit mag overschrijden.

**Waarom:** Hoe specifieker de context, hoe relevanter de AI-output. Generieke prompts produceren generieke code.

______________________________________________________________________

## 3. Anti-patterns

### Anti-pattern 1: Blind Copy-Paste

**Beschrijving:** AI-gegenereerde code wordt geaccepteerd zonder begrip van wat het doet.

**Risico:**

- Verborgen bugs en veiligheidslekken
- Technische schuld die pas later zichtbaar wordt
- Verlies van team-expertise over het eigen codebase

**Mitigatie:** Elke AI-gegenereerde wijziging doorloopt dezelfde review- en testcriteria als handmatig geschreven code. Gebruik de [Definition of Done](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) als toets.

### Anti-pattern 2: Prompt-perfectionisme

**Beschrijving:** De engineer besteedt meer tijd aan het verfijnen van de prompt dan aan het bouwen van de oplossing.

**Risico:**

- Vertraagde oplevering zonder kwaliteitsverbetering
- Vals gevoel van controle (de "perfecte prompt" bestaat niet)

**Mitigatie:** Stel een tijdslimiet op prompt-iteratie. Als de output na drie pogingen niet bruikbaar is, bouw het handmatig en gebruik de prompt als documentatie voor de volgende keer.

### Anti-pattern 3: Context-vervuiling

**Beschrijving:** Te veel of irrelevante context wordt aan de AI aangeboden.

**Risico:**

- Lagere outputkwaliteit (het model raakt "verdwaald" in ruis)
- Hogere kosten door onnodig token-verbruik
- Langzamere responstijden

**Mitigatie:** Pas het principe van "minimale effectieve context" toe. Voeg alleen informatie toe die direct relevant is voor de huidige taak. Gebruik de [Context Builder](../08-rollen-en-verantwoordelijkheden/index.md) aanpak.

### Anti-pattern 4: Ongevalideerde Keten

**Beschrijving:** Meerdere AI-stappen achter elkaar zonder tussentijdse validatie.

**Risico:** Fouten in stap 1 worden versterkt in stap 2, 3, 4 (hallucinatie-escalatie).

**Mitigatie:** Bouw validatiemomenten in na elke significante AI-stap. Gebruik het [3-laags validatiemodel](../01-ai-native-fundamenten/04-validatie-model.md): syntactisch (automatisch), gedrag (tests), intentie (menselijk).

______________________________________________________________________

## 4. Rework Beperken

Onderzoek toont dat een aanzienlijk deel van de tijdswinst door AI-tools verloren gaat aan rework — het corrigeren en herschrijven van AI-gegenereerde output.

**Strategieën om rework te beperken:**

1. **Specificatie-eerst:** Definieer het verwachte resultaat voordat je AI inzet ([SDD Patroon](05-sdd-patroon.md)).
1. **Incrementeel werken:** Laat AI kleine, verifieerbare stukken produceren in plaats van grote blokken.
1. **Directe feedback:** Corrigeer AI-output onmiddellijk en specifiek. Vage feedback leidt tot vage verbeteringen.
1. **Acceptance rate meten:** Monitor welk percentage AI-suggesties daadwerkelijk wordt overgenomen. Een dalende rate is een signaal dat de context verbeterd moet worden.

______________________________________________________________________

## 5. AI-Assisted Development Practices (Type A)

!!! info "Type A versus Type B"
    De patterns hierboven zijn gericht op **Type B**-projecten: systemen die zelf AI bevatten. Dit hoofdstuk richt zich op **Type A**-projecten — teams die AI inzetten als ontwikkeltool (pair programming, code review, codegeneratie) terwijl het eindproduct zelf geen AI bevat. Denk aan een webapplicatie, een API of een mobiele app die gebouwd wordt met hulp van AI-assistenten.

### 5.1 AI Pair Programming

AI pair programming betekent dat een developer samenwerkt met een AI-assistent (zoals Copilot, Cursor of Claude Code) tijdens het schrijven van code. De spelregels:

- **Behandel AI-suggesties als concept-code.** Lees elke suggestie, begrijp wat het doet en pas het aan voordat je het accepteert. "Accept all" is geen workflow.
- **Stuur de kwaliteit via contextbestanden.** Voeg ADR's, codeerconventies en voorbeelden van goede code toe aan de context. Hoe beter de input, hoe bruikbaarder de output.
- **Time-box je AI-sessies.** Stel een limiet (bijv. 20 minuten) per probleemstelling. Als de AI na drie iteraties geen bruikbare output levert, wissel naar handmatig werk. Je bent de programmeur, niet de prompter.
- **Pair, niet delegeer.** Gebruik AI om sneller tot een eerste versie te komen, maar neem altijd het stuur over voor edge cases, foutafhandeling en domeinspecifieke logica.

!!! warning "Anti-pattern: Blind Copy-Paste"
    AI-gegenereerde code accepteren zonder te begrijpen wat het doet is het meest voorkomende en gevaarlijkste anti-pattern. Het leidt tot verborgen bugs, veiligheidslekken en verlies van kennis over je eigen codebase. Zie ook [Anti-pattern 1](#anti-pattern-1-blind-copy-paste).

### 5.2 AI-Assisted Code Review

Een gelaagde review-aanpak combineert snelheid (AI) met diepgang (mens):

| Stap                   | Wie       | Focus                                                                           |
| ---------------------- | --------- | ------------------------------------------------------------------------------- |
| 1. Automatische review | AI        | Conventies, formatting, veelgemaakte fouten, ontbrekende tests, inconsistenties |
| 2. Menselijke review   | Developer | Business-logica, beveiligingsimplicaties, architecturele fit, leesbaarheid      |
| 3. Goedkeuring         | Teamlid   | Definitieve beoordeling en merge-beslissing                                     |

**Waar AI goed in is:**

- Inconsistenties tussen code en bestaande conventies signaleren
- Ontbrekende tests of testscenario's opsporen
- Stijlfouten en formatting-problemen detecteren
- Simpele bugs vinden (null-checks, off-by-one, ongebruikte variabelen)

**Waar AI slecht in is:**

- Business-intentie begrijpen ("doet deze code wat de klant verwacht?")
- Beveiligingsimplicaties inschatten (authenticatie-logica, autorisatie-grenzen)
- Architecturele trade-offs beoordelen (schaalbaarheid vs. complexiteit)
- Herkennen wanneer code technisch correct maar functioneel fout is

!!! danger "Regel"
    AI mag nooit de enige reviewer zijn. Elke pull request moet door minimaal één menselijke reviewer worden goedgekeurd.

### 5.3 Quality Assurance voor AI-Gegenereerde Code

AI-gegenereerde code is code. Er gelden dezelfde kwaliteitseisen als voor handmatig geschreven code — zonder uitzonderingen.

1. **Testdekking.** Dezelfde coverage-eisen gelden. AI-gegenereerde code heeft niet minder tests nodig, eerder meer — omdat de developer minder intiem bekend is met de implementatiedetails.
1. **Security scanning is verplicht.** AI kan subtiele kwetsbaarheden introduceren: hard-coded credentials, SQL-injectie via string-concatenatie, onveilige deserialisatie. Draai SAST/DAST-tools op alle code, ongeacht herkomst.
1. **Licentie-compliance.** AI-modellen zijn getraind op open-source code en kunnen fragmenten reproduceren die onder een specifieke licentie vallen. Gebruik tools voor licentiedetectie als je in een gereguleerde omgeving werkt.
1. **Kwaliteitsmetrieken.** Meet cyclomatische complexiteit, duplicatie en dependency-graad voor AI-gegenereerde code apart. Dit geeft inzicht in of de AI-output de codekwaliteit verbetert of verslechtert.

### 5.4 Verantwoordelijkheid en Accountability

- **De developer die de code commit, is verantwoordelijk.** Het maakt niet uit of de code door een mens, een AI of een combinatie is geschreven. Wie op "merge" klikt, draagt de verantwoordelijkheid.
- **AI-gegenereerde code doorloopt dezelfde gates.** Code review, tests, security scans, Definition of Done — geen uitzonderingen.
- **Documenteer AI-assistentie wanneer relevant.** Voor audit trails, compliance of kennisdeling kan het waardevol zijn om vast te leggen welke onderdelen AI-geassisteerd zijn. Dit is geen schaamte maar transparantie.
- **Teamafspraken vastleggen.** Leg in je teamconventies vast hoe je met AI-tools omgaat: welke tools zijn goedgekeurd, welke kwaliteitscontroles gelden, en hoe je het gebruik documenteert.

### 5.5 Praktische Checklist

Gebruik deze checklist wanneer je team AI-ontwikkeltools gaat inzetten:

- [ ] **Toolselectie:** Goedgekeurde AI-tools zijn gedefinieerd en gecommuniceerd naar het team
- [ ] **Contextbestanden:** ADR's, codeerconventies en voorbeeldcode zijn beschikbaar als AI-context
- [ ] **Review-proces:** Het review-proces beschrijft expliciet de rolverdeling tussen AI- en menselijke review
- [ ] **Testbeleid:** Coverage-eisen gelden gelijk voor AI-gegenereerde en handmatig geschreven code
- [ ] **Security scanning:** SAST/DAST-tooling draait automatisch op alle pull requests
- [ ] **Licentie-compliance:** Licentiedetectie is ingeschakeld als het project dit vereist
- [ ] **Time-boxing:** Teamafspraken over maximale tijdsinvestering in prompt-iteratie zijn vastgelegd
- [ ] **Ownership-regel:** Het team snapt en accepteert dat wie code commit, eigenaar is
- [ ] **Audit trail:** Er is een afspraak of en hoe AI-assistentie wordt gedocumenteerd
- [ ] **Onboarding:** Nieuwe teamleden worden ingewerkt in de AI-werkafspraken

______________________________________________________________________

## 6. Gerelateerde Modules

- [SDD Patroon (Specificatie-gedreven Ontwikkeling)](05-sdd-patroon.md)
- [Validatiemodel](../01-ai-native-fundamenten/04-validatie-model.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Doelkaart (goal card)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)

______________________________________________________________________
