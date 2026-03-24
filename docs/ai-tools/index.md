---
versie: "1.0"
---

# AI-Assistent & MCP

De Blauwdruk biedt twee manieren om AI in te zetten bij het werken met de documentatie: een **ingebouwde chatbot** op de website en een **MCP-server** voor directe integratie met AI-assistenten zoals Claude.

!!! tip "Zoekbalk vs. chatbot"
    De **zoekbalk** (rechtsboven) zoekt op trefwoorden en geeft een lijst pagina's terug.
    De **chatbot** (rechtsonder) begrijpt je vraag en formuleert een antwoord — inclusief bronnen.
    Gebruik de zoekbalk als je weet wat je zoekt; gebruik de chatbot als je een vraag hebt.

---

## Blauwdruk Assistent (chatbot)

De chatbot staat rechtsonder op elke pagina. Klik op het praatballon-icoon om hem te openen.

### Wat kun je vragen?

De assistent doorzoekt de volledige Blauwdruk-documentatie en beantwoordt vragen over:

- Fasen, activiteiten en opleveringen
- Templates en checklists
- Governance, rollen en besluitvorming
- EU AI Act en compliance-eisen
- Methodes, patronen en antipatronen

**Voorbeeldvragen:**

- *"Wat zijn de verplichte opleveringen in Gate 2?"*
- *"Hoe classificeer ik het risico van mijn AI-systeem?"*
- *"Welke stappen horen bij de Fast Lane?"*
- *"Wat eist de EU AI Act voor high-risk systemen?"*

### Taal

De assistent detecteert automatisch of je Nederlands of Engels schrijft en antwoordt in dezelfde taal.

### Beperkingen

!!! info "Gericht op de Blauwdruk"
    De chatbot beantwoordt uitsluitend vragen over de inhoud van de Blauwdruk-documentatie. Algemene AI-vragen of projectspecifieke details (uit jouw eigen context) vallen buiten zijn kennisbasis.

- Maximaal 30 vragen per minuut per gebruiker
- Antwoorden zijn altijd gebaseerd op de gepubliceerde documentatie

---

## MCP-server (voor Claude en AI-editors)

De Blauwdruk biedt een **MCP-server** (Model Context Protocol) waarmee AI-assistenten zoals Claude direct toegang krijgen tot de documentatie als kennisbron.

**Endpoint:** `https://ai-delivery.io/mcp`
**Transport:** streamable-http

### Gebruik in Claude Desktop

Voeg het volgende toe aan je Claude Desktop-configuratie (`claude_desktop_config.json`):

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

Bestandslocatie per platform:

| Platform | Pad |
| -------- | --- |
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

### Gebruik in Cursor of andere MCP-clients

Voeg de server toe als HTTP MCP-server met URL `https://ai-delivery.io/mcp`.

### Gebruik in Claude Code (CLI)

```bash
claude mcp add blueprint --transport http https://ai-delivery.io/mcp
```

Verifieer de verbinding:

```bash
claude mcp list
```

### Wat doet de MCP-server?

Na het toevoegen kan je AI-assistent:

- De Blauwdruk-documentatie doorzoeken op relevante secties
- Templates en checklists ophalen
- Context geven bij fase-specifieke vragen

**Voorbeeldprompt voor Claude:**

> *"Gebruik de Blueprint MCP-server en zoek de Gate 3 checklist op voor mijn project."*

---

## Technische details

| Component | Details |
| --------- | ------- |
| Chatbot API | `https://ai-delivery.io/api/` |
| MCP-server | `https://ai-delivery.io/mcp` |
| Embeddings | `all-MiniLM-L6-v2` (lokaal, ONNX) |
| Generatie | Ollama Cloud (`gemma3:12b-cloud`) |
| Vectordatabase | ChromaDB |
| Index | 924 NL-chunks + 920 EN-chunks |
