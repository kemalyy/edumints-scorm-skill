---
# Birincil kaynaklar (DOĞRULANDI, 2026-07-30 — journals.sagepub.com/doi/10.3102/00346543068002179 +
# ERIC EJ574600): de Jong, T., & van Joolingen, W. R. (1998). "Scientific Discovery Learning with
# Computer Simulations of Conceptual Domains." RER 68(2), 179–201 — çıplak simülasyon YETMEZ;
# öğretimsel destek (model gösterimi, yapılandırılmış görev, çözümleme) şarttır — bu paketin faz
# iskeletinin gerekçesi. Tatbikat mekaniği: Ericsson, K. A., Krampe, R. Th., & Tesch-Römer, C.
# (1993). "The Role of Deliberate Practice in the Acquisition of Expert Performance." Psychological
# Review 100(3), 363–406 (DOĞRULANDI — scirp.org kayıt + royalsocietypublishing 10.1098/rsos.190327
# yeniden-ziyaret makalesi): kasıtlı pratik = zayıf noktaya odaklı, geri bildirimli, tekrarlı
# çalışma. Parça-görev: Wightman, D. C., & Lintern, G. (1985). "Part-Task Training for Tracking
# and Manual Control." Human Factors 27(3), 267–283 (DOĞRULANDI — sagepub
# 10.1177/001872088502700304): segmentation / fractionation / simplification + yeniden bütünleştirme.
pack: sim-drill
name: "Simülasyon Tatbikatı (psikomotor/prosedürel drill)"
version: 1
outcome_types: [psikomotor, prosedür]
prior_knowledge: [1, 8]
error_cost: [düşük, orta, yüksek]
requires_platform: [simulation, worked_example, exploration]
phases:
  - id: brifing
    amac: "Görevin hedefi, başarı ölçütü (doğruluk + akıcılık eşiği) ve kurallar beyan edilir — tatbikatın 'neyi, hangi ölçüte karşı' sorusu ekrana yazılır."
    izinli_ekran_tipleri: [content_slide, tabs, accordion, video]
    skorlanabilir: false
  - id: gosterim_turu
    amac: "Uzman, görevi gerekçeli adımlarla BİR KEZ eksiksiz icra eder (model çalıştırma: her adım eylem + neden) — 1. kanıt kaynağı (K1 türü 1)."
    izinli_ekran_tipleri: [worked_example, video, content_slide, image_compare]
    skorlanabilir: false
  - id: serbest_deneme
    amac: "SKORSUZ deneme turu: öğrenen görevi (ya da parça-görevi) simülasyonda dener; deneme gözlemi/duraksama noktası exploration ile SAKLANIR — çözümlemenin hammaddesi."
    izinli_ekran_tipleri: [simulation, exploration]
    skorlanabilir: false
  - id: cikti_cozumleme
    amac: "Saklanan deneme çıktısı geri oynatılır ve model icrayla karşılaştırılır; hatalı/yavaş kalan ALT-GÖREV teşhis edilir — 2. kanıt kaynağı (K1 türü 3+5)."
    izinli_ekran_tipleri: [content_slide, image_compare, tabs, accordion, data_chart, branching]
    skorlanabilir: false
    sonraki: [serbest_deneme, senaryolu_olcum]
    tekrar_kosulu: "Çözümlemede bir alt-görev hâlâ hatalı ya da akıcılık ölçütünün altındaysa YALNIZ o alt-görev için serbest_deneme fazına dön (parça-görev turu); tüm alt-görevler ölçütü karşılıyorsa senaryolu_olcum fazına geç."
  - id: senaryolu_olcum
    amac: "YENİ bir senaryo varyantında skorlu bütün-görev icrası; kanıt bağı model gösterimi + çözümleme ekranlarına ÇOĞUL kurulur."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [gosterim_turu, cikti_cozumleme]
scoring_allowed_from: senaryolu_olcum
conflicts_with: []
---

# sim-drill — Simülasyon Tatbikatı (C9)

