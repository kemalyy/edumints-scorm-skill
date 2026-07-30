---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — researchgate.net/publication/235701029 +
# simplypsychology.org/learning-kolb.html + torontomu.ca EL kaydı): Kolb, D. A. (1984).
# "Experiential Learning: Experience as the Source of Learning and Development." Englewood
# Cliffs, NJ: Prentice-Hall. — "Öğrenme, deneyimin dönüştürülmesiyle bilgi üretme sürecidir."
# Dört evre (DOĞRULANDI): Concrete Experience (somut deneyim) → Reflective Observation
# (yansıtıcı gözlem) → Abstract Conceptualization (soyut kavramsallaştırma) → Active
# Experimentation (aktif deneme) — döngü aktif denemeden yeni somut deneyime sarmallanır.
pack: kolb-experiential
name: "Kolb Deneyimsel Öğrenme Döngüsü"
version: 1
outcome_types: [tutum, ilke]
prior_knowledge: [1, 10]
error_cost: [düşük, orta, yüksek]
requires_platform: []
phases:
  - id: somut_deneyim
    amac: "Concrete Experience — öğrenen, sonuçlarını HİSSETTİREN bir senaryoyu bizzat yaşar (karar + bedeli); deneyim çıktısı kursun 1. kanıt kaynağıdır."
    izinli_ekran_tipleri: [decision_scenario, branching, simulation, game, video, content_slide]
    skorlanabilir: false
  - id: yansitici_gozlem
    amac: "Reflective Observation — deneyim skorsuz, açık uçlu yansıtılır ('ne oldu, ne hissettim, neden öyle seçtim'); yansıtma metni SAKLANIR ve sonraki fazlar ona atıf yapar."
    izinli_ekran_tipleri: [exploration, poll, content_slide]
    skorlanabilir: false
  - id: soyut_kavramsallastirma
    amac: "Abstract Conceptualization — deneyim ve yansıtmadan kanonik çerçeve/ilke çıkarılır; çerçeve deneyime AÇIK atıfla kurulur (2. kanıt kaynağı)."
    izinli_ekran_tipleri: [content_slide, tabs, accordion, data_chart, timeline, worked_example]
    skorlanabilir: false
  - id: aktif_deneme
    amac: "Active Experimentation — çerçeve YENİ senaryoda skorlu denenir; ölçülen şey bilgi beyanı değil DAVRANIŞ SEÇİMİDİR (tutumun davranışsal kanıtı)."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [somut_deneyim, soyut_kavramsallastirma]
scoring_allowed_from: aktif_deneme
conflicts_with: []
---

# kolb-experiential — Kolb Deneyimsel Öğrenme Döngüsü (C8)

**Ne:** Deneyim-önce döngü yöntemi: öğrenen önce bir durumu **yaşar** (somut deneyim), yaşadığını
**yansıtır** (yansıtıcı gözlem), yansıtmadan **kavramsal çerçeve** çıkarılır (soyut
kavramsallaştırma) ve çerçeve **yeni durumda denenir** (aktif deneme). **Ne zaman:** birincil
rota TUTUM kazanımlarıdır (seçici eşlemesi: `kolb-experiential` + `arcs` kaplaması) — tutum
kursları bugün "iddia + quiz" zincirine düşüyor; bu paket tutumu **davranışsal kanıta** bağlar:
öğrenen doğru cümleyi seçmekle değil, sonuçlu bir senaryoda davranışı SEÇMEKLE ölçülür. İkincil
rota deneyimden çıkarılabilen İLKE kazanımlarıdır ("neden-sonucu yaşayarak gör").

**Kanıt beyanı (Katman 1 bağlantısı — ÇOĞUL):** `evidence_phases: [somut_deneyim,
soyut_kavramsallastirma]`. Kanıt iki kaynaktan gelir: (1) deneyim senaryosunun ürettiği
gözlemlenebilir sonuç — öğrenenin kararları ve bedelleri (K1 türü 3: simülasyon/deneme çıktısı),
(2) o deneyime açık atıfla kurulan kanonik çerçeve (K1 türü 1). `yansitici_gozlem` bilinçli
olarak kanıt fazı DEĞİLDİR: yansıtma kişisel ve serbest metindir, skorlu sorunun cevabı ondan
türetilemez (K2 denetimi anlamsızlaşır) — rolü köprüdür, kaynak değil. Skorlu sorular
`evidence_screen_ids` (ÇOĞUL — scorm-mcp CONTRACTS §1.3 E1) ile deneyim + çerçeve ekranlarına
birden bağlanır.

