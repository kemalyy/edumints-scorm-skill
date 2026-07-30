---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — tandfonline.com/doi/full/10.1080/07370000802212669 +
# ERIC EJ800999): Kapur, M. (2008). "Productive Failure." Cognition and Instruction, 26(3),
# 379–424. — Karmaşık, kötü-yapılandırılmış problemle DESTEKSİZ boğuşma → ardından yapılandırılmış
# konsolidasyon; başarısız denemeler "gizli verimlilik" (hidden efficacy) üretir.
# Faz adları (DOĞRULANDI — Kapur & Bielaczyc 2012, JLS 21(1), 45–83, tandfonline
# 10.1080/10508406.2011.591717): (1) generation & exploration — çözüm ÜRETME/deneme fazı,
# (2) consolidation & knowledge assembly — kanonik çözümün deneme çıktılarıyla karşılaştırılarak
# kurulması. Sınır koşulları (DOĞRULANDI — Sinha & Kapur 2021, RER 91(5), 10.3102/00346543211019105):
# PS-I lehine g≈0.36; küçük yaş/önkoşulsuz gruplarda etki I-PS lehine döner.
pack: productive-failure
name: "Üretken Başarısızlık (Kapur)"
version: 1
outcome_types: [kavram, ilke]
prior_knowledge: [4, 8]
error_cost: [düşük]
requires_platform: [exploration]
phases:
  - id: problem_deneme
    amac: "Generation & exploration — kanonik çözüm GÖSTERİLMEDEN karmaşık problem skorsuz denenir; öğrenenin çözüm denemeleri SAKLANIR (kanıt kaynağının 1. yarısı: K1 türü 5'in 'deneme' ayağı)."
    izinli_ekran_tipleri: [content_slide, exploration, data_chart, image_compare, simulation]
    skorlanabilir: false
  - id: deneme_karsilastirma
    amac: "Deneme çıktıları geri oynatılır ve tipik çözüm yaklaşımlarıyla yan yana konur; her yaklaşımın NEYİ yakalayıp NEREDE kırıldığı görünür kılınır — henüz kanon verilmez."
    izinli_ekran_tipleri: [content_slide, accordion, tabs, data_chart, image_compare]
    skorlanabilir: false
  - id: konsolidasyon
    amac: "Consolidation & knowledge assembly — kanonik çözüm, öğrenenin denemesine AÇIK atıfla kurulur (başarısız deneme + kanonik çözüm karşılaştırması = K1 türü 5'in 'kanon' ayağı)."
    izinli_ekran_tipleri: [worked_example, content_slide, tabs, accordion, video, data_chart]
    skorlanabilir: false
  - id: skorlu_uygulama
    amac: "Kanonik kavram YENİ duruma skorlu uygulanır; kanıt bağı deneme + konsolidasyon ekranlarına ÇOĞUL kurulur."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [problem_deneme, konsolidasyon]
scoring_allowed_from: skorlu_uygulama
conflicts_with: [rosenshine-di]
---

# productive-failure — Üretken Başarısızlık (C6)

**Ne:** Deneme-ÖNCE yöntemin en radikal biçimi. Öğrenen, kanonik çözümü görmeden karmaşık bir
problemle skorsuz boğuşur ve **başarısız olması beklenir** — değer tam buradadır: denemeler
öğrenenin ön-bilgisini etkinleştirir, çözüm uzayının sınırlarını hissettirir ve kanonik çözüm
geldiğinde "neden böyle" sorusunun cevabını kişisel kılar (Kapur 2008'in "hidden efficacy"
bulgusu). **Ne zaman:** kavram/ilke kazanımları, ORTA önbilgi (PK 4–8 — aşağıdaki karar önerisi),
DÜŞÜK hata maliyeti (`5e-inquiry`'nin alternatifi: 5E rehberli keşiftir, PF çözümsüz boğuşmayı
daha uzun ve daha desteksiz tutar). Derin kavramsal anlama ve transfer hedefiyle seçilir;
Sinha & Kapur (2021) meta-analizi deneme-önce tasarımlar lehine orta düzey etki bildirir (g≈0.36).

