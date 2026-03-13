# Informatiearchitectuur — AI Project Blauwdruk

**Versie:** 1.0
**Datum:** 10 maart 2026
**Status:** Definitief

Dit document beschrijft de structuur, plaatsingslogica en verbindingsregels van de AI Project Blauwdruk. Het is de eerste referentie bij het toevoegen, herstructureren of beoordelen van nieuwe content.

______________________________________________________________________

## 1. Missie van de site

De Blauwdruk is een **modulaire, praktische methodologie** voor AI-projectmanagement. De site dient twee publieke doelen:

1. **Vrije referentie** voor AI Project Managers — opzoekbaar, niet lineair leesbaar
1. **Geloofwaardigheidsbasis** voor een betaald consultingaanbod

De site is **geen academische publicatie**, **geen productdocumentatie** en **geen LLM-trainingsset**. Content die niet direct een AI PM helpt beslissingen te nemen of risico's te beheersen hoort hier niet thuis.

______________________________________________________________________

## 2. Primaire doelgroep

| Persona                   | Leesdoel                               | Instappad              |
| ------------------------- | -------------------------------------- | ---------------------- |
| **AI Project Manager**    | Werkwijze, tools, governance           | Navigator → fase-gids  |
| **Tech Lead**             | Architectuurbeslissingen, standaarden  | Technische Standaarden |
| **Guardian / Compliance** | Toezicht, gate reviews, EU AI Act      | Compliance Hub         |
| **Directie / Sponsor**    | Waardebepaling, risico, besluitvorming | Executive Summary      |

De **AI PM** is de primaire gebruiker. Alle content wordt getoetst vanuit de vraag: *helpt dit een AI PM een betere beslissing te nemen?*

______________________________________________________________________

## 3. Contentlagen

De site heeft drie lagen. Elke laag heeft een eigen doel en schrijfregister.

```
Laag 1 — Strategisch Kader      (waarom en wat)
  → Principes, governance, rollen, lifecycle
  → Schrijfregister: overtuigend, beknopt, directie-niveau

Laag 2 — Operationele Fasen     (hoe, wanneer, wie)
  → Fase-voor-fase werkwijze met activiteiten, deliverables, gates
  → Schrijfregister: instructief, stapsgewijs, teamgericht

Laag 3 — Toolkit & Referentie   (invullen en opzoeken)
  → Templates, checklists, bronnen, compliance-details
  → Schrijfregister: functioneel, scanbaar, zonder proza
```

______________________________________________________________________

## 4. Sectiestructuur en plaatsingsregels

### 4.1 Sectie-overzicht

| Sectie                         | Map                                        | Laag | Bevat                                       |
| ------------------------------ | ------------------------------------------ | ---- | ------------------------------------------- |
| Navigator                      | `docs/00-navigator/`                       | 1    | Interactieve wizard — GEEN nieuwe modules   |
| Explorer Kit                   | `docs/00-explorer-kit/`                    | 2    | Versneld instappad voor Verkenners          |
| Strategisch Kader              | `docs/00-strategisch-kader/`               | 1    | Lifecycle, governance, rollen, methodologie |
| AI-Native Fundamenten          | `docs/01-ai-native-fundamenten/`           | 1    | Normatieve principes, validatiemodel, SDD   |
| Fase 1 — Verkenning            | `docs/02-fase-ontdekking/`                 | 2    | Discovery-activiteiten, HAS-H, Fast Lane    |
| Fase 2 — Validatie             | `docs/03-fase-validatie/`                  | 2    | PoV, risicotoets, business case             |
| Fase 3 — Realisatie            | `docs/04-fase-ontwikkeling/`               | 2    | Development, SDD, test                      |
| Fase 4 — Levering              | `docs/05-fase-levering/`                   | 2    | Deployment, traceerbaarheid, overdracht     |
| Fase 5 — Beheer                | `docs/06-fase-monitoring/`                 | 2    | Drift, monitoring, optimalisatie            |
| Doorlopende Verbetering        | `docs/10-doorlopende-verbetering/`         | 2    | Retrospective, Kaizen, KPI                  |
| Project Afsluiting             | `docs/11-project-afsluiting/`              | 2    | Lessons learned, decommissioning            |
| Compliance Hub                 | `docs/07-compliance-hub/`                  | 3    | EU AI Act, Red Teaming, Safety Checklist    |
| Technische Standaarden         | `docs/08-technische-standaarden/`          | 3    | MLOps, architectuur, kosten, Green AI       |
| Rollen & Verantwoordelijkheden | `docs/08-rollen-en-verantwoordelijkheden/` | 1    | Roldefinities, RACI                         |
| Toolkit & Sjablonen            | `docs/09-sjablonen/`                       | 3    | Alle invulbare sjablonen                    |
| 90-Dagen Roadmap               | `docs/12-90-dagen-roadmap/`                | 2    | Week-voor-week uitvoergids                  |
| Organisatieprofielen           | `docs/13-organisatieprofielen/`            | 1    | Verkenner / Bouwer / Visionair              |
| Drie Tracks                    | `docs/14-drie-tracks/`                     | 1    | Transformatierichtingen                     |
| Accelerators                   | `docs/15-accelerators/`                    | 2    | Snelstarttools per track                    |
| Bronnen                        | `docs/16-bronnen/`                         | 3    | Bibliografie `[so-XX]`                      |
| Bijlagen                       | `docs/17-bijlagen/`                        | 3    | Externe onderzoeksintegratie                |
| Termenlijst                    | `docs/termenlijst/`                        | 3    | Centraal glossarium                         |

