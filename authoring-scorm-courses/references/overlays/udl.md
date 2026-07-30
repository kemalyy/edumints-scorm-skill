---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — udlguidelines.cast.org "About the Guidelines 3.0
# Update" + engagement/representation sayfaları): CAST (2024). Universal Design for Learning
# Guidelines version 3.0 (yayın: 30 Temmuz 2024). Üç ilke doğrulandı: Multiple Means of
# Engagement ("neden"i), Multiple Means of Representation ("ne"si), Multiple Means of Action &
# Expression ("nasıl"ı). 3.0 güncellemesi checkpoints → "considerations" adlandırması ve
# önyargı/aidiyet vurgusu ekler; üç-ilke omurgası değişmedi. Kuramsal köken: Meyer, Rose &
# Gordon (2014), Universal Design for Learning: Theory and Practice, CAST Professional Publishing.
overlay: udl
name: "Evrensel Tasarım (UDL)"
version: 1
decision_points: [ekran_secimi, medya, olcme, gezinme]
conflicts:
  - with: cognitive-load
    decision_point: medya
    rule: "İkinci temsil konu-dışı yük itirazıyla karşılaşırsa: temsil ancak AYNI kanıt
           kaynağını taşıyorsa kalır (süs temsil zaten iki kaplamada da yasak); ikisi de kanıt
           taşıyorsa ekran başına temsil sayısı 2'de tutulur ve fazlası ayrı ekrana bölünür —
           bölme kararında cognitive-load önceliklidir."
  - with: accessibility
    decision_point: ekran_secimi
    rule: "Sınır bildirimi: UDL pedagojik seçenek ÇEŞİTLİLİĞİ ekler, accessibility teknik uyumu
           denetler. Aynı kararda çelişirlerse teknik uyum önceliklidir — erişilemeyen temsil
           çeşitlilik sayılmaz (örn. klavyeyle çalışmayan tip, 'ek seçenek' diye eklenemez)."
---

# udl — Evrensel Tasarım (D2)

**Ne:** Tek temsilli kurs (yalnız metin + quiz) hem erişim hem öğrenme sorunudur — v1'in
concept-lesson bulgusu bu desenin şablonlaştığını gösterdi. UDL üç ilkeyle panzehir sunar
(CAST 3.0): **çoklu katılım** (neden öğreniyorum — bağlanma yolları), **çoklu temsil** (bilgi
hangi kiplerde sunuluyor), **çoklu eylem/ifade** (bildiğimi hangi biçimde gösterebiliyorum).
**Ne zaman:** kitle profili heterojense (dil düzeyi, duyusal tercih, önbilgi çeşitliliği) ya da
brief tek-kipli kaynaktan (düz metin politika, slayt dökümü) kurs istiyorsa.

**Kurucu kural — UDL kanıt kaynağını ÇOĞALTIR, yenisini icat etmez:** ikinci temsil AYNI kanıt
kaynağının ikinci kipidir; yeni iddia, yeni olgu, yeni cevap kanalı EKLEMEZ. Kanıt bağlama
(K1–K6) aynen korunur: bir kanıt iki kipte sunuluyorsa skorlu sorunun `evidence_screen_ids`'i
İKİSİNİ birden listeler — böylece kör test (blind-test) iki kipi de söker ve ikinci kip gizli
cevap kanalına (K5 ihlali) dönüşmez.

## Karar noktası kuralları

### `medya` + `ekran_secimi` — çoklu temsil: aynı kanıt, en az iki kip

Ölçmenin bağlandığı **her kanıt kaynağı** için en az iki kip hedeflenir (ikili denetim: kritik
kanıt tek kanalda mı yaşıyor?). 30 ekran tipinin temsil-kanalı haritası:

| Kanal | Taşıyıcı tipler |
|---|---|
| Yazılı metin | `content_slide`, `accordion`, `tabs`, `timeline`, `worked_example` (adım gerekçeleri) |
| Görsel/uzamsal | `data_chart`, `image_compare`, `labeled_diagram`, `hotspot` (anlotasyonlu artefakt), `timeline` |
| İşitsel | her tipte `narration_text` + TTS (`auto_tts` / `synthesize_speech`) |
| Hareketli | `video`, `lottie` (yalnız öğretiyorsa — C4), `render_motion_video` çıktısı |
| Etkileşimli keşif | `flashcards`, `simulation`, `exploration`, `image_compare` kaydırıcısı |