**Ne:** Gösterim-önce tatbikat paketi: uzman icrayı gerekçeli adımlarla BİR KEZ gösterir
(`gosterim_turu`), öğrenen aynı görevi güvenli try-mode simülasyonda **skorsuz** dener
(`serbest_deneme`), deneme çıktısı saklanır ve model icrayla karşılaştırılarak zayıf alt-görev
teşhis edilir (`cikti_cozumleme`), teşhis edilen alt-görev **parça-görev turlarıyla** ölçüte
gelene dek tekrar edilir (döngü) ve skor YALNIZ yeni senaryo varyantındaki bütün-görev icrasına
verilir (`senaryolu_olcum`). Mekanizmanın üç dayanağı: çıplak simülasyon öğretmez, yapılandırılmış
destek ister (de Jong & van Joolingen 1998); ilerleme kasıtlı pratikten gelir — zayıf noktaya
odaklı, geri bildirimli tekrar (Ericsson vd. 1993); karmaşık görev parçalanıp yeniden
bütünleştirilerek çalışılır (Wightman & Lintern 1985: segmentation/fractionation/simplification).
**Ne zaman:** psikomotor (zaman baskılı akıcı icra) ve prosedür kazanımları; hata maliyeti yüksek
alanlarda özellikle değerli — tatbikat, sahada pahalı olan hatayı kurs içinde ucuzlatır (seçici
örnek 7: psikomotor/prosedür · hata maliyeti yüksek · platformda simülasyon → `sim-drill` +
`accessibility`).

**Kanıt beyanı (Katman 1 bağlantısı — ÇOĞUL):** `evidence_phases: [gosterim_turu,
cikti_cozumleme]`. Kanıt iki kaynaktan gelir: (1) model icranın gerekçeli adımları (K1 türü 1 —
çözümlü örnek), (2) öğrenenin SAKLANAN deneme çıktısının model ile karşılaştırıldığı çözümleme
(K1 türü 3 "simülasyon/deneme çıktısı" + türü 5 "deneme + kanonik icra karşılaştırması").
Simülasyon ekranı bu pakette ÇİFT şapkalıdır: `serbest_deneme`'de pratik aracıdır (points 0,
deneme-güvenli — Z3), çıktısı `cikti_cozumleme`'de kanıta dönüşür. Skorlu sorular
`evidence_screen_ids` (ÇOĞUL — scorm-mcp CONTRACTS §1.3 E1) ile iki fazın ekranlarına birden
bağlanır. `serbest_deneme`'nin kendisi kanıt fazı DEĞİLDİR: ham deneme tek başına kanıt taşımaz,
çözümlemede modelle karşılaştırıldığında kanıtlaşır.

**Platform şartı (`requires_platform: [simulation, worked_example, exploration]`):**

1. **`simulation`:** tatbikatın taşıyıcısı — adım adım try-mode (ekran görüntüsü + tık bölgesi /
   metin girişi; yanlışta ipucu). `serbest_deneme`'de `points: 0`, `senaryolu_olcum`'da skorlu.
2. **`worked_example`:** model çalıştırmanın taşıyıcısı — mevcut `simulation` tipi 1. adımdan
   pratik ister (gösterimsiz); gösterim turu bu yüzden ayrı tiple (eylem + gerekçe çifti) kurulur.
