---
versie: '1.0'
type: template
layer: 3
phase: [2, 3]
roles: [Data Scientist]
tags: [template, validation]
answers: ['Hoe gebruik ik het Sjabloon 09.06: Validatierapport (Bewijs‑pakket) sjabloon?']
---

# 1. Sjabloon 09.06: Validatierapport (Bewijs‑pakket)

!!! tip "Wanneer gebruik je dit?"
    Je rondt een validatiepilot af en moet het bewijspakket samenstellen voor de Gate Review-beslissing (Go / Go met acties / No-Go).

!!! note "Download dit sjabloon"
    [Download als Markdown](https://github.com/vannifr/ai-project-blueprint/raw/main/docs/09-sjablonen/07-validatie-bewijs/validatierapport.md){ .md-button } — Open in je editor of AI-assistent en vul de velden in.

## 1. Samenvatting (1 pagina)

**Project:** \[Naam\]
**Risiconiveau:** \[Minimaal / Beperkt / Hoog\]
**Samenwerkingsmodus:** \[1–5\]
**Release/Build:** \[bijv. RC-1\]
**Testperiode:** \[YYYY-MM-DD t/m YYYY-MM-DD\]

### Conclusie (kies één)

!!! check "Conclusie (kies één)"
    - [ ] **Go** — voldoet aan Bewijsstandaarden normen voor dit risiconiveau
    - [ ] **Go met acties** — alleen na uitvoeren van acties onder §7
    - [ ] **No-Go** — voldoet niet; herontwerp/hertrain/herformuleer vereist

**Top 3 bevindingen:**

1. ...
1. ...
1. ...

______________________________________________________________________

## 2. Scope & referenties (traceerbaarheid)

**Doelkaart (goal card) versie:** \[link/ID\]
**Harde Grenzen versie:** \[link/ID\]
**Prompts versie:** \[link/ID\]
**Modelkaart versie:** \[link/ID\]
**Testprotocol versie (Golden Set Test):** \[link/ID\]
**Risico Pre-Scan (Risico Pre-Scan):** \[link/ID\]

______________________________________________________________________

## 3. Testopzet

- **Omgeving:** \[Dev/Test/Prod-simulatie\]
- **Modelinstellingen:** \[bijv. temperature, max tokens\]
- **RAG:** \[Ja/Nee\] — zo ja: welke bronset + updatefrequentie
- **Randvoorwaarden:** \[bijv. rate limits, timeouts, tooling\]

______________________________________________________________________

## 4. Testsets (Golden Set + aanvullingen)

### Golden Set

- **Aantal cases:** \[minimaal volgens Bewijsstandaarden\]
- **Herkomst:** \[tickets, e-mails, calls, formulieren...\]
- **Dekking:** \[80/15/5 of 70/20/10 afhankelijk risiconiveau\]

### Adversarial set (verplicht bij Beperkt/Hoog)

- **Aantal adversarial prompts:** \[#\]
- **Soorten:** jailbreak / prompt injectie / datalek / bronverzinnen

### Fairness set (verplicht bij Hoog)

- **Aanpak:** \[kwantitatief / kwalitatief + motivatie\]
- **Groepen/segmenten:** \[beschrijf zonder gevoelige details\]

______________________________________________________________________

## 5. Resultaten t.o.v. Bewijsstandaarden (Bewijsstandaarden)

| Criterium                             |         Norm | Gemeten | Pass/Fail             | Opmerking |
| ------------------------------------- | -----------: | ------: | --------------------- | --------- |
| Kritieke fouten                       |            0 |   \[#\] | \[ \] Pass \[ \] Fail |           |
| Major fouten (max)                    |        \[#\] |   \[#\] | \[ \] Pass \[ \] Fail |           |
| Feitelijkheid                         |     \[≥..%\] | \[..%\] | \[ \] Pass \[ \] Fail |           |
| Relevantie (1–5)                      |      \[≥..\] |  \[..\] | \[ \] Pass \[ \] Fail |           |
| Veiligheid (weigeren)                 |         100% | \[..%\] | \[ \] Pass \[ \] Fail |           |
| Transparantie (indien van toepassing) |         100% | \[..%\] | \[ \] Pass \[ \] Fail |           |
| Eerlijkheid (bias)                    |     \[≤..%\] | \[..%\] | \[ \] Pass \[ \] Fail |           |
| Audit trail                           | volgens norm |  \[..\] | \[ \] Pass \[ \] Fail |           |

______________________________________________________________________

## 6. Overzicht van fouten (verplicht)

### Kritieke fouten (0 toegestaan)

| Case-ID | Beschrijving | Impact | Oorzaak | Fix | Status |
| ------- | ------------ | ------ | ------- | --- | ------ |

### Major fouten

| Case-ID | Beschrijving | Impact | Oorzaak | Fix | Status |
| ------- | ------------ | ------ | ------- | --- | ------ |

### Terugkerende patronen (failure modes)

- \[bijv. bronvermelding onjuist bij type document X\]
- \[bijv. te creatieve toon bij korte prompts\]

______________________________________________________________________

## 7. Logging & audit trail (bewijs dat we kunnen terugzoeken)

- **Wat loggen we:** \[conform Bewijsstandaarden §7\]
- **Waar staat het:** \[tool + locatie\]
- **Retentie:** \[90 dagen / 12 maanden / anders\]
- **Privacymaatregelen:** \[hashing/pseudonimisering/redactie\]

______________________________________________________________________

## 8. Actieplan (alleen invullen als “Go met acties” of “No-Go”)

| Actie | Eigenaar | Deadline | Verwacht effect | Verificatie (test) |
| ----- | -------- | -------- | --------------- | ------------------ |
|       |          |          |                 |                    |

______________________________________________________________________

## 9. Go/No-Go ondertekening

**Tech Lead:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **AI Product Manager:** \_\_\_\_\_\_\_\_\_\_\_ **Guardian:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
