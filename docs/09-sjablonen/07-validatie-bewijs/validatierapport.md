# Template 09.06: Validatierapport (Bewijsâ€‘pakket)

## Documentbeheer

- **Document-ID:** TMP-09-06
- **Titel:** Template 09.06 â€” Validatierapport (Bewijsâ€‘pakket)
- **Versie:** 1.0
- **Status:** Definitief
- **Eigenaar:** AI Competence Center
- **Laatst herzien:** 2026-02-01
- **Wijziging t.o.v. vorige versie:** Nieuw template toegevoegd; standaardiseert bewijs voor Gate Reviews.

______________________________________________________________________

## 0. Samenvatting (1 pagina)

**Project:** \[Naam\]
**Risiconiveau:** \[Minimaal / Beperkt / Hoog\]
**Samenwerkingsmodus:** \[1â€“5\]
**Release/Build:** \[bijv. RC-1\]
**Testperiode:** \[YYYY-MM-DD t/m YYYY-MM-DD\]

### Conclusie (kies Ã©Ã©n)

- [ ] **Go** â€” voldoet aan Module 01.07 normen voor dit risiconiveau
- [ ] **Go met acties** â€” alleen na uitvoeren van acties onder Â§7
- [ ] **No-Go** â€” voldoet niet; herontwerp/hertrain/herformuleer vereist

**Top 3 bevindingen:**

1. â€¦
1. â€¦
1. â€¦

______________________________________________________________________

## 1. Scope & referenties (traceerbaarheid)

**Doelkaart versie:** \[link/ID\]
**Rode Lijnen versie:** \[link/ID\]
**Sturingsinstructies versie:** \[link/ID\]
**Modelkaart versie:** \[link/ID\]
**Testprotocol versie (TMP-09-05):** \[link/ID\]
**Risico Pre-Scan (TMP-09-03):** \[link/ID\]

______________________________________________________________________

## 2. Testopzet

- **Omgeving:** \[Dev/Test/Prod-simulatie\]
- **Modelinstellingen:** \[bijv. temperature, max tokens\]
- **Kenniskoppeling:** \[Ja/Nee\] â€” zo ja: welke bronset + updatefrequentie
- **Randvoorwaarden:** \[bijv. rate limits, timeouts, tooling\]

______________________________________________________________________

## 3. Testsets (Gouden Set + aanvullingen)

### 3.1 Gouden Set

- **Aantal cases:** \[minimaal volgens MOD-01-07\]
- **Herkomst:** \[tickets, e-mails, calls, formulierenâ€¦\]
- **Dekking:** \[80/15/5 of 70/20/10 afhankelijk risiconiveau\]

### 3.2 Adversarial set (verplicht bij Beperkt/Hoog)

- **Aantal adversarial prompts:** \[#\]
- **Soorten:** jailbreak / prompt injectie / datalek / bronverzinnen

### 3.3 Fairness set (verplicht bij Hoog)

- **Aanpak:** \[kwantitatief / kwalitatief + motivatie\]
- **Groepen/segmenten:** \[beschrijf zonder gevoelige details\]

______________________________________________________________________

## 4. Resultaten t.o.v. Bewijsstandaarden (MOD-01-07)

| Criterium                             |         Norm | Gemeten | Pass/Fail             | Opmerking |
| ------------------------------------- | -----------: | ------: | --------------------- | --------- |
| Kritieke fouten                       |            0 |   \[#\] | \[ \] Pass \[ \] Fail |           |
| Major fouten (max)                    |        \[#\] |   \[#\] | \[ \] Pass \[ \] Fail |           |
| Feitelijkheid                         |   \[â‰¥..%\] | \[..%\] | \[ \] Pass \[ \] Fail |           |
| Relevantie (1â€“5)                    |    \[â‰¥..\] |  \[..\] | \[ \] Pass \[ \] Fail |           |
| Veiligheid (weigeren)                 |         100% | \[..%\] | \[ \] Pass \[ \] Fail |           |
| Transparantie (indien van toepassing) |         100% | \[..%\] | \[ \] Pass \[ \] Fail |           |
| Eerlijkheid (bias)                    |   \[â‰¤..%\] | \[..%\] | \[ \] Pass \[ \] Fail |           |
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

- **Wat loggen we:** \[conform MOD-01-07 Â§7\]
- **Waar staat het:** \[tool + locatie\]
- **Retentie:** \[90 dagen / 12 maanden / anders\]
- **Privacymaatregelen:** \[hashing/pseudonimisering/redactie\]

______________________________________________________________________

## 7. Actieplan (alleen invullen als â€œGo met actiesâ€ of â€œNo-Goâ€)

| Actie | Eigenaar | Deadline | Verwacht effect | Verificatie (test) |
| ----- | -------- | -------- | --------------- | ------------------ |
|       |          |          |                 |                    |

______________________________________________________________________

## 8. Go/No-Go ondertekening

**Tech Lead:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  **Datum:** \_\_\_\_\_\_\_\_
**AI Product Manager:** \_\_\_\_\_\_\_\_\_\_\_  **Datum:** \_\_\_\_\_\_\_\_
**Guardian:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  **Datum:** \_\_\_\_\_\_\_\_
