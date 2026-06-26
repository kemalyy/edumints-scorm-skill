# Anti-slop — SCORM'da jenerik çıktının somut yasakları

**Workflow'dan ÖNCE oku.** Bu dosya, bir LLM'in SCORM/e-öğrenmede default olarak ürettiği
"slop" kalıplarını isimlendirir ve **ikili (binary), sayılabilir** kurallarla yasaklar —
"kaçın / çeşitlendir / idareli" gibi yumuşak dil YOK. Her yasağın bir **override yolu** vardır:
koşul gerçekten karşılanıyorsa kural esner. Override'ı **sessizce kullanma** — pre-flight'ta
(`references/pre-flight.md`) gerekçesini bir cümleyle yaz.

**Okuma kuralı (mekanik):** her spec'i üretmeden önce → bu listeye karşı satır satır denetle →
ihlal say → düzelt → sonra `build_from_spec`. Bir ihlal bile kalmışsa kurs teslime hazır değil.

> Not: aşağıdaki tüm JSON parçacıkları gerçek `build_from_spec` şemasıdır (bkz. `mcp-cookbook.md`).
> Quiz tiplerinde `feedback` varsayılanı `{"correct_html":"Doğru!","incorrect_html":"Tekrar deneyin."}` —
> **bu varsayılanlar başlı başına slop'tur**; B3'e bak.

---

## A. İçerik yapısı

**A1 — Ardışık `content_slide` ≤ 2.** Araya etkileşim (mcq / true_false / drag_drop / hotspot /
matching / sorting / fill_blank / accordion / tabs / flashcards / simulation) girmeden **3+
`content_slide` peş peşe YASAK**. Mekanik: `screens` dizisinde tipi `content_slide` olan ardışık
zinciri say; > 2 ise fail.
→ *Override:* yok. Üç fikir varsa üçüncüden önce bir flashcards/accordion ile "keşfe" çevir ya da
bir yoklama ekle.

**A2 — Ekran başına ≤ 4 madde.** Bir ekranın `body_html`'inde 5+ `<li>` YASAK. **Bir ekran = bir
fikir.** Mekanik: `<li>` say.
→ *Override:* yalnızca açık bir başvuru/checklist ekranı (accordion ya da `flow` modunda) ve brief
açıkça "referans materyali" istiyorsa.

**A3 — Jenerik başlık YASAK.** "Modül 1: Giriş", "Bölüm 2: Genel Bakış", "Konu 3", "Ünite: Temeller"
gibi içeriksiz başlık YASAK. `title` ekranın **tek çıkarımını** taşır (mümkünse soru ya da iddia).
→ *Override:* yok. "Giriş" yerine "Neden 8 saniyede karar veriyoruz?" yaz.

**A4 — Sahte "Sonraki adımlar / Kaynaklar" dolgu ekranı YASAK.** İçeriği taşımayan, sırf kursu
uzatan jenerik kapanış ekranı ekleme. Kapanış = `summary` + tek net çıkarım.
→ *Override:* brief gerçek bir eylem listesi (politika linki, kayıt formu) istiyorsa — somut ve
tıklanabilir olmalı.

