#!/usr/bin/env python3
"""Enrich frontmatter of all docs/ markdown files with structured metadata.

Adds: type, phase, layer, roles, tags — based on INFORMATION_ARCHITECTURE.md
mappings and file path conventions.

Preserves all existing frontmatter fields (versie, description, pdf).
Only modifies .md files (NL source); .en.md files get identical metadata.

Usage:
    python scripts/enrich_frontmatter.py              # dry-run (default)
    python scripts/enrich_frontmatter.py --apply       # write changes
    python scripts/enrich_frontmatter.py --report      # CSV report only
"""

import argparse
import csv
import io
import re
import sys
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs"

# ─── Layer mapping from INFORMATION_ARCHITECTURE.md §4.1 ─────────────────────
DIR_LAYER = {
    "00-navigator": 1,
    "00-explorer-kit": 2,
    "00-strategisch-kader": 1,
    "01-ai-native-fundamenten": 1,
    "02-fase-ontdekking": 2,
    "03-fase-validatie": 2,
    "04-fase-ontwikkeling": 2,
    "05-fase-levering": 2,
    "06-fase-monitoring": 2,
    "07-compliance-hub": 3,
    "08-technische-standaarden": 3,
    "08-rollen-en-verantwoordelijkheden": 1,
    "09-sjablonen": 3,
    "10-doorlopende-verbetering": 2,
    "11-project-afsluiting": 2,
    "12-90-dagen-roadmap": 2,
    "13-organisatieprofielen": 1,
    "14-drie-tracks": 1,
    "15-accelerators": 2,
    "16-bronnen": 3,
    "17-bijlagen": 3,
    "termenlijst": 3,
}

# ─── Phase mapping (only for lifecycle phase directories) ─────────────────────
DIR_PHASE = {
    "02-fase-ontdekking": 1,
    "03-fase-validatie": 2,
    "04-fase-ontwikkeling": 3,
    "05-fase-levering": 4,
    "06-fase-monitoring": 5,
}

# ─── Template-phase relationships from INFORMATION_ARCHITECTURE.md §8 ────────
TEMPLATE_PHASES = {
    "01-project-charter": [1],
    "02-business-case": [2],
    "03-risicoanalyse": [1, 2],
    "04-gate-reviews": [1, 2, 3, 4, 5],
    "06-ai-native-artefacten": [1, 2, 3],
    "07-validatie-bewijs": [2, 3],
    "08-traceerbaarheid-links": [3, 4],
    "10-prompt-engineering": [3, 5],
    "11-privacy-data": [1, 2],
    "12-cheatsheets": [1, 2, 3, 4, 5],
    "13-project-dagboek": [1, 2, 3, 4, 5],
    "14-vendor-management": [2, 3],
    "15-guardian-review": [1, 2, 3, 4, 5],
    "16-rag-design-canvas": [3],
    "17-experiment-ticket": [1, 2],
    "18-modelgezondheid": [5],
}

