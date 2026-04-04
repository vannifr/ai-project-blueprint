# Definition of Done — AI Project Blueprint

**Versie:** 1.0
**Geldig vanaf:** 2026-04-04
**Eigenaar:** Frederik Vannieuwenhuyse
**Status:** Bindend — geen uitzonderingen zonder expliciete beslissing in BACKLOG.md

______________________________________________________________________

> **Kernprincipe:** "Done" betekent: geautomatiseerd geverifieerd, meetbaar correct, en productie-klaar. Checkbox-theater telt niet.

De DoD is gelaagd: elke laag bouwt voort op de vorige. Een feature die laag 2 haalt maar laag 1 niet, is **niet done**.

______________________________________________________________________

## Laag 1 — Documentpagina (elke nieuwe of gewijzigde `.md`)

### 1.1 Frontmatter — geautomatiseerd gecontroleerd door `validate_docs.py`

| Criterium                        | Regel                                                                                                        | Geblokkeerd door         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------ |
| `versie:` aanwezig               | Verplicht in elk bestand                                                                                     | pre-commit + CI          |
| `type:` aanwezig                 | Eén van: `index`, `guide`, `template`, `objectives`, `activities`, `deliverables`, `compliance`, `reference` | pre-commit               |
| `layer:` aanwezig                | `1`, `2` of `3`                                                                                              | pre-commit               |
| `answers:` aanwezig              | Minimaal 1 waarde                                                                                            | pre-commit               |
| Geen generieke answers           | Patroon \`^(Wat is                                                                                           | What is                  |
| Minimaal 2 task-gerichte answers | Begint met actiewoord of specifiek vraagwoord: Welke/Hoe/Wanneer/Wie/Which/How/When/Who                      | validate_docs.py (nieuw) |

### 1.2 Inhoud — gedeeltelijk geautomatiseerd

| Criterium              | Regel                                                                     | Controle            |
| ---------------------- | ------------------------------------------------------------------------- | ------------------- |
| Heading-hiërarchie     | H1 → H2 → H3, geen niveaus overslaan                                      | validate_docs.py    |
| CTA-block aanwezig     | Layer 2 documenten: verplicht `!!! tip "Volgende stap:"` of equivalent    | validate_docs.py    |
| Single Source of Truth | Geen inhoudelijke duplicatie van canonieke concepten (zie STYLE_GUIDE §2) | Redactionele review |
| Samenwerkingsmodus     | Gate-bestanden: `Samenwerkingsmodus:` veld verplicht                      | validate_docs.py    |
| Geen debug-markers     | Geen `TODO`, `FIXME`, `XXX`, `PLACEHOLDER` in gepubliceerde tekst         | pre-commit          |

### 1.3 Vertaling

| Criterium           | Regel                                                                | Controle         |
| ------------------- | -------------------------------------------------------------------- | ---------------- |
| EN-versie bestaat   | Voor elk nieuw NL-bestand moet `.en.md` bestaan vóór merge           | CI               |
| EN-links correct    | EN-bestanden linken naar `.en.md` equivalenten, niet naar NL-versies | validate_docs.py |
| EN-inhoud niet leeg | EN-bestand bevat minimaal de frontmatter en een H1                   | validate_docs.py |

### 1.4 Build

| Criterium                      | Regel                      | Controle |
| ------------------------------ | -------------------------- | -------- |
| `mkdocs build --strict` slaagt | Nul warnings, nul errors   | CI       |
| Geen gebroken interne links    | MkDocs linkchecking slaagt | CI       |

______________________________________________________________________

## Laag 2 — MCP Tool of script (elke nieuwe of gewijzigde Python-functie)

### 2.1 Correctheid

| Criterium                    | Regel                                                                            | Controle |
| ---------------------------- | -------------------------------------------------------------------------------- | -------- |
| Happy path getest            | Minimaal 1 test die de normale werking verifieert                                | pytest   |
| Edge cases getest            | Minimaal 2: lege input, ongeldige parameter                                      | pytest   |
| Error responses correct      | Onbekende/ongeldige input geeft `DecisionStatus.ERROR`, nooit stille fallthrough | pytest   |
| `output_format="json"` werkt | Alle tools: JSON-modus geeft valide JSON terug                                   | pytest   |

### 2.2 Code-kwaliteit

| Criterium             | Regel                                     | Controle               |
| --------------------- | ----------------------------------------- | ---------------------- |
| Ruff clean            | Nul ruff-errors en nul ruff-warnings      | pre-commit + CI        |
| Docstring aanwezig    | Args gedocumenteerd, `Next step:` vermeld | test_qw3_docstrings.py |
| Geen debug-statements | Geen `print()`, `breakpoint()`, `pdb`     | pre-commit             |

### 2.3 Integratie

| Criterium                         | Regel                                                                      | Controle                  |
| --------------------------------- | -------------------------------------------------------------------------- | ------------------------- |
| In cheatsheet opgenomen           | Nieuwe tool verschijnt in `get_tool_cheatsheet()` output                   | test_agents.py            |
| In tool-referentie gedocumenteerd | `docs/ai-tools/mcp-tools.md` bijgewerkt met parameter-handtekening         | Redactionele review       |
| Lifespan-afhankelijkheden correct | Nieuwe indices/stores worden geladen in `lifespan()`, niet alleen in tests | pytest conftest isolation |

### 2.4 Testdekking

| Criterium                   | Drempel                                   | Controle       |
| --------------------------- | ----------------------------------------- | -------------- |
| Branch coverage nieuwe code | ≥ 80% voor elke nieuw toegevoegde functie | `pytest --cov` |
| Geen regressie              | Bestaande 487 tests slagen ongewijzigd    | CI             |

______________________________________________________________________

## Laag 3 — Release (elke versie-bump in `mkdocs.yml`)

### 3.1 Retrieval-kwaliteit — het kritische criterium

| Criterium                           | Drempel                                         | Controle                          |
| ----------------------------------- | ----------------------------------------------- | --------------------------------- |
| Precision@1 op goldset              | ≥ 0.75 (75 van 100 vragen → correcte toppagina) | `scripts/eval_retrieval.py` in CI |
| Precision@3 op goldset              | ≥ 0.90                                          | `scripts/eval_retrieval.py` in CI |
| MRR (Mean Reciprocal Rank)          | ≥ 0.80                                          | `scripts/eval_retrieval.py` in CI |
| Geen regressie t.o.v. vorige versie | Precision@1 daalt niet meer dan 0.03            | CI diff-check                     |

> **Toelichting:** Tot `scripts/eval_retrieval.py` bestaat, geldt: minimaal 15 pagina's handmatig getest met representatieve vragen vóór release. Dit is een tijdelijke uitzondering die vervalt zodra het script klaar is.

### 3.2 Volledigheid

| Criterium                       | Regel                                                                  | Controle                  |
| ------------------------------- | ---------------------------------------------------------------------- | ------------------------- |
| CHANGELOG bijgewerkt            | Elke release heeft een entry met `Added / Changed / Fixed / Removed`   | Redactionele review       |
| llms-full exports geregenereerd | `llms-full.txt` en `llms-full-nl.txt` zijn actueel                     | CI (automatisch bij push) |
| Versienummer consistent         | `mkdocs.yml`, `README.md`, `CHANGELOG.md` tonen hetzelfde versienummer | CI-check                  |

### 3.3 CI-gates — alle moeten groen zijn

```
[ ] validate_docs.py — 0 errors (warnings toegestaan, maar gedocumenteerd)
[ ] mkdocs build --strict — 0 warnings
[ ] pytest mcp_server/tests/ — alle 487+ tests slagen
[ ] ruff + ruff-format — 0 issues
[ ] eval_retrieval.py — ≥ 0.75 precision@1
[ ] pre-commit run --all-files — passed
```

### 3.4 Productie-gereedheid

| Criterium                           | Regel                                                                 | Controle                         |
| ----------------------------------- | --------------------------------------------------------------------- | -------------------------------- |
| Docker healthchecks actief          | `chatbot` en `mcp-server` hebben `healthcheck:` in docker-compose     | deploy/docker-compose.yml        |
| Uptime-monitor actief               | Beide endpoints gemonitord met alerting                               | Extern (UptimeRobot/Betterstack) |
| Breaking change → major versie      | Tool-parameter verwijderd of hernoemd: versienummer major verhoogd    | Redactionele beoordeling         |
| Deprecation-warning geïmplementeerd | Verouderde parameters geven `deprecation_warning` terug voor 1 versie | pytest                           |

______________________________________________________________________

## Laag 4 — Productie-deployment

| Criterium                     | Regel                                                                     | Verificatie      |
| ----------------------------- | ------------------------------------------------------------------------- | ---------------- |
| Health endpoints groen        | `GET /health` op chatbot én MCP server → HTTP 200                         | Deploy-script    |
| Uptime-monitor geen alerting  | Geen openstaande alerts op moment van deploy                              | Handmatige check |
| Rollback gedocumenteerd       | `deploy/ROLLBACK.md` beschrijft exacte commando's voor terugdraaien       | Aanwezig in repo |
| Geen open P0/P1 GitHub issues | Geen openstaande issues gelabeld `priority: critical` of `priority: high` | GitHub           |

______________________________________________________________________

## Wat de DoD niet is

- **Geen aspiratie-lijst.** Elk criterium is binair: pass of fail.
- **Geen uitzonderingen zonder beslissing.** Afwijken vereist een expliciete aantekening in BACKLOG.md met reden en tijdpad.
- **Geen retroactieve toepassing.** Bestaande pagina's die niet aan Laag 1 voldoen worden systematisch bijgewerkt via \[BACKLOG.md\] — ze blokkeren geen nieuwe PRs.

______________________________________________________________________

## Handhaving

| Wat                       | Hoe                                    | Wanneer                   |
| ------------------------- | -------------------------------------- | ------------------------- |
| Laag 1 frontmatter + code | pre-commit hooks                       | Bij elke commit           |
| Laag 1 build              | CI (GitHub Actions)                    | Bij elke push             |
| Laag 2 tests + ruff       | CI                                     | Bij elke push             |
| Laag 3 retrieval eval     | CI (zodra script klaar)                | Bij elke push naar `main` |
| Laag 3 volledigheid       | Verplichte PR-checklist                | Bij elke PR               |
| Laag 4 deployment         | Deploy-script + handmatige verificatie | Bij elke productie-deploy |

______________________________________________________________________

## Implementatie-status P1-items

| Criterium                                   | Status              | Geïmplementeerd         |
| ------------------------------------------- | ------------------- | ----------------------- |
| `scripts/eval_retrieval.py` met goldset     | ✅ Geïmplementeerd  | 2026-04-04              |
| Filler-pattern check in `validate_docs.py`  | ✅ Geïmplementeerd  | 2026-04-04              |
| Docker healthchecks in `docker-compose.yml` | ✅ Geïmplementeerd  | 2026-04-04              |
| `deploy/ROLLBACK.md`                        | ✅ Geïmplementeerd  | 2026-04-04              |
| MCP version header (`X-Blueprint-Version`)  | ✅ Geïmplementeerd  | 2026-04-04              |
| Uptime-monitoring geconfigureerd            | ⏳ Extern — te doen | UptimeRobot/Betterstack |

Alle P1-items zijn geïmplementeerd op de uptime-monitor na (vereist externe configuratie).
