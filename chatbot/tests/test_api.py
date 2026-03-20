"""Tests for the FastAPI endpoints (unit tests with mocked dependencies)."""

from contextlib import asynccontextmanager
from unittest.mock import MagicMock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from blueprint_chat.models import ChatResponse, Source


def _create_test_app(mock_generator):
    """Create a fresh FastAPI app with mocked dependencies (no real lifespan)."""
    from blueprint_chat.api import _request_times
    _request_times.clear()

    @asynccontextmanager
    async def mock_lifespan(app):
        app.state.generator = mock_generator
        app.state.chroma_client = MagicMock()
        yield

    # Import the route handlers but use our mock lifespan
    from blueprint_chat.api import chat, health
    from blueprint_chat.config import settings

    app = FastAPI(lifespan=mock_lifespan)

    from fastapi.middleware.cors import CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_methods=["POST", "GET"],
        allow_headers=["Content-Type"],
    )

    # Re-register routes on this test app
    from blueprint_chat.models import ChatRequest, HealthResponse
    from fastapi import Request, HTTPException
    from blueprint_chat.api import _check_rate_limit

    @app.post("/api/chat", response_model=ChatResponse)
    async def test_chat(request: ChatRequest, req: Request):
        client_ip = req.client.host if req.client else "unknown"
        if not _check_rate_limit(client_ip):
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        generator = req.app.state.generator
        return generator.answer(request.question, request.language)

    @app.get("/api/health", response_model=HealthResponse)
    async def test_health(req: Request):
        client = req.app.state.chroma_client
        try:
            nl_count = client.get_collection("blueprint_nl").count()
        except Exception:
            nl_count = 0
        try:
            en_count = client.get_collection("blueprint_en").count()
        except Exception:
            en_count = 0
        return {"status": "ok", "chunks_nl": nl_count, "chunks_en": en_count}

    return app


@pytest.fixture
def mock_generator():
    gen = MagicMock()
    gen.answer.return_value = ChatResponse(
        answer="Dit is een testantwoord.",
        sources=[Source(title="Test Page", url="https://ai-delivery.io/test/")],
        language="nl",
    )
    return gen


@pytest.fixture
def client(mock_generator):
    from blueprint_chat.api import _request_times
    _request_times.clear()
    app = _create_test_app(mock_generator)
    with TestClient(app) as c:
        yield c
    _request_times.clear()


def test_chat_endpoint(client, mock_generator):
    response = client.post("/api/chat", json={"question": "Wat is de Blauwdruk?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert data["language"] == "nl"
    assert len(data["sources"]) > 0
    mock_generator.answer.assert_called_once()


def test_chat_empty_question(client):
    response = client.post("/api/chat", json={"question": ""})
    assert response.status_code == 422


def test_chat_question_too_long(client):
    response = client.post("/api/chat", json={"question": "x" * 501})
    assert response.status_code == 422


def test_chat_with_language(client, mock_generator):
    response = client.post("/api/chat", json={"question": "What is it?", "language": "en"})
    assert response.status_code == 200
    mock_generator.answer.assert_called_with("What is it?", "en")


def test_chat_invalid_language(client):
    response = client.post("/api/chat", json={"question": "test", "language": "fr"})
    assert response.status_code == 422


def test_health_endpoint(client):
    mock_collection = MagicMock()
    mock_collection.count.return_value = 500
    client.app.state.chroma_client.get_collection.return_value = mock_collection
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_rate_limit(client, mock_generator):
    from blueprint_chat.api import _request_times
    _request_times.clear()

    for i in range(30):
        response = client.post("/api/chat", json={"question": f"test {i}"})
        assert response.status_code == 200, f"Request {i} failed"

    response = client.post("/api/chat", json={"question": "overflow"})
    assert response.status_code == 429
