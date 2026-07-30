---
# Birincil kaynak (DOĞRULANDI, 2026-07-29 — BSCS raporu; scirp.org referans kaydı +
# semanticscholar.org/paper/c1483e0b18dc2109ba4eb2aa3580d6bd865e6e79):
# Bybee, R. W., Taylor, J. A., Gardner, A., Van Scotter, P., Powell, J. C., Westbrook, A., &
# Landes, N. (2006). "The BSCS 5E Instructional Model: Origins and Effectiveness." Colorado
# Springs, CO: BSCS. — Beş faz: Engage (merak) · Explore (keşif) · Explain (açıklama) ·
# Elaborate (derinleştirme/transfer) · Evaluate (değerlendirme).
pack: 5e-inquiry
name: "5E Sorgulama Döngüsü (BSCS)"
version: 1
outcome_types: [kavram, ilke]
prior_knowledge: [3, 7]
error_cost: [düşük, orta]
requires_platform: []
phases:
  - id: merak
    amac: "Engage — çelişik/şaşırtıcı bir durumla merak tetiklenir ve ön-kavramlar yüzeye çıkarılır; öğretim YAPILMAZ."
    izinli_ekran_tipleri: [content_slide, video, image_compare, data_chart, poll, lottie]
    skorlanabilir: false
  - id: kesfet
    amac: "Explore — öğrenen olguyu skorsuz kurcalar; KENDİ tahmin/gözlem çıktısı üretilir ve saklanır (kanıt kaynağı 1)."
    izinli_ekran_tipleri: [exploration, simulation, image_compare, data_chart]
    skorlanabilir: false
  - id: acikla
    amac: "Explain — kanonik kavram/terim, öğrenenin keşif çıktısına AÇIK atıfla verilir (kanıt kaynağı 2)."
    izinli_ekran_tipleri: [content_slide, accordion, tabs, timeline, video, data_chart]
    skorlanabilir: false
  - id: derinlestir
    amac: "Elaborate — kavram YENİ bir bağlama skorsuz transfer edilir; sınırları ve karşı-örnekleri denenir."
    izinli_ekran_tipleri: [mcq, drag_drop, matching, sorting, simulation, decision_scenario, branching]
    skorlanabilir: false
  - id: degerlendir
    amac: "Evaluate — keşif + açıklama kanıtına bağlı skorlu ölçüm."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [kesfet, acikla]
scoring_allowed_from: degerlendir
conflicts_with: [rosenshine-di, cognitive-apprenticeship]
---

# 5e-inquiry — 5E Sorgulama Döngüsü (C3)

**Ne:** Keşif-önce yöntem. Öğrenen kavramı önce KENDİSİ kurcalar (Explore), kanonik açıklama
SONRA gelir ve öğrenenin kendi keşif çıktısına atıfla yapılır (Explain). **Ne zaman:** kavram /
ilke kazanımları, orta önbilgi (PK 3–7 — çürütülecek ön-kavram malzemesi var), düşük-orta hata
maliyeti (yanılmak güvenli ve ucuz). Derin işleme ve kalıcılık hedefiyle seçilir.

**Kanıt beyanı (Katman 1 bağlantısı — ÇOĞUL):** `evidence_phases: [kesfet, acikla]`. Kanıt
İKİ kaynaktan gelir: (1) öğrenenin `kesfet` fazında ürettiği kendi tahmin/gözlem çıktısı
(K1 türü 2), (2) `acikla` fazının bu çıktıya atıf yapan kanonik açıklaması (K1 türü 5'in
akrabası: deneme + kanonik çözüm karşılaştırması). Skorlu sorular `evidence_screen_ids`
(ÇOĞUL — scorm-mcp CONTRACTS §1.3 E1) ile her iki fazın ekranlarına birden bağlanabilir.