# ─── Type detection rules ─────────────────────────────────────────────────────
def detect_type(rel_path: str, filename: str) -> str:
    """Determine file archetype from path and filename conventions."""
    parts = rel_path.split("/")

    # Special top-level files
    if filename == "index.md":
        return "index"
    if filename in ("release-notes.md", "feedback.md"):
        return "meta"
    if parts[0] == "index.md":
        return "index"

    # Navigator & Explorer Kit
    if parts[0] == "00-navigator":
        if "faq" in filename:
            return "faq"
        return "guide"
    if parts[0] == "00-explorer-kit":
        return "guide"

    # Phase directories: objectives / activities / deliverables
    if parts[0] in DIR_PHASE:
        if "doelstellingen" in filename:
            return "objectives"
        if "activiteiten" in filename:
            return "activities"
        if "afleveringen" in filename:
            return "deliverables"
        if "has-h-beoordeling" in filename:
            return "assessment"
        if "fast-lane" in filename:
            return "guide"
        if "sdd-patroon" in filename:
            return "pattern"
        if "drift-detectie" in filename:
            return "guide"
        if "risicoclassificatie" in filename:
            return "guide"
        if "traceerbaarheid" in filename:
            return "guide"
        if filename == "index.md":
            return "index"
        return "guide"

    # Templates
    if parts[0] == "09-sjablonen":
        if len(parts) > 1 and parts[1] == "12-cheatsheets":
            return "cheatsheet"
        if "template" in filename:
            return "template"
        if "checklist" in filename:
            return "template"
        if "pre-scan" in filename:
            return "template"
        if "modelkaart" in filename:
            return "template"
        if "doelkaart" in filename:
            return "template"
        if "validatierapport" in filename:
            return "template"
        if "privacyblad" in filename:
            return "template"
        if "overdracht-checklist" in filename:
            return "template"
        if filename == "index.md":
            return "index"
        return "template"

    # Strategic framework
    if parts[0] == "00-strategisch-kader":
        if "executive-summary" in filename:
            return "strategic"
        if "leeswijzer" in filename:
            return "guide"
        if "methodologie" in filename:
            return "strategic"
        return "strategic"

    # AI-Native foundations
    if parts[0] == "01-ai-native-fundamenten":
        return "foundation"

    # Compliance
    if parts[0] == "07-compliance-hub":
        if "playbook" in filename or "red-teaming" in filename:
            return "playbook"
        if "checklist" in filename:
            return "template"
        return "compliance"

    # Technical standards
    if parts[0] == "08-technische-standaarden":
        return "technical"

    # Roles
    if parts[0] == "08-rollen-en-verantwoordelijkheden":
        if "raci" in filename or "besluitvorming" in filename:
            return "template"
        if "onboarding" in filename:
            return "playbook"
        if "communicatie" in filename:
            return "playbook"
        return "guide"

    # Transformation modules
    if parts[0] in ("12-90-dagen-roadmap", "13-organisatieprofielen",
                     "14-drie-tracks", "15-accelerators"):
        if "beoordeling" in filename:
            return "assessment"
        return "strategic"

    # Continuous improvement & closure
    if parts[0] in ("10-doorlopende-verbetering", "11-project-afsluiting"):
        return "guide"

    # Reference
    if parts[0] in ("16-bronnen", "17-bijlagen"):
        return "reference"
    if parts[0] == "termenlijst":
        return "reference"

    return "guide"


# ─── Tag generation ───────────────────────────────────────────────────────────
TAG_KEYWORDS = {
    "risk": ["risico", "risk", "pre-scan"],
    "gate-review": ["gate", "review", "checklist"],
    "eu-ai-act": ["eu-ai-act", "ai-act", "compliance"],
    "governance": ["governance", "model", "besluitvorming"],
    "ethics": ["ethis", "guardian", "rode-lijnen"],
    "monitoring": ["drift", "monitoring", "gezondheid", "health"],
    "mlops": ["mlops", "pipeline", "ci-cd"],
    "rag": ["rag", "retrieval", "design-canvas"],
    "prompt-engineering": ["prompt"],
    "security": ["red-team", "safety", "incident", "security"],
    "data": ["data", "privacy", "privacyblad"],
    "validation": ["validatie", "bewijs", "evidence"],
    "agile": ["agile", "sprint", "retrospective", "kaizen"],
    "cost": ["kosten", "cost", "green-ai"],
    "vendor": ["vendor", "rfp", "contract"],
    "onboarding": ["onboarding", "explorer", "verkenner", "30-dagen"],
    "stakeholder": ["stakeholder", "communicatie", "raci"],
    "traceability": ["traceer", "trace"],
}


def generate_tags(rel_path: str, filename: str, file_type: str) -> list[str]:
    """Generate semantic tags based on path and filename."""
    tags = []
    search_text = (rel_path + " " + filename).lower()

    for tag, keywords in TAG_KEYWORDS.items():
        if any(kw in search_text for kw in keywords):
            tags.append(tag)

    # Add type-derived tags
    if file_type == "template":
        tags.append("template")
    if file_type == "cheatsheet":
        tags.append("quick-reference")
    if file_type == "playbook":
        tags.append("playbook")

    return sorted(set(tags))


