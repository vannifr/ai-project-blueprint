# AI Project Blueprint

![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-green)
![Version](https://img.shields.io/badge/version-1.5-blue)
![Build Status](https://github.com/vannifr/ai-project-blueprint/actions/workflows/ci.yml/badge.svg)
![Languages](https://img.shields.io/badge/languages-NL%20%7C%20EN-informational)

A comprehensive documentation hub for AI project management, based on PMI-CPMAI standards, EU AI Act compliance, and Agile-AI frameworks.

**Live site:** [ai-delivery.io](https://ai-delivery.io/) | **Mirror:** [vannifr.github.io/ai-project-blueprint](https://vannifr.github.io/ai-project-blueprint/)

## Authors

- **Frederik Vannieuwenhuyse** — [@vannifr](https://github.com/vannifr)
- **Hadrien-Joseph van Durme** — [@hvandurme](https://github.com/hvandurme)

## About

This blueprint provides a standardized, modular approach to managing AI projects from ideation to monitoring. It helps teams navigate the complexity of AI-native development, compliance, and organizational adoption.

### Core Modules

| Module                       | Description                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| **Strategic Framework**      | AI lifecycle, hybrid methodology, governance, and Collaboration Modes (5 levels)        |
| **AI-Native Foundations**    | Goal maps, evidence standards, risk classification, and specification-driven validation |
| **Operational Phases (1-5)** | From Exploration to Monitoring — with Gate Reviews, RACI matrices, and CTA blocks       |
| **Compliance Hub**           | EU AI Act, risk management, ethical guidelines, incident response, and red teaming      |
| **Toolkit & Templates**      | 50+ fillable templates, cheatsheets, Gate Review checklists, and RAG Design Canvas      |
| **90-Day Roadmap**           | Actionable launch plan in 3 phases (Focus > Pilot > Scale) with risk-adjusted timelines |
| **Organization Profiles**    | Three maturity levels (Explorer, Builder, Visionary) with growth guide                  |
| **Three Tracks**             | Strategic reinvention, operational redesign, and AI-first business model                |
| **Explorer Kit**             | 30-day plan for organizations starting with AI                                          |

### Architecture

The documentation is built on three layers:

- **Layer 1 — Strategic:** Why and what (executive-level, persuasive)
- **Layer 2 — Operational:** How, when, who (instructional, step-by-step)
- **Layer 3 — Toolkit:** Fillable templates and reference material (functional, scannable)

## Getting Started

### Online

Visit [ai-delivery.io](https://ai-delivery.io/) and use the **Blueprint Navigator** to find a personalized path through the documentation.

### Run Locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Open [http://localhost:8000](http://localhost:8000).

### LLM Access

The full documentation is available as plain text for AI assistants:

- [llms.txt](https://ai-delivery.io/llms.txt) — Table of contents
- [llms-full.txt](https://ai-delivery.io/llms-full.txt) — Full content (EN)
- [llms-full-nl.txt](https://ai-delivery.io/llms-full-nl.txt) — Full content (NL)

### Blueprint Assistent & MCP Server

The live site includes two backend services:

| Service                 | Endpoint                      | Description                                                               |
| ----------------------- | ----------------------------- | ------------------------------------------------------------------------- |
| **Blueprint Assistent** | `https://ai-delivery.io/api/` | Chat widget — RAG + LLM, answers Blueprint questions in NL and EN         |
| **MCP Server**          | `https://ai-delivery.io/mcp`  | 31 tools: guided agent workflows, search, templates, and session tracking |

Both run as Docker containers behind nginx. Embeddings use `all-MiniLM-L6-v2` (local ONNX, no API key needed).

**Add the MCP server to Claude Code:**

```bash
claude mcp add blueprint --transport http https://ai-delivery.io/mcp
```

**Agent workflows available via MCP:**

| Workflow             | Trigger                                       | Steps                            |
| -------------------- | --------------------------------------------- | -------------------------------- |
| **Project Setup**    | "Help me set up a new AI project"             | Intake → Risk → Charter          |
| **Gate Review**      | "Help me prepare for Gate 2"                  | Intake → Report                  |
| **Compliance**       | "Is my system compliant with the EU AI Act?"  | Intake → Checklist               |
| **Session Tracking** | "Start a project session"                     | Start → Record artifacts → State |
| **Template Advisor** | "Which templates do I need as PM in phase 3?" | Single step                      |
| **Search & Q&A**     | "What are the Gate 1 requirements?"           | search_content / answer_question |

Call `get_tool_cheatsheet()` for a structured overview of all 31 tools and when to use each one.

## Deploy

Initial setup on a Debian VPS with Docker + nginx:

```bash
cd deploy
cp .env.example .env   # fill in CHAT_OLLAMA_API_KEY
bash setup.sh
```

The script handles SSL (Let's Encrypt), MkDocs build, nginx config, Docker containers, and RAG index in one run. See [`deploy/`](deploy/) for details.

To deploy updates after a code or content change:

```bash
cd deploy
bash update.sh
```

## Language Support

The site is built in two languages using the **file suffix strategy** (`mkdocs-static-i18n`):

| Language        | Suffix   | URL    | Status                |
| --------------- | -------- | ------ | --------------------- |
| Dutch (default) | *(none)* | `/`    | Complete              |
| English         | `.en.md` | `/en/` | Core pages translated |

Missing translations automatically fall back to the Dutch version.

### Build per Language

```bash
# HTML site (all languages)
mkdocs build --strict

# PDF per language
MKDOCS_LANG=nl MKDOCS_EXPORTER_PDF=true MKDOCS_PDF_OUTPUT=pdf/ai-project-blauwdruk.nl.pdf mkdocs build --no-directory-urls
MKDOCS_LANG=en MKDOCS_EXPORTER_PDF=true MKDOCS_PDF_OUTPUT=pdf/ai-project-blauwdruk.en.pdf mkdocs build --no-directory-urls
```

## Development Workflow

### Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install
```

This enables automatic quality checks on every commit:

- Markdown formatting (mdformat)
- Trailing whitespace removal
- YAML/TOML/JSON syntax validation
- Python linting and formatting (ruff) — covers both `mcp_server/` and `scripts/`
- Documentation quality validation (terminology, CTA blocks, frontmatter, Collaboration Modes in gates)
- MCP server tests (487 tests, runs automatically on Python changes in `mcp_server/`)

### Manual Quality Check

```bash
python3 scripts/validate_docs.py
```

The validation script (v2.3) checks for:

- Terminology compliance per the Style Guide
- CTA blocks in Layer 2 modules
- Collaboration Mode field in Gate Review checklists
- Lifecycle redundancy (Single Source of Truth)
- Frontmatter with required `versie` field
- Translation coverage (NL > EN)
- Heading hierarchy and debug markers

## Contributing

This project is maintained according to the Style Guide v2.3 (`internal-meta/STYLE_GUIDE.md`). See `internal-meta/BACKLOG.md` for the current roadmap.

**Before submitting a PR:**

1. Run `pre-commit run --all-files`
1. Verify `mkdocs build --strict` passes
1. Confirm `python3 scripts/validate_docs.py` reports no errors

## License

(c) 2026 AI Project Blueprint.
Licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.
