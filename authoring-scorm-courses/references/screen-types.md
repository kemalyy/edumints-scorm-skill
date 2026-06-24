# Screen-type decision guide (28 types)

Pick by *intent*, not habit. Vary them.

## Content / presentation
- **title_slide** — open the course; set relevance. Supports `{{var}}` + background.
- **content_slide** — one idea. `layout`: text / text_media / media_text / full_media. Don't overload.
  **W9:** use `blocks[]` to interleave `paragraph → image → paragraph` in ONE screen instead of 3
  consecutive content slides.
- **accordion** — dense reference / FAQ; let learners expand on demand (native, accessible). *(W9: per-item `image_asset_id`.)*
- **tabs** — parallel facets of one topic (e.g., "What / Why / How"). *(W9: per-tab `image_asset_id`.)*
- **flashcards** — term ↔ definition; vocabulary; self-test recall. *(W9: `front_asset_id`/`back_asset_id`.)*
- **timeline** — chronology, process steps, history. *(W9: per-event `image_asset_id`.)*

> **Inline media (W9):** any `*_html` field accepts `{{asset:<id>}}` to embed a packaged asset inline in
> flowing text, plus inline base64 `<img src="data:image/…">`. Reorder screens with `reorder_screens`.
- **video** — demonstrations, talking-head, screen capture. `require_complete` to gate.
- **lottie** — designer-made animation (concept reveal, celebration, illustration). Opt-in/lazy.

## Practice / assessment (scored → tracked)
- **mcq** — single or multi (`multi_select`) select; the workhorse. Write plausible distractors.
- **true_false** — quick check; avoid ambiguity.
- **fill_blank** — recall of exact terms; list all `accepted` variants.
- **drag_drop** — categorize / map items to targets.
- **matching** — pair two columns (accessible select UI).
- **sorting** — order steps/ranking (give items in CORRECT order; runtime shuffles).
- **hotspot** — "find it on the image" (anatomy, UI, diagrams). Needs an image asset.
- **simulation** — guided multi-step software "try-mode" (İzle→Uygula→Sıra Sizde'nin "Uygula"sı):
  each step = a screenshot + a click region OR a text input; wrong → hint, all correct → scored.
- **decision_scenario** — branching **decision game** in one screen: stateful (score) narrative
  try-mode. Each choice carries a consequence + score delta; ends at a terminal node; scored by
  `pass_score`. Use for compliance/soft-skills/triage "what would you do?" practice.
- **term_match_race** — timed term↔definition matching **game** (gamified `matching` with a
  countdown + speed bonus). Vocabulary, terminology drilling under time pressure.
- **escape_room** — locked puzzle chain **game**: solve to unlock the next; lives + hints. High
  engagement for review/recall; keep puzzles answerable from the taught content.
- **labeled_diagram** — place labels onto positioned pins on an image (anatomy/diagram/map).
  Visual learning; scored. Needs an image asset + pins at normalized (x,y) 0–1000.
- **game** — **composable serious game** (not a fixed type): compose mechanic primitives
  (`score`/`lives`/`timer`/`hints`) + declarative `when event if cond then action` rules + branching
  content `nodes`. Templates: `case_sim` (branching case/decision), `escape_room` (locked chain). Use
  when the mechanic should *carry* the learning (intrinsic integration), e.g. clinical triage, incident
  response. Game a11y is enforced (hint text, timer extend/disable — WCAG 2.2.1). Scored by `pass_score`.
- **adaptive_practice** — competency-adaptive question bank: after each answer it estimates ability
  (**`elo`** — closest-to-target difficulty, flow) or mastery (**`bkt`** — Bayesian Knowledge Tracing,
  mastery + early stop) and serves the next item at the right difficulty. Give ≥4 items with spread
  `difficulty` (logit; harder = higher) + an `explain_html` each. Use for drill/review that should fit
  each learner instead of a fixed quiz.

## Visual content
- **data_chart** — server-side inline SVG chart (`bar`/`line`/`pie`). Passive data presentation /
  comparison; **not scored**. Use real data to make a point, not decoration.
- **image_compare** — draggable before/after slider (two images). Change/contrast (medical,
  design, before-after). Not scored.

## Results & participation
- **results_breakdown** — **customized results**: per-objective score breakdown computed on-show
  from the learner's answers + adaptive advice for weak sections. Map each section to its quiz
  `screen_ids`. Use as a richer, personalized alternative to `summary`. Not scored.
- **poll** — ungraded reflection/opinion (single/multi/open text) → reveals a reflection message.
  Self-assessment / engagement; doesn't gate Next.

## Decision / scenario
- **branching** — choices → different *screens*; consequence-based routing. Add `set_vars` to track
  decisions. (For a self-contained multi-step decision **game with score**, prefer `decision_scenario`.)
- **summary** — close: score, completion, recap.

**Selection heuristics:** sequence → timeline; terms → flashcards/term recall; categorize →
drag_drop/matching; process order → sorting; software "do it" → simulation; "what would you do?" /
consequence game → decision_scenario; **mechanic-driven serious game** (score/lives/timer/hints +
branching, intrinsic integration) → game; **adapt difficulty to the learner** → adaptive_practice;
cross-screen routing → branching; dense optional detail → accordion/tabs; visual concept →
lottie/video. After 1–2 content screens, insert a practice type.
Game design patterns & scoring: see the server's `docs/GAME-PATTERNS.md`, `docs/GAME-ECD.md`,
`docs/GAME-ADAPTIVE.md`. Before publishing a game/adaptive course, run `lint_course` (anti-slop gate).
