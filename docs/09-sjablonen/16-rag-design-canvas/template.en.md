---
versie: '1.0'
type: template
layer: 3
phase: [3]
roles: [Data Scientist]
tags: [rag, template]
---

# RAG Design Canvas

Use this canvas to design and document the architecture of a **Retrieval-Augmented Generation (RAG)** system. Complete it together with the Tech Lead, Data Scientist and Context Builder.

!!! info "When to complete this canvas?"
    Required when the AI system gains access to more than one knowledge source (documents, databases, APIs). See also the [Context Builder role](../../08-rollen-en-verantwoordelijkheden/index.md) and [AI Architecture](../../08-technische-standaarden/05-ai-architectuur.md).

______________________________________________________________________

## A. Use Case & Trigger

| Field                          | Fill in                                                                    |
| :----------------------------- | :------------------------------------------------------------------------- |
| **User question**              | What does the end user typically ask?                                      |
| **Trigger**                    | When is RAG activated? (always / on low confidence / on specific keywords) |
| **What may the model NOT do?** | Hard Boundaries for the retrieval path (e.g. never give medical advice)    |
| **Expected response format**   | Text / Table / JSON / Cited answer with sources                            |

______________________________________________________________________

## B. Document Inventory

| Knowledge source           | File format      | Volume (estimated)           | Update frequency        | Owner    |
| :------------------------- | :--------------- | :--------------------------- | :---------------------- | :------- |
| \[E.g. Product catalogue\] | PDF / DOCX / CSV | \[number of documents / MB\] | Daily / Weekly / Static | \[name\] |
|                            |                  |                              |                         |          |
|                            |                  |                              |                         |          |

**Context pollution risk:** Is there a risk that irrelevant sources degrade model responses? ☐ Yes → see Section G · ☐ No

______________________________________________________________________

## C. Chunking Strategy

| Parameter               | Choice                                                    | Motivation |
| :---------------------- | :-------------------------------------------------------- | :--------- |
| **Split method**        | ☐ Fixed size · ☐ Section-based · ☐ Paragraph · ☐ Semantic |            |
| **Chunk size (tokens)** | \[e.g. 512 tokens\]                                       |            |
| **Overlap (tokens)**    | \[e.g. 64 tokens\]                                        |            |
| **Metadata per chunk**  | ☐ Source title · ☐ Page number · ☐ Date · ☐ Author        |            |

!!! tip "Guideline"
    Use section-based chunking for structured documents (reports, manuals). Use fixed size + overlap for continuous text. Larger chunks provide more context but higher cost per retrieval.

______________________________________________________________________

## D. Embedding Model

| Parameter              | Choice                                                                    |
| :--------------------- | :------------------------------------------------------------------------ |
| **Model**              | \[e.g. text-embedding-3-small (OpenAI) / embed-multilingual-v3 (Cohere)\] |
| **Dimensions**         | \[e.g. 1536\]                                                             |
| **Provider**           | \[e.g. OpenAI / Cohere / Hugging Face / local\]                           |
| **Multilingual?**      | ☐ Yes (NL + EN) · ☐ No                                                    |
| **Cost per 1M tokens** | \[e.g. €0.02\]                                                            |

______________________________________________________________________

## E. Vector Store

| Parameter                  | Choice                                                                         |
| :------------------------- | :----------------------------------------------------------------------------- |
| **Technology**             | ☐ Pinecone · ☐ Weaviate · ☐ pgvector · ☐ Chroma · ☐ Qdrant · ☐ Other: \_\_\_\_ |
| **Hosting model**          | ☐ Cloud (managed) · ☐ Self-hosted · ☐ In-memory (dev/test)                     |
| **Indexing strategy**      | ☐ Flat · ☐ HNSW · ☐ IVF                                                        |
| **Estimated vector count** | \[e.g. 50,000 chunks\]                                                         |
| **Backup & recovery**      | ☐ Daily · ☐ Weekly · ☐ N/A                                                     |

