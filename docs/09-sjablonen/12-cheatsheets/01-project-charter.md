---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [AI Product Manager]
tags: [quick-reference]
---

# Cheatsheet — Project Charter

**Bron:** [Project Charter Template](../01-project-charter/template.md)

______________________________________________________________________

## Verplichte Secties

| Sectie                | Kernvraag                                  | Valkuil                               |
| :-------------------- | :----------------------------------------- | :------------------------------------ |
| **Probleemstelling**  | Welk concreet probleem lossen we op?       | Te breed of te technisch geformuleerd |
| **AI-doelstelling**   | Wat doet het AI-systeem precies?           | Verwarren van output met uitkomst     |
| **Succescriteria**    | Hoe weten we dat het gelukt is? (meetbaar) | Ontbreken van baseline                |
| **Scope**             | Wat valt wel/niet in scope?                | Scope creep door vage grenzen         |
| **Risico's**          | Top 3 risico's + mitigatie                 | Enkel technische risico's benoemen    |
| **Stakeholders**      | Wie is verantwoordelijk, wie betrokken?    | Guardian ontbreekt                    |
| **Budget & Tijdlijn** | Fase-budget + mijlpalen                    | Geen rekening met iteraties           |

______________________________________________________________________

## Minimale Kwaliteitscriteria

- [ ] Succescriteria zijn **meetbaar** (getal + tijdframe)
- [ ] Baseline is **vastgesteld** (huidige prestatie)
- [ ] **Guardian** is benoemd en heeft getekend
- [ ] Risicoclassificatie (Hoog / Beperkt / Minimaal) is bepaald
- [ ] Business Case is goedgekeurd of in voorbereiding
- [ ] Charter is ondertekend door opdrachtgever

______________________________________________________________________

## Rode Vlaggen

!!! danger "Stop als..."
    - Geen meetbare succescriteria zijn geformuleerd
    - De probleemstelling begint met een technologiekeuze ("We gaan ChatGPT gebruiken voor...")
    - Geen eigenaar/Guardian is aangewezen
    - Budget of tijdlijn volledig ontbreekt

______________________________________________________________________

## Snelreferentie Risicoclassificatie

| Risico       | Kenmerken                                                     |
| :----------- | :------------------------------------------------------------ |
| **Hoog**     | Beslissingen over mensen, medisch, juridisch, veiligheid      |
| **Beperkt**  | Klantcontact, geautomatiseerde content, aanbevelingen         |
| **Minimaal** | Intern gebruik, niet-beslissend, menselijk eindoordeel altijd |

**Bron:** [EU AI Act classificatie](../../07-compliance-hub/01-eu-ai-act/index.md)