**PK ve hata maliyeti kısıtlarının GENİŞ olmasının gerekçesi:** `prior_knowledge: [1, 10]` —
deneyim fazı çalışma malzemesini KURSUN KENDİSİ üretir (önbilgi şartı koymaz; akıcı öğrenen de
senaryonun bedelini yaşar), bu yüzden PK bu pakette eleme değil DOZ girdisidir
(`expertise-adaptive` kaplaması ipucu/atlama yollarını ayarlar). `error_cost: [düşük, orta,
yüksek]` — deneyim SİMÜLE edilir (decision_scenario/branching/game): saha bedeli kursa taşınmaz,
tersine yüksek-bedelli alanlarda "bedeli güvenli ortamda yaşat" tam bu paketin işidir; tutum
kazanımında gösterim-önce bir alternatif zaten yoktur (tutum anlatımla değişmez).

**Platform şartı: YOK (`requires_platform: []`).** Somut deneyim çekirdek tiplerle kurulur
(decision_scenario en doğal taşıyıcı). `exploration` (F2) yansıtma fazının TERCİH edilen
taşıyıcısıdır: `input_kind: "text"` yansıtma notunu `store_key` altında saklar,
`soyut_kavramsallastirma` ve `aktif_deneme` ekranları `<span data-exploration-ref>` ile birebir
geri oynatır ("kendi yansıtmanda şunu yazmıştın…" atfı gerçek olur). F2'siz hedefte `poll`
(açık metin, skorsuz) yedektir — yansıtma yine yapılır ama geri oynatılamaz; paket kurulabilir
kaldığı için beyan boştur.

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `somut_deneyim` | Sonuçlu senaryoyu BİZZAT yaşamak — **kanıt 1** | decision_scenario, branching, simulation, game, video, content_slide | ✗ |
| `yansitici_gozlem` | Açık uçlu, skorsuz yansıtma (köprü — kanıt fazı DEĞİL) | exploration* (tercih), poll, content_slide | ✗ |
| `soyut_kavramsallastirma` | Deneyime atıflı kanonik çerçeve — **kanıt 2** | content_slide, tabs, accordion, data_chart, timeline, worked_example | ✗ |
| `aktif_deneme` | YENİ senaryoda skorlu davranış seçimi | hepsi | ✓ |

\* `exploration` = F2 tipi (YAYINDA): yansıtma metni `store_key` ile saklanır ve sonraki
fazlarda geri oynatılır; yapısal skorsuz (puan alanı YOK — yansıtmayı puanlamak onu anket
cevabına çevirir, Z3).

Faz notları:

