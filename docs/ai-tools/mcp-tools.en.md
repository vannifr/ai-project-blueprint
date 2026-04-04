---
versie: '1.0'
type: reference
layer: 3
answers:
  - What are all the MCP tools?
  - Which tools does the Blueprint MCP server offer?
  - How do I use get_tool_cheatsheet?
  - When should I use answer_question vs search_content?
  - How do I start a session in the MCP server?
---

# MCP Tool Reference

The Blueprint MCP server provides **31 tools** and **3 resources** for AI assistants and automated workflows. Use `get_tool_cheatsheet()` as your entry point — it returns a focused table based on your intent.

!!! tip "Entry point for agents"
    Always call `get_tool_cheatsheet(intent="<your goal>")` first. The tool tells you which tool to call next.

______________________________________________________________________

## Overview by category

### Search & Answers

| Tool              | When to use                                            | Next step                              |
| ----------------- | ------------------------------------------------------ | -------------------------------------- |
| `answer_question` | Answer a substantive question about the Blueprint      | `get_template` or `get_phase_guidance` |
| `search_content`  | Search documentation by keyword, phase, layer, or type | `answer_question` or `get_template`    |

### Templates & Phase Content

| Tool                         | When to use                                       | Next step                    |
| ---------------------------- | ------------------------------------------------- | ---------------------------- |
| `get_template`               | Retrieve a template by name                       | `list_template_placeholders` |
| `get_template_for_context`   | Recommended templates for a role and phase        | `get_template`               |
| `get_phase_guidance`         | Objectives, activities or deliverables per phase  | `get_template_for_context`   |
| `template_advisor`           | Which templates do I need? (role + phase)         | `get_template`               |
| `select_template`            | Select the best template from multiple candidates | `get_template`               |
| `list_template_placeholders` | Show the fill-in fields in a template             | `fill_template`              |
| `fill_template`              | Fill in a template with provided values           | —                            |

### Analysis & Decision-making

| Tool                        | When to use                                          | Next step               |
| --------------------------- | ---------------------------------------------------- | ----------------------- |
| `classify_risk`             | Classify an AI system (EU AI Act risk tiers)         | `compliance_checklist`  |
| `check_gate_readiness`      | Evidence gap analysis for a specific gate (1–4)      | `gate_review_intake`    |
| `select_collaboration_mode` | Choose the right Collaboration Mode (1–5)            | `get_phase_guidance`    |
| `get_project_type`          | Classify the project as Type A or B                  | `project_setup_risk`    |
| `get_guidance_for_profile`  | Recommendations based on organisation profile        | `get_phase_guidance`    |
| `can_enter_phase`           | Check whether a project may enter the next phase     | `gate_review_intake`    |
| `validate_project_context`  | Validate project data against Blueprint requirements | `project_setup_charter` |

### Terminology & Utilities

| Tool                  | When to use                                    | Next step         |
| --------------------- | ---------------------------------------------- | ----------------- |
| `lookup_terminology`  | Look up Blueprint concepts and definitions     | —                 |
| `get_workflow_status` | Retrieve the status of the active workflow     | `can_enter_phase` |
| `get_tool_cheatsheet` | Navigate to the right tool based on intent     | (see table)       |
| `reload_content`      | Reload the documentation index (after updates) | —                 |

### Guided Workflows

#### Project Setup (3 steps)

| Step | Tool                    | What you provide                     | What you get back                                        |
| ---- | ----------------------- | ------------------------------------ | -------------------------------------------------------- |
| 1    | `project_setup_intake`  | Project description                  | Type A/B form + risk questions                           |
| 2    | `project_setup_risk`    | B1/B2/B3 scores (0–10)               | Risk score (green/amber/red) + Collaboration Mode advice |
| 3    | `project_setup_charter` | Project name, team, budget, timeline | Pre-filled Project Charter                               |

#### Gate Review (2 steps)

| Step | Tool                 | What you provide                   | What you get back                 |
| ---- | -------------------- | ---------------------------------- | --------------------------------- |
| 1    | `gate_review_intake` | Gate number (1–4) + evidence items | Evidence gap analysis             |
| 2    | `gate_review_report` | Gate number + gaps + actions       | Go/No-Go summary for the Guardian |

