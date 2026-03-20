---
versie: '1.0'
type: template
layer: 3
phase: [3]
roles: [Data Scientist]
tags: [rag, template]
answers: [Hoe gebruik ik het RAG Design Canvas sjabloon?]
---

# RAG Design Canvas

Gebruik dit canvas om de architectuur van een **Retrieval-Augmented Generation (RAG)**-systeem te ontwerpen en te documenteren. Vul het in samen met de Tech Lead, Data Scientist en Context Builder.

!!! info "Wanneer dit canvas invullen?"
    Verplicht wanneer het AI-systeem toegang krijgt tot meer dan één kennisbron (documenten, databases, API's). Zie ook de [Context Builder-rol](../../08-rollen-en-verantwoordelijkheden/index.md) en [AI Architectuur](../../08-technische-standaarden/05-ai-architectuur.md).

______________________________________________________________________

## A. Use Case & Trigger

| Veld                             | Invullen                                                                                   |
| :------------------------------- | :----------------------------------------------------------------------------------------- |
| **Gebruikersvraag**              | Wat stelt de eindgebruiker typisch?                                                        |
| **Trigger**                      | Wanneer wordt RAG geactiveerd? (altijd / bij lage confidence / bij specifieke trefwoorden) |
| **Wat mag het model NIET doen?** | Harde Grenzen voor het retrieval-pad (bijv. nooit medisch advies geven)                    |
| **Verwacht responsformaat**      | Tekst / Tabel / JSON / Geciteerd antwoord met bronnen                                      |

______________________________________________________________________

## B. Documentinventaris

| Kennisbron                 | Bestandsformaat  | Omvang (geschat)           | Updatefrequentie                 | Eigenaar |
| :------------------------- | :--------------- | :------------------------- | :------------------------------- | :------- |
| \[Bijv. Productcatalogus\] | PDF / DOCX / CSV | \[aantal documenten / MB\] | Dagelijks / Wekelijks / Statisch | \[naam\] |
|                            |                  |                            |                                  |          |
|                            |                  |                            |                                  |          |

**Context pollution risico:** Is er kans dat irrelevante bronnen de modelrespons degraderen? ☐ Ja → zie sectie G · ☐ Nee

______________________________________________________________________

## C. Chunking Strategie

| Parameter                  | Keuze                                                         | Motivatie |
| :------------------------- | :------------------------------------------------------------ | :-------- |
| **Split-methode**          | ☐ Vaste grootte · ☐ Sectiegebaseerd · ☐ Alinea · ☐ Semantisch |           |
| **Chunk-grootte (tokens)** | \[bijv. 512 tokens\]                                          |           |
| **Overlap (tokens)**       | \[bijv. 64 tokens\]                                           |           |
| **Metadata per chunk**     | ☐ Brontitel · ☐ Paginanummer · ☐ Datum · ☐ Auteur             |           |

!!! tip "Richtlijn"
    Gebruik sectiegebaseerde chunking bij gestructureerde documenten (rapporten, handleidingen). Gebruik vaste grootte + overlap bij doorlopende tekst. Grotere chunks geven meer context maar hogere kosten per retrieval.

______________________________________________________________________

## D. Embedding Model

| Parameter                | Keuze                                                                      |
| :----------------------- | :------------------------------------------------------------------------- |
| **Model**                | \[bijv. text-embedding-3-small (OpenAI) / embed-multilingual-v3 (Cohere)\] |
| **Dimensies**            | \[bijv. 1536\]                                                             |
| **Provider**             | \[bijv. OpenAI / Cohere / Hugging Face / lokaal\]                          |
| **Meertalig?**           | ☐ Ja (NL + EN) · ☐ Nee                                                     |
| **Kosten per 1M tokens** | \[bijv. €0,02\]                                                            |

______________________________________________________________________

## E. Vectorstore

| Parameter                 | Keuze                                                                           |
| :------------------------ | :------------------------------------------------------------------------------ |
| **Technologie**           | ☐ Pinecone · ☐ Weaviate · ☐ pgvector · ☐ Chroma · ☐ Qdrant · ☐ Anders: \_\_\_\_ |
| **Hostingmodel**          | ☐ Cloud (managed) · ☐ Self-hosted · ☐ In-memory (dev/test)                      |
| **Indexeringsstrategie**  | ☐ Flat · ☐ HNSW · ☐ IVF                                                         |
| **Geschatte vectorcount** | \[bijv. 50.000 chunks\]                                                         |
| **Back-up & herstel**     | ☐ Dagelijks · ☐ Wekelijks · ☐ n.v.t.                                            |

______________________________________________________________________

## F. Retriever Parameters

| Parameter                | Waarde                          | Motivatie                                        |
| :----------------------- | :------------------------------ | :----------------------------------------------- |
| **Top-K**                | \[bijv. 5\]                     | Hoeveel chunks worden meegegeven aan de LLM?     |
| **Similariteitsdrempel** | \[bijv. ≥ 0,75\]                | Minimum cosine similarity voor opname in context |
| **Re-ranking?**          | ☐ Ja (model: \_\_\_\_) · ☐ Nee  | Cross-encoder re-ranking verhoogt precisie       |
| **Hybride zoeken?**      | ☐ Ja (keyword + vector) · ☐ Nee |                                                  |
| **Max context (tokens)** | \[bijv. 4096\]                  | Totale contextlimiet voor retrieval-output       |

______________________________________________________________________

## G. Context Kwaliteit & CDL

De **Context Builder** beheert de Context Development Lifecycle (CDL): welke informatie is actueel, wat is verouderd?

| Check                                                                | Status                                         |
| :------------------------------------------------------------------- | :--------------------------------------------- |
| Is er een proces voor het verwijderen van verouderde documenten?     | ☐ Ja · ☐ Nee → actie vereist                   |
| Worden irrelevante chunks gefilterd vóór LLM-aanroep?                | ☐ Ja · ☐ Nee                                   |
| Is de maximale contextgrootte bepaald (context pollution preventie)? | ☐ Ja · ☐ Nee                                   |
| Worden bronvermeldingen in het antwoord opgenomen?                   | ☐ Ja · ☐ Nee                                   |
| Is de Context Builder-rol toegewezen?                                | ☐ Ja, naam: \_\_\_\_ · ☐ Nee — geautomatiseerd |

______________________________________________________________________

## H. Kwaliteitsmetrieken

| Metriek                                                                                | Definitie                                                    | Doelwaarde    | Meting                          |
| :------------------------------------------------------------------------------------- | :----------------------------------------------------------- | :------------ | :------------------------------ |
| **Precision@K**                                                                        | % relevante chunks in de top-K resultaten                    | ≥ 80%         | Offline evaluatie op Golden Set |
| **Recall@K**                                                                           | % relevante chunks teruggevonden                             | ≥ 70%         | Offline evaluatie op Golden Set |
| **Faithfulness**                                                                       | Antwoord gebaseerd op opgehaalde context (geen hallucinatie) | ≥ 90%         | RAGAS of handmatige beoordeling |
| **Answer Relevance**                                                                   | Antwoord relevant voor de gestelde vraag                     | ≥ 85%         | RAGAS of handmatige beoordeling |
| **Latency (p95)** (95e percentiel — 95% van alle verzoeken is sneller dan deze waarde) | Retrieval + generatie tijd                                   | \< 3 seconden | Productie monitoring            |

______________________________________________________________________

## I. Kosteninschatting

| Kostenpost                 | Eenheid             | Geschat volume/maand | Eenheidsprijs | Maandkosten (€) |
| :------------------------- | :------------------ | :------------------- | :------------ | :-------------- |
| Embedding (initieel)       | per 1M tokens       | \[eenmalig\]         |               |                 |
| Embedding (updates)        | per 1M tokens/maand |                      |               |                 |
| Vectorstore opslag         | per GB/maand        |                      |               |                 |
| LLM-inferentie (retrieval) | per 1M tokens       |                      |               |                 |
| **Totaal (maand)**         |                     |                      |               |                 |

Zie ook: [Kostenoptimalisatie](../../08-technische-standaarden/07-kostenoptimalisatie.md) en GAINS™ framework voor ROI-koppeling.

______________________________________________________________________

## J. Goedkeuring

| Rol             | Naam | Datum | Handtekening |
| :-------------- | :--- | :---- | :----------- |
| Tech Lead       |      |       |              |
| Data Scientist  |      |       |              |
| Context Builder |      |       |              |
| Guardian        |      |       |              |

______________________________________________________________________

**Gerelateerde modules:**

- [AI Architectuur — RAG-patroon](../../08-technische-standaarden/05-ai-architectuur.md)
- [Rollen & Verantwoordelijkheden — Context Builder](../../08-rollen-en-verantwoordelijkheden/index.md)
- [Kostenoptimalisatie](../../08-technische-standaarden/07-kostenoptimalisatie.md)
- [Technische Model Card](../02-business-case/modelkaart.md)
