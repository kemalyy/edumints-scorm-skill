# Contributing to the authoring-scorm-courses skill

Thanks for contributing! This skill teaches an AI client how to author SCORM courses with the
[edumints-scorm-mcp](https://github.com/kemalyy/edumints-scorm-mcp) server. Open-source by
[edumints.com](https://edumints.com).

## Ways to contribute
- Improve the guidance in `references/` (clarity, accuracy, new patterns).
- Add or refine `templates/` and `examples/` (must be original content — no third-party copyrighted material).
- Translate the README.
- Report issues or suggest improvements via [Issues](../../issues).

## Guidelines
- **Keep it tool-accurate.** `references/mcp-cookbook.md` must match the server's actual tools.
- **Endpoints are generic.** Reference the connector as a self-hosted endpoint
  (e.g. `http://localhost:8000/mcp`), not a specific hosted service.
- **No secrets, no third-party copyrighted content** (course text, screenshots, audio) in examples.
- **Valid JSON.** Any `.json` in `templates/`/`examples/` must parse and validate against the server's spec.
- **No emoji in course-facing content;** the skill teaches inline SVG icons instead.

## Pull requests
1. Make your change; ensure JSON files parse.
2. Open a PR using the template; describe the change.
3. CI validates the JSON and skill structure.

By contributing you agree to the [Code of Conduct](CODE_OF_CONDUCT.md) and the [MIT License](LICENSE).
