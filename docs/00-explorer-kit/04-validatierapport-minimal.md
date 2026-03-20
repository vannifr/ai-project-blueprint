---
versie: '1.0'
type: guide
layer: 2
roles: [Data Scientist]
tags: [onboarding, validation]
answers: [Hoe werkt Validatierapport Minimaal?]
---

# Validatierapport Minimaal

## Instructies

Vul dit rapport in op dag 18–20 als voorbereiding op de Gate 1 Review (dag 21). Het rapport is bewust kort gehouden: **2 pagina's, 60–90 minuten invullen**.

De volledige versie van het validatierapport vindt u in [Validatierapport (volledig)](../09-sjablonen/07-validatie-bewijs/validatierapport.md).

______________________________________________________________________

**Project:** \[Naam\]
**Periode:** \[Startdatum\] – \[Einddatum prototype\]
**AI PM:** \[Naam\]
**Developer:** \[Naam\]
**Sponsor:** \[Naam\]
**Gate 1 Review datum:** \[Datum\]

______________________________________________________________________

## Sectie 1 — Wat hebben we gebouwd?

### 1.1 Oplossingsbeschrijving (3–5 zinnen)

\[Beschrijf het prototype. Wat doet het systeem? Hoe werkt het? Welke technologie is gebruikt? Welke samenwerkingsmodus (1–4)?

Bijv.: We hebben een document Q&A-systeem gebouwd dat vragen over onze interne beleidshandleidingen beantwoordt. Het systeem gebruikt RAG (Retrieval-Augmented Generation) om relevante passages op te zoeken en een antwoord te formuleren. De eindgebruiker stelt een vraag via een Jupyter notebook interface; het systeem geeft een antwoord én de bronpassages. Een medewerker beoordeelt het antwoord vóór gebruik (Modus 2 — Adviserend).\]

### 1.2 Technische Configuratie

| Parameter          | Waarde                                                            |
| :----------------- | :---------------------------------------------------------------- |
| AI-model / API     | \[bijv. Claude claude-haiku-4-5 via Anthropic API\]               |
| Databron           | \[bijv. 45 interne PDF-beleidsdocumenten, totaal 320 pagina's\]   |
| Interface          | \[bijv. Jupyter notebook / Python script / Eenvoudige webpagina\] |
| Samenwerkingsmodus | \[bijv. Modus 2 — Adviserend\]                                    |
| Repository         | \[bijv. GitHub repo link of interne locatie\]                     |

______________________________________________________________________

## Sectie 2 — Werkt het? (Golden Set Resultaten)

### 2.1 Testopzet

| Parameter                     | Waarde                                         |
| :---------------------------- | :--------------------------------------------- |
| Aantal testcases (Golden Set) | \[bijv. 20\]                                   |
| Opgesteld door                | \[bijv. Naam domeinexpert, niet de developer\] |
| Testdatum                     | \[Datum\]                                      |
| Randgevallen (edge cases)     | \[bijv. 4 van de 20 cases\]                    |

### 2.2 Resultaten

| Categorie               | Aantal | Percentage                                     |
| :---------------------- | :----- | :--------------------------------------------- |
| ✅ Correct              |        |                                                |
| ⚠️ Gedeeltelijk correct |        |                                                |
| ❌ Fout                 |        |                                                |
| **Kwaliteitsscore**     |        | **(Correct + 0,5 × Gedeeltelijk) / 20 × 100%** |

**Kwaliteitsscore:** \_\_\_%

### 2.3 Opmerkelijke Bevindingen

*Beschrijf maximaal 3 opvallende successen of tekortkomingen.*

| #   | Bevinding                                                                  | Oorzaak                               | Impact               |
| :-- | :------------------------------------------------------------------------- | :------------------------------------ | :------------------- |
| 1   | \[Bijv. Systeem presteert slecht op vragen over wetgeving ouder dan 2020\] | \[Bijv. Oude PDF's niet geïndexeerd\] | \[Laag/Middel/Hoog\] |
| 2   |                                                                            |                                       |                      |
| 3   |                                                                            |                                       |                      |

______________________________________________________________________

## Sectie 3 — Wat hebben we geleerd?

*Noteer 3–5 concrete lessen. Focus op inzichten die waardevol zijn voor de volgende fase, niet op technische details.*

| #   | Les                                                                                       | Aanbeveling voor volgende fase                                        |
| :-- | :---------------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| 1   | \[Bijv. De datakwaliteit van oude PDF's is een grotere bottleneck dan verwacht.\]         | \[Bijv. Investeer in documenthygiëne vóór Fase 2.\]                   |
| 2   | \[Bijv. Domeinexperts stellen veel vragen over context die niet in de documenten staat.\] | \[Bijv. Overweeg een FAQ-aanvulling of expliciete scope-afbakening.\] |
| 3   |                                                                                           |                                                                       |
| 4   |                                                                                           |                                                                       |
| 5   |                                                                                           |                                                                       |

______________________________________________________________________

## Sectie 4 — Aanbeveling

### 4.1 Eindoordeel

*Kies één optie en motiveer in maximaal 3 zinnen.*

- [ ] ✅ **Go** — Het prototype bewijst de waarde van de use case. We gaan door naar de Bouwer-fase met een volledig project charter.
- [ ] 🔄 **Pivot** — De use case is haalbaar, maar we passen de scope/aanpak aan. \[Beschrijf de pivot.\]
- [ ] ⛔ **No-Go** — Het prototype heeft de waarde niet aangetoond. We stoppen het project en documenteren de lessen.

**Motivatie (max. 3 zinnen):**

\[Bijv. Het prototype behaalt een kwaliteitsscore van 85% op de Golden Set en bespaart per e-mail gemiddeld 8 minuten verwerkingstijd. De technische aanpak is haalbaar en de data is van voldoende kwaliteit. We bevelen Go aan mits de scope expliciet wordt beperkt tot NL-talige e-mails.\]

### 4.2 Randvoorwaarden voor Go (alleen bij Go-beslissing)

*Wat moet er geregeld zijn vóór de Bouwer-fase start?*

- [ ] \[Bijv. Formele Guardian benoemd (naam: \_\_\_)\]
- [ ] \[Bijv. Privacy Impact Assessment uitgevoerd voor persoonsgegevens in e-mails\]
- [ ] \[Bijv. Budget goedgekeurd voor productie-infrastructuur (€ \_\_\_)\]
- [ ] \[Bijv. Volledige Project Charter ingevuld vóór \[datum\]\]

______________________________________________________________________

## Beslissing Gate 1 Review

|                                       |     |
| :------------------------------------ | :-- |
| **Beslissing (Go / No-Go / Pivot):**  |     |
| **Datum:**                            |     |
| **Naam Sponsor:**                     |     |
| **Handtekening / E-mailbevestiging:** |     |
| **Motivatie Sponsor (optioneel):**    |     |

______________________________________________________________________

## Gerelateerde Modules

- [30-Dagen Plan](01-30-dagen-plan.md)
- [Volledig Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md)
- [Fase 3: Realisatie (volgende stap na Go)](../04-fase-ontwikkeling/01-doelstellingen.md)
- [Lessons Learned Template](../11-project-afsluiting/01-lessons-learned.md)
