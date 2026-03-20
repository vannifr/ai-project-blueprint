---
versie: '1.1'
type: foundation
layer: 1
roles: [Data Scientist]
tags: [governance, validation]
summary: Beschrijving van de drie validatiedimensies (syntactisch, gedragsmatig, doelgericht) die elke wijziging aan prompts of RAG moet doorlopen.
answers: [Wat houdt Validatie Model in?, Hoeveel validatie is voldoende?]
---

# 1. Validatie Model

!!! abstract "Doel"
    Beschrijving van de drie validatiedimensies (syntactisch, gedragsmatig, doelgericht) die elke wijziging aan prompts of RAG moet doorlopen.

## 1. Drie Dimensies van Validatie

Elke wijziging in de **Prompts** of RAG moet drie validatiecategorieën doorlopen:

### Syntactische Geldigheid

- **Vraag:** Werkt de code? Geen crashes of errors?
- **Methode:** Geautomatiseerde checks op structuur, gestructureerde schema's (zoals JSON, YAML) en linting.

### Gedragsconformiteit

- **Vraag:** Doet het systeem wat we verwachten in gecontroleerde omstandigheden?
- **Methode:** Geautomatiseerde evaluatiesuites die reproduceerbaar zijn (testsets).

### Doelgerichtheid (Intent-Alignment)

- **Vraag:** Helpt het systeem de gebruiker echt in de praktijk?
- **Methode:** Scenario-gebaseerde evaluatie door experts of geavanceerde simulatie.

______________________________________________________________________

## 2. Validatie Diepgang per Risiconiveau

Niet elke wijziging vereist dezelfde validatie-inspanning. De vereiste diepgang is gekoppeld aan het [risiconiveau](05-risicoclassificatie.md) van de wijziging. Onderstaande tabel beschrijft wat elk validatieniveau er concreet uitziet in de praktijk.

### Niveau 1 — Minimale Validatie (Laag Risico)

**Wanneer:** Cosmetische wijzigingen, kleine prompt-aanpassingen die geen Harde Grenzen raken, tekstuele correcties.

| Dimensie        | Wat te doen                                           | Voorbeeld                                                                        |
| :-------------- | :---------------------------------------------------- | :------------------------------------------------------------------------------- |
| Syntactisch     | Geautomatiseerde linting en schema-validatie draaien  | CI-pipeline controleert dat JSON-output schema geldig blijft na prompt-wijziging |
| Gedrag          | Bestaande regressie-testset draaien (geautomatiseerd) | 20 standaard test-cases worden automatisch gevalideerd; alle moeten slagen       |
| Doelgerichtheid | Niet vereist                                          | —                                                                                |

**Doorlooptijd:** minuten (volledig geautomatiseerd).

**Bewijsmateriaal:** CI/CD pipeline-rapport met groene status.

### Niveau 2 — Standaard Validatie (Midden Risico)

**Wanneer:** Wijzigingen in system prompts, toevoegen van nieuwe kennisbronnen aan RAG, aanpassing van retrieval-logica, nieuwe use case binnen bestaand systeem.

| Dimensie        | Wat te doen                                                           | Voorbeeld                                                                                       |
| :-------------- | :-------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| Syntactisch     | Geautomatiseerde linting + schema-validatie + output-formaatcheck     | Valideer dat de API-response structuur intact blijft na RAG-wijziging                           |
| Gedrag          | Golden Set evaluatie (minimaal 50 cases) + regressietest              | Vergelijk scores voor en na wijziging; maximaal 5% regressie op bestaande metrics toegestaan    |
| Doelgerichtheid | Steekproef door domeinexpert (minimaal 10 cases handmatig beoordeeld) | Expert beoordeelt of antwoorden in context van de business nog steeds correct en bruikbaar zijn |

**Doorlooptijd:** 1-2 dagen.

**Bewijsmateriaal:** Golden Set rapport + expert sign-off.

### Niveau 3 — Diepgaande Validatie (Hoog Risico)

**Wanneer:** Wijzigingen die Harde Grenzen raken, nieuw model of modelversie, systeem dat externe beslissingen neemt, persoonsgegevens in scope, hoog-risico classificatie onder EU AI Act.

| Dimensie        | Wat te doen                                                                          | Voorbeeld                                                                                        |
| :-------------- | :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| Syntactisch     | Volledige geautomatiseerde suite + contract testing tussen componenten               | Valideer dat alle upstream/downstream systemen correct communiceren na modelwissel               |
| Gedrag          | Volledige Golden Set (100+ cases) + adversarial testset + bias-analyse + Red Teaming | Red Team probeert het systeem te manipuleren via prompt injection, jailbreaks en edge cases      |
| Doelgerichtheid | Scenario-evaluatie door meerdere domeinexperts + eindgebruikertest + Guardian review | Minimaal 3 experts beoordelen onafhankelijk; eindgebruikers evalueren in realistische scenario's |

**Doorlooptijd:** 1-2 weken.

**Bewijsmateriaal:** Volledig [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md) + Red Teaming rapport + Guardian sign-off + expert beoordelingen.

______________________________________________________________________

## 3. Validatie in de Praktijk

### Vuistregels

1. **Begin altijd met Niveau 1.** Elke wijziging doorloopt minimaal de geautomatiseerde checks. Als die falen, ga niet verder.
1. **Niveau bepaalt de Guardian.** Bij twijfel over het vereiste niveau beslist de Guardian. Liever een niveau te hoog dan te laag.
1. **Geen validatie, geen deployment.** Geen enkele wijziging gaat naar productie zonder dat het bijbehorende validatieniveau is doorlopen en gedocumenteerd.
1. **Combineer niveaus niet neerwaarts.** Als een wijziging meerdere onderdelen raakt waarvan er een Hoog Risico is, dan geldt Niveau 3 voor de gehele wijziging.

### Voorbeeld: validatieflow bij een RAG-update

```
1. Nieuwe kennisbron toevoegen aan vectorstore
2. CI-pipeline draait automatisch (Niveau 1: schema + linting)     ✅
3. Golden Set evaluatie draait (Niveau 2: 50 cases)                 ✅
4. Domeinexpert beoordeelt 10 steekproef-cases                      ✅
5. Geen Harde Grenzen geraakt → Niveau 2 volstaat
6. Resultaat: deployment goedgekeurd met Golden Set rapport + expert sign-off
```

______________________________________________________________________

## 4. Gerelateerde Modules

- [Risicoclassificatie](05-risicoclassificatie.md)
- [Bewijsstandaarden](07-bewijsstandaarden.md)
- [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)
- [SDD Patroon](../04-fase-ontwikkeling/05-sdd-patroon.md)
- [Validatierapport sjabloon](../09-sjablonen/07-validatie-bewijs/validatierapport.md)

______________________________________________________________________