#### ÖNCE / SONRA
```jsonc
// SLOP — 3 ardışık content_slide, jenerik başlık, 6 madde
{ "type":"content_slide", "title":"Modül 1: Giriş",
  "body_html":"<ul><li>…</li><li>…</li><li>…</li><li>…</li><li>…</li><li>…</li></ul>" }
{ "type":"content_slide", "title":"Bölüm 2: Detaylar", "body_html":"<ul>…</ul>" }
{ "type":"content_slide", "title":"Bölüm 3: Özet",     "body_html":"<ul>…</ul>" }
```
```jsonc
// DÜZELTİLMİŞ — tek-fikir ekran → keşif → yoklama
{ "type":"content_slide", "title":"Bir oltalama e-postası 3 saniyede ele verir",
  "body_html":"<p>Gönderen adresi alan adıyla uyuşmuyorsa gerisini okuma.</p>",
  "narration_text":"Çoğu sahte e-posta görseliyle değil, alan adıyla yakalanır." }
{ "type":"flashcards", "title":"Gerçek mi, sahte mi?",
  "cards":[ {"front_html":"<b>destek@bankan1z.com</b>","back_html":"<p>Sahte — '1' harfi 'i' yerine.</p>"} ] }
{ "type":"mcq", "title":"İlk kontrolün ne?", "prompt_html":"<p>E-postayı açtın. İlk neye bakarsın?</p>",
  "points":10, "options":[ {"id":"a","text_html":"Gönderen alan adı","correct":true},
                            {"id":"b","text_html":"Konu satırı"} ],
  "feedback":{ "correct_html":"Evet — alan adı kimliğin özüdür; metin yanıltabilir.",
               "incorrect_html":"Konu kolayca taklit edilir. Önce gönderen alan adını oku." },
  "on_correct":[ {"var":"points","op":"add","value":10} ] }
```

---

## B. Copy / anlatım register'ı

**B1 — Müfredat-listesi açılışı YASAK.** İlk ekran "Hoş geldiniz! Bu kursta X, Y, Z öğreneceksiniz"
ile açamaz. İlk ekran **relevans**la açar: öğrencinin yaşadığı bir risk / sorun / soru. Müfredat
tasarımcının kafasında durur, ekranda değil.
→ *Override:* yok.

**B2 — `narration_text` ekran metnini birebir okuyamaz.** İkili kural ("idareli" değil): anlatım,
`body_html`/maddelerdeki cümlelerin kopyası OLAMAZ. Anlatım ekranı **genişletir, örnekler, bağlar**.
Mekanik: her anlatımlı ekranda narration ile gövde metnini karşılaştır; cümle örtüşmesi varsa fail.
→ *Override:* yok. Birebirse ya metni ya anlatımı yeniden yaz.

**B3 — Tek-kelime / varsayılan feedback YASAK.** Quiz `feedback` alanı `"Doğru!"` / `"Tekrar
deneyin."` (şema varsayılanı) ya da salt "Yanlış" OLAMAZ. Her `feedback`: **(a) neden** + **(b)
doğru modele bağ** + **(c) ilgili İzle/içerik ekranına yönlendirme** içerir. `correct_html` bile en
az "neden doğru" tek cümlesini taşır.
→ *Override:* yok.

**B4 — Filler fiil/sıfat YASAK.** Şu içi boş kalıplar YASAK: "keşfedin", "öğrenin", "harika",
"kolayca", "sadece birkaç tıkla", "bu çok önemli", "unutmayın ki", "bildiğiniz gibi". Her birini
**somut eylem fiili + somut nesne** ile değiştir.
→ *Override:* yok.

**B5 — Jenerik senaryo ismi YASAK.** "Ahmet bir şirkette çalışıyor", "Bir kullanıcı…", "Örnek A.Ş.",
"XYZ firması" gibi boş senaryo YASAK → **kitleye özgü, gerçekçi rol + bağlam + çatışma**.
→ *Override:* gizlilik için anonimleştirme gerekiyorsa **rol somut kalır**: "muhasebe stajyeri, ay
sonu kapanışında acil transfer talebi alıyor".

#### ÖNCE / SONRA — açılış
```jsonc
// SLOP — müfredat listesi, filler
{ "type":"title_slide", "title":"Siber Güvenliğe Hoş Geldiniz",
  "body_html":"<p>Bu kursta oltalamayı, parola güvenliğini ve veri korumayı kolayca öğreneceksiniz.</p>" }
```
```jsonc
// DÜZELTİLMİŞ — relevans + somut senaryo
{ "type":"title_slide", "title":"Bu e-posta CFO'dan geldi. Gerçekten mi?", "subtitle":"6 dk",
  "body_html":"<p>Geçen çeyrek üç şirket tek bir sahte e-postayla altı haneli ödeme yaptı. Bugün o e-postayı sen yakalayacaksın.</p>",
  "narration_text":"Muhasebeye 'acil' bir transfer talebi düşüyor — gönderen, patronun gibi görünüyor." }
```

