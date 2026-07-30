# v1 → v2 geçiş rehberi (G2)

**Kime:** v1 döneminde (paket beyanı ve kanıt bağlama yokken) yazılmış kursu/şablonu olan
yazarlara. v1'in tipik dokusu: iddia slaytı + quiz deseni, "İzle→Uygula→Sıra Sende" (Pattern A)
ya da kavram dersi (Pattern B), skorlu rehberli pratik, "Doğru!" feedback'i, `evidence_screen_ids`
yok. Bu rehber **yeniden yazdırmaz** — üç canlı vitrin kursunun v2'ye gerçekten nasıl
taşındığının damıtılmış oyun kitabıdır (spot-the-phish, password-hero, ad-hominem; üçü de
yapı/tema/medya korunarak taşındı ve prod strict lint'te 0 hata / 0 uyarı / coverage 1.0 ile
yeniden yayımlandı).

## Ne YENİDEN yazılmaz

Geçiş bir bağlama-ve-süpürme işidir, yeniden inşa değil. Üç canlı demoda **korunanlar**:
tema/görsel kimlik, medya varlıkları, ekran sırası ve tipleri, anlatım metinleri, oyun/simülasyon
mekaniği. **Değişenler:** skorlu soruların kanıt bağları (+ gerekiyorsa birkaç yeni kanıt ekranı),
soru gövdeleri/başlıkları (K4), özet/tavsiye metinleri (K5), maddeler-arası sızıntılar (K6),
feedback anatomisi. Tipik ekleme maliyeti kurs başına 1–2 yeni ekran + birkaç SVG oldu.

## Kırıcı değişiklikler ve giderme reçeteleri

| # | Kırıcı değişiklik | Belirti | Reçete |
|---|---|---|---|
| 1 | **YÖNTEM BEYANI zorunlu** (Katman 0) | Pre-flight Madde 1b boş | Seçiciyi çalıştır (`core/method-selector.md`); mevcut v1 yapısını en yakın pakete EŞLE (aşağıdaki Pattern A tablosu) — yapıyı değiştirmeden beyanı yaz. |
| 2 | **Skorlu soru kanıt bağı ister** (E1 lint) | `unbound_scored_question` (normal modda WARN, `strict=True`'da FAIL); `evidence_binding_coverage` < 1.0 | K3 "bağla ya da at": cevabı gerçekten üreten ekran(lar)ı `evidence_screen_ids`'e yaz; kanıt yoksa üret, üretmeyeceksen `points: 0` yap ya da soruyu at. |
| 3 | **Rehberli pratik skorlanamaz** (Z2/Z3) | Pattern A "Uygula" adımı puanlı | Simülasyon/deneme ekranını `points: 0` yap; skoru bağımsız-ölçüm sorusuna taşı. |
| 4 | **"Doğru!"/"Yanlış" feedback yasak** (G1–G3) | Tek kelimelik feedback | Üçlüyü kur: neden doğru + tipik yanılgı neden yanlış + kanıt ekranına geri işaret. |
| 5 | **K4 — gövde kendine-yeterliliği** | Soru gövdesi/başlığı cevabın kritik olgusunu taşıyor | Olguyu kanıt ekranına taşı, gövdeyi atıfla yeniden kur ("kayıttaki damgaya göre…"). |
| 6 | **K5 — özet sızıntısı** | Özet/tavsiye ekranı skorlu cevapları yeniden söylüyor | Kavram düzeyine indir (karar noktalarını adlandır, cevabı kurma) ya da ekranı ilgili sorunun kanıt setine ekle. |
| 7 | **K6 — çapraz-madde kontaminasyonu** | Bir sorunun şıkkı/başlığı başka sorunun cevabını türetiyor | Sızdıran maddeyi nötrleştir ya da iki maddeyi tek karara birleştir. |
| 8 | **`PRIOR_KNOWLEDGE` kadranı + Eğitim Okuması** | Dial gerekçesi yok | Bölüm 0 beyanını ve PK değerini (bilinmiyorsa 3 varsay, beyan et) pre-flight'a yaz. |

Geçiş dönemi notu: sunucu E1 lint'i normal modda bağsız skorlu soruyu **WARN** olarak verir
(v1 kursları derlenmeye devam eder); `strict=True` **FAIL** eder. Hedef her zaman strict-temiz +
coverage 1.0'dır — üç demo da bu hedefe taşındı.

## Pattern A → rosenshine-di eşleme tablosu

v1'in "İzle → Uygula → Sıra Sende" kalıbı atılmadı; `rosenshine-di` paketine eşlendi (canlı hali:
`templates/rosenshine-di.json`, `_pattern_a_eslemesi` bloğu):

