# Bijdragerichtlijnen — AI Project Blauwdruk

Bedankt voor uw bijdrage aan de AI Project Blauwdruk. Deze gids beschrijft hoe u wijzigingen
voorstelt, welke kwaliteitseisen er gelden, en hoe het review-proces verloopt.

______________________________________________________________________

## 1. Aan de slag

### Vereisten

```bash
pip install -r requirements.txt
pip install pre-commit
pre-commit install
```

Controleer uw installatie:

```bash
pre-commit run --all-files   # Alle hooks uitvoeren
python3 scripts/validate_docs.py  # Documentatiekwaliteit
mkdocs serve                 # Lokale preview op http://localhost:8000
```

______________________________________________________________________

## 2. Branchstrategie

| Branch                    | Doel                                             |
| ------------------------- | ------------------------------------------------ |
| `main`                    | Productie — directe commits zijn **geblokkeerd** |
| `feature/<onderwerp>`     | Nieuwe modules of uitbreidingen                  |
| `fix/<onderwerp>`         | Correcties van fouten of verouderde inhoud       |
| `i18n/<taal>-<onderwerp>` | Vertalingen (EN / FR / DE)                       |

**Voorbeelden:**

```bash
git checkout -b feature/fase3-sdd-patroon
git checkout -b fix/leeswijzer-broken-links
git checkout -b i18n/en-executive-summary
```

Maak nooit direct commits op `main`. De pre-commit hook blokkeert dit automatisch.

______________________________________________________________________

## 3. Een nieuwe pagina toevoegen

1. Maak het bestand aan in de juiste map (zie `internal-meta/STYLE_GUIDE.md` voor de mappenstructuur).
1. Voeg verplichte YAML frontmatter toe:
    ```yaml
    ---
    versie: '1.0'
    ---
    ```
1. Schrijf minimaal één H1 kop (`# Titel`).
1. Voeg de pagina toe aan de `nav:` sectie in `mkdocs.yml`.
1. Maak optioneel vertaalplaceholders aan (zie §5).

### Modulestructuur (proces-modules)

Elke proces-module moet de volgende secties bevatten (zie STYLE_GUIDE):

1. **Doelstelling** — één krachtige zin
1. **Intrede Criteria** — wat moet af zijn vóór aanvang
1. **Kernactiviteiten** — 3 tot 5 concrete stappen
1. **RACI** — Responsible en Accountable
1. **Exit Criteria** — afsluiting gate-checklist
1. **Deliverables** — concrete opleverbestanden

______________________________________________________________________

## 4. Kwaliteitseisen

### Stijl (STYLE_GUIDE)

- Schrijf in het **formele "u"** (Vlaamse standaard).

- Gebruik **actieve zinnen**: "Wij evalueren" — niet "Er wordt geëvalueerd".

- Volg de terminologielijst in `internal-meta/STYLE_GUIDE.md`:

    | ❌ Vermijd       | ✅ Gebruik               |
    | ---------------- | ------------------------ |
    | kostenplaatje    | kostenoverzicht          |
    | inregelen        | instellen / configureren |
    | gereedschapskist | toolkit                  |
    | shadow AI        | wildgroei                |
    | model drift      | prestatieverloop         |
    | guardrails       | rode lijnen              |
    | deployment       | ingebruikname / livegang |

### Automatische controles

`validate_docs.py` controleert op:

| Check                                               | Niveau  |
| --------------------------------------------------- | ------- |
| YAML frontmatter aanwezig en `versie`-veld compleet | ERROR   |
| H1-kop aanwezig                                     | ERROR   |
| Onopgeloste merge-conflictmarkers                   | ERROR   |
| Debug-markers in koppen (`(TODO)`, `(WIP)`, …)      | ERROR   |
| Kopniveaus overgeslagen (H1 → H3 zonder H2)         | WARNING |
| Terminologie uit de stijlgids                       | WARNING |
| Stub-pagina's zonder `pdf: false`                   | WARNING |
| Weespagina's niet in nav vermeld                    | WARNING |
| Ontbrekende vertalingen (EN/FR/DE)                  | INFO    |

Voer altijd uit vóór een PR:

```bash
python3 scripts/validate_docs.py
```

Met `--strict-i18n` worden ontbrekende vertalingen als WARNING gerapporteerd.

______________________________________________________________________

## 5. Vertalingen toevoegen

Bestanden volgen de **suffix-strategie**:

| Taal                   | Bestandsextensie |
| ---------------------- | ---------------- |
| Nederlands (standaard) | `pagina.md`      |
| Engels                 | `pagina.en.md`   |
| Frans                  | `pagina.fr.md`   |
| Duits                  | `pagina.de.md`   |

**Stap-voor-stap:**

1. Kopieer de NL-versie als startpunt.
1. Hernoem naar het juiste suffix (bijv. `index.en.md`).
1. Voeg `pdf: false` toe aan de frontmatter zolang de vertaling onvolledig is.
1. Schrijf de inhoud in de doeltaal.
1. Verwijder `pdf: false` zodra de pagina volledig vertaald is.
1. Controleer het resultaat: `mkdocs serve` → navigeer naar `/en/`, `/fr/` of `/de/`.

**Placeholder-formaat:**

```markdown
---
versie: '1.0'
pdf: false
---

# Page Title (English)

!!! info "Translation in progress"
    This page is being translated. See the [Dutch original](pagina.md).
```

______________________________________________________________________

## 6. Pull Request-proces

1. **Fork of branch** aanmaken (zie §2).
1. Wijzigingen uitvoeren en lokaal testen.
1. **Pre-commit** uitvoeren: `pre-commit run --all-files`.
1. **Validatie** uitvoeren: `python3 scripts/validate_docs.py`.
1. PR aanmaken via GitHub — vul de PR-template volledig in.
1. De CI-pipeline controleert automatisch:
    - Pre-commit hooks
    - Documentatievalidatie
    - MkDocs strict build + HTML proofer
1. **Review** door minimaal één andere auteur.
1. Na goedkeuring: merge door de repository-eigenaar.

### Reviewcriteria

Een PR is klaar voor merge als:

- [ ] Alle CI-checks slagen (groen vinkje in GitHub)
- [ ] Inhoud volgt de STYLE_GUIDE
- [ ] Nieuwe pagina's staan in de nav
- [ ] Geen onopgeloste opmerkingen van de reviewer

______________________________________________________________________

## 7. Commit-conventies

Gebruik een korte, beschrijvende commitboodschap in de gebiedende wijs:

```
voeg: leeswijzer-pagina toegevoegd aan strategisch kader
fix: broken link in fase-3 doelstellingen hersteld
update: executive summary bijgewerkt met v1.1 governance
i18n: Engelse vertaling van termenlijst toegevoegd
infra: CI-workflow bijgewerkt voor PDF-matrix build
```

Prefixen: `voeg:`, `fix:`, `update:`, `i18n:`, `infra:`, `stijl:`

______________________________________________________________________

## 8. Vragen of problemen?

- **Documentatiefout gevonden?** → Maak een [Documentatie-verbetering](../../issues/new?template=documentatie-verbetering.md)-issue aan.
- **Vertaling incorrect of ontbrekend?** → Maak een [Vertaalfout](../../issues/new?template=vertaalfout.md)-issue aan.
- **Grote structuurwijziging voorstellen?** → Open eerst een issue om de aanpak te bespreken vóór u code schrijft.

______________________________________________________________________

© 2026 AI Project Blauwdruk · CC BY-NC-SA 4.0