# ─── Role detection ───────────────────────────────────────────────────────────
ROLE_KEYWORDS = {
    "AI Product Manager": ["project-charter", "business-case", "doelstellingen",
                           "activiteiten", "gate", "onboarding", "pm"],
    "Data Scientist": ["data", "model", "drift", "golden-set", "validatie",
                       "prompt-engineering", "rag"],
    "Guardian": ["ethis", "guardian", "compliance", "eu-ai-act", "risico",
                 "red-team", "safety", "rode-lijnen", "privacy"],
    "Tech Lead": ["mlops", "architectuur", "pipeline", "test-framework",
                  "cloud", "sdd", "technische"],
    "Business Sponsor": ["executive", "business-case", "baten", "90-dagen"],
}


def detect_roles(rel_path: str, filename: str) -> list[str]:
    """Detect relevant RACI roles based on content path."""
    roles = []
    search_text = (rel_path + " " + filename).lower()

    for role, keywords in ROLE_KEYWORDS.items():
        if any(kw in search_text for kw in keywords):
            roles.append(role)

    # Phase files are always relevant to AI PM
    parts = rel_path.split("/")
    if parts[0] in DIR_PHASE and "AI Product Manager" not in roles:
        roles.append("AI Product Manager")

    return sorted(roles)


# ─── Phase detection for templates ────────────────────────────────────────────
def detect_phases(rel_path: str) -> list[int] | None:
    """Detect lifecycle phases this file relates to."""
    parts = rel_path.split("/")

    # Direct phase directory
    if parts[0] in DIR_PHASE:
        return [DIR_PHASE[parts[0]]]

    # Template with known phase mapping
    if parts[0] == "09-sjablonen" and len(parts) > 1:
        template_dir = parts[1]
        if template_dir in TEMPLATE_PHASES:
            return TEMPLATE_PHASES[template_dir]

    # Monitoring-related content
    if "monitoring" in rel_path or "drift" in rel_path:
        return [5]

    # Continuous improvement spans all
    if parts[0] == "10-doorlopende-verbetering":
        return [1, 2, 3, 4, 5]

    # Project closure
    if parts[0] == "11-project-afsluiting":
        return [5]

    return None


# ─── Frontmatter parsing and writing ─────────────────────────────────────────
def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content.

    Returns (frontmatter_dict, body) where body includes everything after
    the closing ---.
    """
    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 3:]

    # Simple YAML parsing (no external deps)
    fm = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            # Strip quotes
            if value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            fm[key] = value

    return fm, body


def format_yaml_value(key: str, value) -> str:
    """Format a single YAML key-value pair."""
    if key == "versie":
        return f"versie: '{value}'"
    if key == "pdf":
        return f"pdf: {value}"
    if key == "description":
        # Preserve original quoting style
        if "'" in str(value):
            return f'description: "{value}"'
        return f"description: '{value}'"
    if isinstance(value, list):
        if all(isinstance(v, int) for v in value):
            items = ", ".join(str(v) for v in value)
        else:
            items = ", ".join(f'"{v}"' for v in value)
        return f"{key}: [{items}]"
    if isinstance(value, bool):
        return f"{key}: {str(value).lower()}"
    return f"{key}: {value}"


def build_frontmatter(existing: dict, new_fields: dict) -> str:
    """Build frontmatter string preserving existing fields and adding new ones."""
    lines = []

    # Preserve existing fields in original order
    ordered_keys = ["versie", "description", "pdf"]
    for key in ordered_keys:
        if key in existing:
            lines.append(format_yaml_value(key, existing[key]))

    # Add new enrichment fields in consistent order
    enrichment_order = ["type", "layer", "phase", "roles", "tags"]
    for key in enrichment_order:
        if key in new_fields and new_fields[key] is not None:
            value = new_fields[key]
            if isinstance(value, list) and len(value) == 0:
                continue  # Skip empty lists
            lines.append(format_yaml_value(key, value))

    return "---\n" + "\n".join(lines) + "\n---"


# ─── Main enrichment logic ───────────────────────────────────────────────────
def enrich_file(filepath: Path, dry_run: bool = True) -> dict:
    """Enrich a single file's frontmatter. Returns metadata dict."""
    rel_path = str(filepath.relative_to(DOCS_ROOT))
    filename = filepath.name

    # Skip EN files — they'll be handled alongside their NL counterpart
    if filename.endswith(".en.md"):
        return None

    content = filepath.read_text(encoding="utf-8")
    existing_fm, body = parse_frontmatter(content)

    # Determine the top-level directory
    parts = rel_path.split("/")
    top_dir = parts[0] if parts[0] != filename else ""

    # Special handling for root-level files
    if top_dir == "" or top_dir == filename:
        # index.md, feedback.md, release-notes.md
        file_type = "meta" if filename in ("feedback.md", "release-notes.md") else "index"
        layer = 1 if filename == "index.md" else 3
        phases = None
        roles = []
        tags = []
    else:
        file_type = detect_type(rel_path, filename)
        layer = DIR_LAYER.get(top_dir, 3)
        phases = detect_phases(rel_path)
        roles = detect_roles(rel_path, filename)
        tags = generate_tags(rel_path, filename, file_type)

    new_fields = {
        "type": file_type,
        "layer": layer,
        "phase": phases,
        "roles": roles if roles else None,
        "tags": tags if tags else None,
    }

    new_fm = build_frontmatter(existing_fm, new_fields)
    new_content = new_fm + body

    result = {
        "file": rel_path,
        "type": file_type,
        "layer": layer,
        "phase": phases,
        "roles": roles,
        "tags": tags,
        "changed": content != new_content,
    }

    if not dry_run and content != new_content:
        filepath.write_text(new_content, encoding="utf-8")

        # Also enrich the EN counterpart if it exists
        en_path = filepath.with_suffix(".en.md")
        if en_path.exists():
            en_content = en_path.read_text(encoding="utf-8")
            en_existing_fm, en_body = parse_frontmatter(en_content)
            en_new_fm = build_frontmatter(en_existing_fm, new_fields)
            en_new_content = en_new_fm + en_body
            if en_content != en_new_content:
                en_path.write_text(en_new_content, encoding="utf-8")

    return result


