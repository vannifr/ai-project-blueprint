"""Tests for content_index.py — loading, indexing, and searching."""

from blueprint_mcp.content_index import parse_frontmatter, extract_title, ContentIndex


class TestParseFrontmatter:
    def test_basic_fields(self):
        text = "---\nversie: '1.0'\ntype: guide\nlayer: 2\n---\n# Title\n"
        fm = parse_frontmatter(text)
        assert fm["versie"] == "1.0"
        assert fm["type"] == "guide"
        assert fm["layer"] == 2

    def test_list_of_integers(self):
        text = "---\nphase: [1, 2, 3]\n---\n"
        fm = parse_frontmatter(text)
        assert fm["phase"] == [1, 2, 3]

    def test_list_of_strings(self):
        text = '---\nroles: ["AI Product Manager", "Guardian"]\n---\n'
        fm = parse_frontmatter(text)
        assert fm["roles"] == ["AI Product Manager", "Guardian"]

    def test_empty_list(self):
        text = "---\ntags: []\n---\n"
        fm = parse_frontmatter(text)
        assert fm["tags"] == []

    def test_no_frontmatter(self):
        text = "# Just a title\nSome content."
        fm = parse_frontmatter(text)
        assert fm == {}


class TestExtractTitle:
    def test_extracts_h1(self):
        body = "\n# My Title\n\nSome content."
        assert extract_title(body) == "My Title"

    def test_no_h1(self):
        body = "No heading here."
        assert extract_title(body) == ""


class TestContentIndex:
    def test_loads_documents(self, content_index):
        assert len(content_index.docs) > 0
        # We know there are ~136 EN files
        assert len(content_index.docs) >= 50

    def test_all_docs_are_english(self, content_index):
        for doc in content_index.docs:
            assert doc.path.endswith(".en.md"), f"Expected .en.md: {doc.path}"
            assert doc.language == "en"

    def test_by_path_lookup(self, content_index):
        # Explorer kit index should exist
        matches = [p for p in content_index.by_path if "explorer-kit" in p and "index" in p]
        assert len(matches) >= 1

    def test_by_type_index(self, content_index):
        assert "guide" in content_index.by_type
        assert len(content_index.by_type["guide"]) > 0

    def test_by_phase_index(self, content_index):
        # Phase 1 (Discovery) should have documents
        assert 1 in content_index.by_phase
        assert len(content_index.by_phase[1]) > 0

    def test_by_layer_index(self, content_index):
        assert 1 in content_index.by_layer  # Strategic layer
        assert 2 in content_index.by_layer  # Operational layer

    def test_search_keyword(self, content_index):
        results = content_index.search("risk")
        assert len(results) > 0
        # At least one result should mention risk in title or path
        assert any("risk" in d.title.lower() or "risk" in d.path.lower() for d in results)

    def test_search_with_type_filter(self, content_index):
        results = content_index.search("", type="template")
        for doc in results:
            assert doc.type == "template"

    def test_search_with_phase_filter(self, content_index):
        results = content_index.search("", phase=2)
        for doc in results:
            assert 2 in doc.phases

    def test_get_phase_docs(self, content_index):
        objectives = content_index.get_phase_docs(1, "objectives")
        assert len(objectives) >= 1
        for doc in objectives:
            assert doc.type == "objectives"

    def test_get_templates(self, content_index):
        templates = content_index.get_templates()
        assert len(templates) > 0
        for doc in templates:
            assert doc.type == "template"

    def test_nl_index_loads(self, nl_index):
        assert len(nl_index.docs) > 0
        for doc in nl_index.docs:
            assert not doc.path.endswith(".en.md"), f"NL index should not have .en.md: {doc.path}"
