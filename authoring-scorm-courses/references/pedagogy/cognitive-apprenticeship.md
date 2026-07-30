---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — scirp.org referans kaydı + researchgate 334349642 +
# isls.org "Cognitive Apprenticeship" + aft.org/ae/winter1991/collins_brown_holum özeti):
# Collins, A., Brown, J. S., & Newman, S. E. (1989). "Cognitive Apprenticeship: Teaching the
# Crafts of Reading, Writing, and Mathematics." L. B. Resnick (Ed.), Knowing, Learning, and
# Instruction: Essays in Honor of Robert Glaser içinde (s. 453–494). Hillsdale, NJ: Erlbaum.
# — Çekirdek iddia: uzman DÜŞÜNMESİ görünmezdir; öğretim onu görünür kılmalıdır ("making
# thinking visible"). Altı yöntem (doğrulanan adlar): modeling, coaching, scaffolding (+fading),
# articulation, reflection, exploration. Popülerleştirilmiş anlatım: Collins, Brown & Holum
# (1991), "Cognitive Apprenticeship: Making Thinking Visible," American Educator 15(3).
pack: cognitive-apprenticeship
name: "Bilişsel Çıraklık (Collins, Brown & Newman)"
version: 1
outcome_types: [prosedür, problem çözme, ilke]
prior_knowledge: [2, 8]
error_cost: [düşük, orta]
requires_platform: [worked_example, exploration]
phases:
  - id: modelleme
    amac: "Uzman, görevi SESLİ-DÜŞÜNEREK icra eder: her adımda ne yaptığı DEĞİL neden ve neyi gözeterek yaptığı görünür kılınır (worked_example gerekçesi = uzmanın iç konuşması) — 1. kanıt kaynağı."
    izinli_ekran_tipleri: [worked_example, video, content_slide]
    skorlanabilir: false
  - id: kocluk
    amac: "Öğrenen aynı görev ailesini SKORSUZ dener; ipucu ve gerekçeli düzeltme anında gelir (koçun işi: gözle, yakala, düzelt)."
    izinli_ekran_tipleri: [simulation, adaptive_practice, mcq, true_false, fill_blank, branching, drag_drop, sorting]
    skorlanabilir: false
  - id: iskele_soluklastirma
    amac: "Destek KASITLI olarak azaltılır (scaffolding + fading): gerekçeler kapanır, adımlar öğrenene devredilir (worked_example partial → problem_only ilerleyişi)."
    izinli_ekran_tipleri: [worked_example, simulation, drag_drop, sorting, fill_blank]
    skorlanabilir: false
  - id: dile_getirme
    amac: "Articulation — öğrenen stratejisini KENDİ CÜMLELERİYLE yazar; metin SAKLANIR (exploration text) — 2. kanıt kaynağı (K1 türü 2: öğrenenin kendi ürettiği çıktı)."
    izinli_ekran_tipleri: [exploration, poll]
    skorlanabilir: false
  - id: yansitma
    amac: "Reflection — saklanan dile-getirme geri oynatılır ve uzman modelinin gerekçeleriyle YAN YANA konur; fark noktaları adlandırılır."
    izinli_ekran_tipleri: [content_slide, tabs, accordion, image_compare]
    skorlanabilir: false
  - id: kesif
    amac: "Exploration (CBN'nin 6. yöntemi) — öğrenen YENİ bir problemi bağımsız çözer; skorlu ölçüm burada yaşar ve kanıt bağı model + dile-getirme ekranlarına ÇOĞUL kurulur."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [modelleme, dile_getirme]
scoring_allowed_from: kesif
conflicts_with: [productive-failure, 5e-inquiry]
---

# cognitive-apprenticeship — Bilişsel Çıraklık (C11)

**Ne:** "Düşünmeyi görünür kılma" paketi (Collins, Brown & Newman 1989). Geleneksel çıraklıkta
usta işi göstererek öğretir; bilişsel işlerde gösterilecek şey KAFANIN İÇİDİR — bu yüzden paket,
uzman icrasını sesli-düşünme olarak modeller (`modelleme`), öğreneni koç gözetiminde denetir
(`kocluk`), desteği kasıtlı soluklaştırır (`iskele_soluklastirma`), öğrenenden stratejisini
KENDİ CÜMLELERİYLE istemesini (`dile_getirme`), kendi stratejisini uzmanınkiyle karşılaştırmasını
(`yansitma`) ve yeni problemde bağımsız uçmasını (`kesif`) ister. Altı faz, CBN'nin altı
yönteminin birebir karşılığıdır. **Ne zaman:** uzman muhakemesi isteyen prosedür / problem çözme
/ ilke kazanımları — strateji görünmezse öğrenen yalnız YÜZEYİ taklit eder (adımları ezberler,
kararları kuramaz); orta önbilgi bandı (PK 2–8), düşük-orta hata maliyeti.

