"""FastAPI server for the Blueprint RAG chatbot."""

import time
from collections import defaultdict
from contextlib import asynccontextmanager

import chromadb
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .generator import Generator
from .models import ChatRequest, ChatResponse, HealthResponse
from .retriever import Retriever

# Simple in-memory rate limiter
_request_times: dict[str, list[float]] = defaultdict(list)


def _check_rate_limit(client_ip: str) -> bool:
    """Return True if the client is within rate limits."""
    now = time.time()
    window = 60.0  # 1 minute
    times = _request_times[client_ip]
    # Prune old entries
    _request_times[client_ip] = [t for t in times if now - t < window]
    if len(_request_times[client_ip]) >= settings.rate_limit_rpm:
        return False
    _request_times[client_ip].append(now)
    return True


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize ChromaDB client and generator on startup."""
    chroma_client = chromadb.PersistentClient(path=settings.chroma_path)
    retriever = Retriever(chroma_client=chroma_client)
    app.state.generator = Generator(retriever=retriever)
    app.state.chroma_client = chroma_client
    yield


app = FastAPI(
    title="Blueprint Chat API",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, req: Request):
    """Answer a question about the AI Project Blueprint."""
    client_ip = req.client.host if req.client else "unknown"
    if not _check_rate_limit(client_ip):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    generator: Generator = req.app.state.generator
    return generator.answer(request.question, request.language)


@app.get("/api/health", response_model=HealthResponse)
async def health(req: Request):
    """Health check with collection stats."""
    client: chromadb.PersistentClient = req.app.state.chroma_client
    try:
        nl_count = client.get_collection("blueprint_nl").count()
    except Exception:
        nl_count = 0
    try:
        en_count = client.get_collection("blueprint_en").count()
    except Exception:
        en_count = 0

    return HealthResponse(
        status="ok",
        chunks_nl=nl_count,
        chunks_en=en_count,
    )


def main():
    """Entry point for the CLI."""
    import uvicorn
    uvicorn.run(
        "blueprint_chat.api:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=False,
    )
