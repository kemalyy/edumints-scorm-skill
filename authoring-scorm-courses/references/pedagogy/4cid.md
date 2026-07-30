---
# Birincil kaynak (DOĞRULANDI, 2026-07-29 — Routledge/Springer kayıtları; 3. baskı 2018,
# 4. baskı 2024): van Merriënboer, J. J. G., & Kirschner, P. A. (2018). "Ten Steps to Complex
# Learning: A Systematic Approach to Four-Component Instructional Design" (3rd ed.). Routledge.
# — Dört bileşen: (1) öğrenme görevleri (basit→karmaşık TAM görevler, görev sınıfları),
# (2) destekleyici bilgi, (3) usul bilgisi (tam-zamanında), (4) parça-görev pratiği.
pack: 4cid
name: "4C/ID — Karmaşık Beceri Eğitimi (van Merriënboer)"
version: 1
outcome_types: [prosedür, problem çözme]
prior_knowledge: [1, 6]
error_cost: [düşük, orta, yüksek]
requires_platform: [worked_example]
phases:
  - id: gorev_tam_destek
    amac: "Görev sınıfı 1 — TAM görev, TAM destek: çözümlü örnek + destekleyici bilgi; öğrenen izler ve inceler (kanıt kaynağı 1)."
    izinli_ekran_tipleri: [worked_example, content_slide, video, timeline, accordion, tabs, image_compare]
    skorlanabilir: false
  - id: gorev_soluklastirma
    amac: "Ara görev sınıfları — destek adım adım SOLUKLAŞTIRILIR (tamamlama problemleri, azalan ipucu); denemeler skorsuz (kanıt kaynağı 2)."
    izinli_ekran_tipleri: [worked_example, fill_blank, simulation, mcq, drag_drop, sorting, matching, decision_scenario, adaptive_practice]
    skorlanabilir: false
    sonraki: [gorev_soluklastirma, gorev_bagimsiz]
    tekrar_kosulu: "Destek düzeyi sıfıra inmediyse bir sonraki (daha karmaşık ya da daha az destekli) görev sınıfında bu fazda kal; destek sıfırlandıysa gorev_bagimsiz fazına geç."
  - id: gorev_bagimsiz
    amac: "Son görev sınıfı — destek YOK: tam görev bağımsız ve skorlu icra edilir."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [gorev_tam_destek, gorev_soluklastirma]
scoring_allowed_from: gorev_bagimsiz
conflicts_with: []
---

# 4cid — 4C/ID: Karmaşık Beceri Eğitimi (C4)

**Ne:** Tam-görev yöntemi. Karmaşık beceri parçalara bölünüp ayrı ayrı öğretilmez; ilk andan
itibaren **basitleştirilmiş ama BÜTÜN** görevlerle çalışılır. Görevler basit→karmaşık **görev
sınıfları** halinde diziler; her sınıf içinde destek (çözümlü örnek → tamamlama problemi →
bağımsız icra) soluklaştırılır. **Ne zaman:** çok alt-becerili, koordinasyon isteyen karmaşık
prosedür / problem çözme kazanımları, düşük-orta önbilgi (PK 1–6) — `rosenshine-di`'nin
alternatifi: görev tek-yolluysa rosenshine-di, karmaşık ve bütünleştirme istiyorsa 4cid.

**Dört bileşenin fazlara yerleşimi** (bileşenler faz DEĞİLDİR — görev sınıflarına dağılır):

1. **Öğrenme görevleri** → üç fazın omurgası (tam görev, her sınıfta artan karmaşıklık).
2. **Destekleyici bilgi** → görev sınıfı BAŞINDA (`gorev_tam_destek` / soluklaştırma sınıflarının
   açılışında): alan modeli, yaklaşımlar, "neden" bilgisi (content_slide/accordion/tabs).
3. **Usul bilgisi (tam-zamanında)** → görev İÇİNDE, adım anında: simulation adım ipuçları,
   `hint_html`, worked_example adım notları — önceden yığılmaz, gerektiği anda verilir.
4. **Parça-görev pratiği** → YALNIZ otomatikleşmesi gereken rutin alt-beceri için ve ancak tam
   görev bağlamı kurulduktan SONRA (`gorev_soluklastirma` içinde adaptive_practice ile drill).

**Kanıt beyanı (Katman 1 bağlantısı — ÇOĞUL):** `evidence_phases: [gorev_tam_destek,
gorev_soluklastirma]` — kanıt, destekli görev sınıflarının çözümlü örnekleri ve destekleyici
bilgisidir (K1 türü 1) + soluklaştırma denemelerinin çıktıları (K1 türü 5). Skorlu ekranlar
`evidence_screen_ids` (ÇOĞUL — scorm-mcp CONTRACTS §1.3 E1) ile bu ekranlara açıkça bağlanır.