**Platform şartı: YOK (`requires_platform: []` — paket F2'siz de kurulur).** Keşif fazının
taahhüt→kayıt→açığa-çıkarma mekaniği için sıralama artık şudur:

1. **TERCİH — `exploration` (F2 #113, YAYINDA):** öğrenen girdisi (tahmin taahhüdü
   `input_kind: "prediction"`, sınıflama `"choice"`, gözlem notu `"text"`) `store_key` altında
   SAKLANIR ve `acikla` ekranları `<span data-exploration-ref="store_key"></span>` ile birebir
   GERİ OYNATIR — "senin tahminin şuydu" atfı artık gerçektir, feedback metniyle taklit değil.
   Yapısal skorsuz (puan alanı yok — Z3), koşulsuz kanıt-taşıyabilir (K1 türü 2).
2. **YEDEK — puan-0 formatif quiz:** F2 taşımayan (eski) hedeflerde mcq/true_false
   (`points: 0`) tahmin taahhüdünü alır, feedback açığa-çıkarma işlevini görür; atıf
   feedback + kanıt bağı üzerinden dolaylı yapılır. Bu desen doğrulanmıştır (0 hata /
   0 uyarı / coverage 1.0) ve geçerli kalır — ama geri oynatma sunamaz.

Her iki desende yanına deney/gözlem verisi taşıyan `data_chart`/`simulation`/`image_compare`
gelir. `requires_platform` boş kalır: F2 iyileştirmedir, ön koşul değil.

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `merak` | Engage: çelişik durum + ön-kavramları yüzeye çıkarma | content_slide, video, image_compare, data_chart, poll, lottie | ✗ |
| `kesfet` | Explore: tahmin taahhüdü + skorsuz kurcalama — **kanıt 1** | exploration* (TERCİH — taahhüt + geri oynatma), simulation, image_compare, data_chart; yedek: mcq/true_false (points 0) | ✗ |
| `acikla` | Explain: kanonik açıklama, keşif çıktısına atıfla — **kanıt 2** | content_slide, accordion, tabs, timeline, video, data_chart | ✗ |
| `derinlestir` | Elaborate: yeni bağlama skorsuz transfer | mcq, drag_drop, matching, sorting, simulation, decision_scenario, branching | ✗ |
| `degerlendir` | Evaluate: skorlu ölçüm | hepsi | ✓ |

\* `exploration` = F2 tipi — YAYINDA (sunucu çekirdeğinde, 30 tipin 30.'su; şema: `prompt_html`,
`input_kind: "text" | "choice" | "prediction"`, choice/prediction'da `choices` ≥2, `store_key`
`[a-z0-9_-]+` ≤64 ve kurs genelinde TEKİL). Taahhüt mekaniğinin tercih edilen taşıyıcısıdır ve
öğrenen girdisinin geri oynatımını ekler; `requires_platform` yine boş — puan-0 quiz yedeği
F2'siz hedeflerde geçerli kalır.

Faz notları:

- `merak` ÖĞRETMEZ: cevabı verirsen Explore ölür. Doğru biçim çelişik gözlem/şaşırtıcı veridir
  ("dev gemi çelikten — neden batmıyor?"), tanım/başlık slaytı değil.
- `kesfet`'te yanlış tahmin DEĞERLİDİR ve skorsuzdur (Z3): sonradan Explain'in çürüteceği
  ön-kavram, öğrenmenin hammaddesidir. Denemeyi puanlamak keşfi tahmin-yarışına çevirir.
- `acikla` keşiften KOPUK ders anlatımına dönüşmemeli — her kanonik iddia, öğrenenin az önce
  gördüğü/denediği bir gözleme bağlanır ("3. denemende gördüğün gibi…"). Kopuk Explain, bu
  paketi gizli bir rosenshine-di'ye çevirir (o zaman onu seç, dürüst olur).
- `derinlestir` AYNI kavramı YENİ bağlamda dener (transfer); yeni kavram ekleme fazı değildir.
- `degerlendir` soruları K2 denetiminden geçmeli: cevap keşif+açıklama çıktısından türemeli,
  genel alan bilgisinden değil.

## Bu paket NE ZAMAN seçilmemeli

- **Yüksek hata maliyeti** (`error_cost: yüksek` kapsam DIŞI — sert kısıt): sahada yanılması
  tehlikeli prosedür/karar keşfe bırakılamaz; yanlış genellemenin bedeli ödenemezse gösterim-önce
  (`rosenshine-di`, karmaşık beceri için `4cid`) seç.
- **Çok düşük önbilgi (PK &lt; 3 — uzmanlık-tersinmenin acemi ucu):** kurcalanacak zihinsel
  malzeme yokken keşif kaosa döner; acemi rastgele tıklar, örüntü değil gürültü üretir.
  Rehbersiz/az-rehberli keşfin acemide verimsizliği belgelidir (Kirschner, Sweller & Clark,
  2006) — önce `rosenshine-di` ile temel kur, 5E'yi ikinci modüle sakla.
- **Yüksek önbilgi (PK &gt; 7):** akıcı öğrenen keşif turundan yeni bir şey çıkarmaz; zaman
  maliyeti getirisini aşar (`pbl-case` / `retrieval-spaced` daha verimli).
- **Dar zaman bütçesi (≤ 5 dk):** beş faz sığmaz; fazları kırparak "5E görünümlü anlatım"
  üretme — dürüst seçim daha kısa bir paket kullanmaktır.
- **Olgu ezberi / prosedür icrası kazanımları:** `outcome_types` dışıdır; keşfedilecek
  kavramsal yapı yoksa döngü boşa döner.

## Çakışmalar (`conflicts_with`)

- `rosenshine-di` — **aynı kazanım üzerinde** birleştirilemez: Explore-önce ile model-önce sıra
  felsefeleri zıttır; ikisini aynı kazanımda harmanlamak ya keşfi öldürür (cevap önceden
  gösterildi) ya da modeli sulandırır. Farklı kazanımlar için ayrı modüllere bölerek
  kullanılabilir (seçici kuralı: "kursu böl ya da tek pakete karar ver").
- `cognitive-apprenticeship` — **aynı kazanım üzerinde** birleştirilemez (KARŞILIKLI beyan —
  C11 paketi kendi tarafından da bildirir): çıraklık uzmanın sesli-düşünme modeliyle AÇILIR,
  5E açıklamayı keşiften SONRAYA saklar; ortak `ilke` kazanımında ve kesişen PK bandında iki
  sıra beyanı zıttır.
- `productive-failure` bilinçli olarak LİSTEDE DEĞİL: iki yöntem de deneme-önce ailesindendir
  ve sıra felsefeleri uyumludur; ikisi arasında seçim çakışma değil doz kararıdır (PF, çözümsüz
  boğuşmayı daha uzun tutar).

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: kavram · PK: 5 · hata maliyeti: düşük): *"Bir cismin yüzme/batma davranışını
kütle-hacim ilişkisiyle (yoğunluk) açıklar."* Kitle: ortaokul fen; "ağır batar" ön-kavramı yaygın.