| v1 Pattern A adımı | v2 rosenshine-di fazı | Geçişte ne değişir |
|---|---|---|
| İzle (video, boş caption) | `sunum_model` | Caption/transcript cevabı spec'ten doğrulanabilir biçimde TAŞIR (K1 dış-medya şartı); yanına çözümlü-örnek slaytı eklenir. |
| Uygula (simulation, puanlı) | `rehberli_pratik` | **Skor kaldırılır** (`points: 0`, Z3); feedback G1–G3 üçlüsüne çevrilir. |
| Sıra Sende (mcq, "Doğru!") | `bagimsiz_pratik` | Skorlu ölçüm burada kalır; `evidence_screen_ids` (ÇOĞUL) ile `sunum_model` ekranlarına bağlanır; feedback gerekçeli olur. |
| (karşılığı yoktu) | `gunluk_tekrar` | İlke 1 gereği eklenir; serinin İLK modülünde atlanabilir. |

Pattern B (kavram dersi) aynı mantıkla `merrill-fpi`'ye eşlenir (`templates/merrill-fpi.json`,
`_pattern_b_eslemesi`).

## Oyun kitabı — üç canlı demonun gerçekte izlediği sıra

1. **Skorlu envanter çıkar:** `points > 0` + puana yazan tüm ekranları listele (K3 adım 1).
2. **Her soruya DÜRÜST kanıt ara; yoksa üret.** Bağ ancak ekran cevabı gerçekten üretiyorsa
   yazılır — "yakın konu" yetmez. Gerçek bulgular: *"K1 boşluğu: eşleştirme sorusunun dört terimi
   kursun HİÇBİR yerinde öğretilmiyordu → `terms1` flashcards eklendi"* (spot-the-phish);
   oltalama e-postasının/pop-up'ın kendisi hiçbir ekranda incelenmiyordu → "Delil A" artefakt
   slaytları eklendi (`c_email`, `c_popup`, `c_tr` — K1 tür 4); düz-metin öğreti slaytları,
   sökülemeyen ikinci cevap kanalı olmasın diye blok-artefakta çevrilip kanıt setine alındı.
3. **K4 gövde süpürmesi:** her skorlu gövde/başlıkta kursa-özgü kritik olguyu ara. Gerçek bulgu:
   password-hero'da sorunun BAŞLIĞI ("Length Beats Complexity") cevabın kendisiydi → başlık
   nötrlendi, gövde artefakt-atfına çevrildi; spot-the-phish'te bir oyun düğümünün gövdesi
   değerlendirmeyi baştan söylüyordu → hüküm gövdeden çekildi.
