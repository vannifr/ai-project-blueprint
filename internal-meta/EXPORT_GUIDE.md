# Export- en Publicatiegids

Dit document beschrijft hoe de AI Project Blauwdruk wordt gepubliceerd als HTML-website en als PDF. De gehele pipeline is geautomatiseerd via GitHub Actions en vereist geen handmatige stappen voor een standaard publicatie.

______________________________________________________________________

## Lokale Ontwikkeling

### Vereisten

```bash
pip install -r requirements.txt
```

Playwright (voor PDF via Chromium) wordt apart geïnstalleerd:

```bash
playwright install chromium
```

### HTML-site (live preview)

```bash
mkdocs serve
```

De site is dan beschikbaar op `http://127.0.0.1:8000`. Wijzigingen in `docs/` en `mkdocs.yml` worden automatisch herladen.

### HTML-site (bouwen)

```bash
mkdocs build
```

Genereert een `site/`-map met alle HTML-bestanden. De site is zelfstandig te openen zonder webserver.

### Bouwen met strict-modus (zelfde als CI)

```bash
mkdocs build --strict
```

Laat broken links en onbekende sjabloonvariabelen als fout optreden — gebruik dit lokaal om CI-fouten te voorkomen.

______________________________________________________________________

## PDF Genereren

De PDF wordt gegenereerd door `mkdocs-exporter` met Playwright (Chromium headless).

### Stap 1: Bouw de site met PDF-export ingeschakeld

```bash
MKDOCS_EXPORTER_PDF=true mkdocs build --no-directory-urls
```

De variabele `MKDOCS_EXPORTER_PDF=true` schakelt de PDF-export in. Zonder deze variabele wordt de PDF-export overgeslagen (sneller voor HTML-only builds).

### Stap 2: Nabewerking (inhoudsopgave, omslagen, paginanummering)

```bash
python3 scripts/pdf_postprocess.py site
```

Dit script:

- Voegt de PDF-inhoudsopgave samen met het hoofddocument.
- Injecteert de voor- en achterkant van de omslag.
- Nummert secties door via CSS-paginatellers.

### Uitvoer

Het PDF-bestand verschijnt op: `site/pdf/ai-project-blauwdruk.pdf`

______________________________________________________________________

## Meertalige Builds

De site ondersteunt NL (standaard), EN, FR en DE via de `mkdocs-static-i18n` plugin.

### HTML — alle talen (standaard)

```bash
mkdocs build
```

Dit bouwt alle vier taalversies in één stap:

- `/` → NL
- `/en/` → EN
- `/fr/` → FR
- `/de/` → DE

### HTML — alleen NL (sneller, voor kwaliteitscheck)

```bash
MKDOCS_BUILD_I18N=false mkdocs build --strict
```

### PDF — per taal

```bash
MKDOCS_LANG=nl MKDOCS_EXPORTER_PDF=true mkdocs build --no-directory-urls
python3 scripts/pdf_postprocess.py site
# Uitvoer: site/pdf/ai-project-blauwdruk.nl.pdf

MKDOCS_LANG=en MKDOCS_EXPORTER_PDF=true MKDOCS_PDF_OUTPUT=pdf/ai-project-blauwdruk.en.pdf mkdocs build --no-directory-urls
python3 scripts/pdf_postprocess.py site
# Uitvoer: site/pdf/ai-project-blauwdruk.en.pdf
```

______________________________________________________________________

## Geautomatiseerde CI/CD Pipeline

De GitHub Actions workflow (`.github/workflows/deploy-ftp.yml`) voert automatisch uit bij elke push naar `main`:

| Job          | Wat                                                 | Artefact           |
| :----------- | :-------------------------------------------------- | :----------------- |
| `quality`    | MkDocs strict build (NL) + htmlproofer + pre-commit | —                  |
| `build-site` | MkDocs build (alle talen)                           | `site-build/`      |
| `pdf`        | PDF build NL + nabewerking                          | `pdf-artifact/`    |
| `deploy`     | FTP-upload van site + PDF naar `vannifr.ovh`        | Gepubliceerde site |

De `quality` en `pdf` jobs lopen parallel. De `deploy` job wacht op beide.

______________________________________________________________________

## Validatie

De volgende validaties worden uitgevoerd in de `quality` job:

```bash
python3 scripts/validate_docs.py          # Verbodsterm-check, stub-check, termenlijst-check
mkdocs build --strict                     # Broken links, sjabloonfouten
```

Voer deze lokaal uit vóór een pull request:

```bash
python3 scripts/validate_docs.py
mkdocs build --strict
```

______________________________________________________________________

## Handmatige Publicatie (noodsituatie)

Als de CI/CD pipeline tijdelijk niet beschikbaar is:

1. Bouw lokaal: `mkdocs build`
1. Upload de volledige `site/`-map via FTP naar `vannifr.ovh/ai-project-playbook/`.
1. Verifieer de publicatie: open `https://vannifr.ovh/ai-project-playbook/` in een browser.

______________________________________________________________________

## Probleemoplossing

| Symptoom                                           | Waarschijnlijke oorzaak          | Oplossing                                                           |
| :------------------------------------------------- | :------------------------------- | :------------------------------------------------------------------ |
| `WARNING - Doc file not found`                     | Link naar niet-bestaand bestand  | Corrigeer het pad of maak het bestand aan                           |
| PDF leeg of zonder omslagen                        | Playwright niet geïnstalleerd    | `playwright install chromium`                                       |
| `/en/` geeft 404 op de site                        | `build-site` job niet uitgevoerd | Controleer of de `MKDOCS_BUILD_I18N`-variabele correct is ingesteld |
| `ValueError: future belongs to different loop`     | i18n + PDF-export in combinatie  | Gebruik `MKDOCS_BUILD_I18N=false` voor PDF-builds                   |
| Pre-commit hook `no-commit-to-branch` blokkeert CI | Standaard CI-gedrag op main      | CI gebruikt `SKIP=no-commit-to-branch`                              |
