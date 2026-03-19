---
versie: '1.0'
type: guide
layer: 2
tags: [onboarding]
---

# 30-Dagen Dag-tot-Dag Plan

!!! abstract "Doel"
    Dit plan begeleidt teams stap voor stap door hun **eerste AI-project in 30 dagen**. Het is een concrete, dagelijkse checklist die u van probleemdefiniëring tot een werkend prototype en Gate Review brengt. Bedoeld voor teams zonder eerdere AI-ervaring die structuur nodig hebben om snel maar verantwoord te starten.

## 1. Instructies

Gebruik dit plan als uw dagelijkse gids. Vink elke activiteit af wanneer afgerond. De tijdsaanduidingen zijn indicatief voor een team van 2–3 personen.

!!! warning "Dit is een leidraad, geen rigid schema"
    Pas de planning aan uw eigen ritme aan. Als u meer tijd nodig heeft voor een stap, neem die dan. Het doel op dag 21 (Gate Review) is heilig — de dagindeling ervoor is flexibel.

______________________________________________________________________

## 2. Week 1 — Fundament (Dag 1–5)

### Dag 1–2: Project Charter Light

**Doel:** Gemeenschappelijk begrip van het probleem en de scope.

- [ ] Lees de [Verkenner Kit Overzicht](index.md) volledig (AI PM, 30 min)
- [ ] Plan een kick-off sessie met het team (1–2 uur)
- [ ] Vul sectie 1–3 van het [Project Charter Light](02-project-charter-light.md) in: Probleemstelling, Oplossingsconcept, Teamsamenstelling
- [ ] Vul sectie 4 in: Scope & Uitgesloten (wat doen we NIET)
- [ ] Laat de Sponsor het charter goedkeuren (handtekening of e-mail bevestiging)
- [ ] Sla het charter op als `project-charter-v1.md` in uw projectmap

**Gereed als:** Charter is ingevuld en goedgekeurd door Sponsor.

______________________________________________________________________

### Dag 3–4: Risk Pre-Scan Quick

**Doel:** Vroeg signaleren van blokkerende risico's (juridisch, ethisch, data).

- [ ] Lees de [Risk Pre-Scan Quick](03-risk-prescan-quick.md) (AI PM + Guardian indien beschikbaar, 20 min)
- [ ] Voer de 15 vragen uit — noteer elk antwoord
- [ ] Bereken uw risicoscore (groen / oranje / rood)
- [ ] Bij **groen**: ga door naar dag 5
- [ ] Bij **oranje**: plan een 1-uur risicosessie met een senior stakeholder
- [ ] Bij **rood**: raadpleeg de [volledige Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md) en [EU AI Act module](../07-compliance-hub/01-eu-ai-act/index.md) vóór u verdergaat — dit project vereist aanvullende compliance-maatregelen
- [ ] Documenteer de risicoscore en maatregelen in het project charter (sectie 5)

**Gereed als:** Risicoscore is bepaald en gedocumenteerd. Geen onbehandelde rode vlaggen.

______________________________________________________________________

### Dag 5: Team & Rollen

**Doel:** Duidelijk mandaat voor elke rol voor de komende 25 dagen.

- [ ] Bevestig wie de **AI PM** is (projectaansturing, dagelijkse check-in)
- [ ] Benoem indien mogelijk een **Guardian** (mini-rol: ethiek & risico bewaken)
- [ ] Plan dagelijkse stand-up (15 min, asynchroon via Slack/Teams is OK)
- [ ] Maak een gedeelde projectmap aan (SharePoint, Notion, GitHub — wat u al gebruikt)
- [ ] Sla alle artefacten op in de projectmap: charter, risicoscan

**Gereed als:** Rollen zijn bevestigd. Projectmap is aangemaakt en gedeeld.

______________________________________________________________________

## 3. Week 2 — Verkenning (Dag 6–10)

### Dag 6–8: Data-Evaluatie

