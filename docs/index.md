---
versie: '1.0'
description: 'AI Project Blauwdruk — een modulair open raamwerk voor AI-projectmanagement: strategie, governance, compliance en oplevering. Gebaseerd op PMI-CPMAI en Agile-AI principes.'
type: index
layer: 1
answers: [Wat bevat het onderdeel Welkom bij de AI Project Blauwdruk?]
---

# 1. Welkom bij de AI Project Blauwdruk

!!! abstract "Wat is dit?"
    De AI Project Blauwdruk is een **modulair raamwerk** voor het opzetten, uitvoeren en beheren van AI-projecten. Het biedt antwoord op vragen als:

    - **Hoe manage ik een AI-project van idee tot productie?** — Een complete projectcyclus met gates, sjablonen en bewijsstandaarden.
    - **Hoe bouw ik verantwoord AI-gedreven software?** — Principes voor specificatie-eerst ontwikkeling, harde grenzen en continue validatie.
    - **Hoe onderbouw ik een AI business case?** — Van validatiepilot tot waarderealisatie, met meetbare criteria per fase.
    - **Hoe organiseer ik governance en compliance?** — Rollen, verantwoordelijkheden, EU AI Act compliance en risicoclassificatie.
    - **Hoe werk ik met agentic AI systemen?** — Orchestratiepatronen, samenwerkingsmodi en veiligheidskaders voor autonome AI.

    Het raamwerk is geschikt voor zowel teams die **bouwen met AI** (AI ondersteunt het ontwikkelproces) als teams die **AI in het product** integreren.

## 1. Uw Blauwdruk voor AI-Projectmanagement

Dit is de centrale documentatiehub voor het succesvol managen van AI-projecten, gebaseerd op de **Kernprincipes** van gedragssturing, traceerbaarheid en menselijke regie.

______________________________________________________________________

## 2. Snel Starten

- 🧭 **[Blueprint Navigator](00-navigator/index.md):** Interactieve wizard — vindt uw startpunt in 5 minuten.
- 🚀 **[Verkenner Kit (30 Dagen)](00-explorer-kit/index.md):** Eerste AI-prototype in 30 dagen — templates en dag-tot-dag plan.
- 📖 **[Leeswijzer & Navigatie](00-strategisch-kader/00-leeswijzer.md):** Hoe u deze blauwdruk het meest effectief gebruikt.
- 👥 **[Rollen & Verantwoordelijkheden](08-rollen-en-verantwoordelijkheden/index.md):** Wie doet wat in een AI-team?
- 📅 **[Snelstart: AI-Project in 90 Dagen](12-90-dagen-roadmap/index.md):** Ga direct van strategie naar actie.
- 🧰 **[De toolkit](09-sjablonen/index.md):** Alle sjablonen op één plek.
- 📄 **<a href="pdf/ai-project-blueprint.pdf">Download volledige blauwdruk (PDF, Engels)</a>:** De complete AI Project Blueprint als één PDF-bestand.

______________________________________________________________________

## 3. Documentatie Overzicht

### Strategisch Kader & Fundamenten

- [Strategisch Kader](00-strategisch-kader/01-ai-levenscyclus.md)
- [Kernprincipes](01-ai-native-fundamenten/01-definitie.md)
- [Risicobeheersing & Compliance](07-compliance-hub/index.md)
- [Rollen & Verantwoordelijkheden](08-rollen-en-verantwoordelijkheden/index.md)

### De AI Levenscyclus (Fase Modules)

1. **[Verkenning & Strategie](02-fase-ontdekking/01-doelstellingen.md):** Het probleem doorgronden.
1. **[Validatie](03-fase-validatie/01-doelstellingen.md):** Bewijzen dat het werkt (**Validatiepilot**).
1. **[Realisatie](04-fase-ontwikkeling/01-doelstellingen.md):** De oplossing bouwen (**Specificatie-eerst**).
1. **[Levering](05-fase-levering/01-doelstellingen.md):** Veilige **Ingebruikname**.
1. **[Beheer & Optimalisatie](06-fase-monitoring/01-doelstellingen.md):** Waarde behouden (**Drift**).

______________________________________________________________________

## 4. Voor AI-Agenten & LLM-Verwerking

### Blueprint Assistent

De live site bevat een **Blueprint Assistent** — een chatwidget die vragen over de blauwdruk beantwoordt in het Nederlands en Engels, rechtstreeks vanuit de documentatie (RAG + LLM).

### MCP Server

De blauwdruk is volledig beschikbaar als **MCP-server** met 31 tools voor AI-agenten en Claude Code:

```bash
claude mcp add blueprint --transport http https://ai-delivery.io/mcp
```

Beschikbare workflows via MCP: Project Setup, Gate Review, Compliance, Template Advisor, sessieregistratie en semantisch zoeken. Gebruik `get_tool_cheatsheet()` voor een volledig overzicht.

### LLM-tekstexports

| Formaat                 | Link                                 | Gebruik                                                                                        |
| :---------------------- | :----------------------------------- | :--------------------------------------------------------------------------------------------- |
| **Index** (`llms.txt`)  | [llms.txt](llms.txt)                 | Compacte linkindex — compatibel met Cursor, Perplexity en andere llmstxt-tools                 |
| **Volledige inhoud EN** | [llms-full.txt](llms-full.txt)       | Alle 130 pagina's samengevoegd, HTML/emoji verwijderd, typografische tekens omgezet naar ASCII |
| **Volledige inhoud NL** | [llms-full-nl.txt](llms-full-nl.txt) | Idem in het Nederlands                                                                         |

De volledige exports worden bij elke push opnieuw gegenereerd en volgen de [llmstxt.org](https://llmstxt.org) conventie.

______________________________________________________________________

## 5. Over deze Blauwdruk

De AI Project Blauwdruk is een modulaire, toetsbare werkwijze voor het opzetten, uitvoeren en beheren van AI‑projecten. De blauwdruk beschrijft de volledige projectcyclus — van strategische verkenning tot operationeel beheer — en biedt concrete sjablonen, checklists en bewijsstandaarden waarmee organisaties AI‑systemen controleerbaar, traceerbaar en verantwoord kunnen inzetten.

Meer informatie: **[Over de AI Project Blauwdruk](over.md)** | **[Versiegeschiedenis](release-notes.md)**

**Praktijkvoorbeelden:** Bekijk hoe de blauwdruk in de praktijk wordt toegepast in de **[Praktijkvoorbeelden](17-bijlagen/praktijkvoorbeelden.md)**.

**Auteurs:** Frederik Vannieuwenhuyse, Hadrien-Joseph van Durme

______________________________________________________________________

!!! warning "Disclaimer"
    Alle informatie in deze blauwdruk is louter informatief en bedoeld als referentiekader. De auteurs nemen geen verantwoordelijkheid voor het resultaat van AI-projecten die op basis van dit materiaal worden uitgevoerd. Raadpleeg altijd domeinexperts voor juridische, technische en organisatorische beslissingen.
