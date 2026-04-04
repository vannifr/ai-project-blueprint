---
versie: '1.1'
description: 'Besluitvormingsmatrix: wie beslist wat bij elke gate, wie heeft veto-recht, en wie wordt geïnformeerd — duidelijke autoriteitsstructuur voor AI-projecten.'
type: template
layer: 1
tags: [governance, template]
summary: Expliciete vastlegging van wie welke beslissing neemt bij elke gate en wie een beslissing kan blokkeren.
answers: [Wie beslist de Go/No-Go bij een gate review?, Who decides the Go/No-Go in a gate review?]
---

# Besluitvormingsmatrix

!!! abstract "Doel"
    Expliciete vastlegging van wie welke beslissing neemt bij elke gate en wie een beslissing kan blokkeren.

## Doel

Dit document maakt expliciet wie welke beslissing neemt bij elke gate en wie een beslissing kan blokkeren. Onduidelijkheid over beslisbevoegdheid is een van de meest voorkomende oorzaken van vertraagde AI-projecten.

**Kernregel:**

- **Sponsor** is eindverantwoordelijk voor alle go/no-go beslissingen.
- **Guardian** heeft stop-recht op elke beslissing die een Rode Lijn overschrijdt.
- **Tech Lead** tekent voor technische haalbaarheid — geen go zonder diens akkoord.
- **AI PM** coördineert en informeert, maar beslist niet unilateraal.

______________________________________________________________________

## Besluitvormingsmatrix per gate

| Beslissing                                        | Accountable         | Responsible       | Veto-recht               | Consulteren               | Informeren                          |
| :------------------------------------------------ | :------------------ | :---------------- | :----------------------- | :------------------------ | :---------------------------------- |
| **Go/No-Go Gate 1** (probleemdef. & haalbaarheid) | Sponsor             | AI PM             | Guardian (Harde Grenzen) | Tech Lead, Guardian       | Stuurgroep, Finance                 |
| **Go/No-Go Gate 2** (investeringsbeslissing PoV)  | Sponsor             | AI PM + Finance   | Guardian (Harde Grenzen) | Tech Lead, Guardian       | Stuurgroep, Legal                   |
| **Go/No-Go Gate 3** (productie-go/no-go)          | Sponsor + Tech Lead | Tech Lead + AI PM | Guardian (Harde Grenzen) | Legal, Privacy Officer    | Stuurgroep, Ops                     |
| **Go/No-Go Gate 4** (kwartaalreview beheer)       | Sponsor             | AI PM + Ops       | Guardian (Harde Grenzen) | Tech Lead                 | Finance, Stuurgroep                 |
| **Stop-beslissing** (circuit breaker activering)  | Guardian            | Tech Lead         | —                        | AI PM, Sponsor            | Stuurgroep, Legal                   |
| **Moduswijziging** (Samenwerkingsmodus verhogen)  | Sponsor             | AI PM + Tech Lead | Guardian (Harde Grenzen) | Guardian, Legal           | Stuurgroep                          |
| **Technische haalbaarheid**                       | Tech Lead           | Tech Lead         | —                        | AI PM                     | Sponsor, Guardian                   |
| **Harde Grenzen aanpassen**                       | Guardian + Sponsor  | Guardian          | Sponsor (scope), Legal   | AI PM, Tech Lead, Legal   | Stuurgroep                          |
| **Model vervangen of fine-tunen**                 | Tech Lead           | Tech Lead + AI PM | Guardian (kwaliteit)     | Guardian, Privacy Officer | Sponsor, Ops                        |
| **Incident escalatie** (Hoog Risico systemen)     | Guardian            | AI PM             | —                        | Legal, Tech Lead          | Sponsor, Stuurgroep, Toezichthouder |

______________________________________________________________________

## Toelichting per rol

### Sponsor

Eindverantwoordelijk voor alle strategische go/no-go beslissingen. Heeft het mandaat om investeringen te autoriseren en projecten te stoppen. Is de enige die een Gate 1, 2 of 3 kan aftekenen.

### Guardian

Heeft **stop-recht** op elke beslissing die een Rode Lijn overschrijdt of waarbij de ethische of compliance-beoordeling negatief is. Dit stop-recht overstijgt de Sponsor bij compliance-kwesties. De Guardian initieert ook de noodrem (circuit breaker) bij Modus 4 en 5 systemen.

### Tech Lead

Tekent voor de technische haalbaarheid van elke gate. Geen productie-go zonder expliciete technische goedkeuring. Verantwoordelijk voor de architectuurbeslissingen en de kwaliteit van het Validatierapport.

### AI PM

Coördineert het besluitvormingsproces, bereidt gate-documentatie voor en informeert alle betrokkenen. Is Responsible voor de uitvoering maar niet Accountable voor de uitkomst van strategische beslissingen.

______________________________________________________________________

## Escalatieprocedure bij conflict

Als de Sponsor en de Guardian het oneens zijn:

1. Guardian documenteert het bezwaar schriftelijk in de Gate Review Checklist.
1. Een afkoelperiode van 48 uur — geen beslissing in de tussentijd.
1. Externe mediatie door een onafhankelijke AI-ethiekadviseur (bij Hoog Risico systemen verplicht).
1. Bij aanhoudend conflict: de Sponsor kan de Guardian overrulen maar neemt persoonlijk de compliance-verantwoordelijkheid over, gedocumenteerd in het projectdossier.

!!! danger "Nooit omzeilen"
    De Guardian mag niet worden omzeild door tijdsdruk of commerciële urgentie. Een overrule door de Sponsor bij een Hoog Risico systeem wordt gerapporteerd aan de stuurgroep en, indien van toepassing, aan de relevante toezichthouder.

______________________________________________________________________

**Gerelateerde modules:**

- [Rollen & Verantwoordelijkheden](index.md)
- [Gate Reviews Checklist](../09-sjablonen/08-traceerbaarheid-links/template.md)
- [Compliance Hub](../07-compliance-hub/index.md)

______________________________________________________________________

**Versie:** 1.0
**Datum:** 13 maart 2026
**Status:** Definitief
