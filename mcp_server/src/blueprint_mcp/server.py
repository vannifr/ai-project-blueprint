"""Blueprint MCP Server — exposes AI Project Blueprint as callable tools.

Tools:
    - answer_question: Find relevant pages for a natural language question
    - get_template_for_context: Get templates for a role + phase combination
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

from blueprint_mcp.confidence import score_result
from blueprint_mcp.content_index import ContentIndex
from blueprint_mcp.escalation import EscalationRegistry, EventType
from blueprint_mcp.evidence import evidence_summary, parse_evidence
from blueprint_mcp.glossary import GlossaryIndex
from blueprint_mcp.response_utils import DecisionStatus, build_decision, format_response
from blueprint_mcp.semantic_search import SemanticIndex
from blueprint_mcp.session_store import SessionStore
from blueprint_mcp.template_engine import fill_placeholders, parse_placeholders

DOCS_ROOT = Path(
    os.environ.get(
        "BLUEPRINT_DOCS_PATH",
        Path(__file__).resolve().parent.parent.parent.parent / "docs",
    )
)
LANGUAGE = os.environ.get("BLUEPRINT_LANGUAGE", "en")
CHROMA_PATH = os.environ.get(
    "BLUEPRINT_CHROMA_PATH",
    str(Path(__file__).resolve().parent.parent.parent.parent / "chatbot" / "chroma_data"),
)

# Module-level index for direct function calls (tests, scripts).
# When running as MCP server, the lifespan-loaded index is used instead.
_module_index: ContentIndex | None = None
_module_semantic_index: SemanticIndex | None = None
_module_glossary_index: GlossaryIndex | None = None
_module_session_store: SessionStore | None = None
_module_escalation_registry: EscalationRegistry = EscalationRegistry()


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


def get_semantic_index(ctx=None) -> SemanticIndex | None:
    """Return the semantic index if available, else None."""
    if ctx is not None:
        try:
            return ctx.request_context.lifespan_context.get("semantic_index")
        except (AttributeError, KeyError, TypeError):
            pass
    return _module_semantic_index


def set_semantic_index(index: SemanticIndex | None) -> None:
    """Set module-level semantic index (for testing)."""
    global _module_semantic_index
    _module_semantic_index = index


def get_glossary_index() -> GlossaryIndex | None:
    """Return the glossary index if available, else None."""
    return _module_glossary_index


def set_glossary_index(index: GlossaryIndex | None) -> None:
    """Set module-level glossary index (for testing)."""
    global _module_glossary_index
    _module_glossary_index = index


def get_session_store() -> SessionStore | None:
    """Return the session store if available, else None."""
    return _module_session_store


def set_session_store(store: SessionStore | None) -> None:
    """Set module-level session store (for testing)."""
    global _module_session_store
    _module_session_store = store


def get_escalation_registry() -> EscalationRegistry:
    """Return the module-level escalation registry."""
    return _module_escalation_registry


def register_escalation_hook(event_type: str, callback) -> None:
    """Register a callback for an escalation event type."""
    _module_escalation_registry.register(event_type, callback)


@asynccontextmanager
async def lifespan(server: FastMCP):
    """Load content index and semantic index at startup."""
    index = ContentIndex.load(DOCS_ROOT, language=LANGUAGE)
    try:
        sem_index: SemanticIndex | None = SemanticIndex(CHROMA_PATH, language=LANGUAGE)
        # Trigger a probe search to detect unavailable ChromaDB early
        sem_index.search("probe", n_results=1)
    except Exception:
        sem_index = None
    yield {"index": index, "semantic_index": sem_index}


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
def answer_question(question: str, output_format: str = "markdown") -> str:
    """Find the most relevant Blueprint page(s) for a user question.

    Searches across all document answers, summaries, and titles to find
    the best matches. Returns up to 3 results with summaries and full content
    of the top match.

    Args:
        question: Natural language question (e.g. "How do I classify the risk of my AI project?")
        output_format: Response format — "markdown" (default) or "json"

    Next step: use get_template to retrieve related templates, or get_phase_guidance for phase-specific activities.
    """
    index = get_index()

    # Semantic search (preferred) → keyword fallback
    sem_index = get_semantic_index()
    if sem_index is not None:
        sem_results = sem_index.search(question, n_results=3)
        # Map semantic hits to index documents (by path lookup)
        sem_docs = [index.by_path.get(r.doc_path) for r in sem_results]
        results = [d for d in sem_docs if d is not None]
    else:
        results = []

    if not results:
        results = index.search_by_question(question, limit=3)
    if not results:
        # Final keyword fallback
        results = index.search(question, limit=3)

    if not results:
        return format_response(
            f"No relevant pages found for: '{question}'",
            build_decision(
                "answer_question",
                DecisionStatus.NOT_FOUND,
                "Rephrase the question or use search_content with keywords.",
                {"result_count": 0, "top_match_path": None},
            ),
            output_format,
        )

    sections = []

    # Top result: full content
    top = results[0]
    summary_line = f"**Summary:** {top.summary}\n\n" if top.summary else ""
    answers_line = ""
    if top.answers:
        answers_line = (
            "**Questions this page answers:**\n" + "\n".join(f"- {a}" for a in top.answers) + "\n\n"
        )
    sections.append(
        f"## Best match: {top.title}\n\n"
        f"_Source: `{top.path}`_\n\n"
        f"{summary_line}{answers_line}"
        f"{top.body}"
    )

    # Additional results: summary only
    if len(results) > 1:
        lines = ["## Also relevant:\n"]
        for doc in results[1:]:
            s = f" — {doc.summary}" if doc.summary else ""
            lines.append(f"- **{doc.title}** (`{doc.path}`){s}")
        sections.append("\n".join(lines))

    markdown = "\n\n---\n\n".join(sections)

    # Glossary enrichment — append definitions for terms found in the answer
    glossary = get_glossary_index()
    if glossary is not None:
        markdown = glossary.enrich_answer(markdown)

    top_confidence = score_result(query=question, doc=top)
    return format_response(
        markdown,
        build_decision(
            "answer_question",
            DecisionStatus.OK,
            "Review the best match and additional results above.",
            {
                "result_count": len(results),
                "top_match_path": top.path,
                "top_confidence": top_confidence,
            },
        ),
        output_format,
    )


@mcp.tool()
def get_template_for_context(role: str, phase: int, output_format: str = "markdown") -> str:
    """Get recommended templates for a specific role and lifecycle phase.

    Args:
        role: Role name (e.g. "AI Product Manager", "Guardian", "Tech Lead")
        phase: Lifecycle phase number (1-5)
        output_format: Response format — "markdown" (default) or "json"
    """
    index = get_index()

    templates = [
        d
        for d in index.docs
        if d.type == "template" and phase in d.phases and (not d.roles or role in d.roles)
    ]

    if not templates:
        # Broader search: any template for this phase
        templates = [d for d in index.docs if d.type == "template" and phase in d.phases]

    if not templates:
        return format_response(
            f"No templates found for role '{role}' in phase {phase}.",
            build_decision(
                "get_template_for_context",
                DecisionStatus.NOT_FOUND,
                "Try a different phase or omit the role filter.",
                {"role": role, "phase": phase, "template_count": 0},
            ),
            output_format,
        )

    phase_names = {
        1: "Discovery",
        2: "Validation",
        3: "Development",
        4: "Delivery",
        5: "Monitoring",
    }
    lines = [f"## Templates for {role} in Phase {phase} ({phase_names.get(phase, '')})\n"]

    for doc in templates:
        s = f": {doc.summary}" if doc.summary else ""
        lines.append(f"- **{doc.title}** (`{doc.path}`){s}")

    return format_response(
        "\n".join(lines),
        build_decision(
            "get_template_for_context",
            DecisionStatus.OK,
            "Select a template and call get_template to retrieve full content.",
            {"role": role, "phase": phase, "template_count": len(templates)},
        ),
        output_format,
    )


@mcp.tool()
def get_phase_guidance(phase: int, aspect: str, output_format: str = "markdown") -> str:
    """Get phase guidance from the AI Project Blueprint lifecycle.

    Args:
        phase: Phase number (1=Discovery, 2=Validation, 3=Development, 4=Delivery, 5=Monitoring)
        aspect: One of "objectives", "activities", or "deliverables"
        output_format: Response format — "markdown" (default) or "json"

    Next step: call get_template or get_template_for_context to find relevant templates.
    """
    if phase not in range(1, 6):
        return format_response(
            f"Error: phase must be 1-5, got {phase}",
            build_decision(
                "get_phase_guidance",
                DecisionStatus.ERROR,
                "Correct the phase parameter (1–5).",
                {"phase": phase, "aspect": aspect},
            ),
            output_format,
        )
    if aspect not in ("objectives", "activities", "deliverables"):
        return format_response(
            "Error: aspect must be 'objectives', 'activities', or 'deliverables'",
            build_decision(
                "get_phase_guidance",
                DecisionStatus.ERROR,
                "Use one of: objectives, activities, deliverables.",
                {"phase": phase, "aspect": aspect},
            ),
            output_format,
        )

    index = get_index()
    docs = index.get_phase_docs(phase, aspect)
    if not docs:
        return format_response(
            f"No {aspect} found for phase {phase}.",
            build_decision(
                "get_phase_guidance",
                DecisionStatus.NOT_FOUND,
                "Try a different aspect or check that docs are loaded.",
                {"phase": phase, "aspect": aspect, "doc_count": 0},
            ),
            output_format,
        )

    markdown = "\n\n---\n\n".join(_format_doc_full(d) for d in docs)
    return format_response(
        markdown,
        build_decision(
            "get_phase_guidance",
            DecisionStatus.OK,
            "Review the phase guidance above.",
            {"phase": phase, "aspect": aspect, "doc_count": len(docs)},
        ),
        output_format,
    )


@mcp.tool()
def get_template(name: str, output_format: str = "markdown") -> str:
    """Retrieve a Blueprint template by name.

    Args:
        name: Template name or keyword (e.g. "project-charter", "risk-pre-scan",
              "gate-review", "privacy", "modelkaart", "validatierapport")
        output_format: Response format — "markdown" (default) or "json"

    Next step: call fill_template to populate placeholders with project-specific values.
    """
    index = get_index()
    templates = index.get_templates()

    name_lower = name.lower()

    # Exact path match first
    for doc in templates:
        if name_lower in doc.path.lower():
            return format_response(
                _format_doc_full(doc),
                build_decision(
                    "get_template",
                    DecisionStatus.OK,
                    "Fill in the [placeholder] fields in the template above.",
                    {"template_name": name, "matched_path": doc.path},
                ),
                output_format,
            )

    # Fuzzy: search title and body
    for doc in templates:
        if name_lower in doc.title.lower() or name_lower in doc.body[:500].lower():
            return format_response(
                _format_doc_full(doc),
                build_decision(
                    "get_template",
                    DecisionStatus.OK,
                    "Fill in the [placeholder] fields in the template above.",
                    {"template_name": name, "matched_path": doc.path},
                ),
                output_format,
            )

    # Fallback: list available templates
    names = "\n".join(f"- `{d.path}`: {d.title}" for d in templates)
    return format_response(
        f"Template '{name}' not found. Available templates:\n\n{names}",
        build_decision(
            "get_template",
            DecisionStatus.NOT_FOUND,
            "Choose a template name from the list above and retry.",
            {"template_name": name, "available_count": len(templates)},
        ),
        output_format,
    )


@mcp.tool()
def check_gate_readiness(gate: int, evidence: list[str], output_format: str = "markdown") -> str:
    """Check readiness for a Gate Review by comparing evidence against the checklist.

    Args:
        gate: Gate number (1-5)
        evidence: List of evidence items you have (e.g. ["project charter", "risk scan", "golden set results"])
        output_format: Response format — "markdown" (default) or "json"

    Next step: call gate_review_intake to formally collect evidence, or get_phase_guidance if all gates are passed.
    """
    if gate not in range(1, 6):
        return format_response(
            f"Error: gate must be 1-5, got {gate}",
            build_decision(
                "check_gate_readiness",
                DecisionStatus.ERROR,
                "Correct the gate parameter (1–5).",
                {"gate": gate},
            ),
            output_format,
        )

    index = get_index()

    # Find gate review checklist
    checklist_docs = [
        d
        for d in index.docs
        if "gate" in d.path.lower()
        and ("checklist" in d.path.lower() or "gate-review" in d.path.lower())
    ]
    if not checklist_docs:
        return format_response(
            "Gate review checklist not found in the index.",
            build_decision(
                "check_gate_readiness",
                DecisionStatus.NOT_FOUND,
                "Reload the content index and retry.",
                {"gate": gate},
            ),
            output_format,
        )

    checklist_content = checklist_docs[0].body

    evidence_str = "\n".join(f"- {e}" for e in evidence)

    markdown = (
        f"## Gate {gate} Readiness Check\n\n"
        f"### Evidence provided:\n{evidence_str}\n\n"
        f"### Gate Review Checklist:\n\n{checklist_content}\n\n"
        f"---\n\n"
        f"Compare your evidence against the checklist above. "
        f"Items not covered by your evidence may need attention before the Gate {gate} review."
    )
    return format_response(
        markdown,
        build_decision(
            "check_gate_readiness",
            DecisionStatus.OK,
            "Compare evidence against the checklist and identify gaps.",
            {"gate": gate, "evidence_count": len(evidence)},
        ),
        output_format,
    )


@mcp.tool()
def classify_risk(system_description: str, output_format: str = "markdown") -> str:
    """Get the risk classification framework for an AI system.

    Provides the Blueprint's risk classification content and EU AI Act categories.
    The calling LLM can then reason about the classification for the given system.

    Args:
        system_description: Free-text description of the AI system to classify
        output_format: Response format — "markdown" (default) or "json"

    Next step: call compliance_checklist for a full compliance check, or get_guidance_for_profile for tailored guidance.
    """
    index = get_index()

    sections = []

    # Risk classification framework
    risk_docs = [d for d in index.docs if "risicoclassificatie" in d.path]
    if risk_docs:
        sections.append(_format_doc_full(risk_docs[0]))

    # EU AI Act overview
    euaiact_docs = [
        d for d in index.docs if "eu-ai-act" in d.path and d.type in ("compliance", "index")
    ]
    if euaiact_docs:
        sections.append(_format_doc_full(euaiact_docs[0]))

    if not sections:
        return format_response(
            "Risk classification documents not found.",
            build_decision(
                "classify_risk",
                DecisionStatus.NOT_FOUND,
                "Reload the content index and retry.",
                {"description_excerpt": system_description[:100]},
            ),
            output_format,
        )

    markdown = (
        f"## System to classify:\n\n{system_description}\n\n---\n\n"
        + "\n\n---\n\n".join(sections)
        + "\n\n---\n\nUse the frameworks above to classify the risk level of the described system."
    )
    return format_response(
        markdown,
        build_decision(
            "classify_risk",
            DecisionStatus.OK,
            "Apply the framework above to classify the system, then call project_setup_risk.",
            {"description_excerpt": system_description[:100]},
            next_tool="project_setup_risk",
        ),
        output_format,
    )


@mcp.tool()
def select_collaboration_mode(
    risk_level: str, autonomy_needed: str, output_format: str = "markdown"
) -> str:
    """Get guidance on selecting the right Human-AI collaboration mode (HAS-H levels).

    Args:
        risk_level: Risk level of the use case ("low", "medium", or "high")
        autonomy_needed: Desired level of AI autonomy ("low", "medium", or "high")
        output_format: Response format — "markdown" (default) or "json"

    Next step: call project_setup_charter or project_setup_risk with the selected mode.
    """
    index = get_index()

    # Find HAS-H levels document
    docs = [d for d in index.docs if "has-h" in d.path.lower()]
    if not docs:
        return format_response(
            "Collaboration modes (HAS-H) document not found.",
            build_decision(
                "select_collaboration_mode",
                DecisionStatus.NOT_FOUND,
                "Reload the content index and retry.",
                {"risk_level": risk_level, "autonomy_needed": autonomy_needed},
            ),
            output_format,
        )

    markdown = (
        f"## Collaboration Mode Selection\n\n"
        f"**Risk level:** {risk_level}\n"
        f"**Desired autonomy:** {autonomy_needed}\n\n---\n\n"
        + _format_doc_full(docs[0])
        + "\n\n---\n\nUse the framework above to select the appropriate collaboration mode."
    )
    return format_response(
        markdown,
        build_decision(
            "select_collaboration_mode",
            DecisionStatus.OK,
            "Select a mode number (1–5) based on the framework above.",
            {"risk_level": risk_level, "autonomy_needed": autonomy_needed},
        ),
        output_format,
    )


@mcp.tool()
def lookup_terminology(term: str, output_format: str = "markdown") -> str:
    """Look up a term in the Blueprint glossary.

    Args:
        term: The term to look up (e.g. "guardian", "gate review", "golden set")
        output_format: Response format — "markdown" (default) or "json"

    Next step: call answer_question for deeper context about the term.
    """
    index = get_index()

    glossary_docs = [d for d in index.docs if d.path.startswith("termenlijst/")]
    if not glossary_docs:
        return format_response(
            "Glossary not found.",
            build_decision(
                "lookup_terminology",
                DecisionStatus.NOT_FOUND,
                "Reload the content index and retry.",
                {"term": term, "found": False},
            ),
            output_format,
        )

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
        markdown = f"## Glossary results for '{term}':\n\n" + "\n\n---\n\n".join(results)
        return format_response(
            markdown,
            build_decision(
                "lookup_terminology",
                DecisionStatus.OK,
                "Review the glossary definition above.",
                {"term": term, "found": True, "snippet_count": len(results)},
            ),
            output_format,
        )

    if len(glossary.body) > 5000:
        markdown = f"Term '{term}' not found in glossary headings. Full glossary:\n\n{glossary.body[:5000]}..."
    else:
        markdown = (
            f"Term '{term}' not found in glossary headings. Full glossary:\n\n{glossary.body}"
        )
    return format_response(
        markdown,
        build_decision(
            "lookup_terminology",
            DecisionStatus.NOT_FOUND,
            "Try a different term or browse the full glossary.",
            {"term": term, "found": False},
        ),
        output_format,
    )


@mcp.tool()
def reload_content(output_format: str = "markdown") -> str:
    """Reload all Blueprint content from disk.

    Use this after updating markdown files in docs/ to refresh the index
    without restarting the server.

    Args:
        output_format: Response format — "markdown" (default) or "json"
    """
    global _module_index
    _module_index = ContentIndex.load(DOCS_ROOT, language=LANGUAGE)
    doc_count = len(_module_index.docs)
    return format_response(
        f"Reloaded {doc_count} documents.",
        build_decision(
            "reload_content",
            DecisionStatus.OK,
            "Content index refreshed. All tools now use the updated docs.",
            {"doc_count": doc_count},
        ),
        output_format,
    )


@mcp.tool()
def get_project_type(description: str, output_format: str = "markdown") -> str:
    """Get the Type A vs Type B project classification framework.

    Type A = deterministic AI (rules, classification). Type B = generative AI (LLMs, content creation).
    Returns the framework so the LLM can classify the described project.

    Args:
        description: Brief description of the AI project
        output_format: Response format — "markdown" (default) or "json"

    Next step: call classify_risk with the project description.
    """
    index = get_index()

    docs = index.get_phase_docs(1, "activities")
    if not docs:
        docs = [
            d for d in index.docs if "activiteiten" in d.path and "02-fase-ontdekking" in d.path
        ]

    if not docs:
        return format_response(
            "Project type classification document not found.",
            build_decision(
                "get_project_type",
                DecisionStatus.NOT_FOUND,
                "Reload the content index and retry.",
                {"description_excerpt": description[:100]},
            ),
            output_format,
        )

    markdown = (
        f"## Project to classify:\n\n{description}\n\n---\n\n"
        + _format_doc_full(docs[0])
        + "\n\n---\n\nUse the Type A / Type B framework above to classify this project."
    )
    return format_response(
        markdown,
        build_decision(
            "get_project_type",
            DecisionStatus.OK,
            "Classify as Type A or B, then call project_setup_intake.",
            {"description_excerpt": description[:100]},
            next_tool="project_setup_intake",
        ),
        output_format,
    )


@mcp.tool()
def search_content(
    query: str,
    type: str | None = None,
    phase: int | None = None,
    layer: int | None = None,
    tag: str | None = None,
    output_format: str = "markdown",
) -> str:
    """Search across all Blueprint documentation.

    Args:
        query: Keyword(s) to search for
        type: Filter by document type (e.g. "template", "guide", "objectives", "activities", "deliverables", "compliance")
        phase: Filter by lifecycle phase (1-5)
        layer: Filter by layer (1=Strategic, 2=Operational, 3=Toolkit)
        tag: Filter by tag (e.g. "risk", "gate-review", "onboarding", "rag", "monitoring")
        output_format: Response format — "markdown" (default) or "json"
    """
    index = get_index()
    results = index.search(query, type=type, phase=phase, layer=layer, tag=tag)

    if not results:
        return format_response(
            f"No results found for '{query}' with the given filters.",
            build_decision(
                "search_content",
                DecisionStatus.NOT_FOUND,
                "Try broader keywords or remove filters.",
                {"query": query, "result_count": 0},
            ),
            output_format,
        )

    lines = [f"## Search results for '{query}' ({len(results)} found)\n"]
    for doc in results:
        body_preview = doc.body[:200].replace("\n", " ").strip()
        lines.append(_format_doc_summary(doc))
        lines.append(f"  {body_preview}...\n")

    confidence_scores = [score_result(query=query, doc=doc) for doc in results]
    markdown = "\n".join(lines)
    return format_response(
        markdown,
        build_decision(
            "search_content",
            DecisionStatus.OK,
            "Review the results and use get_template or answer_question for full content.",
            {"query": query, "result_count": len(results), "confidence_scores": confidence_scores},
        ),
        output_format,
    )


# ─── Project Setup Agent ──────────────────────────────────────────────────────

_RISK_QUESTIONS = """\
## Risk Pre-Scan Questions

