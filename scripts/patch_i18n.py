"""Patch mkdocs-static-i18n to fix infinite on_post_build loop (v1.3.1 bug).

The bug: after the EN inner build completes, self.current_language='en' and
self.building=False. A mysterious 3rd on_post_build call (from the same outer
build command, same thread) bypasses the `if self.building` guard and rebuilds
NL → EN → NL → EN indefinitely.

Fix: add a `_multi_build_done` flag that is set to True after the first
complete on_post_build run. Subsequent calls return immediately.

Run before `mkdocs build` when MKDOCS_BUILD_I18N=true:
  python3 scripts/patch_i18n.py
"""

import site
import os
import sys

PATCH_MARKER = "_multi_build_done"

OLD_GUARD = """\
        if self.building:
            return

        self.building = True"""

NEW_GUARD = """\
        if self.building:
            return

        if getattr(self, '_multi_build_done', False):
            return

        self.building = True"""

OLD_DONE = "        self.building = False"
NEW_DONE = "        self._multi_build_done = True\n        self.building = False"


def find_plugin_py():
    candidates = [
        *site.getsitepackages(),
        site.getusersitepackages(),
    ]
    for d in candidates:
        path = os.path.join(d, "mkdocs_static_i18n", "plugin.py")
        if os.path.exists(path):
            return path
    return None


def main():
    plugin_py = find_plugin_py()
    if not plugin_py:
        print("ERROR: mkdocs_static_i18n/plugin.py not found", file=sys.stderr)
        sys.exit(1)

    with open(plugin_py, encoding="utf-8") as f:
        content = f.read()

    if PATCH_MARKER in content:
        print(f"Already patched: {plugin_py}")
        return

    if OLD_GUARD not in content:
        print(f"ERROR: expected guard code not found in {plugin_py}", file=sys.stderr)
        print("Plugin version may have changed — review patch_i18n.py", file=sys.stderr)
        sys.exit(1)

    content = content.replace(OLD_GUARD, NEW_GUARD, 1)
    content = content.replace(OLD_DONE, NEW_DONE, 1)

    with open(plugin_py, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Patched: {plugin_py}")


if __name__ == "__main__":
    main()