#### Compliance (2 steps)

| Step | Tool                   | What you provide               | What you get back                 |
| ---- | ---------------------- | ------------------------------ | --------------------------------- |
| 1    | `compliance_intake`    | System description             | EU AI Act risk tier + obligations |
| 2    | `compliance_checklist` | System description + risk tier | Article-referenced checklist      |

### Sessions & Project Tracking

| Tool                      | When to use                                                 |
| ------------------------- | ----------------------------------------------------------- |
| `session_start`           | Start a new workflow session for a project                  |
| `session_get_state`       | Retrieve the current session state                          |
| `session_record_artifact` | Register an artifact in the session (document, test result) |
| `list_projects`           | Overview of all active project sessions                     |

______________________________________________________________________

## Resources (read-only)

In addition to tools, the server exposes three **resources** that MCP clients can access directly:

| Resource URI                            | Content                                                               |
| --------------------------------------- | --------------------------------------------------------------------- |
| `blueprint://module/{path}`             | Full content of a Blueprint module by path                            |
| `blueprint://phase/{phase_id}/overview` | Complete overview of a phase (objectives + activities + deliverables) |
| `blueprint://glossary`                  | The complete Blueprint glossary                                       |

______________________________________________________________________

## Tool details

### `answer_question`

Answers a substantive question via semantic search (RAG) followed by keyword fallback.

```
answer_question(
    question: str,          # "How do I classify the risk of my AI project?"
    output_format: str      # "markdown" (default) or "json"
)
```

Returns up to 3 results: the best match with full content, the rest with summaries.

______________________________________________________________________

### `search_content`

Search documentation by keyword with optional filters.

```
search_content(
    query: str,             # Search terms
    type: str | None,       # "template", "guide", "objectives", "activities", "deliverables", "compliance"
    phase: int | None,      # Phase 1–5
    layer: int | None,      # 1=Strategic, 2=Operational, 3=Toolkit
    tag: str | None,        # "risk", "gate-review", "onboarding", "rag", "monitoring"
    output_format: str
)
```

______________________________________________________________________

### `get_template`

Retrieve a template by name (exact or partial match).

```
get_template(
    name: str,              # E.g. "Project Charter", "Gate 2 Checklist"
    output_format: str
)
```

______________________________________________________________________

### `check_gate_readiness`

Compare provided evidence against the required gate criteria.

```
check_gate_readiness(
    gate: int,              # Gate number 1–4
    evidence: list[str],    # List of available evidence items
    output_format: str
)
```

______________________________________________________________________

### `classify_risk`

Classify an AI system into an EU AI Act risk tier.

```
classify_risk(
    system_description: str,  # Description of the AI system
    output_format: str
)
```

Returns: `unacceptable` / `high` / `limited` / `minimal` with obligations per tier.

______________________________________________________________________

### `compliance_checklist`

Generate an article-referenced EU AI Act checklist.

```
compliance_checklist(
    system_description: str,
    risk_category: str,       # "unacceptable", "high", "limited", or "minimal"
    output_format: str
)
```

!!! warning "Validation"
    `risk_category` is validated. Always use the English category name. Unknown values return an error.

______________________________________________________________________

### `session_start`

Start a session to track progress, artifacts, and gate results.

```
session_start(
    project_id: str,        # Project identifier (e.g. "fraud-detection-v2")
    project_type: str,      # E.g. "NLP", "CV", "Recommender"
    language: str,          # "nl" (default) or "en"
    output_format: str
)
```

Returns a `session_id` for use in subsequent calls.

______________________________________________________________________

### `get_tool_cheatsheet`

Returns a table of all tools, when to use them, and what the next step is.

```
get_tool_cheatsheet(
    intent: str,            # "gate", "risk", "template", "search", "session", "phase", or empty for all
    output_format: str
)
```

______________________________________________________________________

## Installation

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

### Cursor / other MCP clients

Add an HTTP MCP server with URL `https://ai-delivery.io/mcp`.
