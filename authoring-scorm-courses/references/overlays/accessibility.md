---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — w3.org/TR/WCAG22 + wcag22aa.org kriter sayfaları):
# W3C (2023). Web Content Accessibility Guidelines (WCAG) 2.2 — W3C Recommendation,
# 5 Ekim 2023. Bu dosyanın dayandığı kriterler doğrulandı: 1.1.1 Non-text Content (A),
# 1.2.2 Captions (A), 1.4.3 Contrast (AA), 2.1.1 Keyboard (A), 2.2.1 Timing Adjustable (A),
# 2.5.7 Dragging Movements (AA — 2.2'nin yeni kriteri: sürükleme için tek-işaretçi alternatif
# zorunlu). Platform tabanının dürüst durumu: kemalyy/edumints-scorm-mcp
# docs/ACCESSIBILITY-CONFORMANCE.md (WCAG 2.2 AA KISMİ uygunluk beyanı — ekran tipi başına
# matris + bilinen sınırlar; bu kaplama o beyanın ÜSTÜNE yazım-zamanı kararları ekler).
overlay: accessibility
name: "Erişilebilirlik (WCAG 2.2 AA)"
version: 1
decision_points: [ekran_secimi, medya, dil_ton]
conflicts:
  - with: udl
    decision_point: ekran_secimi
    rule: "Sınır bildirimi: udl pedagojik seçenek çeşitliliği ekler, bu kaplama teknik uyumu
           denetler; aynı kararda çelişirlerse teknik uyum önceliklidir — erişilemeyen seçenek
           çeşitlilik sayılmaz (udl kendi tarafından aynı sınırı bildirir)."
  - with: arcs
    decision_point: ekran_secimi
    rule: "Dikkat/akıcılık gerekçesiyle süre baskılı tip önerilirse: yalnız uzatılabilir VE
           kapatılabilir zamanlayıcı taşıyan bileşim meşrudur (WCAG 2.2.1); aksi hâlde süresiz
           eşdeğer tip seçilir — motivasyon tasarımı zaman sınırını gerekçelendiremez."
---

# accessibility — Erişilebilirlik (D6)

**Ne:** Platform tabanı (oynatıcı odak yönetimi, ARIA canlı bölgeler, RTL, `prefers-reduced-motion`
desteği, oyun zamanlayıcı doğrulayıcısı, `lint_course` alt-metin uyarıları) sunucunun
`docs/ACCESSIBILITY-CONFORMANCE.md` belgesinde ekran tipi başına, koda dayanarak beyan edilmiştir
— **bu kaplama o denetimi TEKRARLAMAZ.** Kaplamanın alanı, platformun otomatik veremediği
**yazım-zamanı kararlarıdır**: hangi tip seçilir, alt metin NE söyler, süre baskısı ne zaman
meşrudur, dil hangi düzeyde yazılır. Hedef: WCAG 2.2 AA (W3C Recommendation, 5 Ekim 2023) —
platformun KISMİ uygunluk beyanının üstünde sahte vaat kurmadan. **Ne zaman:** her kursta
değerlendirilebilir; kamu/kurumsal zorunlu eğitimde ve bilinen engelli kullanıcı kitlesinde seçim
gerekçesi kendiliğinden güçlüdür.

## Karar noktası kuralları

### `ekran_secimi` — klavye erişimi ve süre baskısı (belgeli sınırlara karşı seçim)

Sunucu uygunluk matrisinin bilinen sınırları yazım kararına şöyle çevrilir:

- **`drag_drop` işaretçi-bağımlıdır** (klavye alternatifi YOK — 2.1.1 ve 2.5.7'ye belgeli
  aykırılık). Karar: klavye erişimi gereken her bağlamda aynı görev `matching` (seçim-kutulu)
  ya da `sorting` (▲/▼ düğmeli) olarak yazılır — bu, belgenin kendi önerdiği tek dürüst
  çözümdür. `drag_drop` ancak aynı beceriyi ölçen klavye-erişilebilir eşdeğer madde kursta
  ayrıca varsa kullanılır.
- **`term_match_race` geri sayımı uzatılamaz/kapatılamaz** (2.2.1'e belgeli aykırılık —
  süre dolunca kendiliğinden puanlar). Karar: süre baskısı ancak hedef fiili AKICILIK ise ve
  öğrenen denetimli zamanlayıcıyla kurulabiliyorsa meşrudur → süreli mekanik gerekiyorsa `game`
  bileşimi seçilir: `timer` ilkeli, `allow_extend: true` ve/veya `allow_disable: true` —
  doğrulayıcı ikisi birden kapalıysa build'i zaten reddeder; kaplama kararı bunu YAZIM anına
  çeker (doğrulayıcıya yakalanmak tasarım değildir).
