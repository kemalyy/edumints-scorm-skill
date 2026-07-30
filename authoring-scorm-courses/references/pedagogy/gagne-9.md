---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — niu.edu/citl Gagné dokuz-olay rehberi + EBSCO
# Research Starters "Gagné's Conditions of Learning" + SAGE Encyclopedia of Educational
# Technology "Conditions of Learning: Gagné's Nine Events of Instruction"): Gagné, R. M. (1985).
# The Conditions of Learning and Theory of Instruction (4. baskı). New York: Holt, Rinehart &
# Winston. — Dokuz olay (doğrulanan adlar): (1) gaining attention, (2) informing the learner of
# the objective, (3) stimulating recall of prior learning, (4) presenting the stimulus,
# (5) providing learning guidance, (6) eliciting performance, (7) providing feedback,
# (8) assessing performance, (9) enhancing retention and transfer. Beş öğrenme alanı (sözel
# bilgi, zihinsel beceriler, bilişsel stratejiler, tutumlar, motor beceriler) → outcome_types
# tam listesinin gerekçesi. Kardeş kaynak: Gagné, Briggs & Wager (1992), Principles of
# Instructional Design (4. baskı) — olayların tasarım-uygulaması.
pack: gagne-9
name: "Gagné'nin Dokuz Öğretim Olayı"
version: 1
outcome_types: [olgu, kavram, prosedür, ilke, problem çözme, tutum, psikomotor]
prior_knowledge: [1, 10]
error_cost: [düşük, orta, yüksek]
requires_platform: []
phases:
  - id: dikkat_cekme
    amac: "Olay 1 — dikkat kazanılır: kazanımın SAHADAKİ bedelini gösteren somut kanca (vaka, çarpıcı veri, kısa senaryo); süs değil ilgililik."
    izinli_ekran_tipleri: [title_slide, content_slide, video, data_chart, image_compare]
    skorlanabilir: false
  - id: hedef_bildirimi
    amac: "Olay 2 — öğrenen hedefi öğrenir: kurs sonunda NE yapabilir olacağı ölçülebilir fiille bildirilir (beklenti kurulumu)."
    izinli_ekran_tipleri: [content_slide, title_slide]
    skorlanabilir: false
  - id: on_bilgi_cagirma
    amac: "Olay 3 — ön öğrenme çağrılır: yeni içeriğin bağlanacağı mevcut bilgi skorsuz yoklamayla etkinleştirilir."
    izinli_ekran_tipleri: [poll, mcq, true_false, flashcards, exploration]
    skorlanabilir: false
  - id: uyaran_sunumu
    amac: "Olay 4 — uyaran sunulur: içerik, KANIT ÜRETEN artefaktlarla gelir (vaka belgesi, tablo, zaman çizelgesi, çözümlü örnek) — 1. kanıt kaynağı."
    izinli_ekran_tipleri: [content_slide, worked_example, timeline, accordion, tabs, data_chart, image_compare, video]
    skorlanabilir: false
  - id: ogrenme_rehberligi
    amac: "Olay 5 — öğrenme rehberliği: sunulan içerik örnek/karşıt-örnek, ipucu ve anlamlandırma şemalarıyla İŞLENİR (yarı-örnek, sınıflama, kural→artefakt köprüsü) — 2. kanıt kaynağı."
    izinli_ekran_tipleri: [worked_example, content_slide, tabs, accordion, flashcards, image_compare, data_chart]
    skorlanabilir: false
  - id: performans_cikarma
    amac: "Olay 6 — performans ortaya çıkarılır: öğrenen yeni beceriyi SKORSUZ dener (deneme-güvenli uygulama turu)."
    izinli_ekran_tipleri: [mcq, true_false, fill_blank, drag_drop, matching, sorting, hotspot, simulation, adaptive_practice]
    skorlanabilir: false
  - id: gerekceli_geribildirim
    amac: "Olay 7 — gerekçeli geri bildirim verilir: deneme turunun tipik hataları mekanizmasıyla düzeltilir (G1 anatomisi: neden doğru + neden yanlış + kanıta işaret)."
    izinli_ekran_tipleri: [content_slide, worked_example, tabs, accordion]
    skorlanabilir: false
  - id: performans_degerlendirme
    amac: "Olay 8 — performans değerlendirilir: SKORLU ölçüm; her soru uyaran/rehberlik artefaktlarına bağlanır (kanon-alan kuralı: artefakta-uygulama)."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
  - id: kalicilik_transfer
    amac: "Olay 9 — kalıcılık ve transfer güçlendirilir: aynı beceri YENİ bağlam/varyantta uygulanır; kavram-düzeyi kapanış (cevap cümlesi kurmadan — K5)."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [uyaran_sunumu, ogrenme_rehberligi]
