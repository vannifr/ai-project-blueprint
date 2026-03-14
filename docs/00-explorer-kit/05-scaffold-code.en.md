---
versie: '1.0'
type: guide
layer: 2
tags: [onboarding]
---

# Scaffold Code — Starter Code for 3 Use Cases

## 1. Overview

This page contains working Python starter code for the three most common AI use cases in the Explorer phase. Copy the code that matches your use case and adapt it to your situation.

| Use Case                                         | Technique                            | Suitable for                                          |
| :----------------------------------------------- | :----------------------------------- | :---------------------------------------------------- |
| [📄 Document Q&A](#document-qa)                  | RAG (Retrieval-Augmented Generation) | Questions about internal documents, manuals, policies |
| [📧 Email classification](#email-classification) | LLM classification                   | Sorting and prioritising incoming messages            |
| [✍️ Content generation](#content-generation)     | Structured prompting                 | Reports, product descriptions, summarised content     |

!!! warning "API key required"
    All examples use the **Anthropic Claude API**. Request an API key at [console.anthropic.com](https://console.anthropic.com) and store it in a `.env` file (see Installation section). Replace `claude-haiku-4-5-20251001` with a different model if desired.

______________________________________________________________________

## 2. Installation

### 2.1 Requirements

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install anthropic python-dotenv pypdf2 faiss-cpu sentence-transformers pandas
```

### 2.2 .env file

Create a `.env` file in the root of your project:

```bash
# .env — add this file to .gitignore!
ANTHROPIC_API_KEY=sk-ant-...
```

### 2.3 Docker setup (optional)

For an isolated environment with Jupyter:

```yaml
# docker-compose.yml
services:
  notebook:
    image: jupyter/scipy-notebook:latest
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
      - ./.env:/home/jovyan/.env
    environment:
      - JUPYTER_ENABLE_LAB=yes
    command: start-notebook.sh --NotebookApp.token=''
```

Start with: `docker compose up`

______________________________________________________________________

## 3. Document Q&A (RAG) {#document-qa}

**When to use:** You want users to ask questions about internal documents (policies, manuals, FAQs).

```python
# rag_qa.py — Document Q&A with RAG and Claude
import os
import anthropic
from dotenv import load_dotenv
from pathlib import Path
import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

load_dotenv()

# ── Configuration ────────────────────────────────────────────────────────────
DOCS_FOLDER = "./documents"          # Folder with your PDF/TXT files
MODEL = "claude-haiku-4-5-20251001"  # Fast and affordable for prototypes
EMBED_MODEL = "all-MiniLM-L6-v2"    # Local embedding model (no API costs)
CHUNK_SIZE = 500                     # Characters per chunk
MAX_CONTEXT_CHUNKS = 4               # Number of chunks sent to Claude


# ── Step 1: Load documents and split into chunks ────────────────────────────
def load_documents(folder: str) -> list[dict]:
    """Load all PDF and TXT files from a folder."""
    chunks = []
    for path in Path(folder).rglob("*"):
        if path.suffix == ".pdf":
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = " ".join(p.extract_text() or "" for p in reader.pages)
        elif path.suffix == ".txt":
            text = path.read_text(encoding="utf-8")
        else:
            continue

        # Split into overlapping chunks
        for i in range(0, len(text), CHUNK_SIZE - 100):
            chunk = text[i : i + CHUNK_SIZE]
            if len(chunk) > 100:  # Skip chunks that are too small
                chunks.append({"source": path.name, "text": chunk})
    print(f"✅ {len(chunks)} chunks loaded from {folder}")
    return chunks


# ── Step 2: Build embeddings and store in FAISS index ───────────────────────
def build_index(chunks: list[dict]):
    """Create a FAISS vector index for fast search queries."""
    embed_model = SentenceTransformer(EMBED_MODEL)
    texts = [c["text"] for c in chunks]
    embeddings = embed_model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings, dtype="float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embed_model, chunks


# ── Step 3: Retrieve relevant chunks ───────────────────────────────────────
def search_relevant_chunks(question: str, index, embed_model, chunks) -> list[dict]:
    """Search for the most relevant document chunks for a question."""
    question_embedding = embed_model.encode([question], dtype="float32")
    _, indices = index.search(question_embedding, MAX_CONTEXT_CHUNKS)
    return [chunks[i] for i in indices[0]]


# ── Step 4: Answer question with Claude ─────────────────────────────────────
def answer_question(question: str, relevant_chunks: list[dict]) -> str:
    """Send context and question to Claude and receive an answer."""
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    context = "\n\n---\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}" for c in relevant_chunks
    )

    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a helpful assistant that answers questions based on internal documents.
Use ONLY the document fragments below as your source. If the answer is not in the documents, say so explicitly.

DOCUMENTS:
{context}

QUESTION: {question}

Provide a clear, concise answer. Mention the source files you used.""",
            }
        ],
    )
    return message.content[0].text


# ── Main programme ──────────────────────────────────────────────────────────
def main():
    print("📚 Loading documents...")
    chunks = load_documents(DOCS_FOLDER)
    if not chunks:
        print(f"❌ No documents found in '{DOCS_FOLDER}'. Add PDF or TXT files.")
        return

    print("🔍 Building index...")
    index, embed_model, chunks = build_index(chunks)

    print("\n🤖 Document Q&A ready! Type 'stop' to exit.\n")
    while True:
        question = input("Your question: ").strip()
        if question.lower() == "stop":
            break
        if not question:
            continue

        relevant_chunks = search_relevant_chunks(question, index, embed_model, chunks)
        answer = answer_question(question, relevant_chunks)
        print(f"\n💬 Answer:\n{answer}\n")
        print("─" * 60)


if __name__ == "__main__":
    main()
```

**Usage:** Create a folder `./documents`, add your PDFs or TXT files, and run `python rag_qa.py`.

______________________________________________________________________

## 4. Email Classification {#email-classification}

**When to use:** You want to automatically sort incoming e-mails by type, urgency or department.

```python
# email_classifier.py — Email classification with Claude
import os
import json
import anthropic
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# ── Configuration ────────────────────────────────────────────────────────────
MODEL = "claude-haiku-4-5-20251001"

# Adapt these categories to your situation:
CATEGORIES = [
    "Complaint",
    "Information request",
    "Technical issue",
    "Billing",
    "Compliment",
    "Other",
]

URGENCY_LEVELS = ["Low", "Medium", "High", "Critical"]


# ── Classification function ──────────────────────────────────────────────────
def classify_email(subject: str, body: str) -> dict:
    """Classify an e-mail by category and urgency."""
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    prompt = f"""Classify the following e-mail. Return your answer ONLY as a valid JSON object.

E-MAIL SUBJECT: {subject}
E-MAIL BODY: {body[:2000]}  # Limit to 2000 chars for cost control

Return exactly this JSON format:
{{
  "category": "<one of: {', '.join(CATEGORIES)}>",
  "urgency": "<one of: {', '.join(URGENCY_LEVELS)}>",
  "summary": "<one sentence describing the core of the e-mail>",
  "confidence": <number 0.0 to 1.0>,
  "rationale": "<brief explanation of why you chose this classification>"
}}"""

    message = client.messages.create(
        model=MODEL,
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )

    try:
        return json.loads(message.content[0].text)
    except json.JSONDecodeError:
        # Fallback if JSON parsing fails
        return {
            "category": "Other",
            "urgency": "Medium",
            "summary": "Classification failed — manual review required",
            "confidence": 0.0,
            "rationale": message.content[0].text,
        }


# ── Batch processing from CSV ───────────────────────────────────────────────
def process_csv(input_file: str, output_file: str):
    """
    Expects a CSV with columns: 'subject', 'body'
    Writes results to output_file.
    """
    df = pd.read_csv(input_file)
    results = []

    for idx, row in df.iterrows():
        print(f"Processing {idx + 1}/{len(df)}: {row['subject'][:50]}...")
        result = classify_email(row["subject"], row["body"])
        results.append({**row.to_dict(), **result})

    result_df = pd.DataFrame(results)
    result_df.to_csv(output_file, index=False)
    print(f"\n✅ Results saved to '{output_file}'")

    # Show summary
    print("\n📊 Category distribution:")
    print(result_df["category"].value_counts().to_string())
    print("\n🚨 Urgency distribution:")
    print(result_df["urgency"].value_counts().to_string())


# ── Interactive mode (for testing) ──────────────────────────────────────────
def interactive_mode():
    print("📧 Email Classifier — type 'stop' to exit\n")
    while True:
        subject = input("Subject: ").strip()
        if subject.lower() == "stop":
            break
        body = input("Body (or press Enter for empty): ").strip()

        result = classify_email(subject, body)
        print(f"\n📋 Classification:")
        print(f"  Category:   {result['category']}")
        print(f"  Urgency:    {result['urgency']}")
        print(f"  Summary:    {result['summary']}")
        print(f"  Confidence: {result['confidence']:.0%}")
        print(f"  Rationale:  {result['rationale']}")
        print("─" * 60)


# ── Main programme ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        # Batch mode: python email_classifier.py input.csv output.csv
        process_csv(sys.argv[1], sys.argv[2])
    else:
        # Interactive mode
        interactive_mode()
```

**Usage:**

- Interactive: `python email_classifier.py`
- Batch: `python email_classifier.py emails.csv results.csv`
- CSV format: columns `subject` and `body` required.

______________________________________________________________________

## 5. Content Generation {#content-generation}

**When to use:** You want to generate structured text based on input data (summarised reports, product descriptions, newsletter articles).

```python
# content_generator.py — Structured content generation with Claude
import os
import json
import anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# ── Configuration ────────────────────────────────────────────────────────────
MODEL = "claude-sonnet-4-6"  # Sonnet for higher quality in content generation

# ── Template definitions ─────────────────────────────────────────────────────
# Add your own templates or adapt existing ones.
TEMPLATES = {
    "project_update": {
        "description": "Weekly project status update for stakeholders",
        "input_fields": ["project_name", "progress", "completed_tasks", "risks", "next_steps"],
        "prompt_template": """Write a professional weekly project update for stakeholders.
Keep the tone business-like but approachable. Maximum 250 words.

Project: {project_name}
Progress: {progress}
Completed tasks: {completed_tasks}
Risks: {risks}
Next steps: {next_steps}

Write the update with the following structure:
1. Summary (2 sentences)
2. What was achieved
3. Points of attention
4. Next week""",
    },
    "product_description": {
        "description": "Product description for webshop or catalogue",
        "input_fields": ["product_name", "features", "target_audience", "price", "tone"],
        "prompt_template": """Write a compelling product description.
Tone: {tone} (e.g. professional, enthusiastic, technical)

Product: {product_name}
Features: {features}
Target audience: {target_audience}
Price: {price}

Maximum 150 words. Close with a clear call to action.""",
    },
    "summary": {
        "description": "Summary of a long document or meeting notes",
        "input_fields": ["document_text", "target_audience", "max_length"],
        "prompt_template": """Create a concise summary of the text below.
Target audience: {target_audience}
Maximum length: {max_length} words

Use this structure:
- 1 sentence core message
- 3–5 bullet points with the key takeaways
- 1 sentence recommended follow-up action (if applicable)

TEXT TO SUMMARISE:
{document_text}""",
    },
}


# ── Generation function ─────────────────────────────────────────────────────
def generate_content(template_name: str, inputs: dict) -> str:
    """Generate content based on a template and input data."""
    if template_name not in TEMPLATES:
        raise ValueError(f"Unknown template: '{template_name}'. Choose from: {list(TEMPLATES.keys())}")

    template = TEMPLATES[template_name]
    prompt = template["prompt_template"].format(**inputs)

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


# ── Batch processing from JSON ──────────────────────────────────────────────
def process_batch(input_file: str, output_folder: str):
    """
    Process a JSON file with multiple generation tasks.
    Format: [{"template": "...", "filename": "...", "inputs": {...}}, ...]
    """
    Path(output_folder).mkdir(exist_ok=True)
    tasks = json.loads(Path(input_file).read_text(encoding="utf-8"))

    for i, task in enumerate(tasks):
        print(f"Generating {i + 1}/{len(tasks)}: {task.get('filename', 'output')}")
        content = generate_content(task["template"], task["inputs"])
        output_path = Path(output_folder) / f"{task.get('filename', f'output_{i+1}')}.md"
        output_path.write_text(content, encoding="utf-8")
        print(f"  ✅ Saved: {output_path}")


# ── Interactive mode ────────────────────────────────────────────────────────
def interactive_mode():
    print("✍️  Content Generator\n")
    print("Available templates:")
    for name, info in TEMPLATES.items():
        print(f"  - {name}: {info['description']}")

    print()
    template_name = input("Choose a template: ").strip()
    if template_name not in TEMPLATES:
        print(f"❌ Unknown template. Choose from: {list(TEMPLATES.keys())}")
        return

    template = TEMPLATES[template_name]
    print(f"\nFill in the input fields for '{template_name}':")
    inputs = {}
    for field in template["input_fields"]:
        value = input(f"  {field}: ").strip()
        inputs[field] = value

    print("\n⏳ Generating...")
    result = generate_content(template_name, inputs)
    print(f"\n📝 Result:\n{'─' * 60}\n{result}\n{'─' * 60}")

    save = input("\nSave? (filename without .md, or Enter to skip): ").strip()
    if save:
        Path(f"{save}.md").write_text(result, encoding="utf-8")
        print(f"✅ Saved as '{save}.md'")


# ── Main programme ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        # Batch mode: python content_generator.py tasks.json output_folder/
        process_batch(sys.argv[1], sys.argv[2])
    else:
        interactive_mode()
```

**Usage:**

- Interactive: `python content_generator.py`
- Batch: `python content_generator.py tasks.json output/`
- Batch JSON format:

```json
[
  {
    "template": "project_update",
    "filename": "update-week-12",
    "inputs": {
      "project_name": "AI Email Assistant",
      "progress": "65%",
      "completed_tasks": "RAG index built, first 20 test cases processed",
      "risks": "Data quality of old documents",
      "next_steps": "Expand Golden Set to 50 cases"
    }
  }
]
```

______________________________________________________________________

## 6. Troubleshooting Guide

| Problem                         | Cause                                   | Solution                                             |
| :------------------------------ | :-------------------------------------- | :--------------------------------------------------- |
| `AuthenticationError`           | Invalid or missing API key              | Check `.env` file and `ANTHROPIC_API_KEY`            |
| `RateLimitError`                | Too many requests per minute            | Add `time.sleep(1)` between API calls                |
| `JSONDecodeError` in classifier | Claude sometimes returns invalid JSON   | Use the built-in fallback; consider strict JSON mode |
| Empty embedding index           | No documents found in folder            | Check file extensions (.pdf, .txt) and folder path   |
| High API costs                  | Chunks too large or too much context    | Reduce `CHUNK_SIZE` or `MAX_CONTEXT_CHUNKS`          |
| Poor RAG results                | Documents too large or poorly segmented | Experiment with `CHUNK_SIZE` (200–1,000 characters)  |

______________________________________________________________________

## 7. Related Modules

- [30-Day Plan](01-30-dagen-plan.md) — when and how to use the scaffold code
- [Technical Standards](../08-technische-standaarden/index.md) — for production-ready implementations
- [SDD Pattern](../04-fase-ontwikkeling/05-sdd-patroon.md) — test-first approach after the prototype phase
- [MLOps Standards](../08-technische-standaarden/01-mloops-standaarden.md) — monitoring after go-live
