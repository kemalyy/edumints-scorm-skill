---
# Birincil kaynak (DOĞRULANDI, 2026-07-29 — aft.org/ae/spring2012/rosenshine):
# Rosenshine, B. (2012). "Principles of Instruction: Research-Based Strategies That All
# Teachers Should Know." American Educator, 36(1), 12–19. — 10 ilke: (1) günlük gözden
# geçirme, (2) küçük adımlarla yeni malzeme, (3) soru sorma, (4) model sunma, (5) rehberli
# pratik, (6) anlama kontrolü, (7) yüksek başarı oranı, (8) zor görevlere iskele,
# (9) bağımsız pratik, (10) haftalık/aylık gözden geçirme.
pack: rosenshine-di
name: "Doğrudan Öğretim (Rosenshine)"
version: 1
outcome_types: [olgu, kavram, prosedür]
prior_knowledge: [1, 5]
error_cost: [düşük, orta, yüksek]
requires_platform: []
phases:
  - id: gunluk_tekrar
    amac: "Önceki öğrenme skorsuz geri-getirmeyle ısıtılır; yeni malzemenin bağlanacağı zemin açılır (İlke 1)."
    izinli_ekran_tipleri: [flashcards, mcq, true_false, fill_blank, adaptive_practice]
    skorlanabilir: false
  - id: sunum_model
    amac: "Yeni malzeme küçük adımlarla sunulur ve model/çözümlü örnekle GÖSTERİLİR (İlke 2+4) — kursun kanıt kaynağı burada üretilir."
    izinli_ekran_tipleri: [content_slide, video, timeline, accordion, tabs, image_compare, data_chart]
    skorlanabilir: false
  - id: rehberli_pratik
    amac: "Yüksek soru yoğunluğuyla deneme-güvenli pratik: anlama kontrol edilir, yanlış anlama skor cezasız düzeltilir (İlke 3+5+6+8)."
    izinli_ekran_tipleri: [mcq, true_false, fill_blank, drag_drop, matching, sorting, hotspot, labeled_diagram, simulation]
    skorlanabilir: false
  - id: bagimsiz_pratik
    amac: "İskele çekilir; sunum_model kanıtına bağlı skorlu ölçüm ve bağımsız uygulama (İlke 7+9)."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phase: sunum_model
scoring_allowed_from: bagimsiz_pratik
conflicts_with: [5e-inquiry, productive-failure]
---

# rosenshine-di — Doğrudan Öğretim (C1)

**Ne:** Model-önce yöntem. Yeni malzeme küçük adımlarla, çözümlü örnek/model üzerinden
gösterilir; öğrenen önce yoğun rehberli pratikle (skorsuz) çalışır, iskele adım adım çekilir,
skor ancak bağımsız pratikte girer. **Ne zaman:** düşük önbilgili kitle (PK ≤ 5), iyi
yapılandırılmış olgu/kavram/prosedür kazanımları — özellikle sahada yanılmanın bedeli yüksekse
(keşif denemesi pahalıdır, gösterim + kılavuzlu pratik en güvenli yoldur).

**Kanıt beyanı (Katman 1 bağlantısı):** `evidence_phase: sunum_model` — skorlanan her sorunun
cevabı bu fazın çözümlü örneğinden/modelinden türetilebilir olmalı (K1 türü 1). Skorlu ekranlar
`evidence_screen_ids` (ÇOĞUL — scorm-mcp CONTRACTS §1.3 E1) ile bu fazdaki kanıt ekran(lar)ına
açıkça bağlanır.

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `gunluk_tekrar` | Önceki modülün/ön-şart bilginin skorsuz geri-getirilmesi | flashcards, mcq, true_false, fill_blank, adaptive_practice | ✗ |
| `sunum_model` | Küçük adımlar + model/çözümlü örnek — **kanıt üretimi** | content_slide, video, timeline, accordion, tabs, image_compare, data_chart | ✗ |
| `rehberli_pratik` | Yüksek soru yoğunluğu, ipucu + anında düzeltme, `points: 0` | mcq, true_false, fill_blank, drag_drop, matching, sorting, hotspot, labeled_diagram, simulation | ✗ |
| `bagimsiz_pratik` | İskelesiz, skorlu ölçüm — yüksek başarı oranı hedefiyle | hepsi | ✓ |

Faz notları:

- `gunluk_tekrar` serinin İLK modülünde atlanabilir (geri getirilecek önceki öğrenme yoktur —
  o durumda kurs `sunum_model` ile açılır); dizideki bir sonraki modülde zorunludur (İlke 1).
  İlke 10 (haftalık/aylık tekrar) tek mikrokursun değil kurs DİZİSİNİN işidir — seri
  planlıyorsan aralıklı tekrar modülü ekle (bkz. `retrieval-spaced` paketi).
- `sunum_model`'de doz kuralı: adım başına TEK yeni fikir; her adımda "neden"i göster (çözümlü
  örnek gerekçesiz ekran görüntüsü değildir). Uzun prosedürü `timeline` ya da `blocks[]`'lu
  tek `content_slide` ile böl.
- `rehberli_pratik`'te soru yoğunluğu içerik yoğunluğunu GEÇMELİ (İlke 3): model başına en az
  2–3 skorsuz yoklama. Yanlışta feedback kanıt ekranına geri işaret eder (G3).
- `bagimsiz_pratik`'e geçiş sinyali: rehberli pratikte yüksek başarı (İlke 7, ~%80). Skorlu
  soruların hepsi `evidence_screen_ids` ile `sunum_model` ekran(lar)ına bağlanır.

**Mevcut desen eşlemesi:** `references/course-patterns.md` Pattern A (İzle→Uygula→Sıra Sende)
yapısal olarak bu paketin `sunum_model` → `rehberli_pratik` → `bagimsiz_pratik` dizisine eşlenir
(şablon revizyonu #20/F3 işidir; burada yalnız eşleme beyanı).

## Bu paket NE ZAMAN seçilmemeli

- **Yüksek önbilgili kitle (PK ≥ 6):** uzmanlık-tersinme etkisi — akıcı öğrenene çözümlü örnek
  dozu zaman çalar ve öğrenmeyi DÜŞÜRÜR. `pbl-case` / problem-önce yaklaşımlar öne geçer.
- **Açık uçlu problem çözme kazanımları:** tek doğru çözüm yolu yokken "modeli izle" iskeleti
  stratejiyi ezberletir; `pbl-case` ya da (karmaşık beceri için) `4cid` seç.
- **Tutum kazanımları:** tutum gösterimle değil deneyim + yansıtma döngüsüyle değişir
  (`kolb-experiential`).
- **Kavram keşfiyle kalıcılık hedefleniyorsa** (düşük hata maliyeti + orta önbilgi):
  `5e-inquiry` / `productive-failure` daha derin işleme üretir — model-önce bu fırsatı kapatır.

## Çakışmalar (`conflicts_with`)

- `5e-inquiry` — **aynı kazanım üzerinde** birleştirilemez: keşif-önce (Explore → Explain) ile
  model-önce (sunum → pratik) sıra felsefeleri zıttır. Farklı kazanımlar için ayrı modüllere
  bölerek kullanılabilir (seçici kuralı: "kursu böl ya da tek pakete karar ver").
- `productive-failure` — kasıtlı-başarısızlık yöntemi denemeyi çözümden ÖNCE ister; doğrudan
  öğretim çözümü denemeden önce gösterir. Aynı kazanımda ikisi birden uygulanamaz.

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: prosedür · PK: 2 · hata maliyeti: yüksek): *"Vücut ağırlığına göre pediatrik
parasetamol dozunu mg/kg kuralıyla hesaplar."* Seri içi 2. modül (önceki modül: birimler).

