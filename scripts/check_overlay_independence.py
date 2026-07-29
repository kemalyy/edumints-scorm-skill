#!/usr/bin/env python3
"""B4 (#15) — kaplama paket-bağımsızlık denetimi (grep 0 kapısı).

Kural: kaplama (overlay) metni hiçbir paket faz adı içeremez
(references/overlays/_FRAMEWORK.md). Bu betik references/pedagogy/*.md
ön-maddelerinden tüm faz id'lerini toplar ve references/overlays/*.md
dosyalarında arar; eşleşme sayısı 0 değilse FAIL.

Kullanım (repo kökünden):
    python3 -m pip install --quiet pyyaml
    python3 scripts/check_overlay_independence.py
"""

from __future__ import annotations

import pathlib
import re
import sys

import yaml  # pyyaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
REFS = ROOT / "authoring-scorm-courses" / "references"
PEDAGOGY = REFS / "pedagogy"
OVERLAYS = REFS / "overlays"


def phase_ids() -> set[str]:
    ids: set[str] = set()
    for path in PEDAGOGY.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---", 4)
        if end == -1:
            continue
        try:
            fm = yaml.safe_load(text[4:end]) or {}
        except yaml.YAMLError:
            continue
        for phase in fm.get("phases") or []:
            pid = phase.get("id")
            if pid:
                ids.add(pid)
    return ids


def main() -> int:
    ids = phase_ids()
    overlays = sorted(OVERLAYS.glob("*.md")) if OVERLAYS.is_dir() else []
    if not overlays:
        print("OK: references/overlays/ altında denetlenecek dosya yok")
        return 0
    if not ids:
        print(f"OK: paket faz id'si yok; {len(overlays)} kaplama dosyası trivially temiz")
        return 0

    hits = 0
    for path in overlays:
        text = path.read_text(encoding="utf-8")
        for pid in sorted(ids):
            for m in re.finditer(rf"(?<![\w]){re.escape(pid)}(?![\w])", text):
                line = text.count("\n", 0, m.start()) + 1
                print(f"FAIL {path.relative_to(ROOT)}:{line}: paket faz adı geçiyor: {pid!r}")
                hits += 1

    if hits:
        print(f"FAIL: {hits} eşleşme (0 olmalı) — kaplama metni paket faz adı içeremez (B4)")
        return 1
    print(f"OK: {len(overlays)} kaplama dosyasında {len(ids)} faz adından hiçbiri geçmiyor (grep 0)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