Answer each question with a score: 0 = No / 1 = Partially / 2 = Yes

### Part A — Hard Blockers (answer before scoring)
If any answer below is Yes, **stop immediately** and consult the Compliance Hub.
- Does the system use subliminal/manipulative techniques to influence behaviour without user knowledge?
- Does it apply biometric categorisation based on sensitive characteristics (race, religion, politics)?
- Does it perform real-time biometric identification in public spaces?
- Does it evaluate individuals based on social behaviour ("social scoring")?

### Part B1 — Application Domain (0–10 total)
1. Is the system deployed in critical infrastructure (energy, water, transport)?
2. Does it decide on access to education, employment or social services?
3. Does it decide on credit, insurance or financial services?
4. Is it deployed in law enforcement, migration or the justice system?
5. Does the system affect safety (physical harm possible)?

### Part B2 — Data & Privacy (0–10 total)
1. Does the system process personal data (GDPR)?
2. Does training or inference data contain special categories (health, political, biometric)?
3. Is data from minors being processed?
4. Is the data source external/unknown (e.g. web scraping)?
5. Are user interactions stored without explicit consent?

### Part B3 — Autonomy & Impact (0–10 total)
1. Does the system make decisions without human intervention that impact individuals?
2. Are the consequences of an error difficult to reverse?
3. Are there no alternative control measures if the system fails?
4. Does the system interact directly with end users who do not know it is AI?
5. Does the system affect labour-related decisions (evaluation, selection, dismissal)?

