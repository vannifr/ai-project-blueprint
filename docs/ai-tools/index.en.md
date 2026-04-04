---
versie: '1.0'
type: index
layer: 3
answers:
  - What is assistant mcp?
  - How does assistant mcp work?
  - When should I use assistant mcp?
---

# AI Assistant & MCP

The Blueprint offers two ways to use AI when working with the documentation: a **built-in chatbot** on the website and an **MCP server** for direct integration with AI assistants like Claude.

!!! tip "Search bar vs. chatbot"
    The **search bar** (top right) searches by keyword and returns a list of pages.
    The **chatbot** (bottom right) understands your question and formulates an answer — including sources.
    Use the search bar when you know what you're looking for; use the chatbot when you have a question.

______________________________________________________________________

## Blueprint Assistant (chatbot)

The chatbot is available in the bottom-right corner of every page. Click the speech bubble icon to open it.

### What can you ask?

The assistant searches the full Blueprint documentation and answers questions about:

- Phases, activities and deliverables
- Templates and checklists
- Governance, roles and decision-making
- EU AI Act and compliance requirements
- Methods, patterns and anti-patterns

**Example questions:**

- *"What are the required deliverables at Gate 2?"*
- *"How do I classify the risk level of my AI system?"*
- *"Which steps belong to the Fast Lane?"*
- *"What does the EU AI Act require for high-risk systems?"*

### Language

The assistant automatically detects whether you write in Dutch or English and responds in the same language.

### Limitations

!!! info "Focused on the Blueprint"
    The chatbot only answers questions about the Blueprint documentation. General AI questions or project-specific details from your own context are outside its knowledge base.

- Maximum 30 questions per minute per user
- Answers are always based on the published documentation

______________________________________________________________________

## MCP Server (for Claude and AI editors)

The Blueprint provides an **MCP server** (Model Context Protocol) that gives AI assistants like Claude direct access to the documentation as a knowledge source.

**Endpoint:** `https://ai-delivery.io/mcp`
**Transport:** streamable-http

### Use in Claude Desktop

Add the following to your Claude Desktop configuration (`claude_desktop_config.json`):

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

File location per platform:

| Platform | Path                                                              |
| -------- | ----------------------------------------------------------------- |
| macOS    | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows  | `%APPDATA%\Claude\claude_desktop_config.json`                     |
| Linux    | `~/.config/Claude/claude_desktop_config.json`                     |

### Use in Cursor or other MCP clients

Add the server as an HTTP MCP server with URL `https://ai-delivery.io/mcp`.

### Use in Claude Code (CLI)

```bash
claude mcp add blueprint --transport http https://ai-delivery.io/mcp
```

Verify the connection:

```bash
claude mcp list
```

### Agent workflows

The MCP server offers guided multi-step workflows in addition to standalone lookup tools. The AI assistant orchestrates the steps and asks you for input between them.

| Workflow             | How to trigger                                  | What you get                                                         |
| -------------------- | ----------------------------------------------- | -------------------------------------------------------------------- |
| **Project Setup**    | *"Help me set up a new AI project"*             | Type A/B classification → risk pre-scan → pre-filled Project Charter |
| **Gate Review**      | *"Help me prepare for Gate 2"*                  | Evidence gap check → Guardian-ready Go/No-Go summary                 |
| **Template Advisor** | *"Which templates do I need as PM in phase 3?"* | Recommended templates with context pre-filled                        |
| **Compliance**       | *"Is my system compliant with the EU AI Act?"*  | Risk category classification → article-referenced checklist          |

### Standalone tools

The server also exposes individual tools for direct lookups:

- Search documentation for relevant sections
- Retrieve templates and checklists by name
- Look up terminology, phase guidance, and risk frameworks

**Example prompts for Claude:**

> *"Use the Blueprint MCP server and help me set up my fraud detection project."*

> *"Find the Gate 3 checklist for my project using the Blueprint."*

> *"Check if my AI hiring system is EU AI Act compliant."*

______________________________________________________________________

## Technical details

| Component       | Details                           |
| --------------- | --------------------------------- |
| Chatbot API     | `https://ai-delivery.io/api/`     |
| MCP server      | `https://ai-delivery.io/mcp`      |
| Embeddings      | `all-MiniLM-L6-v2` (local, ONNX)  |
| Generation      | Ollama Cloud (`gemma3:12b-cloud`) |
| Vector database | ChromaDB                          |
| Index           | 924 NL chunks + 920 EN chunks     |
