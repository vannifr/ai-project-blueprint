import os
import re

# Mapping of mojibake patterns to correct UTF-8 characters
REPLACEMENTS = {
    'â€”': '—',   # em dash
    'â€“': '–',   # en dash
    'â€™': '’',   # smart quote / apostrophe
    'â€‘': '‑',   # non-breaking hyphen
    'â€œ': '“',   # left double quote
    'â€': '”',    # right double quote (often seen as â€ followed by space or punctuation)
    'Ã«': 'ë',
    'Ã©': 'é',
    'Ã¯': 'ï',
    'Ã¼': 'ü',
    'Ã³': 'ó',
    'Ã¡': 'á',
    'Ãº': 'ú',
    'Ã': 'à',     # Often used in "Ã " -> "à "
    'â‰¥': '≥',   # greater than or equal
    'â‰¤': '≤',   # less than or equal
    'â†’': '→',   # arrow
    'â‰': '≠',    # not equal
    'âš–ï¸': '⚖️',
    'âš™ï¸': '⚙️',
    'âœ…': '✅',
    'ðŸ§™”â™‚ï¸': '🧙‍♂️',
    'â†”': '↔',
}

def fix_file(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()

    # Remove BOM if present
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]

    try:
        text = content.decode('utf-8')
    except UnicodeDecodeError:
        # Fallback if it's actually latin-1
        text = content.decode('latin-1')

    original_text = text
    for mojibake, correct in REPLACEMENTS.items():
        text = text.replace(mojibake, correct)

    if text != original_text or content.startswith(b'\xef\xbb\xbf'):
        print(f"Fixing {file_path}")
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        return True
    return False

def main():
    docs_dir = 'docs'
    fixed_count = 0
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if fix_file(file_path):
                    fixed_count += 1

    # Also fix the export file if it exists
    if os.path.exists('FULL_PLAYBOOK_EXPORT.md'):
        fix_file('FULL_PLAYBOOK_EXPORT.md')
        fixed_count += 1

    print(f"Finished. Fixed {fixed_count} files.")

if __name__ == "__main__":
    main()
