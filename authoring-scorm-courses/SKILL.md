---
name: authoring-scorm-courses
description: Use when the user wants to create, build, or improve a SCORM-compliant training course, e-learning module, quiz, or interactive lesson with the scorm-mcp connector (your self-hosted server, e.g. http://localhost:8000/mcp). Covers instructional design, screen-type selection, assessment, theming, variables/gamification, media (TTS/ffmpeg), animation, and the build→preview→feedback→fix loop.
---

# Authoring SCORM courses with scorm-mcp

You are the **author**; the scorm-mcp server is the **assembler**. You design the pedagogy and
structure; the server validates, renders, and packages a self-contained SCORM zip that runs on any LMS.
Aim for courses that rival professional e-learning authoring tools — varied, interactive, accessible,
on-brand, slide-stage with a player and timed content reveal — not generic "click-next" modules.

## Workflow

1. **Clarify** (briefly): audience, one measurable learning objective, duration (target microlearning:
   3–8 min), source material, SCORM target (1.2 vs 2004 — use **2004** for branching/variables/games).
2. **Design the outline** before building. Map objective → chunks → practice → assessment → summary.
   Pick screen types deliberately (see `references/screen-types.md`). Vary them — avoid repetition
   (template fatigue is the #1 learner complaint).
3. **Theme**: pick a standard preset (`default`, `academic`, `modern-light`, `high-contrast`, `agency`,
   `dark`) and optionally override brand tokens. Light/neutral/high-contrast is the e-learning standard —
   never an arbitrary dark theme. See `references/themes.md`.
4. **Build** with `build_from_spec` (one JSON, token-efficient, preferred). See `references/mcp-cookbook.md`.
5. **Preview → review → fix loop**: call `preview`, share the hosted URL. The reviewer leaves comments on
   screens; you read them with `list_feedback` (no args = all pending across projects), apply edits, then
   `resolve_feedback`. Re-preview. See `references/mcp-cookbook.md`.
6. **Validate & package**: `validate_package` then `build_package` → download URL for the LMS.

## Quality bar (check before delivering)
- [ ] Objective is measurable (Bloom verb); every chunk maps to it.
- [ ] At least one interaction per ~2 content screens (quiz, drag, accordion, tabs, flashcards, matching…).
- [ ] Assessment is aligned, with feedback on both correct and incorrect.
- [ ] Visual variety (different screen types, not 8 identical content slides).
- [ ] Accessible: alt text on images, clear language, sufficient contrast (themes handle this).
- [ ] Lightweight: only add heavy capabilities (animation, video) where they teach something.
- [ ] Anlatımlı ekranlara `narration_text` (altyazı) + uygun `reveal`; quiz dışı içerik stage modunda akışlı (3–6 reveal bloğu, ölçülü animasyon). Detay: `references/authoring-recommendations.md`.

## When to reach for advanced capabilities
- **Variables/state + conditional** (`references/interactivity-and-gamification.md`): personalization
  (`{{name}}`), adaptive paths (`visible_if`), scoring beyond quizzes.
- **Gamification**: timer (time pressure), points HUD, quiz `on_correct`/`on_wrong` → points. Use
  *intrinsic* mechanics (challenge, progress) — not patronizing leaderboards/stickers.
- **Media** (`references/media.md`): pull narration from a TTS MCP, images from an image MCP, or local
  files → `add_asset` (**primary**); combine a slide image + narration into a video with
  `make_video_from_image_audio`. Built-in **Türkçe TTS**: `synthesize_speech` (Piper, free/offline) for
  quick Turkish narration. Slow server render? Use `tools/local_media.py` to generate media locally.
- **Animation**: `lottie` screens for designer-made motion (opt-in — only loads when used).
- **Programmatic video** (`references/video-generation.md`): `render_motion_video` (scene-spec →
  motion-graphic/data-viz MP4) + `render_screen_video` (stage screen → MP4). Use for explainer
  intros, animated data viz, summaries — passive content that teaches, not for assessment.

## Reference files (load as needed)
- `references/authoring-recommendations.md` — **karar rehberi: ne zaman/nasıl/neden.** Stage/timeline modu, narration yazımı, reveal seçimi, pedagojik ritim, kalite çıtası. Önce bunu oku.
- `references/mcp-cookbook.md` — exact tool calls, full build_from_spec shape (all 18 screen types) + the feedback loop.
- `references/course-patterns.md` — proven course structures to build (tool training, concept lesson, gamified, branching).
- `references/instructional-design.md` — objectives, structure, microlearning, anti-template-fatigue.
- `references/screen-types.md` — decision guide for all 18 screen types (incl. simulation).
- `references/assessment.md` — question/feedback/scoring design.
- `references/interactivity-and-gamification.md` — variables, conditions, timer, points, branching.
- `references/media.md` — TTS/image/video ingestion + ffmpeg + Lottie.
- `references/video-generation.md` — programatik video (VideoSpec → HyperFrames MP4): motion-graphic, veri-viz, slayt→video.
- `references/themes.md` — preset themes + customization.

## Templates & examples (copy and adapt)
- `templates/tool-training.json` — Watch→Apply→Your-Turn blueprint for teaching an app/tool.
- `templates/concept-lesson.json` — narrated concept/theory lesson blueprint.
- `examples/example-cybersecurity-course.json` — a complete, high-quality build_from_spec to study and adapt.