Somut çiftler: sayısal karşılaştırma → tablo (`content_slide`) + `data_chart`; süreç → adım
metni (`worked_example`) + `timeline`; durum değişimi → önce/sonra metni + `image_compare`.

**Dürüstlük sınırı (işitsel kanal — sunucunun belgeli sınırlarına dayanır,
`docs/ACCESSIBILITY-CONFORMANCE.md`):** işitsel kip ancak `narration_text` YAZILIYSA çift
yönlüdür — metin varsa oynatıcı hem TTS/sesi hem CC bandını sunar. Yalnız ses varlığı yüklemek
(metinsiz) transkriptsiz kanal üretir; `video` için senkron altyazı desteği YOKTUR (`<track>`
yok). Bu yüzden kaplama kuralı ikilidir: **anlatım = her zaman `narration_text` ile**; konuşma
taşıyan `video` ancak içeriği spec'ten doğrulanabiliyorsa (caption/transcript metni cevabı
gerçekten taşıyorsa — K1 dış-medya şartıyla aynı) temsil sayılır. "Videoda vardır" temsil değildir.

### `olcme` — çoklu eylem/ifade: cevap biçimi seçenekleri

Aynı beceri farklı yanıt biçimleriyle gösterilebilmeli; biçim, ölçülen beceriyi değiştirmeden
seçilir (hiza `assessment-alignment` kaplamasının işidir; buradaki karar aynı düzeyde BİÇİM
çeşitliliğidir):

- Sınıflama: `drag_drop` yerine/yanında `matching` (seçim-kutulu, klavye-uyumlu biçim).
- Üretim: `fill_blank` (tam terim) ↔ `mcq` (tanıma) — hedef fiil geri getirme İSE `fill_blank`
  kalır, biçim alternatifi eş-düzey başka geri getirme maddesidir.
- Açık ifade: `exploration` (`input_kind: "text"`) skorsuz üretim + `poll` açık uçlu yansıma —
  skorlu ölçümün yerine geçmez, ifade kanalı ekler.
- Çok maddeli pratikte `adaptive_practice`: aynı beceriye farklı zorlukta çok madde — tek
  maddenin biçim yanlılığını seyreltir.

### `gezinme` — çoklu katılım: yol ve bağlam seçeneği

- Bağlam seçimi: aynı kazanım iki sektör/rol varyantıyla sunulabilir (`branching` — "kendi
  alanına en yakın vakayı seç"; iki kol da AYNI kanıt yapısını kurar, `set_vars` ile seçim izi
  tutulur). Katılım ilkesinin "ilgililik/özerklik" ayağı yapısal karşılığını burada bulur.
- Yoğun başvuru içeriği zorunlu akışa değil isteğe bağlı katmana: `accordion`/`tabs` (öğrenen
  neyi ne zaman açacağını seçer); `flow` yerine `stage` ritmi içinde öğrenen-hızlı `reveal`.
- Seçenek eklenir, ZORUNLULUK eklenmez: UDL kaplaması hiçbir ekranı "herkes için ek tur"a
  çevirmez — seçenekler atlanabilir destektir (atlanamayan tek şey kanıt ekranlarıdır; o kural
  `expertise-adaptive` kaplamasında ve K/Z tabanlarında yaşar).

## Somut ekran kararları (parametre düzeyinde)

**1) Aynı kanıt iki kipte + ÇOĞUL kanıt bağı (temsil çoğaltmanın doğru biçimi):**

