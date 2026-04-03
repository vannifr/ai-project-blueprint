#!/usr/bin/env python3
"""Validate enriched frontmatter consistency across all docs/ files.

Checks:
1. Schema: all required fields present with valid values
2. Layer consistency: layer matches INFORMATION_ARCHITECTURE mapping
3. Phase consistency: phase matches directory-based expectations
4. NL/EN parity: EN files have identical metadata to their NL counterparts
5. Type consistency: type matches path-based conventions
6. Cross-references: roles and tags use only allowed values

Exit code 0 = all checks pass, 1 = errors found.

Usage:
    python scripts/validate_frontmatter.py
    python scripts/validate_frontmatter.py --verbose
"""

import argparse
import re
import sys
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs"

# ─── Valid values ─────────────────────────────────────────────────────────────
VALID_TYPES = {
    "objectives", "activities", "deliverables", "template", "cheatsheet",
    "index", "strategic", "compliance", "technical", "foundation",
    "guide", "playbook", "assessment", "reference", "meta", "faq", "pattern",
}

VALID_LAYERS = {1, 2, 3}

VALID_PHASES = {1, 2, 3, 4, 5}

VALID_ROLES = {
    "AI Product Manager", "Data Scientist", "Guardian",
    "Tech Lead", "Business Sponsor",
}

VALID_TAGS = {
    "risk", "gate-review", "eu-ai-act", "governance", "ethics",
    "monitoring", "mlops", "rag", "prompt-engineering", "security",
    "data", "validation", "agile", "cost", "vendor", "onboarding",
    "stakeholder", "traceability", "template", "quick-reference", "playbook",
}

# ─── Layer mapping (must match enrich_frontmatter.py) ─────────────────────────
DIR_LAYER = {
    "00-navigator": 1, "00-explorer-kit": 2, "00-strategisch-kader": 1,
    "01-ai-native-fundamenten": 1, "02-fase-ontdekking": 2,
    "03-fase-validatie": 2, "04-fase-ontwikkeling": 2,
    "05-fase-levering": 2, "06-fase-monitoring": 2,
    "07-compliance-hub": 3, "08-technische-standaarden": 3,
    "08-rollen-en-verantwoordelijkheden": 1, "09-sjablonen": 3,
    "10-doorlopende-verbetering": 2, "11-project-afsluiting": 2,
    "12-90-dagen-roadmap": 2, "13-organisatieprofielen": 1,
    "14-drie-tracks": 1, "15-accelerators": 2,
    "16-bronnen": 3, "17-bijlagen": 3, "termenlijst": 3,
}

DIR_PHASE = {
    "02-fase-ontdekking": 1, "03-fase-validatie": 2,
    "04-fase-ontwikkeling": 3, "05-fase-levering": 4,
    "06-fase-monitoring": 5,
}


