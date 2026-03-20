"""Generate answers using Claude with retrieved context."""

from __future__ import annotations

from anthropic import Anthropic

from .config import settings
from .models import ChatResponse, Source
from .prompts import build_context_prompt, get_system_prompt
from .retriever import Retriever


class Generator:
    """Generate answers for Blueprint questions using RAG."""

    def __init__(self, retriever: Retriever | None = None):
        self.retriever = retriever or Retriever()
        self.client = Anthropic(api_key=settings.anthropic_api_key)

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

        response = self.client.messages.create(
            model=settings.generation_model,
            max_tokens=settings.max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )

        answer_text = response.content[0].text
        sources = self.retriever.to_sources(chunks)

        return ChatResponse(
            answer=answer_text,
            sources=sources,
            language=detected_lang,
        )
