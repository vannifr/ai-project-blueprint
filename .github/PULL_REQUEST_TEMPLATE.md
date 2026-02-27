## Omschrijving

<!-- Wat is er gewijzigd en waarom? Koppel aan een issue indien van toepassing. -->

Fixes #<!-- issue nummer -->

______________________________________________________________________

## Type wijziging

<!-- Zet een x tussen de haakjes -->

- [ ] Nieuwe pagina / module toegevoegd
- [ ] Bestaande inhoud bijgewerkt of gecorrigeerd
- [ ] Vertaling toegevoegd of verbeterd (EN / FR / DE)
- [ ] Structurele of opmaak-wijziging
- [ ] Infrastructuur / CI / scripts

______________________________________________________________________

## Zelfcontrole

Voer onderstaande stappen uit **vóór** het indienen van deze PR:

- [ ] `pre-commit run --all-files` geslaagd (geen fouten)
- [ ] `python3 scripts/validate_docs.py` geslaagd (geen ERRORs)
- [ ] `mkdocs build --strict` geslaagd lokaal (of CI-build groen)
- [ ] Nieuwe pagina's staan vermeld in de `nav:` sectie van `mkdocs.yml`
- [ ] Nieuwe pagina's hebben geldige YAML frontmatter met `versie`-veld
- [ ] Terminologie volgt de STYLE_GUIDE (`kostenoverzicht` i.p.v. `kostenplaatje`, etc.)
- [ ] Actieve schrijfstijl gebruikt ("Wij evalueren" i.p.v. "Er wordt geëvalueerd")
- [ ] Vertaalplaceholders bevatten `pdf: false` in frontmatter

______________________________________________________________________

## Opmerkingen voor de reviewer

<!-- Specifieke aandachtspunten, open vragen, of context voor de reviewer. -->
