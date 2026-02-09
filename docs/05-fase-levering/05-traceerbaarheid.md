---
versie: '1.0'
---

# 1. Traceerbaarheid

## 1. Doel

Traceerbaarheid zorgt ervoor dat we altijd kunnen verklaren waarom een AI-systeem een bepaalde output gaf. Dit is essentieel voor auditing, debugging, incidentanalyse en compliance met de EU AI Act.

______________________________________________________________________

## 2. De Traceerbaarheidspiramide

```
 ┌───────────────┐
 │ Doelkaart │ Waarom bouwen we dit?
 │ (Intent) │
 └───────┬───────┘
 │
 ┌───────v───────┐
 │ Specificatie │ Hoe moet het zich gedragen?
 │ (Contract) │
 └───────┬───────┘
 │
 ┌───────v───────┐
 │Sturingsinstr. │ Welke prompts/configs sturen het?
 │ (Context) │
 └───────┬───────┘
 │
 ┌───────v───────┐
 │ Gouden Set │ Hoe hebben we getest?
 │ (Tests) │
 └───────┬───────┘
 │
 ┌───────v───────┐
 │ Validatie- │ Wat waren de resultaten?
 │ rapport │
 └───────────────┘
```

**Elke laag moet herleidbaar zijn naar de laag erboven.**

______________________________________________________________________

## 3. Traceerbaarheidsmatrix

De traceerbaarheidsmatrix koppelt requirements aan implementatie aan tests.

### Structuur

| Doel-ID | Doelomschrijving           | Spec-ID | Specificatie                  | Prompt-versie | Test-ID | Testresultaat |
| ------- | -------------------------- | ------- | ----------------------------- | ------------- | ------- | ------------- |
| D-001   | Productvragen beantwoorden | S-001   | Antwoord met prijs en bron    | v2.3          | GS-001  | Pass          |
| D-002   | Geen medisch advies        | S-002   | Weigering bij medische vragen | v2.3          | GS-003  | Pass          |
| D-003   | Transparantie              | S-003   | AI-disclaimer tonen           | v2.3          | GS-010  | Pass          |

### Minimale Velden

| Veld             | Beschrijving                           |
| ---------------- | -------------------------------------- |
| Doel-ID          | Referentie naar Doelkaart item         |
| Doelomschrijving | Korte beschrijving van het doel        |
| Spec-ID          | Referentie naar specificatie-item      |
| Specificatie     | Hoe wordt het doel technisch vertaald? |
| Prompt-versie    | Welke versie van Sturingsinstructies?  |
| Test-ID          | Referentie naar Gouden Set testcase    |
| Testresultaat    | Pass/Fail/N.v.t.                       |
| Validatierapport | Link naar bewijs                       |

______________________________________________________________________

## 4. Runtime Traceerbaarheid (Logging)

Naast documentatie-traceerbaarheid is runtime logging essentieel.

### Wat Loggen We?

Per interactie minimaal (zie [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)):

| Veld                       | Voorbeeld                           |
| -------------------------- | ----------------------------------- |
| Timestamp                  | 2026-02-01T14:32:15Z                |
| Request-ID                 | req-abc123                          |
| Gebruiker/Sessie           | user-456 (gehashed indien nodig)    |
| Model + versie             | gpt-4-turbo / v2024-01              |
| Sturingsinstructies-versie | prompts/v2.3                        |
| Input (query)              | "Wat kost product X?"               |
| Gebruikte bronnen          | doc-789, doc-012                    |
| Output                     | "Product X kost €49,99 (bron: ...)" |
| Latency                    | 1.2s                                |
| Human override             | Nee                                 |

Voor systemen die zelfstandig taken uitvoeren, wordt daarnaast vastgelegd welke acties zijn uitgevoerd, binnen welke vooraf vastgestelde kaders, en of daarbij menselijke tussenkomst of goedkeuring heeft plaatsgevonden.

