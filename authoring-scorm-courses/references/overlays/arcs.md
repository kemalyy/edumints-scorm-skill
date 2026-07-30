---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — link.springer.com/article/10.1007/BF02905780 +
# ERIC EJ363865): Keller, J. M. (1987). "Development and use of the ARCS model of instructional
# design." Journal of Instructional Development, 10(3), 2–10. — Dört bileşen doğrulandı:
# Attention (dikkat), Relevance (ilgililik), Confidence (güven), Satisfaction (doyum);
# motivasyon tasarımı, öğretim tasarımı modelleriyle UYUMLU ayrı bir tasarım sürecidir (üslup
# değil yapısal karar — bu kaplamanın varlık gerekçesi). Kitap boyu işleme: Keller, J. M.
# (2010). Motivational Design for Learning and Performance: The ARCS Model Approach. Springer.
overlay: arcs
name: "ARCS Motivasyon Tasarımı (Keller)"
version: 1
decision_points: [ekran_secimi, medya, dil_ton, destek_dozu, geri_bildirim]
conflicts:
  - with: cognitive-load
    decision_point: medya
    rule: "Dikkat amaçlı öge konu-dışı yük adayıdır: yalnız kanıt taşıyan artefakt dikkat ögesi
           olabilir; iki kaplama aynı ekranda çelişirse tutarlılık (coherence) önceliklidir —
           süs-aday öge çıkarılır (cognitive-load kendi tarafından aynı kuralı bildirir)."
---

# arcs — ARCS Motivasyon Tasarımı (D3)

**Ne:** TONE kadranı bugün yalnız üslubu ayarlar; motivasyon tasarımı üslup değil **yapısal
karardır** — hangi ekranın var olacağını, neyi taşıyacağını ve nasıl sıralı-bağımsız
yerleşeceğini etkiler (Keller 1987: motivasyon tasarımı, öğretim tasarımının yanında ayrı ve
sistematik bir süreçtir). Dört bileşen: **Dikkat** (yönelimi kazan), **İlgililik** (öğrenenin
dünyasına bağla), **Güven** (başarabileceğine dair gerçek sinyal), **Doyum** (öğrendiğini
kullanma fırsatı). **Ne zaman:** tutum kazanımları (Katman 0 seçicisinin tutum eşlemesindeki
kaplama budur), gönüllü/`isteğe bağlı` eğitimler, motivasyonu düşük zorunlu kitleler.

## Karar noktası kuralları

### Dikkat → `ekran_secimi` + `medya`

Dikkat, süsle değil **bilişsel çatışmayla** kazanılır: beklenti-ihlali yapan gerçek veri, ucu
açık soru-başlık, çözülmemiş vaka. Somut biçimler: soru kuran `title_slide` başlığı; sezgiyle
çelişen tek-vuruşluk `data_chart`; "bul bakalım" `hotspot`/`image_compare` açılışı. **Sınır
(E1 öğreten-artefakt denetimiyle uyum):** dikkat ögesi bir şey öğretmiyorsa (sorunun sonradan
bağlanabileceği bir artefakt değilse) anti-slop C1/C4'e takılır — parlak stok görsel dikkat
tasarımı DEĞİLDİR; ön-maddedeki cognitive-load bildirimi bu sınırın çakışma kuralıdır.

### İlgililik → `dil_ton` + `ekran_secimi`

İlgililik, anti-slop B1'in ("müfredat açılışı yasak — relevansla aç") yapısal halidir: açılış,
öğrenenin SAHASINDA yaşanan riski/bedeli/kazancı kurar; senaryo rolleri B5 gereği somuttur
(rol + bağlam + çatışma). Hedef-değer bağı: "yapabileceksin" cümlesi, o becerinin öğrenenin
işinde neyi değiştirdiğiyle birlikte verilir — hedef bildirimi gerekçesiz bir müfredat maddesi
olarak bırakılmaz. Kitleye iki bağlam sunulabiliyorsa `branching` ile "kendi vakana en yakın
olanı seç" (ilgililiğin gezinme karşılığı; `udl` kaplamasının katılım kararıyla aynı mekanik —
iki kaplama burada uyumludur, çakışmaz).

