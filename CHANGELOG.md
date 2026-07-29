# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added — v2.1 Katman 0 seçici + paket şeması (Wave 3: B1–B4)
- **`references/core/method-selector.md`** (#12) — Katman 0 yöntem seçici: 7 kazanım türü + 5 girdi
  (PRIOR_KNOWLEDGE / hata maliyeti / zaman / platform / bağlam) → paket(ler) + kaplama(lar).
  Mekanizma (KARAR ÖNERİSİ, needs-decision): **LLM muhakemesi + deterministik uyumluluk elemesi** —
  paket ön-maddesindeki `outcome_types`/`prior_knowledge`/`error_cost`/`requires_platform` sert
  kısıtları eleyici; sağ-kalanlar arasında gerekçeli seçim; son karar yazarın, gerekçe zorunlu.
  7 örnek eşleme + eksik-girdi varsayılanları + B3-uyumlu YÖNTEM BEYANI çıktı biçimi. Hiçbir paket
  kanonik değil; hiçbiri uymazsa belgeli varsayılan `gagne-9` + zorunlu gerekçe.
- `references/pre-flight.md` — yeni Madde 1b: YÖNTEM BEYANI (paket + kaplamalar + elenenler +
  gerekçe) kaydı zorunlu.

### Added — v2.0 Kanıt Bağlama çekirdeği (Wave 1: A1–A5 + E4)
- **`references/core/` (Katman 1 — yöntemden bağımsız çekirdek kurallar; hiçbir kural bir pedagoji
  paketinin faz adını içermez, sıra dayatmaz):**
  - `evidence-binding.md` (#6) — K1–K3: skorlanan her soru kurs-içi kanıt kaynağına bağlanır
    (≥ 6 geçerli kaynak türü); birebir denetim sorusu ("Bu kursu hiç görmemiş ama alanı bilen biri
    bu soruyu zaten cevaplayabilir mi?") + numaralı "bağla ya da at" prosedürü.
  - `alignment.md` (#7) — H1–H3: hedef→soru→kanıt eşleme tablosu biçimi + "skorlanan ekran >
    hedef + 1" sayısal UYARI eşiği (warn, fail değil) + tam eşleme örneği.
  - `feedback-anatomy.md` (#8) — G1–G3: gerekçeli geri bildirimin 3 zorunlu öğesi (neden doğru /
    neden yanlış / kanıta geri işaret); anti-slop B3 TABAN statüsüne yükseltildi ve fazsız yazıldı.
  - `scoring-timing.md` (#9) — Z1–Z3: formatif/summatif tanımları; "kanıt kaynağı üretilmeden skor
    yok" ilkesi; skorsuz erken-deneme istisnası.
- **`references/eval/blind-test.md`** (#11) — kör test protokolü: kanıt kaynakları çıkarılmış kursta
  skorlanan sorular alan-bilgili okuyucu tarafından cevaplanabiliyor mu? Geçme eşiği **≥ 1/2**;
  sonuç kayıt şablonu; pilot koşu kaydı (amiral gemisi örnek: 1/4 → KALDI). F1/F2 ekran tiplerinin
  kapısı.

### Changed — v2.0 Kanıt Bağlama çekirdeği
- `references/anti-slop.md` (#10) — 17 kuralın tavan/taban sınıflandırma tablosu + yeni **T1–T3
  taban kuralları** (skorlanan soruya kanıt kaynağı VAR; iddiaya mekanizma taşıyıcısı VAR;
  `incorrect_html` kanıta geri işaret) + B3 taban yükseltmesi (fazsız yeniden yazım).
- `references/pre-flight.md` — yeni 9d (tabanlar T1–T3) ve 12b (kanıt bağlama) maddeleri; 12'ye
  hedef→soru→kanıt tablosu + H3 eşiği eklendi.
- `SKILL.md` — referans listesine `core/` ve `eval/` dosyaları eklendi.
- CI D4 drift kapısı `references/` alt dizinlerini de sayacak şekilde `rglob`'a çevrildi; README
  Structure ağacına `core/` ve `eval/` eklendi.

### Added — visual storytelling (W11)
- New `references/visual-storytelling.md` — the anti-ordinariness playbook distilled from the
  "Spot the Phish" showcase rebuild: narrative thread (one scene, opened and closed),
  per-screen visual budget, "find don't read" conversions (simulation/image_compare/timeline),
  realistic artifact mockup-SVG recipe, stat-card pattern, `search_images` → `add_asset` flow.
- `SKILL.md` reference list + `pre-flight.md` new item 9c (visual density & narrative checks,
  aligned with the server's new `text_only_run`/`visual_poverty` lint rules).

## [1.3.1] — 2026-07-23

`references/anti-slop.md` A1/A2/A3/B3 kurallarının artık scorm-mcp'nin `lint_course`'unda mekanik
olarak denetlendiğini belirten notlar (matches scorm-mcp 1.4.0's anti-slop mechanization — pre-flight
bu maddeler için artık modelin dürüstçe saymasına değil, gerçek bir sunucu-taraflı WARN'a dayanıyor).

### Changed
- `references/anti-slop.md` — A1 (`consecutive_content_slides`), A2 (`too_many_list_items`), A3
  (`generic_title`), B3 (`default_feedback`) her birine tek satırlık "artık mekanik denetleniyor" notu.

## [1.3.0] — 2026-06-26

Canva cross-MCP pipeline + SVG diagram pipeline (`svg_to_asset`) + `auto_tts` / `blocks[].width`
authoring guidance (matches scorm-mcp 1.3.0).

### Added
- `references/media.md` — **Canva cross-MCP pipeline** (generate → export → `add_asset` → asset id;
  TTL/signed-URL rules; Turkish-prompt + instructional-image rules).
- `references/mcp-cookbook.md` — `auto_tts` in `build_from_spec`; `content_slide` `blocks[].width`;
  `add_asset` return shape (`{ id, … }`) + "callable directly (may not surface in tool-search)" note;
  Canva/TTL note on `assets[]`.
- `SKILL.md` reference-file descriptions updated.
- **SVG diagrams** — `references/media.md` "SVG diagrams" section, `mcp-cookbook.md` `svg_to_asset`,
  anti-slop **C5** (no raw `<svg>`/`<canvas>`/`<script>` in `body_html`), and a "Known limits" section
  in `SKILL.md` (SVG-as-asset, animations → Lottie/MP4, `render_motion_video` Chromium fallback).

## [1.2.0] — 2026-06-24

Richer media authoring + screen reorder (matches scorm-mcp 1.2.0 / W9).

### Added
- `content_slide` **`blocks[]`** — interleave `paragraph → image → paragraph` in one screen
  (instead of consecutive content slides).
- **Per-item images** — `image_asset_id` on accordion/tabs items and timeline events;
  `front_asset_id` / `back_asset_id` on flashcard faces.
- **Inline assets** — `{{asset:<id>}}` interpolation in any `*_html` (embed a packaged asset in
  flowing text) and inline base64 `data:` URI `<img>`.
- **`reorder_screens`** tool documented (set an explicit screen order; `add_screen` appends).
- `references/mcp-cookbook.md` + `references/screen-types.md` updated for all of the above.

## [1.1.0] — 2026-06-15

Composable game engine + adaptive learning + telemetry guidance (matches scorm-mcp 1.1.0).

### Added
- Decision guides for the **2 new screen types** — `game` (composable serious game: mechanic primitives
  + `when event then action` rules + branching nodes; case_sim / escape_room) and `adaptive_practice`
  (Elo / Bayesian Knowledge Tracing → difficulty calibration). 26 → **28 screen types**.
- `references/interactivity-and-gamification.md` — composable game engine, adaptive practice (Elo vs BKT),
  and optional **xAPI / cmi5** telemetry sections.
- `references/mcp-cookbook.md` — `lint_course` (anti-slop quality gate) and `export_qti` (QTI 2.1 export)
  tools + copy-ready `game` / `adaptive_practice` spec shapes.
- `references/pre-flight.md` — mandatory `lint_course` `clean: true` gate before shipping game/adaptive courses.

## [1.0.0] — 2026-06-11

First stable release.

### Added
- **Anti-slop discipline** — a one-line Training Read (Bölüm 0), parametric dials
  (INTERACTIVITY/COGNITIVE_DENSITY/TONE/VISUAL_RICHNESS), `references/anti-slop.md` (binary bans with
  override paths + before/after JSON), and a mechanical `references/pre-flight.md` gate.
- Decision guides for **all 26 screen types** (games, customized results, visuals) + the MCP cookbook
  shapes, including the gamification HUD (`levels`/`lives_var`) authoring.
- **Topic→theme mapping** in `references/themes.md` — pick a subject-fitting visual identity (editorial,
  playground, clinical-calm…) so the interface differs by topic instead of looking uniform.
- Game-design patterns + scoring guidance (`references/` + the server's `docs/GAME-PATTERNS.md`).

## [Unreleased]

### Added
- Initial public release of the authoring-scorm-courses Claude Agent Skill.
- SKILL.md workflow + quality bar; references for instructional design, screen types, assessment,
  interactivity/gamification, media (cross-MCP + Piper TTS + local helper), programmatic video,
  themes, an authoring decision guide, and an MCP cookbook.
- Copy-and-adapt templates and a complete example course spec.
