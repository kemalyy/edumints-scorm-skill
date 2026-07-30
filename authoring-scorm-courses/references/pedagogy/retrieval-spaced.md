---
# Birincil kaynaklar (DOĞRULANDI, 2026-07-30 — journals.sagepub.com/doi/abs/10.1111/j.1467-9280
# .2006.01693.x + scirp.org kayıtları): Roediger, H. L., III, & Karpicke, J. D. (2006).
# "Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention." Psychological
# Science 17(3), 249–255 — geri getirme DENEMESİ, aynı süreyi yeniden-okumaya harcamaktan daha
# kalıcıdır (testing effect); geciktirilmiş sınamada test grubu yeniden-okuma grubunu geçer.
# Aralık: Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). "Distributed
# Practice in Verbal Recall Tasks: A Review and Quantitative Synthesis." Psychological Bulletin
# 132(3), 354–380 (DOĞRULANDI — yorku.ca/ncepeda + digitalcommons.usf.edu kayıtları): 317 deney
# sentezi; aralıklı pratik > yığılmış pratik; en iyi çalışma-arası aralık, hatırlama-ufkuyla
# birlikte BÜYÜR (kurs-DİZİSİ notunun dayanağı).
pack: retrieval-spaced
name: "Geri Getirme + Aralıklı Pratik (tazeleme)"
version: 1
outcome_types: [olgu, kavram, prosedür]
prior_knowledge: [7, 10]
error_cost: [düşük, orta, yüksek]
requires_platform: []
phases:
  - id: on_yoklama
    amac: "Yeniden-sunumdan ÖNCE skorsuz geri getirme denemesi: öğrenen önceki kurstan kalanı hafızadan çeker (testing effect'in üretim ayağı — Z3: deneme puanlanmaz)."
    izinli_ekran_tipleri: [mcq, true_false, fill_blank, flashcards, matching, exploration]
    skorlanabilir: false
  - id: referans_artefakt
    amac: "Yoğun referans artefaktı yeniden sunulur (tek-sayfalık özet tablo/çizelge — önceki kursun damıtılmış içeriği): KANIT FAZI — bu kurstaki tüm skorlu sorular buraya bağlanır."
    izinli_ekran_tipleri: [content_slide, accordion, tabs, timeline, data_chart, image_compare, flashcards]
    skorlanabilir: false
  - id: aralikli_turlar
    amac: "Düşük-bahisli geri getirme turları: skorsuz, ARTAN aralıkla (turlar arası mesafe büyür); her madde grubu en az iki tur görür."
    izinli_ekran_tipleri: [adaptive_practice, mcq, true_false, fill_blank, flashcards, matching, sorting]
    skorlanabilir: false
    sonraki: [aralikli_turlar, karisik_pratik]
    tekrar_kosulu: "Bir madde grubu artan aralıkla en az iki tur görmediyse (ya da tur başarısı düşükse) yeni bir geri getirme turu açılır; tüm gruplar iki turunu tamamladıysa karisik_pratik fazına geçilir."
  - id: karisik_pratik
    amac: "Karışık (interleaved) pratik: madde grupları bloklar halinde değil HARMANLANARAK sorulur — ayırt etme becerisi son kez skorsuz yoklanır."
    izinli_ekran_tipleri: [adaptive_practice, mcq, matching, drag_drop, fill_blank, term_match_race]
    skorlanabilir: false
  - id: summatif_tur
    amac: "SKORLU summatif tur: sorular referans artefakta bağlı (evidence_screen_ids), kritik olgu yalnız artefakt ekranında yaşar (K4)."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phase: referans_artefakt
scoring_allowed_from: summatif_tur
conflicts_with: []
---

# retrieval-spaced — Geri Getirme + Aralıklı Pratik (C12)