- **`somut_deneyim` ANLATIM değildir:** "iş güvenliği önemlidir" slaytı deneyim değildir.
  Deneyim = öğrenenin KARAR verdiği ve kararın BEDELİNİ gördüğü durum (decision_scenario'nun
  `score_delta`'sız kullanılamadığı yerde `branching` + sonuç ekranları). Bu fazda karar
  PUANLANMAZ (Z3): bedel anlatı içinde yaşanır, LMS puanına yazılmaz — puanlanan davranış
  ancak döngü tamamlandıktan sonra (`aktif_deneme`) ölçülür.
- **`yansitici_gozlem` yönlendirilmiş ama açık uçludur:** iyi yansıtma istemi üç soruyu birden
  taşır — ne oldu (betimleme), ne hissettin (duygu), neden öyle seçtin (atıf). Şıklı soruya
  indirgenmiş "yansıtma" gözlem değil yoklamadır.
- **`soyut_kavramsallastirma` deneyimden KOPUK teori dersi olamaz:** her çerçeve öğesi,
  deneyimin bir anına ya da yansıtmanın bir cümlesine bağlanır ("ikinci düğümde hız uğruna
  kontrolü atladın — bunun adı…"). Kopuk çerçeve, paketi gizli bir anlatım kursuna çevirir.
- **`aktif_deneme` YENİ senaryodur, aynı senaryonun tekrarı değil:** aynı senaryoyu tekrar
  oynatmak ezber ölçer; çerçevenin taşınması ancak yeni bağlamda görünür. Ölçülen şey davranış
  SEÇİMİdir; sorunun kanıt bağı deneyim + çerçeve ekranlarına ÇOĞUL kurulur.
- **Döngü SARMALDIR:** Kolb'da aktif deneme yeni somut deneyime açılır. Tek mikrokurs döngüyü
  BİR kez kapatır; sarmalın devamı kurs dizisinin işidir (bir sonraki modül, önceki modülün
  aktif-deneme senaryosunu somut deneyim olarak devralır). Fazları tek kursta iki kez döndürmek
  bütçeyi taşırır — bölmek daha dürüsttür.
- **`arcs` kaplaması doğal eştir (seçici örnek 5):** İlgililik (deneyimin öğrenenin dünyasından
  seçilmesi) ve Duyu-Doyum dokunuşları bu paketle sinerjiktir — kaplama D3 işidir, burada yalnız
  eşleme notu (bu paket kaplama uygulamaz).

## Bu paket NE ZAMAN seçilmemeli

- **Prosedür / olgu kazanımları:** `outcome_types` dışıdır — adım icrası ya da olgu kalıcılığı
  için döngü gereksiz maliyettir (`rosenshine-di`, `retrieval-spaced`; akıcı icra için
  `sim-drill`).
- **Çok dar zaman bütçesi (≤ 5 dk):** dört evre sığmaz; en sık kırpılan evre yansıtmadır ve
  yansıtmasız Kolb, pahalı bir senaryo-quizidir — dürüst seçim `decision_scenario`'lu tek fazlı
  bir tasarımdır (paketsiz) ya da başka pakettir.
- **Deneyim senaryosu kurulamıyorsa** (alan soyut, karar-bedel ilişkisi gösterilemiyor):
  yaşanmayan "deneyim" anlatımdır; `merrill-fpi` (görev-merkezli) ya da `5e-inquiry` düşün.
- **Kavram sınıflama kazanımları** (yeni örneği X'tir/değildir diye ayırt etme): keşif +
  kanonik açıklama daha ekonomiktir (`5e-inquiry` / `productive-failure`); Kolb'un katma değeri
  duygu ve değer bileşeni olan kazanımlardadır.

## Çakışmalar (`conflicts_with`)

Boş — bilinen hedef-düzeyi çakışma yok. Gerekçe: tutum kazanımında bu paketle yarışan diğer
paket yoktur (`outcome_types` kesişimi zaten boş — rosenshine-di/merrill-fpi/4cid tutumu
kapsamaz, kesişen tek tür `ilke`dir ve orada ilişki çakışma değil gerekçeli alternatifliktir:
neden-sonucu YAŞATMAK isteniyorsa kolb-experiential, göstermek yetiyorsa rosenshine-di /
`5e-inquiry`). `arcs` bir kaplamadır ve çatışmaz, eştir (yukarıdaki not).

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: tutum · PK: 3 · hata maliyeti: yüksek): *"Zaman baskısı altında bile
yüksekte çalışma öncesi emniyet kontrolünü yapmayı seçer."* Kitle: saha teknisyenleri; bilgi
zaten var ("kemer takılır" herkes bilir — K2 bunu sormayı yasaklar), eksik olan DAVRANIŞ SEÇİMİ.

```jsonc
{
  "title": "İki Dakika: Yüksekte Çalışmada Emniyet Kararı",
  "description": "Deneyimsel döngü mikrokursu — kolb-experiential",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "screens": [
    { "type": "title_slide", "title": "İki Dakika", "subtitle": "8 dk · önce yaşayacaksın, sonra karar vereceksin" },

    // ── FAZ somut_deneyim (KANIT 1: karar + bedel, anlatı içinde — LMS puanına yazılmaz) ──
    { "type": "branching", "id": "deneyim_vardiya", "title": "Deneyim: 17:40, son iş emri",
      "prompt_html": "<p>Vardiyanın bitmesine 20 dk var; son iş emri çatı anteninde 10 dakikalık bir bağlantı kontrolü. Ekip lideri telsizde: <i>'Hallet gel, servis kalkıyor.'</i> Emniyet kontrolü (kemer + ankraj + zemin) ~5 dk. Ne yapıyorsun?</p>",
      "choices": [
        { "id": "atla", "text_html": "Kontrolü atla — 10 dakikalık iş, hep yaptım", "goto_screen_id": "sonuc_atla" },
        { "id": "yap", "text_html": "Kontrolü yap — servis beklesin", "goto_screen_id": "sonuc_yap" } ] },
    { "type": "content_slide", "id": "sonuc_atla", "title": "18:02 — olay tutanağı",
      "body_html": "<p>Ankraj noktasındaki karabina, önceki ekipten gevşek kalmıştı. Dengeni kaybettiğin anda kemer yükü almadı; korkuluğa tutunarak kurtuldun. Tutanağa 'ramak kala' yazıldı — bugün şanstı. Kontrolün atlanan 5 dakikası, karabinayı görecek TEK andı.</p>" },
    { "type": "content_slide", "id": "sonuc_yap", "title": "17:46 — kontrol bulgusu",
      "body_html": "<p>Kontrolde ankraj karabinasının önceki ekipten gevşek kaldığını gördün; 30 saniyede kilitledin. İş 18:00'de bitti, servis 6 dk bekledi. O karabina, kontrol atlanmış olsaydı yükü almayacaktı — bunu yalnız kontrol gösterebilirdi.</p>" },

    // ── FAZ yansitici_gozlem (skorsuz, açık uçlu; SAKLANIR — F2 tercihi; kanıt fazı DEĞİL) ──
    { "type": "exploration", "id": "yansitma", "title": "Dur ve yaz: kararın anatomisi",
      "input_kind": "text", "store_key": "kolb_yansitma", "min_length": 40,
      "placeholder": "Seçerken aklımdan geçen… beni asıl iten şey… şimdi fark ettiğim…",
      "prompt_html": "<p>Üç soruyu kendi cümlelerinle cevapla: (1) Ne oldu? (2) Karar anında ne hissettin — asıl baskı neydi? (3) Neden öyle seçtin? Notun saklanacak; çerçeve ekranında karşına gelecek. Puan yok, doğru cevap yok.</p>" },

    // ── FAZ soyut_kavramsallastirma (KANIT 2: çerçeve, deneyime + yansıtmaya AÇIK atıfla) ──
    { "type": "content_slide", "id": "cerceve", "title": "Yaşadığının adı: risk normalleşmesi ve iki-dakika kuralı",
      "blocks": [
        { "html": "<p>Kendi yansıtman: <em><span data-exploration-ref=\"kolb_yansitma\"></span></em>. Karar anında hissettiğin baskının adı var: <b>üretim baskısı</b> ('servis kalkıyor') ve <b>risk normalleşmesi</b> ('hep yaptım, bir şey olmadı') — 'bir şey olmaması', kontrolün gereksizliğini değil şansın sürdüğünü gösterir; senaryoda gevşek karabinayı görecek tek an kontroldü.</p>" },
        { "html": "<p>Çerçeve: karar anında iki soruyu sırala — <b>(1) bu gecikmenin bedeli ne?</b> (dakika cinsinden, geri alınabilir) · <b>(2) atlamanın bedeli ne?</b> (geri alınamaz). İkisi aynı birimde değilse — biri dakika, öteki hayat — kıyas bitmiştir: kontrol yapılır. Buna 'iki-dakika kuralı' de: bedeli dakika olan taraf HER ZAMAN bekleyebilir.</p>" } ] },

    // ── FAZ aktif_deneme (SKORLU: YENİ senaryoda davranış seçimi; kanıt bağı ÇOĞUL) ──
    { "type": "decision_scenario", "id": "q_yeni_senaryo", "title": "Skorlu: yeni durum, aynı karar anı", "points": 100, "pass_score": 60,
      "evidence_screen_ids": ["deneyim_vardiya", "sonuc_atla", "sonuc_yap", "cerceve"],  // E1 — ÇOĞUL bağ: deneyim (kanıt 1) + çerçeve (kanıt 2)
      "intro_html": "<p>Farklı gün, farklı baskı: müşteri sahada bekliyor, yağmur başlamak üzere, iskelede 15 dakikalık pano montajı var. Kararlar senin.</p>",
      "nodes": [
        { "id": "n1", "prompt_html": "<p>Müşteri saatine bakıyor. İlk hamlen?</p>", "choices": [
            { "id": "a", "text_html": "İki soruyu sırala: gecikmenin bedeli dakika, atlamanınki geri alınamaz — kontrolü yap", "feedback_html": "<p>Çerçevenin ilk deneyimindeki karşılığını hatırla: bedeli dakika olan taraf bekleyebilir.</p>", "score_delta": 60, "goto_node_id": "n2" },
            { "id": "b", "text_html": "Bu iş kısa ve müşteri bekliyor — çık, panoyu bağla", "feedback_html": "<p>Karar anındaki baskı ilk senaryodakiyle aynı yapıda — o gün bedeli kimin ödediğini olay tutanağı ekranından yeniden oku.</p>", "score_delta": -20, "goto_node_id": "n2" } ] },
        { "id": "n2", "prompt_html": "<p>Ekip arkadaşın 'ben kontrolsüz çıkıyorum, sen raporla' diyor. Ne yaparsın?</p>", "choices": [
            { "id": "c", "text_html": "Durdur — iki-soru kıyasını ona da uygula ve kontrolü birlikte yapın", "feedback_html": "<p>Tutum davranışta görünür: kural kendine uygulandığında değil, bedeli başkası öderken de savunulduğunda oturmuştur.</p>", "score_delta": 40, "goto_node_id": null },
            { "id": "d", "text_html": "Karışma — herkes kendi kararından sorumlu", "feedback_html": "<p>İlk senaryodaki gevşek karabina kimin kararıydı? Bedel, kararı verenle sınırlı kalmıyor — çerçeve ekranındaki kıyası hatırla.</p>", "score_delta": -10, "goto_node_id": null } ] } ] },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Denetim izi: skorlu tek ekran (`q_yeni_senaryo`) → `evidence_screen_ids: ["deneyim_vardiya",
"sonuc_atla", "sonuc_yap", "cerceve"]` — ÇOĞUL bağ, iki kanıt fazına birden (`evidence_phases:
[somut_deneyim, soyut_kavramsallastirma]`); ölçülen şey bilgi değil YENİ senaryoda davranış
seçimi. Deneyim kararı puanlanmadı (branching `set_vars`'sız — bedel anlatıda yaşandı, Z3);
yansıtma yapısal skorsuz (`exploration`, kanıt fazı DEĞİL — köprü); çerçeve ekranı yansıtmayı
`data-exploration-ref` ile geri oynatır. Feedback metinleri cevabı yeniden kurmaz, kanıt
ekranına geri işaret eder (G3/K5).

## Literatür

- **Birincil:** Kolb, D. A. (1984). *Experiential Learning: Experience as the Source of
  Learning and Development.* Englewood Cliffs, NJ: Prentice-Hall. — dört evre + "öğrenme,
  deneyimin dönüştürülmesiyle bilgi üretme sürecidir" tanımı; 2. baskı: Kolb (2015),
  Pearson Education.
- Döngünün kökleri: Dewey (deneyim-eğitim bağı), Lewin (eylem-araştırma döngüsü), Piaget
  (özümseme/uyum) — Kolb (1984) 2. bölümün kendi soykütüğü.
- Eleştirel sınır (öğrenme-stilleri AYRI iddiadır): Kolb'un LSI stil envanteri bu paketin
  DIŞINDADIR — stil-eşleme hipotezinin görgül desteği zayıftır (Pashler, McDaniel, Rohrer &
  Bjork, 2008, *Learning Styles: Concepts and Evidence*); paket yalnız DÖNGÜYÜ kullanır,
  öğrenene stil etiketi yapıştırmaz.
