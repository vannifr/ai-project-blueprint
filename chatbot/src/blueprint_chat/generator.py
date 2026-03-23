"""Generate answers using Ollama with retrieved context."""

from __future__ import annotations

from ollama import Client

from .config import settings
from .models import ChatResponse
from .prompts import build_context_prompt, get_system_prompt
from .retriever import Retriever


def _get_ollama_client() -> Client:
    """Get an Ollama client configured for cloud or local."""
    headers = {}
    if settings.ollama_api_key:
        headers["Authorization"] = f"Bearer {settings.ollama_api_key}"
    return Client(
        host=settings.ollama_host,
        headers=headers,
    )


class Generator:
    """Generate answers for Blueprint questions using RAG."""

    def __init__(self, retriever: Retriever | None = None):
        self.retriever = retriever or Retriever()
        self.client = _get_ollama_client()

    def answer(self, question: str, language: str = "auto") -> ChatResponse:
        """Answer a question using RAG: retrieve, augment, generate."""
        chunks, detected_lang = self.retriever.retrieve(question, language)

        if not chunks:
            no_info = (
                "Ik heb daar geen informatie over in de Blauwdruk. "
                "Bekijk ai-delivery.io of herformuleer je vraag."
                if detected_lang == "nl"
                else "I don't have information about that in the Blueprint. "
                "Please check ai-delivery.io or rephrase your question."
            )
            return ChatResponse(answer=no_info, sources=[], language=detected_lang)

        system_prompt = get_system_prompt(detected_lang)
        user_message = build_context_prompt(question, chunks, detected_lang)

        response = self.client.chat(
            model=settings.generation_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            options={"num_predict": settings.max_tokens},
        )

        answer_text = response["message"]["content"]
        sources = self.retriever.to_sources(chunks)

        return ChatResponse(
            answer=answer_text,
            sources=sources,
            language=detected_lang,
        )
