---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — ERIC ED053419 + uky.edu/~gmswan3/EDC608/Bloom_1968.pdf;
# scirp.org referans kayıtları): Bloom, B. S. (1968). "Learning for Mastery." Evaluation Comment
# (UCLA-CSEIP), 1(2), 1–12. — Çekirdek iddia: uygun öğretim kalitesi + yeterli ZAMAN verilirse
# öğrenenlerin büyük çoğunluğu (%90+) ustalaşabilir; mekanizma: birim öğretimi → formatif test →
# eşik altına DÜZELTİCİ (correctives, farklı temsil) → paralel yeniden-test → sonraki birim.
# Kardeş kaynak: Keller, F. S. (1968). "Good-bye, teacher…" JABA, 1(1), 79–89 (PSI: birim-ustalık
# şartı + kendi hızında ilerleme).
pack: mastery-learning
name: "Tam Öğrenme (Bloom)"
version: 1
outcome_types: [olgu, kavram, prosedür]
prior_knowledge: [1, 7]
error_cost: [düşük, orta, yüksek]
requires_platform: [branching, adaptive_practice]
phases:
  - id: unite_sunumu
    amac: "Ünite küçük birimler halinde, kanıt üretecek biçimde sunulur (çözümlü örnek / artefakt / gerekçeli adımlar) — döngünün 1. kanıt kaynağı."
    izinli_ekran_tipleri: [content_slide, worked_example, video, timeline, accordion, tabs, data_chart, image_compare]
    skorlanabilir: false
    sonraki: [formatif_kontrol]
  - id: formatif_kontrol
    amac: "Skorsuz formatif yoklama üniteyi ölçüt eşiğine (~%80) karşı ölçer ve eşik-altı birimleri TEŞHİS eder (Bloom'un formatif test A'sı)."
    izinli_ekran_tipleri: [adaptive_practice, mcq, true_false, fill_blank, branching]
    skorlanabilir: false
    sonraki: [duzeltici_dongu, summatif_olcum]
    tekrar_kosulu: "Formatif başarı ölçüt eşiğinin (%80) altındaysa duzeltici_dongu fazına git; eşik ve üstündeyse summatif_olcum fazına geç."
  - id: duzeltici_dongu
    amac: "Eşik altı kalan birim FARKLI bir temsille yeniden işlenir (correctives: aynı içerik, yeni biçim) — 2. kanıt kaynağı; ardından paralel formatif kontrole dönülür."
    izinli_ekran_tipleri: [content_slide, worked_example, video, accordion, flashcards, data_chart, image_compare, simulation]
    skorlanabilir: false
    sonraki: [formatif_kontrol]
  - id: summatif_olcum
    amac: "Eşiği geçen öğrenen, sunum + düzeltici kanıtına bağlı skorlu summatif ölçüme girer; sonraki ünite bundan sonra açılır."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [unite_sunumu, duzeltici_dongu]
scoring_allowed_from: summatif_olcum
conflicts_with: []
---

# mastery-learning — Tam Öğrenme (C5)

