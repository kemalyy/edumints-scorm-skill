# Screen-type decision guide (19 types)

Pick by *intent*, not habit. Vary them.

## Content / presentation
- **title_slide** — open the course; set relevance. Supports `{{var}}` + background.
- **content_slide** — one idea. `layout`: text / text_media / media_text / full_media. Don't overload.
- **accordion** — dense reference / FAQ; let learners expand on demand (native, accessible).
- **tabs** — parallel facets of one topic (e.g., "What / Why / How").
- **flashcards** — term ↔ definition; vocabulary; self-test recall.
- **timeline** — chronology, process steps, history.
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

## Decision / scenario
- **branching** — choices → different *screens*; consequence-based routing. Add `set_vars` to track
  decisions. (For a self-contained multi-step decision **game with score**, prefer `decision_scenario`.)
- **summary** — close: score, completion, recap.

**Selection heuristics:** sequence → timeline; terms → flashcards/term recall; categorize →
drag_drop/matching; process order → sorting; software "do it" → simulation; "what would you do?" /
consequence game → decision_scenario; cross-screen routing → branching; dense optional detail →
accordion/tabs; visual concept → lottie/video. After 1–2 content screens, insert a practice type.
Game design patterns & scoring: see the server's `docs/GAME-PATTERNS.md`.