### Güven → `destek_dozu` + `ekran_secimi`

Güven, pohpohlama değil **başarılabilirlik kanıtıdır**:

- **Erken kazanım:** kursun ilk üçte birinde en az bir DÜŞÜK zorluklu, SKORSUZ yoklama
  (`points: 0`) — öğrenen "yapabiliyorum" verisini kendi denemesinden alır; Z1 gereği bu
  deneme `passing_score`'a yazmaz.
- **Şeffaf beklenti:** süre (`subtitle: "6 dk"`), ölçme biçimi ve geçme eşiği baştan görünür;
  sonda sürpriz sınav güven tasarımının tersidir.
- **Zorluk rampası:** kolay→zor sıralı skorlu maddeler yerine `adaptive_practice` — `elo`
  kipinde motor, hedefe-en-yakın zorlukta madde seçer (akış hissi: ne bunaltır ne sıkar).
  Madde bankası ≥ 4 madde ve YAYILMIŞ `difficulty` ister; dar zorluk bandı rampayı öldürür.
- **Kontrol edilebilirlik:** yanlıştan dönüş yolu her feedback'te görünür (G1.3 kanıta geri
  işaret zaten zorunlu — güven bileşeni bu kuralın motivasyon gerekçesidir).

### Doyum → `geri_bildirim` + `ekran_secimi`

Doyum, rozet değil **kullanım fırsatıdır**: öğrenilen şeyin YENİ bir duruma uygulandığı transfer
ekranı (yeni vaka artefaktı + skorlu uygulama) + kapanışta içsel ustalaşma mesajı ("artık X'i
tek bakışta ayırt ediyorsun" — `summary` `show_score: true` ile kendi sonucunu gösterir).
Feedback tonu doyumu taşıyabilir (çabaya ve gelişime atıf) ama G1'in üç öğesi (neden doğru /
neden yanlış / kanıta işaret) pazarlıksız kalır — "harika iş!" tek başına doyum değil, B4
filler ihlalidir.

**AÇIK BEYAN — doyum ≠ dekoratif oyunlaştırma:** anti-slop D1 (rozet, konfeti, "+10 PUAN!"
patlaması, liderlik tablosu yasak) ve D2 (anlamsız puan yasak) bu kaplamanın ALTINDA aynen
geçerlidir; kaplamalar Katman 1'i gevşetemez (`overlays/_FRAMEWORK.md`). ARCS'ın doyum
bileşenini "kutlama efekti" diye okumak modeli tersine çevirir: Keller'de doyum, ödülün değil
öğrenilenin işe yaramasının fonksiyonudur. Bu kaplama oyunlaştırma mekaniği EKLEMEZ — yarışmacı
bağlam brief'ten gelirse o D1'in kendi override yoludur, ARCS gerekçe yapılamaz.

## TONE kadranıyla ilişki (üslup ≠ motivasyon yapısı)

| Karar | TONE kadranı (sunum) | arcs kaplaması (yapı) |
|---|---|---|
| Açılış | Başlığın dili: resmi ↔ samimi | Açılışın NE kurduğu: bedel/çatışma vakası (ilgililik) — her tonda |
| Anlatım | Hitap, kayıt, mizah dozu | Anlatının öğrenen sahasına bağlanması (ilgililik) |
| Sorular | Soru metninin sesi | Erken skorsuz kazanım + zorluk rampası (güven) — ekran/parametre kararı |
| Feedback | Cümle tonu | G1 üstüne çaba/gelişim atfı (doyum); üç öğe sabit |
| Kapanış | Kutlama dili ölçüsü | Transfer fırsatı + ustalaşma mesajı (doyum) — D1 yasakları sabit |