**Ne:** Ölçüt-eşikli döngü yöntemi. İçerik ünitelere bölünür; her ünite sunulur, **skorsuz
formatif** testle eşiğe (~%80) karşı ölçülür, eşik altı kalan öğrenen **farklı bir temsille**
(düzeltici) yeniden çalışır ve **paralel** bir formatif yoklamayla döngüye devam eder; skorlu
summatif ölçüm YALNIZ eşik geçildikten sonra gelir. Bloom'un iddiası pedagojik değil aritmetiktir:
sabit tutulan şey BAŞARI DÜZEYİDİR, değişken olan ZAMANDIR (geleneksel kurs bunun tersidir).
**Ne zaman:** tam kapsama garantisi isteyen mevzuat/uyum ve sertifikasyon eğitimleri (seçici
eşlemesi: `gagne-9` + `mastery-learning` bileşimi), iyi yapılandırılmış olgu/kavram/prosedür
kazanımları, PK 1–7. Eşik mantığı hata maliyeti yüksek alanlarda ("%70'i bilen" değil "hepsini
bilen" mezun etmek) özellikle değerlidir.

**Kanıt beyanı (Katman 1 bağlantısı — ÇOĞUL):** `evidence_phases: [unite_sunumu,
duzeltici_dongu]`. Kanıt iki kaynaktan gelir: (1) ünite sunumunun çözümlü örneği/artefaktı
(K1 türü 1), (2) düzeltici turun AYNI içeriği taşıyan FARKLI temsili (yine K1 türü 1 — ikinci
kanal). Skorlu sorular `evidence_screen_ids` (ÇOĞUL — scorm-mcp CONTRACTS §1.3 E1) ile her iki
fazın ekranlarına birden bağlanabilir: düzeltici turdan geçen öğrenen için düzeltici ekran da
meşru kanıt kaynağıdır. `formatif_kontrol` kanıt fazı DEĞİLDİR: yoklama kanıt üretmez, teşhis eder.

**Platform şartı (`requires_platform: [branching, adaptive_practice]`):** döngü bu paketin
tanımıdır ve iki yetenek olmadan kurulamaz:

1. **`branching` (+ `set_vars`/`visible_if` değişkenleri):** eşik-altı → düzeltici, eşik-üstü →
   summatif koşullu yönlendirmesinin taşıyıcısı. SCORM'da döngü ekran-tekrar-ziyaretiyle simüle
   edilir: pratik kalıp, formatif sonucun ardından `branching` ekranının iki yolu (`goto_screen_id`)
   açması ve düzeltici kolun paralel yoklamayla ana hatta geri bağlanmasıdır (aşağıdaki örnek).
2. **`adaptive_practice` (BKT modu):** formatif eşiğin doğal taşıyıcısı —
   `{"strategy":"bkt","mastery_stop":0.9}` birim başına ustalık kestirimi + erken durdurma verir;
   eşik kontrolü göz kararı değil kestirimle yapılır. (elo modu burada yanlış araçtır: akış için
   zorluk ayarlar, ustalık beyan etmez.)

İki yetenek de sunucu çekirdeğinde YAYINDA (`references/screen-types.md`); yeteneği olmayan eski
bir hedefte Katman 0 seçici paketi eler — o durumda dürüst seçim döngüsüz bir paket seçmektir,
"tavsiye niteliğinde düzeltici bölüm" ile tam-öğrenme taklidi yapmak değil (eşiği zorlamayan
düzeltici, Bloom'un mekanizmasının ta kendisini kaldırır).

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `unite_sunumu` | Birim birim, gerekçeli sunum — **kanıt 1** | content_slide, worked_example, video, timeline, accordion, tabs, data_chart, image_compare | ✗ |
| `formatif_kontrol` | Eşiğe karşı skorsuz teşhis (döngünün karar noktası) | adaptive_practice (BKT), mcq, true_false, fill_blank, branching | ✗ |
| `duzeltici_dongu` | Eşik altı birimin FARKLI temsille yeniden işlenmesi — **kanıt 2** (→ paralel formatif kontrole döner) | content_slide, worked_example, video, accordion, flashcards, data_chart, image_compare, simulation | ✗ |
| `summatif_olcum` | Eşiği geçenin skorlu ölçümü | hepsi | ✓ |

Faz notları:

- **Düzeltici ≠ tekrar oynatma.** Bloom'un correctives ilkesi aynı anlatımı ikinci kez göstermek
  değildir — ilk temsil işlemediyse İKİNCİ KEZ de işlemez. Düzeltici tur temsil DEĞİŞTİRİR:
  düzyazı → zaman çizelgesi, anlatım → çözümlü örnek, metin → görsel karşılaştırma. Aynı ekranı
  kopyalayan "düzeltici", paketi sahte döngüye çevirir.
- **Yeniden-yoklama PARALEL formdur.** Düzeltici sonrası formatif kontrol aynı soruları
  soramaz (ezber sızıntısı: öğrenen içeriği değil cevabı öğrenir); aynı birimleri ölçen FARKLI
  maddeler kullanılır (Bloom'un formatif test B'si). `adaptive_practice` madde havuzu bunu
  doğal taşır: havuz yeterince genişse (birim başına ≥2 madde) ikinci tur farklı maddeler çeker.
- **Formatif skorSUZdur (Z1/Z3):** teşhis puanlanmaz — formatif sonucu `passing_score`'a
  yazmak, henüz öğrenme fırsatı bitmemiş öğrenene ceza keser ve döngünün "deneme güvenli"
  zeminini yok eder. Skor tek yerde yaşar: `summatif_olcum`.
- **Eşik beyan edilir:** %80 varsayılandır; kurum farklı bir ölçüt istiyorsa `tekrar_kosulu`
  cümlesine ve kurs briefine yazılır. Eşik ile `tracking.passing_score` AYNI ŞEY DEĞİLDİR:
  ilki döngünün formatif kapısı, ikincisi kursun summatif geçme notudur.
- **Mikrokurs dozu:** tek mikrokursa 1–2 ünite sığar (ünite başına sunum + formatif + düzeltici
  + summatif ≈ 4–6 ekran). Çok üniteli müfredat kurs DİZİSİ ister (ünite başına bir modül);
  SCORM 2004 sequencing ünite kilidini paket düzeyinde de taşıyabilir ama bu paketin asgari
  şartı kurs-içi `branching` yönlendirmesidir.

## Bu paket NE ZAMAN seçilmemeli

- **Keşif / tutum kazanımları:** `outcome_types` dışıdır — eşikli döngü yakınsak (tek-doğrulu)
  içerik ister; açık uçlu keşifte "%80 eşiği" tanımsızdır (kavram keşfi için `5e-inquiry` /
  `productive-failure`, tutum için `kolb-experiential`).
- **Tek oturumluk mikro kurslar (≤ 5 dk):** döngü kurulamaz — düzeltici tur + paralel yoklamaya
  yer yoksa paket "sunum + quiz"e yozlaşır; o zaman dürüst seçim `rosenshine-di`dir.
- **Çok yüksek önbilgi (PK ≥ 8):** akıcı öğrenen için formatif kapı + düzeltici tur boş
  bürokrasidir; `retrieval-spaced` (tazeleme) ya da `pbl-case` (uygulama) daha verimli.
- **Platform koşullu dallanma taşımıyorsa:** `requires_platform` karşılanmaz, paket elenir —
  eşiği zorlamayan "isteğe bağlı tekrar bölümü" tam-öğrenme değildir.
- **Kötü yapılandırılmış problem alanları:** birim + ölçüt-eşiği modeli, doğru cevabı net
  olmayan stratejik kararlarda çalışmaz (`pbl-case` seç).

## Çakışmalar (`conflicts_with`)

Boş — bilinen hedef-düzeyi çakışma yok. `gagne-9` ile bileşim (mevzuat/uyum eşlemesi, seçici
örnek 4) çakışma değil TAMAMLAYICILIKTIR: dokuz-olay yapısı ünite İÇİNİ örgütler, tam-öğrenme
üniteler ARASI eşik kapısını koyar. `rosenshine-di` ile ilişki de çakışma değildir: rehberli →
bağımsız pratik dizisi `unite_sunumu`+`formatif_kontrol` içinde aynen yaşayabilir; iki paket
aynı hedefte yarışıyorsa hakem döngü ihtiyacıdır (eşik garantisi isteniyorsa mastery-learning,
tek geçişli akış yeterliyse rosenshine-di) ve seçim gerekçeyle yazılır.

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: prosedür · PK: 2 · hata maliyeti: yüksek): *"Yeni tedarikçi kaydında şirketin
üç zorunlu doğrulama adımını doğru sırayla uygular."* Bağlam: zorunlu uyum eğitimi; şirket
prosedürü kurum-içidir (kamusal kanon değil — K2 temiz). Döngü SCORM'da tekrar ziyaretle simüle
edilir: formatif sonrası `branching` iki yol açar; düzeltici kol paralel yoklamayla ana hatta
geri bağlanır (tek düzeltici tur açılımı — pratik SCORM karşılığı).

```jsonc
{
  "title": "Tedarikçi Doğrulama: Üç Zorunlu Adım",
  "description": "Tam-öğrenme mikrokursu — mastery-learning",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 },
  "screens": [
    { "type": "title_slide", "title": "Tedarikçi Doğrulama", "subtitle": "7 dk · eşik: %80 — geçemeyen tekrar çalışır, bu bir ceza değil tasarım" },

    // ── FAZ unite_sunumu (KANIT 1: üç adım, gerekçeli çözümlü örnek) ──
    { "type": "worked_example", "id": "unite_adimlar", "title": "Çözümlü örnek: Atlas Ltd. kaydı", "fading": "full",
      "intro_html": "<p>Uzman, yeni tedarikçi Atlas Ltd. kaydını üç zorunlu adımla doğruluyor — sıra neden böyle, adım adım izle.</p>",
      "steps": [
        { "action_html": "<p><b>Adım 1 — Sicil doğrulama:</b> vergi numarası resmi sicil kaydıyla karşılaştırılır.</p>",
          "rationale_html": "<p>Sicili doğrulanmamış firmaya sonraki adımlar boşa emektir: var olmayan tüzel kişiye tarama da ödeme teyidi de yapılamaz.</p>" },
        { "action_html": "<p><b>Adım 2 — Yaptırım taraması:</b> firma unvanı ve ortakları yaptırım listelerinde taranır.</p>",
          "rationale_html": "<p>Tarama sicilden SONRA gelir: doğrulanmış resmi unvan olmadan tarama yanlış ada yapılır ve temiz görünen kirli kayıt üretir.</p>" },
        { "action_html": "<p><b>Adım 3 — Banka teyidi:</b> ödeme hesabı, firmanın resmi iletişim kanalından geri-arama ile teyit edilir.</p>",
          "rationale_html": "<p>Teyit en sona kalır ve formdaki numaradan DEĞİL bağımsız kanaldan yapılır: formu dolduran kişi sahtekârsa formdaki numara da onundur.</p>" } ] },

    // ── FAZ formatif_kontrol (SKORSUZ teşhis — BKT ustalık kestirimi; eşik %80) ──
    { "type": "adaptive_practice", "id": "formatif_a", "title": "Formatif kontrol (puan yok — teşhis)", "points": 0,
      "adaptive": { "strategy": "bkt", "mastery_stop": 0.9 }, "target_success": 0.8,
      "items": [
        { "id": "f1", "difficulty": -1.0, "prompt_html": "<p>Yaptırım taraması hangi adımdan SONRA yapılır?</p>",
          "explain_html": "<p>Sicil doğrulamadan sonra — tarama, doğrulanmış resmi unvana yapılır ('Çözümlü örnek' Adım 2 gerekçesi).</p>",
          "options": [ { "id": "a", "text_html": "Sicil doğrulama", "correct": true }, { "id": "b", "text_html": "Banka teyidi" } ] },
        { "id": "f2", "difficulty": 0.0, "prompt_html": "<p>Banka teyidi neden kayıt formundaki telefondan YAPILMAZ?</p>",
          "explain_html": "<p>Formu dolduran sahtekârsa formdaki numara da onundur — teyit bağımsız kanaldan yapılır (Adım 3 gerekçesi).</p>",
          "options": [ { "id": "a", "text_html": "Bağımsız kanal şartı: form sahibi numarayı da kontrol edebilir", "correct": true }, { "id": "b", "text_html": "Formdaki numara çoğu zaman yazım hatalıdır" } ] },
        { "id": "f3", "difficulty": 0.5, "prompt_html": "<p>Sicil doğrulaması atlanırsa hangi adımların sonucu güvenilmez olur?</p>",
          "explain_html": "<p>Her ikisi de — tarama yanlış ada yapılır, teyit var olmayan tüzel kişiye bağlanır (Adım 1 gerekçesi).</p>",
          "options": [ { "id": "a", "text_html": "Yalnız yaptırım taraması" }, { "id": "b", "text_html": "Hem tarama hem banka teyidi", "correct": true } ] },
        { "id": "f4", "difficulty": 1.0, "prompt_html": "<p>Üç adımın sırasını belirleyen ortak ilke nedir?</p>",
          "explain_html": "<p>Her adım, bir sonrakinin GÜVENDİĞİ bilgiyi üretir: sicil → doğru unvan → tarama; bağımsız teyit en sona.</p>",
          "options": [ { "id": "a", "text_html": "Her adım bir sonrakinin dayandığı bilgiyi üretir", "correct": true }, { "id": "b", "text_html": "Kolaydan zora doğru sıralama" } ] } ] },

    // ── Döngünün karar noktası: branching iki yol açar (eşik-altı → düzeltici; eşik-üstü → summatif) ──
    { "type": "branching", "id": "esik_karar", "title": "Eşik kontrolü",
      "prompt_html": "<p>Formatif kontrol sonucuna bak: <b>%80 ve üstündeysen</b> skorlu ölçüme geç; altındaysan düzeltici tura git — bu bir ceza değil, tasarımın kendisi.</p>",
      "choices": [
        { "id": "c_gecti", "text_html": "%80 ve üstü — skorlu ölçüme geç", "goto_screen_id": "q_summatif" },
        { "id": "c_kaldi", "text_html": "%80 altı — düzeltici turla devam", "goto_screen_id": "duzeltici_zaman" } ] },

    // ── FAZ duzeltici_dongu (KANIT 2: AYNI içerik, FARKLI temsil — düzyazı örnek → zaman çizelgesi) ──
    { "type": "timeline", "id": "duzeltici_zaman", "title": "Düzeltici: aynı üç adım, akış olarak",
      "events": [
        { "date": "1", "title": "Sicil doğrulama", "body_html": "<p>Vergi numarası ↔ resmi sicil. Bu adım olmadan sonraki iki adımın nesnesi yoktur.</p>" },
        { "date": "2", "title": "Yaptırım taraması", "body_html": "<p>Doğrulanmış unvan + ortaklar listelerde taranır — tarama, 1. adımın çıktısına yapılır.</p>" },
        { "date": "3", "title": "Banka teyidi", "body_html": "<p>Ödeme hesabı bağımsız kanaldan geri-aramayla teyit edilir — formdaki iletişim bilgisi kullanılmaz.</p>" } ] },
    // Paralel formatif (test B): aynı birimleri ölçen FARKLI maddeler — sonra ana hatta geri bağlanır
    { "type": "mcq", "id": "formatif_b", "title": "Yeniden yoklama (paralel form — puan yok)", "points": 0,
      "prompt_html": "<p>Tarama TEMİZ çıktı ama sicil doğrulaması hiç yapılmadı. Kayıt ilerleyebilir mi?</p>",
      "options": [
        { "id": "a", "text_html": "Hayır — tarama doğrulanmamış ada yapıldı, sonucu güvenilmez", "correct": true },
        { "id": "b", "text_html": "Evet — tarama temizse risk kalmamıştır" } ],
      "feedback": {
        "correct_html": "<p>Doğru — akıştaki 1. kutu sonrakilerin dayanağıdır; düzeltici çizelgedeki sıra tam bunu gösterir.</p>",
        "incorrect_html": "<p>Düzeltici çizelgeye dön: 2. adım, 1. adımın ÇIKTISINA (doğrulanmış unvan) yapılır — girdisi yoksa çıktısı anlamsızdır.</p>" } },

    // ── FAZ summatif_olcum (eşik geçildi — SKORLU; kanıt bağı AÇIK ve ÇOĞUL: iki kanıt fazına birden) ──
    { "type": "mcq", "id": "q_summatif", "title": "Skorlu: yeni kayıt vakası", "points": 100,
      "evidence_screen_ids": ["unite_adimlar", "duzeltici_zaman"],  // E1 — kanıt: ünite sunumu + düzeltici temsil (evidence_phases: [unite_sunumu, duzeltici_dongu])
      "prompt_html": "<p>Meslektaşın yeni bir tedarikçi kaydında önce ödeme hesabını formdaki numaradan teyit etmiş, sonra sicile bakmayı planlıyor. Prosedüre göre ne söylersin?</p>",
      "options": [
        { "id": "a", "text_html": "İki hata var: teyit bağımsız kanaldan yapılır ve sicil doğrulama her şeyden önce gelir", "correct": true },
        { "id": "b", "text_html": "Sıra fark etmez, üç adım da yapıldığı sürece kayıt uyumludur" },
        { "id": "c", "text_html": "Tek hata var: teyit doğru, yalnız sicil öne alınmalı" } ],
      "feedback": {
        "correct_html": "<p>Doğru — çözümlü örnekteki iki gerekçeyi birden yakaladın: sıra bilgi-bağımlılığından çıkar, teyit bağımsız kanal ister.</p>",
        "incorrect_html": "<p>'Çözümlü örnek' Adım 1 ve Adım 3 gerekçelerine geri dön: sıra keyfî değildir ve formdaki numara teyit kanalı olamaz.</p>" } },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Denetim izi: skorlu tek ekran (`q_summatif`) → `evidence_screen_ids: ["unite_adimlar",
"duzeltici_zaman"]` — ÇOĞUL bağ, iki kanıt fazına birden (`evidence_phases`). Formatif ekranlar
(`formatif_a`, `formatif_b`) `points: 0` (Z1/Z3 — teşhis puanlanmaz); döngü `branching`
(`esik_karar`) ile simüle edilir ve eşiği geçen yol düzeltici ekranları ATLAR (`goto_screen_id:
"q_summatif"`). Düzeltici tur aynı içeriği FARKLI temsille (worked_example → timeline) taşır;
paralel yoklama (`formatif_b`) formatif A'nın maddelerini tekrarlamaz.

## Literatür

- **Birincil:** Bloom, B. S. (1968). *Learning for Mastery.* Evaluation Comment (UCLA Center for
  the Study of Evaluation of Instructional Programs), 1(2), 1–12. (ERIC ED053419.)
- Kardeş model: Keller, F. S. (1968). *"Good-bye, teacher…"* Journal of Applied Behavior
  Analysis, 1(1), 79–89 — PSI: birim-ustalık şartı + kendi hızında ilerleme (bu paketin
  "eşiği geçmeden sonraki ünite açılmaz" kuralının ikinci dayanağı).
- Uygulama sentezi: Guskey, T. R. (2007). *Closing Achievement Gaps: Revisiting Benjamin S.
  Bloom's "Learning for Mastery."* Journal of Advanced Academics, 19(1), 8–31 — düzelticilerin
  "farklı temsil" şartı ve paralel formatif form pratiği.
