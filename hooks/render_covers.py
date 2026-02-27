"""MkDocs hook: render Jinja2 cover-templates voor mkdocs-exporter.

mkdocs-exporter leest cover-bestanden als platte HTML (zonder template-engine).
Deze hook rendert de .html.j2 templates met Jinja2 en schrijft de output naar
.html bestanden die de exporter vervolgens oppikt.
"""

import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader

COVERS_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "resources", "templates", "covers")
TEMPLATES = ["front.html.j2", "back.html.j2"]

MONTHS = {
    "nl": {
        1: "januari", 2: "februari", 3: "maart", 4: "april",
        5: "mei", 6: "juni", 7: "juli", 8: "augustus",
        9: "september", 10: "oktober", 11: "november", 12: "december",
    },
    "en": {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December",
    },
    "fr": {
        1: "janvier", 2: "février", 3: "mars", 4: "avril",
        5: "mai", 6: "juin", 7: "juillet", 8: "août",
        9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre",
    },
    "de": {
        1: "Januar", 2: "Februar", 3: "März", 4: "April",
        5: "Mai", 6: "Juni", 7: "Juli", 8: "August",
        9: "September", 10: "Oktober", 11: "November", 12: "Dezember",
    },
}

LANG_STRINGS = {
    "nl": {
        "subtitle": "AI Governance &amp; Projectmanagement",
        "description": "Modulaire documentatie voor AI-projectmanagement",
        "confidential": "Vertrouwelijk &middot; Alleen voor intern gebruik tenzij anders overeengekomen",
        "toc_title": "Inhoudsopgave",
        "license_text": (
            "Dit werk is gelicenseerd onder de Creative Commons "
            "Naamsvermelding-NietCommercieel-GelijkDelen 4.0 Internationale Licentie "
            "(<strong>CC BY-NC-SA 4.0</strong>).<br /><br />"
            "U bent vrij om dit materiaal te delen en te bewerken, mits u de oorspronkelijke "
            "auteurs vermeldt, het niet voor commerciële doeleinden gebruikt, en afgeleide "
            "werken onder dezelfde licentie deelt."
        ),
    },
    "en": {
        "subtitle": "AI Governance &amp; Project Management",
        "description": "Modular documentation for AI project management",
        "confidential": "Confidential &middot; For internal use only unless otherwise agreed",
        "toc_title": "Table of Contents",
        "license_text": (
            "This work is licensed under the Creative Commons "
            "Attribution-NonCommercial-ShareAlike 4.0 International License "
            "(<strong>CC BY-NC-SA 4.0</strong>).<br /><br />"
            "You are free to share and adapt this material, provided you give appropriate "
            "credit, do not use it for commercial purposes, and distribute your contributions "
            "under the same license."
        ),
    },
    "fr": {
        "subtitle": "Gouvernance IA &amp; Gestion de Projet",
        "description": "Documentation modulaire pour la gestion de projets IA",
        "confidential": "Confidentiel &middot; Usage interne uniquement sauf accord contraire",
        "toc_title": "Table des matières",
        "license_text": (
            "Cette œuvre est sous licence Creative Commons "
            "Attribution-NonCommercial-ShareAlike 4.0 International "
            "(<strong>CC BY-NC-SA 4.0</strong>).<br /><br />"
            "Vous êtes libre de partager et d'adapter ce matériel, à condition de citer "
            "les auteurs originaux, de ne pas l'utiliser à des fins commerciales et de "
            "distribuer vos contributions sous la même licence."
        ),
    },
    "de": {
        "subtitle": "KI-Governance &amp; Projektmanagement",
        "description": "Modulare Dokumentation für KI-Projektmanagement",
        "confidential": "Vertraulich &middot; Nur für internen Gebrauch, sofern nicht anders vereinbart",
        "toc_title": "Inhaltsverzeichnis",
        "license_text": (
            "Dieses Werk ist lizenziert unter der Creative Commons "
            "Namensnennung-NichtKommerziell-Weitergabe unter gleichen Bedingungen "
            "4.0 International Lizenz (<strong>CC BY-NC-SA 4.0</strong>).<br /><br />"
            "Sie dürfen dieses Material teilen und bearbeiten, sofern Sie die ursprünglichen "
            "Autoren nennen, es nicht für kommerzielle Zwecke verwenden und Ihre Beiträge "
            "unter derselben Lizenz weitergeben."
        ),
    },
}


def _localized_now(lang):
    """Retourneert datetime met een strftime-wrapper die gelokaliseerde maandnamen gebruikt."""
    dt = datetime.now()
    month_names = MONTHS.get(lang, MONTHS["nl"])

    class LocalizedDatetime:
        """Dunne wrapper rond datetime met gelokaliseerde datumformattering."""

        def strftime(self, fmt):
            result = dt.strftime(fmt)
            result = result.replace(dt.strftime("%B"), month_names[dt.month])
            result = result.replace(dt.strftime("%b"), month_names[dt.month][:3])
            return result

    return LocalizedDatetime()


def on_config(config):
    # Alleen uitvoeren als PDF-export actief is
    if not os.environ.get("MKDOCS_EXPORTER_PDF"):
        return config

    lang = os.environ.get("MKDOCS_LANG", "nl")
    lang_strings = LANG_STRINGS.get(lang, LANG_STRINGS["nl"])

    covers_dir = os.path.normpath(COVERS_DIR)
    env = Environment(loader=FileSystemLoader(covers_dir), autoescape=False)

    context = {
        "config": config,
        "now": lambda: _localized_now(lang),
        "lang": lang_strings,
    }

    for template_name in TEMPLATES:
        template_path = os.path.join(covers_dir, template_name)
        if not os.path.exists(template_path):
            continue

        template = env.get_template(template_name)
        rendered = template.render(**context)

        output_name = template_name.replace(".html.j2", ".html")
        output_path = os.path.join(covers_dir, output_name)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered)

    # Pas exporter-config aan om gerenderde .html bestanden te gebruiken
    for plugin in config.get("plugins", {}).values():
        plugin_config = getattr(plugin, "config", None)
        if plugin_config is None:
            continue
        formats = plugin_config.get("formats") if hasattr(plugin_config, "get") else None
        if formats is None:
            continue
        pdf_config = formats.get("pdf") if hasattr(formats, "get") else None
        if pdf_config is None:
            continue
        covers = pdf_config.get("covers") if hasattr(pdf_config, "get") else None
        if covers is None:
            continue
        for key in ("front", "back"):
            val = covers.get(key) if hasattr(covers, "get") else None
            if val and val.endswith(".html.j2"):
                covers[key] = val.replace(".html.j2", ".html")

    return config
