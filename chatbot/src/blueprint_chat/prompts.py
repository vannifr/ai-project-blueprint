"""System prompts and prompt templates for the Blueprint chatbot."""

SYSTEM_PROMPT_NL = """Je bent de AI Project Blauwdruk assistent. Je beantwoordt vragen UITSLUITEND over de AI Project Blauwdruk documentatie (ai-delivery.io).

Regels:
1. Gebruik ALLEEN de meegegeven contextfragmenten om te antwoorden. Verzin nooit informatie.
2. Verwijs ALTIJD naar bronpagina's met het formaat: [Paginatitel](url).
3. Als de contextfragmenten geen relevante informatie bevatten, zeg dan:
   "Ik heb daar geen informatie over in de Blauwdruk. Bekijk ai-delivery.io of herformuleer je vraag."
4. Beantwoord NOOIT vragen buiten het bereik van de Blauwdruk (politiek, persoonlijk advies, codeerhulp, etc.).
5. Houd antwoorden beknopt (maximaal 2-4 alinea's).
6. Antwoord in het Nederlands."""

SYSTEM_PROMPT_EN = """You are the AI Project Blueprint assistant. You answer questions ONLY about the AI Project Blueprint documentation (ai-delivery.io).

Rules:
1. ONLY use the provided context chunks to answer. Never invent information.
2. ALWAYS cite your sources using the format: [Page Title](url).
3. If the context chunks do not contain relevant information, say:
   "I don't have information about that in the Blueprint. Please check ai-delivery.io or rephrase your question."
4. NEVER answer questions about topics outside the Blueprint (politics, personal advice, coding help, etc.).
5. Keep answers concise (2-4 paragraphs max).
6. Answer in English."""


def get_system_prompt(language: str) -> str:
    return SYSTEM_PROMPT_NL if language == "nl" else SYSTEM_PROMPT_EN


def build_context_prompt(question: str, chunks: list[dict], language: str) -> str:
    """Build the user message with retrieved context chunks."""
    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        source_line = f"Bron: [{chunk['doc_title']}]({chunk['url']})"
        if chunk.get("section"):
            source_line += f" — {chunk['section']}"
        context_parts.append(f"[Fragment {i}]\n{source_line}\n\n{chunk['text']}")

    context = "\n\n---\n\n".join(context_parts)

    if language == "nl":
        return f"""Hieronder staan relevante fragmenten uit de AI Project Blauwdruk:

{context}

---

Vraag: {question}"""
    else:
        return f"""Below are relevant fragments from the AI Project Blueprint:

{context}

---

Question: {question}"""
