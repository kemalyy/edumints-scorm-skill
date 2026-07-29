# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Changed — v2.1 Paket şablonları (Wave 4b: F3, #20)
- **`templates/` yeniden yazıldı: paket başına bir minimal şablon (C1–C4).** Her şablon
  YÖNTEM BEYANI (`_yontem_beyani`, method-selector çıktı biçimi) + faz açıklamalı ekranlar
  (`_phase`) + tek kazanımlı gerçekçi mikrokurs içerir; skorlu her soru ÇOĞUL
  `evidence_screen_ids` ile kanıt ekranlarına bağlı, geri bildirimler G1–G3 uyumlu (salt
  onay/ret grep 0). İnşa edilebilir şablonlar gerçek sunucu lint'inden doğrulandı
  (build_from_spec + lint_course): **rosenshine-di, merrill-fpi, 5e-inquiry üçü de 0 error ·
  0 warn · `evidence_binding_coverage` 1.0.** Şablonlar kendi başına build edilebilsin diye
  `assets[]` PLACEHOLDER veri-URI'leri taşır (gerçek varlıkla değiştirilir).
- **`templates/rosenshine-di.json`** — `tool-training.json`ın (Pattern A İzle→Uygula→Sıra
  Sende) paket eşlemesi: dosya EŞLENDİ, atılmadı (`_pattern_a_eslemesi` eski-adım→faz
  tablosu). Denetim düzeltmeleri: İzle'nin boş dış-varlık slotu kanıt taşıyan caption'a
  dönüştü (K1 dış-medya şartı); Uygula'nın 20 puanı kaldırıldı (rehberli pratik skorsuz, Z3);
  B3-ihlali salt-onay/salt-ret feedback'i gerekçeli üçlüyle değiştirildi; skorlu soru
  `evidence_screen_ids: [izle, model]`.
- **`templates/merrill-fpi.json`** — `concept-lesson.json`ın (Pattern B) kanıt-bağlı halefi
  (`_pattern_b_eslemesi`): iddia+pasif-tur zinciri (tanım→tabs→flashcards→"*"-kabullü
  fill_blank) görev-merkezli döngüye taşındı — gerçek görev (rıza metni değerlendirme) +
  karşılaştırmalı gösterim (kanıt) + skorsuz destekli deneme + kanıta bağlı skorlu ölçüm +
  skorsuz bütünleştirme.
- **`templates/5e-inquiry.json`** — C3 şablonu, tahminini-kilitle keşif mekaniğiyle BUGÜN
  inşa edilebilir: kesfet = skorsuz mcq (feedback ders anlatmaz, yalnız deney sonucunu açıklar)
  + data_chart deney verisi; skorlu soru üç kanıt ekranına birden çoğul bağlı
  (kesfet×2 + acikla).
- **`templates/4cid.json`** — C4 şablonu `_draft: true`: `worked_example` (F1) ekran tipi
  sunucuda henüz yok; taklit ekran tipiyle sahte build yerine taslak beyanı
  (`_draft_reason` + F1 sonrası yükseltme adımları). build_from_spec taslağı bilinçli reddeder.
- **SKILL.md** — "Templates & examples" bölümü 4 paket şablonuna güncellendi (lint-temiz
  invariantı + eski şablonların halefiyet notu).