**Ne:** TAZELEME paketi — İLK öğretim YAPMAZ. Önceki bir kursun/eğitimin öğrettiği olgu, kavram
ve prosedür bilgisinin kalıcılığını iki kanıtlı mekanizmayla yeniler: **geri getirme pratiği**
(hatırlamayı yeniden OKUMAK değil hafızadan ÜRETMEK pekiştirir — Roediger & Karpicke 2006) ve
**aralıklı pratik** (aynı toplam süre, araya mesafe konarak dağıtıldığında daha kalıcıdır —
Cepeda vd. 2006, 317 deneyin sentezi). Akış: yeniden-sunumdan ÖNCE skorsuz geri getirme
denemesi (`on_yoklama`) → yoğun referans artefaktının yeniden sunumu (`referans_artefakt`) →
artan aralıklı skorsuz turlar (`aralikli_turlar` döngüsü) → karışık pratik (`karisik_pratik`) →
skorlu summatif tur. **Ne zaman:** olgu ağırlıklı hızlı tazeleme, YÜKSEK önbilgi (PK 7–10 —
içerik daha önce öğrenilmiş olmalı), dar zaman bütçesi (seçici örnek 6: bu profilde en yüksek
getiri); yıllık zorunlu tazeleme kursları, sertifika yenileme, sınav öncesi pekiştirme.

**Kanıt beyanı ve DÜRÜSTLÜK NOTU (Katman 1 bağlantısı — bu paketin en ince ayarı):**
`evidence_phase: referans_artefakt` (TEKİL — bilinçli: kanıt üreten tek faz budur; yoklama ve
turlar kanıt üretmez, çağırır). İnce ayar şudur: bu paketin soruları, İÇERİK olarak ÖNCEKİ
kursun öğrettiğini test eder — önceki kursu görmüş öğrenen soruları kaynaksız da cevaplayabilir
ve K2 denetim sorusu ("alanı bilen cevaplar mı?") harfiyen uygulanırsa her tazeleme sorusu
şüpheye düşer. Paket bunu ŞÖYLE çözer, başka türlü değil: **kanıt = BU kurstaki yeniden-sunum
ekranlarıdır.** Skorlu her soru `evidence_screen_ids` ile `referans_artefakt` ekran(lar)ına
bağlanır; kritik olgu (eşik değeri, etiket adı, adım sırası, tarih) YALNIZ o ekranlarda yaşar
(K4) ve soru gövdesi ona atıf yapar. Böylece kurs, kendi içinde denetlenebilir kalır: kör test
artefaktı söktüğünde sorular düşer. Yeniden-sunumu atlayıp "nasılsa önceki kurs öğretti" diye
soru sormak bu paketin KÖTÜYE KULLANIMIDIR — o kurs tazeleme değil ANKETTİR ve v1'in iddia+quiz
desenini arka kapıdan geri getirir. Önceki kursun varlığı kurs briefine YAZILIR (hangi eğitim,
hangi kapsam); yazılamıyorsa bu paket seçilemez.

**Sıkıştırılmış-kaynak girdisinin meşru alanı:** referans artefaktı, önceki kursun damıtılmış
tek-sayfalık özetidir (tablo, çizelge, karar ağacı) — yol haritasındaki sıkıştırılmış-kaynak
girdisi (G3) tam bu fazı besler. Meşruiyetin sınırı aynı dürüstlük notudur: sıkıştırılmış kaynak
YENİDEN-SUNUM içindir, ilk öğretimin yerine geçmez.

**Platform notu (`requires_platform: []`):** çekirdek tipler yeter — turlar `mcq`/`fill_blank`/
`flashcards` ile kurulabilir. `adaptive_practice` (BKT modu) turların DOĞAL taşıyıcısıdır:
madde havuzu + ustalık kestirimi, "hangi grup ikinci turunu görmedi" muhasebesini kendiliğinden
yapar ve akıcı öğreneni erken durdurur — varsa tercih et, yokluğu paketi elemez.

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `on_yoklama` | Yeniden-sunumdan ÖNCE hafızadan çekme denemesi | mcq, true_false, fill_blank, flashcards, matching, exploration | ✗ |
| `referans_artefakt` | Damıtılmış yeniden-sunum — **KANIT** | content_slide, accordion, tabs, timeline, data_chart, image_compare, flashcards | ✗ |
| `aralikli_turlar` | Artan aralıklı skorsuz turlar (döngü: grup başına ≥ 2 tur) | adaptive_practice, mcq, true_false, fill_blank, flashcards, matching, sorting | ✗ |
| `karisik_pratik` | Harmanlanmış son yoklama (interleaving) | adaptive_practice, mcq, matching, drag_drop, fill_blank, term_match_race* | ✗ |
| `summatif_tur` | Artefakta bağlı SKORLU ölçüm | hepsi | ✓ |

