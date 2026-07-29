# Authoring SCORM Courses — a Claude Agent Skill

> A **Claude Agent Skill** that teaches an AI client how to author high-quality, interactive,
> SCORM-compliant e-learning courses with the **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)** server.

**🌐 Languages:** [English](README.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Azərbaycanca](README.az.md) · [Қазақша](README.kk.md) · [Кыргызча](README.ky.md)

Open-source, developed by the **[edumints.com](https://edumints.com)** platform. Open to contribution.

---

## What this is

A [Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) is a folder of
instructions that an AI client loads on demand. This skill gives the model the **instructional-design
judgment** and the **exact tool recipes** to turn a request like *"make a 6-minute course on phishing"*
into a polished SCORM package: clear objectives, varied screen types, aligned assessment, on-brand
theming, a slide-stage player with timed reveal, media, and the build → preview → feedback loop.

The skill is the **author's playbook**; the scorm-mcp server is the **assembler**.

## Structure (progressive disclosure)

```
authoring-scorm-courses/
├── SKILL.md                         # entry point: workflow + quality bar
├── references/
│   ├── anti-slop.md                 # anti-slop discipline: training read + parametric dials (read FIRST)
│   ├── pre-flight.md                # MANDATORY pre-build quality-gate matrix
│   ├── core/                        # Layer 1 — method-independent core rules (+ the Layer-0 selector)
│   │   ├── method-selector.md       # Layer 0 — outcome type + dials → method pack(s) + overlay(s)
│   │   ├── evidence-binding.md      # every scored question binds to an in-course evidence source (K1–K6)
│   │   ├── alignment.md             # objective→question→evidence mapping + warn threshold (H1–H3)
│   │   ├── feedback-anatomy.md      # 3 mandatory feedback elements — floor rule (G1–G3)
│   │   └── scoring-timing.md        # formative/summative + "no score before evidence" (Z1–Z3)
│   ├── eval/
│   │   └── blind-test.md            # blind-test protocol (≥ 1/2 pass threshold) — gate for new screen types
│   ├── pedagogy/                    # Layer 3 — method packs (C series)
│   │   ├── _SCHEMA.md               # pack front-matter contract (evidence_phase(s) REQUIRED) + validation command
│   │   ├── _STUB-dogrusal.md        # schema-validation example: linear flow (not a pack)
│   │   ├── _STUB-dongulu.md         # schema-validation example: cyclic flow (not a pack)
│   │   ├── rosenshine-di.md         # C1 — Direct Instruction: model-first, guided→independent practice
│   │   ├── merrill-fpi.md           # C2 — Merrill First Principles: task-centered activation→demonstration→application→integration
│   │   ├── 5e-inquiry.md            # C3 — BSCS 5E inquiry cycle: explore-first (requires the exploration screen type)
│   │   └── 4cid.md                  # C4 — 4C/ID complex-skill training: whole tasks, simple→complex, fading support
│   ├── overlays/                    # Layer 2 — method-orthogonal overlays (D series)
│   │   └── _FRAMEWORK.md            # overlay file format + pack-independence rule + conflict format
│   ├── visual-storytelling.md       # narrative thread + per-screen visual budget + mockup-SVG recipes
│   ├── authoring-recommendations.md # when/how/why decision guide
│   ├── mcp-cookbook.md              # exact tool calls + full build_from_spec shape
│   ├── course-patterns.md           # proven course structures
│   ├── instructional-design.md      # objectives, microlearning, anti-template-fatigue
│   ├── screen-types.md              # decision guide for all screen types
│   ├── assessment.md                # question/feedback/scoring design
│   ├── interactivity-and-gamification.md
│   ├── media.md                     # cross-MCP media + built-in Turkish TTS + local helper
│   ├── video-generation.md          # programmatic motion-graphic / data-viz video
│   └── themes.md
├── templates/                       # copy-and-adapt blueprints
└── examples/                        # a complete, high-quality example course spec
```

## Requirements

- The **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)** server, reachable by your
  AI client (self-host it, or point at your own deployment).
- An MCP client that supports Agent Skills (e.g., Claude).

## Install

**claude.ai (Skills):** zip the `authoring-scorm-courses/` folder and upload it under
Settings → Capabilities → Skills → Create skill.
```bash
cd authoring-scorm-courses && zip -r ../authoring-scorm-courses.zip . && cd ..
```

**Claude Code / local:** copy the `authoring-scorm-courses/` folder into your skills directory
(e.g. `~/.claude/skills/authoring-scorm-courses/`).

Then connect the scorm-mcp server and ask the model to build a course — it will follow this skill.

## License

**MIT** — see [LICENSE](LICENSE). Developed by **edumints.com**. Product names referenced are
trademarks of their respective owners (nominative use only).
