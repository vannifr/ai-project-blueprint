# Implementatieplan v2 — Test-First

**Datum:** 2026-04-04
**Basis:** DoD v1.0 — 6 openstaande P1-items + answers: kwaliteitsverbetering
**Aanpak:** Red → Green → Refactor. Geen implementatie zonder falende test.

______________________________________________________________________

## Afhankelijkheidsgraaf

```
Sprint 1: eval_retrieval.py + goldset   ← ALLES hangt hiervan af
    ↓
Sprint 2: /health endpoint + version header  (testbare server-wijzigingen)
    ↓
Sprint 3: filler-pattern check in validate_docs.py
    ↓
Sprint 4: answers: curation op basis van eval-data
    ↓
Sprint 5: Docker healthchecks + ROLLBACK.md + uptime-monitoring  (ops)
```

Sprint 1 is de meetlaag. Zonder baseline weet je niet of Sprint 4 werkt.

______________________________________________________________________

## Sprint 1 — Retrieval Evaluatie (fundament)

### Wat

`scripts/eval_retrieval.py` + goldset van 60 vraag→pagina-paren.
Dit is zelf een testscript — TDD betekent hier: definieer eerst de goldset (de "gewenste output"), dan schrijf je het script dat die goldset runt, dan meet je de baseline.

### Stap 1.1 — Definieer de goldset

De goldset is de ground truth. Elke entry is: vraag → verwacht bestand (NL pad).

