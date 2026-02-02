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
    required_fields = ['versie', 'laatst_herzien']
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


def validate_file(filepath: str) -> List[ValidationError]:
    """Run all validation checks on a single file."""
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

    return errors


def main():
    """Main validation function."""
    docs_dir = Path('docs')

    if not docs_dir.exists():
        print(f"ERROR: {docs_dir} directory not found")
        sys.exit(1)

    all_errors = []
    files_checked = 0

    # Find all markdown files
    for md_file in docs_dir.rglob('*.md'):
        # Skip build artifacts
        if 'site' in md_file.parts:
            continue

        files_checked += 1
        errors = validate_file(str(md_file))
        all_errors.extend(errors)

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