```jsonc
// Kanıt: vardiya devir kayıtlarındaki gecikme deseni — kip 1: tablo metni
{ "type": "content_slide", "id": "kanit_tablo", "title": "Devir kayıtları: üç vardiyanın gecikmeleri",
  "body_html": "<p>Son 12 devirde gecikmeler (dk): Gece→Sabah 22 · 19 · 25 · 21 — diğer iki geçiş 0–6 aralığında.</p>" },
// kip 2: aynı verinin grafiği (yeni olgu YOK — aynı kanıt, ikinci kip) + görsel kipin metin alternatifi caption'da
{ "type": "data_chart", "id": "kanit_grafik", "chart_type": "bar", "title": "Aynı kayıtlar, grafikte",
  "caption": "Gece→Sabah geçişi 20 dk bandında; diğer geçişler 6 dk altında.", "data": { /* aynı sayılar */ } },
// skorlu soru İKİ kipe birden bağlanır — kör test ikisini de söker (K5 güvenliği)
{ "type": "mcq", "id": "q_devir", "points": 20, "evidence_screen_ids": ["kanit_tablo", "kanit_grafik"],
  "prompt_html": "<p>Kayıtlara göre iyileştirme bütçesi hangi geçişe ayrılmalı?</p>", "options": [ /* … */ ] }
```

**2) Eylem/ifade seçeneği — sınıflama görevinin klavye-uyumlu biçimi:**

```jsonc
// drag_drop yerine matching: aynı sınıflama becerisi, seçim-kutulu ifade biçimi
// (drag_drop'un işaretçi-bağımlılığı sunucu uygunluk belgesinde belgeli sınırdır)
{ "type": "matching", "id": "q_siniflama", "points": 20,
  "evidence_screen_ids": ["kanit_tablo", "kanit_grafik"],
  "pairs": [
    { "left_html": "Devir gecikmesi 20 dk bandında", "right_html": "Yapısal sorun — süreç yeniden tasarlanır" },
    { "left_html": "Tek seferlik 25 dk sapma", "right_html": "Vaka bazlı — kök neden kaydı açılır" } ] }
```

**3) Katılım — bağlam seçimi `branching` ile (iki kol, aynı kanıt yapısı):**

```jsonc
{ "type": "branching", "id": "baglam_secimi", "title": "Vakanı seç: saha mı, ofis mi?",
  "prompt_html": "<p>Aynı devir problemi iki bağlamda yaşanıyor. Sana yakın olanı seç — ikisi de aynı beceriyi kurar.</p>",
  "choices": [
    { "text_html": "Üretim sahası vardiyası", "goto": "vaka_saha", "set_vars": [{ "var": "baglam", "op": "set", "value": 1 }] },
    { "text_html": "Çağrı merkezi nöbeti",   "goto": "vaka_ofis", "set_vars": [{ "var": "baglam", "op": "set", "value": 2 }] } ] }
```

## Sınırlar (bu kaplama NE YAPMAZ)

- Teknik erişilebilirlik uyumu vermez — alt metin kalitesi, klavye/odak, kontrast, zamanlayıcı
  kararları `accessibility` kaplamasının alanıdır (ön-maddedeki sınır bildirimi: çelişkide
  teknik uyum önceliklidir).
- Temsil çeşitliliğini zorunluluğa çevirmez: seçenek sunar, herkese ek tur dayatmaz.
- Kanıt icat etmez: her ek kip, mevcut kanıt kaynağının kipidir ve `evidence_screen_ids`'e
  eklenir; yeni iddia/olgu taşıyan "ek temsil" temsil değil yeni içeriktir ve K1 denetimine girer.
- Sıra dayatmaz: hangi kipin hangi fazda geleceği paketin işidir.

## Literatür

- **Birincil:** CAST (2024). *Universal Design for Learning Guidelines version 3.0* (yayın:
  30 Temmuz 2024). udlguidelines.cast.org — üç ilke (Engagement / Representation / Action &
  Expression) ve 3.0 güncelleme kapsamı DOĞRULANDI.
- Kuramsal köken: Meyer, A., Rose, D. H., & Gordon, D. (2014). *Universal Design for Learning:
  Theory and Practice.* Wakefield, MA: CAST Professional Publishing.
- Teknik uyum sınırının dayanağı: scorm-mcp `docs/ACCESSIBILITY-CONFORMANCE.md` (WCAG 2.2 AA
  kısmi uygunluk beyanı — video senkron altyazı yok; `narration_text` yoksa transkript yok;
  `drag_drop` işaretçi-bağımlı). Bu kaplama o sınırların ÜSTÜNDE vaat kurmaz.
