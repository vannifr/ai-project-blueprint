import os
import yaml
import datetime
import re

# Custom loader to ignore tags like !!python/name:...
class CustomLoader(yaml.SafeLoader):
    pass

def construct_undefined(loader, node):
    return None

CustomLoader.add_constructor(None, construct_undefined)

REPO_ROOT = os.getcwd()
MKDOCS_YAML = os.path.join(REPO_ROOT, "mkdocs.yml")
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
OUTPUT_FILE = os.path.join(REPO_ROOT, "FULL_PLAYBOOK_EXPORT.md")

def get_nav_files(nav):
    files = []
    if not nav:
        return []
    for item in nav:
        if isinstance(item, str):
            files.append(item)
        elif isinstance(item, dict):
            for k, v in item.items():
                if isinstance(v, str):
                    files.append(v)
                elif isinstance(v, list):
                    files.extend(get_nav_files(v))
    return files

def main():
    print(f"Exporting Playbook Documentation to {OUTPUT_FILE}...")

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    with open(MKDOCS_YAML, 'r', encoding='utf-8') as f:
        config = yaml.load(f, Loader=CustomLoader)

    nav_files = get_nav_files(config.get('nav', []))

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        outfile.write(f"# AI Project Playbook - Full Export\n\nGenerated on: {datetime.datetime.now()}\n\n---\n")

        for relative_path in nav_files:
            # mkdocs nav paths are relative to docs_dir
            absolute_path = os.path.join(DOCS_DIR, relative_path)

            if os.path.exists(absolute_path):
                print(f"Processing: {relative_path}")

                title = os.path.splitext(os.path.basename(relative_path))[0].replace('-', ' ').title()
                outfile.write(f"\n# Document: {title}\n")
                outfile.write(f"Source: {relative_path}\n")
                outfile.write("---")

                with open(absolute_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    # Strip frontmatter
                    content = re.sub(r'^---.*?---\n\n?', '', content, flags=re.DOTALL)
                    outfile.write(content)

                outfile.write("\n\n---\n")
            else:
                print(f"Warning: File not found: {absolute_path}")

    print(f"Export completed: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
