#!/usr/bin/env python3
"""Retrieval quality evaluation against the goldset.

Measures how well answers: frontmatter routes real user questions to the
correct Blueprint page. Uses ContentIndex directly (no ChromaDB needed),
so this runs in CI without any external services.

Usage:
    python scripts/eval_retrieval.py                      # full report
    python scripts/eval_retrieval.py --threshold 0.75     # exit 1 if below
    python scripts/eval_retrieval.py --json               # machine-readable output
    python scripts/eval_retrieval.py --lang nl            # NL queries only
    python scripts/eval_retrieval.py --category compliance  # one category
    python scripts/eval_retrieval.py --compare scripts/eval_baseline.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "mcp_server" / "src"))

from blueprint_mcp.content_index import ContentIndex  # noqa: E402

# ─── Goldset ──────────────────────────────────────────────────────────────────
# Each entry: question → expected base path (without language suffix).
# Match logic: NL → path as-is, EN → path with .md → .en.md.
# Scoring: precision@1, precision@3, MRR.

GOLDSET: list[dict] = [
    # ── Gate deliverables ─────────────────────────────────────────────────────
    {
        "id": "gd-01",
        "question": "Welke documenten moet ik aanleveren voor Gate 1?",
        "lang": "nl",
        "expected": "02-fase-ontdekking/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "gd-02",
        "question": "Welke documenten moet ik aanleveren voor Gate 2?",
        "lang": "nl",
        "expected": "03-fase-validatie/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "gd-03",
        "question": "What documents do I need to deliver for Gate 2?",
        "lang": "en",
        "expected": "03-fase-validatie/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "gd-04",
        "question": "Welke opleveringen zijn vereist voor de go-live beslissing?",
        "lang": "nl",
        "expected": "05-fase-levering/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "gd-05",
        "question": "What are the required deliverables at Gate 4?",
        "lang": "en",
        "expected": "05-fase-levering/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "gd-06",
        "question": "Wat moet ik opleveren na de Discovery-fase?",
        "lang": "nl",
        "expected": "02-fase-ontdekking/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "gd-07",
        "question": "Which deliverables are mandatory for Gate 3?",
        "lang": "en",
        "expected": "04-fase-ontwikkeling/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    # ── Compliance & EU AI Act ────────────────────────────────────────────────
    {
        "id": "co-01",
        "question": "Welke EU AI Act-verplichtingen gelden voor high-risk systemen?",
        "lang": "nl",
        "expected": "07-compliance-hub/01-eu-ai-act/index.md",
        "category": "compliance",
    },
    {
        "id": "co-02",
        "question": "Is mijn AI-systeem high-risk onder de EU AI Act?",
        "lang": "nl",
        "expected": "07-compliance-hub/01-eu-ai-act/index.md",
        "category": "compliance",
    },
    {
        "id": "co-03",
        "question": "How do I classify the risk level of my AI system?",
        "lang": "en",
        "expected": "01-ai-native-fundamenten/05-risicoclassificatie.md",
        "category": "compliance",
    },
    {
        "id": "co-04",
        "question": "Hoe reageer ik op een AI-incident?",
        "lang": "nl",
        "expected": "07-compliance-hub/05-incidentrespons.md",
        "category": "compliance",
    },
    {
        "id": "co-05",
        "question": "What is red teaming in the context of AI safety?",
        "lang": "en",
        "expected": "07-compliance-hub/07-red-teaming.md",
        "category": "compliance",
    },
    {
        "id": "co-06",
        "question": "Hoe beheer ik risico's in een AI-project?",
        "lang": "nl",
        "expected": "07-compliance-hub/02-risicobeheer/index.md",
        "category": "compliance",
    },
    # ── Rollen & besluitvorming ───────────────────────────────────────────────
    {
        "id": "ro-01",
        "question": "Wat doet de Guardian in een AI-project?",
        "lang": "nl",
        "expected": "08-rollen-en-verantwoordelijkheden/index.md",
        "category": "roles",
    },
    {
        "id": "ro-02",
        "question": "Wie beslist de Go/No-Go bij een gate review?",
        "lang": "nl",
        "expected": "08-rollen-en-verantwoordelijkheden/besluitvormingsmatrix.md",
        "category": "roles",
    },
    {
        "id": "ro-03",
        "question": "Who decides the Go/No-Go in a gate review?",
        "lang": "en",
        "expected": "08-rollen-en-verantwoordelijkheden/besluitvormingsmatrix.md",
        "category": "roles",
    },
    {
        "id": "ro-04",
        "question": "Welke rollen zijn verplicht in een AI-projectteam?",
        "lang": "nl",
        "expected": "08-rollen-en-verantwoordelijkheden/index.md",
        "category": "roles",
    },
    {
        "id": "ro-05",
        "question": "How do I onboard a new AI project manager?",
        "lang": "en",
        "expected": "08-rollen-en-verantwoordelijkheden/04-ai-pm-onboarding.md",
        "category": "roles",
    },
    # ── Templates ─────────────────────────────────────────────────────────────
    {
        "id": "tp-01",
        "question": "Hoe vul ik een Project Charter in?",
        "lang": "nl",
        "expected": "09-sjablonen/01-project-charter/template.md",
        "category": "templates",
    },
    {
        "id": "tp-02",
        "question": "Wat is de RAG Design Canvas en hoe gebruik ik die?",
        "lang": "nl",
        "expected": "09-sjablonen/16-rag-design-canvas/template.md",
        "category": "templates",
    },
    {
        "id": "tp-03",
        "question": "How do I fill in the Gate Review checklist?",
        "lang": "en",
        "expected": "09-sjablonen/04-gate-reviews/checklist.md",
        "category": "templates",
    },
    {
        "id": "tp-04",
        "question": "Welke velden zijn verplicht in een Business Case?",
        "lang": "nl",
        "expected": "09-sjablonen/02-business-case/template.md",
        "category": "templates",
    },
    {
        "id": "tp-05",
        "question": "Hoe doe ik een risico pre-scan voor mijn AI-project?",
        "lang": "nl",
        "expected": "09-sjablonen/03-risicoanalyse/pre-scan.md",
        "category": "templates",
    },
    {
        "id": "tp-06",
        "question": "What is the Guardian Review template?",
        "lang": "en",
        "expected": "09-sjablonen/15-guardian-review/template.md",
        "category": "templates",
    },
    # ── Fase-activiteiten & doelstellingen ────────────────────────────────────
    {
        "id": "fa-01",
        "question": "Welke stappen voer ik uit in de validatiefase?",
        "lang": "nl",
        "expected": "03-fase-validatie/02-activiteiten.md",
        "category": "phase-activities",
    },
    {
        "id": "fa-02",
        "question": "What activities are part of the Discovery phase?",
        "lang": "en",
        "expected": "02-fase-ontdekking/02-activiteiten.md",
        "category": "phase-activities",
    },
    {
        "id": "fa-03",
        "question": "Hoe bewaak ik modelprestaties na ingebruikname?",
        "lang": "nl",
        "expected": "06-fase-monitoring/02-activiteiten.md",
        "category": "phase-activities",
    },
    {
        "id": "fa-04",
        "question": "Wanneer is de validatiefase succesvol afgerond?",
        "lang": "nl",
        "expected": "03-fase-validatie/01-doelstellingen.md",
        "category": "phase-activities",
    },
    {
        "id": "fa-05",
        "question": "What is the Specification-First pattern?",
        "lang": "en",
        "expected": "04-fase-ontwikkeling/05-sdd-patroon.md",
        "category": "phase-activities",
    },
    # ── Concepten ─────────────────────────────────────────────────────────────
    {
        "id": "kn-01",
        "question": "Wat zijn de vijf samenwerkingsmodi?",
        "lang": "nl",
        "expected": "00-strategisch-kader/06-has-h-niveaus.md",
        "category": "concepts",
    },
    {
        "id": "kn-02",
        "question": "What are the five Collaboration Modes?",
        "lang": "en",
        "expected": "00-strategisch-kader/06-has-h-niveaus.md",
        "category": "concepts",
    },
    {
        "id": "kn-03",
        "question": "Wat is een rode lijn in een AI-systeem?",
        "lang": "nl",
        "expected": "01-ai-native-fundamenten/01-definitie.md",
        "category": "concepts",
    },
    {
        "id": "kn-04",
        "question": "How does the AI project lifecycle work?",
        "lang": "en",
        "expected": "00-strategisch-kader/01-ai-levenscyclus.md",
        "category": "concepts",
    },
    {
        "id": "kn-05",
        "question": "Wat is het verschil tussen Type A en Type B project?",
        "lang": "nl",
        "expected": "00-strategisch-kader/01-ai-levenscyclus.md",
        "category": "concepts",
    },
    # ── Strategie & governance ────────────────────────────────────────────────
    {
        "id": "st-01",
        "question": "Hoe start ik een AI-project in 90 dagen?",
        "lang": "nl",
        "expected": "12-90-dagen-roadmap/index.md",
        "category": "strategy",
    },
    {
        "id": "st-02",
        "question": "Welk organisatieprofiel past bij mijn bedrijf?",
        "lang": "nl",
        "expected": "13-organisatieprofielen/index.md",
        "category": "strategy",
    },
    {
        "id": "st-03",
        "question": "How do I build an AI business case?",
        "lang": "en",
        "expected": "09-sjablonen/02-business-case/template.md",
        "category": "strategy",
    },
    {
        "id": "st-04",
        "question": "Hoe selecteer ik een AI-leverancier?",
        "lang": "nl",
        "expected": "09-sjablonen/14-vendor-management/01-selectie-framework.md",
        "category": "strategy",
    },
    # ── MCP & AI-tools ────────────────────────────────────────────────────────
    {
        "id": "mc-01",
        "question": "Hoe voeg ik de Blueprint MCP-server toe aan Claude Code?",
        "lang": "nl",
        "expected": "ai-tools/index.md",
        "category": "mcp",
    },
    {
        "id": "mc-02",
        "question": "Which MCP tools are available for compliance checks?",
        "lang": "en",
        "expected": "ai-tools/mcp-tools.md",
        "category": "mcp",
    },
]


# ─── Evaluation logic ─────────────────────────────────────────────────────────


def _expected_path(entry: dict, lang: str) -> str:
    """Return the actual path to match against for the given language."""
    base = entry["expected"]
    if lang == "en":
        return base.replace(".md", ".en.md")
    return base


def _matches(result_path: str, expected_path: str) -> bool:
    """Flexible match: exact or one contains the other."""
    return (
        result_path == expected_path or expected_path in result_path or result_path in expected_path
    )


def _search(index: ContentIndex, question: str, limit: int = 5) -> list:
    """Combined search: answers-based first, keyword second (deduplicated)."""
    seen: set[str] = set()
    results: list = []

    for doc in index.search_by_question(question, limit=limit):
        if doc.path not in seen:
            seen.add(doc.path)
            results.append(doc)

    if len(results) < limit:
        for doc in index.search(question, limit=limit):
            if doc.path not in seen:
                seen.add(doc.path)
                results.append(doc)
            if len(results) >= limit:
                break

    return results[:limit]


def _eval_entry(index: ContentIndex, entry: dict) -> dict:
    lang = entry["lang"]
    expected = _expected_path(entry, lang)
    hits = _search(index, entry["question"], limit=5)
    hit_paths = [h.path for h in hits]

    rank = next((i + 1 for i, p in enumerate(hit_paths) if _matches(p, expected)), None)

    return {
        "id": entry["id"],
        "question": entry["question"],
        "lang": lang,
        "category": entry["category"],
        "expected": expected,
        "rank": rank,
        "top3_paths": hit_paths[:3],
        "p1": rank == 1,
        "p3": rank is not None and rank <= 3,
        "rr": (1.0 / rank) if rank else 0.0,
    }


def run_eval(goldset: list[dict]) -> dict:
    nl_index = ContentIndex.load(REPO_ROOT / "docs", language="nl")
    en_index = ContentIndex.load(REPO_ROOT / "docs", language="en")

    results = []
    for entry in goldset:
        index = nl_index if entry["lang"] == "nl" else en_index
        results.append(_eval_entry(index, entry))

    n = len(results)
    precision_1 = sum(r["p1"] for r in results) / n
    precision_3 = sum(r["p3"] for r in results) / n
    mrr = sum(r["rr"] for r in results) / n

    by_category: dict[str, dict] = {}
    for r in results:
        cat = r["category"]
        by_category.setdefault(cat, []).append(r)
    cat_stats = {
        cat: {
            "n": len(items),
            "p1": round(sum(i["p1"] for i in items) / len(items), 3),
            "p3": round(sum(i["p3"] for i in items) / len(items), 3),
        }
        for cat, items in by_category.items()
    }

    return {
        "n": n,
        "precision_at_1": round(precision_1, 4),
        "precision_at_3": round(precision_3, 4),
        "mrr": round(mrr, 4),
        "by_category": cat_stats,
        "failures": [r for r in results if not r["p1"]],
        "results": results,
    }


# ─── Reporting ────────────────────────────────────────────────────────────────


def _delta_str(current: float, prev: float | None) -> str:
    if prev is None:
        return ""
    d = current - prev
    sign = "+" if d >= 0 else ""
    color = "\033[32m" if d > 0 else ("\033[31m" if d < 0 else "")
    reset = "\033[0m" if color else ""
    return f"  {color}({sign}{d:.3f}){reset}"


def print_report(report: dict, prev: dict | None = None) -> None:
    p = prev or {}
    print("\n\033[1m── Blueprint Retrieval Eval ─────────────────────────────\033[0m")
    print(f"  Questions : {report['n']}")
    print(
        f"  Precision@1 : \033[1m{report['precision_at_1']:.3f}\033[0m"
        f"{_delta_str(report['precision_at_1'], p.get('precision_at_1'))}"
    )
    print(
        f"  Precision@3 : {report['precision_at_3']:.3f}"
        f"{_delta_str(report['precision_at_3'], p.get('precision_at_3'))}"
    )
    print(f"  MRR         : {report['mrr']:.3f}" f"{_delta_str(report['mrr'], p.get('mrr'))}")

    print("\n\033[1m── By category ──────────────────────────────────────────\033[0m")
    for cat, stats in sorted(report["by_category"].items(), key=lambda x: x[1]["p1"]):
        filled = int(stats["p1"] * 10)
        bar = "\033[32m" + "█" * filled + "\033[90m" + "░" * (10 - filled) + "\033[0m"
        prev_cat = p.get("by_category", {}).get(cat, {})
        delta = _delta_str(stats["p1"], prev_cat.get("p1"))
        print(f"  {cat:<22} {bar}  p@1={stats['p1']:.2f}  p@3={stats['p3']:.2f}{delta}")

    if report["failures"]:
        print(
            f"\n\033[1m── Failures ({len(report['failures'])}) ──────────────────────────────────────\033[0m"
        )
        for r in sorted(report["failures"], key=lambda x: x["rr"], reverse=True):
            rank_str = f"rank={r['rank']}" if r["rank"] else "\033[31mnot found\033[0m"
            top = r["top3_paths"][0] if r["top3_paths"] else "—"
            print(f"  [{r['id']}] {r['question'][:55]:<55}  {rank_str}")
            print(f"         expected: {r['expected']}")
            print(f"         got:      {top}")
    print()


# ─── CLI ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate Blueprint retrieval quality.")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.0,
        metavar="FLOAT",
        help="Exit 1 if precision@1 is below this value.",
    )
    parser.add_argument(
        "--lang", choices=["nl", "en", "all"], default="all", help="Filter goldset by language."
    )
    parser.add_argument(
        "--category", default=None, help="Filter goldset by category (e.g. 'compliance')."
    )
    parser.add_argument(
        "--compare", metavar="PATH", help="Path to a previous JSON report for delta comparison."
    )
    parser.add_argument("--save", metavar="PATH", help="Save the JSON report to this path.")
    args = parser.parse_args()

    goldset = GOLDSET
    if args.lang != "all":
        goldset = [e for e in goldset if e["lang"] == args.lang]
    if args.category:
        goldset = [e for e in goldset if e["category"] == args.category]

    if not goldset:
        print("No goldset entries match the given filters.", file=sys.stderr)
        sys.exit(1)

    report = run_eval(goldset)

    prev = None
    if args.compare:
        compare_path = Path(args.compare)
        if compare_path.exists():
            prev = json.loads(compare_path.read_text())
        else:
            print(f"Warning: compare file not found: {args.compare}", file=sys.stderr)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report, prev)

    if args.save:
        Path(args.save).write_text(json.dumps(report, indent=2))
        print(f"Report saved to {args.save}")

    if args.threshold and report["precision_at_1"] < args.threshold:
        print(
            f"FAIL: precision@1 {report['precision_at_1']:.3f} < threshold {args.threshold:.2f}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
