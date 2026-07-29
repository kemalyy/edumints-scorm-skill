#!/usr/bin/env python3
"""B3 (#14) — paket ön-madde doğrulayıcısı.

references/pedagogy/ altındaki her .md dosyasının (paketler + _STUB-* örnekleri;
_SCHEMA.md hariç) YAML ön-maddesini pack-frontmatter.schema.json'a karşı doğrular
ve şemanın ifade edemediği bütünlük denetimlerini yapar.

Kullanım (repo kökünden):
    python3 -m pip install --quiet pyyaml jsonschema
    python3 scripts/validate_packs.py
"""

from __future__ import annotations

import json
import pathlib
import sys

import yaml  # pyyaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parent.parent
PEDAGOGY = ROOT / "authoring-scorm-courses" / "references" / "pedagogy"
SCHEMA_PATH = PEDAGOGY / "pack-frontmatter.schema.json"


def frontmatter(path: pathlib.Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return yaml.safe_load(text[4:end])


def semantic_errors(fm: dict) -> list[str]:
    """Şemanın ifade edemediği bütünlük kuralları (_SCHEMA.md'de belgeli)."""
    errs: list[str] = []
    pk = fm.get("prior_knowledge") or []
    if len(pk) == 2 and pk[0] > pk[1]:
        errs.append(f"prior_knowledge min > max: {pk}")

    phases = fm.get("phases") or []
    ids = [p.get("id") for p in phases]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errs.append(f"tekrarlanan faz id'leri: {sorted(dup)}")
    idset = set(ids)

    declared = ([fm["evidence_phase"]] if "evidence_phase" in fm else []) + list(
        fm.get("evidence_phases") or []
    )
    for ph in declared:
        if ph not in idset:
            errs.append(f"evidence_phase(s) tanımsız faza işaret ediyor: {ph!r}")

    saf = fm.get("scoring_allowed_from")
    if saf not in idset:
        errs.append(f"scoring_allowed_from tanımsız faz: {saf!r}")
    else:
        cut = ids.index(saf)
        for p in phases[:cut]:
            if p.get("skorlanabilir"):
                errs.append(
                    f"faz {p['id']!r} scoring_allowed_from ({saf!r}) ÖNCESİNDE ama skorlanabilir: true"
                )

    if not any(p.get("skorlanabilir") for p in phases):
        errs.append("hiçbir faz skorlanabilir değil (en az biri true olmalı)")

    for p in phases:
        for nxt in p.get("sonraki") or []:
            if nxt not in idset:
                errs.append(f"faz {p['id']!r} 'sonraki' tanımsız faza işaret ediyor: {nxt!r}")
        if len(p.get("sonraki") or []) > 1 and not p.get("tekrar_kosulu"):
            errs.append(f"faz {p['id']!r}: birden çok 'sonraki' hedefi var ama 'tekrar_kosulu' yok")
    return errs


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    targets = sorted(p for p in PEDAGOGY.glob("*.md") if p.name != "_SCHEMA.md")
    if not targets:
        print("HATA: references/pedagogy/ altında doğrulanacak dosya yok")
        return 1

    failed = False
    for path in targets:
        fm = frontmatter(path)
        rel = path.relative_to(ROOT)
        if fm is None:
            print(f"FAIL {rel}: YAML ön-maddesi yok (--- ... --- bloğu)")
            failed = True
            continue
        errs = [
            f"şema: {'/'.join(map(str, e.path)) or '<kök>'}: {e.message}"
            for e in validator.iter_errors(fm)
        ] + semantic_errors(fm)
        if errs:
            failed = True
            print(f"FAIL {rel}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"OK   {rel} (pack: {fm.get('pack')})")

    if failed:
        return 1
    print(f"OK: {len(targets)} dosya şema + bütünlük denetiminden geçti")
    return 0


if __name__ == "__main__":
    sys.exit(main())