```jsonc
{
  "title": "Pediatrik Doz Hesabı: mg/kg Kuralı",
  "description": "Doğrudan öğretim mikrokursu — rosenshine-di",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "screens": [
    { "type": "title_slide", "title": "Pediatrik Doz Hesabı", "subtitle": "6 dk · mg/kg kuralı" },

    // ── FAZ gunluk_tekrar (İlke 1 — skorsuz geri-getirme; önceki modülün birim bilgisi) ──
    { "type": "flashcards", "id": "tekrar_birim", "title": "Isınma: birimleri hatırla",
      "cards": [
        { "front_html": "<b>1 g = ? mg</b>", "back_html": "<p>1000 mg</p>" },
        { "front_html": "<b>15 mg/kg ne demek?</b>", "back_html": "<p>Her kilogram vücut ağırlığı için 15 mg ilaç</p>" } ] },

    // ── FAZ sunum_model (İlke 2+4 — KANIT KAYNAĞI: adım adım, gerekçeli çözümlü örnek) ──
    { "type": "content_slide", "id": "model_doz", "title": "Çözümlü örnek: 18 kg çocuk, 15 mg/kg",
      "blocks": [
        { "html": "<p><b>Adım 1 — kural:</b> doz = ağırlık (kg) × doz katsayısı (mg/kg). Katsayı prospektüsten alınır; parasetamol için 15 mg/kg.</p>" },
        { "html": "<p><b>Adım 2 — yerine koy:</b> 18 kg × 15 mg/kg = <b>270 mg</b>. Birimler sadeleşir: kg × mg/kg → mg. Birim sadeleşmiyorsa yanlış değer çarptın demektir.</p>" },
        { "html": "<p><b>Adım 3 — güvenlik kontrolü:</b> sonucu günlük üst sınırla karşılaştır (60 mg/kg/gün). 270 mg tek doz, 4 doz × 270 = 1080 mg &lt; 18 × 60 = 1080 mg → sınırın İÇİNDE.</p>" } ] },

    // ── FAZ rehberli_pratik (İlke 3+5+6 — yüksek soru yoğunluğu, points: 0, ipuçlu) ──
    { "type": "mcq", "id": "rehber_adim2", "title": "Kılavuzlu deneme: 12 kg çocuk", "points": 0,
      "prompt_html": "<p>12 kg çocuk için 15 mg/kg doz kaç mg? (Puan yok — dene, yanıl, gör.)</p>",
      "options": [
        { "id": "a", "text_html": "180 mg", "correct": true },
        { "id": "b", "text_html": "27 mg" },
        { "id": "c", "text_html": "1800 mg" } ],
      "feedback": {
        "correct_html": "<p>Doğru: 12 × 15 = 180 mg — çözümlü örnekteki Adım 2'nin aynısı.</p>",
        "incorrect_html": "<p>Birim sadeleşmesine bak: kg × mg/kg → mg. 'Çözümlü örnek' ekranındaki Adım 2'ye geri dön.</p>" } },
    { "type": "fill_blank", "id": "rehber_kontrol", "title": "Kılavuzlu deneme: güvenlik kontrolü", "points": 0,
      "prompt_html": "<p>Adım 3'ün amacı sonucu günlük ___ sınırla karşılaştırmaktır.</p>",
      "blanks": [ { "id": "b1", "accepted": ["üst", "ust"] } ] },

    // ── FAZ bagimsiz_pratik (İlke 9 — iskele yok, SKORLU; kanıt bağı AÇIK ve ÇOĞUL) ──
    { "type": "mcq", "id": "q_doz_bagimsiz", "title": "Skorlu: yeni vaka", "points": 50,
      "evidence_screen_ids": ["model_doz"],           // E1 — kanıt: sunum_model fazının çözümlü örneği
      "prompt_html": "<p>22 kg çocuk, 15 mg/kg. Tek doz kaç mg ve güvenlik kontrolü ne der?</p>",
      "options": [
        { "id": "a", "text_html": "330 mg; 4 doz/gün üst sınırın içinde", "correct": true },
        { "id": "b", "text_html": "330 mg; güvenlik kontrolü gerekmez" },
        { "id": "c", "text_html": "33 mg; üst sınırın içinde" } ],
      "feedback": {
        "correct_html": "<p>Doğru — 22 × 15 = 330 mg; 4 × 330 = 1320 ≤ 22 × 60 = 1320. Üç adımı da çözümlü örnekteki sırayla uyguladın.</p>",
        "incorrect_html": "<p>Adım atladın. 'Çözümlü örnek: 18 kg çocuk' ekranındaki 3 adımı sırayla uygula: kural → yerine koy → güvenlik kontrolü.</p>" } },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Örnekte denetim izi: skorlu tek ekran (`q_doz_bagimsiz`) → `evidence_screen_ids: ["model_doz"]`
→ `sunum_model` fazı = `evidence_phase` beyanı. Rehberli pratik ekranları `points: 0` (Z3,
deneme-güvenli); skor yalnız `scoring_allowed_from: bagimsiz_pratik` fazında.

## Literatür

- **Birincil:** Rosenshine, B. (2012). *Principles of Instruction: Research-Based Strategies
  That All Teachers Should Know.* American Educator, 36(1), 12–19.
  https://www.aft.org/ae/spring2012/rosenshine
- Arka plan: süreç-ürün araştırması + bilişsel yük kuramı (çözümlü örnek etkisi); uzmanlık-tersinme
  sınırı için Kalyuga vd. (2003), *The Expertise Reversal Effect*.