4. **K5 özet süpürmesi:** özet + `results_breakdown` tavsiye metinlerinde her skorlu sorunun
   cevap önermesini ara. Gerçek bulgu: üç kursun ÜÇÜNDE de kapanış/tavsiye ekranı skorlu
   cevapları tek nefeste yeniden söylüyordu → kavram-düzeyi çerçeveye indirildi ("üç yargı
   alanını adlandır, hükmü söyleme").
5. **K6 çapraz-madde süpürmesi:** madde çiftlerini tara. Gerçek bulgu: ad-hominem'de oyun
   segmentinin metni, eşleştirme sorusunda öğretilen örneğin BİREBİR kopyasıydı — kanıt
   sökülse bile cevap öteki maddeden okunuyordu → segmente taze bir vaka cümlesi yazıldı;
   spot-the-phish'te doğru şık + oyun ipucu bir tekniğin ADINI verip başka sorunun cevabını
   türetiyordu → adlandırma nötrleştirildi.
6. **Strict lint'e koş:** hedef `clean=True, 0 hata / 0 uyarı, evidence_binding_coverage 1.0`
   (üç demonun üçünde de tutturuldu).
7. **Kalan kanonu BELGELE, zorlama:** kamusal-kanon soruları artefakta-uygulamaya çevirmek bazen
   yeni içerik ister; ucuz değilse soruyu dürüstçe bağlı bırak ve "kalan kanon" listesine yaz
   (üç demoda da yapıldı) — ya da K3 gereği skorsuzlaştır. Dönüştürme tekniği:
   `references/source-expansion.md`.

## Uçtan uca örnek: mini Pattern A kursu v1 → v2

**v1 (ÖNCE)** — üç tipik ihlal: skorlu Uygula (Z3), bağsız + "Doğru!" feedback'li Sıra-Sende
(E1 + G1), cevabı yeniden söyleyen özet (K5):

```jsonc
{ "title": "Etiket Yazıcısında Şerit Değişimi", "scorm_version": "2004", "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "assets": [ { "id": "demo_serit", "filename": "demo.mp4", "source": "data:video/mp4;base64,AAAAGGZ0eXBtcDQyAAAAAG1wNDJpc29t" },
              { "id": "shot_kapak", "filename": "kapak.png", "source": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==" } ],
  "screens": [
    { "id": "intro", "type": "title_slide", "title": "Şerit Değişimi", "subtitle": "Bu kursta şunları öğreneceksiniz" },
    { "id": "izle1", "type": "video", "title": "İzle", "video_asset_id": "demo_serit", "caption": "" },
    { "id": "uygula1", "type": "simulation", "title": "Uygula", "points": 20,
      "prompt_html": "<p>Adımları uygula.</p>",
      "feedback": { "correct_html": "Doğru!", "incorrect_html": "Yanlış." },
      "steps": [ { "image_asset_id": "shot_kapak", "instruction_html": "<p><b>1.</b> Kapağı açan mandala tıkla.</p>",
                   "regions": [ { "id": "r1", "shape": "rect", "coords": [400, 260, 200, 120], "correct": true } ] } ] },
    { "id": "ss1", "type": "mcq", "title": "Sıra sende", "points": 30,
      "prompt_html": "<p>Baskı soluk çıkıyorsa ilk kontrol edilecek şey nedir?</p>",
      "options": [ { "id": "a", "text_html": "Şeridin mürekkepli yüzünün etikete bakması", "correct": true },
                   { "id": "b", "text_html": "Yazıcının ağ bağlantısı" } ],
      "feedback": { "correct_html": "Doğru!", "incorrect_html": "Yanlış, tekrar dene." } },
    { "id": "ozet", "type": "summary", "title": "Özet",
      "body_html": "<p>Unutma: baskı soluksa şeridin mürekkepli yüzü etikete bakmıyordur.</p>" } ] }
```

Bu spec bugün derlenir ama normal lint'te bağsız-soru uyarısı alır, `strict=True`'da FAIL'dir
ve coverage < 1.0'dır.

**v2 (SONRA)** — aynı yapı, aynı medya; reçetelerin uygulanmış hali (1: beyan, 2: bağ,
3: skor→0, 4: feedback üçlüsü, 5: K4 — kritik olgu modele taşındı, 6: özet kavram düzeyi):

```jsonc
{ "_yontem_beyani": [
    "- kazanım: O1 (tür: prosedür · PK: 2 · hata maliyeti: düşük · bütçe: 4 dk)",
    "  paket: rosenshine-di  · kaplamalar: []",
    "  elenenler: [5e-inquiry (prosedür kapsam dışı), 4cid (tek kısa görevde görev-dizisi gereksiz)]",
    "  gerekçe: \"Tek-yollu kısa prosedür, kitle ilk kez görüyor; model-önce gösterim + skorsuz deneme en kısa güvenli yol. (Pattern A yapısı korunarak eşlendi.)\"" ],
  "title": "Etiket Yazıcısında Şerit Değişimi", "scorm_version": "2004", "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "assets": [ { "id": "demo_serit", "filename": "demo.mp4", "source": "data:video/mp4;base64,AAAAGGZ0eXBtcDQyAAAAAG1wNDJpc29t" },
              { "id": "shot_kapak", "filename": "kapak.png", "source": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==" } ],
  "screens": [
    { "id": "intro", "type": "title_slide", "title": "Şerit bitti, hat bekliyor",
      "subtitle": "~4 dk · değiştir → yönünü doğrula → test bas" },
    { "id": "izle1", "type": "video", "title": "İzle: 90 saniyede şerit değişimi", "video_asset_id": "demo_serit",
      "caption": "Adım adım: (1) Mandala bas, kapak açılır. (2) Biten ruloyu çıkar, yenisini yerleştir. (3) Şeridi gergin geçir — mürekkepli (mat) yüz ETİKETE bakar; parlak yüz kafaya sürtünür. (4) Kapağı kilitle, test etiketi bas. Yön neden kritik: mürekkep etikete değil kafaya basarsa çıktı soluk kalır ve kafa kirlenir." },
    { "id": "model_serit", "type": "content_slide", "title": "Çözümlü örnek: soluk çıktının teşhis zinciri",
      "blocks": [
        { "html": "<p><b>Adım 1 — belirtiyi oku:</b> test etiketi soluk/boş. <i>Neden önce bu:</i> belirti, zincirin hangi halkasına bakılacağını söyler.</p>" },
        { "html": "<p><b>Adım 2 — yön kontrolü:</b> kapağı aç, şeridin MAT (mürekkepli) yüzünün etikete baktığını doğrula. <i>Neden önce yön, sonra başka şey:</i> ters yön, soluk çıktının en sık ve en ucuz düzeltilen nedenidir — videoda kafa kirlenmesi maliyeti de gösterildi.</p>" },
        { "html": "<p><b>Adım 3 — gerginlik:</b> yön doğruysa şerit boşluğunu al ve yeniden test bas.</p>" } ] },
    { "id": "uygula1", "type": "simulation", "title": "Uygula (puan yok — dene, yanıl, gör)", "points": 0,
      "prompt_html": "<p>Takılırsan ipucu; sonra çözümlü örneğe dön.</p>",
      "feedback": { "correct_html": "<p>Mandal → kapak → rulo sırası doğru: kapak açılmadan yön ne görülür ne düzeltilir.</p>",
                    "incorrect_html": "<p>Kapağı açan mandalı atlıyorsun — yön kontrolü kapalı kapakla yapılamaz. Videodaki 1. adıma geri dön.</p>" },
      "steps": [ { "image_asset_id": "shot_kapak", "instruction_html": "<p><b>1.</b> Kapağı açan mandala tıkla.</p>",
                   "hint_html": "<p>Rulo yuvasının hemen önündeki mandal.</p>",
                   "image_alt": "Etiket yazıcısının önden görünümü; rulo yuvasının önünde kapak mandalı",
                   "regions": [ { "id": "r1", "shape": "rect", "coords": [400, 260, 200, 120], "correct": true } ] } ] },
    { "id": "q_serit", "type": "mcq", "title": "Skorlu: hat başındaki teşhis", "points": 50,
      "evidence_screen_ids": ["izle1", "model_serit"],
      "prompt_html": "<p>Vardiya arkadaşın şeridi az önce değiştirdi; test etiketi soluk çıktı. Çözümlü örnekteki zincire göre İLK kontrol hangisi?</p>",
      "options": [ { "id": "a", "text_html": "Şeridin mat yüzünün etikete bakıp bakmadığı", "correct": true },
                   { "id": "b", "text_html": "Yazıcının ağ bağlantısı ve sürücü sürümü" },
                   { "id": "c", "text_html": "Etiket rulosunun son kullanma tarihi" } ],
      "feedback": { "correct_html": "<p>Doğru — soluk çıktının en sık ve en ucuz düzeltilen nedeni ters yöndür; videodaki yön kuralı + çözümlü örneğin 2. adımı bu sırayı kurar.</p>",
                    "incorrect_html": "<p>Belirti baskı KALİTESİ, bağlantı/tarih belirtileri farklıdır. Çözümlü örneğin 'neden önce yön' gerekçesine ve videodaki yön kuralına geri dön.</p>" } },
    { "id": "ozet", "type": "summary", "title": "Özet",
      "body_html": "<p>Bir değişim, bir teşhis zinciri: belirtiyi oku, zincirin en ucuz halkasından başla. Sıradaki soluk etikette zincir senin.</p>",
      "show_score": true, "show_completion": true } ] }
```

**Doğrulama (gerçek sunucu, in-memory `build_from_spec` + `lint_course`, 2026-07-30):**
v1 spec — normal mod 0 hata / 3 uyarı (`unbound_scored_question`: `uygula1` + `ss1`,
`missing_alt_text`: simülasyon ekran görüntüsü), coverage 0.0; `strict=True` aynı üçü hataya
terfi eder → FAIL. v2 spec — `clean=True`, 0 hata / 0 uyarı (strict),
`evidence_binding_coverage 1.0`. Kalan kanon notu:
`q_serit` yön kuralı deneyimli teknisyenin bildiği bilgidir — burada dürüstçe bağlı bırakıldı
ve belgelendi (oyun kitabı adım 7); tam artefakta-uygulama dönüşümü için
`references/source-expansion.md`.

## Geçiş kontrol listesi (özet)

- [ ] YÖNTEM BEYANI yazıldı (yapı en yakın pakete eşlendi; Pattern A/B tabloları)
- [ ] Skorlu envanter + her soruya `evidence_screen_ids` (K3: bağla / skorsuz / at)
- [ ] Rehberli pratik `points: 0` (Z3)
- [ ] Feedback üçlüsü her skorlu soruda (G1–G3)
- [ ] K4 gövde süpürmesi · K5 özet süpürmesi · K6 çapraz-madde süpürmesi yapıldı
- [ ] `lint_course(strict=True)` → 0 hata / 0 uyarı / coverage 1.0
- [ ] Kalan kanon soruları listelendi (zorlanmadı); kör test koşuldu (`eval/blind-test.md`)