3. **`exploration` (F2, YAYINDA — `store_key` + `data-exploration-ref`):** deneme çıktısının
   SAKLANMASI şarttır — `simulation` tipi çıktı saklamaz; öğrenenin deneme gözlemi ("hangi adımda
   durakladım / neyi yanlış tıkladım") exploration ile kaydedilir ve çözümleme ekranı ona birebir
   atıf yapar. F2'siz "denemeni modelle karşılaştır" cümlesi taklittir — paket elenir.

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `brifing` | Hedef + başarı ölçütü + kurallar | content_slide, tabs, accordion, video | ✗ |
| `gosterim_turu` | Uzmanın gerekçeli model icrası — **kanıt 1** | worked_example, video, content_slide, image_compare | ✗ |
| `serbest_deneme` | Skorsuz try-mode; deneme gözlemi SAKLANIR | simulation (points 0), exploration | ✗ |
| `cikti_cozumleme` | Deneme ↔ model karşılaştırması; zayıf alt-görev teşhisi — **kanıt 2** (→ parça-görev döngüsü) | content_slide, image_compare, tabs, accordion, data_chart, branching | ✗ |
| `senaryolu_olcum` | YENİ senaryoda skorlu bütün-görev icrası | hepsi | ✓ |

Faz notları:

- **Parça-görev döngüsü (Wightman & Lintern 1985):** `cikti_cozumleme → serbest_deneme` dönüşü
  BÜTÜN görevi değil teşhis edilen ALT-GÖREVİ tekrar eder (fractionation: akıcılık isteyen parça
  yalıtılır; simplification: hız/karmaşıklık düşürülerek başlanabilir). Son tur her zaman
  **yeniden bütünleştirir**: skorlu ölçüm bütün-görevdir, parça-görev asla skorlanmaz — parçada
  akıcı olmak bütünde akıcı olmak değildir.
- **Kasıtlı pratik ≠ kör tekrar (Ericsson vd. 1993):** aynı görevi aynı biçimde N kez oynatmak
  tatbikat değildir. Her tekrar turu çözümlemenin TEŞHİSİNE bağlanır (hangi alt-görev, hangi
  ölçüt) ve simülasyonun adım-içi ipuçları geri bildirimi anında verir. Teşhissiz tekrar turu
  eklemek paketi "aynı oyunu üç kez oyna" slop'una çevirir.
- **Akıcılık ölçütü brifingde BEYAN edilir:** psikomotor kazanımın tanımı zaman baskılı icradır;
  "hatasız VE ≤ N saniye/adım" ölçütü brifing ekranına yazılır ki çözümlemenin "yavaş kaldın"
  teşhisi keyfî kalmasın.
- **Süreli oyun varyantları (WCAG 2.2.1 — platform doğrulayıcısı ZORLAR):** akıcılık tatbikatına
  süreli oyun (`game` zamanlayıcı mekaniği, `term_match_race`) eklenebilir — YALNIZ
  `allow_extend: true` + `allow_disable: true` ile (süre uzatılabilir/kapatılabilir olmalı;
  sunucu doğrulayıcısı aksini reddeder). Süre baskısı akıcılık ÖLÇÜTÜ değil pratik DOZUDUR:
  süreyi kapatan öğrenen aynı içeriği süresiz tatbik eder; skorlu ölçümde geçme kararı süre
  bonusuna bağlanamaz.
- **Deneme gözlemi exploration ile saklanır:** simülasyon turunun hemen ardından tek soruluk
  exploration ("hangi adımda durakladın / neyi ilk denedin?") — çözümleme ekranı
  `data-exploration-ref` ile bu nota birebir atıf yapar. "Denemen muhtemelen şöyleydi" diye
  yazmak (saklamadan) taklittir.

## Bu paket NE ZAMAN seçilmemeli

- **Simülasyona değmeyecek basit olgu/kavram kazanımları:** `outcome_types` dışıdır — tık
  bölgeli try-mode'a sarılmış tanım ezberi, pahalı bir flashcards'tır (olgu için
  `retrieval-spaced`, kavram için `5e-inquiry` / `rosenshine-di`).
- **Platform şartı karşılanmıyorsa:** `simulation` + `worked_example` + `exploration` üçlüsünden
  biri yoksa paket elenir — "adımları oku, aklında dene" tatbikat değildir; dürüst alternatif
  `rosenshine-di` (rehberli → bağımsız pratik) ya da karmaşık beceri için `4cid`tir.
- **Tek oturumluk mikro kurs (≤ 5 dk):** gösterim + deneme + çözümleme + parça-tur + skorlu
  ölçüm sığmaz; döngü kırpılırsa paket "izle ve quiz çöz"e yozlaşır (o zaman `rosenshine-di`).
- **Kötü yapılandırılmış problem alanları:** tatbikat TEK doğru icrası olan görevlerde çalışır;
  savunulabilir çok-çözümlü stratejik kararlar `pbl-case` / `cognitive-apprenticeship` işidir.
- **Çok yüksek önbilgi (PK &gt; 8):** icrası zaten akıcı öğrenene gösterim turu + parça-görev
  döngüsü boş bürokrasidir; kalıcılık bakımı `retrieval-spaced` ile daha ucuzdur.

## Çakışmalar (`conflicts_with`)

Boş — bilinen hedef-düzeyi çakışma yok, gerekçesi: `psikomotor`da yarışan başka paket yok;
`prosedür` kesişimindeki adaylarla (`rosenshine-di`, `4cid`, `mastery-learning`) ilişki çakışma
değil SEÇİM kararıdır — üçü de gösterim-önce ailesindendir, sıra beyanları çelişmez; hakem
platform şartı ve görev doğasıdır (kas-hafızalı/zaman-baskılı icra + simülasyon varsa sim-drill;
simülasyonsuz prosedür anlatımı rosenshine-di; çok-beceri bütün görev 4cid). Deneme-önce
paketlerle (`productive-failure`, `5e-inquiry`) outcome kesişimi boştur — aynı hedefte zaten
yarışamazlar, beyan gereksizdir.

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: psikomotor · PK: 2 · hata maliyeti: yüksek): *"Yangın alarm panelinde
tahliye anonsunu 60 saniye içinde, adım atlamadan başlatır."* Bağlam: tesis görevlisi
oryantasyonu; panel arayüzü kurum-içidir (K2 temiz). Parça-görev döngüsü SCORM'da `branching`
ile simüle edilir: çözümleme sonrası iki yol — zayıf alt-görev turu ya da skorlu ölçüm.