- **Ekran-düzeyi `timer_sec` hiçbir tipte uzatılamaz** (belgeli sınır: her tipe eklenebilen
  geri sayımın öğrenen denetimi yok). Karar: `timer_sec` içerik/ölçüm ekranlarında KULLANILMAZ;
  `on_timeout`/`timeout_goto` ile içerik ya da soru kilitleme yasak karardır. Süre isteyen tek
  meşru yer yukarıdaki `game` zamanlayıcısıdır.
- **`hotspot` bölge adı `title` özniteliğine dayanır** (belgeli sınır — yardımcı teknolojide
  tutarsız). Karar: her bölgeye `label` yazılır ve bölgenin İÇERİĞİ (hangi cümle/öge olduğu)
  etikette adlandırılır; "bölge 1" etiket değildir.

### `medya` — alt metin KALİTESİ, grafik/video dürüstlüğü

`lint_course` alt metnin VARLIĞINI uyarır (`missing_alt_text` — tavsiye düzeyi); **içeriği
yazarın kararıdır** ve bu kaplamanın kuralı ikilidir:

- **Öğreten görselin alt metni kanıt taşır:** E1'in öğreten-artefakt tanımıyla aynı ölçüt —
  görsele bağlanan soru, yalnız alt metni okuyan öğrenen için de cevaplanabilir kalmalıdır.
  "Grafik", "ekran görüntüsü", "diyagram" alt metin değildir; alt metin artefaktın KRİTİK
  içeriğini betimler ("form altında önceden işaretli 'kabul ediyorum' kutusu" gibi). Dikkat:
  alt metin kanıt-DIŞI bir ekranın görselindeyse cevabı yeniden söyleyemez (K5 alt metne de
  uygulanır).
- **`data_chart` SVG'si programatik ad taşımaz** (belgeli sınır). Karar: `caption` alanı
  ZORUNLU yazılır ve grafiğin çıkarımını metinle kurar ("Gece→Sabah geçişi 20 dk bandında") —
  eksen okuyamayan kullanıcının tek güvenilir kanalı budur.
- **`video` senkron altyazı taşımaz** (belgeli sınır — `<track>`/WebVTT yok; 1.2.2). Karar:
  konuşma taşıyan video ancak içeriği `caption` + `narration_text` ile spec'te tam veriliyorsa
  kullanılır (K1 dış-medya şartıyla aynı test); veremiyorsan aynı içeriği anlatımlı ekran
  dizisine çevir. Ses anlatımı HER ZAMAN `narration_text` ile gelir — metinsiz ses yüklemek
  transkriptsiz kanal üretir (belgeli sınır), yasak karardır.
- **`lottie` `prefers-reduced-motion`'ı yok sayar ve durdurulamaz** (belgeli sınır). Karar:
  döngülü/uzun animasyon kritik içerik TAŞIYAMAZ; lottie yalnız kısa, tek-geçişli, içeriği
  başka kanalda da var olan süsleme-üstü rollerde (o rol de C4'ü geçmek zorundadır).
- **Kontrast temaya bağlıdır** (belgeli: paket temalar AA hedefli, özel temalar denetimsiz).
  Karar: özel marka teması yazarken vurgu rengi + metin çiftleri AA oranıyla seçilir; anti-slop
  C3 (keyfi koyu tema yasağı) zaten tavan — bu kaplama override koşuluna "kontrast AA ölçülerek"
  şartını hatırlatır, yeniden tanımlamaz.

### `dil_ton` — okuma düzeyi

- Kısa cümle, tek fikir; edilgen zincir yerine özne-fiil netliği. Jargon ilk geçişte tanımlanır
  (cognitive-load kaplamasının ön-eğitim kararıyla aynı hamle — iki kaplama burada uyumludur).
- Yönergeler duyuya değil işleve atıf yapar: "yeşil düğmeye bas" değil "Bildir düğmesine bas"
  (renk tek kanal olamaz — 1.4.1'in yazım karşılığı).
- Ekran başlığı içeriğin sözleşmesidir (A3 tek-çıkarım kuralı buradaki gezinme yararıyla
  birleşir: ekran menüsünden başlık okuyan kullanıcı içeriği kestirebilmeli).

## Somut ekran kararları (parametre düzeyinde)

**1) Sınıflama görevi: `drag_drop` → `matching` (klavye-erişilebilir eşdeğer):**

```jsonc
// ÖNCE (belgeli 2.1.1/2.5.7 aykırılığı): sürükle-bırak tek yol
{ "type": "drag_drop", "id": "q_kategori", "points": 20,
  "items": [ { "text_html": "Önceden işaretli kutu" } ], "targets": [ { "label": "İrade kusuru" } ] }
// SONRA — aynı sınıflama, seçim-kutulu biçim; beceri değişmedi, erişim kanalı değişti
{ "type": "matching", "id": "q_kategori", "points": 20, "evidence_screen_ids": ["artefakt_form"],
  "pairs": [ { "left_html": "Önceden işaretli kutu", "right_html": "İrade kusuru" },
             { "left_html": "Tek kutuda üç amaç",    "right_html": "Belirlilik kusuru" } ] }
```

**2) Süreli mekanik: `timer_sec` değil, öğrenen-denetimli `game` zamanlayıcısı:**

