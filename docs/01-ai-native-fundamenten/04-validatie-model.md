---
versie: '1.0'
type: foundation
layer: 1
roles: [Data Scientist]
tags: [governance, validation]
---

# 1. Validatie Model

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

## 2. Gerelateerde Modules

- [Risicoclassificatie](05-risicoclassificatie.md)
- [Bewijsstandaarden](07-bewijsstandaarden.md)
- [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)
- [SDD Patroon](../04-fase-ontwikkeling/05-sdd-patroon.md)

______________________________________________________________________