### Added — v2.1 İlk dalga yöntem paketleri (Wave 4a: C1–C4)
- **`references/pedagogy/rosenshine-di.md`** (#16) — C1 Doğrudan Öğretim paketi: günlük tekrar →
  küçük adımlar + model/çözümlü örnek (`evidence_phase: sunum_model`) → rehberli pratik (skorsuz,
  yüksek soru yoğunluğu) → bağımsız pratik (skorlu). Uzmanlık-tersinme "ne zaman seçilmemeli"
  bölümü; `conflicts_with: [5e-inquiry, productive-failure]` (aynı kazanımda keşif-önce ↔
  model-önce zıtlığı); Pattern A (İzle→Uygula→Sıra Sende) eşleme beyanı (şablon işi #20'de);
  uçtan uca build_from_spec örneği (pediatrik doz hesabı; skorlu soru `evidence_screen_ids` ile
  kanıt ekranına bağlı — scorm-mcp CONTRACTS §1.3 E1). Kaynak: Rosenshine (2012), American
  Educator 36(1) — doğrulandı.
- **`references/pedagogy/merrill-fpi.md`** (#17) — C2 Merrill İlk İlkeler (görev-merkezli):
  gerçek görev tanıtımı → etkinleştirme (bilinçli olarak kanıt fazı DEĞİL — K2 gerekçesi gövdede)
  → gösterim (`evidence_phase: gosterim` — gösterimsiz kurs yapısal olarak üretilemez) →
  destekli uygulama (skorsuz) → bağımsız uygulama (skorlu) → bütünleştirme (skorsuz yansıtma).
  "Görev tanımlanamıyorsa paket seçilemez" kuralı; 4cid ile ölçek-farkı seçici notu (çakışma
  değil); `conflicts_with: []`. build_from_spec örneği: hata (bug) raporu yazma görevi. Kaynak:
  Merrill (2002), ETR&D 50(3), 43–59 — doğrulandı. Dosya adı seçici kimliğiyle hizalı
  (`merrill-fpi`; şema kuralı: dosya adı == pack).
- **`references/pedagogy/5e-inquiry.md`** (#18) — C3 5E Sorgulama Döngüsü: merak (Engage) →
  kesfet (Explore, skorsuz keşif) → acikla (Explain, keşif çıktısına atıflı kanonik açıklama) →
  derinlestir (Elaborate, skorsuz transfer) → degerlendir (Evaluate, skorlu). ÇOĞUL kanıt beyanı
  `evidence_phases: [kesfet, acikla]`; `requires_platform: [exploration]` (F2 — öğrenen girdisini
  saklayıp geri oynatma; yetenek yoksa seçici paketi ELER, kâğıt-üstü 5E üretilmez). "Ne zaman
  seçilmemeli": yüksek hata maliyeti (sert kısıt dışı), PK<3 (uzmanlık-tersinmenin acemi ucu —
  Kirschner/Sweller/Clark 2006 atfı), dar bütçe; `conflicts_with: [rosenshine-di]`
  (productive-failure bilinçli listede değil — aynı deneme-önce ailesi). build_from_spec örneği:
  yoğunluk kavramı; skorlu soru iki kanıt fazına birden çoğul bağlı. Kaynak: Bybee vd. (2006),
  The BSCS 5E Instructional Model — doğrulandı.
- **`references/pedagogy/4cid.md`** (#19) — C4 4C/ID Karmaşık Beceri Eğitimi: görev sınıfları
  basit→karmaşık TAM görevler; gorev_tam_destek (çözümlü örnek + destekleyici bilgi) →
  gorev_soluklastirma (tamamlama problemleri; `sonraki`/`tekrar_kosulu` döngüsüyle destek 0'a
  inene dek) → gorev_bagimsiz (skorlu). ÇOĞUL kanıt: `evidence_phases: [gorev_tam_destek,
  gorev_soluklastirma]`; `requires_platform: [worked_example]` (F1 — soluklaştırma düzeyleri).
  Dört bileşenin fazlara yerleşim haritası (bileşen ≠ faz); "ne zaman seçilmemeli": tekil
  olgu/kavram, tek-yollu kısa prosedür (rosenshine-di alternatifi — çakışma değil), kısa kurs,
  yüksek PK; `conflicts_with: []`. build_from_spec örneği: SQL yönetici raporu, 3 görev sınıfı;
  skorlu soru iki kanıt fazına çoğul bağlı. Kaynak: van Merriënboer & Kirschner (2018), Ten
  Steps to Complex Learning (3. baskı) — doğrulandı.

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
- **`PRIOR_KNOWLEDGE` yöntem kadranı** (#13) — SKILL.md'de 1–10 ölçek + uç değer betimleri;
  sunum kadranlarından AYRI düzlemde (Katman 0 seçici girdisi, "ton ayarı" değil); 3 satırlık
  kadran→seçici etki tablosu (uzmanlık-tersinme: yüksek PK'da çözümlü örnek dozu düşer,
  problem-önce öne geçer) + dört sunum kadranıyla çelişki taraması (çapraz referans bölümü).
- **Eğitim Okuması baskın-mod enum'una `gösterim`** (#13) — keşif | gösterim | uygulama |
  değerlendirme; gösterim-ağırlıklı kurslar artık adlandırılabilir.
- **`references/pedagogy/` paket sözleşmesi** (#14) — `pack-frontmatter.schema.json` (JSON Schema,
  Türkçe alan açıklamalı) + `_SCHEMA.md` sözleşme belgesi: `pack`, `name`, `outcome_types`,
  `prior_knowledge` (aralık), `error_cost`, `requires_platform`, `phases` (amaç + izinli ekran
  tipleri + skorlanabilir; `sonraki`/`tekrar_kosulu` ile döngü-koşul), **`evidence_phase` VEYA
  `evidence_phases` ZORUNLU** (kanıt üreten faz — çoğul serbest, 1:1 dayatması yok; soru-düzeyi
  bağ zaten çoğul: `evidence_screen_ids`, scorm-mcp CONTRACTS §1.3 E1 ile terminoloji-uyumlu),
  `scoring_allowed_from` (Z2'nin paket-düzeyi beyanı), `conflicts_with`. Doğrulama:
  `scripts/validate_packs.py` (şema + bütünlük denetimleri; CI'da çalışır) + 2 çalışan örnek stub
  (`_STUB-dogrusal.md` doğrusal, `_STUB-dongulu.md` döngülü).

- **`references/overlays/_FRAMEWORK.md`** (#15) — Katman 2 kaplama çerçevesi: "sıra dayatan =
  paket, sırasız değiştiren = kaplama" ayracı (mastery-learning sınır örneğiyle); 6 kaplamanın
  (cognitive-load, udl, arcs, expertise-adaptive, assessment-alignment, accessibility) listesi +
  her birinin kapsam SINIRI; kaplama dosya biçimi (`decision_points` beyanı + 8 karar-noktası
  sözlüğü); **paket-bağımsızlık kuralı** (kaplama metninde paket faz adı = 0 — mekanik:
  `scripts/check_overlay_independence.py`, CI'da grep-0 kapısı); çakışma bildirim biçimi
  (`with` + `decision_point` + `rule`) ve productive-failure örneği.

### Changed — v2.1 Katman 0 seçici + paket şeması
- SKILL.md dört mevcut kadranı **"sunum kadranı"** olarak sınıflandırdı (geriye-uyumluluk notu:
  v1 adları ve anlamları sabit); pre-flight Madde 1 PRIOR_KNOWLEDGE beyanını da sorar.

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
