---
versie: '1.0'
type: technical
layer: 3
roles: [Tech Lead]
---

# 1. Test Frameworks

!!! abstract "Doel"
    Testaanpak voor AI-systemen die deterministische tests combineert met evaluatie van probabilistisch gedrag.

## 1. Doel

Deze module definieert hoe wij AI-systemen testen. Anders dan traditionele software vereist AI een combinatie van deterministische tests én evaluatie van probabilistisch gedrag.

______________________________________________________________________

## 2. Testniveaus

### Componenttests (Unit Tests)

Testen van individuele onderdelen in isolatie.

**Wat testen we:**

- Data-transformatiefuncties (input → verwachte output)
- Prompt-parsing en -formatting
- API-integratiecode (met mocks)
- Foutafhandeling (edge cases)

**Kenmerken:**

- Snel uitvoerbaar (seconden)
- Deterministisch (zelfde input = zelfde resultaat)
- Automatisch bij elke code-wijziging

### Integratietests

Testen van de samenwerking tussen componenten.

**Wat testen we:**

- End-to-end flow van input naar output
- Integratie met externe systemen (databases, API's)
- Datavalidatie in de volledige pipeline

**Kenmerken:**

- Trager dan unit tests (minuten)
- Kan externe afhankelijkheden vereisen
- Periodiek of bij belangrijke wijzigingen

### AI-gedragstests (Golden Set)

Testen van het AI-gedrag op representatieve scenario's.

**Wat testen we:**

- Feitelijkheid en relevantie van antwoorden
- Naleving van Harde Grenzen
- Consistentie over meerdere runs
- Prestaties per gebruikersgroep (eerlijkheid)

**Kenmerken:**

- Vereist menselijke beoordeling of geautomatiseerde evaluatie
- Variatie mogelijk door probabilistisch karakter
- Verplicht voor elke Gate Review

______________________________________________________________________

## 3. De Golden Set

De Golden Set is de centrale testset voor AI-gedrag. Zie [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md) voor minimale eisen per risiconiveau.

### Samenstelling

| Categorie         | Beschrijving                                  |    Minimaal % |
| ----------------- | --------------------------------------------- | ------------: |
| Standaardcases    | Typische, realistische scenario's             |        70-80% |
| Complexe cases    | Randgevallen, meerstaps-vragen                |        15-20% |
| Adversarial cases | Jailbreaks, prompt-injectie, policy-omzeiling |         5-10% |
| Fairness cases    | Scenario's per relevante gebruikersgroep      | Naar behoefte |

### Format per Testcase

| Veld                | Beschrijving                                    |
| ------------------- | ----------------------------------------------- |
| ID                  | Unieke identificatie (bijv. GS-001)             |
| Categorie           | Standaard / Complex / Adversarial / Fairness    |
| Input               | De exacte prompt of vraag                       |
| Verwachte uitkomst  | Correcte antwoord óf beoordelingscriteria       |
| Beoordelingsmethode | Exact match / Keywords / Menselijke beoordeling |
| Kritiek?            | Ja/Nee (Kritieke fout als incorrect?)           |

### Onderhoud

- Golden Set wordt periodiek herzien (minimaal per release)
- Nieuwe scenario's worden toegevoegd bij incidenten of nieuwe functionaliteit
- Verouderde cases worden verwijderd of geupdate

______________________________________________________________________

## 4. Adversarial Testing

Specifieke tests om de veiligheid en robuustheid te valideren.

### Verplichte Adversarial Scenario's

| Scenario                          | Beschrijving                                                                              | Verwacht gedrag                                        |
| --------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Jailbreak                         | Poging om instructies te negeren                                                          | Weigering                                              |
| Prompt-injectie                   | Verborgen instructies in user input                                                       | Instructie negeren                                     |
| Policy-omzeiling                  | Slim omzeilen van Harde Grenzen                                                           | Weigering                                              |
| Bronvervalsing                    | "Verzin een bron" of "doe alsof"                                                          | Weigering                                              |
| PII-extractie                     | Poging om trainingsdata te achterhalen                                                    | Weigering                                              |
| Tool abuse / privilege escalation | Poging om via tools hogere rechten te verkrijgen of ongeautoriseerde acties uit te voeren | Weigering + logging                                    |
| Data-exfiltratie via tool-output  | Poging om gevoelige data te extraheren via tool-responses of -artefacten                  | Blokkering + alert                                     |
| Retrieval poisoning               | Injectie van malafide bronnen in kennisbank om output te manipuleren                      | Detectie (monitoring) + blokkering/weigering + logging |
| Action injection                  | Manipulatie van tool-schema's om onbedoelde acties te triggeren                           | Schema-validatie + weigering                           |

Bronnen: \[so-1\], \[so-10\]

### Uitvoering

- **Minimaal Risico:** Kwalitatieve steekproef door Guardian
- **Beperkt Risico:** Gestructureerde adversarial set (minimaal 5% van Golden Set)
- **Hoog Risico:** Uitgebreide adversarial testing + externe red team indien relevant

______________________________________________________________________

## 5. Regressietesting

Het automatisch herhalen van tests bij wijzigingen om achteruitgang te detecteren.

### Wat triggert regressietests?

| Wijziging          | Regressietest niveau                |
| ------------------ | ----------------------------------- |
| Codewijziging      | Componenttests + Integratietests    |
| Prompt-wijziging   | Integratietests + Golden Set sample |
| Modelversie-update | Volledige Golden Set                |
| Databron-wijziging | Volledige Golden Set + Fairness     |

### Automatisering

| Niveau | Aanpak                               | Tooling voorbeelden       |
| ------ | ------------------------------------ | ------------------------- |
| L0     | Handmatige uitvoering bij release    | Spreadsheet tracking      |
| L1     | Geplande periodieke tests            | Cron jobs, CI scheduled   |
| L2     | Automatisch bij elke commit          | GitHub Actions, GitLab CI |
| L3     | Continuous testing met quality gates | MLflow, custom pipelines  |

______________________________________________________________________

## 6. Evaluatiemetrics

| Metric          | Toepassing              | Berekening                     |
| --------------- | ----------------------- | ------------------------------ |
| Feitelijkheid   | Factual correctness     | % correct / totaal             |
| Relevantie      | Antwoord past bij vraag | Gemiddelde score (1-5 schaal)  |
| Consistentie    | Stabiliteit over runs   | Standaarddeviatie over N runs  |
| Weigeringsgraad | Adversarial scenario's  | % correct geweigerd            |
| Fairness        | Verschil tussen groepen | Max verschil in foutpercentage |

______________________________________________________________________

## 7. Checklist Test Framework

!!! check "7. Checklist Test Framework"
    - [ ] Componenttests dekken kritieke functies
    - [ ] Integratietests valideren end-to-end flow
    - [ ] Golden Set is samengesteld conform [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
    - [ ] Adversarial scenarios zijn gedefinieerd en getest
    - [ ] Regressietest-strategie is vastgelegd
    - [ ] Evaluatiemetrics zijn gedefinieerd
    - [ ] Testresultaten worden vastgelegd in [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)

______________________________________________________________________

## 8. Gerelateerde Modules

- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [Golden Set Test Template](../09-sjablonen/07-validatie-bewijs/template.md)