```jsonc
{
  "title": "Tahliye Anonsu: 60 Saniyede Hatasız",
  "description": "Simülasyon tatbikatı mikrokursu — sim-drill",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 },
  "screens": [
    { "type": "title_slide", "title": "Tahliye Anonsu Tatbikatı", "subtitle": "8 dk · önce izle, sonra güvenle yanıl — skor en sonda" },

    // ── FAZ brifing (hedef + ölçüt + kurallar) ──
    { "type": "content_slide", "id": "brifing_olcut", "title": "Görev ve ölçüt",
      "body_html": "<p>Görev: panelde tahliye anonsunu başlatmak. Ölçüt: <b>üç adım, doğru sırada, toplam 60 saniye içinde</b>. Bu kursta iki deneme turu skorsuz — yanılmak tatbikatın parçası. Skor yalnız son senaryoda.</p>" },

    // ── FAZ gosterim_turu (KANIT 1: model icra, gerekçeli adımlar) ──
    { "type": "worked_example", "id": "model_icra", "title": "Model icra: görevli anonsu başlatıyor", "fading": "full",
      "intro_html": "<p>Uzman görevli aynı paneli kullanıyor — her adımda NE yaptığına değil, NEDEN o sırayla yaptığına bak.</p>",
      "steps": [
        { "action_html": "<p><b>Adım 1 — Yetki anahtarı:</b> anahtar 'Denetim' konumuna çevrilir.</p>",
          "rationale_html": "<p>Panel yetkisiz dokunuşa kilitlidir: anahtar çevrilmeden hiçbir tuş işlemez — 1. adım atlanırsa sonraki tıklar sessizce yutulur ve saniyeler kaybolur.</p>" },
        { "action_html": "<p><b>Adım 2 — Bölge seçimi:</b> tahliye edilecek bölgenin tuşuna basılır (ör. B-Blok).</p>",
          "rationale_html": "<p>Anons bölgeye gider: bölge seçilmeden başlatılan anons TÜM binaya çalar — gereksiz tahliye, gerçek acilde paniğin ta kendisidir.</p>" },
        { "action_html": "<p><b>Adım 3 — Anons başlat:</b> 'Tahliye Anonsu' tuşuna basılı tutulur (3 sn).</p>",
          "rationale_html": "<p>Basılı tutma kazara dokunmayı eler; tuş kısa basışta bilerek tepki vermez — 'çalışmıyor' sanıp panele vurmak en sık acemi hatasıdır.</p>" } ] },

    // ── FAZ serbest_deneme (SKORSUZ try-mode + deneme gözlemi SAKLANIR) ──
    { "type": "simulation", "id": "deneme_tam", "title": "Dene: anonsu kendin başlat (puan yok)", "points": 0,
      "prompt_html": "<p>Aynı panel, senin elinde. Yanlış tık = anında ipucu; puan yok, sayaç yok — bu tur öğrenmek için.</p>",
      "steps": [
        { "instruction_html": "<p><b>1.</b> Paneli işleme aç</p>", "image_asset_id": "panel_kapali",
          "regions": [ { "id": "r_anahtar", "shape": "rect", "coords": [40, 320, 120, 90], "correct": true, "hint": "Tuşlar kilitli — önce yetki anahtarı." } ] },
        { "instruction_html": "<p><b>2.</b> B-Blok için bölgeyi seç</p>", "image_asset_id": "panel_acik",
          "regions": [ { "id": "r_bolge", "shape": "rect", "coords": [300, 180, 90, 60], "correct": true, "hint": "Anons nereye gidecek? Bölge tuşları orta sırada." } ] },
        { "instruction_html": "<p><b>3.</b> Anonsu başlat</p>", "image_asset_id": "panel_bolge_secili",
          "regions": [ { "id": "r_anons", "shape": "rect", "coords": [520, 340, 110, 70], "correct": true, "hint": "Kısa basış yetmez — tuşu basılı tut." } ] } ] },
    { "type": "exploration", "id": "deneme_gozlem", "title": "Deneme gözlemin",
      "input_kind": "choice", "store_key": "drill_zayif_adim",
      "prompt_html": "<p>Hangi adımda durakladın ya da ipucuna düştün? Cevabın saklanacak — çözümleme ekranı onunla çalışacak.</p>",
      "choices": [
        { "id": "a1", "text_html": "Adım 1 — yetki anahtarı" },
        { "id": "a2", "text_html": "Adım 2 — bölge seçimi" },
        { "id": "a3", "text_html": "Adım 3 — basılı tutma" },
        { "id": "a0", "text_html": "Hiçbirinde — akıcı geçtim" } ] },

    // ── FAZ cikti_cozumleme (KANIT 2: deneme ↔ model karşılaştırması + parça-görev kararı) ──
    { "type": "content_slide", "id": "cozumleme", "title": "Denemen masada: modelle karşılaştır",
      "body_html": "<p>Takıldığını söylediğin adım: <b><span data-exploration-ref=\"drill_zayif_adim\"></span></b>. Model icrayla yan yana koy: en sık kayıp <b>1. adımın atlanmasıdır</b> — kilitli panelde tık yutulur ve görevli 'bozuk' sanır; ikinci kayıp 3. adımda kısa basıştır — tuş 3 sn basılı tutulmadan tepki vermez. Bölge seçilmeden başlatılan anons ise tüm binaya çalar: hata sessiz değil PAHALIDIR. Takıldığın adımı parça turunda yalıtarak tekrar et; akıcıysan skorlu senaryoya geç.</p>" },
    { "type": "branching", "id": "parca_karar", "title": "Parça-görev kararı",
      "prompt_html": "<p>Çözümlemeye göre: bir adımda ipucuna düştüysen o adımı yalıtılmış tekrar et; akıcı geçtiysen skorlu ölçüme ilerle.</p>",
      "choices": [
        { "id": "c_tekrar", "text_html": "Takıldığım adımı parça turunda tekrar edeceğim", "goto_screen_id": "deneme_parca" },
        { "id": "c_gec", "text_html": "Akıcıyım — skorlu senaryoya geç", "goto_screen_id": "olcum_senaryo" } ] },
    // Parça-görev turu (fractionation): yalnız en sık kaybedilen alt-görev, sadeleştirilmiş bağlamda
    { "type": "simulation", "id": "deneme_parca", "title": "Parça turu: yalnız açılış + başlatma (puan yok)", "points": 0,
      "prompt_html": "<p>Bütün görev değil, iki kritik parça: kilitli paneli açmak ve basılı-tutmayı oturtmak. İstediğin kadar tekrar et.</p>",
      "steps": [
        { "instruction_html": "<p><b>1.</b> Kilitli paneli işleme aç</p>", "image_asset_id": "panel_kapali",
          "regions": [ { "id": "p_anahtar", "shape": "rect", "coords": [40, 320, 120, 90], "correct": true, "hint": "Tuşlardan önce anahtar — kilitli panelde her tık yutulur." } ] },
        { "instruction_html": "<p><b>2.</b> Anons tuşunu 3 sn basılı tut</p>", "image_asset_id": "panel_bolge_secili",
          "regions": [ { "id": "p_anons", "shape": "rect", "coords": [520, 340, 110, 70], "correct": true, "hint": "Kısa basış = tepkisizlik; bas ve say: bir-iki-üç." } ] } ] },

    // ── FAZ senaryolu_olcum (SKORLU: YENİ senaryo varyantı — bütün görev; kanıt bağı ÇOĞUL) ──
    { "type": "simulation", "id": "olcum_senaryo", "title": "Skorlu senaryo: D-Blok gece vardiyası", "points": 100,
      "evidence_screen_ids": ["model_icra", "cozumleme"],  // E1 — ÇOĞUL bağ: model icra (kanıt 1) + çözümleme (kanıt 2)
      "prompt_html": "<p>Yeni durum: gece vardiyasında D-Blok'ta duman ihbarı. Anonsu doğru sırayla, ipucusuz başlat.</p>",
      "steps": [
        { "instruction_html": "<p><b>1.</b> İlk hamleni yap</p>", "image_asset_id": "panel_kapali_gece",
          "regions": [ { "id": "s1", "shape": "rect", "coords": [40, 320, 120, 90], "correct": true, "hint": "Model icradaki 1. adımın gerekçesini hatırla: kilitli panelde tık yutulur." } ] },
        { "instruction_html": "<p><b>2.</b> Anonsun hedefini belirle</p>", "image_asset_id": "panel_acik_gece",
          "regions": [ { "id": "s2", "shape": "rect", "coords": [300, 250, 90, 60], "correct": true, "hint": "Bu senaryoda tahliye edilecek blok D — bölge tuşları orta sırada." } ] },
        { "instruction_html": "<p><b>3.</b> Anonsu başlat</p>", "image_asset_id": "panel_d_secili",
          "regions": [ { "id": "s3", "shape": "rect", "coords": [520, 340, 110, 70], "correct": true, "hint": "Çözümlemedeki ikinci kayıp: kısa basış. Basılı tut." } ] },
      ],
      "feedback": {
        "correct_html": "<p>Üç adım, doğru sıra — model icradaki gerekçeler artık senin: kilidi aç ki tık yutulmasın, bölgeyi seç ki anons hedefe gitsin, basılı tut ki panel bilerek tepki versin.</p>",
        "incorrect_html": "<p>Sıra bozuldu. 'Model icra' ekranındaki adım gerekçelerine ve çözümlemedeki iki tipik kayba (atlanan anahtar, kısa basış) geri dön; parça turu hâlâ açık.</p>" } },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Denetim izi: skorlu tek ekran (`olcum_senaryo`) → `evidence_screen_ids: ["model_icra",
"cozumleme"]` — ÇOĞUL bağ, iki kanıt fazına birden (`evidence_phases`). Deneme ekranları
(`deneme_tam`, `deneme_parca`) `points: 0` (Z3 — deneme puanlanmaz); deneme gözlemi `store_key:
"drill_zayif_adim"` ile saklanır ve `cozumleme` ona `data-exploration-ref` ile birebir atıf yapar
(taklit değil). Parça-görev döngüsü `branching` (`parca_karar`) ile simüle edilir; skorlu ölçüm
YENİ senaryo varyantıdır (gece/D-Blok) ve parça değil bütün görevi ölçer. Süreli oyun varyantı bu
örnekte kullanılmadı; eklenirse `allow_extend` + `allow_disable` zorunlu (WCAG 2.2.1).

## Literatür

- **Birincil (simülasyonla öğrenme):** de Jong, T., & van Joolingen, W. R. (1998). *Scientific
  Discovery Learning with Computer Simulations of Conceptual Domains.* Review of Educational
  Research, 68(2), 179–201. https://doi.org/10.3102/00346543068002179 — çıplak simülasyonun
  yetmediği, yapılandırılmış öğretimsel destek gerektiği bulgusu (faz iskeletinin gerekçesi).
- **Tatbikat mekaniği:** Ericsson, K. A., Krampe, R. Th., & Tesch-Römer, C. (1993). *The Role of
  Deliberate Practice in the Acquisition of Expert Performance.* Psychological Review, 100(3),
  363–406 — kasıtlı pratik: zayıf noktaya odaklı, geri bildirimli, tekrarlı çalışma
  (çözümleme→parça-tur döngüsünün dayanağı).
- **Parça-görev eğitimi:** Wightman, D. C., & Lintern, G. (1985). *Part-Task Training for
  Tracking and Manual Control.* Human Factors, 27(3), 267–283 — segmentation / fractionation /
  simplification + parçaların bütüne yeniden entegrasyonu (skorlu ölçümün bütün-görev şartı).
