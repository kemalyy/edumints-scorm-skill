# Interactivity, variables & gamification

These build on the **variables** system (declare in `variables`, persist in suspend_data → SCORM 2004).

## Variables
```jsonc
"variables": [ {"name":"name","type":"text","default":"Öğrenci"},
               {"name":"points","type":"number","default":0} ]
```
- **Interpolation:** `{{name}}` in any screen text shows the live value (personalization).
- **Set/modify:** `on_enter` (screen shown), `set_vars` (branch choice), `on_correct`/`on_wrong` (quiz),
  `on_timeout` (timer). Each: `[{"var":"x","op":"set|add","value":…}]`.

## Conditional paths
- `visible_if: {"var":"points","cmp":">=","value":100}` — screen is **skipped** in linear navigation when
  false. Use for adaptive remediation/enrichment (e.g., show a bonus screen only if score is high, or a
  remedial screen only if a flag is set).
- **branching** with `set_vars` — decisions that change later content/score. Build choose-your-path scenarios.

## Gamification (intrinsic, not patronizing)
- **Points HUD:** set course-level `points_var: "points"` → header shows a live points value, live. Feed it from
  `on_correct`, `set_vars`, `on_enter`.
- **Timer:** screen `timer_sec: 30` shows a ⏱ countdown (urgent < 10s). On expiry → `on_timeout` actions
  and `timeout_goto` (or auto-advance). Great for time-pressure challenges / serious games.
- **Patterns:** challenge progression (raise difficulty), feedback loops (points + immediate result),
  consequence (branching), mastery (gate enrichment behind score). Avoid leaderboards/sticker-only schemes.

## Animation
- **lottie** screens: designer animation (After Effects → Lottie JSON asset). Use for concept reveals,
  celebrations, illustrations. Opt-in/lazy — the library loads only if the course uses it (keeps simple
  courses light). Provide the JSON via `add_asset` (data-URI or URL; mime `application/json`).

## Composable game engine (`game` screen)
A serious game is a **composition**, not a fixed type — pick the mechanic that *carries* the learning
(intrinsic integration; the mechanic↔objective isomorphism is the #1 anti-slop rule). A `game` screen has:
- **`mechanics`** — any of `score` (streak/multiplier), `lives`, `timer` (must allow extend or disable —
  WCAG 2.2.1), `hints` (graduated, **cost-bearing** — free hints undercut learning).
- **`nodes`** — situation `content_html` + `choices`; each choice `on_choose` runs actions
  (`score.correct`/`lives.lose`/…) and `to` the next node (`null` = end). Give a `feedback_html` rationale
  on every consequence (especially penalties — teach *why*).
- **`rules`** — global `when <event> if <cond> then <actions>` (e.g. `when choice.taken then var.add`).
- **`template`** — `case_sim` (branching case/decision) or `escape_room` (locked chain). Scored by `pass_score`.
- **Design rule:** choices in a node must lead to *different* outcomes (no fake choice); the score must be
  tied to real decisions (not decoration). The `lint_course` tool enforces both.

## Adaptive practice (`adaptive_practice` screen)
Difficulty that fits the learner (flow / ZPD). Provide `items` (MCQ + `difficulty` logit + `explain_html`)
and choose `adaptive.strategy`:
- **`elo`** — tracks a single ability; serves the item whose success-probability is closest to
  `target_success` (~0.7). Good for mixed-topic practice / fast calibration.
- **`bkt`** — Bayesian Knowledge Tracing; tracks per-skill mastery, goes easiest→hardest, and can stop
  early at `mastery_stop`. Good for single-skill mastery + reporting.
Give ≥4 items with spread difficulty (range ≥0.5) — a flat bank makes adaptivity meaningless.

## Telemetry (xAPI / cmi5) — optional
Set course-level `xapi: { enabled: true, mode: "cmi5" | "explicit", activity_base }` to emit xAPI
statements (answered/passed/failed + ability/mastery extensions) from game/adaptive screens to an LRS.
Default **off**. cmi5 reads the LRS from the LMS launch; `explicit` takes an `endpoint`. **No LRS →
silent no-op (SCORM tracking is unaffected).** This is how mastery curves reach an LRS.
