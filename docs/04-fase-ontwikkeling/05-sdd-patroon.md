---
versie: '1.0'
type: pattern
layer: 2
phase: [3]
roles: [AI Product Manager, Tech Lead]
summary: Werkwijze waarbij eerst formeel wordt vastgelegd wat het AI-systeem moet doen, voordat er gebouwd wordt, om correcties achteraf te voorkomen en compliance aantoonbaar te maken.
answers: [Wat is Specificatie-eerst Patroon?]
---

# 1. Specificatie-eerst Patroon

!!! abstract "Doel"
    Werkwijze waarbij eerst formeel wordt vastgelegd wat het AI-systeem moet doen, voordat er gebouwd wordt, om correcties achteraf te voorkomen en compliance aantoonbaar te maken.

## 1. Doel

Het Specificatie-eerst Patroon (Specification-Driven Development) is een werkwijze waarbij wij eerst formeel vastleggen wat het AI-systeem moet doen, voordat we beginnen met bouwen. Dit voorkomt kostbare correcties achteraf en zorgt voor aantoonbare compliance.

______________________________________________________________________

## 2. Kernprincipe: Specificatie Vóór Implementatie

```
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Doelkaart (goal card) │ --> │ Specificatie │ --> │ Implementatie │
│ (Intent) │ │ (Contract) │ │ (Code/Prompts) │
└─────────────────┘ └─────────────────┘ └─────────────────┘
 │ │ │
 v v v
 Wat willen we? Hoe gedraagt het Hoe bouwen we het?
 zich precies?
```

**Het verschil met traditionele ontwikkeling:**

| Traditioneel                | Specificatie-eerst                      |
| --------------------------- | --------------------------------------- |
| Bouw eerst, test later      | Specificeer eerst, bouw naar spec       |
| "Het werkt!" = klaar        | "Het voldoet aan spec" = klaar          |
| Specificatie vaak impliciet | Specificatie expliciet en versiebeheerd |
| Validatie achteraf          | Validatie vooraf (shift-left)           |

______________________________________________________________________

## 3. De Specificatiecyclus

### Doeldefinitie Opstellen

De **AI Product Manager** legt de business-intentie vast in de [Doelkaart (goal card)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md).

**Minimaal vastleggen:**

- Wat is het doel? (Doeldefinitie)
- Wat mag nooit gebeuren? (Harde Grenzen)
- Wie zijn de gebruikers?
- Wat is succes? (Meetbare criteria)

### Specificatie Uitwerken

De **Tech Lead** en **ML Engineer** vertalen de Doelkaart (goal card) naar een technische specificatie.

**Onderdelen van de specificatie:**

| Component                 | Beschrijving                            | Voorbeeld                           |
| ------------------------- | --------------------------------------- | ----------------------------------- |
| Input-formaat             | Wat ontvangt het systeem?               | JSON met velden X, Y, Z             |
| Output-formaat            | Wat levert het systeem op?              | Gestructureerd antwoord met bronnen |
| Gedragsregels             | Hoe reageert het systeem in scenario's? | Bij vraag over X, verwijs naar Y    |
| Randvoorwaarden           | Technische beperkingen                  | Max 500 tokens, latency \< 2s       |
| Harde Grenzen (technisch) | Concrete implementatie van constraints  | Filter op PII-patronen              |

### Specificatie Review

De specificatie wordt gereviewd voordat implementatie start.

**Review-checklist:**

- [ ] Dekt de specificatie alle scenario's uit de Doelkaart (goal card)?
- [ ] Zijn de Harde Grenzen concreet en implementeerbaar?
- [ ] Is de specificatie testbaar (kunnen we Golden Set afleiden)?
- [ ] Zijn edge cases beschreven?
- [ ] Guardian akkoord op Harde Grenzen-implementatie?

### Golden Set Afleiden

Vanuit de specificatie leiden we de testcases af.

**Per gedragsregel:**

- Minimaal 1 positieve testcase (happy flow)
- Minimaal 1 negatieve testcase (wat mag niet?)
- Edge cases waar relevant

### Implementatie tegen Specificatie

Nu pas beginnen we met bouwen:

- Prompts (prompts/configs) opstellen
- Integratie met databronnen
- Implementatie van filters en harde grenzen

### Validatie tegen Specificatie

We valideren of de implementatie voldoet aan de specificatie:

