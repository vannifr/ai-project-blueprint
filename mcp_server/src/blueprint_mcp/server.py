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
def answer_question(question: str) -> str:
    """Find the most relevant Blueprint page(s) for a user question.

    Searches across all document answers, summaries, and titles to find
    the best matches. Returns up to 3 results with summaries and full content
    of the top match.

    Args:
        question: Natural language question (e.g. "How do I classify the risk of my AI project?")
    """
    index = get_index()
    results = index.search_by_question(question, limit=3)

    if not results:
        # Fall back to keyword search
        results = index.search(question, limit=3)

    if not results:
        return f"No relevant pages found for: '{question}'"

    sections = []

    # Top result: full content
    top = results[0]
    summary_line = f"**Summary:** {top.summary}\n\n" if top.summary else ""
    answers_line = ""
    if top.answers:
        answers_line = "**Questions this page answers:**\n" + "\n".join(f"- {a}" for a in top.answers) + "\n\n"
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

    return "\n\n---\n\n".join(sections)


@mcp.tool()
def get_template_for_context(role: str, phase: int) -> str:
    """Get recommended templates for a specific role and lifecycle phase.

    Args:
        role: Role name (e.g. "AI Product Manager", "Guardian", "Tech Lead")
        phase: Lifecycle phase number (1-5)
    """
    index = get_index()

    templates = [
        d for d in index.docs
        if d.type == "template"
        and phase in d.phases
        and (not d.roles or role in d.roles)
    ]

    if not templates:
        # Broader search: any template for this phase
        templates = [d for d in index.docs if d.type == "template" and phase in d.phases]

    if not templates:
        return f"No templates found for role '{role}' in phase {phase}."

    phase_names = {1: "Discovery", 2: "Validation", 3: "Development", 4: "Delivery", 5: "Monitoring"}
    lines = [f"## Templates for {role} in Phase {phase} ({phase_names.get(phase, '')})\n"]

    for doc in templates:
        s = f": {doc.summary}" if doc.summary else ""
        lines.append(f"- **{doc.title}** (`{doc.path}`){s}")

    return "\n".join(lines)


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
def project_setup_intake(description: str) -> str:
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
    """
    index = get_index()

    # Fetch project type framework
    type_docs = index.get_phase_docs(1, "activities")
    if not type_docs:
        type_docs = [d for d in index.docs if "activiteiten" in d.path and "02-fase-ontdekking" in d.path]

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

    return (
        f"# Project Setup — Step 1: Intake\n\n"
        f"{type_section}\n\n"
        f"---\n\n"
        f"{_RISK_QUESTIONS}\n\n"
        f"---\n\n"
        f"**Next step:** Present the risk questions to the user, collect their B1/B2/B3 scores, "
        f"then call `project_setup_risk` with `description`, `project_type` (A or B), "
        f"and `risk_scores_b1`, `risk_scores_b2`, `risk_scores_b3`."
    )


@mcp.tool()
def project_setup_risk(
    description: str,
    project_type: str,
    risk_scores_b1: int,
    risk_scores_b2: int,
    risk_scores_b3: int,
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
    """
    index = get_index()

    total, colour, interpretation = _risk_level(risk_scores_b1, risk_scores_b2, risk_scores_b3)
    mode_guidance = _COLLAB_MODE_GUIDANCE.get(colour, _COLLAB_MODE_GUIDANCE["amber"])

    # Fetch HAS-H collaboration modes content
    has_h_docs = [d for d in index.docs if "has-h" in d.path.lower()]
    has_h_section = ""
    if has_h_docs:
        has_h_section = f"\n\n---\n\n## Collaboration Modes Reference\n\n{has_h_docs[0].body[:1500]}..."

    return (
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


@mcp.tool()
def project_setup_charter(
    description: str,
    project_type: str,
    risk_level: str,
    collaboration_mode: str,
    additional_context: str = "",
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
    """
    index = get_index()

    # Fetch the project charter template
    charter_docs = [
        d for d in index.docs
        if "project-charter" in d.path and d.type == "template"
    ]
    if not charter_docs:
        charter_docs = [d for d in index.docs if "project-charter" in d.path]

    if not charter_docs:
        return "Project Charter template not found in the index."

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

    return (
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
        f"> - Fill `Concept` using the project description: \"{description}\"\n"
        f"> - Leave team names, budget, and success criteria as `[placeholder]` "
        f"if not provided — ask the user.\n"
        f"> - Present the filled charter to the user for approval before proceeding to Gate 1."
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
        mcp.settings.port = int(os.environ.get("BLUEPRINT_PORT", "8902"))
        # Behind a reverse proxy the Host header is the public domain, not localhost.
        # DNS-rebinding protection is not needed here; nginx handles security.
        mcp.settings.transport_security.enable_dns_rebinding_protection = False
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()
