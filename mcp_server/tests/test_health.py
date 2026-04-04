"""Tests for /health endpoint and X-Blueprint-Version header.

Written BEFORE the implementation (TDD, Red phase).
These tests document the contract that server.py must fulfil.
"""

from __future__ import annotations

import re
import time

import pytest
from starlette.testclient import TestClient


@pytest.fixture(scope="module")
def http_client():
    """Starlette TestClient against the real streamable-http app."""
    from blueprint_mcp.server import mcp

    app = mcp.streamable_http_app()
    return TestClient(app, raise_server_exceptions=True)


# ─── /health endpoint ─────────────────────────────────────────────────────────


class TestHealthEndpoint:
    def test_returns_200(self, http_client: TestClient) -> None:
        resp = http_client.get("/health")
        assert resp.status_code == 200

    def test_content_type_is_json(self, http_client: TestClient) -> None:
        resp = http_client.get("/health")
        assert "application/json" in resp.headers.get("content-type", "")

    def test_body_has_status_ok(self, http_client: TestClient) -> None:
        resp = http_client.get("/health")
        assert resp.json()["status"] == "ok"

    def test_body_has_version(self, http_client: TestClient) -> None:
        resp = http_client.get("/health")
        data = resp.json()
        assert "version" in data
        assert re.match(r"\d+\.\d+", data["version"]), f"Bad version: {data['version']!r}"

    def test_body_has_doc_count(self, http_client: TestClient) -> None:
        resp = http_client.get("/health")
        data = resp.json()
        assert "doc_count" in data
        assert isinstance(data["doc_count"], int)
        assert (
            data["doc_count"] >= 100
        ), f"doc_count={data['doc_count']} — expected at least 100 (we have 130+ pages)"

    def test_body_has_transport(self, http_client: TestClient) -> None:
        resp = http_client.get("/health")
        assert "transport" in resp.json()

    def test_is_fast(self, http_client: TestClient) -> None:
        """Health check must not load documents or do expensive I/O."""
        start = time.monotonic()
        http_client.get("/health")
        elapsed = time.monotonic() - start
        assert elapsed < 0.5, f"Health check took {elapsed:.3f}s — must be < 500ms"

    def test_only_get_allowed(self, http_client: TestClient) -> None:
        """POST to /health should return 405 Method Not Allowed."""
        resp = http_client.post("/health", json={})
        assert resp.status_code == 405


# ─── X-Blueprint-Version header ───────────────────────────────────────────────


class TestVersionHeader:
    def test_health_response_has_version_header(self, http_client: TestClient) -> None:
        resp = http_client.get("/health")
        assert "x-blueprint-version" in {k.lower() for k in resp.headers}

    def test_version_header_format(self, http_client: TestClient) -> None:
        resp = http_client.get("/health")
        version = resp.headers.get("X-Blueprint-Version") or resp.headers.get("x-blueprint-version")
        assert version is not None, "X-Blueprint-Version header missing"
        assert re.match(r"\d+\.\d+", version), f"Bad header format: {version!r}"

    def test_version_header_matches_body(self, http_client: TestClient) -> None:
        resp = http_client.get("/health")
        header_version = resp.headers.get("X-Blueprint-Version") or resp.headers.get(
            "x-blueprint-version"
        )
        body_version = resp.json().get("version")
        assert (
            header_version == body_version
        ), f"Header version {header_version!r} != body version {body_version!r}"


# ─── Integration: health reflects loaded index ────────────────────────────────


class TestHealthIntegration:
    def test_doc_count_is_nonzero_after_lifespan(self, http_client: TestClient) -> None:
        """If ContentIndex loaded correctly, doc_count must be > 0."""
        resp = http_client.get("/health")
        assert resp.json()["doc_count"] > 0

    def test_multiple_calls_return_consistent_count(self, http_client: TestClient) -> None:
        """Doc count must be stable across calls (index is not re-loaded)."""
        counts = [http_client.get("/health").json()["doc_count"] for _ in range(3)]
        assert len(set(counts)) == 1, f"Inconsistent doc counts: {counts}"