### 4.2 Beslisboom voor nieuwe content

```
Is het nieuw materiaal over een BESTAAND onderwerp?
  → Ja: voeg toe aan het bestaande document. Maak geen nieuw bestand.

Is het een PRINCIPE of GOVERNANCE-beslissing?
  → Ja: hoort in Laag 1 (00-strategisch-kader of 01-ai-native-fundamenten)

Is het een WERKWIJZE per fase?
  → Ja: hoort in de betreffende fase-map (02 t/m 06)

Is het een invulbaar SJABLOON of checklist?
  → Ja: hoort in docs/09-sjablonen/ met een eigen submap

Is het COMPLIANCE-specifiek of juridisch?
  → Ja: hoort in docs/07-compliance-hub/

Is het een TECHNISCHE architectuurbeslissing?
  → Ja: hoort in docs/08-technische-standaarden/

Past het nergens?
  → Stop. Stel de vraag: "Helpt dit een AI PM een betere beslissing nemen?"
  → Nee: schrijf het niet.
```

______________________________________________________________________

## 5. Bestandsnaamgeving

### Vaste conventies

| Situatie             | Naamformaat                      | Voorbeeld                                            |
| -------------------- | -------------------------------- | ---------------------------------------------------- |
| Nederlands (default) | `[volgnummer]-[kebab-case].md`   | `03-ai-architectuur.md`                              |
| Engels (vertaling)   | `[zelfde naam].en.md`            | `03-ai-architectuur.en.md`                           |
| Sjabloon             | `template.md` / `template.en.md` | `docs/09-sjablonen/16-rag-design-canvas/template.md` |
| Index van sectie     | `index.md` / `index.en.md`       | `docs/09-sjablonen/index.md`                         |
| Cheatsheet           | `cheatsheet-[onderwerp].md`      | `cheatsheet-rode-lijnen.md`                          |

### Regels

- **Altijd kebab-case** — geen spaties, geen underscores, geen hoofdletters
- **Altijd een volgnummer** binnen een sectie-map (zorgt voor volgorde in nav)
- **Nooit** een bestand aanmaken zonder het toe te voegen aan `mkdocs.yml`
- **Nooit** een NL-bestand aanmaken zonder direct een EN-equivalent te plannen (mag later worden gevuld, maar moet in nav staan)

______________________________________________________________________

## 6. Nav-beheer (mkdocs.yml)

De navigatie staat volledig hardcoded in `mkdocs.yml`. MkDocs auto-discovery is uitgeschakeld.

### Bij toevoegen van een nieuw bestand

1. Voeg het toe aan de juiste plek in `nav:` (NL-sectie)
1. Voeg een vertaling toe in `plugins.i18n.languages[en].nav_translations`
1. Controleer of de sectie-index (`index.md`) een link bevat naar het nieuwe bestand

### Nav-diepte

