# Screen-type decision guide (17 types)

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

## Decision / scenario
- **branching** — choices → different screens; consequence-based learning. Add `set_vars` to track decisions.
- **summary** — close: score, completion, recap.

**Selection heuristics:** sequence → timeline; terms → flashcards; categorize → drag_drop/matching;
process order → sorting; decision/consequence → branching; dense optional detail → accordion/tabs;
visual concept → lottie/video. After 1–2 content screens, insert a practice type.