**Kanıt beyanı (Katman 1 bağlantısı — ÇOĞUL):** `evidence_phases: [modelleme, dile_getirme]`.
Kanıt iki kaynaktan gelir ve bu paketin ayırt edici imzasıdır: (1) uzmanın sesli-düşünme modeli —
`worked_example` adımlarının `rationale_html` alanı burada uzman İÇ KONUŞMASIDIR ("burada önce
X'e bakarım çünkü…"), eylem listesi değil (K1 türü 1); (2) öğrenenin SAKLANAN dile-getirmesi —
`exploration` (`input_kind: "text"`, `store_key`) ile kaydedilen strateji metni (K1 türü 2:
öğrenenin KENDİ ürettiği çıktı). Skorlu sorular `evidence_screen_ids` (ÇOĞUL — scorm-mcp
CONTRACTS §1.3 E1) ile iki kaynağa birden bağlanabilir; yansıtma ekranı öğrenenin metnine
`data-exploration-ref` ile birebir atıf yapar — "muhtemelen şöyle düşündün" taklidi YASAKTIR.
`kocluk` ve `iskele_soluklastirma` kanıt fazı DEĞİLDİR: deneme ve devir üretir, yeni kanıt üretmez.

**Platform şartı (`requires_platform: [worked_example, exploration]` — ikisi de YAYINDA):**

1. **`worked_example` (F1):** sesli-düşünme modelinin taşıyıcısı — adım = eylem + gerekçe çifti;
   `fading: "full" → "partial" → "problem_only"` ilerleyişi `iskele_soluklastirma` fazının
   MOTORUDUR (destek azaltma şemaya gömülü).
2. **`exploration` (F2):** dile-getirme kayıt cihazı — issue'nun öngördüğü doğal eşleşme;
   F2 yayında olduğundan `fill_blank`/`poll` yaklaşımları GEÇİCİ YEDEK olmaktan çıkarıldı ve
   şart sertleştirildi: dile-getirme saklanamıyorsa yansıtma fazının karşılaştırması ve kanıt
   beyanının 2. ayağı kurulamaz — paket elenir (dürüst alternatif: `rosenshine-di` ya da
   karmaşık beceri için `4cid`).

## Faz rehberi

| Faz (CBN yöntemi) | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `modelleme` (modeling) | Uzman sesli-düşünmesi — **kanıt 1** | worked_example, video, content_slide | ✗ |
| `kocluk` (coaching) | Skorsuz deneme + anında gerekçeli düzeltme | simulation, adaptive_practice, mcq, true_false, fill_blank, branching, drag_drop, sorting | ✗ |
| `iskele_soluklastirma` (scaffolding+fading) | Desteğin kasıtlı azaltılması, adım devri | worked_example (partial/problem_only), simulation, drag_drop, sorting, fill_blank | ✗ |
| `dile_getirme` (articulation) | Öğrenenin strateji metni SAKLANIR — **kanıt 2** | exploration (text), poll | ✗ |
| `yansitma` (reflection) | Öğrenen metni ↔ uzman modeli yan yana | content_slide, tabs, accordion, image_compare | ✗ |
| `kesif` (exploration) | YENİ problemde bağımsız, SKORLU icra | hepsi | ✓ |

Faz notları:

- **Gerekçe = iç konuşma, ansiklopedi değil:** modelleme adımının `rationale_html`'i "bu adım
  önemlidir çünkü…" ders cümlesi değil, uzmanın O ANKİ karar konuşmasıdır ("ilk cümleye önce
  öfke var mı diye bakarım; varsa özürden önce kabul cümlesi kurarım…"). Ders cümlesiyle yazılan
  model, paketi pahalı bir rosenshine-di'ye çevirir.
- **Koçluk turunda feedback anında ve gerekçelidir (G1):** koçun işi doğruyu söylemek değil,
  öğrenenin akıl yürütmesindeki kırılmayı ADLANDIRMAKTIR — `incorrect_html` yanılgıyı adlandırır
  ve model ekranının ilgili adımına geri işaret eder. Koçluk skorSUZdur (Z1): gözetimli deneme
  puanlanırsa deneme-güvenliği ölür.
- **Soluklaştırma GERÇEKTEN soluklaştırır:** `iskele_soluklastirma` fazında aynı `fading: "full"`
  örneğini tekrarlamak faz sahteciliğidir — en az bir ekran `partial` (gerekçeleri öğrenen
  kurar) ya da `problem_only` (adımları öğrenen açar) olmalıdır. Devredilmeyen destek, çıraklığın
  "usta gider, iş kalır" hedefini boşa düşürür.
- **Dile getirme yönergesi SOMUT ister:** "ne öğrendin?" değil — "bu görev ailesinde SENİN karar
  sıran ne? Üç adımını ve her adımda neye baktığını yaz" (min_length ile boş geçiş kapanır).
  Saklanan metin yanlış/eksik olabilir ve ÖYLE KALIR: yansıtma fazının malzemesi tam budur.
- **Yansıtma cevap sızdırmaz (K5):** uzman modeliyle karşılaştırma, skorlu soruların cevabını
  yeniden cümlelemeden yapılır — fark NOKTALARI adlandırılır ("senin sıranda kabul cümlesi
  yoktu"), yeni problemin cevabı kurulmaz.
- **Keşif fazı YENİ problem ister:** modellenen görevin aynısını skorlamak taklidi ölçer,
  stratejiyi değil. Skorlu ekran, aynı görev AİLESİNDEN yeni bir örnek üzerinde karar sorar ve
  gövde-yeterlilik denetiminden (K4) geçer.

## Bu paket NE ZAMAN seçilmemeli

- **Düşük süre bütçeli mikro kurs (≤ 5 dk):** altı faz sığmaz; modelleme + quiz'e kırpılan
  çıraklık, `rosenshine-di`nin kötü kopyasıdır — o zaman onu seç.
- **Saf olgu hedefi:** `outcome_types` dışıdır — dile getirilecek strateji yoksa articulation
  fazı boş anket üretir (olgu için `retrieval-spaced`, tanım/sınıflama için `rosenshine-di`).
- **Yüksek hata maliyeti (sert kısıt):** koçluk/keşif fazları öğrenen hatasını çalışma malzemesi
  yapar; sahaya yakın yüksek-bedelli icra, ölçüte-karşı tatbikat ister (`sim-drill` — akıcılık
  eşiği + parça-görev döngüsü). Çıraklığın "hata = konuşulacak şey" kültürü, "hata = alarm"
  alanına taşınmaz.
- **Çok yüksek önbilgi (PK &gt; 8):** stratejisi zaten kurulu öğrenene modelleme + koçluk
  bürokrasidir; `pbl-case` (bağımsız vaka) doğru araçtır.
- **Platform F1/F2 taşımıyorsa:** sesli-düşünme modeli ve dile-getirme kaydı kurulamaz —
  paket elenir (yukarıdaki platform notu).

## Çakışmalar (`conflicts_with`)

- `productive-failure` — **aynı kazanım üzerinde** birleştirilemez (KARŞILIKLI beyan — C6
  dosyası kendi tarafından bildirir): PF kanonik çözüm GÖSTERİLMEDEN boğuşma ister, çıraklık
  uzman modeliyle AÇILIR; ortak `ilke` kazanımında iki sıra beyanı taban tabana zıttır. Farklı
  kazanımlarda aynı kursta birlikte yaşayabilirler (kapsam HEDEFTİR — `_SCHEMA.md`).
- `5e-inquiry` — **aynı kazanım üzerinde** birleştirilemez (KARŞILIKLI beyan — C3 dosyası kendi
  tarafından bildirir): 5E açıklamayı keşiften SONRAYA saklar, çıraklık modeli BAŞA koyar;
  ortak `ilke` kazanımında ve kesişen PK bandında (3–7) ikisi de elemeden sağ çıkabilir —
  çakışma beyanı bu yüzden gerçek ve gereklidir.
- `rosenshine-di` LİSTEDE DEĞİL — bilinçli: ikisi de gösterim-önce ailesindendir, sıra
  beyanları uyumludur; aradaki fark çakışma değil DERİNLİK kararıdır (adım icrası yeterliyse
  rosenshine-di; karar stratejisinin kendisi hedefse çıraklık — dile getirme + yansıtma
  fazları farkı taşır). `4cid` için de aynı gerekçe geçerlidir (bütün-görev basitten karmaşığa
  dizisi ≠ strateji görünürlüğü; iki paket aynı hedefte yarışırsa seçim gerekçeyle yazılır).

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: problem çözme · PK: 4 · hata maliyeti: orta): *"Öfkeli bir müşteri
şikayet e-postasına, gerilimi düşüren ve çözüm adımı taahhüt eden bir yanıt stratejisi kurar."*
Bağlam: müşteri hizmetleri gelişim programı — CBN'nin ana sahası olan YAZMA becerisi; strateji
(kabul → sınır → taahhüt sırası ve her adımda neye bakıldığı) uzmanın kafasındadır ve
görünür kılınmadan öğretilemez.

```jsonc
{
  "title": "Öfkeli E-postaya Yanıt: Uzman Gibi Düşün",
  "description": "Bilişsel çıraklık mikrokursu — cognitive-apprenticeship",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "screens": [
    { "type": "title_slide", "title": "Uzman Gibi Düşün", "subtitle": "10 dk · önce ustanın kafasının içini izle, sonra kendi stratejini kur" },

    // ── FAZ modelleme (KANIT 1: sesli-düşünme — gerekçe = iç konuşma) ──
    { "type": "content_slide", "id": "vaka_eposta", "title": "Gelen e-posta: 'Üçüncü kez yazıyorum!'",
      "body_html": "<p><em>\"Üçüncü kez yazıyorum ve hâlâ kargom yok. Paramı çaldınız. Bugün çözülmezse tüketici hakem heyetine gidiyorum ve her platforma yazacağım.\"</em></p>" },
    { "type": "worked_example", "id": "model_strateji", "title": "Uzman yanıtı kurarken sesli düşünüyor", "fading": "full",
      "intro_html": "<p>Kıdemli temsilci aynı e-postayı açtı. Yazdığı cümleler değil, YAZMADAN ÖNCE kafasından geçenler asıl ders.</p>",
      "steps": [
        { "action_html": "<p><b>Adım 1 — Önce duyguyu okurum, konuyu değil:</b> ilk cümlem kabul cümlesi: 'Üç kez yazmak zorunda kalmanız kabul edilebilir değil.'</p>",
          "rationale_html": "<p>İç konuşma: 'Öfkeli okuyucu ilk cümlede kendini arar — orada süreç savunması görürse gerisini okumaz. Haklılık payını ÖNCE ben söylersem tehdit gündemden düşer.'</p>" },
        { "action_html": "<p><b>Adım 2 — Sınırı suçlamasız çizerim:</b> 'çaldınız' ifadesini tartışmam; olguyu nötr dille yeniden kurarım: 'ödemeniz bekleyen siparişinizde görünüyor.'</p>",
          "rationale_html": "<p>İç konuşma: 'Suçlamayı düzeltmeye kalkarsam davaya girerim; görmezden gelirsem kabullenmiş olurum. Üçüncü yol: olguyu kendi dilimle, sıfat kullanmadan yeniden yazmak.'</p>" },
        { "action_html": "<p><b>Adım 3 — Taahhüdü TARİHLİ ve TEK adımlı veririm:</b> 'yarın 17.00'a kadar kargo takip numaranızı bu e-postadan ileteceğim.'</p>",
          "rationale_html": "<p>İç konuşma: ''En kısa sürede' öfkeli okuyucuda üçüncü ihanettir. Küçük ama tarihli tek taahhüt seçerim — tutabileceğimden emin olduğum ve müşterinin takip edebileceği bir adım.'</p>" } ] },

    // ── FAZ kocluk (SKORSUZ deneme + anında gerekçeli düzeltme) ──
    { "type": "mcq", "id": "kocluk_ilk_cumle", "title": "Koçluk turu (puan yok): ilk cümleyi sen seç", "points": 0,
      "prompt_html": "<p>Benzer bir öfkeli e-postaya yanıt yazıyorsun. İlk cümlen hangisi olurdu?</p>",
      "options": [
        { "id": "a", "text_html": "\"Yaşattığımız gecikme ve üç kez yazmak zorunda kalmanız kabul edilebilir değil.\"", "correct": true },
        { "id": "b", "text_html": "\"Kargo süreçlerimiz yoğunluk nedeniyle uzayabilmektedir.\"" },
        { "id": "c", "text_html": "\"Hırsızlık iddianızı kabul etmediğimizi belirtmek isteriz.\"" } ],
      "feedback": {
        "correct_html": "<p>Uzmanın 1. adım iç konuşması: öfkeli okuyucu ilk cümlede kendini arar — kabul cümlesi tehdidi gündemden düşürür.</p>",
        "incorrect_html": "<p>Süreç savunması ya da suçlama tartışması — ikisi de uzmanın 1. ve 2. adımda bilerek KAÇINDIĞI hamleler. 'Sesli düşünüyor' ekranındaki 1. adımın iç konuşmasına dön.</p>" } },

    // ── FAZ iskele_soluklastirma (destek azalır: gerekçeleri ÖĞRENEN kurar) ──
    { "type": "worked_example", "id": "iskele_yari", "title": "Şimdi gerekçeler sende: adımlar açık, nedenler kapalı", "fading": "partial",
      "intro_html": "<p>Aynı strateji, yeni e-posta (iade edilmeyen ücret). Adımlar açık; her adımın NEDENİNİ önce kendin kur, sonra uzmanınkiyle karşılaştır.</p>",
      "self_explanation_prompt_html": "<p>Açmadan önce: bu adım öfkeli okuyucuda neyi engelliyor?</p>",
      "steps": [
        { "action_html": "<p><b>Adım 1:</b> 'İki haftadır iadenizin yapılmamış olması kabul edilebilir değil.'</p>",
          "rationale_html": "<p>Kabul cümlesi önce — okuyucu haklılığını ilk cümlede bulur, savunma refleksi devreye girmez.</p>" },
        { "action_html": "<p><b>Adım 2:</b> 'Dolandırıcılık' ifadesine cevap yok; olgu nötr: 'iade tutarınız sistemde onay bekliyor.'</p>",
          "rationale_html": "<p>Suçlamayı ne tartış ne kabullen — olguyu sıfatsız yeniden kur.</p>" },
        { "action_html": "<p><b>Adım 3:</b> 'Perşembe 12.00'a kadar iade onay ekran görüntüsünü ileteceğim.'</p>",
          "rationale_html": "<p>Tarihli, tek, tutulabilir taahhüt — 'en kısa sürede' yasak.</p>" } ] },

    // ── FAZ dile_getirme (KANIT 2: öğrenenin strateji metni SAKLANIR) ──
    { "type": "exploration", "id": "strateji_metni", "title": "Stratejini kendi cümlelerinle yaz",
      "input_kind": "text", "store_key": "ca_strateji", "min_length": 60,
      "placeholder": "1) Önce ... çünkü ... 2) Sonra ... çünkü ... 3) En son ... çünkü ...",
      "prompt_html": "<p>Öfkeli bir şikayet e-postası açtığında SENİN karar sıran ne? Üç adımını ve her adımda NEYE baktığını yaz. Metnin saklanacak ve birazdan uzmanınkiyle yan yana gelecek.</p>" },

    // ── FAZ yansitma (öğrenen metni ↔ uzman modeli; fark adlandırılır, cevap kurulmaz) ──
    { "type": "content_slide", "id": "yansitma_karsilastirma", "title": "Senin stratejin uzmanınkiyle yan yana",
      "blocks": [
        { "html": "<p><b>Senin yazdığın:</b> <em><span data-exploration-ref=\"ca_strateji\"></span></em></p>" },
        { "html": "<p>Uzman modeliyle karşılaştır ve üç noktayı yokla: (1) İLK adımın okuyucunun duygusuna mı, kendi sürecine mi bakıyor? (2) Suçlamalı ifadeye bir cevabın var mı — tartışmak ve görmezden gelmek dışında üçüncü bir yol kurdun mu? (3) Taahhüdünde bir TARİH var mı? Eksik bulduğun nokta hata değil, keşif turunun çalışma listesi.</p>" } ] },

    // ── FAZ kesif (SKORLU: YENİ problem, bağımsız karar; kanıt bağı ÇOĞUL) ──
    { "type": "content_slide", "id": "vaka_yeni", "title": "Yeni vaka: sosyal medyadan gelen şikayet",
      "body_html": "<p><em>\"Mağazanızda kasada bekletildim, personel yüzüme bakmadı. Videoyu çektim, yarın paylaşıyorum. Bu nasıl hizmet?\"</em> — kanal farklı, gerilim aynı.</p>" },
    { "type": "mcq", "id": "q_kesif", "title": "Skorlu: yanıt stratejisini kur", "points": 100,
      "evidence_screen_ids": ["model_strateji", "strateji_metni", "vaka_yeni"],  // E1 — ÇOĞUL: uzman modeli (kanıt 1) + öğrenenin dile-getirmesi (kanıt 2) + yeni vaka artefaktı (K4)
      "prompt_html": "<p>Yeni-vaka ekranındaki mesaja yanıt kuruyorsun. Kendi yazdığın stratejiyle uzman modelini birlikte uygula: hangi plan üç karar noktasını da doğru kurar?</p>",
      "options": [
        { "id": "a", "text_html": "Bekletilme deneyimini kabul et → video tehdidini tartışmadan olguyu nötr kur → mağaza yöneticisinin YARIN saat vererek arayacağını taahhüt et", "correct": true },
        { "id": "b", "text_html": "Videonun izinsiz paylaşımının hukuki sonuçlarını hatırlat → sonra hizmet standardını anlat" },
        { "id": "c", "text_html": "Özür dile ve 'en kısa sürede ilgileneceğiz' güvencesi ver" } ],
      "feedback": {
        "correct_html": "<p>Doğru — üç karar noktası da yerinde: kabul önce (tehdit gündemden düşer), suçlama/tehdit tartışılmadan olgu nötr kurulur, taahhüt tarihli ve tek. Kendi stratejinde eksik bulduğun nokta varsa bu planla kapat.</p>",
        "incorrect_html": "<p>Hukuki hatırlatma 2. adımın 'davaya girme' tuzağının ta kendisi; 'en kısa sürede' ise 3. adımın yasakladığı taahhüt. Uzman modelinin iç konuşmalarına ve kendi yazdığın stratejiye geri dön.</p>" } },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true,
      "body_html": "<p>Bu kursta bir stratejiyi üç kez kurdun: uzmanın kafasında izledin, kendi cümlelerinle yazdın, yeni vakada uyguladın. Sıradaki zor e-postada karar sıran artık görünür.</p>" }
  ]
}
```

Denetim izi: skorlu tek ekran (`q_kesif`) → `evidence_screen_ids: ["model_strateji",
"strateji_metni", "vaka_yeni"]` — ÇOĞUL bağ: uzman modeli (kanıt 1) + öğrenenin SAKLANAN
dile-getirmesi (kanıt 2 — öğrenenin kendi çıktısı kanıt kaynağıdır, K1 türü 2) + yeni-vaka
artefaktı (K4: vaka olgusu gövdede değil `vaka_yeni` ekranında yaşar). Koçluk turu `points: 0`
(Z1), soluklaştırma ekranı `fading: "partial"` (destek gerçekten azalır), yansıtma ekranı
`data-exploration-ref` ile birebir atıf yapar ve cevap cümlesi kurmaz (K5 — karar noktalarını
adlandırır). `store_key` kurs genelinde tekil.

## Literatür

- **Birincil:** Collins, A., Brown, J. S., & Newman, S. E. (1989). *Cognitive Apprenticeship:
  Teaching the Crafts of Reading, Writing, and Mathematics.* L. B. Resnick (Ed.), *Knowing,
  Learning, and Instruction: Essays in Honor of Robert Glaser* içinde (s. 453–494). Hillsdale,
  NJ: Lawrence Erlbaum Associates — altı yöntem: modeling, coaching, scaffolding (+fading),
  articulation, reflection, exploration.
- Popüler anlatım: Collins, A., Brown, J. S., & Holum, A. (1991). *Cognitive Apprenticeship:
  Making Thinking Visible.* American Educator, 15(3), 6–11, 38–46 — "düşünmeyi görünür kılma"
  formülasyonu ve okuma/yazma/matematik örnekleri.
- İskele kavramının kökeni: Wood, D., Bruner, J. S., & Ross, G. (1976). *The Role of Tutoring
  in Problem Solving.* Journal of Child Psychology and Psychiatry, 17(2), 89–100 — scaffolding
  teriminin kaynağı (soluklaştırma fazının arka planı).
