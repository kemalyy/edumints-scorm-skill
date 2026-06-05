# Themes

E-learning standard = light/neutral background, high-contrast text, one or two accent colors, generous
whitespace, WCAG AA. **Never an arbitrary dark theme** unless the brand truly calls for it.

## Presets (pass the name as `theme`)
- **default** — clean blue, white bg, professional. Safe corporate default.
- **modern-light** — teal accent, crisp, generous spacing. Modern/product training.
- **academic** — serif headings, warm neutral, navy/gold. Education/scholarly.
- **high-contrast** — WCAG AA+, Atkinson Hyperlegible, black/white/strong accent. Accessibility-critical.
- **agency** — bold indigo, Sora headings. Marketing/creative.
- **dark** — tasteful dark; only when intended (e.g., dev/IT audience).

## Customization (preset + brand overrides)
Pick a preset, then override only the tokens you need via `set_theme` (deep-merge — unset tokens keep the
preset's values), or pass a full ThemeTokens object as `theme`.
```jsonc
// build_from_spec with a preset, then brand the primary color:
set_theme(project_id, { "color": { "primary": "#FF6B00", "primary_hover": "#e85f00" } })
```
ThemeTokens groups: `typography` (fonts, scale, weights, line-height), `color` (primary/secondary/accent
+ bg/surface/border/text/state colors + focus_ring), `spacing`, `radii`, `elevation`, `motion`
(durations/easing, `reduce_motion_respect`), `background_pattern` (none/dots/grid/gradient), `custom_css`.

## Tips
- Match the accent to the brand; keep text near-black on near-white for contrast.
- `background_pattern: "gradient"` adds subtle depth on title-heavy courses; "none" for dense reading.
- Don't override so much that you break contrast — verify against the high-contrast baseline if unsure.
