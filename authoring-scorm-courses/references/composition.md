# Composition — focal point, emphasis hierarchy, balance

Every screen needs **one** place the eye lands first, a readable order after that, and a layout
chosen for the content — symmetric when the content is balanced, asymmetric when something must
lead. The server can do most of this for you; your job is to override it where the meaning
demands it.

> Applies to projects with `composition: "auto"` — the default for every **new** project
> (`create_project`, `build_from_spec`, `wrap_artifact`). Older projects are `"classic"` and ignore
> these fields (lint says `composition_ignored_classic`); upgrade one with
> `set_composition(project_id, "auto")`. Current release renders composition on `title_slide` and
> `content_slide`; other types keep their own layout for now.

## 1. Let the server choose first

If a screen has no `composition`, the server picks a pattern from the content itself:

| Content | Pattern it picks |
|---|---|
| title slide with a background image | `hero-focal` |
| title slide without | `centered` |
| a `lead` + ≤ 25 words, no media | `statement` |
| two images (≤ 3 blocks) | `split-halves` |
| 3–4 blocks with ≥ 2 images | `z-flow` |
| one image | `split-thirds` (mirrors on consecutive screens) |
| ≥ 4 list items or > 120 words | `f-flow` |
| anything else | `centered` |

It also sets the **course rhythm**: first screen, last screen and each unit opener are `high`
intensity, explanation screens `calm`, practice `normal` — and never three `high` in a row, never
the same pattern four times in a row. `lint_course` / `preview` return the resolved choice per
screen (`compositions: [...]`), so check it and override only where it is wrong for the meaning.

## 2. Focal point and the rule of thirds

- The focal element sits on one of the four **thirds intersections** — not dead centre — unless
  the moment is formal or symmetric (a title, a section opener, a single decision).
- Focal = the thing the question will be about: the image region, the number, the one sentence.
  If there is an image, the image is focal; otherwise `lead`; otherwise the title.
- **One focal per screen.** Two things competing (a big `lead` *and* a big image in `statement`)
  → `multiple_focal_points`.

## 3. Eye flow

- **Z-flow** — little text, strong visuals, a sequence or cause → effect. The eye goes
  top-left → top-right → bottom-left → **bottom-right**; put the result / call to action last.
- **F-flow** — scannable text, checklists, procedures. Left-aligned; the first lines carry the
  weight, so put the decisive item first.
- **Center** — one message, formal, calm.

## 4. Symmetric or asymmetric?

| Choose | When |
|---|---|
| **symmetric** (`centered`, `split-halves`) | comparison of equals, before/after, formal moments, balance is the point |
| **asymmetric** (`split-thirds`, `statement`, `hero-focal`, `z-flow`, `f-flow`) | something must lead: evidence + short explanation, a striking number, a scene, a sequence |

In asymmetric layouts **whitespace is the counterweight** — do not fill the empty two-thirds of a
`statement` screen.

## 5. Emphasis levels (type + colour together)

| Level | Role | Where it comes from |
|---|---|---|
| **E1** | focus — the one message | `lead`, the focal image frame, a big number |
| **E2** | structure | title, question stem |
| **E3** | emphasis | `kicker`, `<mark>` in any `*_html` |
| **E4** | body | paragraphs, options |
| **E5** | background | captions, sources, progress |

Rules: one E1 per screen · `lead` ≤ 20 words (`lead_too_long`) · ≤ 3 `<mark>` per screen
(`mark_overuse`) · emphasised text (`<mark>` + `<strong>`) ≤ 20 % of the block
(`emphasis_inflation`). Colours come from the theme (`mint` by default; `ink`, `slate` also ship);
hierarchy is carried by neutrals with a **single accent family** — never several bright colours.

## 6. Writing it

```jsonc
// 1 · just a pattern
{ "type": "content_slide", "title": "Check the sender", "kicker": "Step 1",
  "lead": "The domain is one letter off.", "media_asset_id": "mail",
  "body_html": "<p>Read the address <mark>letter by letter</mark>.</p>",
  "composition": "split-thirds" }

// 2 · pattern + fine-tuning: image left, focal on the lower-left intersection
{ "composition": { "preset": "split-thirds", "mirror": true, "focal": "r3c1" } }

// 3 · fully free: 1:2 columns, text top-left, media bottom-right, Z flow, generous whitespace
{ "composition": { "grid": "1:2",
                   "areas": { "support": "c1r1-c1r2", "focal": "c2r2-c2r3" },
                   "focal": "focal", "flow": "z", "whitespace": "high" } }
```

Grid cells are `c{column}r{row}` (1-based, rows 1–3); an area is `cXrY-cXrY` (both ends
inclusive). Slots: `support` (title + text), `focal`, `aux` (second image), `steps` (z-flow
sequence). `list_compositions()` lists the catalogue and which screen types each pattern fits.
Invalid patterns/areas fail the build (`composition_unknown`, `focal_area_empty`).