**Kanıt beyanı (Katman 1 bağlantısı — ÇOĞUL):** `evidence_phases: [problem_deneme,
konsolidasyon]`. Bu paket, kanıt bağlama kuralının (K1) en sıra dışı ama meşru örneğidir: kanıt
kaynağı **K1 türü 5** — "başarısız deneme + kanonik çözüm karşılaştırması" — ve iki yarısı iki
ayrı fazda üretilir: öğrenenin SAKLANAN denemesi (`problem_deneme`) + o denemeye atıfla kurulan
kanonik çözüm (`konsolidasyon`). Skorlu sorular `evidence_screen_ids` (ÇOĞUL — scorm-mcp
CONTRACTS §1.3 E1) ile iki fazın ekranlarına birden bağlanır. Z2 ihlali YOKTUR: denemeler
skorsuzdur (Z3 istisnası bu paketin omurgasıdır — yasak olan deneme değil, denemeyi puanlamaktır).

**Platform şartı (`requires_platform: [exploration]` — F2 olmadan paket kâğıt üstünde kalır):**
K1 türü 5'in "deneme" ayağı, öğrenen çıktısının SAKLANIP sonradan GERİ OYNATILMASINI gerektirir —
`exploration` (F2, YAYINDA: `store_key` + `<span data-exploration-ref="store_key">`) tam bu iştir.
5e-inquiry'nin puan-0 quiz yedeği burada YETMEZ: 5E'de taahhüt tek bir tahmindir ve feedback'le
dolaylı atıf kabul edilebilir; PF'de kanıtın kendisi öğrenenin ürettiği çözüm DENEMESİDİR ve
konsolidasyon o denemeye birebir atıf yapamıyorsa "kendi denemenle karşılaştır" mekaniği taklide
düşer. Bu yüzden beyan serttir: F2 taşımayan hedefte Katman 0 seçici paketi eler — dürüst
alternatif `5e-inquiry`(F2'siz yedeğiyle) ya da `rosenshine-di`dir.

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `problem_deneme` | Kanonsuz, skorsuz boğuşma; deneme SAKLANIR — **kanıt ayağı 1** | content_slide (problem sunumu), exploration*, data_chart, image_compare, simulation | ✗ |
| `deneme_karsilastirma` | Deneme çıktılarının geri oynatımı + tipik yaklaşımların kırılma noktaları | content_slide, accordion, tabs, data_chart, image_compare | ✗ |
| `konsolidasyon` | Kanonik çözüm, denemeye AÇIK atıfla — **kanıt ayağı 2** | worked_example, content_slide, tabs, accordion, video, data_chart | ✗ |
| `skorlu_uygulama` | Yeni duruma skorlu transfer | hepsi | ✓ |

\* `exploration` = `requires_platform` beyanındaki F2 tipi (sunucu çekirdeğinde, 30 tipin
30.'su): `input_kind: "text"` çözüm taslağı/gerekçe notu, `"prediction"`/`"choice"` taahhüt;
girdi `store_key` altında saklanır, sonraki fazlar `data-exploration-ref` ile birebir geri
oynatır. Yapısal skorsuz (puan alanı YOK — Z3), koşulsuz kanıt-taşıyabilir.

Faz notları:

- **Problem KARMAŞIK ve ERİŞİLEBİLİR olmalı:** Kapur'un problemleri kötü-yapılandırılmıştır ama
  öğrenenin ön-bilgisiyle DENENEBİLİR — hiç tutamak vermeyen problem boğuşma değil donma üretir.
  İyi PF problemi çok sayıda makul-ama-eksik çözüm yolu barındırır (aşağıdaki örnekte: tutarlılığı
  aralıkla, ortalama sapmayla, "göz kararı" ile ölçme denemeleri).
- **`problem_deneme`'de İPUCU ve DOĞRULAMA YOK:** destek eklemek paketi 5E'ye çevirir (o zaman
  onu seç, dürüst olur). Yanlış/eksik deneme DEĞERLİDİR ve düzeltilmeden saklanır.
- **`deneme_karsilastirma` kanon SIZDIRMAZ (K5 ile uyum):** tipik yaklaşımların "neyi yakalayıp
  nerede kırıldığı" gösterilir ama doğru çözüm henüz KURULMAZ — kanon bu fazda söylenirse
  konsolidasyonun karşılaştırma işi ölür ve skorlu soruların cevabı erken sızar.
- **`konsolidasyon` denemeden KOPUK ders anlatımına dönüşmemeli:** her kanonik adım, öğrenenin
  denemesindeki bir karara ya da tipik yaklaşımlardan birine bağlanır ("senin taslağın aralığı
  ölçtü; aralık iki uç değere teslimdir — kanonik çözüm her değeri hesaba katar…"). Kopuk
  konsolidasyon, pahalı bir rosenshine-di'dir.
- **`skorlu_uygulama` soruları K2/K4 denetiminden geçmeli:** kavram kamusal kanonsa (istatistik,
  fizik yasası…) soru kanonu değil kanonun YENİ VERİYE uygulanmasını ölçer; yeni veri gövdeye
  değil bir kanıt ekranına konur (K4 — aşağıdaki örnekte `veri_yeni`).

## PF × uzmanlık-tersinme gerilimi ve KARAR ÖNERİSİ (needs-decision çözümü)

**Gerilim:** PF ile uzmanlık-tersinme etkisi (Kalyuga vd. 2003) aynı eksenin iki ucudur.
Rehbersiz problem çözme ACEMİDE verimsizdir (Kirschner, Sweller & Clark 2006): şeması olmayan
öğrenen çözüm uzayında rastgele dolanır, boğuşma üretken değil EZİCİDİR. Aynı destek yüksek
önbilgide TERS teper: akıcı öğrenene çözümlü örnek dozu zaman çalar. PF bu iki uç arasındaki
bantta yaşar — ama bandın alt sınırı beyan edilmezse seçici paketi acemiye önerebilir.

**KARAR ÖNERİSİ (kullanıcı onayına sunulur — PR gövdesinde "Karar önerisi" bölümü):**

1. **PRIOR_KNOWLEDGE alt tabanı: 4/10** (`prior_knowledge: [4, 8]` ön-maddede BAĞLAYICI sert
   kısıttır). Gerekçe literatürden: Kapur'un örneklemleri (2008 on birinci sınıf; Kapur &
   Bielaczyc 2012 yedinci-dokuzuncu sınıf, Singapur devlet okulları) hedef kavramın ÖNKOŞUL
   bilgisine sahipti — ortalama/oran aritmetiği bilen ama varyansı bilmeyen öğrenciler;
   "üretken" başarısızlık, denemeyi kurabilecek kadar malzeme İSTER. Sinha & Kapur (2021)
   sınır koşulları aynı yönü gösterir: küçük yaş gruplarında ve alan-genel becerilerde etki
   I-PS (önce öğretim) lehine döner. PK < 4 profilinde seçici PF'yi ELEMELİ ve `rosenshine-di`
   / `5e-inquiry`(alt sınırı 3) önermelidir. Üst sınır 8: PK > 8'de öğrenen kanonu zaten
   kurabilir — "başarısızlık" üretilemez, zaman maliyeti kalır (`pbl-case` öne geçer).
2. **`error_cost: [düşük]` — yalnız düşük:** başarısızlık TASARIMIN İÇİNDEyse hatanın kurs
   içindeki bedeli sıfıra yakın olmalı; yüksek hata maliyeti alanında (sahada yanlış genelleme
   pahalı) kasıtlı-başarısızlık savunulamaz.
3. **cognitive-load kaplamasıyla çakışma çözümü:** hedef-düzeyi `conflicts_with`'e YAZILMAZ —
   çakışma karar-noktası düzeyindedir ve kaplama tarafında bildirilir
   (`overlays/_FRAMEWORK.md` biçimi: `with: productive-failure · decision_point: destek_dozu ·
   rule:` "paketin kasıtlı-zorluk fazında kaplamanın destek-artırma önerileri askıya alınır;
   paket beyanı önceliklidir"). Yani: cognitive-load kaplaması bu paketle AYNI hedefte
   kullanılabilir; deneme fazının kasıtlı zorluğuna dokunamaz, diğer fazlarda (medya temizliği,
   doz, bölünmüş-dikkat) aynen çalışır. D1 kaplama dosyası yazılırken bu bildirim oraya konur.

## Bu paket NE ZAMAN seçilmemeli

- **Düşük önbilgi (PK &lt; 4 — sert kısıt):** uzmanlık-tersinmenin acemi ucu; şemasız öğrenen
  için boğuşma üretken değil ezicidir (yukarıdaki karar önerisi + Kirschner vd. 2006).
  Önce `rosenshine-di` ile temel kur; PF'yi dizinin ileriki modülüne sakla.
- **Yüksek/orta hata maliyeti (sert kısıt):** güvenlik-kritik prosedürler, klinik kararlar,
  geri alınamaz işlemler — kasıtlı başarısızlık bu alanlarda yanlış genellemeyi prova ettirir;
  gösterim-önce (`rosenshine-di`, karmaşık beceri için `4cid`) seç.
- **Olgu / prosedür kazanımları:** `outcome_types` dışıdır — keşfedilecek kavramsal derinlik
  yoksa boğuşma katma değersiz süre yakar (olgu için `retrieval-spaced`).
- **Dar zaman bütçesi (≤ 5 dk):** gerçek bir boğuşma fazı + karşılaştırma + konsolidasyon
  sığmaz; fazları kırpmak "PF görünümlü anlatım" üretir.
- **F2 (`exploration`) taşımayan hedef:** platform şartı karşılanmaz — deneme saklanamıyorsa
  paketin kanıt mekaniği kurulamaz (yukarıdaki platform notu).

## Çakışmalar (`conflicts_with`)

- `rosenshine-di` — **aynı kazanım üzerinde** birleştirilemez (KARŞILIKLI beyan — C1 paketi bu
  çakışmayı kendi tarafından zaten bildirir): doğrudan öğretim çözümü denemeden ÖNCE gösterir,
  PF denemeyi çözümden önce ister; aynı kazanımda ikisi birden uygulanamaz. Farklı kazanımlarda
  aynı kursta birlikte yaşayabilirler (kapsam HEDEFTİR — `_SCHEMA.md` B2 örneği tam budur).
- `5e-inquiry` bilinçli olarak LİSTEDE DEĞİL: iki yöntem de deneme-önce ailesindendir; aradaki
  fark çakışma değil DOZ kararıdır (5E rehberli keşif + erken açıklama; PF desteksiz boğuşmayı
  daha uzun tutar) — 5E paketi de aynı gerekçeyle PF'yi listelemez, beyanlar simetriktir.
- `cognitive-load` kaplaması LİSTEDE DEĞİL: çakışma hedef-düzeyi değil karar-noktası
  düzeyindedir ve kaplama tarafında `destek_dozu` bildirimi ile çözülür (yukarıdaki karar
  önerisi, madde 3).

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: kavram · PK: 5 · hata maliyeti: düşük): *"İki veri kümesinin tutarlılığını
karşılaştırmak için dağılım (varyans/standart sapma) kavramını kurar ve uygular."* Kitle:
ortalama hesabını akıcı bilen, dağılım kavramını hiç görmemiş yetişkinler (Kapur & Bielaczyc
2012'nin klasik problemi — futbolcu tutarlılığı — kurumsal bağlama uyarlanmış).

```jsonc
{
  "title": "Hangisi Daha Tutarlı? Dağılımı Kendin Kur",
  "description": "Üretken başarısızlık mikrokursu — productive-failure",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "screens": [
    { "type": "title_slide", "title": "Hangisi Daha Tutarlı?", "subtitle": "9 dk · önce SEN dene — yanılmak bu kursun planıdır" },

    // ── FAZ problem_deneme (kanon YOK, ipucu YOK, skor YOK; denemeler SAKLANIR — kanıt ayağı 1) ──
    { "type": "content_slide", "id": "problem_veri", "title": "Problem: iki satış temsilcisi, bir terfi",
      "body_html": "<p>İki temsilcinin son 6 aylık satış adetleri (aylık):<br><b>Aylin:</b> 14 · 9 · 16 · 8 · 15 · 10 — <b>Baran:</b> 12 · 11 · 13 · 12 · 11 · 13.<br>İkisinin de TOPLAMI ve ORTALAMASI aynı (72 adet, ayda 12). Terfi kriteri: <b>istikrar</b>. Hangisi daha tutarlı — ve bunu bir SAYIYLA nasıl gösterirsin? Kanonik yöntem yok; kendi ölçünü kur.</p>" },
    { "type": "exploration", "id": "deneme_tahmin", "title": "Taahhüt: hangisi daha tutarlı?",
      "input_kind": "prediction", "store_key": "pf_tahmin",
      "prompt_html": "<p>Önce taahhüt et — tahminin saklanacak ve kanonik çözümde karşına gelecek.</p>",
      "choices": [
        { "id": "aylin", "text_html": "Aylin" },
        { "id": "baran", "text_html": "Baran" },
        { "id": "esit", "text_html": "Ayırt edilemez — ortalamaları aynı" } ] },
    { "type": "exploration", "id": "deneme_olcut", "title": "Kendi tutarlılık ölçünü tasarla",
      "input_kind": "text", "store_key": "pf_olcut", "min_length": 40,
      "placeholder": "Örn: en büyük ve en küçük ayın farkına bakarım, çünkü…",
      "prompt_html": "<p>Bir SAYI üret: tutarlılığı nasıl ölçerdin? Yöntemini ve 6 aylık verilerle hesapladığın değeri <b>kendi cümlelerinle</b> yaz. Yanlış diye bir şey yok — bu taslak, birazdan kanonik çözümle karşılaştıracağın kanıtındır.</p>" },

    // ── FAZ deneme_karsilastirma (geri oynatma + tipik yaklaşımların kırılma noktaları; kanon HÂLÂ verilmez) ──
    { "type": "content_slide", "id": "karsilastirma", "title": "Denemeler masada: neyi yakaladılar, nerede kırıldılar?",
      "blocks": [
        { "html": "<p>Senin taahhüdün: <b><span data-exploration-ref=\"pf_tahmin\"></span></b> · senin ölçün: <em><span data-exploration-ref=\"pf_olcut\"></span></em>. Şimdi bu problemde en sık kurulan üç ölçüyle yan yana koy:</p>" },
        { "html": "<p><b>Aralık (max−min):</b> farkı tek sayıya indirir — ama yalnız İKİ ayı okur; aradaki dört ay ölçünün dışında kalır. <b>Ortalamadan sapmaların toplamı:</b> her ayı okur — ama artı ve eksi sapmalar birbirini götürür ve toplam hep 0'a çöker. <b>Göz kararı:</b> hızlıdır — ama iki temsilci yakınlaştıkça savunulamaz. Üç yaklaşım da tutarlılığın İZİNİ sürüyor; hiçbiri her değeri hem okuyup hem götürmeden sayamıyor. Eksik olan tek hamle ne olabilir?</p>" } ] },

    // ── FAZ konsolidasyon (kanonik çözüm, denemeye AÇIK atıfla — kanıt ayağı 2) ──
    { "type": "worked_example", "id": "kanonik_cozum", "title": "Kanonik çözüm: sapmaları yok etmeden saymak", "fading": "full",
      "intro_html": "<p>Karşılaştırma ekranındaki kırılma noktası tam şuydu: sapmalar birbirini götürüyor. Kanonik çözüm o tek hamleyi ekler.</p>",
      "steps": [
        { "action_html": "<p><b>Adım 1:</b> her ayın ortalamadan sapmasını yaz (Aylin: +2, −3, +4, −4, +3, −2).</p>",
          "rationale_html": "<p>Tutarlılık ortalamaya uzaklık sorusudur — her ay tek tek okunmalı; aralık ölçüsünün kaçırdığı dört ay burada hesaba girer.</p>" },
        { "action_html": "<p><b>Adım 2:</b> sapmaların KARESİNİ al — işaret yok olur, götürme biter.</p>",
          "rationale_html": "<p>Deneme masasındaki 'toplam 0'a çöker' kırılmasının cevabı: kare alma artı/eksiyi aynı yöne çevirir; büyük sapma orantısızca daha çok sayılır (istikrarsızlık cezası).</p>" },
        { "action_html": "<p><b>Adım 3:</b> karelerin ortalaması = varyans; karekökü = standart sapma. Aylin ≈ 3,1 · Baran ≈ 0,8.</p>",
          "rationale_html": "<p>Tek sayıya iniş, senin ölçünün de hedefiydi — fark şu: bu sayı 6 ayın HEPSİNİ okur ve birimi veriye döner (karekök). Küçük değer = tutarlı: taahhüdünü bu sayıyla sına.</p>" } ] },

    // ── FAZ skorlu_uygulama (SKORLU; yeni veri GÖVDEDE DEĞİL kanıt ekranında — K4; kanıt bağı ÇOĞUL) ──
    { "type": "content_slide", "id": "veri_yeni", "title": "Yeni vaka: iki tedarikçinin teslim süreleri",
      "body_html": "<p>Son 6 teslimatın süreleri (gün):<br><b>Tedarikçi K:</b> 5 · 9 · 4 · 10 · 5 · 9 — <b>Tedarikçi L:</b> 7 · 7 · 8 · 6 · 7 · 7.<br>İkisinin de ortalaması 7 gün.</p>" },
    { "type": "mcq", "id": "q_uygulama", "title": "Skorlu: tutarlı tedarikçiyi seç", "points": 50,
      "evidence_screen_ids": ["deneme_olcut", "kanonik_cozum", "veri_yeni"],  // E1 — ÇOĞUL bağ: deneme (kanıt ayağı 1) + kanon (ayağı 2) + yeni veri artefaktı (K4)
      "prompt_html": "<p>Yeni-vaka ekranındaki iki tedarikçinin ortalaması aynı. Kanonik ölçüyü o verilere uygula: teslimatı öngörülebilir kılmak isteyen ekip hangisini seçmeli, hangi gerekçeyle?</p>",
      "options": [
        { "id": "a", "text_html": "L — sapmaların karesi küçük kalıyor: aynı ortalamada düşük dağılım, öngörülebilirlik demek", "correct": true },
        { "id": "b", "text_html": "K — bazı teslimatları daha hızlı: en iyi ayı öne alan ölçü onu seçer" },
        { "id": "c", "text_html": "Fark yok — ortalamaları eşit olduğuna göre ölçü de eşit çıkar" } ],
      "feedback": {
        "correct_html": "<p>Doğru — ilk problemde kendi ölçünün kırıldığı yerde yaptığın hamlenin aynısı: her değeri oku, işareti yok etmeden say, tek sayıya in.</p>",
        "incorrect_html": "<p>Ortalama eşitken karar dağılımdan çıkar. 'Kanonik çözüm' ekranındaki 3 adımı grafikteki değerlere uygula — en iyi tek ay ya da ortalama eşitliği ölçü değildir.</p>" } },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Denetim izi: skorlu tek ekran (`q_uygulama`) → `evidence_screen_ids: ["deneme_olcut",
"kanonik_cozum", "veri_yeni"]` — ÇOĞUL bağ: K1 türü 5'in iki ayağı (saklanan deneme + kanonik
çözüm) + yeni-vaka verisi bir kanıt ekranında (K4: sayılar gövdede DEĞİL `veri_yeni`
artefaktında yaşar; gövde ona atıf yapar). Deneme ekranları yapısal skorsuz (`exploration` — puan alanı YOK, Z3);
`deneme_karsilastirma` kanonu SÖYLEMEZ (K5: kanon yalnız `kanonik_cozum`'da kurulur); skor
yalnız `skorlu_uygulama` fazında. `store_key`'ler kurs genelinde TEKİL.

## Literatür

- **Birincil:** Kapur, M. (2008). *Productive Failure.* Cognition and Instruction, 26(3),
  379–424. https://doi.org/10.1080/07370000802212669
- Faz tasarımı: Kapur, M., & Bielaczyc, K. (2012). *Designing for Productive Failure.* Journal
  of the Learning Sciences, 21(1), 45–83 — generation & exploration + consolidation & knowledge
  assembly fazları; Singapur örneklemlerinin önkoşul-bilgi profili (PK tabanının gerekçesi).
- Sınır koşulları: Sinha, T., & Kapur, M. (2021). *When Problem Solving Followed by Instruction
  Works: Evidence for Productive Failure.* Review of Educational Research, 91(5), 761–798 —
  PS-I lehine g≈0.36; küçük yaş/alan-genel becerilerde tersine dönüş (karar önerisinin meta-analitik dayanağı).
- Karşı kutup (acemi ucu): Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). *Why Minimal
  Guidance During Instruction Does Not Work.* Educational Psychologist, 41(2), 75–86; uzmanlık-tersinme:
  Kalyuga vd. (2003), *The Expertise Reversal Effect.*
