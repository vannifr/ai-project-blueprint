---
versie: '1.0'
---

# Scaffold Code — Startcode voor 3 Use Cases

## 1. Overzicht

Deze pagina bevat werkende Python-startcode voor de drie meest voorkomende AI use cases in de Verkenner-fase. Kopieer de code die bij uw use case past en pas hem aan uw situatie aan.

| Use Case                                       | Techniek                             | Geschikt voor                                           |
| :--------------------------------------------- | :----------------------------------- | :------------------------------------------------------ |
| [📄 Document Q&A](#document-qa)                | RAG (Retrieval-Augmented Generation) | Vragen over interne documenten, handleidingen, beleid   |
| [📧 E-mailclassificatie](#email-classificatie) | LLM classificatie                    | Sorteren en prioriteren van inkomende berichten         |
| [✍️ Contentgeneratie](#contentgeneratie)       | Gestructureerde prompting            | Rapportages, productbeschrijvingen, samengevatte inhoud |

!!! warning "Vereiste API-sleutel"
    Alle voorbeelden gebruiken de **Anthropic Claude API**. Vraag een API-sleutel aan via [console.anthropic.com](https://console.anthropic.com) en sla hem op in een `.env` bestand (zie sectie Installatie). Vervang `claude-haiku-4-5-20251001` door een ander model indien gewenst.

______________________________________________________________________

## 2. Installatie

### 2.1 Vereisten

```bash
# Maak een virtual environment aan
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Installeer dependencies
pip install anthropic python-dotenv pypdf2 faiss-cpu sentence-transformers pandas
```

### 2.2 .env bestand

Maak een `.env` bestand aan in de root van uw project:

```bash
# .env — voeg dit bestand toe aan .gitignore!
ANTHROPIC_API_KEY=sk-ant-...
```

### 2.3 Docker-setup (optioneel)

Voor een geïsoleerde omgeving met Jupyter:

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

Start met: `docker compose up`

______________________________________________________________________

## 3. Document Q&A (RAG) {#document-qa}

**Wanneer gebruiken:** U wilt dat gebruikers vragen kunnen stellen over interne documenten (beleid, handleidingen, FAQ's).

```python
# rag_qa.py — Document Q&A met RAG en Claude
import os
import anthropic
from dotenv import load_dotenv
from pathlib import Path
import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

load_dotenv()

# ── Configuratie ─────────────────────────────────────────────────────────────
DOCS_FOLDER = "./documenten"        # Map met uw PDF/TXT bestanden
MODEL = "claude-haiku-4-5-20251001"  # Snel en goedkoop voor prototypes
EMBED_MODEL = "all-MiniLM-L6-v2"    # Lokaal embedding model (geen API-kosten)
CHUNK_SIZE = 500                     # Tekens per chunk
MAX_CONTEXT_CHUNKS = 4               # Aantal chunks meegestuurd naar Claude


# ── Stap 1: Documenten laden en in chunks verdelen ───────────────────────────
def laad_documenten(folder: str) -> list[dict]:
    """Laad alle PDF- en TXT-bestanden uit een map."""
    chunks = []
    for pad in Path(folder).rglob("*"):
        if pad.suffix == ".pdf":
            with open(pad, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                tekst = " ".join(p.extract_text() or "" for p in reader.pages)
        elif pad.suffix == ".txt":
            tekst = pad.read_text(encoding="utf-8")
        else:
            continue

        # Verdeel in overlappende chunks
        for i in range(0, len(tekst), CHUNK_SIZE - 100):
            chunk = tekst[i : i + CHUNK_SIZE]
            if len(chunk) > 100:  # Sla te kleine chunks over
                chunks.append({"bron": pad.name, "tekst": chunk})
    print(f"✅ {len(chunks)} chunks geladen uit {folder}")
    return chunks


# ── Stap 2: Embeddings bouwen en opslaan in FAISS-index ─────────────────────
def bouw_index(chunks: list[dict]):
    """Creëer een FAISS vector index voor snelle zoekquery's."""
    embed_model = SentenceTransformer(EMBED_MODEL)
    teksten = [c["tekst"] for c in chunks]
    embeddings = embed_model.encode(teksten, show_progress_bar=True)
    embeddings = np.array(embeddings, dtype="float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embed_model, chunks


# ── Stap 3: Relevante chunks ophalen ─────────────────────────────────────────
def zoek_relevante_chunks(vraag: str, index, embed_model, chunks) -> list[dict]:
    """Zoek de meest relevante document-chunks voor een vraag."""
    vraag_embedding = embed_model.encode([vraag], dtype="float32")
    _, indices = index.search(vraag_embedding, MAX_CONTEXT_CHUNKS)
    return [chunks[i] for i in indices[0]]


# ── Stap 4: Vraag beantwoorden met Claude ────────────────────────────────────
def beantwoord_vraag(vraag: str, relevante_chunks: list[dict]) -> str:
    """Stuur de context en vraag naar Claude en ontvang een antwoord."""
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    context = "\n\n---\n\n".join(
        f"[Bron: {c['bron']}]\n{c['tekst']}" for c in relevante_chunks
    )

    bericht = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""U bent een behulpzame assistent die vragen beantwoordt op basis van interne documenten.
Gebruik ALLEEN de onderstaande documentfragmenten als bron. Als het antwoord niet in de documenten staat, zeg dat dan expliciet.

DOCUMENTEN:
{context}

VRAAG: {vraag}

Geef een helder, beknopt antwoord. Vermeld de bronbestanden die u gebruikte.""",
            }
        ],
    )
    return bericht.content[0].text


# ── Hoofdprogramma ────────────────────────────────────────────────────────────
def main():
    print("📚 Documenten laden...")
    chunks = laad_documenten(DOCS_FOLDER)
    if not chunks:
        print(f"❌ Geen documenten gevonden in '{DOCS_FOLDER}'. Voeg PDF- of TXT-bestanden toe.")
        return

    print("🔍 Index bouwen...")
    index, embed_model, chunks = bouw_index(chunks)

    print("\n🤖 Document Q&A klaar! Type 'stop' om te beëindigen.\n")
    while True:
        vraag = input("Uw vraag: ").strip()
        if vraag.lower() == "stop":
            break
        if not vraag:
            continue

        relevante_chunks = zoek_relevante_chunks(vraag, index, embed_model, chunks)
        antwoord = beantwoord_vraag(vraag, relevante_chunks)
        print(f"\n💬 Antwoord:\n{antwoord}\n")
        print("─" * 60)


if __name__ == "__main__":
    main()
```

**Gebruik:** Maak een map `./documenten` aan, voeg uw PDF's of TXT-bestanden toe, en run `python rag_qa.py`.

______________________________________________________________________

## 4. E-mailclassificatie {#email-classificatie}

**Wanneer gebruiken:** U wilt inkomende e-mails automatisch sorteren op type, urgentie of afdeling.

```python
# email_classifier.py — E-mailclassificatie met Claude
import os
import json
import anthropic
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# ── Configuratie ─────────────────────────────────────────────────────────────
MODEL = "claude-haiku-4-5-20251001"

# Pas deze categorieën aan uw situatie aan:
CATEGORIEEN = [
    "Klacht",
    "Informatieverzoek",
    "Technisch probleem",
    "Facturatie",
    "Compliment",
    "Overig",
]

URGENTIENIVEAUS = ["Laag", "Middel", "Hoog", "Kritiek"]


# ── Classificatiefunctie ──────────────────────────────────────────────────────
def classificeer_email(onderwerp: str, inhoud: str) -> dict:
    """Classificeer een e-mail op categorie en urgentie."""
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    prompt = f"""Classificeer de volgende e-mail. Geef uw antwoord ALLEEN als geldig JSON-object.

E-MAIL ONDERWERP: {onderwerp}
E-MAIL INHOUD: {inhoud[:2000]}  # Begrens tot 2000 tekens voor kostenbeheersing

Geef precies dit JSON-formaat terug:
{{
  "categorie": "<één van: {', '.join(CATEGORIEEN)}>",
  "urgentie": "<één van: {', '.join(URGENTIENIVEAUS)}>",
  "samenvatting": "<één zin die de kern van de e-mail beschrijft>",
  "vertrouwen": <getal 0.0 tot 1.0>,
  "toelichting": "<kort waarom u deze classificatie koos>"
}}"""

    bericht = client.messages.create(
        model=MODEL,
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )

    try:
        return json.loads(bericht.content[0].text)
    except json.JSONDecodeError:
        # Fallback als JSON parsing mislukt
        return {
            "categorie": "Overig",
            "urgentie": "Middel",
            "samenvatting": "Classificatie mislukt — handmatige review vereist",
            "vertrouwen": 0.0,
            "toelichting": bericht.content[0].text,
        }


# ── Batch-verwerking van een CSV ──────────────────────────────────────────────
def verwerk_csv(invoerbestand: str, uitvoerbestand: str):
    """
    Verwacht een CSV met kolommen: 'onderwerp', 'inhoud'
    Schrijft resultaten naar uitvoerbestand.
    """
    df = pd.read_csv(invoerbestand)
    resultaten = []

    for idx, rij in df.iterrows():
        print(f"Verwerking {idx + 1}/{len(df)}: {rij['onderwerp'][:50]}...")
        resultaat = classificeer_email(rij["onderwerp"], rij["inhoud"])
        resultaten.append({**rij.to_dict(), **resultaat})

    resultaat_df = pd.DataFrame(resultaten)
    resultaat_df.to_csv(uitvoerbestand, index=False)
    print(f"\n✅ Resultaten opgeslagen in '{uitvoerbestand}'")

    # Toon samenvatting
    print("\n📊 Verdeling categorieën:")
    print(resultaat_df["categorie"].value_counts().to_string())
    print("\n🚨 Urgentieverdeling:")
    print(resultaat_df["urgentie"].value_counts().to_string())


# ── Interactieve modus (voor testen) ─────────────────────────────────────────
def interactieve_modus():
    print("📧 E-mail Classifier — type 'stop' om te beëindigen\n")
    while True:
        onderwerp = input("Onderwerp: ").strip()
        if onderwerp.lower() == "stop":
            break
        inhoud = input("Inhoud (of druk Enter voor leeg): ").strip()

        resultaat = classificeer_email(onderwerp, inhoud)
        print(f"\n📋 Classificatie:")
        print(f"  Categorie:   {resultaat['categorie']}")
        print(f"  Urgentie:    {resultaat['urgentie']}")
        print(f"  Samenvatting: {resultaat['samenvatting']}")
        print(f"  Vertrouwen:  {resultaat['vertrouwen']:.0%}")
        print(f"  Toelichting: {resultaat['toelichting']}")
        print("─" * 60)


# ── Hoofdprogramma ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        # Batch-modus: python email_classifier.py invoer.csv uitvoer.csv
        verwerk_csv(sys.argv[1], sys.argv[2])
    else:
        # Interactieve modus
        interactieve_modus()
```

**Gebruik:**

- Interactief: `python email_classifier.py`
- Batch: `python email_classifier.py emails.csv resultaten.csv`
- CSV-formaat: kolommen `onderwerp` en `inhoud` vereist.

______________________________________________________________________

## 5. Contentgeneratie {#contentgeneratie}

**Wanneer gebruiken:** U wilt gestructureerde tekst genereren op basis van invoerdata (samengevatte rapporten, productbeschrijvingen, nieuwsbriefartikelen).

```python
# content_generator.py — Gestructureerde contentgeneratie met Claude
import os
import json
import anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# ── Configuratie ─────────────────────────────────────────────────────────────
MODEL = "claude-sonnet-4-6"  # Sonnet voor hogere kwaliteit bij contentgeneratie

# ── Template-definities ───────────────────────────────────────────────────────
# Voeg uw eigen templates toe of pas bestaande aan.
TEMPLATES = {
    "projectupdate": {
        "beschrijving": "Wekelijkse projectstatusupdate voor stakeholders",
        "invoervelden": ["projectnaam", "voortgang", "voltooide_taken", "risicos", "volgende_stappen"],
        "prompt_template": """Schrijf een professionele wekelijkse projectupdate voor stakeholders.
Houd de toon zakelijk maar toegankelijk. Maximaal 250 woorden.

Project: {projectnaam}
Voortgang: {voortgang}
Voltooide taken: {voltooide_taken}
Risico's: {risicos}
Volgende stappen: {volgende_stappen}

Schrijf de update met de volgende structuur:
1. Samenvatting (2 zinnen)
2. Wat is bereikt
3. Aandachtspunten
4. Volgende week""",
    },
    "productbeschrijving": {
        "beschrijving": "Productbeschrijving voor webshop of catalogus",
        "invoervelden": ["productnaam", "kenmerken", "doelgroep", "prijs", "toon"],
        "prompt_template": """Schrijf een overtuigende productbeschrijving.
Toon: {toon} (bijv. professioneel, enthousiast, technisch)

Product: {productnaam}
Kenmerken: {kenmerken}
Doelgroep: {doelgroep}
Prijs: {prijs}

Maximaal 150 woorden. Sluit af met een duidelijke call-to-action.""",
    },
    "samenvatting": {
        "beschrijving": "Samenvatting van een lang document of vergaderverslag",
        "invoervelden": ["document_tekst", "doelgroep", "maximale_lengte"],
        "prompt_template": """Maak een beknopte samenvatting van de onderstaande tekst.
Doelgroep: {doelgroep}
Maximale lengte: {maximale_lengte} woorden

Gebruik een structuur met:
- 1 zin kernboodschap
- 3–5 bullet points met de belangrijkste punten
- 1 zin aanbevolen vervolgactie (indien van toepassing)

TEKST OM SAMEN TE VATTEN:
{document_tekst}""",
    },
}


# ── Generatiefunctie ──────────────────────────────────────────────────────────
def genereer_content(template_naam: str, invoer: dict) -> str:
    """Genereer content op basis van een template en invoerdata."""
    if template_naam not in TEMPLATES:
        raise ValueError(f"Onbekend template: '{template_naam}'. Kies uit: {list(TEMPLATES.keys())}")

    template = TEMPLATES[template_naam]
    prompt = template["prompt_template"].format(**invoer)

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    bericht = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return bericht.content[0].text


# ── Batch-verwerking vanuit JSON ──────────────────────────────────────────────
def verwerk_batch(invoerbestand: str, uitvoermap: str):
    """
    Verwerk een JSON-bestand met meerdere generatieopdrachten.
    Formaat: [{"template": "...", "bestandsnaam": "...", "invoer": {...}}, ...]
    """
    Path(uitvoermap).mkdir(exist_ok=True)
    taken = json.loads(Path(invoerbestand).read_text(encoding="utf-8"))

    for i, taak in enumerate(taken):
        print(f"Generatie {i + 1}/{len(taken)}: {taak.get('bestandsnaam', 'output')}")
        inhoud = genereer_content(taak["template"], taak["invoer"])
        uitvoerpad = Path(uitvoermap) / f"{taak.get('bestandsnaam', f'output_{i+1}')}.md"
        uitvoerpad.write_text(inhoud, encoding="utf-8")
        print(f"  ✅ Opgeslagen: {uitvoerpad}")


# ── Interactieve modus ────────────────────────────────────────────────────────
def interactieve_modus():
    print("✍️  Content Generator\n")
    print("Beschikbare templates:")
    for naam, info in TEMPLATES.items():
        print(f"  - {naam}: {info['beschrijving']}")

    print()
    template_naam = input("Kies een template: ").strip()
    if template_naam not in TEMPLATES:
        print(f"❌ Onbekend template. Kies uit: {list(TEMPLATES.keys())}")
        return

    template = TEMPLATES[template_naam]
    print(f"\nVul de invoervelden in voor '{template_naam}':")
    invoer = {}
    for veld in template["invoervelden"]:
        waarde = input(f"  {veld}: ").strip()
        invoer[veld] = waarde

    print("\n⏳ Genereren...")
    resultaat = genereer_content(template_naam, invoer)
    print(f"\n📝 Resultaat:\n{'─' * 60}\n{resultaat}\n{'─' * 60}")

    opslaan = input("\nOpslaan? (bestandsnaam zonder .md, of Enter om over te slaan): ").strip()
    if opslaan:
        Path(f"{opslaan}.md").write_text(resultaat, encoding="utf-8")
        print(f"✅ Opgeslagen als '{opslaan}.md'")


# ── Hoofdprogramma ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        # Batch-modus: python content_generator.py taken.json uitvoermap/
        verwerk_batch(sys.argv[1], sys.argv[2])
    else:
        interactieve_modus()
```

**Gebruik:**

- Interactief: `python content_generator.py`
- Batch: `python content_generator.py taken.json uitvoer/`
- Batch JSON-formaat:

```json
[
  {
    "template": "projectupdate",
    "bestandsnaam": "update-week-12",
    "invoer": {
      "projectnaam": "AI E-mailassistent",
      "voortgang": "65%",
      "voltooide_taken": "RAG-index gebouwd, eerste 20 testcases verwerkt",
      "risicos": "Datakwaliteit oude documenten",
      "volgende_stappen": "Golden Set uitbreiden naar 50 cases"
    }
  }
]
```

______________________________________________________________________

## 6. Probleemoplossingsgids

| Probleem                        | Oorzaak                                     | Oplossing                                                  |
| :------------------------------ | :------------------------------------------ | :--------------------------------------------------------- |
| `AuthenticationError`           | Ongeldige of ontbrekende API-sleutel        | Controleer `.env` bestand en `ANTHROPIC_API_KEY`           |
| `RateLimitError`                | Te veel verzoeken per minuut                | Voeg `time.sleep(1)` toe tussen API-calls                  |
| `JSONDecodeError` in classifier | Claude geeft soms geen geldig JSON          | Gebruik de ingebouwde fallback; overweeg strikte JSON-mode |
| Lege embedding-index            | Geen documenten gevonden in map             | Controleer bestandsextensies (.pdf, .txt) en mappad        |
| Hoge API-kosten                 | Te grote chunks of te veel context          | Verklein `CHUNK_SIZE` of `MAX_CONTEXT_CHUNKS`              |
| Slechte RAG-resultaten          | Documenten te groot of slecht gesegmenteerd | Experimenteer met `CHUNK_SIZE` (200–1000 tekens)           |

______________________________________________________________________

## 7. Gerelateerde Modules

- [30-Dagen Plan](01-30-dagen-plan.md) — wanneer en hoe de scaffold code te gebruiken
- [Technische Standaarden](../08-technische-standaarden/index.md) — voor productie-klare implementaties
- [SDD Patroon](../04-fase-ontwikkeling/05-sdd-patroon.md) — test-first aanpak na de prototype-fase
- [MLOps Standaarden](../08-technische-standaarden/01-mloops-standaarden.md) — monitoring na go-live
