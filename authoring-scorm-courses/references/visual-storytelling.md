# Visual Storytelling — from "correct" to "memorable"

A structurally sound course can still feel **ordinary**: walls of centered text, isolated
concept→quiz units, the same layout fourteen times. This reference distills the rules that
turn that course into one people remember — proven on a full showcase rebuild (the
"Spot the Phish" demo) and now partially machine-checked by `lint_course`.

**Read this after `anti-slop.md`. Apply it during outlining, not as a polish pass** — narrative
and visuals decided after the fact always look bolted on.

## 1. The narrative thread (one scene, opened and closed)

Open the course inside a concrete scene and close it inside the same scene. Screens are not
independent units; they are moments of one unfolding situation.

- Weak: title "Email Security Essentials" → 12 topic screens → summary "Course complete".
- Strong: title **"Monday, 8:47 a.m. — three emails are waiting; one is a trap"** → every
  screen advances that morning (dissect email 1, compare email 3 to its clone, triage the
  inbox) → summary **"9:00 a.m. — inbox zero, breach zero"**.

Rules of thumb:
- The learner has a role in the scene (second person works: *your* inbox, *your* allowance).
- Interactive screens are **events in the story**, not exercises about it ("8:52 — clear your
  inbox" instead of "Knowledge check 2").
- The summary returns to the opening scene and names what changed.

## 2. Per-screen visual budget

Every concept gets the question: **"what would this look like?"** If three consecutive screens
have no visual, that is a design smell — and `lint_course` now warns (`text_only_run` at 4+,
`visual_poverty` below 25% visual screens on 8+ screen courses). Don't write toward the limit;
treat one visual-bearing screen in every two-to-three as the floor.

What counts as a visual: `blocks[]` images in content slides, per-item images (accordion,
tabs, timeline, flashcards, game/scenario nodes), and the inherently visual screen types
(`data_chart`, `image_compare`, `hotspot`, `labeled_diagram`, `simulation`, `video`, `lottie`).

## 3. Find, don't read — show, don't tell

The strongest upgrade path for any explanatory screen:

| If the content is… | Don't write a paragraph — use |
|---|---|
| "here are the N things to check on X" | `simulation` steps ON a realistic image of X — learner clicks each thing ("Find the red flags" on a mock phishing email) |
| a comparison of two states/versions | `image_compare` slider (real email ↔ its malicious clone; trained model ↔ untrained) |
| a process that unfolds over time | `timeline` with an image per event ("what one click sets in motion: 08:49 click → 08:50 harvest → 11:20 weaponised → day 3 ransomware") |
| a striking number | a **stat-card SVG**: one huge number + one sentence (see §5) |
| parts of a structure | `labeled_diagram` on your own SVG |

`image_compare` lesson learned: put per-image labels/badges on the **same side** for both
images (e.g. top-left) so the visible badge always belongs to the content on that side of the
slider — a right-side badge produces a misleading chimera at the midpoint.

## 4. Realistic artifact mockups as SVG

When the subject IS an artifact (an email, a UI, a form, a receipt), the centerpiece visual is
a realistic mockup of that artifact, authored as SVG and attached with `add_asset` (data-URI)
or `svg_to_asset`. Recipe for an email-client mockup that reads as real:

- Window chrome: rounded card on a grey desktop, traffic-light dots, a muted header bar.
- Subject as a bold 24-26px line; sender row with avatar circle, **display name AND the real
  address in angle brackets** (the address is where the teaching happens — color it).
- Body in 15-16px system font (`-apple-system, Segoe UI, …`), realistic copy, not lorem.
- A CTA button **plus the true link target printed beside it** (that mismatch is a lesson).
- An attachment chip (icon square + filename + size).
- Give the SVG explicit `width`/`height` attributes — hotspot/simulation region math uses
  `naturalWidth`, which for SVG comes from those attributes.
- Simulation/hotspot region coords are **natural-image pixels**, rect = `[x, y, WIDTH,
  HEIGHT]` (not x2/y2). Compute them from your own SVG geometry, then verify by clicking.

## 5. Data as image

Two reusable patterns, both plain SVG:

- **Stat card**: dark rounded rectangle, one enormous number (90-110px, accent color), one
  short muted sentence under it; optionally two stats split by a hairline. Use as the first
  `blocks[]` item with the prose below it, and cite the source in the block `caption`.
- **Chain-of-events cards**: for timeline events, small landscape cards (icon disc + title +
  one-line consequence) with a colored edge strip that escalates (amber → red → purple).

## 6. Sourcing images: `search_images` → `add_asset`

For photographic/illustrative needs, the server's `search_images` tool queries **CC0/Public
Domain** sources (Openverse, Wikimedia Commons) and returns candidates with `url`, `license`,
`creator`. Pick one and attach it with `add_asset(project_id, source=url, filename=…)` —
download and SSRF checks happen server-side. Credit the creator in a caption when one is
named. For diagrams, mockups and stat cards, authored SVG (this document) beats stock every
time.

## Pre-flight addition

Before building, verify alongside the `pre-flight.md` matrix:
- [ ] The course opens and closes inside one concrete scene, and quiz/game screens are events
      in it.
- [ ] No 3+ consecutive screens without a visual; every "list of things to check/compare/
      steps" got the §3 treatment instead of a paragraph.
- [ ] Headers carry content ("The One Signal That Can't Be Faked"), not furniture
      ("Checkpoint", "Quick Check").