scoring_allowed_from: performans_degerlendirme
conflicts_with: []
---

# gagne-9 — Gagné'nin Dokuz Öğretim Olayı (C10)

**Ne:** Tam-kapsama iskeleti: dokuz öğretim olayı (Gagné 1985) dikkat → hedef → ön bilgi →
uyaran → rehberlik → performans → geri bildirim → değerlendirme → kalıcılık/transfer dizisiyle,
"iddia + quiz" zincirinin atladığı işlevlerin HER BİRİNİ ayrı ayrı zorlar. v1'in uyum kursu
deseni (intro → tanım → tabs → flashcards → fill_blank → özet) tam bu ayrımın yokluğuydu:
sunumdan ölçmeye ara işlev olmadan atlanıyordu. **Ne zaman:** mevzuat/zorunlu eğitim ve uyum
kursları (seçici örnek 4: `gagne-9` + `mastery-learning` + `assessment-alignment`); ayrıca
Katman 0 elemesinin boş küme döndürdüğü durumun **belgeli varsayılanı** (en geniş kazanım-türü
kapsamı + platform şartı yok — `core/method-selector.md`; varsayılana düşüş zorunlu gerekçe
ister). `outcome_types` tam listedir çünkü Gagné'nin beş öğrenme alanı (sözel bilgi, zihinsel
beceriler, bilişsel stratejiler, tutumlar, motor beceriler) yedi türün tamamını kapsar — bu
genişlik paketin gücü değil NÖTRLÜĞÜDÜR: dokuz olay her türe uyar ama hiçbirine özelleşmiş
mekanik (döngü, deneme-önce, vaka ailesi) sunmaz; özelleşmiş paket sağ kaldığında o tercih edilir.

**DOKUZ OLAY EKRAN DEĞİL İŞLEVDİR (en kritik uyarı):** "9 olay = 9 ekran" okuma hatası paketi
şişkin şablona çevirir. Olay bir İŞLEVDİR: iki olay tek ekranda birleşebilir (dikkat + hedef tek
açılış ekranında; performans denemesi + geri bildirim aynı soru ekranının feedback alanında),
bir olay birden çok ekrana yayılabilir (uyaran sunumu üç artefakt ekranı). Denetim sorusu ekran
saymaz: "dokuz işlevin her biri KURSUN NERESİNDE yerine geliyor?" — cevabı boş kalan olay
tasarım açığıdır, ekran açığı değil.

**Kanıt beyanı (Katman 1 bağlantısı — ÇOĞUL):** `evidence_phases: [uyaran_sunumu,
ogrenme_rehberligi]`. Kanıt iki kaynaktan gelir: (1) uyaran sunumunun artefaktları — vaka
belgesi, tablo, çizelge, çözümlü örnek (K1 türleri 1/4/6), (2) rehberlik fazının örnek /
karşıt-örnek işlemesi (K1 türü 1 — ikinci kanal: kuralın artefakta NASIL uygulandığını gösteren
işlenmiş örnek). Skorlu sorular `evidence_screen_ids` (ÇOĞUL — scorm-mcp CONTRACTS §1.3 E1) ile
iki fazın ekranlarına birden bağlanabilir. Olay 3 (`on_bilgi_cagirma`) ve olay 6
(`performans_cikarma`) kanıt fazı DEĞİLDİR: ilki mevcut bilgiyi çağırır, ikincisi dener — ikisi
de yeni kanıt üretmez.

