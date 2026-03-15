---
versie: '1.0'
type: guide
layer: 2
phase: [3]
roles: [Tech Lead]
tags: [mlops, security, validation]
---

# 1. Engineering Patterns voor AI-Gedreven Ontwikkeling

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
- **Rode Lijnen:** Expliciete constraints die de AI nooit mag overschrijden.

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

## 5. Gerelateerde Modules

- [SDD Patroon (Specificatie-gedreven Ontwikkeling)](05-sdd-patroon.md)
- [Validatiemodel](../01-ai-native-fundamenten/04-validatie-model.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Doelkaart (goal card)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)

______________________________________________________________________
