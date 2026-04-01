# Blueprint MCP Server

MCP server that exposes the AI Project Blueprint as callable tools for AI agents (Claude Desktop, Claude Code, Cursor, etc.).

## Setup

```bash
cd mcp_server
uv venv && uv pip install -e . pytest
```

## Usage

### Claude Code (`.claude/settings.json`)

```json
{
  "mcpServers": {
    "blueprint": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/mcp_server", "blueprint-mcp"]
    }
  }
}
```

### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "blueprint": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/mcp_server", "blueprint-mcp"],
      "env": {
        "BLUEPRINT_DOCS_PATH": "/path/to/ai-project-blueprint/docs",
        "BLUEPRINT_LANGUAGE": "en"
      }
    }
  }
}
```

### Environment variables

| Variable              | Default                            | Description                      |
| --------------------- | ---------------------------------- | -------------------------------- |
| `BLUEPRINT_DOCS_PATH` | `../../docs` (relative to package) | Path to the `docs/` directory    |
| `BLUEPRINT_LANGUAGE`  | `en`                               | Language to index (`en` or `nl`) |

## Agent Workflows (8 tools)

Guided multi-step workflows. The calling LLM orchestrates the steps and collects user input between them. Each workflow tool description explicitly tells the LLM when to use it and what to call next.

### Project Setup Agent

| Tool                    | Step | Description                                                     |
| ----------------------- | ---- | --------------------------------------------------------------- |
| `project_setup_intake`  | 1    | Classify Type A/B + present EU AI Act risk pre-scan questions   |
| `project_setup_risk`    | 2    | Score B1/B2/B3 → green/amber/red + recommend collaboration mode |
| `project_setup_charter` | 3    | Generate pre-filled Project Charter with accumulated context    |

### Gate Review Agent

| Tool                 | Step | Description                                     |
| -------------------- | ---- | ----------------------------------------------- |
| `gate_review_intake` | 1    | Present gate checklist + identify evidence gaps |
| `gate_review_report` | 2    | Generate Guardian-ready Go/No-Go summary        |

### Template Advisor

| Tool               | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| `template_advisor` | Recommend and return templates for a role + phase with context pre-filled |

### Compliance Agent

| Tool                   | Step | Description                                                    |
| ---------------------- | ---- | -------------------------------------------------------------- |
| `compliance_intake`    | 1    | Heuristic EU AI Act risk classification + relevant obligations |
| `compliance_checklist` | 2    | Article-referenced checklist per risk category                 |

## Standalone Tools (11)

| Tool                        | Description                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| `answer_question`           | Find relevant Blueprint pages for a natural language question           |
| `get_template_for_context`  | Get templates for a role + phase combination                            |
| `get_phase_guidance`        | Get objectives, activities, or deliverables for a lifecycle phase (1-5) |
| `get_template`              | Retrieve a template by name (fuzzy match)                               |
| `check_gate_readiness`      | Compare evidence against gate review checklist                          |
| `classify_risk`             | Get risk classification framework + EU AI Act categories                |
| `select_collaboration_mode` | Get HAS-H collaboration mode guidance                                   |
| `lookup_terminology`        | Search the Blueprint glossary                                           |
| `get_project_type`          | Get Type A vs Type B classification framework                           |
| `search_content`            | Full-text search with filters (type, phase, layer, tag)                 |
| `reload_content`            | Reload all docs from disk without restarting the server                 |

## Resources (3)

| URI                               | Description                                             |
| --------------------------------- | ------------------------------------------------------- |
| `blueprint://module/{path}`       | Full content of a specific module                       |
| `blueprint://phase/{id}/overview` | Phase overview (objectives + activities + deliverables) |
| `blueprint://glossary`            | Complete glossary                                       |

## Content updates

The server loads all 276 docs at startup. After editing files in `docs/`, either:

- Call the `reload_content` tool to refresh the index
- Restart the server (takes ~1 second)

## Tests

```bash
cd mcp_server
.venv/bin/pytest tests/ -v
```

## Development

```bash
# Run with MCP inspector
.venv/bin/mcp dev src/blueprint_mcp/server.py

# Run directly
.venv/bin/blueprint-mcp
```
