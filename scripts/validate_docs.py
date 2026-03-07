#!/usr/bin/env python3
"""
Documentation Quality Validation Script
Catches common quality issues in markdown documentation.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple  # noqa: F401


class ValidationError:
    def __init__(self, severity: str, file: str, line: int, message: str):
        self.severity = severity
        self.file = file
        self.line = line
        self.message = message

    def __str__(self):
        return f"{self.severity}: {self.file}:{self.line} - {self.message}"


def check_duplicate_parenthetical_text(filepath: str, content: List[str]) -> List[ValidationError]:
    """Detect repeated parenthetical text like '(text) (text) (text)'."""
    errors = []

    for i, line in enumerate(content, 1):
        # Find all parenthetical text
        matches = re.findall(r'\(([^)]+)\)', line)
        if matches:
            # Check for duplicates
            for text in set(matches):
                count = matches.count(text)
                if count >= 3:  # 3 or more repetitions is suspicious
                    errors.append(ValidationError(
                        "ERROR",
                        filepath,
                        i,
                        f"Text '{text}' repeated {count} times in parentheses"
                    ))

    return errors


def check_duplicate_words_in_headings(filepath: str, content: List[str]) -> List[ValidationError]:
    """Detect duplicate words in headings like 'Sjablonen & Sjablonen'."""
    errors = []

    for i, line in enumerate(content, 1):
        if line.startswith('#'):
            # Remove heading markers and emojis
            heading_text = re.sub(r'^#+\s*', '', line)
            heading_text = re.sub(r'[\U0001F300-\U0001F9FF]', '', heading_text).strip()

            # Split on common separators
            words = re.split(r'[&/\-\s]+', heading_text)
            words = [w.lower().strip() for w in words if w.strip()]

            # Check for consecutive duplicates
            for j in range(len(words) - 1):
                if words[j] == words[j + 1] and len(words[j]) > 3:
                    errors.append(ValidationError(
                        "WARNING",
                        filepath,
                        i,
                        f"Duplicate word '{words[j]}' in heading"
                    ))

    return errors


def check_frontmatter(filepath: str, content: List[str]) -> List[ValidationError]:
    """Verify YAML frontmatter exists and has required fields."""
    errors = []

    if not content or not content[0].strip() == '---':
        errors.append(ValidationError(
            "ERROR",
            filepath,
            1,
            "Missing YAML frontmatter (should start with ---)"
        ))
        return errors

    # Extract frontmatter
    frontmatter_lines = []
    in_frontmatter = False
    end_line = 0

    for i, line in enumerate(content):
        if i == 0 and line.strip() == '---':
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == '---':
                end_line = i + 1
                break
            frontmatter_lines.append(line)

    frontmatter_text = ''.join(frontmatter_lines)

    # Check required fields
    required_fields = ['versie']
    for field in required_fields:
        if f'{field}:' not in frontmatter_text:
            errors.append(ValidationError(
                "ERROR",
                filepath,
                end_line,
                f"Missing required frontmatter field: {field}"
            ))

    return errors


def check_spelling_consistency(filepath: str, content: List[str]) -> List[ValidationError]:
    """Check for common spelling inconsistencies."""
    errors = []

    # Common misspellings or inconsistencies
    patterns = {
        r'\bheruitving\b': 'heruitvinding',
    }

    full_text = ''.join(content)

    for pattern, correction in patterns.items():
        if re.search(pattern, full_text, re.IGNORECASE):
            # Find line number
            for i, line in enumerate(content, 1):
                if re.search(pattern, line, re.IGNORECASE):
                    errors.append(ValidationError(
                        "WARNING",
                        filepath,
                        i,
                        f"Possible misspelling: found pattern matching '{pattern}', should be '{correction}'"
                    ))
                    break

    return errors


def check_h1_presence(filepath: str, content: List[str]) -> List[ValidationError]:
    """Verify every page has at least one H1 heading."""
    errors = []
    h1_count = sum(1 for line in content if re.match(r'^# ', line))
    if h1_count == 0:
        errors.append(ValidationError(
            "ERROR",
            filepath,
            1,
            "Page has no H1 heading (# Title) — required for PDF running header and bookmarks"
        ))
    return errors


def check_debug_markers(filepath: str, content: List[str]) -> List[ValidationError]:
    """Detect development artifacts left in headings.

    Flags markers only when they appear in parentheses (e.g. '(NOT DONE)', '(TODO)')
    to avoid false positives on legitimate content like 'De "NOT DONE" Lijst'.
    """
    errors = []
    # Match markers inside parentheses: (NOT DONE), (TODO), (FIXME), (TBD), (WIP), (PLACEHOLDER)
    pattern = re.compile(r'\((NOT DONE|TODO|FIXME|TBD|WIP|PLACEHOLDER)\)', re.IGNORECASE)
    for i, line in enumerate(content, 1):
        if line.startswith('#'):
            match = pattern.search(line)
            if match:
                errors.append(ValidationError(
                    "ERROR",
                    filepath,
                    i,
                    f"Debug marker '({match.group(1)})' found in heading — remove before publishing"
                ))
    return errors


def check_stub_pdf_exclusion(filepath: str, content: List[str]) -> List[ValidationError]:
    """Stub/placeholder pages should have pdf: false in frontmatter."""
    errors = []
    stub_phrases = [
        'Inhoud volgt nog', 'wordt uitgewerkt in een toekomstige versie',
        'This page is being translated',
    ]
    full_text = ''.join(content)

    is_stub = any(phrase in full_text for phrase in stub_phrases)
    if not is_stub:
        return errors

    # Extract frontmatter text (between first --- and second ---)
    frontmatter = ''
    if content and content[0].strip() == '---':
        for line in content[1:]:
            if line.strip() == '---':
                break
            frontmatter += line

    if 'pdf: false' not in frontmatter:
        errors.append(ValidationError(
            "WARNING",
            filepath,
            1,
            "Stub/placeholder page should have 'pdf: false' in frontmatter to exclude from PDF export"
        ))
    return errors


def check_merge_conflict_markers(filepath: str, content: List[str]) -> List[ValidationError]:
    """Detect unresolved git merge conflict markers."""
    errors = []
    markers = ("<<<<<<< ", ">>>>>>> ", "=======")
    for i, line in enumerate(content, 1):
        stripped = line.strip()
        if any(stripped.startswith(m) for m in markers) or stripped == "=======":
            errors.append(ValidationError(
                "ERROR",
                filepath,
                i,
                "Unresolved merge conflict marker — resolve before committing"
            ))
    return errors


# Forbidden terms from the STYLE_GUIDE lexicon.
# Format: (regex_pattern, suggested_replacement)
_FORBIDDEN_TERMS = [
    (r'\bkostenplaatje\b', 'kostenoverzicht'),
    (r'\binregelen\b', 'instellen/configureren'),
    (r'\bgereedschapskist\b', 'toolkit'),
    (r'\bshadow\s+ai\b', 'wildgroei'),
    (r'\bmodel\s+drift\b', 'prestatieverloop'),
    (r'\bguardrails\b', 'rode lijnen'),
    (r'\bintent\s+records?\b', 'doeldefinitie'),
    (r'\bhyperparameter\s+tuning\b', 'afstellen van het model'),
    (r'\bdeployment\b', 'ingebruikname/livegang'),
    (r'\bproof\s+of\s+value\b', 'validatiepilot (Praktijkproef)'),
    (r'\binference\s+costs?\b', 'gebruikskosten'),
]


def check_terminology(filepath: str, content: List[str]) -> List[ValidationError]:
    """Flag forbidden terms from the STYLE_GUIDE lexicon (case-insensitive).

    Only flags terms that are in the NL content (not inside code blocks or URLs).
    Skips the termenlijst (glossary) where forbidden terms are explicitly defined.
    """
    # The termenlijst is the reference that explains these terms — skip it
    if "termenlijst" in filepath:
        return []

    errors = []
    in_code_block = False

    for i, line in enumerate(content, 1):
        stripped = line.strip()
        # Track fenced code blocks
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
        if in_code_block:
            continue
        # Skip inline code, links, and frontmatter
        if stripped.startswith("    ") or stripped.startswith("---"):
            continue

        for pattern, suggestion in _FORBIDDEN_TERMS:
            if re.search(pattern, line, re.IGNORECASE):
                errors.append(ValidationError(
                    "WARNING",
                    filepath,
                    i,
                    f"Stijlgids: gebruik '{suggestion}' in plaats van de gevonden term (patroon: {pattern})"
                ))
    return errors


def check_heading_hierarchy(filepath: str, content: List[str]) -> List[ValidationError]:
    """Detect skipped heading levels (e.g. H1 → H3 without H2).

    Skipped levels make the document structure ambiguous and break PDF bookmarks.
    """
    errors = []
    prev_level = 0
    in_code_block = False

    for i, line in enumerate(content, 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
        if in_code_block:
            continue

        m = re.match(r'^(#{1,6})\s+', line)
        if not m:
            continue

        level = len(m.group(1))
        if prev_level > 0 and level > prev_level + 1:
            errors.append(ValidationError(
                "WARNING",
                filepath,
                i,
                f"Kopniveau overgeslagen: H{prev_level} → H{level} (voeg H{prev_level + 1} toe)"
            ))
        prev_level = level

    return errors


def check_translation_coverage(docs_dir: Path, languages: List[str], strict: bool = False) -> List[ValidationError]:
    """Report which source pages (NL, no suffix) are missing translations.

    Uses INFO severity by default; WARNING when strict=True (for CI-gating).
    """
    errors = []
    severity = "WARNING" if strict else "INFO"

    for md_file in sorted(docs_dir.rglob('*.md')):
        if 'site' in md_file.parts:
            continue

        name = md_file.name
        # Skip files that already have a language suffix (e.g. index.en.md)
        parts = name.rsplit('.', 2)
        if len(parts) == 3 and parts[1] in languages:
            continue

        stem = md_file.stem  # e.g. "index"
        for lang in languages:
            translated = md_file.parent / f"{stem}.{lang}.md"
            if not translated.exists():
                errors.append(ValidationError(
                    severity,
                    str(md_file.relative_to(docs_dir.parent)),
                    1,
                    f"Missing {lang.upper()} translation: {translated.name}",
                ))

    return errors


def check_nav_completeness(docs_dir: Path) -> List[ValidationError]:
    """Check for orphaned markdown files not referenced in mkdocs.yml nav."""
    errors = []

    mkdocs_path = Path('mkdocs.yml')
    if not mkdocs_path.exists():
        return errors

    try:
        with open(mkdocs_path, 'r', encoding='utf-8') as f:
            mkdocs_content = f.read()
    except Exception as e:
        errors.append(ValidationError("WARNING", "mkdocs.yml", 0, f"Could not read mkdocs.yml: {e}"))
        return errors

    # Extract all .md file references from mkdocs.yml using regex
    nav_files = set(re.findall(r'[\w/-]+\.md', mkdocs_content))

    # Find all .md files on disk (skip language-suffix variants managed by i18n plugin)
    i18n_suffixes = {'.en.md'}
    disk_files = set()
    for md_file in docs_dir.rglob('*.md'):
        if 'site' in md_file.parts:
            continue
        if any(md_file.name.endswith(sfx) for sfx in i18n_suffixes):
            continue
        rel = str(md_file.relative_to(docs_dir))
        disk_files.add(rel)

    # Report orphans
    for rel in sorted(disk_files - nav_files):
        errors.append(ValidationError(
            "WARNING",
            str(docs_dir / rel),
            1,
            "File not referenced in mkdocs.yml nav (orphaned page — unreachable via navigation)"
        ))

    return errors


def validate_file(filepath: str) -> List[ValidationError]:
    """Run all per-file validation checks on a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.readlines()
    except Exception as e:
        return [ValidationError("ERROR", filepath, 0, f"Failed to read file: {e}")]

    errors = []
    errors.extend(check_merge_conflict_markers(filepath, content))
    errors.extend(check_duplicate_parenthetical_text(filepath, content))
    errors.extend(check_duplicate_words_in_headings(filepath, content))
    errors.extend(check_frontmatter(filepath, content))
    errors.extend(check_spelling_consistency(filepath, content))
    errors.extend(check_h1_presence(filepath, content))
    errors.extend(check_debug_markers(filepath, content))
    errors.extend(check_stub_pdf_exclusion(filepath, content))
    errors.extend(check_terminology(filepath, content))
    errors.extend(check_heading_hierarchy(filepath, content))

    return errors