**Doel:** Beoordeel of uw data geschikt is voor de gekozen use case.

- [ ] Identificeer alle potentiële databronnen (intern, extern, synthetisch)
- [ ] Voer de Data-Evaluatie checklist uit per bron:
    - [ ] **Toegang:** Kunnen we bij de data? (Ja / Nee / Gedeeltelijk)
    - [ ] **Volume:** Voldoende voorbeelden? (\< 100 = rood, 100–500 = oranje, > 500 = groen)
    - [ ] **Kwaliteit:** Is de data schoon en representatief? (Steekproef van 20 records)
    - [ ] **Privacy:** Bevat de data persoonsgegevens? (Ja → [Privacy-blad](../09-sjablonen/11-privacy-data/privacyblad.md) invullen)
    - [ ] **Licentie:** Mogen we deze data gebruiken voor AI-training/inferentie?
- [ ] Maak een datakwaliteitsscore per bron (groen/oranje/rood)
- [ ] Selecteer de beste databron(nen) voor uw prototype

**Gereed als:** Minimaal één groene databron geïdentificeerd. Privacy-risico's gedocumenteerd.

______________________________________________________________________

### Dag 9–10: Use Case Selectie

**Doel:** Kies de optimale use case voor een 30-dagen prototype.

Gebruik de scorecard hieronder. Score elke kandidaat-use case op 1 (laag) tot 3 (hoog):

| Criterium            | Omschrijving                               | Wegingsfactor |
| :------------------- | :----------------------------------------- | :------------ |
| **Impact**           | Hoe groot is het probleem dat we oplossen? | × 2           |
| **Haalbaarheid**     | Kunnen we dit in 2 weken bouwen?           | × 3           |
| **Data beschikbaar** | Is er een groene databron?                 | × 2           |
| **Risico**           | Laag risico (groen pre-scan)?              | × 2           |
| **Zichtbaarheid**    | Ziet de Sponsor resultaten?                | × 1           |

**Bereken:** (Impact × 2) + (Haalbaarheid × 3) + (Data × 2) + (Risico × 2) + (Zichtbaarheid × 1) = max 30.

- [ ] Score minimaal 2 kandidaat-use cases met de scorecard
- [ ] Selecteer de use case met de hoogste score (minimaal 18/30 aanbevolen)
- [ ] Documenteer de keuze en de afgewezen alternatieven in het project charter
    - 📄 **Document Q&A**: vragen over interne documenten, handleidingen, beleid
    - 📧 **E-mailclassificatie**: sorteren en prioriteren van inkomende berichten
    - ✍️ **Contentgeneratie**: gestructureerde tekst of rapportages genereren

______________________________________________________________________

## 4. Week 3 — Prototype Bouwen & Testen (Dag 11–17)

### Dag 11–15: Prototype Bouwen

**Doel:** Een werkend prototype dat 20 testcases kan verwerken.

- [ ] Configureer de API-sleutel en databron
- [ ] Voer de eerste testrun uit met 5 voorbeeldinputs
- [ ] Verfijn de prompt of configuratie op basis van de eerste resultaten
- [ ] Bouw een minimale interface of script voor de Sponsor-demo (dag 21)
- [ ] Commit alle code naar uw projectrepository (GitHub of intern)

!!! tip "Houd het simpel"
    Het prototype hoeft niet perfect te zijn. Een werkend notebook dat 20 cases verwerkt en reproduceerbare resultaten geeft, is voldoende voor Gate 1.

**Gereed als:** Prototype draait stabiel en verwerkt inputdata reproduceerbaar.

______________________________________________________________________

### Dag 16–17: Golden Set Test (20 Testcases)

**Doel:** Objectieve kwaliteitsmeting met een referentieset.

- [ ] Stel een Golden Set samen van **20 representatieve testcases**:
    - Kies cases die de breedte van het probleem dekken
    - Inclusief minstens 3 randgevallen (edge cases)
    - Laat een domeinexpert (niet de developer) de verwachte uitkomsten bepalen