**→ Next step:** Score each section (B1, B2, B3) and call `project_setup_risk` with the subtotals."""

_RISK_THRESHOLDS = [
    (6, "green", "Low risk — proceed to charter"),
    (15, "amber", "Elevated risk — additional measures required before proceeding"),
    (30, "red", "High risk — stop or redefine the project scope"),
]

_COLLAB_MODE_GUIDANCE = {
    "green": (
        "**Recommended starting point: Mode 2 (Advisory) or Mode 3 (Collaborative).**\n"
        "Low risk allows more AI autonomy. Start at Mode 2 and consider Mode 3 once trust is established."
    ),
    "amber": (
        "**Recommended starting point: Mode 2 (Advisory).**\n"
        "Elevated risk requires human approval for all AI outputs. "
        "Modes 4 and 5 require explicit Guardian approval."
    ),
    "red": (
        "**Recommended starting point: Mode 1 (Instrumental).**\n"
        "High risk demands minimal AI autonomy. Human must initiate every action. "
        "Do not proceed without Guardian and legal review."
    ),
}


def _risk_level(b1: int, b2: int, b3: int) -> tuple[int, str, str]:
    """Return (total, colour, interpretation) for the given B-scores."""
    b1 = max(0, min(10, b1))
    b2 = max(0, min(10, b2))
    b3 = max(0, min(10, b3))
    total = b1 + b2 + b3
    for threshold, colour, interpretation in _RISK_THRESHOLDS:
        if total <= threshold:
            return total, colour, interpretation
    return total, "red", _RISK_THRESHOLDS[-1][2]


@mcp.tool()
def project_setup_intake(description: str, output_format: str = "markdown") -> str:
    """START HERE when a user wants to set up, start, or kick off a new AI project or use case.

    This is Step 1 of the guided Project Setup workflow (3 steps total):
      1. project_setup_intake  ← you are here
      2. project_setup_risk
      3. project_setup_charter

    Do NOT call get_project_type, classify_risk, or get_template individually for project setup —
    use this workflow instead. Those tools are for standalone lookups only.

    Returns:
    - Type A / Type B classification framework applied to the description
    - Hard blocker checks (EU AI Act prohibited practices)
    - Scored risk questions (B1/B2/B3) for the user to complete

    After presenting this to the user and collecting their B1/B2/B3 subtotal scores,
    call `project_setup_risk` as the next step.

    Args:
        description: Free-text description of the AI project or use case
        output_format: Response format — "markdown" (default) or "json"
    """
    index = get_index()

    # Fetch project type framework
    type_docs = index.get_phase_docs(1, "activities")
    if not type_docs:
        type_docs = [
            d for d in index.docs if "activiteiten" in d.path and "02-fase-ontdekking" in d.path
        ]

    type_section = ""
    if type_docs:
        type_section = (
            f"## Step 1a: Classify your project type\n\n"
            f"**Project description:** {description}\n\n"
            f"Use the Type A / Type B framework below to classify this project, "
            f"then confirm the type with the user.\n\n"
            f"---\n\n{_format_doc_full(type_docs[0])}"
        )
    else:
        type_section = (
            f"## Step 1a: Project type\n\n"
            f"**Project description:** {description}\n\n"
            f"- **Type A** — Deterministic AI: rules, classification, prediction (e.g. fraud detection, document routing)\n"
            f"- **Type B** — Generative AI: LLMs, content creation, summarisation, conversation\n\n"
            f"Classify the project and confirm with the user."
        )

    markdown = (
        f"# Project Setup — Step 1: Intake\n\n"
        f"{type_section}\n\n"
        f"---\n\n"
        f"{_RISK_QUESTIONS}\n\n"
        f"---\n\n"
        f"**Next step:** Present the risk questions to the user, collect their B1/B2/B3 scores, "
        f"then call `project_setup_risk` with `description`, `project_type` (A or B), "
        f"and `risk_scores_b1`, `risk_scores_b2`, `risk_scores_b3`."
    )
    return format_response(
        markdown,
        build_decision(
            "project_setup_intake",
            DecisionStatus.OK,
            "Present risk questions to the user, then call project_setup_risk with scores.",
            {"description_excerpt": description[:100]},
            next_tool="project_setup_risk",
        ),
        output_format,
    )


@mcp.tool()
def project_setup_risk(
    description: str,
    project_type: str,
    risk_scores_b1: int,
    risk_scores_b2: int,
    risk_scores_b3: int,
    output_format: str = "markdown",
) -> str:
    """Step 2 of the guided Project Setup workflow: calculate risk level and recommend collaboration mode.

    Call this ONLY after running project_setup_intake (Step 1) and collecting B1/B2/B3 scores from the user.
    Returns risk level (green/amber/red) and recommended collaboration mode.

    Present the findings to the user for confirmation, then call `project_setup_charter` (Step 3).

    Args:
        description: Free-text description of the AI project
        project_type: "A" (deterministic) or "B" (generative)
        risk_scores_b1: Part B1 subtotal (Application Domain), 0–10
        risk_scores_b2: Part B2 subtotal (Data & Privacy), 0–10
        risk_scores_b3: Part B3 subtotal (Autonomy & Impact), 0–10
        output_format: Response format — "markdown" (default) or "json"
    """
    index = get_index()

    total, colour, interpretation = _risk_level(risk_scores_b1, risk_scores_b2, risk_scores_b3)
    mode_guidance = _COLLAB_MODE_GUIDANCE.get(colour, _COLLAB_MODE_GUIDANCE["amber"])

    # Fetch HAS-H collaboration modes content
    has_h_docs = [d for d in index.docs if "has-h" in d.path.lower()]
    has_h_section = ""
    if has_h_docs:
        has_h_section = (
            f"\n\n---\n\n## Collaboration Modes Reference\n\n{has_h_docs[0].body[:1500]}..."
        )

    markdown = (
        f"# Project Setup — Step 2: Risk Assessment\n\n"
        f"**Project:** {description}\n"
        f"**Type:** {project_type.upper()}\n\n"
        f"## Risk Score\n\n"
        f"| Section | Score |\n"
        f"|:--------|------:|\n"
        f"| B1 — Application Domain | {max(0, min(10, risk_scores_b1))}/10 |\n"
        f"| B2 — Data & Privacy     | {max(0, min(10, risk_scores_b2))}/10 |\n"
        f"| B3 — Autonomy & Impact  | {max(0, min(10, risk_scores_b3))}/10 |\n"
        f"| **Total**               | **{total}/30** |\n\n"
        f"**Risk level: {colour.upper()}** — {interpretation}\n\n"
        f"## Recommended Collaboration Mode\n\n"
        f"{mode_guidance}"
        f"{has_h_section}\n\n"
        f"---\n\n"
        f"**Next step:** Present this summary to the user for confirmation. "
        f"Ask for the collaboration mode number (1–5) they want to proceed with, "
        f"then call `project_setup_charter` with `description`, `project_type`, "
        f"`risk_level` ('{colour}'), `collaboration_mode`, and any `additional_context` "
        f"(team, budget, timeline, etc.)."
    )
    return format_response(
        markdown,
        build_decision(
            "project_setup_risk",
            DecisionStatus.OK,
            f"Risk is {colour.upper()}. Confirm with user and call project_setup_charter.",
            {
                "risk_level": colour,
                "total_score": total,
                "scores": {
                    "b1": max(0, min(10, risk_scores_b1)),
                    "b2": max(0, min(10, risk_scores_b2)),
                    "b3": max(0, min(10, risk_scores_b3)),
                },
            },
            next_tool="project_setup_charter",
        ),
        output_format,
    )


@mcp.tool()
def project_setup_charter(
    description: str,
    project_type: str,
    risk_level: str,
    collaboration_mode: str,
    additional_context: str = "",
    output_format: str = "markdown",
) -> str:
    """Step 3 (final) of the guided Project Setup workflow: generate a pre-filled Project Charter.

    Call this ONLY after running project_setup_risk (Step 2) and the user has confirmed their
    risk level and collaboration mode. Returns the Project Charter template with all known fields
    pre-filled from the accumulated context.

    Fill in any remaining [placeholder] fields based on the conversation so far.
    Present the result to the user for review and approval.

    Args:
        description: Free-text description of the AI project
        project_type: "A" (deterministic) or "B" (generative)
        risk_level: Risk colour from step 2 ("green", "amber", or "red")
        collaboration_mode: Mode number as string ("1"–"5") confirmed by user
        additional_context: Optional extra context (team, budget, timeline, stakeholders, etc.)
        output_format: Response format — "markdown" (default) or "json"
    """
    index = get_index()

    # Fetch the project charter template
    charter_docs = [d for d in index.docs if "project-charter" in d.path and d.type == "template"]
    if not charter_docs:
        charter_docs = [d for d in index.docs if "project-charter" in d.path]

    if not charter_docs:
        return format_response(
            "Project Charter template not found in the index.",
            build_decision(
                "project_setup_charter",
                DecisionStatus.NOT_FOUND,
                "Reload the content index and retry.",
                {"project_type": project_type, "risk_level": risk_level},
            ),
            output_format,
        )

    charter_template = charter_docs[0].body

    mode_names = {
        "1": "Mode 1 — Instrumental (The Tool)",
        "2": "Mode 2 — Advisory (The Advisor)",
        "3": "Mode 3 — Collaborative (The Partner)",
        "4": "Mode 4 — Delegated (The Executor)",
        "5": "Mode 5 — Autonomous (The Agent)",
    }
    mode_label = mode_names.get(str(collaboration_mode), f"Mode {collaboration_mode}")

    eu_risk = {
        "green": "Minimal",
        "amber": "Limited",
        "red": "High",
    }.get(risk_level.lower(), risk_level)

    context_section = ""
    if additional_context:
        context_section = f"\n\n## Additional Context Provided\n\n{additional_context}"

    markdown = (
        f"# Project Setup — Step 3: Project Charter\n\n"
        f"The template below is pre-filled with the context gathered in steps 1 and 2. "
        f"Fill in the remaining `[placeholder]` fields based on what you know from the conversation. "
        f"Present the completed charter to the user for review and approval.\n\n"
        f"---\n\n"
        f"**Prefilled values:**\n"
        f"- Project type: **{project_type.upper()}**\n"
        f"- Risk level: **{risk_level.upper()}** → EU AI Act category: **{eu_risk}**\n"
        f"- Collaboration mode: **{mode_label}**\n"
        f"- Description: {description}"
        f"{context_section}\n\n"
        f"---\n\n"
        f"{charter_template}\n\n"
        f"---\n\n"
        f"> **Instructions for filling the charter:**\n"
        f"> - Replace `\\[Route\\]` with Fast Lane or Standard based on risk level "
        f"(green = Fast Lane eligible, amber/red = Standard lifecycle).\n"
        f"> - Set `Collaboration Mode` to: {mode_label}\n"
        f"> - Set `Risk Category (EU AI Act)` to: {eu_risk}\n"
        f'> - Fill `Concept` using the project description: "{description}"\n'
        f"> - Leave team names, budget, and success criteria as `[placeholder]` "
        f"if not provided — ask the user.\n"
        f"> - Present the filled charter to the user for approval before proceeding to Gate 1."
    )
    return format_response(
        markdown,
        build_decision(
            "project_setup_charter",
            DecisionStatus.OK,
            "Present the charter to the user for approval, then proceed to Gate 1.",
            {
                "project_type": project_type.upper(),
                "risk_level": risk_level,
                "collaboration_mode": str(collaboration_mode),
            },
        ),
        output_format,
    )


# ─── Gate Review Agent ────────────────────────────────────────────────────────


@mcp.tool()
def gate_review_intake(gate: int, evidence: list[str], output_format: str = "markdown") -> str:
    """START HERE for Gate Review preparation. Step 1 of the Gate Review workflow.

    This is Step 1 of the guided Gate Review workflow (2 steps total):
      1. gate_review_intake  ← you are here
      2. gate_review_report

    Do NOT call check_gate_readiness directly for gate review preparation —
    use this workflow instead.

    Takes the gate number and a list of evidence items the team has prepared.
    Returns the gate checklist, identifies gaps, and guides the calling LLM to
    collect missing items from the user before generating the review report.

    Args:
        gate: Gate number (1–4)
        evidence: List of evidence items available (e.g. ["project charter", "risk scan"])
        output_format: Response format — "markdown" (default) or "json"
    """
    if gate not in range(1, 5):
        return format_response(
            f"Error: gate must be 1–4, got {gate}",
            build_decision(
                "gate_review_intake",
                DecisionStatus.ERROR,
                "Correct the gate parameter (1–4).",
                {"gate": gate},
            ),
            output_format,
        )

    index = get_index()

    # Fetch gate checklist
    checklist_docs = [
        d
        for d in index.docs
        if "gate-review" in d.path.lower()
        or ("gate" in d.path.lower() and "checklist" in d.path.lower())
    ]

    checklist_content = checklist_docs[0].body if checklist_docs else ""

    evidence_str = "\n".join(f"- {e}" for e in evidence) if evidence else "_(none provided)_"

    # Simple gap detection: flag checklist items not mentioned in evidence
    gaps = []
    if checklist_content:
        evidence_lower = " ".join(evidence).lower()
        for line in checklist_content.splitlines():
            line = line.strip()
            if not line or not (line.startswith("- [ ]") or line.startswith("- [x]")):
                continue
            item = line.removeprefix("- [ ]").removeprefix("- [x]").strip()
            if not any(word in evidence_lower for word in item.lower().split() if len(word) > 4):
                gaps.append(item)

    gaps_str = (
        "\n".join(f"- {g}" for g in gaps[:8])
        if gaps
        else "_(no obvious gaps detected — verify manually)_"
    )

    ev_items = parse_evidence(evidence, gate=gate)
    ev_summary = evidence_summary(ev_items)

    markdown = (
        f"# Gate Review — Step 1: Intake (Gate {gate})\n\n"
        f"## Evidence provided\n\n{evidence_str}\n\n"
        f"## Potential gaps\n\n{gaps_str}\n\n"
        f"---\n\n"
        f"## Gate {gate} Checklist\n\n{checklist_content}\n\n"
        f"---\n\n"
        f"**Next step:** Present the gaps to the user. Ask them to confirm or clarify each gap. "
        f"Then call `gate_review_report` with `gate`, the confirmed `evidence` list, "
        f"and the confirmed `gaps` list to generate the Guardian-ready review summary."
    )
    return format_response(
        markdown,
        build_decision(
            "gate_review_intake",
            DecisionStatus.OK,
            "Present gaps to user, confirm, then call gate_review_report.",
            {
                "gate": gate,
                "evidence_count": len(evidence),
                "gap_count": len(gaps),
                "evidence_summary": ev_summary,
            },
            next_tool="gate_review_report",
        ),
        output_format,
    )


@mcp.tool()
def gate_review_report(
    gate: int, evidence: list[str], gaps: list[str], output_format: str = "markdown"
) -> str:
    """Step 2 of the Gate Review workflow: generate a Guardian-ready review summary.

    Call this ONLY after running gate_review_intake (Step 1) and confirming
    evidence and gaps with the user.

    Returns a structured gate review summary the Guardian can use to make
    a Go / No-Go decision.

    Args:
        gate: Gate number (1–4)
        evidence: Confirmed list of available evidence items
        gaps: Confirmed list of gaps or missing items (empty list = no gaps)
        output_format: Response format — "markdown" (default) or "json"
    """
    if gate not in range(1, 5):
        return format_response(
            f"Error: gate must be 1–4, got {gate}",
            build_decision(
                "gate_review_report",
                DecisionStatus.ERROR,
                "Correct the gate parameter (1–4).",
                {"gate": gate},
            ),
            output_format,
        )

    gate_names = {
        1: "Go/No-Go Discovery",
        2: "Pilot Investment",
        3: "Production-Ready",
        4: "Go-Live",
    }
    gate_label = gate_names.get(gate, f"Gate {gate}")

    evidence_str = "\n".join(f"- ✅ {e}" for e in evidence) if evidence else "_(none)_"

    if gaps:
        gaps_str = "\n".join(f"- ⚠️ {g}" for g in gaps)
        readiness = "**NOT READY** — gaps must be resolved before Guardian sign-off."
        decision = "- [ ] **No-Go / Address gaps first**\n- [ ] **Conditional Go** _(gaps accepted with mitigation)_"
    else:
        gaps_str = "_(none — all criteria met)_"
        readiness = "**READY** — all evidence present. Proceed to Guardian review."
        decision = "- [ ] **Go** _(proceed to next phase)_\n- [ ] **No-Go** _(Guardian decision)_"

    ready = not gaps
    ev_items = parse_evidence(evidence, gate=gate)
    ev_summary = evidence_summary(ev_items)

    # Fire escalation event
    event_type = EventType.GATE_REVIEW_PASSED if ready else EventType.GATE_REVIEW_FAILED
    _module_escalation_registry.fire(
        event_type,
        data={
            "gate": gate,
            "evidence_count": len(evidence),
            "gap_count": len(gaps),
            "ready": ready,
        },
    )

    markdown = (
        f"# Gate {gate} Review Summary — {gate_label}\n\n"
        f"## Readiness assessment\n\n{readiness}\n\n"
        f"## Evidence\n\n{evidence_str}\n\n"
        f"## Gaps\n\n{gaps_str}\n\n"
        f"---\n\n"
        f"## Guardian Decision\n\n{decision}\n\n"
        f"**Guardian:** \\[Name\\]\n"
        f"**Date:** \\[Date\\]\n"
        f"**Remarks:** \\[Any conditions, observations, or follow-up actions\\]\n\n"
        f"---\n\n"
        f"> Present this summary to the Guardian for sign-off. "
        f"If gaps exist, agree on a resolution plan before proceeding."
    )
    return format_response(
        markdown,
        build_decision(
            "gate_review_report",
            DecisionStatus.OK,
            "Present to Guardian for sign-off."
            if ready
            else "Resolve gaps before Guardian review.",
            {
                "gate": gate,
                "evidence_count": len(evidence),
                "gap_count": len(gaps),
                "ready": ready,
                "evidence_summary": ev_summary,
            },
        ),
        output_format,
    )


# ─── Template Advisor ──────────────────────────────────────────────────────────


@mcp.tool()
def template_advisor(
    role: str, phase: int, context: str = "", output_format: str = "markdown"
) -> str:
    """Get recommended templates for a role and lifecycle phase, with context pre-filled.

    Use this when a user asks which templates they need, wants to start filling
    a template, or asks what to do next in a given phase.

    Returns the recommended templates for the role + phase combination with
    any provided context already woven into the instructions.

    Args:
        role: Role name (e.g. "AI Product Manager", "Guardian", "Tech Lead")
        phase: Lifecycle phase number (1–5)
        context: Optional project context to pre-fill into template instructions
                 (e.g. "Type A, green risk, fraud detection project")
        output_format: Response format — "markdown" (default) or "json"
    """
    if phase not in range(1, 6):
        return format_response(
            f"Error: phase must be 1–5, got {phase}",
            build_decision(
                "template_advisor",
                DecisionStatus.ERROR,
                "Correct the phase parameter (1–5).",
                {"role": role, "phase": phase},
            ),
            output_format,
        )

    index = get_index()
    phase_names = {
        1: "Discovery",
        2: "Validation",
        3: "Development",
        4: "Delivery",
        5: "Monitoring",
    }
    phase_label = phase_names.get(phase, f"Phase {phase}")

    # Role + phase match first
    templates = [
        d
        for d in index.docs
        if d.type == "template" and phase in d.phases and (not d.roles or role in d.roles)
    ]
    # Broaden if no role match
    if not templates:
        templates = [d for d in index.docs if d.type == "template" and phase in d.phases]

    if not templates:
        return format_response(
            f"No templates found for {role} in phase {phase} ({phase_label}).",
            build_decision(
                "template_advisor",
                DecisionStatus.NOT_FOUND,
                "Try a different role or phase.",
                {"role": role, "phase": phase, "template_count": 0},
            ),
            output_format,
        )

    context_note = f"\n\n**Project context:** {context}" if context else ""

    sections = [
        f"# Template Advisor — {role} / Phase {phase}: {phase_label}{context_note}\n\n"
        f"The following templates are recommended for your role and phase. "
        f"Each template is shown in full — fill in the `[placeholder]` fields.\n"
    ]

    for doc in templates:
        sections.append(_format_doc_full(doc))

    markdown = "\n\n---\n\n".join(sections)
    return format_response(
        markdown,
        build_decision(
            "template_advisor",
            DecisionStatus.OK,
            "Fill in the [placeholder] fields and present to the user for approval.",
            {"role": role, "phase": phase, "template_count": len(templates)},
        ),
        output_format,
    )


# ─── Compliance Agent ──────────────────────────────────────────────────────────


_EU_RISK_KEYWORDS = {
    "unacceptable": [
        "social scor",
        "subliminal",
        "manipulat",
        "biometric categor",
        "real-time biometric",
        "emotion recognit",
        "exploit vulnerabl",
    ],
    "high": [
        "hire",
        "hiring",
        "recruit",
        "cv screen",
        "employment",
        "credit scor",
        "loan",
        "insurance",
        "law enforcement",
        "border",
        "migration",
        "asylum",
        "critical infrastructure",
        "energy grid",
        "water supply",
        "transport",
        "education admission",
        "exam",
        "welfare benefit",
        "social service",
        "medical device",
        "safety component",
    ],
    "limited": [
        "chatbot",
        "virtual assistant",
        "deepfake",
        "synthetic content",
        "emotion detect",
        "ai-generated",
        "customer service bot",
    ],
}


def _classify_eu_risk(description: str) -> str:
    """Heuristic EU AI Act risk classification based on description keywords."""
    desc_lower = description.lower()
    for category, keywords in _EU_RISK_KEYWORDS.items():
        if any(kw in desc_lower for kw in keywords):
            return category
    return "minimal"


@mcp.tool()
def compliance_intake(description: str, output_format: str = "markdown") -> str:
    """START HERE for EU AI Act compliance assessment. Step 1 of the Compliance workflow.

    This is Step 1 of the guided Compliance workflow (2 steps total):
      1. compliance_intake   ← you are here
      2. compliance_checklist

    Do NOT call classify_risk directly for compliance assessment —
    use this workflow instead.

    Classifies the AI system against EU AI Act risk categories and returns
    the relevant obligations. Present findings to the user for confirmation,
    then call compliance_checklist.

    Args:
        description: Free-text description of the AI system
        output_format: Response format — "markdown" (default) or "json"
    """
    index = get_index()

    heuristic_category = _classify_eu_risk(description)

    # Fetch EU AI Act overview
    eu_docs = [
        d
        for d in index.docs
        if "eu-ai-act" in d.path and d.type in ("compliance", "index", "guide", "strategic")
    ]
    eu_content = _format_doc_full(eu_docs[0]) if eu_docs else ""

    category_guidance = {
        "unacceptable": (
            "🔴 **Unacceptable Risk (Art. 5) — PROHIBITED**\n\n"
            "This system appears to fall under prohibited AI practices. "
            "It cannot be deployed in the EU. Consult legal counsel immediately."
        ),
        "high": (
            "🟠 **High Risk (Art. 6 + Annex III)**\n\n"
            "This system likely qualifies as high-risk AI. Mandatory requirements apply: "
            "risk management system (Art. 9), data governance (Art. 10), technical documentation "
            "(Art. 11–12), transparency (Art. 13), human oversight (Art. 14), and accuracy (Art. 15)."
        ),
        "limited": (
            "🟡 **Limited Risk — Transparency Obligations (Art. 50)**\n\n"
            "This system has transparency obligations. Users must be informed they are "
            "interacting with an AI system. AI-generated content must be labelled."
        ),
        "minimal": (
            "🟢 **Minimal Risk**\n\n"
            "This system falls under minimal risk. No mandatory EU AI Act obligations apply, "
            "but voluntary codes of conduct are recommended."
        ),
    }

    guidance = category_guidance.get(heuristic_category, category_guidance["minimal"])

    markdown = (
        f"# Compliance Assessment — Step 1: Intake\n\n"
        f"**System description:** {description}\n\n"
        f"## Preliminary classification\n\n"
        f"{guidance}\n\n"
        f"⚠️ _This is a heuristic classification. Confirm with the user before proceeding._\n\n"
        f"---\n\n"
        f"{eu_content}\n\n"
        f"---\n\n"
        f"**Next step:** Present the preliminary classification to the user for confirmation. "
        f"Ask if the category is correct. Then call `compliance_checklist` with `description` "
        f"and `risk_category` (unacceptable / high / limited / minimal)."
    )
    return format_response(
        markdown,
        build_decision(
            "compliance_intake",
            DecisionStatus.OK,
            "Confirm category with user, then call compliance_checklist.",
            {"heuristic_category": heuristic_category, "description_excerpt": description[:100]},
            next_tool="compliance_checklist",
        ),
        output_format,
    )


@mcp.tool()
def compliance_checklist(
    description: str, risk_category: str, output_format: str = "markdown"
) -> str:
    """Step 2 of the Compliance workflow: generate a specific EU AI Act compliance checklist.

    Call this ONLY after compliance_intake (Step 1) and user confirmation of the risk category.

    Returns a concrete checklist with EU AI Act article references tailored to
    the system description and risk category.

    Args:
        description: Free-text description of the AI system
        risk_category: Confirmed risk category: "unacceptable", "high", "limited", or "minimal"
        output_format: Response format — "markdown" (default) or "json"
    """
    index = get_index()

    category = risk_category.lower().strip()

    if category == "unacceptable":
        blocked_text = (
            f"# Compliance Checklist — BLOCKED\n\n"
            f"**System:** {description}\n\n"
            f"🔴 **This system is prohibited under EU AI Act Art. 5.**\n\n"
            f"Deployment in the EU is not permitted. Required actions:\n\n"
            f"- [ ] Halt all development and deployment activities\n"
            f"- [ ] Consult legal counsel specialised in EU AI Act\n"
            f"- [ ] Document the decision and rationale\n"
            f"- [ ] Consider redesigning the use case to remove the prohibited element\n\n"
            f"Refer to Art. 5 of the EU AI Act for the full list of prohibited practices."
        )
        return format_response(
            blocked_text,
            build_decision(
                "compliance_checklist",
                DecisionStatus.ERROR,
                "STOP — this system is prohibited. Halt all development immediately.",
                {"risk_category": "unacceptable", "blocked": True},
            ),
            output_format,
        )

    # Fetch detailed compliance content
    compliance_docs = [
        d for d in index.docs if "07-compliance-hub" in d.path and "eu-ai-act" in d.path
    ]
    checklist_content = ""
    for doc in compliance_docs:
        if len(doc.body) > 500:
            checklist_content = doc.body
            break

    checklists_by_category = {
        "high": (
            "### Pre-development\n"
            "- [ ] **Art. 9** — Risk management system established and documented\n"
            "- [ ] **Art. 10** — Data governance policy covers training, validation, and test data\n"
            "- [ ] **Art. 11** — Technical documentation prepared (technical dossier)\n"
            "- [ ] **Annex III** — Confirmed system falls under high-risk category\n\n"
            "### During development\n"
            "- [ ] **Art. 12** — Logging and record-keeping mechanisms in place\n"
            "- [ ] **Art. 13** — Transparency measures designed (user-facing documentation)\n"
            "- [ ] **Art. 14** — Human oversight mechanisms defined per collaboration mode\n"
            "- [ ] **Art. 15** — Accuracy, robustness, and cybersecurity requirements addressed\n\n"
            "### Before go-live\n"
            "- [ ] **Art. 9** — Risk management system tested and validated\n"
            "- [ ] **Art. 16** — Conformity assessment completed\n"
            "- [ ] **Art. 49** — EU Declaration of Conformity signed\n"
            "- [ ] **Art. 49** — CE marking applied (where applicable)\n"
            "- [ ] Guardian sign-off obtained\n\n"
            "### After go-live\n"
            "- [ ] **Art. 9** — Risk management system actively monitored\n"
            "- [ ] **Art. 72** — Post-market monitoring plan active\n"
            "- [ ] **Art. 73** — Serious incident reporting procedure in place\n"
            "- [ ] Annual review of technical documentation scheduled\n"
        ),
        "limited": (
            "### Before go-live\n"
            "- [ ] **Art. 50** — Users are informed they are interacting with an AI system\n"
            "- [ ] **Art. 50** — AI-generated content is labelled as such (where applicable)\n"
            "- [ ] Disclosure mechanism implemented (e.g. 'Powered by AI' notice)\n\n"
            "### Recommended (voluntary)\n"
            "- [ ] Human oversight contact designated\n"
            "- [ ] Feedback mechanism for users provided\n"
            "- [ ] Internal logging of interactions enabled\n"
        ),
        "minimal": (
            "### Recommended (voluntary — no mandatory obligations)\n"
            "- [ ] Document the system purpose and intended use\n"
            "- [ ] Designate an accountable owner\n"
            "- [ ] Apply basic transparency (users know it is AI)\n"
            "- [ ] Enable human override in case of errors\n"
            "- [ ] Follow Voluntary Code of Conduct (EU AI Office)\n"
        ),
    }

    specific_checklist = checklists_by_category.get(category, checklists_by_category["minimal"])

    extra_content = (
        f"\n\n---\n\n## Detailed Blueprint Compliance Reference\n\n{checklist_content}"
        if checklist_content
        else ""
    )

    markdown = (
        f"# Compliance Checklist — {risk_category.capitalize()} Risk\n\n"
        f"**System:** {description}\n\n"
        f"---\n\n"
        f"{specific_checklist}"
        f"{extra_content}\n\n"
        f"---\n\n"
        f"> Review each item with your Guardian and legal counsel. "
        f"High-risk systems require conformity assessment before deployment."
    )
    return format_response(
        markdown,
        build_decision(
            "compliance_checklist",
            DecisionStatus.OK,
            "Work through the checklist with Guardian and legal counsel.",
            {"risk_category": category, "blocked": False},
        ),
        output_format,
    )


# ─── Conditional Guidance & Template Selection ────────────────────────────────

_VALID_PROJECT_TYPES = {"A", "B"}
_VALID_RISK_LEVELS = {"green", "amber", "red"}


@mcp.tool()
def get_guidance_for_profile(
    project_type: str,
    risk_level: str,
    phase: int,
    role: str = "",
    output_format: str = "markdown",
) -> str:
    """Get tailored guidance for a specific project profile (type × risk × phase × role).

    Use when: An agent knows the project type, risk level, and current phase and
    needs to surface the most relevant Blueprint guidance without a free-text search.
    Do NOT use when: You only need a template — use select_template instead.

    Args:
        project_type: "A" (deterministic) or "B" (generative).
        risk_level: "green", "amber", or "red".
        phase: Lifecycle phase 1–5.
        role: Optional role filter (e.g. "Guardian", "Tech Lead").
        output_format: "markdown" (default) or "json".

    Next step: call select_template to find relevant templates for the guidance returned.
    """
    if project_type not in _VALID_PROJECT_TYPES:
        return format_response(
            f"Error: project_type must be 'A' or 'B', got '{project_type}'",
            build_decision(
                "get_guidance_for_profile",
                DecisionStatus.ERROR,
                "Use 'A' for deterministic AI or 'B' for generative AI.",
                {"project_type": project_type},
            ),
            output_format,
        )
    if risk_level not in _VALID_RISK_LEVELS:
        return format_response(
            f"Error: risk_level must be 'green', 'amber', or 'red', got '{risk_level}'",
            build_decision(
                "get_guidance_for_profile",
                DecisionStatus.ERROR,
                "Use one of: green, amber, red.",
                {"risk_level": risk_level},
            ),
            output_format,
        )
    if phase not in range(1, 6):
        return format_response(
            f"Error: phase must be 1–5, got {phase}",
            build_decision(
                "get_guidance_for_profile",
                DecisionStatus.ERROR,
                "Correct the phase parameter (1–5).",
                {"phase": phase},
            ),
            output_format,
        )

    index = get_index()
    phase_names = {
        1: "Discovery",
        2: "Validation",
        3: "Development",
        4: "Delivery",
        5: "Monitoring",
    }

    # Collect docs matching the profile: phase + optionally role
    candidates = [
        d
        for d in index.docs
        if phase in d.phases
        and d.type not in ("template",)
        and (not role or not d.roles or role in d.roles)
    ]

    # Score by relevance: risk_level tag match, type match
    risk_tag_map = {
        "red": ["risk", "compliance", "security"],
        "amber": ["risk", "validation"],
        "green": [],
    }
    preferred_tags = set(risk_tag_map.get(risk_level, []))

    def _score(doc) -> int:
        s = 0
        if preferred_tags & set(doc.tags):
            s += 2
        if doc.type in ("objectives", "activities", "deliverables"):
            s += 1
        return s

    candidates.sort(key=_score, reverse=True)
    top = candidates[:5]

    if not top:
        return format_response(
            f"No guidance found for project_type={project_type}, risk={risk_level}, phase={phase}.",
            build_decision(
                "get_guidance_for_profile",
                DecisionStatus.NOT_FOUND,
                "Try broadening the search with search_content.",
                {
                    "project_type": project_type,
                    "risk_level": risk_level,
                    "phase": phase,
                    "doc_count": 0,
                },
            ),
            output_format,
        )

    sections = [
        f"# Guidance for Type {project_type} / {risk_level.capitalize()} Risk / "
        f"Phase {phase} ({phase_names.get(phase, '')})" + (f" / {role}" if role else "") + "\n"
    ]
    for doc in top:
        sections.append(f"## {doc.title}\n\n_`{doc.path}`_\n\n{doc.body[:800]}...")

    markdown = "\n\n---\n\n".join(sections)
    return format_response(
        markdown,
        build_decision(
            "get_guidance_for_profile",
            DecisionStatus.OK,
            "Review the guidance above and adapt to your specific context.",
            {
                "project_type": project_type,
                "risk_level": risk_level,
                "phase": phase,
                "role": role,
                "doc_count": len(top),
            },
        ),
        output_format,
    )


@mcp.tool()
def select_template(
    goal: str,
    phase: int | None = None,
    role: str = "",
    output_format: str = "markdown",
) -> str:
    """Select the most relevant Blueprint template for a stated goal.

    Use when: A user or agent knows what they want to produce (e.g. "project charter",
    "risk pre-scan") and needs the matching template.
    Do NOT use when: You need phase guidance, not a template — use get_guidance_for_profile.

    Args:
        goal: Free-text description of what the user wants to create or fill in.
        phase: Optional lifecycle phase filter (1–5).
        role: Optional role filter (e.g. "Guardian").
        output_format: "markdown" (default) or "json".
    """
    index = get_index()
    goal_lower = goal.lower()

    templates = index.get_templates()

    # Apply phase and role filters
    if phase is not None:
        templates = [t for t in templates if phase in t.phases]
    if role:
        role_match = [t for t in templates if role in t.roles]
        if role_match:
            templates = role_match

    if not templates:
        return format_response(
            f"No templates found matching goal='{goal}'" + (f", phase={phase}" if phase else ""),
            build_decision(
                "select_template",
                DecisionStatus.NOT_FOUND,
                "Try removing the phase or role filter.",
                {"goal": goal, "match_count": 0},
            ),
            output_format,
        )

    # Score templates by keyword overlap with goal
    def _score(doc) -> int:
        text = (doc.title + " " + doc.path + " " + (doc.summary or "")).lower()
        return sum(1 for word in goal_lower.split() if len(word) > 3 and word in text)

    templates.sort(key=_score, reverse=True)
    best = [t for t in templates if _score(t) > 0]

    if not best:
        names = "\n".join(f"- `{d.path}`: {d.title}" for d in templates[:10])
        return format_response(
            f"No strong match for '{goal}'. Available templates:\n\n{names}",
            build_decision(
                "select_template",
                DecisionStatus.NOT_FOUND,
                "Try a different keyword or use get_template with a path from the list.",
                {"goal": goal, "match_count": 0},
            ),
            output_format,
        )

    top = best[:3]
    sections = [f'# Template Selection for: "{goal}"\n']
    for doc in top:
        sections.append(f"## {doc.title}\n\n_`{doc.path}`_\n\n{doc.body[:600]}...")

    markdown = "\n\n---\n\n".join(sections)
    return format_response(
        markdown,
        build_decision(
            "select_template",
            DecisionStatus.OK,
            f"Best match: '{top[0].title}'. Fill in [placeholder] fields.",
            {"goal": goal, "match_count": len(top), "top_match_path": top[0].path},
        ),
        output_format,
    )


# ─── Workflow Meta-tools ──────────────────────────────────────────────────────

PHASE_PREREQUISITES: dict[int, list[int]] = {
    1: [],
    2: [1],
    3: [1, 2],
    4: [2, 3],
    5: [3, 4],
}

_WORKFLOWS: dict[str, dict] = {
    "project_setup": {
        "description": "Set up a new AI project from scratch",
        "steps": [
            {"step": 1, "tool": "project_setup_intake", "required_params": ["description"]},
            {
                "step": 2,
                "tool": "project_setup_risk",
                "required_params": [
                    "description",
                    "project_type",
                    "risk_scores_b1",
                    "risk_scores_b2",
                    "risk_scores_b3",
                ],
            },
            {
                "step": 3,
                "tool": "project_setup_charter",
                "required_params": [
                    "description",
                    "project_type",
                    "risk_level",
                    "collaboration_mode",
                ],
            },
        ],
    },
    "gate_review": {
        "description": "Prepare and execute a Gate Review",
        "steps": [
            {"step": 1, "tool": "gate_review_intake", "required_params": ["gate", "evidence"]},
            {
                "step": 2,
                "tool": "gate_review_report",
                "required_params": ["gate", "evidence", "gaps"],
            },
        ],
    },
    "compliance_assessment": {
        "description": "EU AI Act compliance assessment for an AI system",
        "steps": [
            {"step": 1, "tool": "compliance_intake", "required_params": ["description"]},
            {
                "step": 2,
                "tool": "compliance_checklist",
                "required_params": ["description", "risk_category"],
            },
        ],
    },
}

_CONTEXT_SCHEMA: dict = {
    "required": ["description"],
    "optional": ["project_type", "risk_level", "collaboration_mode", "phase", "gate"],
    "valid_project_types": ["A", "B"],
    "valid_risk_levels": ["green", "amber", "red"],
    "valid_collaboration_modes": ["1", "2", "3", "4", "5"],
    "valid_phases": [1, 2, 3, 4, 5],
    "valid_gates": [1, 2, 3, 4],
}


@mcp.tool()
def can_enter_phase(phase: int, completed_gates: list[int], output_format: str = "markdown") -> str:
    """Check whether all required gates are complete before entering a lifecycle phase.

    Use this before calling get_phase_guidance to confirm the team is eligible
    to proceed. Next step: call get_phase_guidance if can_enter is True, or
    gate_review_intake to complete missing gates.

    Args:
        phase: Target phase number (2–5).
        completed_gates: List of gate numbers the team has already passed.
        output_format: "markdown" (default) or "json".
    """
    if phase not in range(1, 6):
        return format_response(
            f"Error: phase must be 1–5, got {phase}",
            build_decision(
                "can_enter_phase",
                DecisionStatus.ERROR,
                "Correct the phase parameter (1–5).",
                {"phase": phase},
            ),
            output_format,
        )
    required = PHASE_PREREQUISITES[phase]
    missing = [g for g in required if g not in completed_gates]
    can_enter = len(missing) == 0
    action = (
        f"All prerequisites met — proceed to Phase {phase}."
        if can_enter
        else f"Complete gate(s) {missing} before entering Phase {phase}."
    )
    phase_names = {
        1: "Discovery",
        2: "Validation",
        3: "Development",
        4: "Delivery",
        5: "Monitoring",
    }
    markdown = (
        f"## Phase {phase} ({phase_names.get(phase, '')}) Entry Check\n\n"
        f"**Can enter:** {'✅ Yes' if can_enter else '❌ No'}\n\n"
        f"**Required gates:** {required or 'None'}\n"
        f"**Completed gates:** {sorted(completed_gates) or 'None'}\n"
        f"**Missing gates:** {missing or 'None'}\n\n"
        f"**Next action:** {action}"
    )
    return format_response(
        markdown,
        build_decision(
            "can_enter_phase",
            DecisionStatus.OK,
            action,
            {
                "can_enter": can_enter,
                "phase": phase,
                "missing_gates": missing,
                "completed_gates": sorted(completed_gates),
            },
        ),
        output_format,
    )


@mcp.tool()
def get_workflow_status(output_format: str = "markdown") -> str:
    """Return an overview of all available MCP workflows and their tool sequences.

    Use this when an agent needs to discover which multi-step workflows exist
    and what tools each workflow involves. Useful as a starting point before
    deciding which workflow to follow. Next step: call the first tool of the
    relevant workflow (e.g. project_setup_intake, gate_review_intake).

    Args:
        output_format: "markdown" (default) or "json".
    """
    total_tools = sum(len(w["steps"]) for w in _WORKFLOWS.values())
    lines = ["# Blueprint Workflows\n"]
    for name, wf in _WORKFLOWS.items():
        lines.append(f"## {name}\n\n_{wf['description']}_\n")
        lines.append("| Step | Tool | Required parameters |")
        lines.append("|------|------|---------------------|")
        for step in wf["steps"]:
            params = ", ".join(f"`{p}`" for p in step["required_params"])
            lines.append(f"| {step['step']} | `{step['tool']}` | {params} |")
        lines.append("")
    markdown = "\n".join(lines)
    return format_response(
        markdown,
        build_decision(
            "get_workflow_status",
            DecisionStatus.OK,
            "Select a workflow and call its first step tool.",
            {
                "workflows": list(_WORKFLOWS.keys()),
                "total_workflows": len(_WORKFLOWS),
                "total_tools": total_tools,
            },
        ),
        output_format,
    )


@mcp.tool()
def validate_project_context(data: dict, output_format: str = "markdown") -> str:
    """Validate that a project context dict has sufficient information to start a workflow.

    Call this before any workflow to surface missing or invalid fields early.
    The decision data includes a recommended next_tool based on what context
    is present. Next step: call the tool named in next_tool from the decision data.

    Args:
        data: Project context dict. Recognised keys: description, project_type
              (A/B), risk_level (green/amber/red), collaboration_mode (1–5),
              phase (1–5), gate (1–4).
        output_format: "markdown" (default) or "json".
    """
    missing_required: list[str] = []
    invalid_values: dict[str, str] = {}
    suggestions: list[str] = []
    for field in _CONTEXT_SCHEMA["required"]:
        if field not in data or not data[field]:
            missing_required.append(field)
    if (
        "project_type" in data
        and data["project_type"] not in _CONTEXT_SCHEMA["valid_project_types"]
    ):
        invalid_values["project_type"] = (
            f"Must be one of {_CONTEXT_SCHEMA['valid_project_types']}, got '{data['project_type']}'"
        )
    if "risk_level" in data and data["risk_level"] not in _CONTEXT_SCHEMA["valid_risk_levels"]:
        invalid_values["risk_level"] = (
            f"Must be one of {_CONTEXT_SCHEMA['valid_risk_levels']}, got '{data['risk_level']}'"
        )
    if (
        "collaboration_mode" in data
        and str(data["collaboration_mode"]) not in _CONTEXT_SCHEMA["valid_collaboration_modes"]
    ):
        invalid_values["collaboration_mode"] = (
            f"Must be one of {_CONTEXT_SCHEMA['valid_collaboration_modes']}, got '{data['collaboration_mode']}'"
        )
    if "phase" in data and data["phase"] not in _CONTEXT_SCHEMA["valid_phases"]:
        invalid_values["phase"] = (
            f"Must be one of {_CONTEXT_SCHEMA['valid_phases']}, got '{data['phase']}'"
        )
    if "gate" in data and data["gate"] not in _CONTEXT_SCHEMA["valid_gates"]:
        invalid_values["gate"] = (
            f"Must be one of {_CONTEXT_SCHEMA['valid_gates']}, got '{data['gate']}'"
        )
    is_valid = not missing_required and not invalid_values
    has_description = "description" in data and data.get("description")
    has_gate = "gate" in data and data.get("gate") and "gate" not in invalid_values
    has_project_type = "project_type" in data and "project_type" not in invalid_values
    has_risk_level = "risk_level" in data and "risk_level" not in invalid_values
    has_collab_mode = "collaboration_mode" in data and "collaboration_mode" not in invalid_values
    if has_gate and has_description:
        next_tool = "gate_review_intake"
    elif has_description and has_project_type and has_risk_level and has_collab_mode:
        next_tool = "project_setup_charter"
    elif has_description and has_project_type:
        next_tool = "project_setup_risk"
    elif has_description:
        next_tool = "project_setup_intake"
    else:
        next_tool = None
    if missing_required:
        suggestions.append(f"Provide the required field(s): {', '.join(missing_required)}")
    if invalid_values:
        suggestions.append(f"Fix invalid values for: {', '.join(invalid_values.keys())}")
    if is_valid and next_tool:
        suggestions.append(f"Context is valid — call `{next_tool}` next.")
    status_str = DecisionStatus.OK if is_valid else DecisionStatus.ERROR
    action = suggestions[0] if suggestions else "Context validated."
    lines = ["## Project Context Validation\n"]
    lines.append(f"**Valid:** {'✅ Yes' if is_valid else '❌ No'}\n")
    if missing_required:
        lines.append(f"**Missing required:** {', '.join(missing_required)}")
    if invalid_values:
        for field, msg in invalid_values.items():
            lines.append(f"**Invalid `{field}`:** {msg}")
    if suggestions:
        lines.append("\n**Suggestions:**")
        for s in suggestions:
            lines.append(f"- {s}")
    return format_response(
        "\n".join(lines),
        build_decision(
            "validate_project_context",
            status_str,
            action,
            {
                "is_valid": is_valid,
                "missing_required": missing_required,
                "invalid_values": invalid_values,
                "suggestions": suggestions,
                "next_recommended_tool": next_tool,
            },
            next_tool=next_tool,
        ),
        output_format,
    )


# ─── Template Customisation Tools ────────────────────────────────────────────


@mcp.tool()
def list_template_placeholders(template_path: str, output_format: str = "markdown") -> str:
    """List all ``{{placeholder}}`` tokens in a Blueprint template.

    Args:
        template_path: Relative path of the template doc (matches ContentIndex keys).
        output_format: "markdown" (default) or "json".
    """
    index = get_index()
    doc = index.by_path.get(template_path)
    if doc is None:
        matches = [d for d in index.docs if template_path in d.path]
        doc = matches[0] if matches else None
    if doc is None:
        return format_response(
            f"Template '{template_path}' not found.",
            build_decision(
                "list_template_placeholders",
                DecisionStatus.NOT_FOUND,
                "Check the template path with search_content.",
                {"template_path": template_path, "placeholders": []},
            ),
            output_format,
        )
    placeholders = parse_placeholders(doc.body)
    markdown = f"## Placeholders in `{doc.title}`\n\n" + (
        ("\n".join(f"- `{{{{{p}}}}}`" for p in placeholders))
        if placeholders
        else "_No placeholders found in this template._"
    )
    return format_response(
        markdown,
        build_decision(
            "list_template_placeholders",
            DecisionStatus.OK,
            "Use fill_template to populate these placeholders.",
            {"template_path": template_path, "placeholders": placeholders},
        ),
        output_format,
    )


@mcp.tool()
def fill_template(template_path: str, values: dict, output_format: str = "markdown") -> str:
    """Fill ``{{placeholder}}`` tokens in a Blueprint template with provided values.

    Args:
        template_path: Relative path of the template doc.
        values: Dict mapping placeholder names to replacement strings.
        output_format: "markdown" (default) or "json".
    """
    index = get_index()
    doc = index.by_path.get(template_path)
    if doc is None:
        matches = [d for d in index.docs if template_path in d.path]
        doc = matches[0] if matches else None
    if doc is None:
        return format_response(
            f"Template '{template_path}' not found.",
            build_decision(
                "fill_template",
                DecisionStatus.NOT_FOUND,
                "Check the template path with search_content.",
                {
                    "template_path": template_path,
                    "filled_content": None,
                    "missing_placeholders": [],
                },
            ),
            output_format,
        )
    filled, missing = fill_placeholders(doc.body, values)
    status = DecisionStatus.OK
    if missing:
        action = f"Provide values for missing placeholders: {', '.join(missing)}"
    else:
        action = "Template fully populated — review the filled content below."
    markdown = f"## Filled Template: {doc.title}\n\n{filled}"
    if missing:
        markdown += (
            f"\n\n> **Missing placeholders:** {', '.join(f'`{{{{{p}}}}}`' for p in missing)}"
        )
    return format_response(
        markdown,
        build_decision(
            "fill_template",
            status,
            action,
            {
                "template_path": template_path,
                "filled_content": filled,
                "missing_placeholders": missing,
            },
        ),
        output_format,
    )


# ─── Session Tools ────────────────────────────────────────────────────────────


@mcp.tool()
def session_start(
    project_id: str, project_type: str, language: str = "nl", output_format: str = "markdown"
) -> str:
    """Start a new workflow session and return its session ID.

    Args:
        project_id: Caller-supplied project identifier.
        project_type: E.g. "NLP", "CV", "Recommender".
        language: "nl" (default) or "en".
        output_format: "markdown" (default) or "json".

    Next step: pass the returned session_id to session_record_artifact or gate_review_intake.
    """
    store = get_session_store()
    if store is None:
        return format_response(
            "Session store is not configured.",
            build_decision(
                "session_start",
                DecisionStatus.ERROR,
                "Session store not available.",
                {"session_id": None},
            ),
            output_format,
        )
    sid = store.create_session(project_id=project_id, project_type=project_type, language=language)
    markdown = (
        f"## Session Started\n\nSession ID: `{sid}`\n\nProject: {project_id} ({project_type})"
    )
    return format_response(
        markdown,
        build_decision(
            "session_start",
            DecisionStatus.OK,
            "Session created. Use session_id in subsequent calls.",
            {"session_id": sid, "project_id": project_id, "project_type": project_type},
        ),
        output_format,
    )


@mcp.tool()
def session_get_state(session_id: str, output_format: str = "markdown") -> str:
    """Retrieve the current state of a workflow session.

    Args:
        session_id: Session ID returned by session_start.
        output_format: "markdown" (default) or "json".

    Next step: use can_enter_phase with the completed_gates list, or gate_review_intake to progress.
    """
    store = get_session_store()
    if store is None:
        return format_response(
            "Session store is not configured.",
            build_decision(
                "session_get_state", DecisionStatus.ERROR, "Session store not available.", {}
            ),
            output_format,
        )
    state = store.get_state(session_id)
    if state is None:
        return format_response(
            f"Session `{session_id}` not found.",
            build_decision(
                "session_get_state",
                DecisionStatus.NOT_FOUND,
                "Session not found. Start a new session with session_start.",
                {"session_id": session_id},
            ),
            output_format,
        )
    markdown = (
        f"## Session State\n\n"
        f"**Project:** {state.project_id} ({state.project_type})\n"
        f"**Language:** {state.language}\n"
        f"**Completed gates:** {state.completed_gates or 'None'}\n"
        f"**Artifacts:** {len(state.artifacts)}"
    )
    data = {
        "session_id": state.session_id,
        "project_id": state.project_id,
        "project_type": state.project_type,
        "language": state.language,
        "completed_gates": state.completed_gates,
        "artifacts": state.artifacts,
        "extra": state.extra,
    }
    return format_response(
        markdown,
        build_decision("session_get_state", DecisionStatus.OK, "Session state retrieved.", data),
        output_format,
    )


@mcp.tool()
def session_record_artifact(
    session_id: str, artifact_type: str, artifact_path: str, output_format: str = "markdown"
) -> str:
    """Record an artifact in a workflow session.

    Args:
        session_id: Session ID returned by session_start.
        artifact_type: Type of artifact (e.g. "document", "test_result").
        artifact_path: Path or URL of the artifact.
        output_format: "markdown" (default) or "json".

    Next step: call gate_review_intake to include this artifact in a formal gate review.
    """
    store = get_session_store()
    if store is None:
        return format_response(
            "Session store is not configured.",
            build_decision(
                "session_record_artifact", DecisionStatus.ERROR, "Session store not available.", {}
            ),
            output_format,
        )
    state = store.get_state(session_id)
    if state is None:
        return format_response(
            f"Session `{session_id}` not found.",
            build_decision(
                "session_record_artifact",
                DecisionStatus.NOT_FOUND,
                "Session not found.",
                {"session_id": session_id},
            ),
            output_format,
        )
    store.record_artifact(session_id, artifact_type=artifact_type, artifact_path=artifact_path)
    markdown = f"## Artifact Recorded\n\n**Type:** {artifact_type}\n**Path:** {artifact_path}"
    return format_response(
        markdown,
        build_decision(
            "session_record_artifact",
            DecisionStatus.OK,
            "Artifact recorded in session.",
            {
                "session_id": session_id,
                "artifact_type": artifact_type,
                "artifact_path": artifact_path,
            },
        ),
        output_format,
    )


@mcp.tool()
def list_projects(output_format: str = "markdown") -> str:
    """List all projects (sessions) known to the session store.

    Args:
        output_format: "markdown" (default) or "json".

    Next step: call session_get_state with a specific session_id to inspect details.
    """
    store = get_session_store()
    if store is None:
        return format_response(
            "## Projects\n\nNo session store configured.",
            build_decision(
                "list_projects", DecisionStatus.OK, "No session store available.", {"projects": []}
            ),
            output_format,
        )
    sessions = store.list_sessions()
    if not sessions:
        markdown = "## Projects\n\nNo projects found."
    else:
        lines = ["## Projects\n"]
        for s in sessions:
            lines.append(
                f"- `{s['session_id']}` — **{s['project_id']}** ({s['project_type']}, {s['language']})"
            )
        markdown = "\n".join(lines)
    return format_response(
        markdown,
        build_decision(
            "list_projects",
            DecisionStatus.OK,
            "Use session_get_state to inspect a specific session.",
            {"projects": sessions},
        ),
        output_format,
    )


# ─── Tool Cheatsheet ──────────────────────────────────────────────────────────

_TOOL_CHEATSHEET: list[dict] = [
    # Discovery & search
    {
        "name": "answer_question",
        "category": "search",
        "when": "User asks a natural language question about the Blueprint",
        "next": "get_template or get_phase_guidance",
        "example": "How do I classify the risk of my AI project?",
    },
    {
        "name": "search_content",
        "category": "search",
        "when": "Keyword search with optional filters (type, phase, layer, tag)",
        "next": "answer_question or get_template",
        "example": "search_content('risk', type='guide', phase=1)",
    },
    {
        "name": "lookup_terminology",
        "category": "search",
        "when": "User asks what a term means (gate, guardian, HAS-H, etc.)",
        "next": "answer_question",
        "example": "What is a Gate Review?",
    },
    # Phase & guidance
    {
        "name": "get_phase_guidance",
        "category": "phase",
        "when": "User wants objectives / activities / deliverables for a lifecycle phase",
        "next": "get_template or check_gate_readiness",
        "example": "What do I need to do in phase 2?",
    },
    {
        "name": "get_guidance_for_profile",
        "category": "phase",
        "when": "Tailored guidance based on project type (A/B), risk level, phase, role",
        "next": "select_template",
        "example": "get_guidance_for_profile('B', 'amber', 2, role='Guardian')",
    },
    {
        "name": "can_enter_phase",
        "category": "phase",
        "when": "Check if a team has completed the required gates to enter a phase",
        "next": "get_phase_guidance",
        "example": "can_enter_phase(3, completed_gates=[1, 2])",
    },
    {
        "name": "get_workflow_status",
        "category": "phase",
        "when": "Overview of all available MCP workflows and their steps",
        "next": "any workflow tool",
        "example": "What workflows are available?",
    },
    # Templates
    {
        "name": "get_template",
        "category": "template",
        "when": "Retrieve a specific template by name",
        "next": "fill_template",
        "example": "get_template('gate-review')",
    },
    {
        "name": "get_template_for_context",
        "category": "template",
        "when": "Get recommended templates for a role + phase combination",
        "next": "fill_template",
        "example": "get_template_for_context('Guardian', 2)",
    },
    {
        "name": "template_advisor",
        "category": "template",
        "when": "User describes a need; tool recommends the right template",
        "next": "get_template or fill_template",
        "example": "I need to document my risk assessment",
    },
    {
        "name": "select_template",
        "category": "template",
        "when": "Keyword-scored template matching by goal, phase, role",
        "next": "fill_template",
        "example": "select_template('project charter', phase=1)",
    },
    {
        "name": "list_template_placeholders",
        "category": "template",
        "when": "Discover what {{placeholders}} a template contains before filling",
        "next": "fill_template",
        "example": "list_template_placeholders('09-sjablonen/...')",
    },
    {
        "name": "fill_template",
        "category": "template",
        "when": "Fill {{placeholders}} in a template with project-specific values",
        "next": "gate_review_intake",
        "example": "fill_template(path, {'project_name': 'Atlas', 'team': 'Alpha'})",
    },
    # Gate review workflow
    {
        "name": "gate_review_intake",
        "category": "gate",
        "when": "Step 1 of Gate Review — collect and type evidence items",
        "next": "gate_review_report",
        "example": "gate_review_intake(1, ['project charter', 'risk scan'])",
    },
    {
        "name": "gate_review_report",
        "category": "gate",
        "when": "Step 2 of Gate Review — generate Guardian-ready summary with Go/No-Go",
        "next": "session_record_artifact",
        "example": "gate_review_report(1, evidence, gaps)",
    },
    {
        "name": "check_gate_readiness",
        "category": "gate",
        "when": "Quick readiness check against gate checklist before formal review",
        "next": "gate_review_intake",
        "example": "check_gate_readiness(2, ['risk scan', 'stakeholder sign-off'])",
    },
    # Risk & compliance
    {
        "name": "classify_risk",
        "category": "risk",
        "when": "Classify a project's EU AI Act risk level (prohibited/high/limited/minimal)",
        "next": "compliance_checklist or get_guidance_for_profile",
        "example": "classify_risk('A fraud detection model used in credit scoring')",
    },
    {
        "name": "compliance_intake",
        "category": "risk",
        "when": "Step 1 of compliance workflow — gather project context for compliance check",
        "next": "compliance_checklist",
        "example": "compliance_intake('NLP model for HR screening')",
    },
    {
        "name": "compliance_checklist",
        "category": "risk",
        "when": "Step 2 — full compliance checklist based on risk level and phase",
        "next": "gate_review_intake",
        "example": "compliance_checklist('high', phase=2)",
    },
    # Project setup workflow
    {
        "name": "project_setup_intake",
        "category": "setup",
        "when": "Step 1 of project setup — capture initial project description",
        "next": "project_setup_risk",
        "example": "project_setup_intake('NLP chatbot for customer service')",
    },
    {
        "name": "project_setup_risk",
        "category": "setup",
        "when": "Step 2 — classify project risk and collaboration mode",
        "next": "project_setup_charter",
        "example": "project_setup_risk(description, answers)",
    },
    {
        "name": "project_setup_charter",
        "category": "setup",
        "when": "Step 3 — generate a project charter from intake + risk data",
        "next": "get_phase_guidance",
        "example": "project_setup_charter(context)",
    },
    # Context & validation
    {
        "name": "validate_project_context",
        "category": "setup",
        "when": "Validate that a context dict has enough info to start a workflow",
        "next": "recommended tool from decision data",
        "example": "validate_project_context({'description': '...', 'project_type': 'A'})",
    },
    {
        "name": "get_project_type",
        "category": "setup",
        "when": "Classify project as Type A (predictive) or Type B (generative/agentic)",
        "next": "classify_risk",
        "example": "get_project_type('GPT-based document summariser')",
    },
    {
        "name": "select_collaboration_mode",
        "category": "setup",
        "when": "Determine HAS-H collaboration level (1=Instrumental … 5=Autonomous)",
        "next": "project_setup_charter",
        "example": "select_collaboration_mode('High risk, minimal autonomy')",
    },
    # Session & state
    {
        "name": "session_start",
        "category": "session",
        "when": "Start a persistent workflow session to track gates and artifacts",
        "next": "any workflow tool with session_id",
        "example": "session_start('proj-1', 'NLP', 'nl')",
    },
    {
        "name": "session_get_state",
        "category": "session",
        "when": "Retrieve current state of an ongoing session",
        "next": "can_enter_phase or gate_review_intake",
        "example": "session_get_state(session_id)",
    },
    {
        "name": "session_record_artifact",
        "category": "session",
        "when": "Record a completed document or test result in a session",
        "next": "gate_review_intake",
        "example": "session_record_artifact(session_id, 'document', 'docs/charter.md')",
    },
    {
        "name": "list_projects",
        "category": "session",
        "when": "List all known projects/sessions in the store",
        "next": "session_get_state",
        "example": "list_projects()",
    },
    # Utility
    {
        "name": "get_tool_cheatsheet",
        "category": "utility",
        "when": "Agent needs to know which tool to call and when",
        "next": "any tool listed here",
        "example": "get_tool_cheatsheet(intent='gate')",
    },
    {
        "name": "reload_content",
        "category": "utility",
        "when": "Docs have been updated and the index needs refreshing",
        "next": "answer_question",
        "example": "reload_content()",
    },
]


@mcp.tool()
def get_tool_cheatsheet(intent: str = "", output_format: str = "markdown") -> str:
    """Return a structured guide to which tool to call and when.

    Helps agents navigate the 30+ available tools by mapping intents to
    the right tool, typical next step, and a usage example.

    Args:
        intent: Optional keyword to filter tools (e.g. "gate", "risk", "template",
                "search", "session", "phase"). Empty string returns all tools.
        output_format: "markdown" (default) or "json".
    """
    tools = _TOOL_CHEATSHEET
    if intent:
        lower = intent.lower()
        filtered = [
            t
            for t in tools
            if lower in t["category"] or lower in t["name"] or lower in t["when"].lower()
        ]
        tools = filtered if filtered else _TOOL_CHEATSHEET  # unknown intent → all

    # Build markdown table
    lines = ["## Blueprint MCP — Tool Selection Guide\n"]
    if intent and tools is not _TOOL_CHEATSHEET:
        lines.append(f"_Filtered by intent: **{intent}**_\n")

    lines.append("| Tool | When to use | Typical next tool |")
    lines.append("|---|---|---|")
    for t in tools:
        lines.append(f"| `{t['name']}` | {t['when']} | `{t['next']}` |")

    lines.append("\n### Usage examples\n")
    for t in tools[:8]:
        lines.append(f"- **`{t['name']}`**: `{t['example']}`")

    markdown = "\n".join(lines)
    return format_response(
        markdown,
        build_decision(
            "get_tool_cheatsheet",
            DecisionStatus.OK,
            "Use the table above to select the right tool for your intent.",
            {"intent": intent or "all", "tools": tools, "tool_count": len(tools)},
        ),
        output_format,
    )


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

    phase_names = {
        1: "Discovery",
        2: "Validation",
        3: "Development",
        4: "Delivery",
        5: "Monitoring",
    }
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
        mcp.settings.port = int(os.environ.get("BLUEPRINT_PORT", "8902"))
        # Behind a reverse proxy the Host header is the public domain, not localhost.
        # DNS-rebinding protection is not needed here; nginx handles security.
        mcp.settings.transport_security.enable_dns_rebinding_protection = False
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()
