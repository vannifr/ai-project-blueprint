"""Shared fixtures for script tests."""

import textwrap
from pathlib import Path

import pytest


@pytest.fixture
def tmp_docs(tmp_path: Path) -> Path:
    """Create a temporary docs/ directory structure."""
    docs = tmp_path / "docs"
    docs.mkdir()
    return docs


def write_doc(docs: Path, rel_path: str, frontmatter: str, body: str = "") -> Path:
    """Write a markdown file with given frontmatter and body."""
    path = docs / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    content = f"---\n{textwrap.dedent(frontmatter).strip()}\n---\n\n{body}"
    path.write_text(content, encoding="utf-8")
    return path
