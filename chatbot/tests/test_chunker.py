"""Tests for document chunker."""

from blueprint_chat.chunker import (
    chunk_all_docs,
    chunk_document,
    extract_body,
    extract_title,
    parse_frontmatter,
)


def test_parse_frontmatter(sample_nl_doc):
    fm = parse_frontmatter(sample_nl_doc)
    assert fm["versie"] == "1.0"
    assert fm["type"] == "guide"
    assert fm["roles"] == ["AI Product Manager"]
    assert fm["tags"] == ["onboarding"]


def test_extract_body_strips_frontmatter(sample_nl_doc):
    body = extract_body(sample_nl_doc)
    assert not body.startswith("---")
    assert "# Voorbeelddocument" in body


def test_extract_title(sample_nl_doc):
    body = extract_body(sample_nl_doc)
    title = extract_title(body)
    assert title == "Voorbeelddocument"


def test_chunk_at_h2_boundaries(sample_nl_doc):
    chunks = chunk_document(sample_nl_doc, "01-sample.md", "nl")
    # Should have: preamble + Sectie A + Sectie B + Sectie C = 4 chunks
    assert len(chunks) == 4
    assert chunks[0].section == ""  # preamble
    assert chunks[1].section == "Sectie A"
    assert chunks[2].section == "Sectie B"
    assert chunks[3].section == "Sectie C"


def test_chunk_inherits_metadata(sample_nl_doc):
    chunks = chunk_document(sample_nl_doc, "01-sample.md", "nl")
    for chunk in chunks:
        assert chunk.doc_path == "01-sample.md"
        assert chunk.doc_title == "Voorbeelddocument"
        assert chunk.language == "nl"
        assert chunk.metadata["type"] == "guide"
        assert chunk.metadata["summary"] == "Een voorbeeldpagina voor tests."


def test_chunk_ids_are_unique(sample_nl_doc):
    chunks = chunk_document(sample_nl_doc, "01-sample.md", "nl")
    ids = [c.id for c in chunks]
    assert len(ids) == len(set(ids))


def test_no_h2_produces_single_chunk(sample_no_headings_doc):
    chunks = chunk_document(sample_no_headings_doc, "02-no-headings.md", "nl")
    assert len(chunks) == 1
    assert "Plat Document" in chunks[0].text or "geen H2" in chunks[0].text


def test_chunk_all_docs_nl(sample_docs_dir):
    chunks = chunk_all_docs(sample_docs_dir, language="nl")
    # Should only include .md files, not .en.md
    paths = {c.doc_path for c in chunks}
    assert any("01-sample.md" in p for p in paths)
    assert not any(".en.md" in p for p in paths)


def test_chunk_all_docs_en(sample_docs_dir):
    chunks = chunk_all_docs(sample_docs_dir, language="en")
    paths = {c.doc_path for c in chunks}
    assert any(".en.md" in p for p in paths)
    assert not any(p == "01-sample.md" for p in paths)


def test_oversized_section_is_split():
    """A very large section should be split at paragraph boundaries."""
    big_section = "Paragraph one.\n\n" * 200  # ~3000 chars
    doc = (
        "---\ntype: guide\nsummary: test\n---\n"
        "# Big Doc\n\n## Big Section\n\n"
        + big_section
    )
    chunks = chunk_document(doc, "big.md", "nl")
    # Should produce more than 1 chunk
    assert len(chunks) > 1