#### ÖNCE / SONRA — feedback (varsayılanları ezmek)
```jsonc
// SLOP — şema varsayılanı = slop
{ "type":"mcq", "title":"Soru", "prompt_html":"<p>…?</p>",
  "options":[ {"id":"a","text_html":"Üzerine gel, URL'yi oku","correct":true},
              {"id":"b","text_html":"Hemen tıkla"} ] }   // feedback yok → "Doğru!"/"Tekrar deneyin."
```
```jsonc
// DÜZELTİLMİŞ — iki yönlü, gerekçeli, remediation
{ "type":"mcq", "title":"Bağlantıya tıklamadan önce?", "prompt_html":"<p>Şüpheli bir bağlantı gördün. İlk hamlen?</p>",
  "points":10, "options":[ {"id":"a","text_html":"Üzerine gel, gerçek URL'yi oku","correct":true},
                            {"id":"b","text_html":"Hemen tıkla, sonra bakarım"} ],
  "feedback":{ "correct_html":"Doğru — fareyle üzerine gelince gerçek hedef altta belirir; alan adı uyuşmuyorsa tıklama.",
               "incorrect_html":"Tıkladıktan sonra geç olur. 'Bağlantıyı Doğrula' ekranına dönüp üzerine-gel kontrolünü tekrar gör." } }
```

---

## C. Görsel / medya

**C1 — Klişe stok görsel YASAK.** Şunları üretme/ekleme: el sıkışan takım, parlayan ampul (fikir),
dişli çark (süreç), ekrana parmakla işaret eden gülümseyen ofis ekibi, soyut "dijital ağ" mavi-parçacık,
dümdüz dekoratif gradient arka plan. Bunlar bilgi taşımaz.
→ *Bunun yerine:* (1) **anlotasyonlu gerçek ekran görüntüsü** (özellikle `simulation`/`hotspot` için —
öğretir), (2) **veri-görseli** (`render_motion_video` ile basit grafik), (3) **kavramı gösteren özel
diyagram/SVG** ya da `lottie`, (4) görsel bir şey öğretmiyorsa **görselsiz, tipografi-güçlü stage**.
→ *Override:* yok (gerçek ürün fotoğrafı / kuruma ait saha fotoğrafı klişe değildir, serbest).

**C2 — Tek animasyonun kurs boyu tekrarı YASAK.** Aynı `animation` değerini (örn. `zoom`) **ardışık
3+ ekranda** kullanma. Varsayılan `fade-up` (sakin/profesyonel); `zoom`/`slide-left` yalnız **vurgu**
için seyrek. Mekanik: ardışık aynı-animation zincirini say; > 2 ise fail.
→ *Override:* yok. `prefers-reduced-motion` zaten otomatik — sen ekstra uğraşma.

**C3 — Keyfi koyu tema YASAK (hard ban).** Açık / nötr / yüksek-kontrast e-öğrenme standardıdır:
`modern-light`, `academic`, `high-contrast`. Marka için **yalnız vurgu rengini** override et.
→ *Override:* brief açıkça **marka koyu temasını zorunlu kılıyorsa** ve kontrast WCAG AA'yı geçiyorsa
(alt metin + okunurluk korunarak).

**C4 — Ağır medyayı "havalı" diye ekleme.** `video` / `lottie` / `render_motion_video` yalnızca
**bir şey öğretiyorsa** girer (explainer, veri-viz, demo). Dekoratif intro/outro videosu YASAK.
→ *Override:* brief marka açılış sting'i istiyorsa ≤ birkaç sn, tek yerde.