______________________________________________________________________

## F. Retriever Parameters

| Parameter                | Value                           | Motivation                                         |
| :----------------------- | :------------------------------ | :------------------------------------------------- |
| **Top-K**                | \[e.g. 5\]                      | How many chunks are passed to the LLM?             |
| **Similarity threshold** | \[e.g. ≥ 0.75\]                 | Minimum cosine similarity for inclusion in context |
| **Re-ranking?**          | ☐ Yes (model: \_\_\_\_) · ☐ No  | Cross-encoder re-ranking increases precision       |
| **Hybrid search?**       | ☐ Yes (keyword + vector) · ☐ No |                                                    |
| **Max context (tokens)** | \[e.g. 4096\]                   | Total context limit for retrieval output           |

______________________________________________________________________

## G. Context Quality & CDL

The **Context Builder** manages the Context Development Lifecycle (CDL): which information is current, what is outdated?

| Check                                                                        | Status                                   |
| :--------------------------------------------------------------------------- | :--------------------------------------- |
| Is there a process for removing outdated documents?                          | ☐ Yes · ☐ No → action required           |
| Are irrelevant chunks filtered before LLM call?                              | ☐ Yes · ☐ No                             |
| Has the maximum context size been determined (context pollution prevention)? | ☐ Yes · ☐ No                             |
| Are source citations included in the response?                               | ☐ Yes · ☐ No                             |
| Has the Context Builder role been assigned?                                  | ☐ Yes, name: \_\_\_\_ · ☐ No — automated |

______________________________________________________________________

## H. Quality Metrics

| Metric                                                                               | Definition                                           | Target       | Measurement                      |
| :----------------------------------------------------------------------------------- | :--------------------------------------------------- | :----------- | :------------------------------- |
| **Precision@K**                                                                      | % relevant chunks in top-K results                   | ≥ 80%        | Offline evaluation on Golden Set |
| **Recall@K**                                                                         | % relevant chunks retrieved                          | ≥ 70%        | Offline evaluation on Golden Set |
| **Faithfulness**                                                                     | Answer based on retrieved context (no hallucination) | ≥ 90%        | RAGAS or manual review           |
| **Answer Relevance**                                                                 | Answer relevant to the question asked                | ≥ 85%        | RAGAS or manual review           |
| **Latency (p95)** (95th percentile — 95% of all requests are faster than this value) | Retrieval + generation time                          | \< 3 seconds | Production monitoring            |

______________________________________________________________________

## I. Cost Estimate

| Cost item                 | Unit                | Estimated volume/month | Unit price | Monthly cost (€) |
| :------------------------ | :------------------ | :--------------------- | :--------- | :--------------- |
| Embedding (initial)       | per 1M tokens       | \[one-time\]           |            |                  |
| Embedding (updates)       | per 1M tokens/month |                        |            |                  |
| Vector store storage      | per GB/month        |                        |            |                  |
| LLM inference (retrieval) | per 1M tokens       |                        |            |                  |
| **Total (month)**         |                     |                        |            |                  |

See also: [Cost Optimisation](../../08-technische-standaarden/07-kostenoptimalisatie.md) and GAINS™ framework for ROI linkage.

______________________________________________________________________

## J. Approval

| Role            | Name | Date | Signature |
| :-------------- | :--- | :--- | :-------- |
| Tech Lead       |      |      |           |
| Data Scientist  |      |      |           |
| Context Builder |      |      |           |
| Guardian        |      |      |           |

______________________________________________________________________

**Related modules:**

- [AI Architecture — RAG pattern](../../08-technische-standaarden/05-ai-architectuur.md)
- [Roles & Responsibilities — Context Builder](../../08-rollen-en-verantwoordelijkheden/index.md)
- [Cost Optimisation](../../08-technische-standaarden/07-kostenoptimalisatie.md)
- [Technical Model Card](../02-business-case/modelkaart.md)
