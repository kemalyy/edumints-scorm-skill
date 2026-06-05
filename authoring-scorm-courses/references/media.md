# Media — cross-MCP ingestion & ffmpeg

The unique strength: you (Claude) **orchestrate other MCP servers and local files**, then feed media to
scorm-mcp, which assembles + processes it into the package.

## Ingesting media (`add_asset`)
`add_asset(project_id, source, filename)` — `source` is either:
- a **data-URI** (`data:<mime>;base64,…`) — for bytes you produce or read from a local file, or
- an **https URL** — fetched server-side, **SSRF-guarded** (internal IPs blocked, redirects re-checked,
  size-capped, mime allowlisted: images, mp4/webm/ogg video, mp3/m4a/aac/ogg/wav/webm audio, pdf, json).

Typical orchestration (**primary path** for all media — audio/image/video):
- **Narration:** call a TTS MCP → get audio (URL or bytes) → `add_asset` → use as `narration_asset_id`
  (per-screen audio player) or feed into a video (below).
- **Images:** call an image-gen MCP or use provided URLs → `add_asset` → `media_asset_id` / `image_asset_id`.
- **Video:** call a video MCP (or `render_motion_video`, see `video-generation.md`) → `add_asset` / `video_asset_id`.
- **Local files:** read a file in the working dir → base64 data-URI → `add_asset`.

> Bringing media from **your own MCPs** is the main way — it gives you top quality and any language/voice.

## Built-in Turkish TTS (Piper) — optional alternative
- `synthesize_speech(project_id, text, voice=None, filename="narration.mp3")` → **Türkçe** mp3 narration
  asset (Piper, free, **offline, no GPU**). Use as `narration_asset_id`. Good for quick Turkish narration
  without an external TTS MCP. For top studio quality or other languages, prefer your own TTS MCP (above).
- LAZY: if Piper isn't installed the tool errors clearly; nothing else is affected.

## Local media helper (offload slow server render / local TTS)
Server video render has no GPU (slow). Run heavy media **locally** instead:
`python tools/local_media.py tts --text "…" --out a.mp3 --upload --project <id> --key sk_…`
or `... render --spec spec.json --out v.mp4 --quality high --upload …` — generates audio/video on your
machine (fast) and uploads via `add_asset`. Needs local piper-tts + Node/HyperFrames.

## Processing with ffmpeg (server-side, lazy)
- `make_video_from_image_audio(project_id, image_asset_id, audio_asset_id, filename)` → an **mp4** (still
  image + narration → narrated video, H.264/AAC). Use it for `video` screens. Great for turning a designed
  slide + TTS voice into a polished video segment.
- `normalize_audio_asset(project_id, audio_asset_id, filename)` → tarayıcı-safe mp3 (44.1k/128k) — run on
  wav/ogg/m4a from other MCPs so it plays everywhere.

ffmpeg is opt-in: it only runs when you call these tools; courses without media processing are unaffected.

## Guidance
- Keep media purposeful (it should teach, not decorate). Compress large media; the asset size counts
  against quota. Provide alt text / captions for accessibility.