**C5 — `body_html`/`*_html` içine ham `<svg>` / `<canvas>` / `<script>` YASAK (hard ban).** Sanitizer
bunları siler → görsel hiç çıkmaz. Diyagramı her zaman asset pipeline'ından geçir: **`svg_to_asset`**
(ham SVG ver, tercih edilen) veya `add_asset` (`data:image/svg+xml;base64,…`) → dönen `id`'yi
`media_asset_id` / `image_asset_id` / blok `asset_id`'de kullan; ekran `<img>` ile render eder.
Animasyon için Lottie asset veya MP4 (`render_motion_video` / `make_video_from_image_audio`).
Script/etkileşim gerekiyorsa `<script>` gömme — `simulation` veya `game` ekran tipini kullan (player
sandbox'ı içinde güvenle çalışır). Grafik için `data_chart` ekran tipi (sunucu-taraflı güvenli SVG üretir).
→ *Override:* yok.

---

## D. Oyunlaştırma

**D1 — Patronlaştırıcı oyunlaştırma YASAK.** Rozet, yıldız, "🏆 Liderlik Tablosu", "+10 PUAN!"
patlaması/konfeti, "Seviye atladın!" pop-up'ları YASAK. Kullanıcı tercihi: **içsel ustalaşma**
mekaniği. Puanı sessiz ilerleme olarak tut (`points_var` HUD) ve kapanışta **ustalaşma mesajı** ver
("Artık üç oltalama işaretini tek bakışta ayırıyorsun"), kutlama-spam'i değil.
→ *Override:* brief açıkça **yarışmacı bir bağlam** istiyorsa (örn. satış ekibi turnuvası) — o zaman
puan/sıralama amaçlıdır, dekoratif değil.

**D2 — Anlamsız puan YASAK.** Her ekrana rastgele `points` dağıtma. Puan yalnız **skorlanan
değerlendirmede** anlamlıdır ve geçme eşiğiyle (`tracking.passing_score`) tutarlı olmalı.
→ *Override:* yok.

**D3 — Sahte karar senaryosu YASAK** (`decision_scenario`). Şunlar YASAK: (a) bir seçenek bariz
doğru, ötekiler saçma → gerçek ikilem yok; (b) tüm seçenekler aynı düğüme gider, `score_delta`'lar
eşit → dallanma sahte; (c) `feedback_html` sonucu/gerekçeyi söylemiyor (B3 senaryoya da uygulanır);
(d) tek düğüm (≥2 düğüm + en az bir gerçek dallanma olmalı). Kötü kararın `score_delta`'sı **negatif**
olmalı (sonuç gerçek olsun).
→ *Override:* yok. Gerçek ikilem yoksa `mcq` kullan, senaryo numarası yapma.

#### ÖNCE / SONRA — kapanış
```jsonc
// SLOP — kutlama spam'i
{ "type":"summary", "title":"🎉 TEBRİKLER! 🏆", "body_html":"<p>+100 PUAN kazandın! Rozetini topla!</p>",
  "show_score": true }
```
```jsonc
// DÜZELTİLMİŞ — ustalaşma + tek çıkarım
{ "type":"summary", "title":"Artık sahte e-postayı patron yazmış gibi görünse de yakalarsın",
  "body_html":"<p>Üç işaret: uyuşmayan alan adı, aciliyet baskısı, alışılmadık ödeme yolu. Şüphedeysen telefonla doğrula.</p>",
  "show_score": true, "show_completion": true }
```

---

## Override disiplini

Bir kuralı esnetiyorsan: (1) koşulun gerçekten karşılandığından emin ol, (2) `pre-flight.md`'de o
maddenin yanına **tek cümleyle gerekçe** yaz. Gerekçesiz override = ihlal. Kurallar katı ama esnek;
amaç öğreten kurs, kural saymak değil — ama "öğretiyor" iddiası bu listeyi geçmekle kanıtlanır.