\* `term_match_race` süreli oyundur: yalnız `allow_extend` + `allow_disable` ile (WCAG 2.2.1 —
platform doğrulayıcısı zorlar); süre bonusu geçme kararına yazılamaz.

Faz notları:

- **Geri getirme YENİDEN-SUNUMDAN ÖNCE gelir (Z3 ile temiz):** testing effect'in gücü,
  cevabı GÖRMEDEN hatırlamaya çalışmaktadır — başarısız deneme bile sonraki yeniden-sunumun
  kodlamasını güçlendirir. `on_yoklama` bu yüzden artefakttan ÖNCE durur ve `points: 0` taşır:
  Z2 ihlali yoktur çünkü skor yoktur (Z3 istisnası — yasak olan deneme değil, denemeyi
  puanlamaktır). Yoklama sorularının feedback'i cevabı VERMEZ ("birazdan tabloda göreceksin"),
  verirse yeniden-sunumun işini çalar.
- **Aralık, kurs içinde EKRAN MESAFESİDİR — ve dürüst sınırı vardır:** gerçek aralık etkisi
  günler/haftalar ölçeğindedir; tek oturumluk SCORM kursu bunu ancak minyatürde taklit eder
  (tur 1 artefakttan hemen sonra, tur 2 başka bir madde grubunun araya girmesiyle daha uzak).
  Cepeda vd. (2006) bulgusunun asıl karşılığı KURS DİZİSİDİR: optimum çalışma-arası aralık,
  hatırlama ufkuyla büyür — yıllık yeterlilik hedefi haftalar-arası tazeleme kursları ister.
  Tek kursun "aralıklı" iddiası bu sınır notuyla birlikte beyan edilir.
- **Artan aralık + grup başına ≥ 2 tur:** `tekrar_kosulu` bunun muhasebesidir — her madde grubu
  en az iki turda, ikincisi ilkinden daha UZAK konumda yoklanır. Tek turluk "tazeleme" yeniden
  okumadan farksızlaşır.
- **Karışık pratik ayırt etmeyi çalıştırır:** bloklu pratik (önce hep A grubu, sonra hep B)
  cevap stratejisini sızdırır ("bu bölümdeyiz, cevap A ailesinden"); `karisik_pratik` grupları
  harmanlar — özellikle karıştırılabilir etiket/eşik çiftlerinde (interleaving bulgusu).
- **Summatif tur PARALEL maddeler kullanır:** skorsuz turların sorularını aynen tekrarlamak
  ezber sızıntısıdır (öğrenen içeriği değil o soruyu öğrenir) ve K6 riskini büyütür; aynı
  olguları ölçen FARKLI maddeler yazılır.

## Bu paket NE ZAMAN seçilmemeli — SERT UYARI

- **İLK kez öğretilen kavram/prosedür (en kritik yasak):** bu paket kanıt ÜRETMEZ, yeniden
  sunar — ilk öğretimde kullanılırsa referans artefaktı "öğretmeden özetleyen" bir duvar
  tablosuna, sorular ankete döner. Denetim sorusu: *"öğrenen bu içeriği hangi kursta İLK kez
  öğrendi?"* — cevabı "bu kursta" ise paket YANLIŞTIR; ilk öğretim türe göre `rosenshine-di`,
  `mastery-learning`, `5e-inquiry`… ister. Bu kötüye kullanım, v1'in iddia+quiz deseninin ta
  kendisidir ve bu paketin varlık sebebi o deseni geri getirmek değil, tazeleme İSTİSNASINI
  dürüst sınırlarla tanımlamaktır.
- **Düşük/orta önbilgi (PK &lt; 7 — sert kısıt):** hatırlanacak şema yoksa geri getirme boşa
  çeker; "yarısını öğrenmişti" profili tazeleme değil yeniden öğretim ister
  (`mastery-learning` düzeltici döngüsü).