```python
# scripts/eval_retrieval.py  — goldset sectie

GOLDSET = [
    # ── Gate deliverables (hoogste prioriteit) ────────────────────────────────
    {
        "id": "g01",
        "question": "Welke documenten moet ik aanleveren voor Gate 1?",
        "lang": "nl",
        "expected": "02-fase-ontdekking/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "g02",
        "question": "Welke documenten moet ik aanleveren voor Gate 2?",
        "lang": "nl",
        "expected": "03-fase-validatie/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "g03",
        "question": "What documents do I need to deliver for Gate 2?",
        "lang": "en",
        "expected": "03-fase-validatie/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "g04",
        "question": "Welke opleveringen zijn vereist voor de ingebruikname?",
        "lang": "nl",
        "expected": "05-fase-levering/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    {
        "id": "g05",
        "question": "What are the required deliverables at Gate 4?",
        "lang": "en",
        "expected": "05-fase-levering/03-afleveringen.md",
        "category": "gate-deliverables",
    },
    # ── Compliance ────────────────────────────────────────────────────────────
    {
        "id": "c01",
        "question": "Welke EU AI Act-verplichtingen gelden voor high-risk systemen?",
        "lang": "nl",
        "expected": "07-compliance-hub/01-eu-ai-act/index.md",
        "category": "compliance",
    },
    {
        "id": "c02",
        "question": "Is mijn AI-systeem high-risk onder de EU AI Act?",
        "lang": "nl",
        "expected": "07-compliance-hub/01-eu-ai-act/index.md",
        "category": "compliance",
    },
    {
        "id": "c03",
        "question": "How do I classify the risk level of my AI system?",
        "lang": "en",
        "expected": "01-ai-native-fundamenten/05-risicoclassificatie.md",
        "category": "compliance",
    },
    {
        "id": "c04",
        "question": "Hoe reageer ik op een AI-incident?",
        "lang": "nl",
        "expected": "07-compliance-hub/05-incidentrespons.md",
        "category": "compliance",
    },
    {
        "id": "c05",
        "question": "What is red teaming in AI?",
        "lang": "en",
        "expected": "07-compliance-hub/07-red-teaming.md",
        "category": "compliance",
    },
    # ── Rollen ────────────────────────────────────────────────────────────────
    {
        "id": "r01",
        "question": "Wat doet de Guardian in een AI-project?",
        "lang": "nl",
        "expected": "08-rollen-en-verantwoordelijkheden/index.md",
        "category": "roles",
    },
    {
        "id": "r02",
        "question": "Wie beslist de Go/No-Go bij een gate review?",
        "lang": "nl",
        "expected": "08-rollen-en-verantwoordelijkheden/besluitvormingsmatrix.md",
        "category": "roles",
    },
    {
        "id": "r03",
        "question": "Who decides the Go/No-Go in a gate review?",
        "lang": "en",
        "expected": "08-rollen-en-verantwoordelijkheden/besluitvormingsmatrix.md",
        "category": "roles",
    },
    {
        "id": "r04",
        "question": "Welke rollen zijn verplicht in een AI-projectteam?",
        "lang": "nl",
        "expected": "08-rollen-en-verantwoordelijkheden/index.md",
        "category": "roles",
    },
    {
        "id": "r05",
        "question": "How do I onboard a new AI project manager?",
        "lang": "en",
        "expected": "08-rollen-en-verantwoordelijkheden/04-ai-pm-onboarding.md",
        "category": "roles",
    },
    # ── Templates ─────────────────────────────────────────────────────────────
    {
        "id": "t01",
        "question": "Hoe vul ik een Project Charter in?",
        "lang": "nl",
        "expected": "09-sjablonen/01-project-charter/template.md",
        "category": "templates",
    },
    {
        "id": "t02",
        "question": "Wat is de RAG Design Canvas?",
        "lang": "nl",
        "expected": "09-sjablonen/16-rag-design-canvas/template.md",
        "category": "templates",
    },
    {
        "id": "t03",
        "question": "How do I fill in the Gate Review checklist?",
        "lang": "en",
        "expected": "09-sjablonen/04-gate-reviews/checklist.md",
        "category": "templates",
    },
    {
        "id": "t04",
        "question": "Welke velden zijn verplicht in een Business Case?",
        "lang": "nl",
        "expected": "09-sjablonen/02-business-case/template.md",
        "category": "templates",
    },
    {
        "id": "t05",
        "question": "Hoe doe ik een risico pre-scan voor mijn AI-project?",
        "lang": "nl",
        "expected": "09-sjablonen/03-risicoanalyse/pre-scan.md",
        "category": "templates",
    },
    {
        "id": "t06",
        "question": "What is the Guardian Review template?",
        "lang": "en",
        "expected": "09-sjablonen/15-guardian-review/template.md",
        "category": "templates",
    },
    # ── Fase-activiteiten ─────────────────────────────────────────────────────
    {
        "id": "f01",
        "question": "Welke stappen voer ik uit in de validatiefase?",
        "lang": "nl",
        "expected": "03-fase-validatie/02-activiteiten.md",
        "category": "phase-activities",
    },
    {
        "id": "f02",
        "question": "What activities are part of the Discovery phase?",
        "lang": "en",
        "expected": "02-fase-ontdekking/02-activiteiten.md",
        "category": "phase-activities",
    },
    {
        "id": "f03",
        "question": "Hoe bewaak ik modelprestaties na ingebruikname?",
        "lang": "nl",
        "expected": "06-fase-monitoring/02-activiteiten.md",
        "category": "phase-activities",
    },
    {
        "id": "f04",
        "question": "Wanneer is de validatiefase succesvol afgerond?",
        "lang": "nl",
        "expected": "03-fase-validatie/01-doelstellingen.md",
        "category": "phase-objectives",
    },
    {
        "id": "f05",
        "question": "What is specification-first development?",
        "lang": "en",
        "expected": "04-fase-ontwikkeling/01-doelstellingen.md",
        "category": "phase-objectives",
    },
    # ── Concepten ─────────────────────────────────────────────────────────────
    {
        "id": "k01",
        "question": "Wat zijn de vijf samenwerkingsmodi?",
        "lang": "nl",
        "expected": "00-strategisch-kader/06-has-h-niveaus.md",
        "category": "concepts",
    },
    {
        "id": "k02",
        "question": "What are the five Collaboration Modes?",
        "lang": "en",
        "expected": "00-strategisch-kader/06-has-h-niveaus.md",
        "category": "concepts",
    },
    {
        "id": "k03",
        "question": "Wat is een rode lijn in een AI-systeem?",
        "lang": "nl",
        "expected": "01-ai-native-fundamenten/01-definitie.md",
        "category": "concepts",
    },
    {
        "id": "k04",
        "question": "How does the AI lifecycle work?",
        "lang": "en",
        "expected": "00-strategisch-kader/01-ai-levenscyclus.md",
        "category": "concepts",
    },
    {
        "id": "k05",
        "question": "Wat is het verschil tussen Type A en Type B project?",
        "lang": "nl",
        "expected": "00-strategisch-kader/01-ai-levenscyclus.md",
        "category": "concepts",
    },
    # ── Governance & strategie ────────────────────────────────────────────────
    {
        "id": "s01",
        "question": "Hoe start ik een AI-project in 90 dagen?",
        "lang": "nl",
        "expected": "12-90-dagen-roadmap/index.md",
        "category": "strategy",
    },
    {
        "id": "s02",
        "question": "Welk organisatieprofiel past bij mijn bedrijf?",
        "lang": "nl",
        "expected": "13-organisatieprofielen/index.md",
        "category": "strategy",
    },
    {
        "id": "s03",
        "question": "How do I build an AI business case?",
        "lang": "en",
        "expected": "09-sjablonen/02-business-case/template.md",
        "category": "strategy",
    },
    {
        "id": "s04",
        "question": "Hoe selecteer ik een AI-leverancier?",
        "lang": "nl",
        "expected": "09-sjablonen/14-vendor-management/01-selectie-framework.md",
        "category": "strategy",
    },
    # ── MCP & AI-tools ────────────────────────────────────────────────────────
    {
        "id": "m01",
        "question": "Hoe voeg ik de Blueprint MCP-server toe aan Claude?",
        "lang": "nl",
        "expected": "ai-tools/index.md",
        "category": "mcp",
    },
    {
        "id": "m02",
        "question": "Which MCP tools are available for gate reviews?",
        "lang": "en",
        "expected": "ai-tools/mcp-tools.md",
        "category": "mcp",
    },
]
```

