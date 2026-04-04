"""Structured decision dict and response wrapping for Blueprint MCP tools.

Every tool appends a fenced JSON block to its markdown output so that
calling agents can extract machine-readable decisions without parsing prose.

Usage::

    from blueprint_mcp.response_utils import build_decision, wrap_response, DecisionStatus

    decision = build_decision(
        tool="check_gate_readiness",
        status=DecisionStatus.OK,
        primary_action="Review the identified gaps before proceeding.",
        data={"gate": 1, "evidence_count": 2, "gaps": ["missing charter"]},
        next_tool="gate_review_report",
    )
    return wrap_response(markdown_text, decision)

Agents extract the JSON block with::

    import json
    json_part = result.split("```json\\n")[1].split("\\n```")[0]
    parsed = json.loads(json_part)
"""

import json


class DecisionStatus:
    OK = "ok"
    ERROR = "error"
    NOT_FOUND = "not_found"


def build_decision(
    tool: str,
    status: str,
    primary_action: str,
    data: dict,
    next_tool: str | None = None,
) -> dict:
    """Build a structured decision dict for a tool response.

    Args:
        tool: Name of the tool producing this response.
        status: One of DecisionStatus.OK / ERROR / NOT_FOUND.
        primary_action: One-line directive for the calling agent.
        data: Tool-specific structured fields (gate, gaps, risk_level, …).
        next_tool: Next tool to call in a workflow, or None.

    Returns:
        Dict with keys: tool, status, primary_action, data, next_tool.
    """
    return {
        "tool": tool,
        "status": status,
        "primary_action": primary_action,
        "data": data,
        "next_tool": next_tool,
    }


def wrap_response(markdown: str, decision: dict) -> str:
    """Append a fenced JSON decision block to a markdown string.

    The block is separated from the markdown by a horizontal rule so it
    renders cleanly in human-facing interfaces while remaining parseable
    by agents.

    Args:
        markdown: The human-readable markdown response.
        decision: A dict produced by build_decision().

    Returns:
        The combined string: markdown + separator + JSON block.
    """
    json_block = json.dumps(decision, ensure_ascii=False, indent=2)
    return f"{markdown}\n\n---\n\n```json\n{json_block}\n```"


def format_response(markdown: str, decision: dict, output_format: str = "markdown") -> str:
    """Format a tool response as markdown+JSON or pure JSON.

    Args:
        markdown: Human-readable prose response.
        decision: A dict produced by build_decision().
        output_format: ``"markdown"`` (default) appends a fenced JSON block;
            ``"json"`` returns only the decision dict as a JSON string.

    Returns:
        Combined markdown+JSON string, or a bare JSON string.

    Raises:
        ValueError: If output_format is not ``"markdown"`` or ``"json"``.
    """
    if output_format == "markdown":
        return wrap_response(markdown, decision)
    if output_format == "json":
        return json.dumps(decision, ensure_ascii=False, indent=2)
    raise ValueError(f"output_format must be 'markdown' or 'json', got '{output_format}'")
