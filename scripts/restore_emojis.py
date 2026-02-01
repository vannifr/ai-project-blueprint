import os
import glob
import re

# Emojis
ROCKET = "\U0001F680"
BOOK = "\U0001F4D6"
TARGET = "\U0001F3AF"
SHIELD = "\U0001F6E1"
PEOPLE = "\U0001F465"
CALENDAR = "\U0001F4C5"
TOOLBOX = "\U0001F9F0"
PAPER = "\U0001F4C4"
BALANCE = "\u2696"
PIN = "\U0001F4CD"
WARNING = "\u26A0\uFE0F" # Adding VS16 for emoji presentation

# Mappings
CLEANUP_MAPPINGS = {
    "📍ï¸": PIN,
    r"\*\*Titel:\*\*\s*📍\s*": f"**Titel:** {ROCKET} ",
    r"(?m)^# 📍 ": f"# {ROCKET} ",
    r"📍\s*\*\*\[Leeswijzer": f"{BOOK} **[Leeswijzer",
    r"📍\s*\*\*\[90-Dagen": f"{CALENDAR} **[90-Dagen",
    r"📍\s*\*\*\[De toolkit": f"{TOOLBOX} **[De toolkit",
    r"📍 Ik ga bouwen": f"{TOOLBOX} Ik ga bouwen",
    r"📍 Hoe werkt dit": f"{BOOK} Hoe werkt dit",
    r"📍 Legenda": f"{BOOK} Legenda",
    r"📍 Doel:": f"{TARGET} **Doel:**",
    r"📍 Activiteit:": "📝 **Activiteit:**",
    r"📍 Checklist:": "✅ **Checklist:**",
    r"📍 Risico:": f"{WARNING} **Risico:**",
    r"📍 Rollen:": f"{PEOPLE} **Rollen:**"
}

DOCS_DIR = os.path.join(os.getcwd(), "docs")

def main():
    print("Starting emoji cleanup...")
    for file_path in glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        modified = False

        for key, value in CLEANUP_MAPPINGS.items():
            if re.search(key, content):
                content = re.sub(key, value, content)
                modified = True

        # Final check for ?? corruption
        if "??" in content:
             # This is a bit risky as ?? might be valid text, but following the PS1 logic
             # The PS1 logic was: if ($content -match "\?\?") { $content = $content -replace "\?\?", $pin }
             # We will be slightly more conservative and only replace if it looks like a bullet or icon
             if re.search(r"^\s*\?\?\s", content, re.MULTILINE):
                content = re.sub(r"^\s*\?\?\s", f"{PIN} ", content, flags=re.MULTILINE)
                modified = True

        if modified and content != original_content:
            print(f"Cleaned up: {file_path}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

    print("Emoji cleanup complete.")

if __name__ == "__main__":
    main()
