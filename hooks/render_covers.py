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

NL_MONTHS = {
    1: "januari", 2: "februari", 3: "maart", 4: "april",
    5: "mei", 6: "juni", 7: "juli", 8: "augustus",
    9: "september", 10: "oktober", 11: "november", 12: "december",
}


def _nl_now():
    """Retourneert datetime met een strftime-wrapper die Nederlandse maandnamen gebruikt."""
    dt = datetime.now()

    class NlDatetime:
        """Dunne wrapper rond datetime met Nederlandse datumformattering."""

        def strftime(self, fmt):
            result = dt.strftime(fmt)
            # Vervang Engelse maandnaam door Nederlandse
            result = result.replace(dt.strftime("%B"), NL_MONTHS[dt.month])
            result = result.replace(dt.strftime("%b"), NL_MONTHS[dt.month][:3])
            return result

    return NlDatetime()


def on_config(config):
    # Alleen uitvoeren als PDF-export actief is
    if not os.environ.get("MKDOCS_EXPORTER_PDF"):
        return config

    covers_dir = os.path.normpath(COVERS_DIR)
    env = Environment(loader=FileSystemLoader(covers_dir), autoescape=False)

    context = {
        "config": config,
        "now": _nl_now,
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
