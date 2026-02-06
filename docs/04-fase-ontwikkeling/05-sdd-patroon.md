---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# 2.3.3 Specificatie-eerst Patroon (SDD)

## 2.3.3.1 Doel

Het Specificatie-eerst Patroon (Specification-Driven Development) is een werkwijze waarbij wij eerst formeel vastleggen wat het AI-systeem moet doen, voordat we beginnen met bouwen. Dit voorkomt kostbare correcties achteraf en zorgt voor aantoonbare compliance.

______________________________________________________________________

## 2.3.3.2 Kernprincipe: Specificatie Vóór Implementatie

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Doelkaart     │ --> │  Specificatie   │ --> │  Implementatie  │
│   (Intent)      │     │  (Contract)     │     │  (Code/Prompts) │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                      │                       │
         v                      v                       v
    Wat willen we?      Hoe gedraagt het    Hoe bouwen we het?
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

## 2.3.3.3 De SDD-Cyclus

### 2.3.3.3.1 Doeldefinitie Opstellen

De **AI Product Manager** legt de business-intentie vast in de [Doelkaart](../09-sjablonen/06-ai-native-artefacten/doelkaart.md).

**Minimaal vastleggen:**

- Wat is het doel? (Doeldefinitie)
- Wat mag nooit gebeuren? (Rode Lijnen)
- Wie zijn de gebruikers?
- Wat is succes? (Meetbare criteria)

### 2.3.3.3.2 Specificatie Uitwerken

De **Tech Lead** en **ML Engineer** vertalen de Doelkaart naar een technische specificatie.

**Onderdelen van de specificatie:**

| Component               | Beschrijving                            | Voorbeeld                           |
| ----------------------- | --------------------------------------- | ----------------------------------- |
| Input-formaat           | Wat ontvangt het systeem?               | JSON met velden X, Y, Z             |
| Output-formaat          | Wat levert het systeem op?              | Gestructureerd antwoord met bronnen |
| Gedragsregels           | Hoe reageert het systeem in scenario's? | Bij vraag over X, verwijs naar Y    |
| Randvoorwaarden         | Technische beperkingen                  | Max 500 tokens, latency \< 2s       |
| Rode Lijnen (technisch) | Concrete implementatie van constraints  | Filter op PII-patronen              |

### 2.3.3.3.3 Specificatie Review

De specificatie wordt gereviewd voordat implementatie start.

**Review-checklist:**

- [ ] Dekt de specificatie alle scenario's uit de Doelkaart?
- [ ] Zijn de Rode Lijnen concreet en implementeerbaar?
- [ ] Is de specificatie testbaar (kunnen we Gouden Set afleiden)?
- [ ] Zijn edge cases beschreven?
- [ ] Guardian akkoord op Rode Lijnen-implementatie?

### 2.3.3.3.4 Gouden Set Afleiden

Vanuit de specificatie leiden we de testcases af.

**Per gedragsregel:**

- Minimaal 1 positieve testcase (happy flow)
- Minimaal 1 negatieve testcase (wat mag niet?)
- Edge cases waar relevant

### 2.3.3.3.5 Implementatie tegen Specificatie

Nu pas beginnen we met bouwen:

- Sturingsinstructies (prompts/configs) opstellen
- Integratie met databronnen
- Implementatie van filters en guardrails

### 2.3.3.3.6 Validatie tegen Specificatie

We valideren of de implementatie voldoet aan de specificatie:

- Gouden Set uitvoeren
- Resultaten vergelijken met verwachtingen
- Afwijkingen analyseren en oplossen

______________________________________________________________________

## 2.3.3.4 Voordelen van SDD

| Voordeel                | Toelichting                                   |
| ----------------------- | --------------------------------------------- |
| Vroege foutdetectie     | Fouten in intentie worden ontdekt vóór bouwen |
| Aantoonbare compliance  | Specificatie = bewijs van bedoeling           |
| Efficiënte ontwikkeling | Minder iteraties door helder contract         |
| Betere samenwerking     | Business en Tech spreken dezelfde taal        |
| Testbaarheid            | Gouden Set volgt logisch uit specificatie     |

______________________________________________________________________

## 2.3.3.5 Praktische Tips

### 2.3.3.5.1 Start Klein

Begin met de belangrijkste scenario's. Breid de specificatie iteratief uit.

### 2.3.3.5.2 Specificatie Is Levend Document

Update de specificatie wanneer requirements veranderen. Oude versies blijven bewaard voor audit.

### 2.3.3.5.3 Specificatie ≠ Documentatie

De specificatie is geen handleiding voor gebruikers, maar een contract voor ontwikkelaars en testers.

### 2.3.3.5.4 Integratie met Gates

- **Gate 2:** Specificatie goedgekeurd, Gouden Set afgeleid
- **Gate 3:** Implementatie voldoet aan specificatie

______________________________________________________________________

## 2.3.3.6 Voorbeeld: Klantenservice Chatbot

**Doelkaart (excerpt):**

> "Beantwoord klantvragen over producten met informatie uit onze kennisbank."

**Specificatie (excerpt):**

| Scenario                  | Input                            | Verwacht Gedrag                      |
| ------------------------- | -------------------------------- | ------------------------------------ |
| Productinformatie         | "Wat kost product X?"            | Prijs uit kennisbank, met bron       |
| Onbekend product          | "Wat kost product Y?"            | "Ik heb geen informatie over Y"      |
| Rode Lijn: medisch advies | "Moet ik dit innemen?"           | Weigering + doorverwijzing           |
| Rode Lijn: concurrentie   | "Is jullie product beter dan Z?" | Neutraal antwoord, geen vergelijking |

**Gouden Set (afgeleid):**

- GS-001: Vraag over prijs product X → prijs + bron
- GS-002: Vraag over onbekend product → "geen informatie"
- GS-003: Medisch advies vraag → weigering
- GS-004: Concurrentie vergelijking → neutraal

______________________________________________________________________

## 2.3.3.7 Checklist SDD

- [ ] Doelkaart is opgesteld en goedgekeurd
- [ ] Specificatie is uitgewerkt met input/output/gedragsregels
- [ ] Specificatie is gereviewd door Tech Lead en Guardian
- [ ] Gouden Set is afgeleid uit specificatie
- [ ] Implementatie is gevalideerd tegen specificatie
- [ ] Afwijkingen zijn gedocumenteerd en opgelost

______________________________________________________________________

## 2.3.3.8 Gerelateerde Modules

- [Doelkaart Sjabloon](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Test Frameworks](../08-technische-standaarden/04-test-frameworks.md)
- [Specificatie-eerst Methode](../01-ai-native-fundamenten/06-specificatie-gedreven-ontwikkeling.md)
