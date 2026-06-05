# Assessment design

**Align to the objective.** Test what you taught, at the right Bloom level. If the objective is "apply",
use a scenario MCQ, not a recall true/false.

**Question quality:**
- Stem: one clear question; no negatives/trick wording.
- Distractors (MCQ): plausible, parallel in length/grammar; based on real misconceptions; no "all/none of
  the above" as filler.
- fill_blank: list every `accepted` spelling/synonym; set `case_sensitive` only when it truly matters.
- matching/sorting: keep sets small (2–6) and unambiguous.

**Feedback (always set both):** `feedback.correct_html` reinforces *why* it's right; `feedback.incorrect_html`
corrects the misconception (not just "wrong"). `show_correct_answer: true` for learning checks, false for
high-stakes graded items.

**Scoring & completion:** put `points` on graded items; set `tracking.completion_rule`
(`viewed_all` / `passed_quiz` / `viewed_all_and_passed`) and `passing_score`. Use **SCORM 2004** so
completion_status and success_status are tracked separately.

**Gamify assessment (optional):** `on_correct: [{var:"points",op:"add",value:10}]` + `points_var` → a live
points HUD. Add a `timer_sec` for time-pressure quizzes. Keep it *intrinsic* (mastery, challenge) — not
patronizing.

**Knowledge checks vs exams:** sprinkle ungraded checks (immediate feedback, retry-friendly) through the
content; reserve a graded assessment for the end.