- Golden Set uitvoeren
- Resultaten vergelijken met verwachtingen
- Afwijkingen analyseren en oplossen

______________________________________________________________________

## 4. Voordelen van SDD

| Voordeel                | Toelichting                                   |
| ----------------------- | --------------------------------------------- |
| Vroege foutdetectie     | Fouten in intentie worden ontdekt vóór bouwen |
| Aantoonbare compliance  | Specificatie = bewijs van bedoeling           |
| Efficiënte ontwikkeling | Minder iteraties door helder contract         |
| Betere samenwerking     | Business en Tech spreken dezelfde taal        |
| Testbaarheid            | Golden Set volgt logisch uit specificatie     |

______________________________________________________________________

## 5. Praktische Tips

### Start Klein

Begin met de belangrijkste scenario's. Breid de specificatie iteratief uit.

### Specificatie Is Levend Document

Update de specificatie wanneer requirements veranderen. Oude versies blijven bewaard voor audit.

### Specificatie ≠ Documentatie

De specificatie is geen handleiding voor gebruikers, maar een contract voor ontwikkelaars en testers.

### Integratie met Gates

- **Gate 2:** Specificatie goedgekeurd, Golden Set afgeleid
- **Gate 3:** Implementatie voldoet aan specificatie

______________________________________________________________________

## 6. Voorbeeld: Klantenservice Chatbot

**Doelkaart (goal card) (excerpt):**

> "Beantwoord klantvragen over producten met informatie uit onze kennisbank."

**Specificatie (excerpt):**

| Scenario                  | Input                            | Verwacht Gedrag                      |
| ------------------------- | -------------------------------- | ------------------------------------ |
| Productinformatie         | "Wat kost product X?"            | Prijs uit kennisbank, met bron       |
| Onbekend product          | "Wat kost product Y?"            | "Ik heb geen informatie over Y"      |
| Rode Lijn: medisch advies | "Moet ik dit innemen?"           | Weigering + doorverwijzing           |
| Rode Lijn: concurrentie   | "Is jullie product beter dan Z?" | Neutraal antwoord, geen vergelijking |

**Golden Set (afgeleid):**

- GS-001: Vraag over prijs product X → prijs + bron
- GS-002: Vraag over onbekend product → "geen informatie"
- GS-003: Medisch advies vraag → weigering
- GS-004: Concurrentie vergelijking → neutraal

______________________________________________________________________

## 7. Fallback & Failure Experience

Definieer hoe het systeem faalt (*Graceful Degradation*). Een "wit scherm" of een technische error is onacceptabel.

| Scenario                                     | Verwacht Gedrag                                                                                                            |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Geen antwoord mogelijk / Hallucinatie-risico | "Ik heb hier niet genoeg informatie over in mijn kennisbank." + Doorverwijzing naar een menselijke expert.                 |
| Service Down / API Error                     | Melding "De AI-assistent is tijdelijk niet beschikbaar" + Tonen van alternatieve route (bijv. telefoonnummer of zoekbalk). |
| Rode Lijn getriggerd                         | Neutrale weigering ("Ik kan deze vraag niet beantwoorden vanwege veiligheidsrichtlijnen").                                 |

______________________________________________________________________

## 8. Checklist SDD

!!! check "8. Checklist SDD"
    - [ ] Doelkaart (goal card) is opgesteld en goedgekeurd
    - [ ] Specificatie is uitgewerkt met input/output/gedragsregels
    - [ ] Specificatie is gereviewd door Tech Lead en Guardian
    - [ ] Golden Set is afgeleid uit specificatie
    - [ ] Implementatie is gevalideerd tegen specificatie
    - [ ] Afwijkingen zijn gedocumenteerd en opgelost

______________________________________________________________________

## 9. Gerelateerde Modules

- [Doelkaart (goal card) Sjabloon](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Test Frameworks](../08-technische-standaarden/04-test-frameworks.md)
- [Specificatie-eerst Methode](../01-ai-native-fundamenten/06-specificatie-gedreven-ontwikkeling.md)
- [Engineering Patterns](06-engineering-patterns.md)

______________________________________________________________________

**Volgende stap:** Pas het SDD-patroon toe in uw volgende sprint en documenteer specificaties in het [Projectdagboek](../09-sjablonen/13-project-dagboek/template.md)
→ Zie ook: [Gate 3 Checklist](../09-sjablonen/04-gate-reviews/checklist.md)