### Logging per Risiconiveau

| Niveau   | Logging-eis                                      |
| -------- | ------------------------------------------------ |
| Minimaal | Metadata (timestamp, model, versie, status)      |
| Beperkt  | Metadata + sampling van input/output (bijv. 10%) |
| Hoog     | 100% input/output + bronverwijzingen + context   |

### Retentie

- **Minimaal/Beperkt:** 90 dagen standaard
- **Hoog Risico:** 12 maanden of langer (afhankelijk van regelgeving)

______________________________________________________________________

## 5. Incidentanalyse met Traceerbaarheid

Wanneer een incident optreedt, volgen we de traceerbaarheidsketen terug:

### Analyse-stappenplan

1. **Identificeer de output:** Welke response veroorzaakte het probleem?
1. **Haal logging op:** Request-ID, input, model, bronnen
1. **Check Sturingsinstructies:** Was de juiste versie actief?
1. **Vergelijk met specificatie:** Voldeed de output aan de spec?
1. **Check Gouden Set:** Hadden we dit scenario getest?
1. **Terug naar Doelkaart:** Was dit gedrag bedoeld of een gap?

### Root Cause Categorieën

| Categorie         | Beschrijving                         | Actie                   |
| ----------------- | ------------------------------------ | ----------------------- |
| Spec Gap          | Scenario niet gespecificeerd         | Specificatie uitbreiden |
| Implementatie Bug | Spec correct, implementatie wijkt af | Code/prompt corrigeren  |
| Test Gap          | Scenario niet in Gouden Set          | Testcase toevoegen      |
| Onvoorzien Gedrag | Probabilistisch karakter van AI      | Guardrails versterken   |

______________________________________________________________________

## 6. Traceerbaarheid voor Audit

### EU AI Act Vereisten (Hoog Risico)

- Alle beslissingen moeten herleidbaar zijn
- Documentatie moet beschikbaar zijn voor toezichthouders
- Wijzigingen in het systeem moeten gedocumenteerd zijn

### Audit-Ready Package

Voor elke productierelease:

| Document               | Inhoud                            |
| ---------------------- | --------------------------------- |
| Doelkaart              | Intent en Rode Lijnen             |
| Specificatie           | Gedragscontract                   |
| Sturingsinstructies    | Prompts/configs (versiebeheerd)   |
| Gouden Set             | Testcases en verwachte resultaten |
| Validatierapport       | Testresultaten en conclusie       |
| Traceerbaarheidsmatrix | Koppelingen tussen bovenstaande   |
| Wijzigingslog          | Alle changes sinds vorige release |

______________________________________________________________________

## 7. Tooling Suggesties

| Doel                     | Opties                                   |
| ------------------------ | ---------------------------------------- |
| Document traceerbaarheid | Git (alles als code), Confluence, Notion |
| Runtime logging          | CloudWatch, Datadog, ELK Stack, custom   |
| Traceerbaarheidsmatrix   | Spreadsheet, Jira, dedicated tools       |
| Audit trail              | Onveranderbare logging (append-only)     |

______________________________________________________________________

## 8. Checklist Traceerbaarheid

!!! check "8. Checklist Traceerbaarheid"
    - [ ] Traceerbaarheidsmatrix is opgesteld
    - [ ] Alle Doelkaart-items zijn gekoppeld aan specificaties
    - [ ] Alle specificaties zijn gekoppeld aan testcases
    - [ ] Runtime logging is ingericht conform risiconiveau
    - [ ] Logging voldoet aan [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
    - [ ] Retentie is afgestemd met privacybeleid
    - [ ] Audit-ready package is compleet

______________________________________________________________________

## 9. Gerelateerde Modules

- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Traceerbaarheid Sjabloon](../09-sjablonen/08-traceerbaarheid-links/template.md)
- [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [Incidentrespons](../07-compliance-hub/05-incidentrespons.md)
