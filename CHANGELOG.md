# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [1.3.1] — 2026-07-23

`references/anti-slop.md` A1/A2/A3/B3 kurallarının artık scorm-mcp'nin `lint_course`'unda mekanik
olarak denetlendiğini belirten notlar (matches scorm-mcp 1.4.0's anti-slop mechanization — pre-flight
bu maddeler için artık modelin dürüstçe saymasına değil, gerçek bir sunucu-taraflı WARN'a dayanıyor).

### Changed
- `references/anti-slop.md` — A1 (`consecutive_content_slides`), A2 (`too_many_list_items`), A3
  (`generic_title`), B3 (`default_feedback`) her birine tek satırlık "artık mekanik denetleniyor" notu.

## [1.3.0] — 2026-06-26

Canva cross-MCP pipeline + SVG diagram pipeline (`svg_to_asset`) + `auto_tts` / `blocks[].width`
authoring guidance (matches scorm-mcp 1.3.0).

### Added
- `references/media.md` — **Canva cross-MCP pipeline** (generate → export → `add_asset` → asset id;
  TTL/signed-URL rules; Turkish-prompt + instructional-image rules).
- `references/mcp-cookbook.md` — `auto_tts` in `build_from_spec`; `content_slide` `blocks[].width`;
  `add_asset` return shape (`{ id, … }`) + "callable directly (may not surface in tool-search)" note;
  Canva/TTL note on `assets[]`.
- `SKILL.md` reference-file descriptions updated.
- **SVG diagrams** — `references/media.md` "SVG diagrams" section, `mcp-cookbook.md` `svg_to_asset`,
  anti-slop **C5** (no raw `<svg>`/`<canvas>`/`<script>` in `body_html`), and a "Known limits" section
  in `SKILL.md` (SVG-as-asset, animations → Lottie/MP4, `render_motion_video` Chromium fallback).

## [1.2.0] — 2026-06-24

Richer media authoring + screen reorder (matches scorm-mcp 1.2.0 / W9).

### Added
- `content_slide` **`blocks[]`** — interleave `paragraph → image → paragraph` in one screen
  (instead of consecutive content slides).
- **Per-item images** — `image_asset_id` on accordion/tabs items and timeline events;
  `front_asset_id` / `back_asset_id` on flashcard faces.
- **Inline assets** — `{{asset:<id>}}` interpolation in any `*_html` (embed a packaged asset in
  flowing text) and inline base64 `data:` URI `<img>`.
- **`reorder_screens`** tool documented (set an explicit screen order; `add_screen` appends).
- `references/mcp-cookbook.md` + `references/screen-types.md` updated for all of the above.

## [1.1.0] — 2026-06-15

Composable game engine + adaptive learning + telemetry guidance (matches scorm-mcp 1.1.0).

### Added
- Decision guides for the **2 new screen types** — `game` (composable serious game: mechanic primitives
  + `when event then action` rules + branching nodes; case_sim / escape_room) and `adaptive_practice`
  (Elo / Bayesian Knowledge Tracing → difficulty calibration). 26 → **28 screen types**.
- `references/interactivity-and-gamification.md` — composable game engine, adaptive practice (Elo vs BKT),
  and optional **xAPI / cmi5** telemetry sections.
- `references/mcp-cookbook.md` — `lint_course` (anti-slop quality gate) and `export_qti` (QTI 2.1 export)
  tools + copy-ready `game` / `adaptive_practice` spec shapes.
- `references/pre-flight.md` — mandatory `lint_course` `clean: true` gate before shipping game/adaptive courses.

## [1.0.0] — 2026-06-11

First stable release.

### Added
- **Anti-slop discipline** — a one-line Training Read (Bölüm 0), parametric dials
  (INTERACTIVITY/COGNITIVE_DENSITY/TONE/VISUAL_RICHNESS), `references/anti-slop.md` (binary bans with
  override paths + before/after JSON), and a mechanical `references/pre-flight.md` gate.
- Decision guides for **all 26 screen types** (games, customized results, visuals) + the MCP cookbook
  shapes, including the gamification HUD (`levels`/`lives_var`) authoring.
- **Topic→theme mapping** in `references/themes.md` — pick a subject-fitting visual identity (editorial,
  playground, clinical-calm…) so the interface differs by topic instead of looking uniform.
- Game-design patterns + scoring guidance (`references/` + the server's `docs/GAME-PATTERNS.md`).

## [Unreleased]

### Added
- Initial public release of the authoring-scorm-courses Claude Agent Skill.
- SKILL.md workflow + quality bar; references for instructional design, screen types, assessment,
  interactivity/gamification, media (cross-MCP + Piper TTS + local helper), programmatic video,
  themes, an authoring decision guide, and an MCP cookbook.
- Copy-and-adapt templates and a complete example course spec.
