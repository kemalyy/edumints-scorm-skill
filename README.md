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
│   ├── authoring-recommendations.md # when/how/why decision guide (read first)
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
