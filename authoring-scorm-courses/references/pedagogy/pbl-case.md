---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — Wiley 10.1111/j.1365-2923.1986.tb01386.x +
# semanticscholar kaydı): Barrows, H. S. (1986). "A Taxonomy of Problem-Based Learning Methods."
# Medical Education, 20(6), 481–486. — "PBL" tek bir yöntem değildir; taksonominin ayırıcı
# değişkenleri problem biçimi ve öğrenen-yönlendirmesi derecesidir (vaka-anlatımından tam
# problem-temelli / kapalı-döngü tasarıma). Bu paket taksonomiden "problem-önce + öğrenen-analizli"
# ucu alır: problem/vaka ÖNCE gelir, öğrenme ihtiyacını vaka tanımlar. Kök: Barrows & Tamblyn
# (1980), Problem-Based Learning: An Approach to Medical Education. Springer.
pack: pbl-case
name: "Vaka/Problem Temelli Öğrenme (Barrows)"
version: 1
outcome_types: [problem çözme, ilke]
prior_knowledge: [6, 10]
error_cost: [düşük, orta, yüksek]
requires_platform: []
phases:
  - id: vaka_dosyasi
    amac: "Vaka dosyası — kursun KENDİSİNİN inşa ettiği zengin artefakt ailesi (belgeler, zaman çizelgesi, veriler, yazışmalar) + bütün-vaka sürükleyici soru sunulur (kanıt ailesi 1)."
    izinli_ekran_tipleri: [content_slide, timeline, data_chart, accordion, tabs, image_compare, hotspot, video]
    skorlanabilir: false
  - id: problem_tanimlama
    amac: "Sürükleyici soru karşısında problem skorsuz tanımlanır: bilinenler, bilinmeyenler, hipotezler, öğrenme ihtiyaçları — cevap değil ÇERÇEVE üretilir."
    izinli_ekran_tipleri: [exploration, poll, mcq, true_false, content_slide]
    skorlanabilir: false
  - id: analiz_arastirma
    amac: "Dosya derinleştirilir: sorgulama ilerledikçe EK vaka belgeleri açılır (aşamalı ifşa — kanıt ailesi 2) ve hipotezler dosyaya karşı skorsuz sınanır."
    izinli_ekran_tipleri: [accordion, tabs, data_chart, timeline, hotspot, branching, mcq, fill_blank, drag_drop, matching]
    skorlanabilir: false
  - id: cozum_onerisi
    amac: "Vaka kararı verilir: kanonun/alan bilgisinin VAKA ARTEFAKTINA uygulanması skorlu ölçülür (kanon-alan kuralı: cevabın kritik parçası dosyadan gelir)."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
  - id: karsilastirma_genelleme
    amac: "Verilen karar uzman yaklaşımıyla karşılaştırılır ve vaka-ötesi ilkeye genellenir; transfer soruları skorlu olabilir."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [vaka_dosyasi, analiz_arastirma]
scoring_allowed_from: cozum_onerisi
conflicts_with: []
---

# pbl-case — Vaka/Problem Temelli Öğrenme (C7)

**Ne:** Problem-önce yöntem: öğretim bir konu anlatımıyla değil, zengin ve gerçekçi bir **vaka
dosyasıyla** açılır; öğrenme ihtiyacını vaka tanımlar, içerik o ihtiyaca cevaben (ve kısmen
öğrenenin sorgulamasıyla) açılır. **Ne zaman:** problem çözme / ilke kazanımları + YÜKSEK önbilgi
(PK 6–10 — seçici eşlemesi: `pbl-case` + `expertise-adaptive` kaplaması): akıcı öğrenene çözümlü
örnek dozu uzmanlık-tersinme maliyeti üretir, gerçekçi vaka problem-önce çalışır.