def main():
    """Main validation function."""
    import argparse
    parser = argparse.ArgumentParser(description="Documentation quality validation")
    parser.add_argument(
        '--strict-i18n', action='store_true',
        help="Treat missing translations as WARNING (for CI-gating)"
    )
    args = parser.parse_args()

    docs_dir = Path('docs')

    if not docs_dir.exists():
        print(f"ERROR: {docs_dir} directory not found")
        sys.exit(1)

    all_errors = []
    files_checked = 0

    # Per-file checks (skip i18n translation files — stubs are checked separately)
    i18n_suffixes = ('.en.md',)
    # Directories excluded from all checks (internal/meta files, not content)
    excluded_dirs = {'admin'}
    for md_file in sorted(docs_dir.rglob('*.md')):
        if 'site' in md_file.parts:
            continue
        if any(part in excluded_dirs for part in md_file.parts):
            continue
        if md_file.name.endswith(i18n_suffixes):
            continue

        files_checked += 1
        errors = validate_file(str(md_file))
        all_errors.extend(errors)

    # Global checks (cross-file)
    all_errors.extend(check_nav_completeness(docs_dir))
    all_errors.extend(check_translation_coverage(
        docs_dir, languages=["en"], strict=args.strict_i18n
    ))

    # Print results
    print(f"\n{'='*70}")
    print(f"Documentation Quality Validation")
    print(f"{'='*70}")
    print(f"Files checked: {files_checked}")

    if not all_errors:
        print("\n✅ All validation checks passed!")
        print(f"{'='*70}\n")
        sys.exit(0)

    # Group errors by severity
    errors_by_severity = {'ERROR': [], 'WARNING': [], 'INFO': []}
    for error in all_errors:
        errors_by_severity[error.severity].append(error)

    # Print errors
    for severity in ['ERROR', 'WARNING', 'INFO']:
        if errors_by_severity[severity]:
            print(f"\n{severity}S ({len(errors_by_severity[severity])}):")
            for error in errors_by_severity[severity]:
                print(f"  {error}")

    print(f"\n{'='*70}")
    print(f"Total issues: {len(all_errors)}")
    print(f"{'='*70}\n")

    # Exit with error if there are any ERROR level issues
    if errors_by_severity['ERROR']:
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
