# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/).

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
