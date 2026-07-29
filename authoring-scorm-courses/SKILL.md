---
name: authoring-scorm-courses
description: Use when the user wants to create, build, or improve a SCORM-compliant training course, e-learning module, quiz, or interactive lesson with the scorm-mcp connector (your self-hosted server, e.g. http://localhost:8000/mcp). Covers instructional design, screen-type selection, assessment, theming, variables/gamification, media (TTS/ffmpeg), animation, and the build→preview→feedback→fix loop. Enforces an anti-slop discipline: a one-line Training Read (Bölüm 0), parametric dials, and a mechanical pre-flight gate.
---

# Authoring SCORM courses with scorm-mcp

You are the **author**; the scorm-mcp server is the **assembler**. You design the pedagogy and
structure; the server validates, renders, and packages a self-contained SCORM zip that runs on any LMS.
Aim for courses that rival professional e-learning authoring tools — varied, interactive, accessible,
on-brand, slide-stage with a player and timed content reveal — not generic "click-next" modules.

## Bölüm 0: EĞİTİM OKUMASI (workflow'dan ÖNCE — en yüksek kaldıraç)

Tasarıma başlamadan, briefi tek satırlık bir **beyana** indir:

> "Bunu şöyle okuyorum: **\<kitle\>** için **\<hedef davranış\>** kazandıran, **\<ton\>** dilinde,
> **\<X dk\>** mikroöğrenme; baskın mod **\<keşif | gösterim | uygulama | değerlendirme\>**."

(`gösterim` v2.1'de eklendi: çözümlü örnek / adım-adım gösterme ağırlıklı kurslar artık
adlandırılabilir — "uygulama"ya sıkıştırılmaz.)

Brief belirsizse **TEK** soru sor (yalnız en kritik eksik), varsayma. Çıkarabiliyorsan sorma — beyan
et ve devam et. Bu beyan dial'ları (aşağı) ve tüm ekran kararlarını yönlendirir; pre-flight Madde 0
bunu sorar.

### Anti-Default Disiplini
SCORM'da modelin default reach ettiği kalıplar **slop**'tur. İsimlerini bil ve **bilinçli olarak
gitme** (somut yasaklar + ÖNCE/SONRA: `references/anti-slop.md`):
- Üst üste `content_slide` + madde-işareti duvarı (tek-fikir/ekran değil).
- "Hoş geldiniz, bu kursta şunları öğreneceksiniz" müfredat açılışı.
- Ekran metnini birebir okuyan `narration_text`.
- "Doğru!"/"Yanlış" tek-kelime (şema varsayılanı) feedback.
- Klişe stok görsel (el sıkışma, ampul, dişli), keyfi koyu tema, tek animasyonun tekrarı.
- Rozet / liderlik tablosu / "+10 puan!" patlaması.

**Bir ekran üretmeden önce** `anti-slop.md`'yi oku; teslimden önce `pre-flight.md`'yi çalıştır.

## DIALS — parametrik ayar (Eğitim Okuması override etmedikçe baseline)

Briefi dört **sunum kadranına** (1–10) eşle. Bu adlar **sabittir** (cross-reference için;
geriye-uyumluluk: v1'deki dört ad ve anlam değişmedi — v2.1 yalnız bunları "sunum kadranı"
olarak sınıflandırdı, çünkü sunumu modüle ederler, yöntemi SEÇMEZLER):

| Dial | 1 (düşük) | 10 (yüksek) |
|---|---|---|
| `INTERACTIVITY` | pasif okuma, seyrek yoklama | her ekranda challenge/simülasyon |
| `COGNITIVE_DENSITY` | tek fikir/ekran, havadar | yoğun referans, çok bilgi/ekran |
| `TONE` | resmi kurumsal CPD | oyunlaştırılmış, samimi/çocuk |
| `VISUAL_RICHNESS` | metin-ağırlıklı, tipografi | video/animasyon-ağırlıklı |

**Kitleye göre baseline preset** (Eğitim Okuması farklı söylemedikçe bunu kullan):

| Kitle | INTERACTIVITY | COGNITIVE_DENSITY | TONE | VISUAL_RICHNESS |
|---|---|---|---|---|
| Çocuk (7–9 yaş) | 8 | 2 | 8 | 8 |
| Üniversite öğrencisi | 6 | 6 | 4 | 5 |
| Sağlık-profesyoneli CPD | 5 | 7 | 2 | 4 |
| Kurumsal zorunlu eğitim | 6 | 4 | 3 | 5 |

Dial → karar (örnek eşleme):
- **INTERACTIVITY** yüksek → İzle→Uygula→Sıra Sizde + ~her içerik ekranında bir etkileşim; düşük →
  ~3 ekranda 1 yoklama. (Yine de anti-slop A1 tavanı geçerli: ardışık `content_slide` ≤ 2.)
- **COGNITIVE_DENSITY** düşük → `reveal:"click"`, ekran başına 1–2 fikir, çok ekran; yüksek →
  accordion/tabs ile katmanla. (A2 ≤ 4 madde yine geçerli.)
- **TONE** düşük → düz başlık, ölçülü anlatım; yüksek → soru-başlık, oyun mekaniği. (D1
  patronlaştırıcı oyunlaştırma her tonda yasak.)
- **VISUAL_RICHNESS** yüksek → video/lottie/`render_motion_video`; düşük → tipografi-güçlü stage,
  gerçek ekran görüntüsü. (C4 öğretmeyen medya yine yasak.)

Dial'lar anti-slop'u **gevşetmez** — yalnız izin verilen aralık içinde tonu ayarlar. Seçtiğin
değerleri pre-flight Madde 1'de gerekçele.

### YÖNTEM kadranı: `PRIOR_KNOWLEDGE` (1–10) — sunum kadranı DEĞİL

Bu kadran ayrı düzlemdedir: sunumu değil, **Katman 0 yöntem seçimini** besler
(`references/core/method-selector.md`). "Ton ayarı" sanma — yanlış PK değeri yanlış YÖNTEM seçer.

| Kadran | 1 (düşük) | 10 (yüksek) |
|---|---|---|
| `PRIOR_KNOWLEDGE` | konuyu ilk kez görüyor; tam gösterim + çözümlü örnek olmadan ilerleyemez | alanında akıcı; gösterim fazlası zaman çalar ve öğrenmeyi DÜŞÜRÜR (uzmanlık-tersinme) |

Kadran → seçici etkisi (uzmanlık-tersinme etkisi):

| PK | Seçiciye etkisi |
|---|---|
| Düşük (1–3) | Gösterim derinliği ve çözümlü-örnek dozu YÜKSEK; gösterim/kılavuzlu-uygulama paketleri öne; problem-önce paketler aralık dışı kalıp elenir. |
| Orta (4–6) | Gösterim kısalır: tam çözümlü örnek yerine tamamlama/soluk-örnek; keşif paketleri güvenli hata-maliyetinde seçilebilir olur. |
| Yüksek (7–10) | Çözümlü örnek dozu DÜŞER, problem-önce yaklaşımlar öne geçer; gereksiz gösterim zarar sayılır (`expertise-adaptive` kaplamasını değerlendir). |

**Çapraz referans — sunum kadranlarıyla çelişki taraması (v2.1):**
- `INTERACTIVITY` ile çelişmez: o etkileşim SIKLIĞINI ayarlar; PK etkileşimin TÜRÜNÜ
  (gösterim mi, deneme mi) yöntem seçimi üzerinden belirler.
- `COGNITIVE_DENSITY` ile çelişmez ama bağlaşıktır: **düşük PK + yüksek DENSITY tehlikeli
  kombinasyondur** — pre-flight Madde 1'de ayrıca gerekçe ister.
- `TONE` / `VISUAL_RICHNESS` ile dik eksenler: etkileşim yok.
- Kitle-baseline preset tablosu PK **içermez** (bilinçli): PK kitleden değil kitle×konudan
  çıkar — sessizce varsayılamaz; bilinmiyorsa 3 varsay ve beyan et (`method-selector.md`).

## Workflow

1. **Clarify** (briefly): audience, one measurable learning objective, duration (target microlearning:
   3–8 min), source material, SCORM target (1.2 vs 2004 — use **2004** for branching/variables/games).
2. **Yöntemi seç (Katman 0), sonra outline'ı tasarla.** Önce seçiciyi çalıştır
   (`references/core/method-selector.md`): kazanım türü (7 tür) + PRIOR_KNOWLEDGE + hata maliyeti +
   zaman/platform/bağlam → paket(ler) (`references/pedagogy/`) + kaplama(lar) (`references/overlays/`).
   Sert kısıt elemesinden geçenler arasından gerekçeyle seç ve **YÖNTEM BEYANI**'nı kaydet
   (pre-flight Madde 1b). Sonra outline: map objective → chunks → practice → assessment → summary.
   Pick screen types deliberately (see `references/screen-types.md`). Vary them — avoid repetition
   (template fatigue is the #1 learner complaint).
3. **Theme**: arayüz **konuya göre farklılaşsın** — her kursu aynı varsayılana düşürme. Eğitim Okuması'ndaki
   kitle/tona göre konu-uygun bir görsel kimlik seç (çocuk → `playground`, beşeri/akademik → `editorial`,
   sağlık → `clinical-calm`, kurumsal → marka/`default`); gerekirse vurgu rengini markayla override et.
   Tema = renk + başlık fontu + radii + desen + `custom_css`. Açık/nötr/AA standardı; keyfi koyu tema yok.
   **Konu→tema eşlemesi ve kaldıraçlar: `references/themes.md`.**
4. **Build** with `build_from_spec` (one JSON, token-efficient, preferred). See `references/mcp-cookbook.md`.
5. **Preview → review → fix loop**: call `preview`, share the hosted URL. The reviewer leaves comments on
   screens; you read them with `list_feedback` (no args = all pending across projects), apply edits, then
   `resolve_feedback`. Re-preview. See `references/mcp-cookbook.md`.
6. **Validate & package**: `validate_package` then `build_package` → download URL for the LMS.

## Quality gate (teslimden önce ZORUNLU)
Kısa bir checklist değil — **mekanik denetim matrisi** çalıştır: `references/pre-flight.md`. Bir kutu
bile dürüstçe işaretlenemiyorsa kurs teslime hazır DEĞİL. Matris niyet (Eğitim Okuması + dial gerekçesi),
anti-slop sayımı (`references/anti-slop.md`) ve mekanik/teslim adımlarını sayılabilir biçimde kapsar.

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
- `references/anti-slop.md` — **ÖNCE BUNU OKU.** SCORM slop'unun somut/ikili yasakları + override yolları + ÖNCE/SONRA JSON. Her ekran üretmeden önce buna karşı denetle.
- `references/pre-flight.md` — teslim öncesi **zorunlu** mekanik denetim matrisi (sayılabilir). Quality gate burada.
- `references/core/method-selector.md` — **Katman 0 seçici:** kazanım türü + PRIOR_KNOWLEDGE + hata maliyeti → paket(ler) + kaplama(lar); sert-kısıt elemesi + gerekçeli seçim + YÖNTEM BEYANI çıktı biçimi. Outline'dan ÖNCE çalıştır.
- `references/core/evidence-binding.md` — **Katman 1 çekirdeği (yöntemden bağımsız):** skorlanan her soru kurs-içi kanıt kaynağına bağlanır (K1–K3); denetim sorusu + "bağla ya da at" prosedürü. Skorlanan soru içeren HER kursta oku.
- `references/core/alignment.md` — **Katman 1:** hedef–ölçme hizası (H1–H3): hedef→soru→kanıt eşleme tablosu + "skorlanan > hedef + 1" uyarı eşiği.
- `references/core/feedback-anatomy.md` — **Katman 1 tabanı:** gerekçeli geri bildirimin 3 zorunlu öğesi (G1–G3): neden doğru + neden yanlış + kanıta geri işaret.
- `references/core/scoring-timing.md` — **Katman 1:** formatif/summatif ayrımı (Z1–Z3): "kanıt kaynağı üretilmeden skor yok" + skorsuz erken-deneme istisnası.
- `references/pedagogy/_SCHEMA.md` — **Katman 3 paket sözleşmesi:** her yöntem paketinin ön-madde şeması (`pack-frontmatter.schema.json`); `evidence_phase(s)` ZORUNLU, kanıt beyanı çoğul olabilir; döngü/koşul ifade edilebilir; doğrulama komutu belgeli.
- `references/overlays/_FRAMEWORK.md` — **Katman 2 kaplama çerçevesi:** 6 kaplama (cognitive-load, udl, arcs, expertise-adaptive, assessment-alignment, accessibility) + "sıra dayatan = paket, sırasız değiştiren = kaplama" ayracı + paket-bağımsızlık kuralı + çakışma bildirim biçimi.
- `references/eval/blind-test.md` — **kör test protokolü:** kanıt kaynakları çıkarılınca skorlanan sorular hâlâ cevaplanabiliyor mu? Geçme eşiği ≥ 1/2 + sonuç kayıt şablonu + pilot koşu.
- `references/visual-storytelling.md` — **sıradanlık panzehiri:** anlatı ipliği (tek sahne), ekran-başına görsel bütçesi, "oku değil BUL" dönüşümleri (simulation/image_compare/timeline), gerçekçi artefakt mockup SVG reçetesi, stat-kartı deseni, `search_images` → `add_asset` akışı.
- `references/authoring-recommendations.md` — **karar rehberi: ne zaman/nasıl/neden.** Stage/timeline modu, narration yazımı, reveal seçimi, pedagojik ritim.
- `references/mcp-cookbook.md` — exact tool calls, full build_from_spec shape (all 28 screen types) + game/adaptive shapes, `content_slide` `blocks[]` inline multi-image, per-item visuals (accordion/tabs/flashcards/timeline), `reorder_screens`, `auto_tts`, `add_asset` (callable directly, may not surface in tool-search), `lint_course`/`export_qti` + the feedback loop.
- `references/course-patterns.md` — proven course structures to build (tool training, concept lesson, gamified, branching).
- `references/instructional-design.md` — objectives, structure, microlearning, anti-template-fatigue.
- `references/screen-types.md` — decision guide for all 28 screen types (incl. simulation, decision_scenario, **composable game**, **adaptive practice**).
- `references/assessment.md` — question/feedback/scoring design.
- `references/interactivity-and-gamification.md` — variables, conditions, timer, points, branching, **composable game engine** (game), **adaptive practice** (Elo/BKT), **xAPI/cmi5** telemetry.
- `references/media.md` — TTS/image/video ingestion + ffmpeg + Lottie, **Canva cross-MCP pipeline** (generate → export → `add_asset` → asset id).
- `references/video-generation.md` — programatik video (VideoSpec → HyperFrames MP4): motion-graphic, veri-viz, slayt→video.
- `references/themes.md` — preset themes + customization.

## Known limits (Claude → SCORM pipeline)
- **No raw `<svg>`/`<canvas>`/`<script>` in `body_html`** — the sanitizer strips them. Diagrams go
  through the asset pipeline: `svg_to_asset` (preferred) or `add_asset` → `media_asset_id`/`image_asset_id`/
  block `asset_id` (rendered as `<img>`). See `references/media.md` → "SVG diagrams".
- **Animations** — canvas/JS animations don't survive packaging. Use a **Lottie** asset or an **MP4**
  (`render_motion_video` / `make_video_from_image_audio`).
- **`render_motion_video`** — needs Chromium on the server; if absent it returns `render_unavailable`.
  Fallbacks: `make_video_from_image_audio` (PNG+TTS→MP4), a static SVG/PNG asset, or local render.

## Templates & examples (copy and adapt)
One minimal template per first-wave method pack (C1–C4). Each buildable template passes the server
lint clean (0 errors, 0 warns, `evidence_binding_coverage` 1.0) — keep that invariant when adapting.
- `templates/rosenshine-di.json` — C1 Direct Instruction micro-course (successor of the old
  `tool-training.json` Pattern A: the Watch→Apply→Your-Turn steps are mapped to pack phases in the
  file's `_pattern_a_eslemesi` table; guided practice is now unscored, scored questions carry
  `evidence_screen_ids`).
- `templates/merrill-fpi.json` — C2 task-centered micro-course (successor of the old
  `concept-lesson.json` Pattern B — see `_pattern_b_eslemesi`; chosen over 5E because 5E's
  `exploration` platform requirement isn't shipped yet).
- `templates/5e-inquiry.json` — C3 5E inquiry cycle, **`_draft: true`**: uses the `exploration`
  screen type (F2) which the server doesn't ship yet; build_from_spec rejects it until then.
- `templates/4cid.json` — C4 4C/ID complex-skill training, **`_draft: true`**: uses the
  `worked_example` screen type (F1); same gate.
- `examples/example-cybersecurity-course.json` — a complete, high-quality build_from_spec to study and adapt.
