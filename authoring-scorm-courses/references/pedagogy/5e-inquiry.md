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
requires_platform: [exploration]
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
conflicts_with: [rosenshine-di]
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

**Platform şartı (`requires_platform: [exploration]`):** denetim bulgusu — mevcut 28 çekirdek
ekran tipi öğrenen girdisini SAKLAYIP sonraki ekranda geri oynatamıyor; oysa Explain'in gücü
"senin az önceki tahminin şuydu, gözlemin bunu gösterdi" atfındadır. `exploration` ekran tipi
(kemalyy/edumints-scorm-mcp F2 konusu) bu yeteneği sağlar. Yetenek platformda yoksa Katman 0
seçici bu paketi ELER (varsayılan platform varsayımı altında paket seçilemez — bilinçli beyan;
kâğıt-üstü 5E üretmek yerine paket kendini eletmeyi seçer).

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `merak` | Engage: çelişik durum + ön-kavramları yüzeye çıkarma | content_slide, video, image_compare, data_chart, poll, lottie | ✗ |
| `kesfet` | Explore: skorsuz kurcalama; öğrenen çıktısı saklanır — **kanıt 1** | exploration*, simulation, image_compare, data_chart | ✗ |
| `acikla` | Explain: kanonik açıklama, keşif çıktısına atıfla — **kanıt 2** | content_slide, accordion, tabs, timeline, video, data_chart | ✗ |
| `derinlestir` | Elaborate: yeni bağlama skorsuz transfer | mcq, drag_drop, matching, sorting, simulation, decision_scenario, branching | ✗ |
| `degerlendir` | Evaluate: skorlu ölçüm | hepsi | ✓ |

\* `exploration` = `requires_platform` beyanındaki F2 tipi (çekirdek 28'in dışında; paket ancak
bu yetenek varken seçilebilir olduğundan listede yer alır). Diğer adlar çekirdek 28'dendir.

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

    // ── FAZ kesfet (Explore — KANIT 1: öğrenenin KENDİ tahmin/gözlem çıktısı; exploration = F2 tipi) ──
    { "type": "exploration", "id": "kesif_yuzme", "title": "Dene: kütleyi ve hacmi değiştir", "points": 0,
      "prompt_html": "<p>Sanal küpün kütlesini ve hacmini ayrı ayrı değiştir, suya bırak, ne olduğunu kaydet. Önce TAHMİN et, sonra dene — tahminlerin saklanacak ve birazdan karşına gelecek.</p>",
      // F2 sözleşmesi: öğrenen girdisi (tahmin + deneme kaydı) saklanır ve sonraki ekranlarda
      // {{exploration:kesif_yuzme.*}} ile geri oynatılır (kemalyy/edumints-scorm-mcp F2)
      "trials": [
        { "id": "t1", "setup_html": "<p>Kütle 2×, hacim sabit → tahminin?</p>", "options": ["yüzer", "batar"] },
        { "id": "t2", "setup_html": "<p>Kütle sabit, hacim 2× → tahminin?</p>", "options": ["yüzer", "batar"] } ] },

    // ── FAZ acikla (Explain — KANIT 2: kanonik açıklama, keşif çıktısına AÇIK atıfla) ──
    { "type": "content_slide", "id": "aciklama_yogunluk", "title": "Gözleminin adı: yoğunluk",
      "blocks": [
        { "html": "<p>İlk tahminin şuydu: <b>{{exploration:kesif_yuzme.t1}}</b>. Denemede gördün: kütle tek başına sonucu belirlemedi — hacmi büyüttüğünde AYNI kütle yüzdü.</p>" },
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
      "evidence_screen_ids": ["kesif_yuzme", "aciklama_yogunluk"],  // E1 — kanıt: keşif çıktısı + kanonik açıklama (evidence_phases: [kesfet, acikla])
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
"aciklama_yogunluk"]` — ÇOĞUL bağ, iki kanıt fazına birden (`evidence_phases: [kesfet, acikla]`).
Keşif ve transfer denemeleri `points: 0` (Z3); skor yalnız `degerlendir` fazında.

## Literatür

- **Birincil:** Bybee, R. W., Taylor, J. A., Gardner, A., Van Scotter, P., Powell, J. C.,
  Westbrook, A., & Landes, N. (2006). *The BSCS 5E Instructional Model: Origins and
  Effectiveness.* Colorado Springs, CO: BSCS.
- Sınır koşulu (acemi ucu / rehbersiz keşif eleştirisi): Kirschner, P. A., Sweller, J., &
  Clark, R. E. (2006). *Why Minimal Guidance During Instruction Does Not Work.* Educational
  Psychologist, 41(2), 75–86. — bu paketin PK alt sınırının (3) gerekçesi.
