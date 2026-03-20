---
versie: '1.1'
type: activities
layer: 2
phase: [2]
roles: [AI Product Manager, Data Scientist]
tags: [validation]
summary: Overzicht van de kernactiviteiten en rolverdelingen tijdens de Validatiefase, inclusief de Validatiepilot (PoV) en Business Case opstelling.
answers: [Welke activiteiten voer ik uit in deze fase?, Hoeveel validatie is voldoende?]
---

# 1. Kernactiviteiten & Rollen (Validatie)

!!! abstract "Doel"
    Overzicht van de kernactiviteiten en rolverdelingen tijdens de Validatiefase, inclusief de Validatiepilot (PoV) en Business Case opstelling.

## 1. Kernactiviteiten

### Validatiepilot (PoV)

Een kleinschalig experiment om te testen of de AI de specifieke bedrijfscontext begrijpt.

- **Testset Samenstellen:** Verzamel 50-100 representatieve voorbeelden uit de praktijk
- **Baseline Meting:** Hoe presteren mensen of bestaande systemen nu?
- **AI Experiment:** Laat de AI dezelfde voorbeelden verwerken
- **Succescriterium:** Scoort de AI een voldoende (>90%) op de testset?

### Betrouwbaarheidstesten

Statistische check of de resultaten stabiel zijn en niet op toeval berusten.

- **Reproduceerbaarheid:** Geeft de AI consistente antwoorden bij herhaling?
- **Edge Cases:** Hoe reageert het systeem op ongewone of extreme input?
- **Bias Detectie:** Zijn er systematische fouten in bepaalde categorieën?

### Het Kostenoverzicht

Een volledige raming van investering en operationele kosten.

#### Investeringskosten

- **Mensen:** Ontwikkeling, training, beheer (FTE's)
- **Technologie:** Licenties, cloud-infrastructuur, tools
- **Data:** Opschoning, labeling, verrijking

#### Operationele Kosten (per maand/jaar)

- **Gebruikskosten:** Cloud/API-kosten per taak of transactie
- **Onderhoud:** Monitoring, updates, ondersteuning
- **Risico:** Mogelijke kosten van fouten of incidenten

#### Return on Investment (ROI)

- **Tijdwinst:** Hoeveel uur besparen we per week/maand?
- **Kwaliteitsverbetering:** Minder fouten, hogere klanttevredenheid
- **Omzetgroei:** Nieuwe mogelijkheden, snellere doorlooptijd

## 2. Team & Rollen

| Rol                    | Verantwoordelijkheid in Validatie                                                       |
| :--------------------- | :-------------------------------------------------------------------------------------- |
| **Data Scientist**     | **R**esponsible: Uitvoeren van de Validatiepilot (PoV) en betrouwbaarheidstesten.       |
| **AI Product Manager** | **A**ccountable: Eigenaar van de business case en ROI-berekening (Het Kostenoverzicht). |
| **Business Sponsor**   | **C**onsulted: Valideert de testset en succescriteria.                                  |
| **Finance**            | **C**onsulted: Controleert de kostenraming en ROI-berekening.                           |
| **Stakeholders**       | **I**nformed: Ontvangen updates over de voortgang.                                      |

______________________________________________________________________

## 5. Gerelateerde Modules

**Sjablonen:**

- [Business Case & Modelkaart](../09-sjablonen/02-business-case/template.md)
- [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)

**Zie ook:** [Overzicht Fase 2](01-doelstellingen.md) · [Opleveringen](03-afleveringen.md)

______________________________________________________________________

**Volgende stap:** Voer de Validatiepilot uit en documenteer de resultaten in het Validatierapport.
→ Gebruik het [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md) als startpunt.
→ Zie ook: [Business Case](../09-sjablonen/02-business-case/template.md) | [Gate 2 Checklist](../09-sjablonen/04-gate-reviews/checklist.md)