**KANON-ALAN KURALI BU PAKETTE KRİTİKTİR:** mevzuat/uyum içeriği tanımı gereği KAMUSAL KANONDUR —
kursu hiç görmemiş uzman, kuralı bilir; K2 denetim sorusu kanon-hatırlatan her soruda "evet"
çıkar. Bu yüzden `performans_degerlendirme` soruları kanunun/politikanın KENDİSİNİ soramaz;
kanonun **kursun ürettiği artefakta uygulanmasını** ölçer (`core/evidence-binding.md`
"Kanon-alan içerikleri" bölümü — dönüştürme kalıbı: "kural nedir?" → "kanıt ekranındaki ŞU
artefakta göre kural neyi gerektirir?"). Kritik olgu (tarih, tutar, madde içeriği, form cümlesi)
YALNIZ uyaran/rehberlik ekranlarında yaşar (K4); soru gövdesi ona atıf yapar, değerini
kopyalamaz. Uyum kursunda bu kuralı atlamak, kursu bakanlık sınav bankasının kötü kopyasına
çevirir.

## Faz rehberi

| Faz (olay) | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `dikkat_cekme` (1) | Sahadaki bedeli gösteren kanca | title_slide, content_slide, video, data_chart, image_compare | ✗ |
| `hedef_bildirimi` (2) | Ölçülebilir "yapabileceksin" beyanı | content_slide, title_slide | ✗ |
| `on_bilgi_cagirma` (3) | Mevcut bilginin skorsuz etkinleştirilmesi | poll, mcq, true_false, flashcards, exploration | ✗ |
| `uyaran_sunumu` (4) | Artefaktlı içerik sunumu — **kanıt 1** | content_slide, worked_example, timeline, accordion, tabs, data_chart, image_compare, video | ✗ |
| `ogrenme_rehberligi` (5) | Örnek/karşıt-örnek işleme, kural→artefakt köprüsü — **kanıt 2** | worked_example, content_slide, tabs, accordion, flashcards, image_compare, data_chart | ✗ |
| `performans_cikarma` (6) | Skorsuz deneme turu | mcq, true_false, fill_blank, drag_drop, matching, sorting, hotspot, simulation, adaptive_practice | ✗ |
| `gerekceli_geribildirim` (7) | Tipik hataların mekanizmalı düzeltimi | content_slide, worked_example, tabs, accordion | ✗ |
| `performans_degerlendirme` (8) | SKORLU ölçüm (artefakta-uygulama) | hepsi | ✓ |
| `kalicilik_transfer` (9) | Yeni bağlam/varyant + kavram-düzeyi kapanış | hepsi | ✓ |

Faz notları:

- **Mevzuat bağlamında HERKES AYNI İÇERİĞİ GÖRÜR:** zorunlu eğitimde tam kapsama yasal
  yükümlülüktür — uyarlanabilir ATLAMA yolu (ön bilgisi yüksek öğrenene uyaran sunumunu
  atlatmak) bu bağlamda KULLANILMAZ; `adaptive_practice` yalnız deneme turunun (olay 6) doz
  ayarında meşrudur, içerik atlatmada değil. `expertise-adaptive` kaplamasının atlama-yolu
  önerileri bu paketin mevzuat kullanımında karar-noktası düzeyinde çelişir; bildirim kaplama
  tarafında yapılır (D4 dosyası yazılırken, `overlays/_FRAMEWORK.md` biçimiyle) — hedef-düzeyi
  `conflicts_with` beyanı DEĞİLDİR.
- **Olay 6 + 7 çifti quiz değildir:** deneme turu SKORSUZDUR (Z1 — `passing_score`'a yazmaz) ve
  geri bildirim olayı ayrı bir işlevdir: tipik yanılgılar mekanizmasıyla düzeltilir (G1 üç öğe:
  neden doğru + neden yanlış + kanıta işaret; G2 — şablon gerekçe yasak). Deneme turunu skorlu
  yapmak Z2'yi ihlal etmez (kanıt üretilmiş durumda) ama Gagné'nin ayrımını öldürür: performans
  çıkarma ÖĞRENME olayıdır, ölçme olayı değil — skor olay 8'de yaşar.
- **Uyaran sunumu artefakt ÜRETİR, iddia sıralamaz:** olay 4'ün ekranları "X önemlidir" cümleleri
  değil, sorunun sonra bağlanacağı incelemelik malzemedir (form örneği, kayıt, çizelge, işlenmiş
  vaka). Artefaktsız uyaran sunumu, olay 8'i kanon-hatırlatmaya mahkûm eder.
- **Olay 9 özet değildir:** kalıcılık/transfer YENİ bağlam ister (farklı departman senaryosu,
  farklı belge, varyant vaka) — aynı soruların tekrarı ya da cevapları yeniden söyleyen kapanış
  (K5 ihlali) değil. Skorlu transfer sorusu meşrudur (olay 8'den sonra gelir); kapanış cümlesi
  kavram düzeyinde kalır.
- **`mastery-learning` ile bileşim (seçici örnek 4):** dokuz olay ünite İÇİNİ örgütler,
  tam-öğrenme üniteler ARASI eşik kapısını koyar — çakışma değil tamamlayıcılık (iki paketin
  `conflicts_with`'i karşılıklı boş). Bileşimde olay 6–8 zinciri tam-öğrenmenin formatif→summatif
  döngüsüne oturur; eşik mekaniği mastery-learning beyanından okunur.

## Bu paket NE ZAMAN seçilmemeli

- **Keşif ağırlıklı kavram inşası:** dokuz olay gösterim-önce akar (uyaran → rehberlik →
  performans); kavramın öğrenen tarafından KURULMASI hedefse `5e-inquiry` /
  `productive-failure` doğru araçtır — dokuz olayla keşif taklidi, olay 4'ü "ipucu ekranı"na
  çevirip iki yöntemi de bozar.
- **Çok kısa mikro-öğrenme (≤ 3–4 dk):** dokuz işlev sığmaz; işlev atlaya atlaya "gagne-9
  görünümlü intro+quiz" üretmektense dürüst seçim tek-geçişli `rosenshine-di` ya da tazelemede
  `retrieval-spaced`tir.
- **Özelleşmiş paket sağ kalmışken varsayılan diye seçmek:** eleme sonrası `sim-drill` /
  `pbl-case` / `mastery-learning` gibi hedefe özelleşmiş bir paket ayaktaysa, gagne-9'un
  genişliği gerekçe DEĞİLDİR — nötr iskelet, özelleşmiş mekaniğin yerini tutmaz. Varsayılana
  düşüş yalnız eleme boş küme döndürdüğünde ve yazılı gerekçeyle meşrudur.
- **Ölçme yasağı olan bağlamlar (yalnız bilgilendirme):** olay 8 paketin omurgasıdır; skorlu
  ölçüm istenmeyen duyuru/bilgilendirme içeriği paket gerektirmez.

## Çakışmalar (`conflicts_with`)

Boş — bilinen hedef-düzeyi çakışma yok. `mastery-learning` ile bileşim tamamlayıcılıktır
(yukarıdaki faz notu). Deneme-önce paketlerle (`productive-failure`, `5e-inquiry`) sıra beyanı
zıttır ama fiilî yarışma alanı dardır: o paketler kavram/ilke + belirli PK bandına özelleşmiştir
ve aynı hedefte ikisi birden seçilirse hakem, bağlamdır (mevzuat/tam-kapsama → gagne-9; güvenli
keşif alanı → deneme-önce) — seçim gerekçeyle yazılır, çakışma beyanı değil seçim kararıdır.
`expertise-adaptive` kaplamasıyla gerilim hedef-düzeyi değil karar-noktası düzeyindedir
(`gezinme`/atlama yolları — mevzuat kullanımında askıya alınır); bildirim kaplama dosyası
yazılırken o tarafta yapılır.

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: kavram · PK: 3 · hata maliyeti: yüksek): *"Bir açık-rıza metnini KVKK
geçerlilik koşullarına göre değerlendirir ve geçersiz kılan kusuru gösterir."* Bağlam: zorunlu
KVKK uyum eğitimi — kanon-alan örneği bilerek seçildi: geçerlilik koşulları KAMUSAL KANONDUR,
sorular bu yüzden kanonu değil kanonun KURSUN ÜRETTİĞİ rıza-metni artefaktlarına uygulanmasını
ölçer. Dokuz olay 8 ekranda: olay 1+2 tek açılışta, olay 6+7 tek soru ekranı + feedback'te
birleşti (olay ≠ ekran).

```jsonc
{
  "title": "Açık Rıza: Geçerli mi, Geçersiz mi?",
  "description": "Dokuz-olay uyum mikrokursu — gagne-9",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 },
  "screens": [
    // ── OLAY 1+2 (dikkat_cekme + hedef_bildirimi — tek ekranda: olay ≠ ekran) ──
    { "type": "content_slide", "id": "acilis_kanca", "title": "Tek kutucuk, yedi haneli ceza",
      "body_html": "<p>Geçen yıl bir e-ticaret şirketi, üyelik formundaki TEK önceden-işaretli kutucuk yüzünden idari para cezası aldı: kutucuk 'rıza' sayılmadı. Bu kursun sonunda bir açık-rıza metnini geçerlilik koşullarına göre değerlendirebilecek ve geçersiz kılan kusuru METİN ÜZERİNDE gösterebileceksin.</p>" },

    // ── OLAY 3 (on_bilgi_cagirma — skorsuz etkinleştirme) ──
    { "type": "poll", "id": "onbilgi_yoklama", "title": "Sence rıza nedir?",
      "prompt_html": "<p>Puan yok. Sence bir web formunda 'kişisel verilerimin işlenmesini kabul ediyorum' kutusunu işaretlemek TEK BAŞINA geçerli rıza mıdır?</p>",
      "options": [ { "id": "p1", "text_html": "Evet — işaretlediyse kabul etmiştir" }, { "id": "p2", "text_html": "Hayır — başka koşullar da aranır" } ],
      "reflection_html": "<p>Birazdan iki gerçek metin üzerinde göreceksin: işaret tek başına yetmiyor — neyin, hangi koşulla arandığı bu kursun konusu.</p>" },

    // ── OLAY 4 (uyaran_sunumu — KANIT 1: iki rıza-metni artefaktı yan yana) ──
    { "type": "tabs", "id": "artefakt_metinler", "title": "İncelemelik: iki üyelik formu",
      "tabs": [
        { "title": "Form A — Moda sitesi", "content_html": "<p><em>\"Üyeliğinizin oluşturulması, kampanyalardan haberdar edilmeniz ve verilerinizin iş ortaklarımızla paylaşılması için kişisel verilerinizin işlenmesini kabul ediyorum.\"</em> — kutucuk ÖNCEDEN İŞARETLİ; tek kutu, üç ayrı amaç.</p>" },
        { "title": "Form B — Kargo takip", "content_html": "<p><em>\"Kargonuzun teslim bildirimi için telefon numaranız SMS gönderiminde kullanılacaktır. Onaylıyorsanız işaretleyin; onaylamazsanız bildirimi e-postanızdan takip edebilirsiniz.\"</em> — kutucuk BOŞ; tek amaç; reddetme yolu açık.</p>" } ] },

    // ── OLAY 5 (ogrenme_rehberligi — KANIT 2: koşul → metin köprüsü, örnek/karşıt-örnek) ──
    { "type": "worked_example", "id": "rehber_kosullar", "title": "Uzman iki formu koşul koşul okuyor", "fading": "full",
      "intro_html": "<p>Geçerli rızanın üç koşulu (belirli konuya dayalı + bilgilendirmeye dayalı + özgür irade) iki metne tek tek uygulanıyor.</p>",
      "steps": [
        { "action_html": "<p><b>Koşul 1 — Belirli konu:</b> Form A tek kutuda ÜÇ amacı topluyor (üyelik + kampanya + paylaşım); Form B tek amaç bildiriyor.</p>",
          "rationale_html": "<p>Amaçlar ayrışmayınca kullanıcı NEYE rıza verdiğini seçemez — 'battaniye rıza' belirlilik koşulunu düşürür; B'de konu tek ve nettir.</p>" },
        { "action_html": "<p><b>Koşul 2 — Bilgilendirme:</b> A, 'iş ortakları'nın kim olduğunu ve verinin ne olacağını söylemiyor; B, hangi verinin (telefon) ne için (SMS bildirimi) kullanılacağını söylüyor.</p>",
          "rationale_html": "<p>Rıza ancak ne olacağını BİLEREK verilirse rızadır; muğlak 'iş ortağı' ifadesi bilgilendirmeyi boşaltır.</p>" },
        { "action_html": "<p><b>Koşul 3 — Özgür irade:</b> A'da kutucuk önceden işaretli; B'de kutu boş VE reddetme yolu (e-posta takibi) gösterilmiş.</p>",
          "rationale_html": "<p>Önceden işaretli kutu iradeyi kullanıcı yerine kurgular — açılıştaki ceza vakasının kusuru tam buydu; B, 'hayır' diyene işleyen bir yol bırakarak iradeyi özgür kılar.</p>" } ] },

    // ── OLAY 6+7 (performans_cikarma + gerekceli_geribildirim — skorsuz deneme, feedback olay 7'yi taşır) ──
    { "type": "mcq", "id": "deneme_a", "title": "Deneme turu (puan yok)", "points": 0,
      "prompt_html": "<p>Form A'yı ('İncelemelik' sekmesi) yeniden aç. Üç koşuldan HANGİLERİ bu metinde düşüyor?</p>",
      "options": [
        { "id": "a", "text_html": "Yalnız özgür irade (önceden işaretli kutu)" },
        { "id": "b", "text_html": "Üçü birden — battaniye amaç + muğlak paylaşım + işaretli kutu", "correct": true },
        { "id": "c", "text_html": "Hiçbiri — kutu işaretlendiyse rıza tamamdır" } ],
      "feedback": {
        "correct_html": "<p>Doğru — uzman okumasındaki üç adımın üçü de A'da düşüyordu: tek kutuda üç amaç, kim olduğu belirsiz 'iş ortakları', önceden işaretli kutu.</p>",
        "incorrect_html": "<p>En görüneni işaretli kutu ama tek kusur o değil. 'Uzman iki formu koşul koşul okuyor' ekranına dön: koşul 1 ve 2 adımları A için ne diyordu?</p>" } },

    // ── OLAY 8 (performans_degerlendirme — SKORLU; kanon-alan: kural değil ARTEFAKT sorulur; kanıt bağı ÇOĞUL) ──
    { "type": "hotspot", "id": "q_kusur", "title": "Skorlu: kusuru metinde göster", "points": 60,
      "evidence_screen_ids": ["artefakt_metinler", "rehber_kosullar"],  // E1 — ÇOĞUL: uyaran artefaktı + rehberlik işlemesi
      "image_asset_id": "form_c_ekran",
      "prompt_html": "<p>Yeni bir form (C) ekranda. Uzman okumasındaki koşullardan BİRİNİ düşüren cümleyi/ögeyi metin üzerinde işaretle.</p>",
      "regions": [
        { "id": "r_kutu", "shape": "rect", "coords": [80, 610, 560, 70], "correct": true,
          "label": "Önceden işaretli 'kabul ediyorum' kutusu" } ],
      "feedback": {
        "correct_html": "<p>Doğru — iradeyi kullanıcı yerine kurgulayan öge bu: koşul-3 okuması (uzman adım 3) C'de de aynı biçimde düşüyor.</p>",
        "incorrect_html": "<p>İşaretlediğin öge üç koşuldan hiçbirini düşürmüyor. Rehber ekranındaki 3. adımın A'da yakaladığı kusuru C'de ara.</p>" } },
    { "type": "mcq", "id": "q_duzeltme", "title": "Skorlu: geçerli kılan düzeltme", "points": 40,
      "evidence_screen_ids": ["artefakt_metinler", "rehber_kosullar"],
      "prompt_html": "<p>Form A'yı geçerli kılmak isteyen ekip TEK değişikliğe bütçe buldu. Uzman okumasına göre en çok koşulu birden ayağa kaldıran değişiklik hangisi?</p>",
      "options": [
        { "id": "a", "text_html": "Tek kutuyu amaç başına ayrı BOŞ kutulara bölmek", "correct": true },
        { "id": "b", "text_html": "Metnin puntosunu büyütüp başlık eklemek" },
        { "id": "c", "text_html": "'Kabul ediyorum'u 'okudum, anladım' yapmak" } ],
      "feedback": {
        "correct_html": "<p>Doğru — amaç başına boş kutu hem belirliliği (amaçlar ayrışır) hem iradeyi (işaret kullanıcıya kalır) kaldırır; B formunun iki gücü A'ya taşınmış olur.</p>",
        "incorrect_html": "<p>Biçimsel rötuş koşul kaldırmaz. Rehber ekranında A'nın düşen koşullarını yeniden say: hangi değişiklik aynı anda ikisine dokunur?</p>" } },

    // ── OLAY 9 (kalicilik_transfer — yeni bağlam varyantı, skorlu; kapanış kavram düzeyinde) ──
    { "type": "mcq", "id": "q_transfer", "title": "Transfer: İK bağlamı", "points": 20,
      "evidence_screen_ids": ["rehber_kosullar"],
      "prompt_html": "<p>Aynı okumayı yeni bağlama taşı: işe alım formundaki 'özgeçmişimin şirket grubu bünyesinde değerlendirilmesini kabul ediyorum' cümlesi, uzman okumasının HANGİ adımındaki kusurla aynı ailedendir?</p>",
      "options": [
        { "id": "a", "text_html": "Koşul 2 ailesi — 'şirket grubu' kim, değerlendirme ne: bilgilendirme boş", "correct": true },
        { "id": "b", "text_html": "Koşul 3 ailesi — kutunun rengi ve konumu" },
        { "id": "c", "text_html": "Hiçbiri — İK formları rıza kapsamı dışındadır" } ],
      "feedback": {
        "correct_html": "<p>Doğru — 'şirket grubu', moda sitesindeki 'iş ortakları' muğlaklığının İK'daki ikizi: bağlam değişti, okuma aynı.</p>",
        "incorrect_html": "<p>Kutunun biçimi bu cümlenin sorunu değil. Rehber ekranındaki 2. adımın A'da yakaladığı muğlaklıkla bu cümleyi yan yana koy.</p>" } },
    { "type": "summary", "id": "kapanis", "title": "Özet", "show_score": true, "show_completion": true,
      "body_html": "<p>Bu kursta üç karar noktasından geçtin: bir rıza metninde amacın nasıl okunacağı, bilgilendirmenin nasıl sınanacağı ve iradenin nereden görüneceği. Sıradaki formu bu üç okumayla aç.</p>" }
  ]
}
```

Denetim izi: skorlu ekranlar (`q_kusur`, `q_duzeltme`, `q_transfer`) → hepsi
`evidence_screen_ids` ile uyaran + rehberlik ekranlarına ÇOĞUL bağlı (`evidence_phases`).
Kanon-alan kuralı işletildi: hiçbir soru "geçerli rızanın koşulları nelerdir?" diye kanonu
sormaz — üç soru da koşulların ARTEFAKTA (Form A/B/C, İK cümlesi) uygulanmasını ölçer; kusurlu
öge yalnız artefakt/kanıt ekranlarında yaşar (K4). Deneme turu `points: 0` (olay 6, Z1) ve
feedback'i olay 7'yi taşır (G1 üç öğe). Kapanış kavram düzeyindedir (K5 — cevap cümlesi
kurmaz). Dokuz olay 8 ekranda: 1+2 ve 6+7 birleşik — "olay ≠ ekran" beyanının kendisi.

## Literatür

- **Birincil:** Gagné, R. M. (1985). *The Conditions of Learning and Theory of Instruction*
  (4. baskı). New York: Holt, Rinehart & Winston — dokuz öğretim olayı + beş öğrenme alanı
  (outcome_types tam listesinin dayanağı).
- Tasarım uygulaması: Gagné, R. M., Briggs, L. J., & Wager, W. W. (1992). *Principles of
  Instructional Design* (4. baskı). Fort Worth: Harcourt Brace Jovanovich — olayların ders/ekran
  tasarımına dönüştürülmesi ("olay = işlev, ekran değil" okumasının kaynağı).
- Olay adlarının çapraz doğrulaması: NIU Center for Innovative Teaching and Learning, "Gagné's
  Nine Events of Instruction" rehberi + SAGE Encyclopedia of Educational Technology (2015),
  "Conditions of Learning: Gagné's Nine Events of Instruction" maddesi.
