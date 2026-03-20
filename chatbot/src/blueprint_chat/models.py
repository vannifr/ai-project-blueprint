"""Request/response models."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=500)
    language: str = Field(default="auto", pattern=r"^(nl|en|auto)$")


class Source(BaseModel):
    title: str
    url: str
    section: str | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]
    language: str


class HealthResponse(BaseModel):
    status: str
    chunks_nl: int
    chunks_en: int