### Stap 1.2 — Schrijf het eval-script

```python
# scripts/eval_retrieval.py

#!/usr/bin/env python3
"""Retrieval quality evaluation against the goldset.

Usage:
    python scripts/eval_retrieval.py                    # print report
    python scripts/eval_retrieval.py --json             # machine-readable
    python scripts/eval_retrieval.py --threshold 0.75   # exit 1 if below
    python scripts/eval_retrieval.py --compare baseline.json  # diff
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "mcp_server" / "src"))

from blueprint_mcp.content_index import ContentIndex

DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs"

# [goldset here — zie Stap 1.1]


def run_eval(index: ContentIndex, goldset: list[dict]) -> dict:
    results = []
    for entry in goldset:
        hits = index.search_by_question(entry["question"], limit=5)
        hit_paths = [h.path for h in hits]

        rank = None
        for i, path in enumerate(hit_paths):
            if entry["expected"] in path or path in entry["expected"]:
                rank = i + 1
                break

        results.append(
            {
                "id": entry["id"],
                "question": entry["question"],
                "lang": entry["lang"],
                "category": entry["category"],
                "expected": entry["expected"],
                "rank": rank,
                "hit_paths": hit_paths[:3],
                "p1": rank == 1,
                "p3": rank is not None and rank <= 3,
                "rr": (1 / rank) if rank else 0.0,
            }
        )

    n = len(results)
    precision_1 = sum(r["p1"] for r in results) / n
    precision_3 = sum(r["p3"] for r in results) / n
    mrr = sum(r["rr"] for r in results) / n

    return {
        "n": n,
        "precision_at_1": round(precision_1, 4),
        "precision_at_3": round(precision_3, 4),
        "mrr": round(mrr, 4),
        "by_category": _by_category(results),
        "failures": [r for r in results if not r["p1"]],
        "results": results,
    }


def _by_category(results: list[dict]) -> dict:
    cats = {}
    for r in results:
        cats.setdefault(r["category"], []).append(r)
    return {
        cat: {
            "n": len(items),
            "p1": round(sum(i["p1"] for i in items) / len(items), 2),
            "p3": round(sum(i["p3"] for i in items) / len(items), 2),
        }
        for cat, items in cats.items()
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--threshold", type=float, default=0.0)
    parser.add_argument("--lang", choices=["nl", "en", "all"], default="all")
    parser.add_argument("--compare", help="Path to previous JSON report for diff")
    args = parser.parse_args()

    lang = None if args.lang == "all" else args.lang
    index = ContentIndex.load(DOCS_ROOT, language=lang or "en")
    goldset = [e for e in GOLDSET if args.lang == "all" or e["lang"] == args.lang]

    report = run_eval(index, goldset)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        _print_report(report, args.compare)

    if args.threshold and report["precision_at_1"] < args.threshold:
        print(
            f"\nFAIL: precision@1 {report['precision_at_1']:.3f} < threshold {args.threshold}",
            file=sys.stderr,
        )
        sys.exit(1)


def _print_report(report: dict, compare_path: str | None):
    prev = None
    if compare_path:
        with open(compare_path) as f:
            prev = json.load(f)

    def _delta(key):
        if not prev:
            return ""
        d = report[key] - prev[key]
        return f"  ({'+' if d >= 0 else ''}{d:.3f})"

    print("\n── Blueprint Retrieval Eval ────────────────────────")
    print(f"  N questions : {report['n']}")
    print(f"  Precision@1 : {report['precision_at_1']:.3f}{_delta('precision_at_1')}")
    print(f"  Precision@3 : {report['precision_at_3']:.3f}{_delta('precision_at_3')}")
    print(f"  MRR         : {report['mrr']:.3f}{_delta('mrr')}")
    print()
    print("── By category ─────────────────────────────────────")
    for cat, stats in report["by_category"].items():
        bar = "█" * int(stats["p1"] * 10) + "░" * (10 - int(stats["p1"] * 10))
        print(f"  {cat:<22} {bar} p@1={stats['p1']:.2f}  p@3={stats['p3']:.2f}")
    if report["failures"]:
        print()
        print("── Failures (not in top-1) ──────────────────────────")
        for r in report["failures"]:
            rank_str = f"rank={r['rank']}" if r["rank"] else "not found"
            print(f"  [{r['id']}] {r['question'][:60]:<60}  {rank_str}")
    print()


if __name__ == "__main__":
    main()
```

