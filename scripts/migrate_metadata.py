import os
import re

# Extremely robust string concatenation
P1 = r"## Documentbeheer\s+"
P2 = r"- \**Document-ID:\** .*\s+"
P3 = r"- \**Titel:\** .*\s+"
P4 = r"- \**Versie:\** (.*)\s+"
P5 = r"- \**Status:\** .*\s+"
P6 = r"- \**Eigenaar:\** .*\s+"
P7 = r"- \**Laatst herzien:\** (.*)\s+"
P8 = r"- \**Wijziging t.o.v. vorige versie:\** .*\s+"
P9 = r"______________________________________________________________________\s+"

DOC_BEHEER_PATTERN = re.compile(P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9, re.MULTILINE)

F1 = r"______________________________________________________________________\s+"
F2 = r"© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0."

MD_FOOTER_PATTERN = re.compile(F1 + F2, re.MULTILINE)


def migrate_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    versie = "1.0"
    datum = "2026-02-01"

    match = DOC_BEHEER_PATTERN.search(content)
    if match:
        versie = match.group(1).strip()
        datum = match.group(2).strip()
        content = DOC_BEHEER_PATTERN.sub("", content)

    content = MD_FOOTER_PATTERN.sub("", content)
    content = content.lstrip()

    if not content.startswith("---\n"):
        frontmatter = "---\nversie: '" + versie + "'\nlaatst_herzien: '" + datum + "'\n---\n\n"
        content = frontmatter + content

    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    return True


def main():
    docs_dir = "docs"
    count = 0
    for root, _dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                if migrate_file(file_path):
                    count += 1
    print("Finished. Migrated " + str(count) + " files.")


if __name__ == "__main__":
    main()