```jsonc
// YASAK karar: herhangi bir ekranda "timer_sec": 60 → uzatılamaz geri sayım (2.2.1)
// MEŞRU biçim — akıcılık hedefinde game bileşimi; uzat VE kapat denetimleri öğrenende:
{ "type": "game", "id": "akicilik_turu", "points": 20,
  "mechanics": { "timer": { "seconds": 90, "allow_extend": true, "allow_disable": true } },
  "nodes": [ /* … */ ] }
// doğrulayıcı allow_extend+allow_disable ikisi de kapalıysa build'i reddeder — karar yazımda verilir
```

**3) `data_chart` + çıkarım taşıyan caption ve kanıt-taşıyan alt metin:**

```jsonc
{ "type": "data_chart", "id": "kanit_grafik", "chart_type": "bar",
  "title": "Devir gecikmeleri geçişe göre",
  "caption": "Gece→Sabah geçişi 19–25 dk bandında; diğer iki geçiş 6 dk altında — soru bu farka bağlanıyor.",
  "data": { /* … */ } }
// caption, SVG'yi hiç 'göremeyen' kullanıcı için soruyu cevaplanabilir kılan TEK kanal (belgeli sınır)
```

## Sınırlar (bu kaplama NE YAPMAZ)

- Platform lint'ini/doğrulayıcısını tekrarlamaz: alt metin VARLIĞI, oyun zamanlayıcı kapısı,
  odak/ARIA davranışı sunucu tarafındadır — kaplama yalnız yazım-zamanı seçim ve içerik kararı
  verir; uygunluk beyanının kaynağı her zaman `docs/ACCESSIBILITY-CONFORMANCE.md`'dir.
- Pedagojik temsil çeşitliliği kurmaz (o `udl`); tema estetiği seçmez (o `themes.md` +
  anti-slop C3).
- Kursun ÜSTÜNDE uygunluk iddiası üretmez: platform beyanı KISMİdir (video altyazı, lottie,
  `timer_sec`, `drag_drop` sınırları belgeli) — kaplamanın işi bu sınırlara ÇARPMAYAN yazım
  kararları vermektir; sınıra çarpan bir tip bilinçli seçiliyorsa pre-flight'a tek cümle
  gerekçe + telafi kanalı yazılır.

## Literatür / normatif kaynaklar

- **Birincil:** W3C (2023). *Web Content Accessibility Guidelines (WCAG) 2.2.* W3C
  Recommendation, 5 Ekim 2023. https://www.w3.org/TR/WCAG22/ — kullanılan kriterler: 1.1.1,
  1.2.2, 1.4.1, 1.4.3, 2.1.1, 2.2.1, 2.5.7 (2.2'nin yeni AA kriteri: sürüklemeye tek-işaretçi
  alternatif) DOĞRULANDI.
- Platform durumu (dürüst taban): kemalyy/edumints-scorm-mcp `docs/ACCESSIBILITY-CONFORMANCE.md`
  — 29 ekran tipi × kriter matrisi, bilinen sınırlar (video altyazı yok; `narration_text`'siz
  ses transkriptsiz; `drag_drop` işaretçi-bağımlı; `term_match_race`/`timer_sec` süre denetimsiz;
  lottie hareket-azaltmaya duyarsız; `data_chart` SVG adsız) ve test metodolojisi.
