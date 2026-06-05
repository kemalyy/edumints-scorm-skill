# Course patterns — production recipes

Proven structures to build with `build_from_spec`. Pick the pattern that fits the goal, then fill it with
the learner's content. Narrate every screen (`narration_asset_id`) and theme it (a light/standard preset).

## Pattern A — Tool / software training (the default for "teach an app/tool")
For **each sub-skill** of the tool, repeat **Watch → Apply → Your Turn**:
1. **Watch (İzle):** a `video` screen demonstrating the task in the real UI (narrated). Use
   `make_video_from_image_audio` if you only have a slide + narration.
2. **Apply (Uygula):** a `simulation` screen — guided, step-by-step over real screenshots. Each step is a
   click region OR a text-input (`input_accepted`); wrong → hint, correct → next; completing it scores.
3. **Your Turn (Sıra Sizde):** an unaided `mcq` / quiz with `feedback` and **remediation** — on wrong,
   branch back to the relevant Watch screen (use `branching` + `visible_if`), then return.
Wrap with: title → short intro → (Watch→Apply→Your Turn)×skills → summary (score). Track cumulative points
with a `points` variable + `points_var` (HUD) and `on_correct` on quizzes.

```
title → intro → [ video(İzle) → simulation(Uygula) → mcq(Sıra Sizde, remediation) ] × N → summary
```

## Pattern B — Concept / theory lesson (no specific tool)
For conceptual content (definitions, frameworks, why-it-matters):
- A few well-paced `content_slide`s (mix `layout`s + a `media_asset_id`), or `tabs`/`accordion` to chunk.
- A `timeline` if there's a sequence/history; `flashcards` for terms.
- Close with an **open reflection** (a free-text prompt) rather than a graded quiz, then a `summary`.
- Keep it one focused, narrated arc.

## Pattern C — Gamified assessment / challenge
- A `points` variable + `points_var` HUD; each `mcq`/`matching`/`sorting` adds points via `on_correct`.
- Add **time pressure** with `timer_sec` on some screens (`on_timeout` / `timeout_goto`).
- Use `visible_if` to unlock a bonus/celebration (`lottie`) screen when the score passes a threshold.
- End with a `summary` showing `{{points}}`.

## Pattern D — Branching scenario (decision training)
- `branching` screens where choices set variables (`set_vars`) and route to consequence screens.
- Use `visible_if` to show outcome screens based on the accumulated decisions.
- Good for soft-skills, compliance dilemmas, "what would you do" training.

## Universal quality rules
- Microlearning: one objective, ~4–8 min. Vary screen types (anti template-fatigue).
- Interaction at least every ~2 content screens. Feedback on correct AND incorrect.
- SCORM **2004** for branching/variables/games. Narrate everything. Accessible + light theme.
