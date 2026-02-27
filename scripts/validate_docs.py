#!/usr/bin/env python3
"""
Documentation Quality Validation Script
Catches common quality issues in markdown documentation.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple


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
    stub_phrases = ['Inhoud volgt nog', 'wordt uitgewerkt in een toekomstige versie']
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

    # Find all .md files on disk
    disk_files = set()
    for md_file in docs_dir.rglob('*.md'):
        if 'site' in md_file.parts:
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
    errors.extend(check_duplicate_parenthetical_text(filepath, content))
    errors.extend(check_duplicate_words_in_headings(filepath, content))
    errors.extend(check_frontmatter(filepath, content))
    errors.extend(check_spelling_consistency(filepath, content))
    errors.extend(check_h1_presence(filepath, content))
    errors.extend(check_debug_markers(filepath, content))
    errors.extend(check_stub_pdf_exclusion(filepath, content))

    return errors


def main():
    """Main validation function."""
    docs_dir = Path('docs')

    if not docs_dir.exists():
        print(f"ERROR: {docs_dir} directory not found")
        sys.exit(1)

    all_errors = []
    files_checked = 0

    # Per-file checks
    for md_file in sorted(docs_dir.rglob('*.md')):
        if 'site' in md_file.parts:
            continue

        files_checked += 1
        errors = validate_file(str(md_file))
        all_errors.extend(errors)

    # Global checks (cross-file)
    all_errors.extend(check_nav_completeness(docs_dir))

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
    errors_by_severity = {'ERROR': [], 'WARNING': []}
    for error in all_errors:
        errors_by_severity[error.severity].append(error)

    # Print errors
    for severity in ['ERROR', 'WARNING']:
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