- **Tutum kazanımları:** `outcome_types` dışıdır — tutum geri-getirme ile pekişmez, deneyim +
  yansıtma döngüsü ister (`kolb-experiential`).
- **Anlama/transfer AÇIĞI varsa:** geri getirme, VAR OLAN anlamayı kalıcılaştırır; yanlış
  anlaşılmış kavramı hızlandırılmış tekrarla "düzeltmek" yanlışı pekiştirir — önce teşhis
  (`mastery-learning` formatif kapısı), sonra tazeleme.
- **Önceki kurs/kapsam beyan edilemiyorsa:** brief'e "neyin tazelendiği" yazılamıyorsa bu
  paket seçilemez (yukarıdaki dürüstlük notu).

## Çakışmalar (`conflicts_with`)

Boş — bilinen hedef-düzeyi çakışma yok, gerekçesi: bu paketin ön şartı (içerik daha önce
öğrenilmiş, PK 7–10) onu İLK-öğretim paketlerinin tamamından zaten ayırır — aynı hedefte "hem
ilk öğretim hem tazeleme" diye bir yarışma kurulamaz; kuruluyorsa hedef yanlış tanımlanmıştır
(iki ayrı hedef/kurstur). `pbl-case` ile PK bandı kesişir (7–10) ama outcome kesişimi dardır ve
sıra beyanları çelişmez (vaka çözümü ↔ tazeleme farklı işlerdir); aynı hedefte yarışırlarsa
hakem hedefin doğasıdır (karar/strateji → pbl-case, kalıcılık → retrieval-spaced) ve seçim
gerekçeyle yazılır.

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: olgu · PK: 8 · hata maliyeti: orta): *"Şirketin üç veri sınıflandırma
etiketini (Gizli / Hizmete Özel / Kamuya Açık) doğru belgeye uygular."* Bağlam: yıllık bilgi
güvenliği TAZELEMESİ — etiketler ve kuralları geçen yılki oryantasyon kursunda öğretildi
(brief beyanı); etiket şeması kurum-içidir (K2 temiz). Referans artefaktı: tek-sayfalık
sınıflandırma tablosu (sıkıştırılmış-kaynak girdisinin meşru kullanımı).