### Stap 1.3 — CI-integratie

```yaml
# .github/workflows/ci.yml — nieuwe stap toevoegen na MCP tests:

- name: Retrieval quality check
  run: |
    pip install -e "mcp_server/[dev]"
    python scripts/eval_retrieval.py --threshold 0.75 --lang all
  env:
    PYTHONPATH: mcp_server/src
```

### Done-criteria Sprint 1

- [ ] Script draait zonder errors: `python scripts/eval_retrieval.py`
- [ ] Baseline-rapport opgeslagen als `scripts/eval_baseline.json`
- [ ] CI-stap toegevoegd (threshold tijdelijk op actuele score – 0.05 gezet, zodat CI niet direct faalt)
- [ ] Per-categorie breakdown zichtbaar — weten welke categorieën het slechtst scoren

______________________________________________________________________

## Sprint 2 — `/health` endpoint + version header

### Wat

MCP server krijgt een `/health` endpoint en een `X-Blueprint-Version` header op alle responses. Chatbot krijgt ook een `/health` endpoint.

### Stap 2.1 — Tests schrijven (EERST)

```python
# mcp_server/tests/test_health.py  — nieuw bestand

"""Tests for /health endpoint and API versioning headers.

Written before the implementation — these tests will fail until Sprint 2 is done.
"""

from __future__ import annotations

import re

import pytest
from fastapi.testclient import TestClient

from blueprint_mcp.server import mcp


@pytest.fixture(scope="module")
def client(content_index):
    """TestClient against the real MCP FastAPI app."""
    app = mcp.get_asgi_app()
    return TestClient(app)


class TestHealthEndpoint:
    def test_health_returns_200(self, client):
        resp = client.get("/health")
        assert resp.status_code == 200

    def test_health_body_has_status_ok(self, client):
        resp = client.get("/health")
        data = resp.json()
        assert data["status"] == "ok"

    def test_health_reports_doc_count(self, client):
        resp = client.get("/health")
        data = resp.json()
        assert "doc_count" in data
        assert data["doc_count"] >= 100  # sanity: we have 130+ pages

    def test_health_reports_version(self, client):
        resp = client.get("/health")
        data = resp.json()
        assert "version" in data
        assert re.match(r"\d+\.\d+", data["version"])

    def test_health_is_fast(self, client):
        """Health check must not do expensive work."""
        import time
        start = time.monotonic()
        client.get("/health")
        elapsed = time.monotonic() - start
        assert elapsed < 0.1, f"Health check took {elapsed:.3f}s — must be < 100ms"


class TestVersionHeader:
    def test_health_response_has_version_header(self, client):
        resp = client.get("/health")
        assert "X-Blueprint-Version" in resp.headers

    def test_version_header_format(self, client):
        resp = client.get("/health")
        version = resp.headers["X-Blueprint-Version"]
        assert re.match(r"\d+\.\d+", version), f"Bad version format: {version}"

    def test_mcp_sse_endpoint_has_version_header(self, client):
        """Every MCP response must carry the version header."""
        # SSE endpoint (streamable-http transport root)
        resp = client.get("/")
        assert "X-Blueprint-Version" in resp.headers


class TestHealthIntegration:
    def test_health_reflects_loaded_index(self, client, content_index):
        """Doc count in /health matches what ContentIndex loaded."""
        resp = client.get("/health")
        data = resp.json()
        # Allow small delta (language filtering)
        assert abs(data["doc_count"] - len(content_index.docs)) <= 10
```

