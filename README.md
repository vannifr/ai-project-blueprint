# AI Project Gids

![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-green)
![Version](https://img.shields.io/badge/version-1.0-blue)
![Build Status](https://github.com/vannifr/ai-project-playbook/actions/workflows/deploy-ftp.yml/badge.svg)

De centrale documentatiehub voor AI-projectmanagement, gebaseerd op PMI-CPMAI standaarden, EU AI Act compliance en Agile-AI frameworks.

## 📖 Over dit project

Deze gids (v1.0) biedt een gestandaardiseerde, modulaire aanpak om AI-projecten te beheren van ideatie tot monitoring. Het is ontworpen om teams te helpen navigeren door de complexiteit van AI-native ontwikkeling, compliance en organisatie-adoptie.

### Kernmodules

- **Executive Summary (MOD-00.01):** Snelle blik op de methodiek en implementatiepaden.
- **Strategisch Kader:** Hybride waterval/agile methodiek en governance (HAS H niveaus).
- **Snelle Route (Fast Lane):** Versnelde procedure voor AI-experimenten met laag risico.
- **AI-Native Fundamenten:** Doelkaarten, bewijsstandaarden en specificatie-gedreven validatie.
- **Levenscyclus:** 5 fasen van Discovery tot Monitoring met Gate Reviews.
- **Compliance Hub:** Praktische toepassing van de EU AI Act en Privacy-by-Design (AVG/GDPR).
- **13-Weken Roadmap:** Een uitvoerbaar startplan voor teams.

## 🚀 Aan de slag

### De Website bekijken

De documentatie is geoptimaliseerd voor MkDocs.

**Lokaal draaien:**

1. Zorg dat Python geïnstalleerd is.
1. Installeer de dependencies:
    ```bash
    pip install -r requirements.txt
    ```
1. Start de server:
    ```bash
    mkdocs serve
    ```
1. Open [http://localhost:8000](http://localhost:8000).

### Ontwikkelworkflow

**Pre-commit hooks instellen (aanbevolen):**

```bash
pip install pre-commit
pre-commit install
```

Dit activeert automatische kwaliteitscontroles bij elke commit:

- Markdown formatting (mdformat)
- Trailing whitespace verwijderen
- YAML syntax validatie
- **Documentatie kwaliteitsvalidatie** (duplicate text detection, frontmatter checks)

**Handmatige kwaliteitscontrole:**

```bash
python3 scripts/validate_docs.py
```

Dit script controleert op:

- Herhaalde tekst patronen (bijv. "(Gate 1) (Gate 1) (Gate 1)")
- Ontbrekende of inconsistente YAML frontmatter
- Spellingfouten en naamgevingsinconsistenties
- Duplicate woorden in koppen

## 🤝 Bijdragen

Dit project wordt beheerd volgens strikte documentatiestandaarden. Zie de `internal-meta/BACKLOG.md` voor de huidige roadmap.

### Documentatiestandaarden

- **Taal:** Nederlands, professioneel en zakelijk.
- **Stijl:** Gebruik de gestandaardiseerde `Documentbeheer` headers.
- **Frontmatter:** Alle `.md` bestanden vereisen YAML frontmatter met `versie` en `laatst_herzien`.
- **Links:** Alle interne links worden automatisch gevalideerd tijdens build.

### Kwaliteitsborging

Alle wijzigingen doorlopen automatisch:

1. **Pre-commit hooks:** Formatting, linting, en custom validaties
1. **GitHub Actions CI:** Quality checks + link validation (strict mode)
1. **Automated deployment:** Alleen bij succesvolle validatie

**Voor het indienen van een PR:**

- Voer `pre-commit run --all-files` uit
- Controleer dat `mkdocs build --strict` slaagt
- Verifieer dat `python3 scripts/validate_docs.py` geen errors geeft

## 📄 Licentie

© 2026 AI Project Gids.
Gelicenseerd onder de **Creative Commons Naamsvermelding-NietCommercieel-GelijkDelen 4.0 Internationaal (CC BY-NC-SA 4.0)**.
Zie de footer van elk document voor copyright informatie.