**Platform şartı (`requires_platform: [worked_example]`):** soluklaştırma bu paketin motorudur
ve `worked_example` ekran tipinin soluklaştırma düzeyleriyle doğallaşır — tip YAYINDA
(kemalyy/edumints-scorm-mcp F1 #112, `fading: "full" | "partial" | "problem_only"`): `full`
tam çözüm, `partial` eylemler açık + gerekçeler adım başına reveal ardında, `problem_only`
yalnız problem açık. Beyan kalır ve artık karşılanabilirdir: F1 taşıyan sunucuda paket
seçilebilir; yeteneği olmayan (eski) bir hedefte Katman 0 seçici paketi yine eler — o durumda
dürüst seçim rosenshine-di'dir, worked_example'ı content_slide + fill_blank ile taklit etmek değil.

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `gorev_tam_destek` | Görev sınıfı 1: tam görev + tam destek (çözümlü örnek, destekleyici bilgi) — **kanıt 1** | worked_example*, content_slide, video, timeline, accordion, tabs, image_compare | ✗ |
| `gorev_soluklastirma` | Ara sınıflar: tamamlama problemleri, azalan ipucu; skorsuz — **kanıt 2** (döngü: destek 0'a inene dek) | worked_example*, fill_blank, simulation, mcq, drag_drop, sorting, matching, decision_scenario, adaptive_practice | ✗ |
| `gorev_bagimsiz` | Son sınıf: desteksiz, skorlu tam görev | hepsi | ✓ |

\* `worked_example` = `requires_platform` beyanındaki F1 tipi — YAYINDA (sunucu çekirdeğinde,
30 tipin 29.'su; şema: `steps[{action_html, rationale_html, artifact_asset_id?,
artifact_caption?}]` ≥2 + `fading` + ops. `intro_html` / `self_explanation_prompt_html`;
PUAN ALANI YOK — yapısal skorsuz, koşulsuz kanıt-taşıyabilir). Beyan, paketi F1'siz eski
hedeflerde seçilemez tutmayı sürdürür.

Faz notları:

- **Görev sınıfı ≠ konu başlığı:** her sınıf, GERÇEK görevin basitleştirilmiş ama bütün bir
  sürümüdür (SQL örneği: "tek tablodan rapor çek" bütün bir görevdir; "SELECT sözdizimi" değildir).
- Sınıf içi soluklaştırma sırası `fading` düzeyleriyle kurulur: `full` (tam çözümlü örnek) →
  `partial` (eylemler açık, gerekçeyi öğrenen önce KENDİSİ kurar, sonra reveal ile karşılaştırır)
  → `problem_only` (yalnız problem açık, her adım tek tek açılır) → bağımsız deneme.
  `gorev_soluklastirma` döngüsü (`sonraki` + `tekrar_kosulu`) hem sınıf içinde desteği düşürmeyi
  hem yeni (daha karmaşık) sınıfa geçmeyi taşır.
- Skor SADECE destek sıfırlandıktan sonra (`scoring_allowed_from: gorev_bagimsiz`): destekli
  denemeyi puanlamak, desteği ölçmektir — öğreneni değil (Z2/Z3).
- Mikrokurs bütçesine sığdırma: 3 görev sınıfı × 2–3 ekran tipik tavandır; daha fazlası kurs
  DİZİSİ ister (sınıf başına bir modül).

## Bu paket NE ZAMAN seçilmemeli

- **Tekil olgu / kavram kazanımları:** tam-görev iskeleti gereksiz ağırlık katar; olgu için
  `retrieval-spaced`, kavram için `5e-inquiry` ya da `rosenshine-di` seç.
- **Tek-yollu, kısa prosedürler** (5–10 adımlık sabit akış): görev sınıfı dizisi kurulacak
  karmaşıklık yoktur; `rosenshine-di` aynı güvenceyi daha az maliyetle verir.
- **Çok kısa kurslar (≤ 5 dk):** tek görev sınıfına bile yer yoksa soluklaştırma anlamsızlaşır.
- **Yüksek önbilgi (PK ≥ 7):** akıcı öğrenene görev sınıfı 1'in tam desteği uzmanlık-tersinme
  maliyeti üretir; problem-önce (`pbl-case`) düşün.
- **Tutum / psikomotor-akıcılık kazanımları:** `outcome_types` dışıdır (deneyim döngüsü
  `kolb-experiential`, tatbikat `sim-drill`).

## Çakışmalar (`conflicts_with`)

Boş — bilinen kurs-düzeyi çakışma yok. `rosenshine-di` ile ilişki çakışma DEĞİL alternatiflik:
aynı seçici profilinde (prosedür + düşük PK + yüksek hata maliyeti) görev karmaşıklığı hakemdir
(karmaşık/bütünleştirmeli → 4cid; tek-yollu → rosenshine-di) ve seçim gerekçeyle yazılır.
`merrill-fpi` ile akrabalık ölçek farkıdır (kısa-orta tek görev ↔ görev sınıfları dizisi) —
o da seçici notudur, çakışma değil.

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: problem çözme · PK: 2 · hata maliyeti: orta): *"Satış verisinden yönetici
sorusunu cevaplayan bir SQL raporu kurar."* Görev sınıfları: (1) tek tablo + filtre,
(2) + gruplama, (3) desteksiz tam rapor. (Mikrokursa 3 sınıf sığdırıldı; her sınıf TAM görevdir.)

```jsonc
{
  "title": "SQL ile Yönetici Raporu: Tam Görev Eğitimi",
  "description": "4C/ID mikrokursu — 4cid",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "screens": [
    { "type": "title_slide", "title": "SQL ile Yönetici Raporu", "subtitle": "9 dk · ilk dakikadan itibaren BÜTÜN görev" },

    // ── FAZ gorev_tam_destek — görev sınıfı 1: TAM görev + TAM destek (KANIT 1) ──
    { "type": "content_slide", "id": "destek_bilgi", "title": "Destekleyici bilgi: bir rapor sorgusunun anatomisi",
      "body_html": "<p>Her rapor sorgusu aynı soruyu cevaplar: <b>hangi tablodan</b> (FROM), <b>hangi satırlar</b> (WHERE), <b>hangi sütunlar</b> (SELECT). Yönetici sorusunu bu üç parçaya çevirmek, sözdiziminden önce gelir.</p>" },
    // worked_example (F1 — YAYINDA): fading "full" → her adım eylem + gerekçe, tam açık
    { "type": "worked_example", "id": "ornek_sinif1", "title": "Çözümlü örnek: 'Mart'ta İzmir satışları?'", "fading": "full",
      "intro_html": "<p>Görev sınıfı 1 — tam görev, tam destek: uzmanın çözümünü adım adım, gerekçeleriyle izle.</p>",
      "steps": [
        { "action_html": "<p><b>Soruyu çevir:</b> tablo = satislar; satırlar = ay='Mart' VE sehir='İzmir'; sütunlar = tarih, tutar.</p>",
          "rationale_html": "<p>Yönetici sorusu üç parçaya çevrilmeden sorgu kurulamaz: FROM (hangi tablo), WHERE (hangi satırlar), SELECT (hangi sütunlar) — sözdiziminden önce gelir.</p>" },
        { "action_html": "<p><b>Kur:</b> <code>SELECT tarih, tutar FROM satislar WHERE ay='Mart' AND sehir='İzmir';</code></p>",
          "rationale_html": "<p>İki koşul birden gerektiği için AND: yalnız ay filtresi İzmir dışını da getirir, yalnız şehir filtresi diğer ayları da getirir.</p>" },
        { "action_html": "<p><b>Doğrula:</b> dönen satır sayısı mantıklı mı? Mart ≈ 30 gün → yüzlerce satır beklenir.</p>",
          "rationale_html": "<p>0 satır = büyük olasılıkla filtre hatası; beklenti kurmak hatayı sorgu çalıştığı anda yakalatır.</p>" } ] },

    // ── FAZ gorev_soluklastirma — görev sınıfı 2: fading "partial" → eylemler açık, gerekçeler
    //    adım başına REVEAL ardında (öğrenen gerekçeyi önce kendisi kurar; KANIT 2).
    //    Dikkat: worked_example PUAN ALANI taşımaz — yapısal skorsuz (Z3), "points": 0 bile yazılmaz.
    { "type": "worked_example", "id": "tamamlama_sinif2", "title": "Görev sınıfı 2: 'Şehir başına Mart toplamı?' — gerekçeyi önce sen kur", "fading": "partial",
      "intro_html": "<p>Destek azaldı: eylemler açık, her adımın gerekçesini önce KENDİN kur, sonra uzmanınkiyle karşılaştır.</p>",
      "steps": [
        { "action_html": "<p><b>Soruyu çevir:</b> şehir BAŞINA toplam → yeni öğe: gruplama (GROUP BY sehir) + toplam (SUM(tutar)).</p>",
          "rationale_html": "<p>'Başına' kelimesi her zaman gruplamaya işaret eder: satır satır liste değil, grup başına TEK özet satırı istenmektedir.</p>" },
        { "action_html": "<p><b>Kur:</b> <code>SELECT sehir, SUM(tutar) FROM satislar WHERE ay='Mart' GROUP BY sehir;</code></p>",
          "rationale_html": "<p>WHERE gruplamadan ÖNCE çalışır: önce Mart satırları süzülür, sonra kalanlar şehre göre gruplanır — sıra ters olsaydı diğer aylar toplama karışırdı.</p>" } ],
      "self_explanation_prompt_html": "<p>Kendi cümlelerinle: <b>GROUP BY</b> bu soruda neden zorunlu? WHERE tek başına neden yetmez? (Skorsuz — LMS'e yazılmaz.)</p>" },
    { "type": "fill_blank", "id": "tamamlama_dogrula", "title": "Tamamlama: doğrulama adımı", "points": 0,
      "prompt_html": "<p>Sınıf-1 örneğindeki 3. adımı bu sorguya uygula: şehir sayın 12 ise sonuç en fazla ___ satır olmalı.</p>",
      "blanks": [ { "id": "b1", "accepted": ["12", "on iki", "oniki"] } ],
      "feedback": {
        "correct_html": "<p>Evet — gruplama, grup başına TEK satır döndürür; doğrulama beklentisi de buna göre kurulur.</p>",
        "incorrect_html": "<p>'Çözümlü örnek' 3. adıma dön: dönen satır sayısı beklentisi sorgu türünden çıkar — grup başına bir satır.</p>" } },

    // ── FAZ gorev_bagimsiz — son görev sınıfı: destek YOK, SKORLU (kanıt bağı AÇIK ve ÇOĞUL) ──
    { "type": "mcq", "id": "q_rapor_bagimsiz", "title": "Skorlu tam görev: yeni yönetici sorusu", "points": 50,
      "evidence_screen_ids": ["ornek_sinif1", "tamamlama_sinif2"],  // E1 — kanıt: sınıf-1 çözümlü örneği + sınıf-2 tamamlama çıktısı (evidence_phases)
      "prompt_html": "<p>Yönetici soruyor: <i>\"Nisan'da ürün başına toplam satış nedir?\"</i> Doğru sorgu hangisi?</p>",
      "options": [
        { "id": "a", "text_html": "<code>SELECT urun, SUM(tutar) FROM satislar WHERE ay='Nisan' GROUP BY urun;</code>", "correct": true },
        { "id": "b", "text_html": "<code>SELECT urun, tutar FROM satislar WHERE ay='Nisan';</code>" },
        { "id": "c", "text_html": "<code>SELECT SUM(tutar) FROM satislar GROUP BY ay='Nisan';</code>" } ],
      "feedback": {
        "correct_html": "<p>Doğru — çeviri adımını (tablo/satır/sütun) ve sınıf-2'de tamamladığın gruplama desenini yeni soruya taşıdın.</p>",
        "incorrect_html": "<p>'Ürün BAŞINA toplam' iki öğe ister: SUM + GROUP BY. Sınıf-1 çözümlü örneğinin çeviri adımına ve sınıf-2'de doldurduğun boşluğa geri dön.</p>" } },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Denetim izi: skorlu tek ekran (`q_rapor_bagimsiz`) → `evidence_screen_ids: ["ornek_sinif1",
"tamamlama_sinif2"]` — ÇOĞUL bağ, iki kanıt fazına birden (`evidence_phases`). `worked_example`
ekranları yapısal olarak skorsuzdur (puan alanı YOK — Z3: destekli denemeyi puanlamak desteği
ölçer); soluklaştırma fazının quiz denemeleri (`tamamlama_dogrula`) `points: 0` taşır; skor
yalnız destek sıfırlandıktan sonra. Lint-temiz tam fikstür: sunucu deposunda
`examples/worked-example-4cid.tr.json` (3 fading düzeyi + kanıt bağı).

## Literatür

- **Birincil:** van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten Steps to Complex
  Learning: A Systematic Approach to Four-Component Instructional Design* (3rd ed.). Routledge.
  (4. baskı: van Merriënboer, Kirschner & Frerejean, 2024.)
- Modelin kökü: van Merriënboer, J. J. G. (1997). *Training Complex Cognitive Skills.*
  Educational Technology Publications. — 4C/ID'nin ilk bütünlüklü sunumu.
