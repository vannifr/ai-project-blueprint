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
        # Skip table rows (common to have repeated short terms)
        if line.strip().startswith('|'):
            continue
        # Find all parenthetical text
        matches = re.findall(r'\(([^)]+)\)', line)
        if matches:
            # Check for duplicates (ignore short abbreviations)
            for text in set(matches):
                if len(text) <= 5:
                    continue
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
_FORBIDDEN_TERMS_NL = [
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

# English style guide: forbidden terms in EN content
_FORBIDDEN_TERMS_EN = [
    (r'\bguardrails\b', 'hard boundaries'),
    (r'\bmodel\s+drift\b', 'performance degradation'),
    (r'\bshadow\s+ai\b', 'AI sprawl'),
    (r'\bproof\s+of\s+concept\b', 'validation pilot'),
    (r'\bhyperparameter\s+tuning\b', 'model tuning'),
    (r'\binference\s+costs?\b', 'usage costs'),
]

# Keep backward compat alias
_FORBIDDEN_TERMS = _FORBIDDEN_TERMS_NL


def check_terminology(filepath: str, content: List[str]) -> List[ValidationError]:
    """Flag forbidden terms from the STYLE_GUIDE lexicon (case-insensitive).

    Applies NL terms to .md files and EN terms to .en.md files.
    Skips the termenlijst (glossary) where forbidden terms are explicitly defined.
    """
    # The termenlijst is the reference that explains these terms — skip it
    if "termenlijst" in filepath:
        return []

    is_en = filepath.endswith('.en.md')
    forbidden = _FORBIDDEN_TERMS_EN if is_en else _FORBIDDEN_TERMS_NL

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

        for pattern, suggestion in forbidden:
            if re.search(pattern, line, re.IGNORECASE):
                # Skip "not X" contexts where the forbidden term is cited as
                # an example of what NOT to use (e.g. '(not "guardrails")')
                if re.search(r'(?:not|niet)\s+["\u201c]?' + pattern, line, re.IGNORECASE):
                    continue
                label = "Style guide" if is_en else "Stijlgids"
                errors.append(ValidationError(
                    "WARNING",
                    filepath,
                    i,
                    f"{label}: use '{suggestion}' instead (pattern: {pattern})"
                ))
    return errors


def check_cta_blocks(filepath: str, content: str) -> list[str]:
    """Warn if a Layer 2 module file lacks a CTA block."""
    warnings = []
    layer2_patterns = [
        '/02-fase-', '/03-fase-', '/04-fase-', '/05-fase-', '/06-fase-',
        '/10-doorlopende-', '/11-project-', '/12-90-dagen-'
    ]
    is_layer2 = any(p in filepath for p in layer2_patterns)
    if is_layer2 and filepath.endswith('.md') and not filepath.endswith('.en.md'):
        if '**Volgende stap:**' not in content and '**Next step:**' not in content:
            warnings.append(f"WARN [v2.3-CTA] Missing CTA block ('Volgende stap:') in: {filepath}")
    return warnings


def check_collaboration_mode_in_gates(filepath: str, content: str) -> list[str]:
    """Warn if a gate review file lacks a Collaboration Mode field."""
    warnings = []
    if '08-gate-reviews' in filepath and filepath.endswith('.md'):
        if 'Samenwerkingsmodus' not in content and 'Collaboration mode' not in content:
            warnings.append(f"WARN [v2.3-MODE] Gate file missing 'Samenwerkingsmodus' field: {filepath}")
    return warnings


def check_no_lifecycle_redundancy(filepath: str, content: str) -> list[str]:
    """Warn if a phase module re-explains the full lifecycle."""
    warnings = []
    phase_patterns = ['/02-fase-', '/03-fase-', '/04-fase-', '/05-fase-', '/06-fase-']
    is_phase = any(p in filepath for p in phase_patterns)
    if is_phase and filepath.endswith('.md'):
        redundancy_markers = ['bestaat uit 5 fasen', 'vijf fasen zijn', 'five phases are', 'bestaat uit vijf fasen']
        for marker in redundancy_markers:
            if marker in content.lower():
                warnings.append(f"WARN [v2.3-REDUNDANCY] Possible lifecycle re-explanation in: {filepath}")
                break
    return warnings


def check_role_consistency(filepath: str, content: List[str]) -> List[ValidationError]:
    """Flag inconsistent role name variants (e.g. 'AI PM' vs 'AI Product Manager')."""
    errors = []
    # Canonical names → forbidden abbreviations/variants
    role_variants = {
        r'\bAI\s+PM\b': 'AI Product Manager',
        r'\bGuardian\s*\(Ethicist\)': 'Guardian',
        r'\bGuardian\s*\(Ethicus\)': 'Guardian',
    }
    in_code_block = False
    for i, line in enumerate(content, 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
        if in_code_block:
            continue
        for pattern, canonical in role_variants.items():
            if re.search(pattern, line):
                errors.append(ValidationError(
                    "INFO",
                    filepath,
                    i,
                    f"Role variant: use '{canonical}' consistently (found: {pattern})"
                ))
    return errors


# Regex to extract markdown links: [text](path)
_RE_MD_LINK = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')


def check_link_integrity(filepath: str, content: List[str], docs_dir: Path) -> List[ValidationError]:
    """Validate all internal markdown links resolve to existing files.

    Also checks cross-language correctness: .en.md files should link to .en.md targets.
    """
    errors = []
    file_path = Path(filepath)
    file_dir = file_path.parent
    is_en = filepath.endswith('.en.md')

    in_code_block = False
    for i, line in enumerate(content, 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
        if in_code_block:
            continue

        for _text, link in _RE_MD_LINK.findall(line):
            # Skip external links, anchors-only, mailto, images
            if link.startswith(('http://', 'https://', '#', 'mailto:')):
                continue
            # Skip image references and special protocols
            if link.startswith(('..', '.')) or not link.startswith('/'):
                pass  # relative links — we check these
            else:
                continue  # absolute or special

            # Strip anchor from link
            link_path = link.split('#')[0]
            if not link_path:
                continue  # anchor-only link

            # Resolve relative to file's directory
            target = (file_dir / link_path).resolve()

            # Check if target exists
            # MkDocs allows directory links (e.g. ../foo/) which resolve to foo/index.md
            target_exists = target.exists()
            if not target_exists and link_path.endswith('/'):
                # Try as directory with index.md
                index_target = target / 'index.md'
                target_exists = index_target.exists()
            if not target_exists and not link_path.endswith('.md'):
                # Try adding .md extension
                target_exists = Path(str(target) + '.md').exists()
            if not target_exists:
                errors.append(ValidationError(
                    "ERROR",
                    filepath,
                    i,
                    f"Broken link: '{link_path}' (resolved to {target})"
                ))
            elif is_en and link_path.endswith('.md') and not link_path.endswith('.en.md'):
                # EN file linking to NL file — check if .en.md version exists
                en_target = target.parent / target.name.replace('.md', '.en.md')
                if en_target.exists():
                    errors.append(ValidationError(
                        "INFO",
                        filepath,
                        i,
                        f"EN file links to NL version: '{link_path}' — "
                        f"consider using '{link_path.replace('.md', '.en.md')}'"
                    ))

    return errors


def check_content_parity(docs_dir: Path) -> List[ValidationError]:
    """Compare NL and EN files structurally: headings, tables, checkboxes.

    Reports significant structural differences that suggest content is out of sync.
    """
    errors = []

    for nl_file in sorted(docs_dir.rglob('*.md')):
        if 'site' in nl_file.parts:
            continue
        if nl_file.name.endswith('.en.md'):
            continue

        en_file = nl_file.parent / nl_file.name.replace('.md', '.en.md')
        if not en_file.exists():
            continue  # Missing translation — handled by check_translation_coverage

        try:
            nl_content = nl_file.read_text(encoding='utf-8')
            en_content = en_file.read_text(encoding='utf-8')
        except Exception:
            continue

        rel_path = str(nl_file.relative_to(docs_dir.parent))

        # Compare heading structure
        nl_headings = re.findall(r'^(#{1,6})\s+', nl_content, re.MULTILINE)
        en_headings = re.findall(r'^(#{1,6})\s+', en_content, re.MULTILINE)
        if len(nl_headings) != len(en_headings):
            errors.append(ValidationError(
                "WARNING",
                rel_path,
                0,
                f"Heading count mismatch: NL has {len(nl_headings)}, "
                f"EN has {len(en_headings)} headings"
            ))

        # Compare table count
        nl_tables = len(re.findall(r'^\|.*\|.*\|', nl_content, re.MULTILINE))
        en_tables = len(re.findall(r'^\|.*\|.*\|', en_content, re.MULTILINE))
        if abs(nl_tables - en_tables) > 2:  # Allow small differences
            errors.append(ValidationError(
                "WARNING",
                rel_path,
                0,
                f"Table row count mismatch: NL has {nl_tables}, "
                f"EN has {en_tables} table rows"
            ))

        # Compare checkbox count
        nl_checkboxes = len(re.findall(r'- \[[ x]\]', nl_content))
        en_checkboxes = len(re.findall(r'- \[[ x]\]', en_content))
        if abs(nl_checkboxes - en_checkboxes) > 2:
            errors.append(ValidationError(
                "WARNING",
                rel_path,
                0,
                f"Checkbox count mismatch: NL has {nl_checkboxes}, "
                f"EN has {en_checkboxes} checkboxes"
            ))

    return errors


def check_related_modules_section(filepath: str, content: List[str]) -> List[ValidationError]:
    """Check that layer 2 operational files have a Related Modules section."""
    errors = []
    # Only check layer 2 phase files and operational modules
    layer2_dirs = [
        '/02-fase-', '/03-fase-', '/04-fase-', '/05-fase-', '/06-fase-',
        '/10-doorlopende-', '/11-project-',
    ]
    is_layer2 = any(d in filepath for d in layer2_dirs)
    if not is_layer2:
        return errors

    # Skip index files
    if os.path.basename(filepath).startswith('index'):
        return errors

    content_str = ''.join(content)
    has_related = (
        'Gerelateerde Modules' in content_str
        or 'Related Modules' in content_str
        or 'Zie ook' in content_str
        or 'See also' in content_str
    )
    if not has_related:
        errors.append(ValidationError(
            "INFO",
            filepath,
            0,
            "Missing 'Related Modules' section — consider adding cross-references"
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


def validate_file(filepath: str, docs_dir: Path = None) -> List[ValidationError]:
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
    errors.extend(check_role_consistency(filepath, content))
    errors.extend(check_related_modules_section(filepath, content))

    # Link integrity (needs docs_dir for resolution)
    if docs_dir is not None:
        errors.extend(check_link_integrity(filepath, content, docs_dir))

    # v2.3 checks (operate on full content string)
    content_str = ''.join(content)
    for warning_msg in check_cta_blocks(filepath, content_str):
        errors.append(ValidationError("WARNING", filepath, 0, warning_msg))
    for warning_msg in check_collaboration_mode_in_gates(filepath, content_str):
        errors.append(ValidationError("WARNING", filepath, 0, warning_msg))
    for warning_msg in check_no_lifecycle_redundancy(filepath, content_str):
        errors.append(ValidationError("WARNING", filepath, 0, warning_msg))

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

    # Directories excluded from all checks (internal/meta files, not content)
    excluded_dirs = {'admin'}

    # Per-file checks: validate ALL markdown files (NL and EN)
    for md_file in sorted(docs_dir.rglob('*.md')):
        if 'site' in md_file.parts:
            continue
        if any(part in excluded_dirs for part in md_file.parts):
            continue

        files_checked += 1
        errors = validate_file(str(md_file), docs_dir=docs_dir)
        all_errors.extend(errors)

    # Global checks (cross-file)
    all_errors.extend(check_nav_completeness(docs_dir))
    all_errors.extend(check_translation_coverage(
        docs_dir, languages=["en"], strict=args.strict_i18n
    ))
    all_errors.extend(check_content_parity(docs_dir))

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

    # v2.3 checks summary
    v23_warnings = [e for e in all_errors if 'v2.3-' in e.message]
    print(f"v2.3 checks: {len(v23_warnings)} warnings")

    print(f"\n{'='*70}")
    print(f"Total issues: {len(all_errors)}")
    print(f"{'='*70}\n")

    # Exit with error if there are any ERROR level issues
    if errors_by_severity['ERROR']:
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