### Stap 2.2 — Implementatie in server.py

```python
# mcp_server/src/blueprint_mcp/server.py — toevoegen

import os
from starlette.middleware.base import BaseHTTPMiddleware

BLUEPRINT_VERSION = "1.0"


class VersionHeaderMiddleware(BaseHTTPMiddleware):
    """Adds X-Blueprint-Version to every response."""

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Blueprint-Version"] = BLUEPRINT_VERSION
        return response


# In lifespan/app setup — na mcp = FastMCP(...):
mcp.add_middleware(VersionHeaderMiddleware)


# Nieuwe route — BUITEN @mcp.tool():
@mcp.custom_route("/health", methods=["GET"])
async def health(request) -> dict:
    """Health check endpoint for load balancers and Docker healthchecks."""
    index = get_index()
    return {
        "status": "ok",
        "version": BLUEPRINT_VERSION,
        "doc_count": len(index.docs) if index else 0,
        "transport": os.environ.get("BLUEPRINT_TRANSPORT", "streamable-http"),
    }
```

> **Opmerking:** De exacte FastMCP API voor custom routes aflezen uit de FastMCP documentatie. Als `custom_route` niet beschikbaar is, gebruik dan Starlette's `add_route` of een aparte FastAPI app gemounteerd op `/health`.

### Stap 2.3 — Chatbot /health (apart, in chatbot/src/)

```python
# chatbot/tests/test_health.py  — nieuw

def test_chatbot_health_returns_200(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "chroma_doc_count" in data
```

```python
# chatbot/src/blueprint_chat/app.py — toevoegen

@app.get("/health")
async def health():
    try:
        count = chroma_client.count()
    except Exception:
        count = -1
    return {"status": "ok", "chroma_doc_count": count}
```

### Done-criteria Sprint 2

- [ ] `test_health.py`: alle tests groen
- [ ] `GET /health` → 200 + JSON body met `status`, `version`, `doc_count`
- [ ] Elke MCP-response heeft `X-Blueprint-Version: 1.0` header
- [ ] Chatbot heeft eigen `/health` endpoint met ChromaDB count

______________________________________________________________________

## Sprint 3 — Filler-pattern check in validate_docs.py

### Wat

`validate_docs.py` blokkeert nieuwe pagina's met generieke `answers:` patterns. Pre-commit hook gooit een error (niet warning) bij overtreding.

### Stap 3.1 — Tests schrijven (EERST)

```python
# tests/test_validate_frontmatter.py — uitbreiden met nieuwe klasse

class TestAnswersQuality:
    """Tests for the new answers: quality checker."""

    GOOD_ANSWERS = [
        "Welke documenten moet ik aanleveren voor Gate 2?",
        "How do I classify the risk level of my AI system?",
        "Wanneer is de validatiefase succesvol afgerond?",
        "Who decides the Go/No-Go in a gate review?",
        "Hoe bereid ik een Gate 3 review voor?",
        "Which templates are required for phase 3?",
    ]

    BAD_ANSWERS = [
        "Wat is Gate Review?",
        "What is the Validation Phase?",
        "Wat bevat het onderdeel Rollen?",
        "What does the Compliance Hub section contain?",
        "Wat houdt Samenwerkingsmodi in?",
        "What does The Explorer entail?",
        "Hoe werkt Compliance Hub?",
        "How does Validation work?",
    ]

    def _check(self, answers: list[str]) -> list[str]:
        """Call the validate function directly — import from validate_docs."""
        from scripts.validate_docs import check_answers_quality  # to be implemented
        return check_answers_quality(answers)

    @pytest.mark.parametrize("answer", BAD_ANSWERS)
    def test_rejects_generic_answer(self, answer):
        errors = self._check([answer])
        assert errors, f"Should have rejected: {answer!r}"

    @pytest.mark.parametrize("answer", GOOD_ANSWERS)
    def test_accepts_specific_answer(self, answer):
        errors = self._check([answer])
        assert not errors, f"Should have accepted: {answer!r} — got: {errors}"

    def test_requires_minimum_two_answers(self):
        errors = self._check(["Welke documenten voor Gate 2?"])
        assert any("minimaal 2" in e.lower() or "minimum" in e.lower() for e in errors)

    def test_two_good_answers_pass(self):
        errors = self._check([
            "Welke documenten moet ik aanleveren voor Gate 2?",
            "Wanneer is de validatiefase afgerond?",
        ])
        assert not errors

    def test_one_good_one_bad_still_fails(self):
        errors = self._check([
            "Welke documenten voor Gate 2?",
            "Wat is Gate Review?",
        ])
        assert errors  # the bad one triggers an error

    def test_error_message_names_the_offending_answer(self):
        bad = "Wat is Gate Review?"
        errors = self._check([bad])
        assert any("Wat is Gate Review" in e for e in errors)
```