**Kanıt beyanı (Katman 1 bağlantısı — ÇOĞUL) — bu paketin varlık sebebi:** `evidence_phases:
[vaka_dosyasi, analiz_arastirma]`. Kanıt kaynağı **VAKA DOSYASININ KENDİSİDİR** (K1 türü 4 —
artefakt ailesi): açılış dosyası (`vaka_dosyasi`) + sorgulamayla aşamalı açılan ek belgeler
(`analiz_arastirma`). Bu tasarım, amiral-gemisi slop bulgusunun ("cevabı hiçbir yerde
öğretilmeyen soru") yapısal panzehiridir: **skorlu her soru vaka dosyasına bağlanmak
ZORUNDADIR** — cevabın kritik olgusu (damga, tutar, satır, cümle) yalnız dosya ekranlarında
yaşar (K4), soru gövdesi dosyaya atıf yapar, değerini kopyalamaz. Skorlu sorular
`evidence_screen_ids` (ÇOĞUL — scorm-mcp CONTRACTS §1.3 E1) ile dosyanın birden çok parçasına
birden bağlanabilir; iyi vaka sorusu zaten çoğu zaman İKİ belgeyi çapraz okutur.

**Kanon-alan kuralı bu paketin yerlisidir** (`core/evidence-binding.md` son bölüm): PK 6–10
kitlesi alan kanonunu zaten bilir, bu yüzden K2 denetimi ("kursu görmemiş uzman cevaplar mı?")
kanon-hatırlama sorularını acımasızca eler. Bu pakette skorlu soru DAİMA
**"kural nedir?" değil "dosyadaki ŞU artefakta göre kural neyi gerektirir?"** biçimindedir —
dönüştürme kalıbı ve ÖNCE/SONRA çiftleri evidence-binding'dedir.

**Platform şartı: YOK (`requires_platform: []`).** Vaka dosyası mevcut çekirdek tiplerle kurulur:
`content_slide` (blocks) belgeler, `timeline` olay örgüsü, `data_chart` sayısal kanıt, `accordion`
dosya gözleri (tutanaklar, e-postalar, kayıtlar), `hotspot` belge üzerinde inceleme. `exploration`
(F2) problem-tanımlama notu için TERCİH edilen iyileştirmedir (hipotez saklanır,
`karsilastirma_genelleme` geri oynatır) ama ön koşul değildir — F2'siz hedefte `poll`/points-0
yoklama aynı işi dolaylı görür.

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `vaka_dosyasi` | Dosyanın açılışı + bütün-vaka sürükleyici soru — **kanıt ailesi 1** | content_slide, timeline, data_chart, accordion, tabs, image_compare, hotspot, video | ✗ |
| `problem_tanimlama` | Bilinen/bilinmeyen/hipotez çerçevesi (skorsuz) | exploration (tercih), poll, mcq/true_false (points 0), content_slide | ✗ |
| `analiz_arastirma` | Aşamalı ifşa: ek belgeler + hipotez sınama — **kanıt ailesi 2** | accordion, tabs, data_chart, timeline, hotspot, branching, mcq, fill_blank, drag_drop, matching (hepsi points 0) | ✗ |
| `cozum_onerisi` | Vaka kararı — kanonun ARTEFAKTA uygulanması (skorlu) | hepsi | ✓ |
| `karsilastirma_genelleme` | Uzman karşılaştırması + vaka-ötesi ilke; transfer (skorlu olabilir) | hepsi | ✓ |

Faz notları:

- **Sürükleyici soru BÜTÜN-VAKADIR, ekran-başı quiz değil:** dosya açılışında tek bir soru
  ortaya konur ("Bu fire artışının kök nedeni ne ve yarın sabah ne yapmalı?") ve kursun bütün
  skorlu kararları bu sorunun parçalarıdır. Sorusuz vaka, süslü bir anlatımdır.
- **Vaka dosyası TUTARLI bir mikro-evrendir:** tarihler, tutarlar, adlar belgeler arasında
  birbirini doğrular (çapraz okuma soruları ancak böyle kurulabilir). Belgeler gerçekçi türde
  yazılır: tutanak tutanak gibi, e-posta e-posta gibi kokar — vaka gerçekçiliği bu paketin
  motivasyon motorudur.
- **Aşamalı ifşa gerçek PBL sorgusudur (Barrows'un serbest-sorgu ucu):** her şey ilk ekranda
  verilmez; `analiz_arastirma` fazında ek belgeler (accordion gözleri, yeni çizelge satırları)
  öğrenenin hipotez sınamasına cevaben açılır. `branching` "hangi belgeyi istersin?" seçimini
  taşıyabilir — ama TÜM yollar aynı zorunlu kanıt kümesinden geçmelidir (görmediği belgeden
  soru sorulmaz; Z2).
- **`problem_tanimlama` ve `analiz_arastirma` skorSUZdur (Z3):** hipotez kurma ve sınama
  deneme-güvenlidir; yanlış hipotez değerli malzemedir (`karsilastirma_genelleme` ona atıf
  yapar). Skor ancak dosya kanıtı TAMAMLANDIKTAN sonra girer (`scoring_allowed_from:
  cozum_onerisi`).
- **`karsilastirma_genelleme` cevap SIZDIRMAZ (K5/K6):** uzman karşılaştırması, skorlu vaka
  kararlarının doğru cevabını yeniden söyleyemez — karar noktalarını kavram düzeyinde adlandırır
  ve vaka-ötesi ilkeyi YENİ bir mini-duruma taşır; transfer sorusunun yeni-durum olgusu da
  gövdeye değil bir artefakt ekranına konur (K4 transfer kuralı).

## Bu paket NE ZAMAN seçilmemeli

- **Düşük/orta önbilgi (PK &lt; 6 — sert kısıt):** vaka zengindir ve zenginlik acemiye
  GÜRÜLTÜDÜR — şeması olmayan öğrenen dosyada kaybolur, ilgisiz ayrıntıyı sinyal sanır. Önce
  `rosenshine-di`/`4cid` ile temel kur; vakayı dizinin son modülüne koy.
- **Olgu ezberi kazanımları:** `outcome_types` dışıdır — tekil olgular için vaka iskeleti
  gereksiz ağırlıktır (`retrieval-spaced` seç).
- **Tek-doğru-yollu kısa prosedürler:** vaka analizi açık uçlu karar ister; sabit akışın
  ölçümü için `rosenshine-di` / `sim-drill` doğru araçtır.
- **Dar zaman bütçesi (≤ 5 dk):** tutarlı bir dosya + sorgu + karar sığmaz; kırpılmış "mini
  vaka anlatımı" PBL değildir (o zaman `merrill-fpi`'nin görev-tanıtımı yeter).
- **Vaka kurulamıyorsa** (gerçekçi belge/veri üretilemiyor, alan soyut): dosyasız PBL, adı
  değişmiş bir soru bankasıdır — dürüst seçim başka pakettir.

## Çakışmalar (`conflicts_with`)

Boş — bilinen hedef-düzeyi çakışma yok. Gerekçe: sıra-felsefesi zıtlığı taşıyan adaylar
(`rosenshine-di`, `4cid` — gösterim-önce) bu paketle AYNI HEDEFTE zaten yarışamaz: PK aralıkları
ayrıktır (`pbl-case` 6–10; rosenshine-di 1–5, 4cid 1–6), Katman 0'ın sert kısıt elemesi ikisini
aynı hedefte hayatta bırakmaz — beyan edilecek gerçek bir çakışma senaryosu kalmaz (çakışma
beyanı eleme-sonrası birlikte SAĞ KALANLAR için anlamlıdır). `productive-failure` ile ilişki
akrabalıktır, çakışma değil: ikisi de problem-önce ailesindendir; hakem kazanım türü + PK'dır
(kavram inşası + orta PK → PF; stratejik karar + yüksek PK → pbl-case). `merrill-fpi` ile fark
ölçek ve yöndür (görev-merkezli gösterim-önce ↔ vaka-merkezli problem-önce) — seçici notu.

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: problem çözme · PK: 7 · hata maliyeti: orta): *"Üretim hattındaki fire
artışının kök nedenini vaka dosyasından teşhis eder ve düzeltici eylemi gerekçelendirir."*
Kitle: deneyimli üretim mühendisleri/vardiya amirleri (kök-neden metodolojisini bilirler —
kanon-alan: soru metodolojiyi değil DOSYAYA uygulanmasını ölçer).

```jsonc
{
  "title": "Fire Neden İkiye Katlandı? — Vaka Dosyası",
  "description": "Vaka temelli mikrokurs — pbl-case",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "screens": [
    { "type": "title_slide", "title": "Fire Neden İkiye Katlandı?", "subtitle": "10 dk · dosya masada — kararı sen vereceksin" },

    // ── FAZ vaka_dosyasi (KANIT AİLESİ 1: çizelge + veri + tutanak; bütün-vaka sürükleyici soru) ──
    { "type": "content_slide", "id": "dosya_kapak", "title": "Dosya: B2 hattı fire artışı",
      "body_html": "<p>Sürükleyici soru: <b>B2 hattında fire oranı üç haftada neden yaklaşık ikiye katlandı ve yarın sabahki vardiyadan önce hangi düzeltici eylem alınmalı?</b> Aşağıdaki belgeler gerçek kayıtlardan derlendi; karar bu dosyadan çıkacak.</p>" },
    { "type": "timeline", "id": "dosya_cizelge", "title": "Belge 1 — Olay çizelgesi (son 4 hafta)",
      "events": [
        { "date": "Hafta 1", "title": "Referans dönem", "body_html": "<p>Fire %2,1. Planlı bakım tamamlandı (kalıp seti A).</p>" },
        { "date": "Hafta 2, Salı", "title": "Kalıp değişimi", "body_html": "<p>Kalıp seti A → yedek set C (A revizyona alındı). Devreye alma testi: 'uygun' — tek ölçümle.</p>" },
        { "date": "Hafta 2, Perşembe", "title": "Gece vardiyası notu", "body_html": "<p>Operatör kaydı: 'kenar çapağı arttı, ayar talebi iletildi'. Talep iş emri sistemine GİRİLMEMİŞ.</p>" },
        { "date": "Hafta 3–4", "title": "Fire tırmanışı", "body_html": "<p>Fire %2,1 → %4,3. Çapak kaynaklı ret, toplam retlerin %78'i.</p>" } ] },
    { "type": "data_chart", "id": "dosya_veri", "title": "Belge 2 — Ret nedenleri dağılımı (Hafta 3–4)", "chart_type": "bar",
      "data": [
        { "label": "Kenar çapağı", "value": 78 },
        { "label": "Ölçü sapması", "value": 12 },
        { "label": "Yüzey lekesi", "value": 7 },
        { "label": "Diğer", "value": 3 } ],
      "caption": "Ret nedeni başına pay (%) — kalite kayıtlarından" },

    // ── FAZ problem_tanimlama (skorsuz çerçeve; hipotez SAKLANIR — F2 tercihi) ──
    { "type": "exploration", "id": "hipotez_notu", "title": "İlk hipotezin",
      "input_kind": "text", "store_key": "pbl_hipotez", "min_length": 30,
      "placeholder": "Kök neden bence… çünkü çizelgede/veride…",
      "prompt_html": "<p>Dosyanın ilk iki belgesine göre: kök neden hipotezin ne, hangi belgeye dayanıyor ve neyi BİLMİYORSUN? Notun saklanacak — kapanışta uzman analiziyle karşılaştıracaksın.</p>" },

    // ── FAZ analiz_arastirma (KANIT AİLESİ 2: aşamalı ifşa — ek belgeler; hipotez sınama points 0) ──
    { "type": "accordion", "id": "dosya_ekler", "title": "Belge 3 — Sorgulamanın açtığı ekler",
      "items": [
        { "title": "Bakım kaydı: yedek set C", "body_html": "<p>Set C'nin son revizyonu 14 ay önce; öngörülen revizyon aralığı 6 ay. Devreye alma testinde tek parça ölçülmüş, seri ölçüm atlanmış.</p>" },
        { "title": "İş emri sistemi dökümü", "body_html": "<p>Hafta 2 Perşembe–Hafta 4 arası B2 için AÇIK ayar iş emri: 0. Operatör talebi sözlü kalmış; vardiya devir formunda da yok.</p>" },
        { "title": "Hammadde girişleri", "body_html": "<p>Aynı dönemde hammadde partisi değişmemiş; sertifika değerleri referans aralıkta.</p>" } ] },
    { "type": "mcq", "id": "hipotez_sinama", "title": "Hipotez sınama (puan yok)", "points": 0,
      "prompt_html": "<p>Ek belgeler hammadde hipotezini destekliyor mu?</p>",
      "options": [
        { "id": "a", "text_html": "Hayır — parti değişmemiş, sertifikalar aralıkta: bu hat elenir", "correct": true },
        { "id": "b", "text_html": "Evet — fire arttıysa hammadde mutlaka değişmiştir" } ],
      "feedback": {
        "correct_html": "<p>Doğru okuma — 'Hammadde girişleri' eki bu hipotezi kapatıyor; kalan izler kalıp ve iletişim hattında.</p>",
        "incorrect_html": "<p>'Hammadde girişleri' ekine geri dön: parti ve sertifika verisi ne diyor? Hipotez, belgeye yenilirse elenir.</p>" } },

    // ── FAZ cozum_onerisi (SKORLU — kanonun DOSYAYA uygulanması; kanıt bağı ÇOĞUL: çapraz belge okuma) ──
    { "type": "mcq", "id": "q_kokneden", "title": "Skorlu: kök neden teşhisi", "points": 40,
      "evidence_screen_ids": ["dosya_cizelge", "dosya_ekler"],  // E1 — çapraz okuma: çizelgedeki iki olay + ek belgelerin ikisi
      "prompt_html": "<p>Dosyaya göre fire artışının kök nedeni hangi ZİNCİRDİR? (Çizelgedeki olayları ve ek belgeleri çapraz oku.)</p>",
      "options": [
        { "id": "a", "text_html": "Revizyonu geçmiş yedek kalıbın eksik testle devreye alınması + ayar talebinin iş emrine dönüşmemesi", "correct": true },
        { "id": "b", "text_html": "Hammadde partisinin değişmesi + gece vardiyasının deneyimsizliği" },
        { "id": "c", "text_html": "Planlı bakımın gecikmesi + ölçü sapması retlerinin birikmesi" } ],
      "feedback": {
        "correct_html": "<p>Doğru zincir — iki belge birbirini doğruluyor: bakım kaydı (revizyon aşımı + tek ölçümlü test) ve iş emri dökümü (talep kaybolmuş). Tek neden değil, zincir.</p>",
        "incorrect_html": "<p>Elenen hipotezi taşıyorsun ya da çizelgeyle çelişiyorsun. 'Belge 3' eklerini çizelgenin Salı/Perşembe satırlarıyla yan yana koy.</p>" } },
    { "type": "decision_scenario", "id": "q_eylem", "title": "Skorlu: yarın sabahki eylem", "points": 40, "pass_score": 20,
      "evidence_screen_ids": ["dosya_cizelge", "dosya_veri", "dosya_ekler"],  // E1 — karar üç belgeye birden yaslanır
      "intro_html": "<p>Vardiya başlamadan karar senin. Dosyadaki kanıt zincirine göre hamleni seç.</p>",
      "nodes": [
        { "id": "n1", "prompt_html": "<p>İlk hamlen?</p>", "choices": [
            { "id": "a", "text_html": "Set C'yi seri ölçümlü devreye-alma testine al; ayar talebini iş emrine çevir", "feedback_html": "<p>Dosyanın gösterdiği iki kırık halkayı birden onarıyorsun: eksik test ve kaybolan talep.</p>", "score_delta": 25, "goto_node_id": "n2" },
            { "id": "b", "text_html": "Hattı durdurup A setinin revizyondan dönmesini bekle", "feedback_html": "<p>Aşırı tepki: dosyada set C'nin ayarla düzelemeyeceğine dair kanıt yok; üretim kaybı gerekçesiz.</p>", "score_delta": -10, "goto_node_id": "n2" } ] },
        { "id": "n2", "prompt_html": "<p>Sistemik önlem?</p>", "choices": [
            { "id": "c", "text_html": "Sözlü ayar taleplerini vardiya devrinde zorunlu iş-emri alanına bağla", "feedback_html": "<p>Perşembe notunun kaybolduğu deliği kapatır — vaka tekrarını engelleyen önlem budur.</p>", "score_delta": 15, "goto_node_id": null },
            { "id": "d", "text_html": "Gece vardiyasına ek kalite eğitimi planla", "feedback_html": "<p>Dosya operatörün HATASINI değil, talebinin kaybolduğunu gösteriyor — eğitim bu vakada yanlış hedef.</p>", "score_delta": -5, "goto_node_id": null } ] } ] },

    // ── FAZ karsilastirma_genelleme (uzman karşılaştırması + hipotez geri-oynatma + vaka-ötesi ilke; cevap sızdırmaz — K5) ──
    { "type": "content_slide", "id": "uzman_genelleme", "title": "Uzmanın okuma sırası ve vaka-ötesi ilke",
      "blocks": [
        { "html": "<p>Senin ilk hipotezin: <em><span data-exploration-ref=\"pbl_hipotez\"></span></em>. Uzman analizle karşılaştır: uzman önce NE DEĞİŞTİ sorusunu çizelgeye sorar, sonra her hipotezi bir BELGEYLE sınar ve belgeye yenilen hipotezi eler — senin sınadığın yolun aynısı.</p>" },
        { "html": "<p>Vaka-ötesi ilke: kök neden çoğu zaman tek olay değil, bir <b>değişiklik + kopan iletişim halkası</b> zinciridir; teşhisin gücü, hipotezi belgeyle sınama disiplinindedir. Bir sonraki vakanda aynı üç soruyla başla: ne değişti · kim bildirdi · kayıt nerede?</p>" } ] },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Denetim izi: iki skorlu ekran → `q_kokneden` `evidence_screen_ids: ["dosya_cizelge",
"dosya_ekler"]`, `q_eylem` `["dosya_cizelge", "dosya_veri", "dosya_ekler"]` — ÇOĞUL bağlar iki
kanıt fazına birden (`evidence_phases: [vaka_dosyasi, analiz_arastirma]`); kritik olgular
(revizyon aşımı, kayıp iş emri, %78 çapak payı) YALNIZ dosya ekranlarında yaşar, soru gövdeleri
atıf yapar (K4). Hipotez ekranı yapısal skorsuz (`exploration`); sınama `points: 0` (Z3); uzman
karşılaştırması skorlu kararların cevabını yeniden kurmaz (K5 — süreci adlandırır, zinciri
söylemez). `q_kokneden` ile `q_eylem` birbirinin cevabını sızdırmaz (K6: eylem düğümlerinin
gerekçeleri teşhis seçeneğinin metnini tekrarlamaz).

## Literatür

- **Birincil:** Barrows, H. S. (1986). *A Taxonomy of Problem-Based Learning Methods.* Medical
  Education, 20(6), 481–486. https://doi.org/10.1111/j.1365-2923.1986.tb01386.x
- Kök: Barrows, H. S., & Tamblyn, R. M. (1980). *Problem-Based Learning: An Approach to Medical
  Education.* New York: Springer — problem-önce sıranın ve serbest sorgunun ilk bütünlüklü sunumu.
- Sınır koşulu (acemi ucu): Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). *Why Minimal
  Guidance During Instruction Does Not Work.* Educational Psychologist, 41(2), 75–86 — PK alt
  sınırının (6) gerekçesi; PBL'nin yüksek-önbilgi ucundaki savunması için Schmidt vd. (2007),
  *Problem-Based Learning is Compatible with Human Cognitive Architecture.* Educational
  Psychologist, 42(2), 91–97.
