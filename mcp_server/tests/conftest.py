"""Shared test fixtures for Blueprint MCP server tests."""

import pytest
from pathlib import Path

from blueprint_mcp.content_index import ContentIndex

DOCS_ROOT = Path(__file__).resolve().parent.parent.parent / "docs"


@pytest.fixture(scope="session")
def content_index():
    """Load the full English content index once for all tests."""
    return ContentIndex.load(DOCS_ROOT, language="en")


@pytest.fixture(scope="session")
def nl_index():
    """Load the Dutch content index."""
    return ContentIndex.load(DOCS_ROOT, language="nl")
