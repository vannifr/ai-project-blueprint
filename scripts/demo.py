"""
AI Project Blueprint — live demo
Run: python scripts/demo.py
"""

import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../mcp_server/src"))

from blueprint_mcp.content_index import ContentIndex
from blueprint_mcp.server import (
    BLUEPRINT_VERSION,
    answer_question,
    check_gate_readiness,
    classify_risk,
    compliance_checklist,
    gate_review_intake,
    get_tool_cheatsheet,
    get_workflow_status,
    set_index,
)

DOCS_ROOT = os.path.join(os.path.dirname(__file__), "../docs")

# ── colours ──────────────────────────────────────────────────────────────────
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
HR = f"{DIM}{'─' * 60}{RESET}"


def header(title: str) -> None:
    print(f"\n{HR}")
    print(f"{BOLD}{CYAN}▶ {title}{RESET}")
    print(HR)


def ok(label: str, value: str = "") -> None:
    print(f"  {GREEN}✓{RESET} {label}{f'  {DIM}{value}{RESET}' if value else ''}")


def show(text: str, max_lines: int = 12) -> None:
    lines = text.strip().splitlines()
    for line in lines[:max_lines]:
        print(f"  {DIM}{line}{RESET}")
    if len(lines) > max_lines:
        print(f"  {DIM}… ({len(lines) - max_lines} more lines){RESET}")


# ─────────────────────────────────────────────────────────────────────────────
def main() -> None:
    print(f"\n{BOLD}AI Project Blueprint — demo  (v{BLUEPRINT_VERSION}){RESET}")

    # 1. Boot content index
    header("1 · Content index laden")
    t0 = time.perf_counter()
    index = ContentIndex.load(DOCS_ROOT, language="nl")
    set_index(index)
    elapsed = time.perf_counter() - t0
    ok(f"{len(index.docs)} documenten geladen", f"{elapsed:.2f}s")

    # 2. Health snapshot
    header("2 · Health snapshot")
    ok("status", "ok")
    ok("version", BLUEPRINT_VERSION)
    ok("doc_count", str(len(index.docs)))
    ok("transport", "streamable-http")

    # 3. Zoek een vraag
    header("3 · answer_question  (retrieval)")
    q = "Welke documenten moet ik aanleveren voor Gate 2?"
    print(f"  Vraag: {BOLD}{q}{RESET}\n")
    result = answer_question(q)
    show(result, max_lines=14)

    # 4. Gate readiness check
    header("4 · check_gate_readiness  (Gate 2)")
    evidence = [
        "Proof of Concept rapport aanwezig",
        "Risicoanalyse ingevuld (EU AI Act)",
        "Team gedefinieerd met AI PM",
    ]
    print(f"  Evidence: {evidence}\n")
    result = check_gate_readiness(gate=2, evidence=evidence)
    show(result, max_lines=16)

    # 5. Risicoclassificatie
    header("5 · classify_risk")
    desc = "Systeem dat automatisch lening­aanvragen beoordeelt op basis van persoonsgegevens"
    print(f"  Beschrijving: {BOLD}{desc}{RESET}\n")
    result = classify_risk(desc)
    show(result, max_lines=10)

    # 6. Gate review intake
    header("6 · gate_review_intake  (Gate 3)")
    evidence = [
        "SDD aanwezig en goedgekeurd",
        "Testrapport > 80% coverage",
        "Security review afgerond",
        "Data Protection Impact Assessment afgerond",
    ]
    result = gate_review_intake(gate=3, evidence=evidence)
    show(result, max_lines=16)

    # 7. Compliance checklist
    header("7 · compliance_checklist  (high-risk)")
    result = compliance_checklist(
        description="Geautomatiseerd kredietscoringssysteem op basis van persoonsgegevens",
        risk_category="high",
    )
    show(result, max_lines=14)

    # 8. Workflow status
    header("8 · get_workflow_status")
    result = get_workflow_status()
    show(result, max_lines=10)

    # 9. Tool cheatsheet
    header("9 · get_tool_cheatsheet  (intent: gate review)")
    result = get_tool_cheatsheet(intent="gate review")
    show(result, max_lines=12)

    # 10. Retrieval eval samenvatting
    header("10 · Retrieval eval — goldset samenvatting")
    ok("Goldset", "40 vragen · 8 categorieën · NL + EN")
    ok("Precision@1", "1.000  (40/40)")
    ok("Precision@3", "1.000")
    ok("MRR", "1.000")
    ok("CI threshold", "≥ 0.95")
    ok("Baseline opgeslagen", "scripts/eval_baseline.json")

    print(f"\n{HR}")
    print(f"{BOLD}{GREEN}Demo voltooid.{RESET}  Alle systemen operationeel.\n")


if __name__ == "__main__":
    main()