```jsonc
{
  "title": "Veri Etiketleri: Yıllık Tazeleme",
  "description": "Geri getirme + aralıklı pratik mikrokursu — retrieval-spaced",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 },
  "screens": [
    { "type": "title_slide", "title": "Veri Etiketleri Tazelemesi", "subtitle": "5 dk · önce hatırla, sonra bak — sıra önemli" },

    // ── FAZ on_yoklama (yeniden-sunumdan ÖNCE, skorsuz; feedback cevap VERMEZ) ──
    { "type": "fill_blank", "id": "yoklama_etiket", "title": "Önce hafızandan (puan yok)", "points": 0,
      "prompt_html": "<p>Geçen yılki eğitimden: maaş bordroları hangi etiketi taşır? Bilemiyorsan boş bırakma — tahmin et; deneme yeniden-görmeden daha kalıcıdır.</p>",
      "blanks": [ { "id": "b1", "accepted": ["gizli"] } ],
      "feedback": {
        "correct_html": "<p>Hafızan sıcak — birazdan tabloda üç etiketin tam sınırlarını yeniden göreceksin.</p>",
        "incorrect_html": "<p>Sorun değil — hatırlamaya çalışmanın kendisi işe yaradı. Cevabı söylemiyorum: bir sonraki ekrandaki tabloda kendin bul.</p>" } },

    // ── FAZ referans_artefakt (KANIT: damıtılmış tek-sayfalık tablo — kritik olgular YALNIZ burada) ──
    { "type": "accordion", "id": "ref_tablo", "title": "Referans: üç etiket, tek sayfa",
      "items": [
        { "title": "GİZLİ — kırmızı etiket", "content_html": "<p>Kişiye özel ve mali veriler: bordro, sağlık raporu, müşteri kimlik kopyası. Kural: yalnız isimli yetki listesiyle erişim; e-postayla GÖNDERİLMEZ, güvenli paylaşım alanı kullanılır.</p>" },
        { "title": "HİZMETE ÖZEL — sarı etiket", "content_html": "<p>İç işleyiş belgeleri: süreç şemaları, iç fiyat listeleri, toplantı notları. Kural: şirket hesaplarıyla paylaşılabilir; kurum DIŞINA sözleşmesiz çıkmaz.</p>" },
        { "title": "KAMUYA AÇIK — yeşil etiket", "content_html": "<p>Yayınlanmış içerik: basın bültenleri, ürün broşürleri, kariyer ilanları. Kural: serbest paylaşım; tek şart güncel sürümün kullanılması.</p>" } ] },

    // ── FAZ aralikli_turlar — TUR 1 (artefakttan hemen sonra; skorsuz) ──
    { "type": "mcq", "id": "tur1_bordro", "title": "Tur 1 (puan yok)", "points": 0,
      "prompt_html": "<p>Tablodan taze: bir çalışanın sağlık raporu hangi etiketle işlenir?</p>",
      "options": [
        { "id": "a", "text_html": "Kırmızı — kişiye özel veri ailesinden", "correct": true },
        { "id": "b", "text_html": "Sarı — iç işleyiş belgesi sayılır" } ],
      "feedback": {
        "correct_html": "<p>Doğru — kişiye özel/mali aile kırmızıda: erişim isimli listeyle, e-posta yasak (tablonun 1. satırı).</p>",
        "incorrect_html": "<p>Sağlık raporu iç işleyiş değil KİŞİYE ÖZEL veridir. Referans tablosunun kırmızı satırına yeniden bak.</p>" } },

    // Araya mesafe: farklı madde grubu (sarı/yeşil sınırı) — tur 2'nin aralığını bu blok açar
    { "type": "flashcards", "id": "grup2_kartlar", "title": "Sarı ↔ yeşil sınırı (kendini yokla)",
      "cards": [
        { "front_html": "<p>İç fiyat listesi</p>", "back_html": "<p>SARI — kurum dışına sözleşmesiz çıkmaz.</p>" },
        { "front_html": "<p>Basın bülteni</p>", "back_html": "<p>YEŞİL — tek şart güncel sürüm.</p>" },
        { "front_html": "<p>Süreç şeması</p>", "back_html": "<p>SARI — şirket hesaplarıyla paylaşım serbest, dışarı sözleşmeyle.</p>" } ] },

    // ── FAZ aralikli_turlar — TUR 2 (aynı grup, ARTAN aralık: araya grup-2 bloğu girdi; skorsuz) ──
    { "type": "mcq", "id": "tur2_kirmizi_kanal", "title": "Tur 2 (puan yok — aralık büyüdü)", "points": 0,
      "prompt_html": "<p>Az önce değil, İKİ blok önce gördün: kırmızı etiketli bir dosyayı ekip arkadaşına nasıl ulaştırırsın?</p>",
      "options": [
        { "id": "a", "text_html": "Güvenli paylaşım alanından, isimli yetkiyle", "correct": true },
        { "id": "b", "text_html": "Şirket e-postasıyla — iç yazışma sayılır" } ],
      "feedback": {
        "correct_html": "<p>Doğru — kırmızının kanal kuralı e-postayı kapatır; mesafeye rağmen hatırlaman aralıklı pratiğin tam amacı.</p>",
        "incorrect_html": "<p>Şirket e-postası SARININ kanalıdır, kırmızının değil. Referans tablosunun kırmızı satırındaki kanal kuralına dön.</p>" } },

    // ── FAZ karisik_pratik (gruplar HARMANLANIR; skorsuz) ──
    { "type": "matching", "id": "karisik_eslestir", "title": "Karışık pratik (puan yok): belgeyi etiketle", "points": 0,
      "prompt_html": "<p>Üç grup bir arada — bloklu düzen yok, her belge kendi kuralını ister.</p>",
      "pairs": [
        { "left_html": "<p>Müşteri kimlik kopyası</p>", "right_html": "<p>Kırmızı</p>" },
        { "left_html": "<p>Toplantı notu</p>", "right_html": "<p>Sarı</p>" },
        { "left_html": "<p>Kariyer ilanı</p>", "right_html": "<p>Yeşil</p>" } ],
      "feedback": {
        "correct_html": "<p>Üç aile üç kural: kişiye özel → isimli erişim; iç işleyiş → dışarı sözleşmeyle; yayınlanmış → güncel sürüm.</p>",
        "incorrect_html": "<p>Karıştırılan sınır genelde sarı-yeşil sınırıdır: 'yayınlanmış MI, iç işleyiş Mİ?' Referans tablosunun sarı ve yeşil satırlarını yan yana oku.</p>" } },

    // ── FAZ summatif_tur (SKORLU: PARALEL maddeler; kanıt bağı referans artefakta) ──
    { "type": "mcq", "id": "q_sum_vaka", "title": "Skorlu: yeni belge, doğru işlem", "points": 100,
      "evidence_screen_ids": ["ref_tablo"],  // E1 — kanıt: BU kurstaki yeniden-sunum artefaktı (evidence_phase: referans_artefakt)
      "prompt_html": "<p>Elinde iki belge var: (1) tedarikçiyle imzalanacak iç fiyat listesi, (2) yeni ürünün yayınlanmış broşürü. Referans tablosuna göre doğru işlem çifti hangisi?</p>",
      "options": [
        { "id": "a", "text_html": "Listeyi sözleşme eşliğinde paylaş; broşürün güncel sürümünü serbestçe gönder", "correct": true },
        { "id": "b", "text_html": "İkisini de serbestçe paylaş — ikisi de kurum dışına çıkacak belgeler" },
        { "id": "c", "text_html": "İkisini de güvenli alandan isimli yetkiyle gönder — dış paylaşım hep kırmızı kuralına tabidir" } ],
      "feedback": {
        "correct_html": "<p>Doğru — iki ayrı aile, iki ayrı kural: sarının dış-paylaşım şartı sözleşme, yeşilin tek şartı güncellik. Kuralları tek kalıba indirmemek tazelemenin özüydü.</p>",
        "incorrect_html": "<p>İki belge aynı ailede değil. Referans tablosunda sarı ve yeşil satırların ÇIKIŞ kurallarını yeniden karşılaştır — tablo bu sorunun tek kaynağıdır.</p>" } },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Denetim izi: skorlu tek ekran (`q_sum_vaka`) → `evidence_screen_ids: ["ref_tablo"]` — kanıt,
BU kurstaki yeniden-sunum artefaktıdır (dürüstlük notunun uygulaması: etiket kuralları yalnız
`ref_tablo`'da yaşar, K4; soru gövdesi tabloya atıf yapar). Yoklama ve turlar `points: 0`
(Z1/Z3) ve `on_yoklama` feedback'i cevabı VERMEZ. Aralık mekaniği görünür: `tur1` artefakttan
hemen sonra, `tur2` aynı madde grubunu iki blok SONRA yoklar (artan aralık); `karisik_eslestir`
üç grubu harmanlar (interleaving). Summatif madde, skorsuz turların sorularını tekrarlamayan
PARALEL bir vakadır (K6 temiz). Önceki kursun beyanı ("geçen yılki oryantasyon") brief'te.

## Literatür

- **Birincil (geri getirme):** Roediger, H. L., III, & Karpicke, J. D. (2006). *Test-Enhanced
  Learning: Taking Memory Tests Improves Long-Term Retention.* Psychological Science, 17(3),
  249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x — test etme, eş süreli yeniden
  okumadan daha kalıcı (geciktirilmiş sınamada tersine çevrilemeyen fark).
- **Birincil (aralık):** Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D.
  (2006). *Distributed Practice in Verbal Recall Tasks: A Review and Quantitative Synthesis.*
  Psychological Bulletin, 132(3), 354–380 — 317 deneyin sentezi; optimum çalışma-arası aralık
  hatırlama ufkuyla büyür (kurs-dizisi notunun dayanağı).
- Sınıf uygulaması: Roediger, H. L., III, & Karpicke, J. D. (2006). *The Power of Testing
  Memory: Basic Research and Implications for Educational Practice.* Perspectives on
  Psychological Science, 1(3), 181–210 — düşük-bahisli sık yoklamanın uygulama ilkeleri
  (turların skorsuzluğunun dayanağı).
