"""Tests for the generator module (prompt assembly and scope guard)."""

from blueprint_chat.prompts import build_context_prompt, get_system_prompt


def test_system_prompt_nl():
    prompt = get_system_prompt("nl")
    assert "UITSLUITEND" in prompt
    assert "Nederlands" in prompt


def test_system_prompt_en():
    prompt = get_system_prompt("en")
    assert "ONLY" in prompt
    assert "English" in prompt


def test_build_context_prompt_nl():
    chunks = [
        {
            "text": "Dit is testinhoud over risicoclassificatie.",
            "doc_title": "Risicoclassificatie",
            "url": "https://ai-delivery.io/01-ai-native-fundamenten/05-risicoclassificatie/",
            "section": "Niveaus",
        }
    ]
    prompt = build_context_prompt("Hoe classificeer ik risico?", chunks, "nl")
    assert "Fragment 1" in prompt
    assert "Risicoclassificatie" in prompt
    assert "risicoclassificatie" in prompt.lower()
    assert "Vraag:" in prompt


def test_build_context_prompt_en():
    chunks = [
        {
            "text": "This is test content about risk classification.",
            "doc_title": "Risk Classification",
            "url": "https://ai-delivery.io/en/01-ai-native-fundamenten/05-risicoclassificatie/",
            "section": "",
        }
    ]
    prompt = build_context_prompt("How do I classify risk?", chunks, "en")
    assert "Fragment 1" in prompt
    assert "Question:" in prompt


def test_build_context_prompt_multiple_chunks():
    chunks = [
        {"text": "Chunk 1", "doc_title": "Title 1", "url": "http://a/", "section": "S1"},
        {"text": "Chunk 2", "doc_title": "Title 2", "url": "http://b/", "section": ""},
    ]
    prompt = build_context_prompt("test?", chunks, "en")
    assert "Fragment 1" in prompt
    assert "Fragment 2" in prompt
    assert "---" in prompt


def test_context_prompt_includes_source_urls():
    chunks = [
        {
            "text": "Content",
            "doc_title": "My Page",
            "url": "https://ai-delivery.io/test/",
            "section": "Intro",
        }
    ]
    prompt = build_context_prompt("question", chunks, "nl")
    assert "https://ai-delivery.io/test/" in prompt
    assert "My Page" in prompt