TONE 2'de de 8'de de ARCS kararları aynıdır; değişen yalnız cümlelerin kıyafetidir. Motivasyon
sorunu üslup değişikliğiyle çözülmez — yapı değişikliğiyle çözülür; tersine, TONE'u yükseltmek
ARCS uygulamadan "motivasyon eklendi" saymak v1 tekdüzeliğinin motivasyon versiyonudur.

## Somut ekran kararları (parametre düzeyinde)

**1) Dikkat + ilgililik — açılış kancası (B1/B5 uyumlu, artefakt taşıyan):**

```jsonc
{ "type": "title_slide", "title": "Bu teklif 40 saniyede kaybedildi. Nerede?", "subtitle": "7 dk",
  "body_html": "<p>Geçen çeyrek üç satış görüşmesi, teknik olarak doğru ama alıcının derdine bağlanmayan açılış yüzünden ilk dakikada koptu. Bugün o 40 saniyeyi sen kurtaracaksın.</p>",
  "narration_text": "Alıcı daha ilk cümlede 'bu benim sorunum değil' dediyse gerisini dinlemez — kopuş anını birazdan kayıttan izleyeceksin." }
// dikkat ögesi = çözülmemiş gerçek vaka (sonradan kanıt ekranına dönüşür); süs görsel YOK
```

**2) Güven — erken skorsuz kazanım + elo rampası:**

```jsonc
// ilk üçte birde: düşük zorluk, points: 0 (Z1 — geçme notuna yazmaz)
{ "type": "mcq", "id": "erken_kazanim", "title": "İlk adım: kopuş cümlesini seç (puan yok)", "points": 0,
  "prompt_html": "<p>Kayıttaki iki açılıştan hangisi alıcının derdiyle açıyor?</p>", "options": [ /* net ayrımlı iki seçenek */ ],
  "feedback": { "correct_html": "…mekanizma…", "incorrect_html": "…yanılgı + kayıt ekranına dön…" } },
// pratik: adaptive_practice elo kipi — hedefe-en-yakın zorluk (akış); yayılmış difficulty ZORUNLU
{ "type": "adaptive_practice", "id": "rampa", "mode": "elo",
  "items": [ { "difficulty": -1.5, /* … */ }, { "difficulty": -0.5 }, { "difficulty": 0.5 }, { "difficulty": 1.5 } ] }
```

**3) Doyum — transfer + ustalaşma kapanışı (D1 temiz):**

```jsonc
{ "type": "summary", "id": "kapanis", "title": "Artık açılışı alıcının derdinden kuruyorsun",
  "body_html": "<p>Bu kursta üç karardan geçtin: derdi bulmak, ilk cümleye taşımak, kanıtla sürdürmek. Yarınki ilk görüşmen bu üç kararın sahası.</p>",
  "show_score": true, "show_completion": true }
// rozet yok, konfeti yok, "+N puan" patlaması yok — skor sessiz veri, mesaj ustalaşma
```

## Sınırlar (bu kaplama NE YAPMAZ)

- Oyunlaştırma mekaniği eklemez; anti-slop D1/D2 yasakları her tonda ve her bileşende geçerli
  kalır (yukarıdaki açık beyan).
- Sıra dayatmaz: "erken kazanım ilk üçte birde" bir yerleşim kararıdır, faz sırası değil —
  hangi fazın ilk üçte biri oluşturduğu paketin işidir.
- Kanıt bağlamayı esnetmez: dikkat/doyum amaçlı hiçbir ekran, skorlu soruların cevabını kanıt
  zinciri dışında yeniden söyleyemez (K5) — kapanış ustalaşma mesajı kavram düzeyinde kalır.

## Literatür

- **Birincil:** Keller, J. M. (1987). *Development and use of the ARCS model of instructional
  design.* Journal of Instructional Development, 10(3), 2–10. https://doi.org/10.1007/BF02905780
  — dört bileşen ve "motivasyon tasarımı ayrı, uyumlu süreçtir" tezi DOĞRULANDI.
- Kitap boyu işleme: Keller, J. M. (2010). *Motivational Design for Learning and Performance:
  The ARCS Model Approach.* New York: Springer.
