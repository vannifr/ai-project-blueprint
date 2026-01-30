def on_page_content(html, page, config, files):
    # Voeg noindex meta tag toe aan de head (via een hack, want we kunnen niet direct in <head> schrijven met deze hook)
    # Een betere manier voor Material theme is via 'extra_head' template block, maar dat vereist theme extension.
    # Voor nu vertrouwen we op robots.txt, maar we kunnen proberen het via JS te injecteren als fallback.
    return html

def on_config(config):
    # Zorg dat de theme custom_dir ingesteld is om templates te overschrijven
    config['theme']['custom_dir'] = 'overrides'
    return config
