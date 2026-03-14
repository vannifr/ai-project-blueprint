"""Blueprint MCP Server — exposes AI Project Blueprint as callable tools.

Tools:
    - get_phase_guidance: Phase objectives, activities, deliverables
    - get_template: Retrieve a template by name
    - check_gate_readiness: Compare evidence against gate checklist
    - classify_risk: Return risk classification framework
    - select_collaboration_mode: HAS-H collaboration mode selection
    - lookup_terminology: Search the glossary
    - get_project_type: Type A vs Type B classification
    - search_content: Full-text search with frontmatter filters

Resources:
    - blueprint://module/{path}: Full content of a specific module
    - blueprint://phase/{id}/overview: Phase overview
    - blueprint://glossary: Full glossary
"""

import os
from contextlib import asynccontextmanager
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from blueprint_mcp.content_index import ContentIndex

DOCS_ROOT = Path(os.environ.get(
    "BLUEPRINT_DOCS_PATH",
    Path(__file__).resolve().parent.parent.parent.parent / "docs",
))
LANGUAGE = os.environ.get("BLUEPRINT_LANGUAGE", "en")

# Module-level index for direct function calls (tests, scripts).
# When running as MCP server, the lifespan-loaded index is used instead.
_module_index: ContentIndex | None = None


def get_index(ctx=None) -> ContentIndex:
    """Extract ContentIndex from MCP context or fall back to module-level index."""
    if ctx is not None:
        try:
            return ctx.request_context.lifespan_context["index"]
        except (AttributeError, KeyError, TypeError):
            pass
    global _module_index
    if _module_index is None:
        _module_index = ContentIndex.load(DOCS_ROOT, language=LANGUAGE)
    return _module_index


def set_index(index: ContentIndex) -> None:
    """Set module-level index (for testing)."""
    global _module_index
    _module_index = index


@asynccontextmanager
async def lifespan(server: FastMCP):
    """Load content index at startup."""
    index = ContentIndex.load(DOCS_ROOT, language=LANGUAGE)
    yield {"index": index}


mcp = FastMCP(
    "AI Project Blueprint",
    instructions="Query AI Project Blueprint guidance, templates, and checklists",
    lifespan=lifespan,
)


def _format_doc_summary(doc) -> str:
    """Format a document as a brief summary line."""
    phases = ", ".join(str(p) for p in doc.phases)
    return f"- **{doc.title}** (`{doc.path}`) [type={doc.type}, layer={doc.layer}, phase={phases}]"


def _format_doc_full(doc) -> str:
    """Format a document with full content."""
    return f"# {doc.title}\n\n_Source: `{doc.path}`_\n\n{doc.body}"


# ─── Tools ────────────────────────────────────────────────────────────────────


@mcp.tool()
def get_phase_guidance(phase: int, aspect: str) -> str:
    """Get phase guidance from the AI Project Blueprint lifecycle.

    Args:
        phase: Phase number (1=Discovery, 2=Validation, 3=Development, 4=Delivery, 5=Monitoring)
        aspect: One of "objectives", "activities", or "deliverables"
    """
    if phase not in range(1, 6):
        return f"Error: phase must be 1-5, got {phase}"
    if aspect not in ("objectives", "activities", "deliverables"):
        return f"Error: aspect must be 'objectives', 'activities', or 'deliverables'"

    index = get_index()
    docs = index.get_phase_docs(phase, aspect)
    if not docs:
        return f"No {aspect} found for phase {phase}."

    return "\n\n---\n\n".join(_format_doc_full(d) for d in docs)


@mcp.tool()
def get_template(name: str) -> str:
    """Retrieve a Blueprint template by name.

    Args:
        name: Template name or keyword (e.g. "project-charter", "risk-pre-scan",
              "gate-review", "privacy", "modelkaart", "validatierapport")
    """
    index = get_index()
    templates = index.get_templates()

    name_lower = name.lower()

    # Exact path match first
    for doc in templates:
        if name_lower in doc.path.lower():
            return _format_doc_full(doc)

    # Fuzzy: search title and body
    for doc in templates:
        if name_lower in doc.title.lower() or name_lower in doc.body[:500].lower():
            return _format_doc_full(doc)

    # Fallback: list available templates
    names = "\n".join(f"- `{d.path}`: {d.title}" for d in templates)
    return f"Template '{name}' not found. Available templates:\n\n{names}"


