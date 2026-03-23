"""Tests for the retriever module."""

from blueprint_chat.retriever import detect_language, doc_path_to_url


def test_detect_language_dutch():
    assert detect_language("Hoe start ik een AI-project?") == "nl"
    assert detect_language("Wat zijn de risico's van dit project?") == "nl"


def test_detect_language_english():
    assert detect_language("How do I start an AI project?") == "en"
    assert detect_language("What are the risks?") == "en"


def test_detect_language_ambiguous_defaults_to_en():
    assert detect_language("AI") == "en"


def test_doc_path_to_url_nl():
    url = doc_path_to_url("02-fase-ontdekking/01-doelstellingen.md", "nl")
    assert url == "https://ai-delivery.io/02-fase-ontdekking/01-doelstellingen/"


def test_doc_path_to_url_en():
    url = doc_path_to_url("02-fase-ontdekking/01-doelstellingen.en.md", "en")
    assert url == "https://ai-delivery.io/en/02-fase-ontdekking/01-doelstellingen/"


def test_doc_path_to_url_index():
    url = doc_path_to_url("07-compliance-hub/index.md", "nl")
    assert url == "https://ai-delivery.io/07-compliance-hub/"


def test_doc_path_to_url_root_index():
    url = doc_path_to_url("index.md", "nl")
    assert url == "https://ai-delivery.io/"
    url_en = doc_path_to_url("index.en.md", "en")
    assert url_en == "https://ai-delivery.io/en/"