# ─── Frontmatter parser ──────────────────────────────────────────────────────
def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter, handling lists and scalars."""
    if not content.startswith("---"):
        return {}

    end = content.find("---", 3)
    if end == -1:
        return {}

    fm = {}
    fm_text = content[3:end].strip()

    for line in fm_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue

        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()

        # Parse lists: [1, 2, 3] or ["a", "b"]
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                fm[key] = []
            else:
                items = [item.strip().strip('"').strip("'") for item in inner.split(",")]
                # Try to parse as int
                parsed = []
                for item in items:
                    try:
                        parsed.append(int(item))
                    except ValueError:
                        parsed.append(item)
                fm[key] = parsed
        elif value.startswith("'") and value.endswith("'"):
            fm[key] = value[1:-1]
        elif value.startswith('"') and value.endswith('"'):
            fm[key] = value[1:-1]
        elif value in ("true", "false"):
            fm[key] = value == "true"
        else:
            try:
                fm[key] = int(value)
            except ValueError:
                fm[key] = value

    return fm


# ─── Validation checks ───────────────────────────────────────────────────────
class ValidationResult:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: str, msg: str):
        self.errors.append(f"ERROR  {path}: {msg}")

    def warn(self, path: str, msg: str):
        self.warnings.append(f"WARN   {path}: {msg}")


def validate_file(filepath: Path, result: ValidationResult, verbose: bool = False):
    """Run all validation checks on a single file."""
    rel_path = str(filepath.relative_to(DOCS_ROOT))
    is_en = filepath.name.endswith(".en.md")

    content = filepath.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)

    # 1. Required field: versie
    if "versie" not in fm:
        result.error(rel_path, "missing required field 'versie'")

    # 2. Required field: type
    if "type" not in fm:
        result.error(rel_path, "missing required field 'type'")
    elif fm["type"] not in VALID_TYPES:
        result.error(rel_path, f"invalid type '{fm['type']}' — valid: {sorted(VALID_TYPES)}")

    # 3. Required field: layer
    if "layer" not in fm:
        result.error(rel_path, "missing required field 'layer'")
    elif fm["layer"] not in VALID_LAYERS:
        result.error(rel_path, f"invalid layer '{fm['layer']}' — valid: {sorted(VALID_LAYERS)}")

    # 4. Layer consistency with directory
    parts = rel_path.replace(".en.md", ".md").split("/")
    top_dir = parts[0] if len(parts) > 1 else ""
    if "layer" in fm and top_dir in DIR_LAYER:
        expected_layer = DIR_LAYER[top_dir]
        if fm["layer"] != expected_layer:
            result.error(rel_path, f"layer {fm['layer']} doesn't match directory expectation {expected_layer}")

    # 5. Phase validation
    if "phase" in fm:
        phases = fm["phase"]
        if not isinstance(phases, list):
            result.error(rel_path, f"'phase' must be a list, got {type(phases).__name__}")
        else:
            for p in phases:
                if p not in VALID_PHASES:
                    result.error(rel_path, f"invalid phase value {p}")

        # Phase consistency: files in phase dirs should include that phase
        if top_dir in DIR_PHASE and isinstance(phases, list):
            expected_phase = DIR_PHASE[top_dir]
            if expected_phase not in phases:
                result.error(rel_path, f"file in {top_dir} but phase {expected_phase} not in {phases}")

    # 6. Roles validation
    if "roles" in fm:
        roles = fm["roles"]
        if not isinstance(roles, list):
            result.error(rel_path, f"'roles' must be a list, got {type(roles).__name__}")
        else:
            for role in roles:
                if role not in VALID_ROLES:
                    result.error(rel_path, f"invalid role '{role}' — valid: {sorted(VALID_ROLES)}")

    # 7. Tags validation
    if "tags" in fm:
        tags = fm["tags"]
        if not isinstance(tags, list):
            result.error(rel_path, f"'tags' must be a list, got {type(tags).__name__}")
        else:
            for tag in tags:
                if tag not in VALID_TAGS:
                    result.error(rel_path, f"invalid tag '{tag}' — valid: {sorted(VALID_TAGS)}")

    # 8. NL/EN parity check (only for EN files)
    if is_en:
        nl_path = filepath.parent / filepath.name.replace(".en.md", ".md")
        if nl_path.exists():
            nl_fm = parse_frontmatter(nl_path.read_text(encoding="utf-8"))
            for field in ("type", "layer", "phase", "roles", "tags"):
                nl_val = nl_fm.get(field)
                en_val = fm.get(field)
                if nl_val != en_val:
                    result.error(rel_path, f"NL/EN mismatch on '{field}': NL={nl_val}, EN={en_val}")

    # 9. Phase files should have phase
    if top_dir in DIR_PHASE and "phase" not in fm:
        result.warn(rel_path, f"file in phase directory {top_dir} but no 'phase' field")

    # 10. Templates should have tags including 'template'
    if fm.get("type") == "template":
        tags = fm.get("tags", [])
        if isinstance(tags, list) and "template" not in tags:
            result.warn(rel_path, "type is 'template' but 'template' tag missing")

    # 11. Compliance / playbook docs with regulatory tags must have a sources block
    REGULATORY_TAGS = {"eu-ai-act", "security", "ethics", "validation"}
    REGULATED_TYPES = {"compliance", "playbook"}
    doc_type = fm.get("type", "")
    doc_tags = fm.get("tags", []) or []
    if (
        not is_en
        and doc_type in REGULATED_TYPES
        and isinstance(doc_tags, list)
        and any(t in REGULATORY_TAGS for t in doc_tags)
    ):
        # Check raw content for 'sources:' — the simple parser won't handle nested blocks
        if "sources:" not in content:
            result.warn(rel_path,
                        f"type '{doc_type}' with regulatory tags should have a 'sources:' block "
                        f"(run: python scripts/check_sources.py)")


def main():
    parser = argparse.ArgumentParser(description="Validate enriched frontmatter")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    result = ValidationResult()

    all_files = sorted(DOCS_ROOT.rglob("*.md"))
    for filepath in all_files:
        validate_file(filepath, result, verbose=args.verbose)

    # Report
    total = len(all_files)
    print(f"\n{'=' * 60}")
    print(f"  Frontmatter Validation Report")
    print(f"{'=' * 60}")
    print(f"  Files scanned:   {total}")
    print(f"  Errors:          {len(result.errors)}")
    print(f"  Warnings:        {len(result.warnings)}")
    print()

    if result.errors:
        print("  ERRORS:")
        for e in result.errors:
            print(f"    {e}")
        print()

    if result.warnings:
        print("  WARNINGS:")
        for w in result.warnings:
            print(f"    {w}")
        print()

    if not result.errors and not result.warnings:
        print("  ✓ All checks passed.")
        print()

    sys.exit(1 if result.errors else 0)


if __name__ == "__main__":
    main()
