import os
import re

# Comprehensive Mapping including variations and sub-codes
MAPPING = {
    "MOD-00": "Strategisch Kader",
    "MOD-01-07": "Bewijsstandaarden",
    "MOD-01": "AI-Native Fundamenten",
    "MOD-02": "Verkenning & Strategie",
    "MOD-03": "Validatie",
    "MOD-04": "Realisatie",
    "MOD-05": "Levering",
    "MOD-06": "Beheer & Optimalisatie",
    "MOD-07": "Compliance Hub",
    "MOD-08.01": "Technische Standaarden",
    "MOD-08": "Technische Standaarden",
    "MOD-09": "Toolkit & Templates",
    "MOD-12": "90-Dagen Startplan",
    "TMP-09-01": "Project Charter",
    "TMP-09-02": "Business Case",
    "TMP-09-03": "Risico Pre-Scan",
    "TMP-09-04": "Gate Review Checklist",
    "TMP-09-05": "Gouden Set Test",
    "TMP-09-06": "Doelkaart",
    "TMP-09-07": "Validatierapport",
    "TMP-09-08": "Traceerbaarheid Matrix",
    "TMP-09-10": "Prompt Template",
    "TMP-09-11": "Privacy & Data Blad",
    "GATE 1": "Gate 1 (Go/No-Go Ontdekking)",
    "GATE 2": "Gate 2 (Investering PoV)",
    "GATE 3": "Gate 3 (Productie-klaar)",
    "GATE 4": "Gate 4 (Livegang)",
}


def humanize_content(content, file_path):
    if "08-blueprint-methodologie.md" in file_path:
        return content

    sorted_codes = sorted(MAPPING.keys(), key=len, reverse=True)

    for code in sorted_codes:
        title = MAPPING[code]
        code_esc = re.escape(code).replace(r"\-", r"[-‑]")

        # 1. Handle Markdown Links: [CODE](path) -> [Title](path)
        # We use a lambda to avoid backreference issues with re.sub
        link_pattern = re.compile(r"\[(" + code_esc + r")\]\((.*?)\)", re.IGNORECASE)

        def link_repl(match):
            return f"[{title}]({match.group(2)})"

        content = link_pattern.sub(link_repl, content)

        # 2. Handle Standalone occurrences
        standalone_pattern = re.compile(
            r"(?<![#\-\w‑\[])" + code_esc + r"(?![#\-\w‑\]])", re.IGNORECASE
        )
        content = standalone_pattern.sub(title, content)

    return content


def main():
    docs_dir = "docs"
    changed_count = 0
    for root, _dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()

                new_content = humanize_content(content, file_path)

                if new_content != content:
                    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
                        f.write(new_content)
                    changed_count += 1
                    print(f"Humanized references in {file_path}")

    print(f"Finished. Updated {changed_count} files.")


if __name__ == "__main__":
    main()