```jsonc
{
  "title": "Neden Batıyor? Yoğunluk Kavramı",
  "description": "5E sorgulama mikrokursu — 5e-inquiry",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "screens": [
    { "type": "title_slide", "title": "Neden Batıyor?", "subtitle": "8 dk · bir tahminle başlıyoruz" },

    // ── FAZ merak (Engage — çelişik durum; öğretim YOK) ──
    { "type": "content_slide", "id": "celiski", "title": "300.000 tonluk çelik gemi yüzüyor; 20 gramlık çakıl batıyor",
      "body_html": "<p>Çelik, çakıldan çok daha ağır bir malzeme. Gemi yüzüyor, çakıl batıyor. \"Ağır olan batar\" kuralı burada neden çalışmadı? Tahminini birazdan sınayacaksın.</p>" },

    // ── FAZ kesfet (Explore — KANIT 1: öğrenenin KENDİ tahmin/gözlem çıktısı; exploration = F2, YAYINDA) ──
    // Taahhüt: prediction — girdi store_key altında saklanır (PUAN ALANI YOK: yapısal skorsuz, Z3)
    { "type": "exploration", "id": "kesif_yuzme", "title": "Tahmin et: kütle 2×, hacim sabit",
      "input_kind": "prediction", "store_key": "tahmin_kutle2x",
      "prompt_html": "<p>Sanal küpün <b>kütlesini iki katına</b> çıkarıyoruz, hacmi aynı kalıyor. Suya bırakınca ne olur? Önce taahhüt et — tahminin saklanacak ve birazdan karşına gelecek.</p>",
      "choices": [
        { "id": "yuzer", "text_html": "Yüzer" },
        { "id": "batar", "text_html": "Batar" } ] },
    // Deneme kaydı: text — gözlem notu da saklanır ve acikla'da geri oynatılır
    { "type": "exploration", "id": "kesif_gozlem", "title": "Deneme notun: ne gözlemledin?",
      "input_kind": "text", "store_key": "gozlem_notu", "min_length": 20,
      "placeholder": "Kütleyi/hacmi değiştirince ne oldu? Kendi cümlelerinle…",
      "prompt_html": "<p>Kütleyi ve hacmi ayrı ayrı değiştirip denedin. Gözlemini <b>kendi cümlelerinle</b> kaydet — bu not senin kanıtın; açıklama ekranında birlikte kullanacağız.</p>" },

    // ── FAZ acikla (Explain — KANIT 2: kanonik açıklama, keşif çıktısına AÇIK atıfla) ──
    // Geri oynatma: <span data-exploration-ref="store_key"> — runtime saklanan değeri textContent
    // olarak enjekte eder ("senin tahminin şuydu" atfı GERÇEK; boş değer i18n yer tutucusuna düşer)
    { "type": "content_slide", "id": "aciklama_yogunluk", "title": "Gözleminin adı: yoğunluk",
      "blocks": [
        { "html": "<p>İlk tahminin şuydu: <b><span data-exploration-ref=\"tahmin_kutle2x\"></span></b> · kendi gözlem notun: <em><span data-exploration-ref=\"gozlem_notu\"></span></em>. Denemede gördün: kütle tek başına sonucu belirlemedi — hacmi büyüttüğünde AYNI kütle yüzdü.</p>" },
        { "html": "<p>Belirleyici oran: <b>yoğunluk = kütle ÷ hacim</b>. Suyunkinden (1 g/cm³) büyükse batar, küçükse yüzer. Gemi çeliği ağırdır ama gövdesi devasa bir hacme (içi hava) yayılır → ortalama yoğunluk suyun altına iner.</p>" } ] },

    // ── FAZ derinlestir (Elaborate — YENİ bağlama skorsuz transfer) ──
    { "type": "mcq", "id": "transfer_buz", "title": "Yeni bağlam: buzdağı", "points": 0,
      "prompt_html": "<p>Buz, sudan DONARAK oluşur ama suda yüzer. Yoğunluk açıklaması ne der? (Puan yok.)</p>",
      "options": [
        { "id": "a", "text_html": "Donarken hacmi genişler → yoğunluğu suyun altına düşer", "correct": true },
        { "id": "b", "text_html": "Buz sudan hafif bir maddedir" } ],
      "feedback": {
        "correct_html": "<p>Evet — kütle değişmedi, hacim büyüdü: senin 2. denemendeki desenin aynısı.</p>",
        "incorrect_html": "<p>\"Hafif/ağır\" tek başına açıklamaz — kendi denemende kütlesi aynı kalan küpün hacim büyüyünce yüzdüğünü gördün. 'Gözleminin adı: yoğunluk' ekranına dön.</p>" } },

    // ── FAZ degerlendir (Evaluate — SKORLU; kanıt bağı AÇIK ve ÇOĞUL: iki faza birden) ──
    { "type": "mcq", "id": "q_yogunluk", "title": "Skorlu: hangi cisim yüzer?", "points": 50,
      "evidence_screen_ids": ["kesif_yuzme", "kesif_gozlem", "aciklama_yogunluk"],  // E1 — kanıt: keşif çıktıları + kanonik açıklama (evidence_phases: [kesfet, acikla])
      "prompt_html": "<p>A cismi: 60 g / 40 cm³. B cismi: 30 g / 50 cm³. Suya bırakılırsa ne olur?</p>",
      "options": [
        { "id": "a", "text_html": "A batar (1,5 g/cm³ &gt; 1), B yüzer (0,6 g/cm³ &lt; 1)", "correct": true },
        { "id": "b", "text_html": "A yüzer çünkü daha küçük; B batar çünkü daha büyük" },
        { "id": "c", "text_html": "İkisi de batar çünkü ikisi de sudan ağır" } ],
      "feedback": {
        "correct_html": "<p>Doğru — oranı kurdun: kütle ÷ hacim, 1 g/cm³ eşiğiyle karşılaştırma. Keşifteki desenle aynı.</p>",
        "incorrect_html": "<p>Boyut ya da kütle TEK BAŞINA karar vermez — kendi denemende bunu gözledin. Oranı hesapla: 'Gözleminin adı: yoğunluk' ekranındaki formüle dön.</p>" } },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Denetim izi: skorlu tek ekran (`q_yogunluk`) → `evidence_screen_ids: ["kesif_yuzme",
"kesif_gozlem", "aciklama_yogunluk"]` — ÇOĞUL bağ, iki kanıt fazına birden
(`evidence_phases: [kesfet, acikla]`). `exploration` ekranları yapısal olarak skorsuzdur
(puan alanı YOK — Z3); transfer denemesi `points: 0`; skor yalnız `degerlendir` fazında.
`store_key`'ler kurs genelinde TEKİL olmalıdır (`validate_project` çakışmayı sert hatayla
keser). Lint-temiz tam fikstür: sunucu deposunda `examples/exploration-5e.tr.json`
(prediction + choice + text, geri oynatma + kanıt bağı).

## Literatür

- **Birincil:** Bybee, R. W., Taylor, J. A., Gardner, A., Van Scotter, P., Powell, J. C.,
  Westbrook, A., & Landes, N. (2006). *The BSCS 5E Instructional Model: Origins and
  Effectiveness.* Colorado Springs, CO: BSCS.
- Sınır koşulu (acemi ucu / rehbersiz keşif eleştirisi): Kirschner, P. A., Sweller, J., &
  Clark, R. E. (2006). *Why Minimal Guidance During Instruction Does Not Work.* Educational
  Psychologist, 41(2), 75–86. — bu paketin PK alt sınırının (3) gerekçesi.