### Stap 3.2 — Implementatie in validate_docs.py

```python
# scripts/validate_docs.py — nieuwe functie toevoegen

import re

# Patterns that indicate a generic, non-discriminating answer
_FILLER_PATTERNS = [
    re.compile(r"^(Wat is|What is)\s+\w", re.IGNORECASE),
    re.compile(r"^(Wat bevat|What does .* contain|What does .* section contain)", re.IGNORECASE),
    re.compile(r"^(Wat houdt .* in|What does .* entail)", re.IGNORECASE),
    re.compile(r"^(Hoe werkt|How does .* work)\s+\w+\?$", re.IGNORECASE),
    re.compile(r"^(What is the .* section\?|What does .* include\?)", re.IGNORECASE),
]

_SPECIFIC_STARTERS = re.compile(
    r"^(Welke|Hoe |Wanneer|Wie|Wat zijn de|Wat moet|Wat gebeurt|"
    r"Which|How do|When|Who|What are the required|How should|"
    r"What happens|Why does|Can I)",
    re.IGNORECASE,
)

_MIN_ANSWERS = 2


def check_answers_quality(answers: list[str]) -> list[str]:
    """Return a list of error strings. Empty list = pass."""
    errors = []

    if len(answers) < _MIN_ANSWERS:
        errors.append(
            f"answers: bevat {len(answers)} vraag/vragen — minimaal {_MIN_ANSWERS} vereist"
        )

    for answer in answers:
        answer = answer.strip()
        for pattern in _FILLER_PATTERNS:
            if pattern.match(answer):
                errors.append(
                    f"Generieke answers: verboden patroon — '{answer}'. "
                    f"Gebruik een taakgerichte vraag (Welke/Hoe/Wanneer/Who/Which/How do)."
                )
                break

    return errors
```

Integreer `check_answers_quality` in de bestaande `validate_file()` functie — als error (niet warning) voor nieuwe bestanden, als warning voor bestaande bestanden gedurende de migratieperiode.

### Stap 3.3 — Pre-commit configuratie

```yaml
# .pre-commit-config.yaml — validate-frontmatter hook uitbreiden

- id: validate-frontmatter
  name: Validate frontmatter consistency
  # Bestaande hook krijgt de nieuwe check automatisch via validate_docs.py
  # Geen config-wijziging nodig als check_answers_quality in validate_file() zit
```

### Done-criteria Sprint 3

- [ ] `TestAnswersQuality`: alle 20+ parametrized tests groen
- [ ] `check_answers_quality` geëxporteerd vanuit `validate_docs.py`
- [ ] Nieuwe bestanden met `Wat is X?` worden geblokkeerd door pre-commit
- [ ] Bestaande bestanden krijgen warning (niet error) — zodat CI niet direct rood wordt

______________________________________________________________________

## Sprint 4 — answers: curation (data-driven)

### Wat

Gebruik de eval-baseline uit Sprint 1 om de pagina's te identificeren die het slechtst scoren. Curateer top-15 pagina's handmatig. Meet verbetering.

### Stap 4.1 — Baseline lezen

```bash
python scripts/eval_retrieval.py --json > scripts/eval_baseline_v1.0.json
```

Sorteer failures op categorie. Verwachte zwakste categorieën op basis van huidige `answers:` analyse:

- `gate-deliverables` — antwoorden zijn "Wat is Opleveringen?"
- `roles` — antwoorden zijn "Welke rollen heb ik nodig?" (te generiek)
- `concepts` — ontbreekt of generiek

### Stap 4.2 — Curateerprotocol per pagina

Voor elke pagina in de bottom-10 van precision@1:

1. Open het bestand
1. Lees de werkelijke inhoud (wat staat er echt?)
1. Stel jezelf voor: "Welke vraag zou een PM/tech lead stellen als hij dit document nodig heeft?"
1. Schrijf 2-3 vragen die:
    - Beginnen met een actiewoord of vraagwoord
    - De specifieke termen uit de pagina bevatten (Gate 2, niet "gate")
    - Passen bij de taakvraag, niet bij de paginatitel

**Verbodstabel:**

| Oud (verboden)                   | Nieuw (vereist)                                                                                |
| -------------------------------- | ---------------------------------------------------------------------------------------------- |
| `Wat is Opleveringen Validatie?` | `Welke documenten moet ik aanleveren voor Gate 2?`                                             |
| `Wat houdt Gate Review in?`      | `Hoe bereid ik een Gate 2 review voor?`, `Welke criteria hanteert de Guardian bij Gate 2?`     |
| `Hoe werkt Compliance Hub?`      | `Welke EU AI Act-verplichtingen gelden voor high-risk systemen?`                               |
| `Wat is Risicoclassificatie?`    | `Hoe classificeer ik mijn AI-systeem onder de EU AI Act?`, `Is mijn systeem high-risk?`        |
| `Welke rollen heb ik nodig?`     | `Wie beslist de Go/No-Go bij gate reviews?`, `Wat is de verantwoordelijkheid van de Guardian?` |

### Stap 4.3 — Verificatieprocedure per pagina

Na elke aanpassing van `answers:`:

```bash
# Test specifiek de pagina's die je net bijgewerkt hebt:
python scripts/eval_retrieval.py --json | python3 -c "
import json, sys
report = json.load(sys.stdin)
for r in report['failures']:
    print(r['id'], r['question'][:50], r.get('rank'))
"
```

Pas verder aan als de rank niet verbetert.

### Stap 4.4 — Doel

```bash
# Start: meten
python scripts/eval_retrieval.py --threshold 0.0  # baseline

# Na curation van 15 pagina's: target
python scripts/eval_retrieval.py --threshold 0.75  # moet slagen

# Vergelijken met baseline:
python scripts/eval_retrieval.py --compare scripts/eval_baseline_v1.0.json
```

### Done-criteria Sprint 4

- [ ] Precision@1 ≥ 0.75 op volledige goldset
- [ ] Precision@3 ≥ 0.90
- [ ] MRR ≥ 0.80
- [ ] `eval_retrieval.py --threshold 0.75` slaagt in CI
- [ ] Alle bijgewerkte pagina's slagen voor `check_answers_quality()`
- [ ] CI-threshold bijgesteld naar 0.75 (niet lager)

______________________________________________________________________

## Sprint 5 — Ops (Docker, Rollback, Monitoring)

### Stap 5.1 — Docker healthchecks

```yaml
# deploy/docker-compose.yml

services:
  chatbot:
    # ... bestaande config ...
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8901/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s

  mcp-server:
    # ... bestaande config ...
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8902/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 15s
```

**Verificatie (geen pre-commit, maar deploy-script check):**

```bash
# deploy/update.sh — toevoegen na docker compose up:

echo "Wachten op health checks..."
sleep 10
docker compose ps | grep "(healthy)" | wc -l | xargs -I{} test {} -eq 2 \
  || (echo "ERROR: Niet alle services healthy na deploy" && exit 1)
```

### Stap 5.2 — ROLLBACK.md

````markdown
# deploy/ROLLBACK.md

## Rollback procedure

### Snel terugdraaien (< 5 minuten)

