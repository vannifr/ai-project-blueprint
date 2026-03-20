"""Load and index all Blueprint documentation at startup.

Scans docs/ for markdown files, parses frontmatter, and builds
O(1) lookup indexes by path, type, phase, tag, and layer.
"""

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

RE_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
RE_H1 = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def parse_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter from markdown text using simple regex."""
    m = RE_FRONTMATTER.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        # Parse list values: [a, b, c]
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                fm[key] = []
            else:
                items = []
                for item in inner.split(","):
                    item = item.strip().strip("'\"")
                    # Try to parse as int
                    try:
                        items.append(int(item))
                    except ValueError:
                        items.append(item)
                fm[key] = items
        else:
            # Scalar value
            value = value.strip("'\"")
            try:
                fm[key] = int(value)
            except ValueError:
                fm[key] = value
    return fm


def extract_body(text: str) -> str:
    """Return markdown content without frontmatter."""
    m = RE_FRONTMATTER.match(text)
    if m:
        return text[m.end():]
    return text


def extract_title(body: str) -> str:
    """Extract first H1 heading from markdown body."""
    m = RE_H1.search(body)
    return m.group(1).strip() if m else ""


@dataclass
class Document:
    path: str  # relative to docs/ (e.g. "02-fase-ontdekking/02-activiteiten.en.md")
    title: str
    frontmatter: dict
    body: str
    language: str  # "nl" or "en"

    @property
    def type(self) -> str:
        return self.frontmatter.get("type", "")

    @property
    def layer(self) -> int | None:
        v = self.frontmatter.get("layer")
        return int(v) if v is not None else None

    @property
    def phases(self) -> list[int]:
        p = self.frontmatter.get("phase", [])
        if isinstance(p, list):
            return [int(x) for x in p]
        return [int(p)] if p else []

    @property
    def roles(self) -> list[str]:
        return self.frontmatter.get("roles", [])

    @property
    def tags(self) -> list[str]:
        return self.frontmatter.get("tags", [])

    @property
    def summary(self) -> str:
        return self.frontmatter.get("summary", "")

    @property
    def answers(self) -> list[str]:
        a = self.frontmatter.get("answers", [])
        return a if isinstance(a, list) else [a] if a else []


@dataclass
class ContentIndex:
    docs: list[Document] = field(default_factory=list)
    by_path: dict[str, Document] = field(default_factory=dict)
    by_type: dict[str, list[Document]] = field(default_factory=dict)
    by_phase: dict[int, list[Document]] = field(default_factory=dict)
    by_tag: dict[str, list[Document]] = field(default_factory=dict)
    by_layer: dict[int, list[Document]] = field(default_factory=dict)

    @classmethod
    def load(cls, docs_root: Path, language: str = "en") -> "ContentIndex":
        """Scan docs/ directory and build lookup indexes."""
        index = cls()
        docs_root = Path(docs_root)

        for md_path in sorted(docs_root.rglob("*.md")):
            rel = md_path.relative_to(docs_root).as_posix()

            # Language filtering
            if language == "en":
                if not rel.endswith(".en.md"):
                    continue
            else:
                # NL: skip .en.md files
                if rel.endswith(".en.md"):
                    continue

            text = md_path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            body = extract_body(text)
            title = extract_title(body)

            doc = Document(
                path=rel,
                title=title,
                frontmatter=fm,
                body=body,
                language=language,
            )

            index.docs.append(doc)
            index.by_path[rel] = doc

            # Type index
            if doc.type:
                index.by_type.setdefault(doc.type, []).append(doc)

            # Phase index
            for phase in doc.phases:
                index.by_phase.setdefault(phase, []).append(doc)

            # Tag index
            for tag in doc.tags:
                index.by_tag.setdefault(tag, []).append(doc)

            # Layer index
            if doc.layer is not None:
                index.by_layer.setdefault(doc.layer, []).append(doc)

        return index

    def search(
        self,
        query: str,
        type: str | None = None,
        phase: int | None = None,
        layer: int | None = None,
        tag: str | None = None,
        limit: int = 10,
    ) -> list[Document]:
        """Case-insensitive keyword search with optional frontmatter filters."""
        candidates = self.docs

        if type:
            candidates = [d for d in candidates if d.type == type]
        if phase is not None:
            candidates = [d for d in candidates if phase in d.phases]
        if layer is not None:
            candidates = [d for d in candidates if d.layer == layer]
        if tag:
            candidates = [d for d in candidates if tag in d.tags]

        if not query:
            return candidates[:limit]

        query_lower = query.lower()
        results = []
        for doc in candidates:
            searchable = (doc.title + " " + doc.path + " " + doc.body).lower()
            if query_lower in searchable:
                results.append(doc)
            if len(results) >= limit:
                break

        return results

    def get_phase_docs(self, phase: int, aspect: str) -> list[Document]:
        """Get objectives/activities/deliverables for a phase.

        aspect: "objectives", "activities", or "deliverables"
        """
        phase_docs = self.by_phase.get(phase, [])
        return [d for d in phase_docs if d.type == aspect]

    def get_templates(self) -> list[Document]:
        """All type=template documents."""
        return self.by_type.get("template", [])

    def get_by_tag(self, tag: str) -> list[Document]:
        """Filter by semantic tag."""
        return self.by_tag.get(tag, [])

    def search_by_question(self, question: str, limit: int = 5) -> list[Document]:
        """Find documents whose answers[] or summary best match a question.

        Scores documents by keyword overlap between the question and
        their answers + summary + title fields.
        """
        q_words = set(question.lower().split())
        scored: list[tuple[float, Document]] = []

        for doc in self.docs:
            score = 0.0
            # Check answers (highest weight)
            for answer in doc.answers:
                a_words = set(answer.lower().split())
                overlap = len(q_words & a_words)
                if overlap > 0:
                    score += overlap * 3.0

            # Check summary
            if doc.summary:
                s_words = set(doc.summary.lower().split())
                score += len(q_words & s_words) * 1.5

            # Check title
            if doc.title:
                t_words = set(doc.title.lower().split())
                score += len(q_words & t_words) * 2.0

            if score > 0:
                scored.append((score, doc))

        scored.sort(key=lambda x: -x[0])
        return [doc for _, doc in scored[:limit]]
