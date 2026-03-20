"""Shared test fixtures."""

from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures" / "sample_docs"


@pytest.fixture
def sample_docs_dir():
    return FIXTURES_DIR


@pytest.fixture
def sample_nl_doc():
    return (FIXTURES_DIR / "01-sample.md").read_text(encoding="utf-8")


@pytest.fixture
def sample_en_doc():
    return (FIXTURES_DIR / "01-sample.en.md").read_text(encoding="utf-8")


@pytest.fixture
def sample_no_headings_doc():
    return (FIXTURES_DIR / "02-no-headings.md").read_text(encoding="utf-8")