1. Vorige image terugzetten:
   ```bash
   cd deploy
   git log --oneline -5  # vind de vorige commit
   git checkout <vorige-commit> -- docker-compose.yml
   docker compose up -d --build
````

1. Verifieer:
    ```bash
    curl -f https://ai-delivery.io/health
    curl -f https://ai-delivery.io/mcp/health
    ```

### Rollback documentatie-update (mkdocs)

```bash
cd /path/to/site
git checkout <vorige-commit>
mkdocs build
# nginx serveert uit site/ — geen herstart nodig
```

### Wanneer rollback uitvoeren

- `/health` geeft niet-200 na deploy
- Uptime-monitor triggered alert binnen 5 minuten
- Retrieval eval scoort \< 0.65 precision@1 in productie

````

### Stap 5.3 — Uptime monitoring

Configureer op **UptimeRobot** (gratis tier):

| Monitor | URL | Interval | Alert |
|---------|-----|----------|-------|
| Blueprint Assistent | `https://ai-delivery.io/health` | 5 min | E-mail |
| MCP Server | `https://ai-delivery.io/mcp/health` | 5 min | E-mail |
| Docs site | `https://ai-delivery.io/` | 10 min | E-mail |

Stel status page in op `https://status.ai-delivery.io` (UptimeRobot gratis public status page).

### Stap 5.4 — Version header in MCP endpoint (publiek)

Voeg toe aan `deploy/nginx-ai-delivery.conf`:

```nginx
# Doorstuuren van de version header naar clients:
location /mcp {
    proxy_pass http://127.0.0.1:8902;
    proxy_set_header Host $host;
    add_header X-Blueprint-Version "1.0" always;
}
````

### Done-criteria Sprint 5

- [ ] `docker compose ps` toont `(healthy)` voor beide services na deploy
- [ ] `deploy/ROLLBACK.md` bestaat en is getest (droge run)
- [ ] UptimeRobot monitort 3 endpoints met e-mail alerting
- [ ] `curl -I https://ai-delivery.io/mcp` toont `X-Blueprint-Version: 1.0`

______________________________________________________________________

## Overzicht — alle CI-gates na alle sprints

```yaml
# .github/workflows/ci.yml — volledige volgorde

jobs:
  quality:
    steps:
      - name: Lint & format (ruff)
        run: ruff check . && ruff format --check .

      - name: Validate documentation
        run: python scripts/validate_docs.py  # 0 errors

      - name: Build docs (strict)
        run: mkdocs build --strict

      - name: MCP server tests
        run: |
          pip install -e "mcp_server/[dev]"
          python -m pytest mcp_server/tests/ -q --tb=short

      - name: Retrieval quality check       # nieuw Sprint 1
        run: python scripts/eval_retrieval.py --threshold 0.75

      - name: Pre-commit (all files)
        run: pre-commit run --all-files
```

______________________________________________________________________

## Testpiramide — eindtoestand

```
                    ┌──────────────────────┐
                    │  eval_retrieval.py   │  ← 60 goldset entries (S1)
                    │  (end-to-end, slow)  │     ~10s in CI
                    └──────────────────────┘
               ┌──────────────────────────────────┐
               │  mcp_server/tests/ (487+ tests)  │  ← unit + integratie
               │  + test_health.py (S2)           │     ~30s in CI
               └──────────────────────────────────┘
          ┌────────────────────────────────────────────┐
          │  tests/ (validate_docs, blueprint_lint,    │  ← scripts unit tests
          │  check_sources, validate_frontmatter + S3) │     ~15s in CI
          └────────────────────────────────────────────┘
     ┌──────────────────────────────────────────────────────┐
     │  pre-commit hooks (ruff, mdformat, debug-statements) │  ← per commit
     └──────────────────────────────────────────────────────┘
```

Totale CI-tijd na alle sprints: ~60-90 seconden. Acceptabel.

______________________________________________________________________

## Volgorde van uitvoering

```
Week 1:
  Ma: Sprint 1 — goldset definiëren + eval_retrieval.py schrijven
  Di: Sprint 1 — baseline meten, CI-integratie
  Wo: Sprint 2 — test_health.py schrijven (RED), /health implementeren (GREEN)
  Do: Sprint 2 — version header + chatbot health
  Vr: Sprint 3 — TestAnswersQuality schrijven (RED), check_answers_quality (GREEN)

Week 2:
  Ma-Wo: Sprint 4 — answers: curation op worst-performing pages, eval per batch
  Do: Sprint 4 — eval ≥ 0.75 bereikt, CI-threshold instellen
  Vr: Sprint 5 — Docker healthchecks + ROLLBACK.md

Week 3:
  Ma: Sprint 5 — UptimeRobot configureren, status page
  Di: Volledige DoD-verificatie — alle checkboxen
  Wo: Release v1.6 met CHANGELOG-entry
```