- [ ] Voer de Golden Set door het prototype
- [ ] Scoor elk resultaat: Correct / Gedeeltelijk correct / Fout
- [ ] Bereken de kwaliteitsscore: (Correct + 0,5 × Gedeeltelijk correct) / 20 × 100%
- [ ] Documenteer afwijkingen en hun oorzaken

| Score  | Interpretatie                                | Actie                               |
| :----- | :------------------------------------------- | :---------------------------------- |
| ≥ 80%  | Goed — klaar voor Gate Review                | Ga door naar dag 18                 |
| 60–79% | Acceptabel — verbeterpunten identificeerbaar | Pas prompt aan, hertest 1×, ga door |
| \< 60% | Onvoldoende — fundamenteel probleem          | Heroverwegen use case of data       |

**Gereed als:** Kwaliteitsscore gedocumenteerd. Beslissing genomen over go/no-go voor Gate Review.

______________________________________________________________________

## 5. Week 4 — Rapportage & Beslissing (Dag 18–30)

### Dag 18–20: Validatierapport Minimaal

**Doel:** Documenteer de bevindingen voor de Gate 1 Review.

- [ ] Open het [Validatierapport Minimaal](04-validatierapport-minimal.md)
- [ ] Vul sectie 1 in: Wat hebben we gebouwd?
- [ ] Vul sectie 2 in: Werkt het? (plak de Golden Set resultaten)
- [ ] Vul sectie 3 in: Wat hebben we geleerd? (3–5 lessons learned)
- [ ] Vul sectie 4 in: Aanbeveling (Go / No-Go / Pivot)
- [ ] Laat het rapport reviewen door de Guardian (indien beschikbaar)
- [ ] Bereid een 10-minuten demo voor voor de Sponsor

**Gereed als:** Rapport is compleet. Demo is voorbereid.

______________________________________________________________________

### Dag 21: Gate 1 Review

**Doel:** Go/No-Go beslissing van de Sponsor.

- [ ] Presenteer de demo (10 minuten)
- [ ] Presenteer de kwaliteitsscore en het validatierapport (5 minuten)
- [ ] Bespreek de aanbeveling (5 minuten)
- [ ] Ontvang een expliciete beslissing: **Go / No-Go / Pivot**
- [ ] Documenteer de beslissing en de motivatie in het validatierapport
- [ ] Bij **Go**: ga door naar de [Bouwer-fase](../13-organisatieprofielen/02-ai-piloot.md) en de [Realisatiefase](../04-fase-ontwikkeling/01-doelstellingen.md)
- [ ] Bij **No-Go**: documenteer de lessen en archiveer het project netjes

______________________________________________________________________

### Dag 22–30: Iteratie of Afronding

**Bij Go-beslissing:**

- [ ] Start de [volledige Fase 1: Verkenning & Strategie](../02-fase-ontdekking/01-doelstellingen.md) met het volledige Project Charter
- [ ] Stel een formele Guardian aan (als u dat nog niet hebt)
- [ ] Plan de volgende Gate Review op basis van de roadmap

**Bij No-Go of Pivot:**

- [ ] Voer een korte [Lessons Learned](../11-project-afsluiting/01-lessons-learned.md) sessie uit (1 uur)
- [ ] Documenteer de 3 belangrijkste inzichten
- [ ] Besluit bij Pivot: welke andere use case scoort het hoogst?
- [ ] Archiveer alle artefacten in de projectmap

______________________________________________________________________

## 6. Gerelateerde Modules

- [Verkenner Kit Overzicht](index.md)
- [Project Charter Light](02-project-charter-light.md)
- [Risk Pre-Scan Quick](03-risk-prescan-quick.md)
- [Validatierapport Minimaal](04-validatierapport-minimal.md)