@mcp.tool()
def check_gate_readiness(gate: int, evidence: list[str]) -> str:
    """Check readiness for a Gate Review by comparing evidence against the checklist.

    Args:
        gate: Gate number (1-5)
        evidence: List of evidence items you have (e.g. ["project charter", "risk scan", "golden set results"])
    """
    if gate not in range(1, 6):
        return f"Error: gate must be 1-5, got {gate}"

    index = get_index()

    # Find gate review checklist
    checklist_docs = [
        d for d in index.docs
        if "gate" in d.path.lower() and ("checklist" in d.path.lower() or "gate-review" in d.path.lower())
    ]
    if not checklist_docs:
        return "Gate review checklist not found in the index."

    checklist_content = checklist_docs[0].body

    evidence_str = "\n".join(f"- {e}" for e in evidence)

    return (
        f"## Gate {gate} Readiness Check\n\n"
        f"### Evidence provided:\n{evidence_str}\n\n"
        f"### Gate Review Checklist:\n\n{checklist_content}\n\n"
        f"---\n\n"
        f"Compare your evidence against the checklist above. "
        f"Items not covered by your evidence may need attention before the Gate {gate} review."
    )


@mcp.tool()
def classify_risk(system_description: str) -> str:
    """Get the risk classification framework for an AI system.

    Provides the Blueprint's risk classification content and EU AI Act categories.
    The calling LLM can then reason about the classification for the given system.

    Args:
        system_description: Free-text description of the AI system to classify
    """
    index = get_index()

    sections = []

    # Risk classification framework
    risk_docs = [d for d in index.docs if "risicoclassificatie" in d.path]
    if risk_docs:
        sections.append(_format_doc_full(risk_docs[0]))

    # EU AI Act overview
    euaiact_docs = [
        d for d in index.docs
        if "eu-ai-act" in d.path and d.type in ("compliance", "index")
    ]
    if euaiact_docs:
        sections.append(_format_doc_full(euaiact_docs[0]))

    if not sections:
        return "Risk classification documents not found."

    return (
        f"## System to classify:\n\n{system_description}\n\n---\n\n"
        + "\n\n---\n\n".join(sections)
        + "\n\n---\n\nUse the frameworks above to classify the risk level of the described system."
    )


@mcp.tool()
def select_collaboration_mode(risk_level: str, autonomy_needed: str) -> str:
    """Get guidance on selecting the right Human-AI collaboration mode (HAS-H levels).

    Args:
        risk_level: Risk level of the use case ("low", "medium", or "high")
        autonomy_needed: Desired level of AI autonomy ("low", "medium", or "high")
    """
    index = get_index()

    # Find HAS-H levels document
    docs = [d for d in index.docs if "has-h" in d.path.lower()]
    if not docs:
        return "Collaboration modes (HAS-H) document not found."

    return (
        f"## Collaboration Mode Selection\n\n"
        f"**Risk level:** {risk_level}\n"
        f"**Desired autonomy:** {autonomy_needed}\n\n---\n\n"
        + _format_doc_full(docs[0])
        + "\n\n---\n\nUse the framework above to select the appropriate collaboration mode."
    )


@mcp.tool()
def lookup_terminology(term: str) -> str:
    """Look up a term in the Blueprint glossary.

    Args:
        term: The term to look up (e.g. "guardian", "gate review", "golden set")
    """
    index = get_index()

    glossary_docs = [d for d in index.docs if d.path.startswith("termenlijst/")]
    if not glossary_docs:
        return "Glossary not found."

    term_lower = term.lower()
    glossary = glossary_docs[0]

    # Try to find the specific term in the glossary body
    lines = glossary.body.splitlines()
    results = []

    for i, line in enumerate(lines):
        if term_lower in line.lower():
            start = max(0, i - 1)
            end = min(len(lines), i + 8)
            snippet = "\n".join(lines[start:end])
            results.append(snippet)
            if len(results) >= 3:
                break

    if results:
        return f"## Glossary results for '{term}':\n\n" + "\n\n---\n\n".join(results)

    if len(glossary.body) > 5000:
        return f"Term '{term}' not found in glossary headings. Full glossary:\n\n{glossary.body[:5000]}..."
    return f"Term '{term}' not found in glossary headings. Full glossary:\n\n{glossary.body}"