def main():
    parser = argparse.ArgumentParser(description="Enrich docs/ frontmatter")
    parser.add_argument("--apply", action="store_true", help="Write changes")
    parser.add_argument("--report", action="store_true", help="CSV report only")
    args = parser.parse_args()

    dry_run = not args.apply
    results = []

    # Process all NL markdown files
    for filepath in sorted(DOCS_ROOT.rglob("*.md")):
        if filepath.name.endswith(".en.md"):
            continue
        result = enrich_file(filepath, dry_run=dry_run)
        if result:
            results.append(result)

    if args.report:
        writer = csv.DictWriter(
            sys.stdout,
            fieldnames=["file", "type", "layer", "phase", "roles", "tags", "changed"],
        )
        writer.writeheader()
        for r in results:
            r["phase"] = str(r["phase"]) if r["phase"] else ""
            r["roles"] = "; ".join(r["roles"]) if r["roles"] else ""
            r["tags"] = "; ".join(r["tags"]) if r["tags"] else ""
            writer.writerow(r)
        return

    # Summary
    changed = sum(1 for r in results if r["changed"])
    total = len(results)
    mode = "DRY RUN" if dry_run else "APPLIED"

    print(f"\n{'=' * 60}")
    print(f"  Frontmatter Enrichment — {mode}")
    print(f"{'=' * 60}")
    print(f"  Total NL files scanned:  {total}")
    print(f"  Files to update:         {changed}")
    print(f"  Already up-to-date:      {total - changed}")
    print()

    # Type distribution
    type_counts = {}
    for r in results:
        t = r["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    print("  Type distribution:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {t:<20} {c:>3}")
    print()

    # Layer distribution
    layer_counts = {}
    for r in results:
        l = r["layer"]
        layer_counts[l] = layer_counts.get(l, 0) + 1
    print("  Layer distribution:")
    for l in sorted(layer_counts):
        label = {1: "Strategic", 2: "Operational", 3: "Toolkit"}[l]
        print(f"    Layer {l} ({label:<12}) {layer_counts[l]:>3}")
    print()

    if dry_run:
        print("  Run with --apply to write changes.")
    else:
        # Count EN files updated
        en_count = sum(
            1
            for r in results
            if r["changed"]
            and (DOCS_ROOT / r["file"]).with_suffix(".en.md").exists()
        )
        print(f"  EN files also updated:   {en_count}")

    print()


if __name__ == "__main__":
    main()
