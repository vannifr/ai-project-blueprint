---
versie: '1.0'
type: reference
layer: 3
answers:
  - Wat zijn alle MCP tools?
  - Welke tools biedt de Blueprint MCP-server?
  - Hoe gebruik ik get_tool_cheatsheet?
  - Wanneer gebruik ik answer_question vs search_content?
  - Hoe start ik een sessie in de MCP-server?
---

# MCP Tool Referentie

De Blueprint MCP-server biedt **31 tools** en **3 resources** voor AI-assistenten en geautomatiseerde workflows. Gebruik `get_tool_cheatsheet()` als startpunt — dat geeft een gerichte tabel op basis van je intent.

!!! tip "Startpunt voor agents"
    Roep altijd eerst `get_tool_cheatsheet(intent="<jouw doel>")` aan. De tool vertelt je welke tool je als volgende moet aanroepen.

______________________________________________________________________

## Overzicht per categorie

### Zoeken & Antwoorden

| Tool              | Wanneer gebruiken                                   | Volgende stap                          |
| ----------------- | --------------------------------------------------- | -------------------------------------- |
| `answer_question` | Beantwoord een inhoudelijke vraag over de Blauwdruk | `get_template` of `get_phase_guidance` |
| `search_content`  | Zoek documentatie op trefwoord, fase, laag of type  | `answer_question` of `get_template`    |

### Templates & Fase-inhoud

| Tool                         | Wanneer gebruiken                                     | Volgende stap                |
| ---------------------------- | ----------------------------------------------------- | ---------------------------- |
| `get_template`               | Haal een template op bij naam                         | `list_template_placeholders` |
| `get_template_for_context`   | Aanbevolen templates voor een rol en fase             | `get_template`               |
| `get_phase_guidance`         | Doelstellingen, activiteiten of opleveringen per fase | `get_template_for_context`   |
| `template_advisor`           | Welke templates heb ik nodig? (rol + fase)            | `get_template`               |
| `select_template`            | Selecteer het beste template uit meerdere kandidaten  | `get_template`               |
| `list_template_placeholders` | Toon de invulvelden in een template                   | `fill_template`              |
| `fill_template`              | Vul een template in met opgegeven waarden             | —                            |

### Analyse & Besluitvorming

| Tool                        | Wanneer gebruiken                                   | Volgende stap           |
| --------------------------- | --------------------------------------------------- | ----------------------- |
| `classify_risk`             | Classificeer een AI-systeem (EU AI Act risicotiers) | `compliance_checklist`  |
| `check_gate_readiness`      | Bewijsgapanalyse voor een specifieke gate (1–4)     | `gate_review_intake`    |
| `select_collaboration_mode` | Kies het juiste Collaboration Mode (1–5)            | `get_phase_guidance`    |
| `get_project_type`          | Classificeer het project als Type A of B            | `project_setup_risk`    |
| `get_guidance_for_profile`  | Aanbevelingen op basis van organisatieprofiel       | `get_phase_guidance`    |
| `can_enter_phase`           | Controleer of een project de volgende fase mag in   | `gate_review_intake`    |
| `validate_project_context`  | Valideer projectdata tegen Blauwdruk-vereisten      | `project_setup_charter` |

### Terminologie & Hulp

| Tool                  | Wanneer gebruiken                                | Volgende stap     |
| --------------------- | ------------------------------------------------ | ----------------- |
| `lookup_terminology`  | Opzoeken van Blauwdruk-begrippen en definities   | —                 |
| `get_workflow_status` | Status van de actieve workflow opvragen          | `can_enter_phase` |
| `get_tool_cheatsheet` | Navigeer naar de juiste tool op basis van intent | (zie tabel)       |
| `reload_content`      | Herlaad de documentatie-index (na updates)       | —                 |

### Begeleide Workflows

#### Project Setup (3 stappen)

| Stap | Tool                    | Wat je invult                       | Wat je terugkrijgt                                         |
| ---- | ----------------------- | ----------------------------------- | ---------------------------------------------------------- |
| 1    | `project_setup_intake`  | Projectbeschrijving                 | Typeformulier A/B + risicovragen                           |
| 2    | `project_setup_risk`    | B1/B2/B3-scores (0–10)              | Risicoscore (groen/amber/rood) + Collaboration Mode advies |
| 3    | `project_setup_charter` | Projectnaam, team, budget, tijdlijn | Vooringevuld Project Charter                               |

#### Gate Review (2 stappen)

| Stap | Tool                 | Wat je invult                     | Wat je terugkrijgt                     |
| ---- | -------------------- | --------------------------------- | -------------------------------------- |
| 1    | `gate_review_intake` | Gate-nummer (1–4) + bewijsstukken | Bewijsgapanalyse                       |
| 2    | `gate_review_report` | Gate-nummer + gaps + acties       | Go/No-Go samenvatting voor de Guardian |

#### Compliance (2 stappen)