- **Maximaal 3 niveaus diep** in de nav
- Niveau 1: Sectiegroep (bijv. "⚙️ Operationele Fasen")
- Niveau 2: Module of fase (bijv. "3. Realisatie")
- Niveau 3: Pagina (bijv. "SDD Patroon")
- Dieper dan 3 niveaus: heroverweeg of het een apart sjabloon moet worden

______________________________________________________________________

## 7. Cross-linken

### Verplichte links

Elk document moet bevatten:

- Een `**Gerelateerde modules:**` blok aan het einde met 2–5 relevante links
- Links naar bijbehorende sjablonen als die bestaan
- Backlink naar de fase-index als het een activiteitenpagina is

### Linkformaat

Gebruik altijd **relatieve paden**:

```markdown
[Doelkaart template](../../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
```

Gebruik **nooit** absolute URLs voor interne links.

### Taalgrens

NL-bestanden linken naar NL-bestanden. EN-bestanden linken naar EN-bestanden.
Uitzondering: als een EN-versie niet bestaat, is een link naar het NL-bestand toegestaan met een `(NL)` suffix.

______________________________________________________________________

## 8. Sjabloon-fase relatie

Elk sjabloon in `docs/09-sjablonen/` is primair gekoppeld aan één of meer fasen. Deze koppeling moet expliciet zijn in beide richtingen.

| Sjabloon                  | Primaire fase       | Secundaire fase    |
| ------------------------- | ------------------- | ------------------ |
| Project Charter           | Fase 1 — Verkenning | —                  |
| Risk Pre-Scan             | Fase 1 — Verkenning | Fase 2 — Validatie |
| Business Case             | Fase 2 — Validatie  | —                  |
| Doelkaart (Goal Card)     | Fase 1              | Fase 2, 3          |
| Prompt Engineering        | Fase 3 — Realisatie | Fase 5 — Beheer    |
| Validatierapport          | Fase 2              | Fase 3             |
| Guardian Review Checklist | Alle gates          | —                  |
| RAG Design Canvas         | Fase 3 — Realisatie | —                  |
| RACI Matrix               | Fase 1              | Alle fasen         |

**Regel:** Bij het aanmaken van een nieuw sjabloon altijd de relevante fase-activiteitenpagina bijwerken met een verwijzing naar het nieuwe sjabloon.

______________________________________________________________________

## 9. Wat hoort NIET op de site

- **Productreviews of vergelijkingen** van specifieke AI-tools (veroudert snel, geen governance-waarde)
- **Framework-specifieke implementatiegidsen** (bijv. "hoe LangChain te installeren") — deze horen in externe documentatie
- **Opiniestukken of blogposts** zonder directe methodologische waarde
- **Onvoltooide stubs** — liever geen pagina dan een lege pagina. Gebruik een `!!! info "Binnenkort"` admonition als placeholder maximaal 30 dagen.
- **Dubbele content** — als een concept al bestaat, verdiep of link naar het; maak geen tweede versie

______________________________________________________________________

## 10. Versiebeheer van de methodologie

De Blauwdruk zelf heeft een versienummer. Elk document heeft `versie: '1.x'` in de frontmatter.

| Wijziging                                           | Versie-impact                                   |
| --------------------------------------------------- | ----------------------------------------------- |
| Nieuw module of template                            | Minor bump van het betreffende document         |
| Wijziging in governance-beslissing of gate-criteria | Major bump + vermelding in BACKLOG.md           |
| Typo of stijlcorrectie                              | Geen versie-bump vereist                        |
| Verwijdering van een module                         | Major bump + deprecation notice 30 dagen vooraf |

Zie `internal-meta/BACKLOG.md` voor de roadmap van geplande uitbreidingen.

______________________________________________________________________

**Gerelateerde documenten:**

- [STYLE_GUIDE.md](STYLE_GUIDE.md) — toon, terminologie, opmaak
- [AI_COPYWRITER_CONSTITUTION.md](AI_COPYWRITER_CONSTITUTION.md) — inhoudsprincipes
- [MODULE_BESCHRIJVINGEN.md](MODULE_BESCHRIJVINGEN.md) — beschrijving per module
- [BACKLOG.md](BACKLOG.md) — geplande uitbreidingen
