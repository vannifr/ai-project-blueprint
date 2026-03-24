---
versie: '1.0'
type: index
layer: 3
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

### What does the MCP server do?

Once added, your AI assistant can:

- Search the Blueprint documentation for relevant sections
- Retrieve templates and checklists
- Provide context for phase-specific questions

**Example prompt for Claude:**

> *"Use the Blueprint MCP server and find the Gate 3 checklist for my project."*

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
