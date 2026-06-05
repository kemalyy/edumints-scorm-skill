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