@mcp.tool()
def reload_content() -> str:
    """Reload all Blueprint content from disk.

    Use this after updating markdown files in docs/ to refresh the index
    without restarting the server.
    """
    global _module_index
    _module_index = ContentIndex.load(DOCS_ROOT, language=LANGUAGE)
    return f"Reloaded {len(_module_index.docs)} documents."


@mcp.tool()
def get_project_type(description: str) -> str:
    """Get the Type A vs Type B project classification framework.

    Type A = deterministic AI (rules, classification). Type B = generative AI (LLMs, content creation).
    Returns the framework so the LLM can classify the described project.

    Args:
        description: Brief description of the AI project
    """
    index = get_index()

    docs = index.get_phase_docs(1, "activities")
    if not docs:
        docs = [d for d in index.docs if "activiteiten" in d.path and "02-fase-ontdekking" in d.path]

    if not docs:
        return "Project type classification document not found."

    return (
        f"## Project to classify:\n\n{description}\n\n---\n\n"
        + _format_doc_full(docs[0])
        + "\n\n---\n\nUse the Type A / Type B framework above to classify this project."
    )


@mcp.tool()
def search_content(
    query: str,
    type: str | None = None,
    phase: int | None = None,
    layer: int | None = None,
    tag: str | None = None,
) -> str:
    """Search across all Blueprint documentation.

    Args:
        query: Keyword(s) to search for
        type: Filter by document type (e.g. "template", "guide", "objectives", "activities", "deliverables", "compliance")
        phase: Filter by lifecycle phase (1-5)
        layer: Filter by layer (1=Strategic, 2=Operational, 3=Toolkit)
        tag: Filter by tag (e.g. "risk", "gate-review", "onboarding", "rag", "monitoring")
    """
    index = get_index()
    results = index.search(query, type=type, phase=phase, layer=layer, tag=tag)

    if not results:
        return f"No results found for '{query}' with the given filters."

    lines = [f"## Search results for '{query}' ({len(results)} found)\n"]
    for doc in results:
        body_preview = doc.body[:200].replace("\n", " ").strip()
        lines.append(_format_doc_summary(doc))
        lines.append(f"  {body_preview}...\n")

    return "\n".join(lines)


# ─── Resources ────────────────────────────────────────────────────────────────


@mcp.resource("blueprint://module/{path}")
def get_module(path: str) -> str:
    """Get the full content of a Blueprint module by its path."""
    index = get_index()
    doc = index.by_path.get(path)
    if not doc:
        matches = [d for d in index.docs if path in d.path]
        if matches:
            doc = matches[0]
    if not doc:
        return f"Module '{path}' not found."
    return _format_doc_full(doc)


@mcp.resource("blueprint://phase/{phase_id}/overview")
def get_phase_overview(phase_id: str) -> str:
    """Get a complete overview of a lifecycle phase (objectives + activities + deliverables)."""
    try:
        phase = int(phase_id)
    except ValueError:
        return f"Invalid phase ID: {phase_id}"

    index = get_index()
    sections = []
    for aspect in ("objectives", "activities", "deliverables"):
        docs = index.get_phase_docs(phase, aspect)
        for doc in docs:
            sections.append(_format_doc_full(doc))

    if not sections:
        return f"No documents found for phase {phase}."

    phase_names = {1: "Discovery", 2: "Validation", 3: "Development", 4: "Delivery", 5: "Monitoring"}
    name = phase_names.get(phase, f"Phase {phase}")
    return f"# Phase {phase}: {name} — Complete Overview\n\n" + "\n\n---\n\n".join(sections)


@mcp.resource("blueprint://glossary")
def get_glossary() -> str:
    """Get the complete Blueprint glossary."""
    index = get_index()
    glossary_docs = [d for d in index.docs if d.path.startswith("termenlijst/")]
    if not glossary_docs:
        return "Glossary not found."
    return _format_doc_full(glossary_docs[0])


# ─── Entrypoint ───────────────────────────────────────────────────────────────


def main():
    """Run the Blueprint MCP server.

    Transport is selected via BLUEPRINT_TRANSPORT env var:
        - stdio (default): for Claude Desktop / Claude Code
        - streamable-http: for web hosting (runs on host:port)
    """
    transport = os.environ.get("BLUEPRINT_TRANSPORT", "stdio")
    if transport == "streamable-http":
        mcp.settings.host = os.environ.get("BLUEPRINT_HOST", "0.0.0.0")
        mcp.settings.port = int(os.environ.get("BLUEPRINT_PORT", "8080"))
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()
