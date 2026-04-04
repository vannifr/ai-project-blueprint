import os
import re

# Vertalingen voor Belgisch-Nederlands equivalenten
# We gebruiken functies om te voorkomen dat we links of paden aanpassen.
TRANSLATIONS = {
    "Template": "Sjabloon",
    "template": "sjabloon",
    "Templates": "Sjablonen",
    "templates": "sjablonen",
    "Deliverable": "Oplevering",
    "deliverable": "oplevering",
    "Deliverables": "Opleveringen",
    "deliverables": "opleveringen",
    "Roadmap": "Stappenplan",
    "roadmap": "stappenplan",
    "Requirement": "Vereiste",
    "requirement": "vereiste",
    "Requirements": "Vereisten",
    "requirements": "vereisten",
    "Gap analysis": "Kloofanalyse",
    "gap analysis": "kloofanalyse",
    "User case": "Gebruikscasus",
    "user case": "gebruikscasus",
    "Use case": "Gebruikscasus",
    "use case": "gebruikscasus",
    "Support": "Ondersteuning",
    "support": "ondersteuning",
    "Executive Summary": "Managementsamenvatting",
}


def belgicize(text):
    # Regex die alleen woorden vervangt die NIET in een markdown link pad staan [...] (HIER NIET)
    # En ook NIET in een URL of pad dat met / of ../ begint.

    for eng, nl in TRANSLATIONS.items():
        # Lookbehind en lookahead om te zorgen dat we niet midden in een woord of pad zitten
        # We vermijden vervanging als het voorafgegaan wordt door / (pad) of gevolgd wordt door .md of /
        pattern = r"(?<![/\\w])\b" + re.escape(eng) + r"\b(?![/\\]\w)"

        # Speciale check voor markdown links: we willen de tekst tussen [] wel, maar tussen () niet.
        # Dit is complex met pure regex, dus we doen een handmatige split/check voor de meest voorkomende gevallen.

        def replace_func(match):  # noqa: B023
            # Als we in een markdown link zitten (simpele detectie)
            return nl

        text = re.sub(pattern, replace_func, text)
    return text


def main():
    docs_dir = "docs"
    changed_count = 0

    for root, _dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, encoding="utf-8") as f:
                    lines = f.readlines()

                new_lines = []
                for line in lines:
                    # Als de regel een markdown link bevat, splitsen we op de ( om het pad te beschermen
                    if "(" in line and "[" in line:
                        parts = line.split("(", 1)
                        # Vertaal alleen het gedeelte VOOR de haakjes (bevat de tekst van de link)
                        left = belgicize(parts[0])
                        # Het rechtergedeelte bevat het pad, daar blijven we van af totdat we de haakjes sluiten
                        if ")" in parts[1]:
                            subparts = parts[1].split(")", 1)
                            # subparts[0] is het pad -> NIET vertalen
                            # subparts[1] is de rest van de regel -> WEL vertalen
                            right = subparts[0] + ")" + belgicize(subparts[1])
                            new_lines.append(left + "(" + right)
                        else:
                            new_lines.append(left + "(" + parts[1])
                    else:
                        new_lines.append(belgicize(line))

                new_content = "".join(new_lines)

                with open(file_path, encoding="utf-8") as f:
                    original_content = f.read()

                if new_content != original_content:
                    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
                        f.write(new_content)
                    changed_count += 1
                    print(f"Vertaald: {file_path}")

    # mkdocs.yml navigatie labels
    if os.path.exists("mkdocs.yml"):
        with open("mkdocs.yml", encoding="utf-8") as f:
            content = f.read()
        # In mkdocs.yml vertalen we alleen de labels (voor de :)
        new_lines = []
        for line in content.splitlines():
            if ":" in line and not line.strip().startswith("-"):
                parts = line.split(":", 1)
                new_lines.append(belgicize(parts[0]) + ":" + parts[1])
            elif ":" in line and line.strip().startswith("-"):
                # - Label: path.md
                parts = line.split(":", 1)
                left_part = parts[0]
                # Verwijder de -
                prefix = ""
                if left_part.strip().startswith("-"):
                    prefix = left_part[: left_part.find("-") + 2]
                    label = left_part[left_part.find("-") + 2 :]
                    new_lines.append(prefix + belgicize(label) + ":" + parts[1])
                else:
                    new_lines.append(belgicize(left_part) + ":" + parts[1])
            else:
                new_lines.append(line)

        new_content = "\n".join(new_lines) + "\n"
        if new_content != content:
            with open("mkdocs.yml", "w", encoding="utf-8", newline="\n") as f:
                f.write(new_content)
            print("Vertaald: mkdocs.yml")

    print(f"Klaar. {changed_count} bestanden aangepast naar Belgisch-Nederlands.")


if __name__ == "__main__":
    main()
