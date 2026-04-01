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


# ─── Gate Review Agent ────────────────────────────────────────────────────────


@mcp.tool()
def gate_review_intake(gate: int, evidence: list[str]) -> str:
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
    """
    if gate not in range(1, 5):
        return f"Error: gate must be 1–4, got {gate}"

    index = get_index()

    # Fetch gate checklist
    checklist_docs = [
        d for d in index.docs
        if "gate-review" in d.path.lower() or ("gate" in d.path.lower() and "checklist" in d.path.lower())
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
            item = line.lstrip("- [ ]").lstrip("- [x]").strip()
            if not any(word in evidence_lower for word in item.lower().split() if len(word) > 4):
                gaps.append(item)

    gaps_str = "\n".join(f"- {g}" for g in gaps[:8]) if gaps else "_(no obvious gaps detected — verify manually)_"

    return (
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


@mcp.tool()
def gate_review_report(gate: int, evidence: list[str], gaps: list[str]) -> str:
    """Step 2 of the Gate Review workflow: generate a Guardian-ready review summary.

    Call this ONLY after running gate_review_intake (Step 1) and confirming
    evidence and gaps with the user.

    Returns a structured gate review summary the Guardian can use to make
    a Go / No-Go decision.

    Args:
        gate: Gate number (1–4)
        evidence: Confirmed list of available evidence items
        gaps: Confirmed list of gaps or missing items (empty list = no gaps)
    """
    if gate not in range(1, 5):
        return f"Error: gate must be 1–4, got {gate}"

    gate_names = {1: "Go/No-Go Discovery", 2: "Pilot Investment", 3: "Production-Ready", 4: "Go-Live"}
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

    return (
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


# ─── Template Advisor ──────────────────────────────────────────────────────────


@mcp.tool()
def template_advisor(role: str, phase: int, context: str = "") -> str:
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
    """
    if phase not in range(1, 6):
        return f"Error: phase must be 1–5, got {phase}"

    index = get_index()
    phase_names = {1: "Discovery", 2: "Validation", 3: "Development", 4: "Delivery", 5: "Monitoring"}
    phase_label = phase_names.get(phase, f"Phase {phase}")

    # Role + phase match first
    templates = [
        d for d in index.docs
        if d.type == "template" and phase in d.phases and (not d.roles or role in d.roles)
    ]
    # Broaden if no role match
    if not templates:
        templates = [d for d in index.docs if d.type == "template" and phase in d.phases]

    if not templates:
        return f"No templates found for {role} in phase {phase} ({phase_label})."

    context_note = f"\n\n**Project context:** {context}" if context else ""

    sections = [
        f"# Template Advisor — {role} / Phase {phase}: {phase_label}{context_note}\n\n"
        f"The following templates are recommended for your role and phase. "
        f"Each template is shown in full — fill in the `[placeholder]` fields.\n"
    ]

    for doc in templates:
        sections.append(_format_doc_full(doc))

    return "\n\n---\n\n".join(sections)


# ─── Compliance Agent ──────────────────────────────────────────────────────────


_EU_RISK_KEYWORDS = {
    "unacceptable": [
        "social scor", "subliminal", "manipulat", "biometric categor",
        "real-time biometric", "emotion recognit", "exploit vulnerabl",
    ],
    "high": [
        "hire", "hiring", "recruit", "cv screen", "employment", "credit scor",
        "loan", "insurance", "law enforcement", "border", "migration", "asylum",
        "critical infrastructure", "energy grid", "water supply", "transport",
        "education admission", "exam", "welfare benefit", "social service",
        "medical device", "safety component",
    ],
    "limited": [
        "chatbot", "virtual assistant", "deepfake", "synthetic content",
        "emotion detect", "ai-generated", "customer service bot",
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
def compliance_intake(description: str) -> str:
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
    """
    index = get_index()

    heuristic_category = _classify_eu_risk(description)

    # Fetch EU AI Act overview
    eu_docs = [
        d for d in index.docs
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

    return (
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


@mcp.tool()
def compliance_checklist(description: str, risk_category: str) -> str:
    """Step 2 of the Compliance workflow: generate a specific EU AI Act compliance checklist.

    Call this ONLY after compliance_intake (Step 1) and user confirmation of the risk category.

    Returns a concrete checklist with EU AI Act article references tailored to
    the system description and risk category.

    Args:
        description: Free-text description of the AI system
        risk_category: Confirmed risk category: "unacceptable", "high", "limited", or "minimal"
    """
    index = get_index()

    category = risk_category.lower().strip()

    if category == "unacceptable":
        return (
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

    # Fetch detailed compliance content
    compliance_docs = [d for d in index.docs if "07-compliance-hub" in d.path and "eu-ai-act" in d.path]
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

    extra_content = f"\n\n---\n\n## Detailed Blueprint Compliance Reference\n\n{checklist_content}" if checklist_content else ""

    return (
        f"# Compliance Checklist — {risk_category.capitalize()} Risk\n\n"
        f"**System:** {description}\n\n"
        f"---\n\n"
        f"{specific_checklist}"
        f"{extra_content}\n\n"
        f"---\n\n"
        f"> Review each item with your Guardian and legal counsel. "
        f"High-risk systems require conformity assessment before deployment."
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