| Stap | Tool                   | Wat je invult                     | Wat je terugkrijgt                     |
| ---- | ---------------------- | --------------------------------- | -------------------------------------- |
| 1    | `compliance_intake`    | Systeembeschrijving               | EU AI Act risico-tier + verplichtingen |
| 2    | `compliance_checklist` | Systeembeschrijving + risico-tier | Artikelgerichte checklist              |

### Sessies & Projectbeheer

| Tool                      | Wanneer gebruiken                                              |
| ------------------------- | -------------------------------------------------------------- |
| `session_start`           | Start een nieuwe werkflow-sessie voor een project              |
| `session_get_state`       | Haal de huidige sessie-status op                               |
| `session_record_artifact` | Registreer een artefact in de sessie (document, testresultaat) |
| `list_projects`           | Overzicht van alle actieve projectsessies                      |

______________________________________________________________________

## Resources (alleen-lezen)

Naast tools biedt de server drie **resources** die MCP-clients direct kunnen openen:

| Resource URI                            | Inhoud                                                                 |
| --------------------------------------- | ---------------------------------------------------------------------- |
| `blueprint://module/{path}`             | Volledige inhoud van een Blauwdruk-module op pad                       |
| `blueprint://phase/{phase_id}/overview` | Compleet overzicht van een fase (doelen + activiteiten + opleveringen) |
| `blueprint://glossary`                  | De volledige Blauwdruk-termenlijst                                     |

______________________________________________________________________

## Tool-details

### `answer_question`

Beantwoordt een inhoudelijke vraag via semantisch zoeken (RAG) gevolgd door trefwoord-fallback.

```
answer_question(
    question: str,          # "Hoe classificeer ik het risico van mijn AI-project?"
    output_format: str      # "markdown" (standaard) of "json"
)
```

Geeft tot 3 resultaten terug: het beste match met volledige inhoud, de rest met samenvatting.

______________________________________________________________________

### `search_content`

Doorzoek de documentatie op trefwoord met optionele filters.

```
search_content(
    query: str,             # Zoektermen
    type: str | None,       # "template", "guide", "objectives", "activities", "deliverables", "compliance"
    phase: int | None,      # Fase 1–5
    layer: int | None,      # 1=Strategisch, 2=Operationeel, 3=Toolkit
    tag: str | None,        # "risk", "gate-review", "onboarding", "rag", "monitoring"
    output_format: str
)
```

______________________________________________________________________

### `get_template`

Haal een template op bij naam (exacte of gedeeltelijke match).

```
get_template(
    name: str,              # Bv. "Project Charter", "Gate 2 Checklist"
    output_format: str
)
```

______________________________________________________________________

### `check_gate_readiness`

Vergelijk opgegeven bewijsstukken met de vereiste gate-criteria.

```
check_gate_readiness(
    gate: int,              # Gate-nummer 1–4
    evidence: list[str],    # Lijst van aanwezige bewijsstukken
    output_format: str
)
```

______________________________________________________________________

### `classify_risk`

Classificeer een AI-systeem in een EU AI Act risico-tier.

```
classify_risk(
    system_description: str,  # Beschrijving van het AI-systeem
    output_format: str
)
```

Geeft terug: `unacceptable` / `high` / `limited` / `minimal` met verplichtingen per tier.

______________________________________________________________________

### `compliance_checklist`

Genereer een artikelgerichte EU AI Act checklist.

```
compliance_checklist(
    system_description: str,
    risk_category: str,       # "unacceptable", "high", "limited" of "minimal"
    output_format: str
)
```

!!! warning "Validatie"
    `risk_category` wordt gevalideerd. Gebruik altijd de Engelse categorienaam. Onbekende waarden geven een foutmelding terug.

______________________________________________________________________

### `session_start`

Start een sessie om voortgang, artefacten en gate-resultaten bij te houden.

```
session_start(
    project_id: str,        # Projectidentificatie (bv. "fraud-detection-v2")
    project_type: str,      # Bv. "NLP", "CV", "Recommender"
    language: str,          # "nl" (standaard) of "en"
    output_format: str
)
```

Geeft een `session_id` terug voor gebruik in volgende aanroepen.

______________________________________________________________________

### `get_tool_cheatsheet`

Geeft een tabel met alle tools, wanneer ze te gebruiken en wat de volgende stap is.

```
get_tool_cheatsheet(
    intent: str,            # "gate", "risk", "template", "search", "session", "phase", of leeg voor alles
    output_format: str
)
```

______________________________________________________________________

## Installatie

### Claude Code (CLI)

```bash
claude mcp add blueprint --transport http https://ai-delivery.io/mcp
```

### Claude Desktop

```json
{
  "mcpServers": {
    "blueprint": {
      "type": "http",
      "url": "https://ai-delivery.io/mcp"
    }
  }
}
```

### Cursor / andere MCP-clients

Voeg een HTTP MCP-server toe met URL `https://ai-delivery.io/mcp`.
