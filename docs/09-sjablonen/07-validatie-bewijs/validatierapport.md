---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# Sjabloon 09.06: Validatierapport (Bewijs‑pakket)

## 0. Samenvatting (1 pagina)

**Project:** \[Naam\]
**Risiconiveau:** \[Minimaal / Beperkt / Hoog\]
**Samenwerkingsmodus:** \[1–5\]
**Release/Build:** \[bijv. RC-1\]
**Testperiode:** \[YYYY-MM-DD t/m YYYY-MM-DD\]

### Conclusie (kies één)

- [ ] **Go** — voldoet aan Module 01.07 normen voor dit risiconiveau
- [ ] **Go met acties** — alleen na uitvoeren van acties onder Â§7
- [ ] **No-Go** — voldoet niet; herontwerp/hertrain/herformuleer vereist

**Top 3 bevindingen:**

1. ”¦
1. ”¦
1. ”¦

______________________________________________________________________

## 1. Scope & referenties (traceerbaarheid)

**Doelkaart versie:** \[link/ID\]
**Rode Lijnen versie:** \[link/ID\]
**Sturingsinstructies versie:** \[link/ID\]
**Modelkaart versie:** \[link/ID\]
**Testprotocol versie (Gouden Set Test):** \[link/ID\]
**Risico Pre-Scan (Risico Pre-Scan):** \[link/ID\]

______________________________________________________________________

## 2. Testopzet

- **Omgeving:** \[Dev/Test/Prod-simulatie\]
- **Modelinstellingen:** \[bijv. temperature, max tokens\]
- **Kenniskoppeling:** \[Ja/Nee\] — zo ja: welke bronset + updatefrequentie
- **Randvoorwaarden:** \[bijv. rate limits, timeouts, tooling\]

______________________________________________________________________

## 3. Testsets (Gouden Set + aanvullingen)

### 3.1 Gouden Set

- **Aantal cases:** \[minimaal volgens Bewijsstandaarden\]
- **Herkomst:** \[tickets, e-mails, calls, formulieren”¦\]
- **Dekking:** \[80/15/5 of 70/20/10 afhankelijk risiconiveau\]

### 3.2 Adversarial set (verplicht bij Beperkt/Hoog)

- **Aantal adversarial prompts:** \[#\]
- **Soorten:** jailbreak / prompt injectie / datalek / bronverzinnen

### 3.3 Fairness set (verplicht bij Hoog)

- **Aanpak:** \[kwantitatief / kwalitatief + motivatie\]
- **Groepen/segmenten:** \[beschrijf zonder gevoelige details\]

______________________________________________________________________

## 4. Resultaten t.o.v. Bewijsstandaarden (Bewijsstandaarden)

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

## 5. Overzicht van fouten (verplicht)

### 5.1 Kritieke fouten (0 toegestaan)

| Case-ID | Beschrijving | Impact | Oorzaak | Fix | Status |
| ------- | ------------ | ------ | ------- | --- | ------ |

### 5.2 Major fouten

| Case-ID | Beschrijving | Impact | Oorzaak | Fix | Status |
| ------- | ------------ | ------ | ------- | --- | ------ |

### 5.3 Terugkerende patronen (failure modes)

- \[bijv. bronvermelding onjuist bij type document X\]
- \[bijv. te creatieve toon bij korte prompts\]

______________________________________________________________________

## 6. Logging & audit trail (bewijs dat we kunnen terugzoeken)

- **Wat loggen we:** \[conform Bewijsstandaarden Â§7\]
- **Waar staat het:** \[tool + locatie\]
- **Retentie:** \[90 dagen / 12 maanden / anders\]
- **Privacymaatregelen:** \[hashing/pseudonimisering/redactie\]

______________________________________________________________________

## 7. Actieplan (alleen invullen als “Go met acties” of “No-Go”)

| Actie | Eigenaar | Deadline | Verwacht effect | Verificatie (test) |
| ----- | -------- | -------- | --------------- | ------------------ |
|       |          |          |                 |                    |

______________________________________________________________________

## 8. Go/No-Go ondertekening

**Tech Lead:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  **Datum:** \_\_\_\_\_\_\_\_
**AI Product Manager:** \_\_\_\_\_\_\_\_\_\_\_  **Datum:** \_\_\_\_\_\_\_\_
**Guardian:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  **Datum:** \_\_\_\_\_\_\_\_
