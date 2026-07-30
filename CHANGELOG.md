# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added — v2.2 son paketler (C9–C12, ikinci yarı)
- **`references/pedagogy/sim-drill.md` — C9 Simülasyon Tatbikatı (#26).** Gösterim-önce tatbikat
  paketi (psikomotor/prosedür): brifing (hedef + akıcılık ölçütü) → gösterim turu (worked_example
  model icra — kanıt 1) → serbest deneme (simulation `points: 0` + deneme gözlemi exploration ile
  SAKLANIR) → çıktı çözümleme (deneme ↔ model karşılaştırması, zayıf alt-görev teşhisi — kanıt 2)
  → parça-görev döngüsü (`sonraki`/`tekrar_kosulu`: yalnız teşhisli alt-görev tekrar edilir,
  Wightman & Lintern fractionation) → senaryolu skorlu ölçüm (YENİ varyant, bütün görev).
  `evidence_phases: [gosterim_turu, cikti_cozumleme]` (ÇOĞUL — simülasyon ekranı çift şapkalı:
  pratik aracı + çıktısı kanıt). `requires_platform: [simulation, worked_example, exploration]`
  SERT (F2'siz "denemeni modelle karşılaştır" taklide düşer — issue denetim bulgusunun beyanı).
  Süreli oyun varyantı yalnız `allow_extend` + `allow_disable` ile (WCAG 2.2.1 — platform
  doğrulayıcısı zorlar). Birincil kaynaklar doğrulandı: de Jong & van Joolingen (1998) RER 68(2)
  + Ericsson, Krampe & Tesch-Römer (1993) Psych. Review 100(3) + Wightman & Lintern (1985)
  Human Factors 27(3).
- **`references/pedagogy/gagne-9.md` — C10 Gagné'nin Dokuz Öğretim Olayı (#27).** Tam-kapsama
  iskeleti (mevzuat/zorunlu eğitim; Katman 0'ın belgeli varsayılanı): dikkat → hedef → ön bilgi
  → uyaran sunumu (kanıt 1) → öğrenme rehberliği (kanıt 2) → skorsuz performans çıkarma →
  gerekçeli geri bildirim → skorlu değerlendirme → kalıcılık/transfer. Olay adları Gagné (1985)
  4. baskıdan doğrulandı; `outcome_types` TAM liste (beş öğrenme alanı yedi türü kapsar —
  genişlik = nötrlük, özelleşmiş paket sağ kalmışken varsayılan seçilmez). "9 olay ekran DEĞİL
  işlevdir" uyarısı paketin en kritik bölümü (örnek 9 olayı 8 ekranda birleştirerek gösterir).
  Mevzuat bağlamı: herkes aynı içeriği görür (uyarlanabilir atlama YOK; expertise-adaptive
  gerilimi karar-noktası düzeyinde, D4 yazılırken kaplama tarafında bildirilecek). KANON-ALAN
  kuralı paketin yerlisi: uyum içeriği kamusal kanon → sorular kanonu değil kanonun kurs-üretimi
  artefakta uygulanmasını ölçer (evidence-binding.md "Kanon-alan içerikleri" bölümüne atıf).
  `mastery-learning` ile bileşim tamamlayıcılık (çakışma değil — seçici örnek 4). Birincil
  kaynak doğrulandı: Gagné (1985) Conditions of Learning 4. baskı + Gagné, Briggs & Wager (1992).

### Added — v2.2 ikinci dalga yöntem paketleri (C5–C8, ilk yarı)
- **`references/pedagogy/mastery-learning.md` — C5 Tam Öğrenme (Bloom) (#22).** Döngülü paket:
  ünite sunumu → skorsuz formatif eşik (%80, BKT ustalık kestirimi) → eşik-altı DÜZELTİCİ tur
  (aynı içerik, FARKLI temsil) → paralel yeniden-yoklama → eşik-üstü summatif. Şemanın
  `sonraki`/`tekrar_kosulu` döngü mekaniğiyle ifade edildi; `requires_platform: [branching,
  adaptive_practice]` (koşullu dallanma olmadan eşik zorlanamaz — beyan sert kısıt).
  `evidence_phases: [unite_sunumu, duzeltici_dongu]` (ÇOĞUL — düzeltici temsil ikinci kanıt
  kanalı). build_from_spec örneği döngünün SCORM simülasyonunu gösterir: `branching` eşik-karar
  ekranı iki yol açar, düzeltici kol paralel formatif ile ana hatta geri bağlanır. Birincil
  kaynak doğrulandı: Bloom (1968) *Learning for Mastery*, Evaluation Comment 1(2) + Keller
  (1968) PSI.
- **`references/pedagogy/productive-failure.md` — C6 Üretken Başarısızlık (Kapur) (#23,
  needs-decision ÇÖZÜM ÖNERİLİ).** Deneme-ÖNCE paket: problem_deneme (kanonsuz skorsuz boğuşma —
  exploration/F2 denemeyi SAKLAR) → deneme_karsilastirma (geri oynatma; kanon sızdırmaz, K5) →
  konsolidasyon (kanonik çözüm denemeye AÇIK atıfla — worked_example) → uygulama (skorlu).
  Kanıt = K1 türü 5'in iki ayağı: `evidence_phases: [problem_deneme, konsolidasyon]` (ÇOĞUL).
  `requires_platform: [exploration]` SERT (F2'siz "kendi denemenle karşılaştır" taklide düşer).
  **Karar önerisi (kullanıcı onayına):** PK tabanı 4/10 bağlayıcı (`prior_knowledge: [4, 8]`) —
  Kapur örneklemlerinin önkoşul-bilgi profili + Sinha & Kapur (2021) sınır koşulları + Kirschner
  vd. (2006) acemi ucu; `error_cost: [düşük]` yalnız; cognitive-load çakışması hedef-düzeyi
  değil karar-noktası düzeyinde (kaplama tarafında `destek_dozu` bildirimi) çözülür.
  `conflicts_with: [rosenshine-di]` — C1'in tek taraflı beyanı KARŞILIKLI hale geldi. Birincil
  kaynak doğrulandı: Kapur (2008) C&I 26(3) + Kapur & Bielaczyc (2012) JLS 21(1) faz adları.
- **`references/pedagogy/pbl-case.md` — C7 Vaka/Problem Temelli Öğrenme (Barrows) (#24).**
  Problem-önce paket: vaka_dosyasi (kursun inşa ettiği artefakt ailesi + bütün-vaka sürükleyici
  soru) → problem_tanimlama (hipotez, skorsuz) → analiz_arastirma (aşamalı ifşa: ek belgeler —
  kanıt ailesi 2) → cozum_onerisi (skorlu vaka kararı) → karsilastirma_genelleme (uzman
  karşılaştırması + transfer). `evidence_phases: [vaka_dosyasi, analiz_arastirma]` (ÇOĞUL);
  amiral-gemisi bulgusunun panzehiri: skorlu soru vaka dosyasına bağlanmak ZORUNDA, kritik olgu
  yalnız dosya ekranlarında yaşar (K4) — kanon-alan kalıbı paketin yerlisi. PK 6–10 (vaka
  zenginliği acemiye gürültü); `requires_platform: []` (F2 hipotez notu için opsiyonel
  iyileştirme). `conflicts_with: []` gerekçeli: gösterim-önce adaylarla PK aralıkları ayrık —
  aynı hedefte zaten birlikte sağ kalamazlar. Birincil kaynak doğrulandı: Barrows (1986)
  Medical Education 20(6), 481–486.
- **`references/pedagogy/kolb-experiential.md` — C8 Kolb Deneyimsel Öğrenme Döngüsü (#25).**
  Deneyim-önce döngü: somut_deneyim (karar + bedel, anlatı içinde — puanlanmaz) →
  yansitici_gozlem (açık uçlu, exploration/F2 tercihli — SAKLANIR, kanıt fazı DEĞİL: köprü) →
  soyut_kavramsallastirma (deneyime atıflı kanonik çerçeve) → aktif_deneme (YENİ senaryoda
  skorlu DAVRANIŞ seçimi — tutumun davranışsal kanıtı, "iddia+quiz" zincirinin panzehiri).
  `evidence_phases: [somut_deneyim, soyut_kavramsallastirma]` (ÇOĞUL). PK [1,10] ve error_cost
  tam liste — gerekçeli: deneyim malzemesini kurs üretir, saha bedeli simülasyona taşınmaz.
  `requires_platform: []` (decision_scenario/branching çekirdek; F2 yansıtma geri-oynatması
  iyileştirme). `arcs` kaplaması doğal eş (yalnız eşleme notu — kaplama uygulanmadı).
  `conflicts_with: []` gerekçeli (tutumda yarışan paket yok; outcome kesişimi boş). Birincil
  kaynak doğrulandı: Kolb (1984) *Experiential Learning*, Prentice-Hall — dört evre adı;
  öğrenme-stilleri iddiası paket DIŞI bırakıldı (Pashler vd. 2008 sınır notu).

### Changed — v2.1 F1/F2 entegrasyonu (worked_example + exploration YAYINDA)
- **`references/pedagogy/4cid.md` — F1 gerçek şemaya geçiş.** build_from_spec örneği eski
  taslak alanlardan (`fading_level`, `steps[].html`, `blank_accepted`, worked_example üstünde
  `points`) gerçek şemaya yazıldı: `steps[{action_html, rationale_html, artifact_asset_id?,
  artifact_caption?}]` (≥2), `fading: "full" | "partial" | "problem_only"`, `intro_html`,
  `self_explanation_prompt_html` — yapısal skorsuz (puan alanı YOK). Platform şartı notu:
  worked_example gelecek tip değil YAYINDA (F1 #112); `requires_platform: [worked_example]`
  beyanı kalır ve artık karşılanabilirdir (F1'siz eski hedeflerde paketi elemeyi sürdürür).
- **`references/pedagogy/5e-inquiry.md` — exploration (F2 #113) kesfet fazının TERCİH edilen
  taahhüt mekaniği.** Girdi `store_key` altında saklanır, acikla ekranı
  `<span data-exploration-ref="store_key">` ile birebir geri oynatır ("senin tahminin şuydu"
  atfı artık gerçek); puan-0 formatif quiz YEDEK olarak geçerli kalır (F2'siz hedefler).
  `requires_platform: []` değişmedi. build_from_spec örneği gerçek F2 şemasına yazıldı
  (prediction taahhüdü + text gözlem notu; stale `trials`/`{{exploration:...}}` kaldırıldı).
- **`templates/4cid.json` — `_draft` kaldırıldı, gerçek build.** worked_example soluklaştırma
  dizisi (full → partial → problem_only) + öz-açıklama istemleri + iki adım artefaktı; skorlu
  soru `evidence_screen_ids` ile ÇOĞUL üç worked_example ekranına bağlı. Gerçek sunucu
  doğrulaması: `build_from_spec` + `lint_course(strict=True)` → **0 hata / 0 uyarı /
  evidence_binding_coverage 1.0**.
- **`templates/5e-inquiry.json` — kesfet taahhüdü exploration'a taşındı.** points-0 mcq →
  `exploration` (prediction, `store_key: tahmin_yonetici`); acikla slaytına geri-oynatma
  span'ı; açığa-çıkarma rolü data_chart'a geçti. Aynı harness: **0 / 0 / 1.0**.
- **`references/screen-types.md` — karar rehberi 30 tipe çıktı.** Yeni "Evidence primitives"
  grubu: worked_example (K1 tür 1) + exploration (K1 tür 2) kullanım/kanıt/seçim-sezgisi
  notlarıyla; `references/core/alignment.md` tip sayısı 30'a güncellendi (soru sorabilen 13
  değişmedi — F1/F2 yapısal skorsuz).

### Changed — v2.0 E4 kural revizyonu (kanıt bağlama tabanı)
- **`references/core/evidence-binding.md` — K4: gövde kendine-yeterliliği yasağı (E4-R1, #52).**
  Skorlu sorunun gövdesi, cevabın türetilmesi için gereken kursa-özgü kritik olguyu İÇEREMEZ;
  olgu yalnız `evidence_screen_ids` ekranlarında yaşar, gövde ona atıf yapar ama değerini
  kopyalamaz. İkili denetim (soru başına 3 adım; transfer gövdeleri dahil) + ÖNCE/SONRA çifti
  ilk gerçek E4 koşusunun `q_sinir` sorusundan ("salı 16:40" gövdede → damga yalnız çizelgede).
  Mekanik sayılabilirlik notu: kemalyy/edumints-scorm-mcp E1 lint'ine aday genişletme.
- **`references/eval/blind-test.md` adım 4 — [GÖVDE] sınıflaması.** Gövdesindeki verili olguyla
  çözülen soru kanıttan kopya sayılmaz: dayanağa [GÖVDE] yazılır ve E sayılır (K4 ihlali).
- **`references/core/evidence-binding.md` — K5: cevap sızıntısı yasağı (E4-R2, #53).** Skorlu bir
  sorunun cevabını, o sorunun `evidence_screen_ids`'i dışındaki hiçbir ekran açıkça ifade edemez
  (`summary` dahil — özet kavram düzeyinde çerçeve kurabilir, cevap cümlesi kuramaz). İkili
  denetim (cevap-önermesi × kanıt-dışı ekran taraması) + ÖNCE/SONRA çifti ilk gerçek E4
  koşusunun kapanış özetinden (üç cevap tek cümlede → kavram-düzeyi çerçeve). Mekanik
  sayılabilirlik notu: kemalyy/edumints-scorm-mcp E1 lint'ine aday genişletme.
- **`references/core/evidence-binding.md` — yeni bölüm: kanon-alan içerikleri.** Alanın kuralları
  kamusal kanonsa (mevzuat/standart/ders kitabı) skorlu soru kanonun kendisini değil kanonun
  kursa-özgü artefakta uygulanmasını ölçer; 3 dönüştürme örneği (kural-hatırlama →
  artefakta-uygulama; ikisi E4 koşusunun `q_gecikme`/`q_dil` sorularından).
- **Kör test adım 4 — [KOPYA] sınıflaması** (blind-test.md): sökülmeden kalan kanıt-dışı ekrandan
  okunan cevap da E sayılır (ikinci cevap kanalı; K5 ihlali). Çapraz referanslar K1–K5'e
  güncellendi (SKILL.md, anti-slop.md T1, method-selector.md, README ağacı).
- **`references/core/evidence-binding.md` — K6: çapraz-madde kontaminasyonu yasağı (E4-R3, #55).**
  Skorlu bir sorunun gövdesi/başlığı/şıkları, BAŞKA bir skorlu sorunun cevabını türetmeye yetecek
  kursa-özgü olguyu içeremez (K5'ten fark: sızıntı kanalı kanıt-dışı bir ekran değil, başka bir
  skorlu maddenin kendisi). İkili denetim (madde çifti başına 3 adım) + ÖNCE/SONRA çifti E4 2.
  koşusunun `q_eksen` sorusundan (başlık tekniği adlandırıp `n_satis` oyun düğümünün teşhisini
  ele veriyordu → nötr başlık + kanıt ekranına atıf). Mekanik sayılabilirlik notu: aday genişletme.
- **`references/eval/blind-test.md` adım 4 — [KOPYA] çapraz-madde alt sınıfı.** Sökülmüş kopyada
  cevap tek bir kanıt-dışı ekrandan değil maddeler ARASI bir çıkarım zinciriyle okunuyorsa dayanak
  yine [KOPYA] kalır (köken hücresi ekran id yerine soru id taşır); E sayılır (K6 ihlali). Çapraz
  referanslar K1–K6'ya güncellendi (SKILL.md, anti-slop.md T1, method-selector.md, README ağacı).

### Added — v2.1 Değerlendirme seti (Wave 4b: E3, #21)
- **`eval/` (depo kökü)** — belge + fikstür seti (otomasyon değil): 10 test istemi
  (`eval/prompts/`, kazanım türleri × önbilgi düzeyleri matrisi; 3'ü `sıkıştırılmış-referans`
  etiketli — kopya kâğıdı / mevzuat özeti / politika tablosu, "madde sayısı ≈ ekran sayısı"
  başarısızlık-kökeni girdileri gömülü snippet'lerle). Nicel metrik tanımı: **kanıta bağlı
  skorlanan soru oranı** = sunucu lint'inin `evidence_binding_coverage` alanı (E1/#110;
  vakum/ilgisizlik/QUIZ_TYPES-dışı kör noktaları belgeli). Çerçeve kuralı dosyanın en
  üstünde: **coverage tabandır, hedef değil — tek gerçek kapı E4 kör testidir**; v1↔v2
  karşılaştırmasında karar sütunu kör testten gelir, coverage yalnız ön koşul satırıdır.
- **`eval/results/2026-07-29-v1-baseline.md`** — v1 taban çizgisi koşuldu (artefakt-vekilli,
  gerçek `build_from_spec`+`lint_course`): amiral örnek kursu **coverage 0.0** (0/3 skorlu),
  `tool-training.json` **0.0** (0/2), `concept-lesson.json` **1.0 (vakum, n=0** — hiç ölçüm
  yok**)**; v1 kör test pilotu KALDI (1/4). v2 şablonları aynı harness'ta 1.0 (vakumsuz,
  0 err · 0 warn) — kör testleri ve 10-istem tam koşusu G3'e bırakıldı (kayıtta BEKLEMEDE).
- **`eval/results/TEMPLATE.md`** — sonuç kaydı + v1↔v2 karşılaştırma tablosu şablonu
  (vakum yazım kuralı, source_item_parity sütunu, coverage–kör-test tutarsızlık notu).

### Changed — v2.1 Paket şablonları (Wave 4b: F3, #20)
- **`templates/` yeniden yazıldı: paket başına bir minimal şablon (C1–C4).** Her şablon
  YÖNTEM BEYANI (`_yontem_beyani`, method-selector çıktı biçimi) + faz açıklamalı ekranlar
  (`_phase`) + tek kazanımlı gerçekçi mikrokurs içerir; skorlu her soru ÇOĞUL
  `evidence_screen_ids` ile kanıt ekranlarına bağlı, geri bildirimler G1–G3 uyumlu (salt
  onay/ret grep 0). İnşa edilebilir şablonlar gerçek sunucu lint'inden doğrulandı
  (build_from_spec + lint_course): **rosenshine-di, merrill-fpi, 5e-inquiry üçü de 0 error ·
  0 warn · `evidence_binding_coverage` 1.0.** Şablonlar kendi başına build edilebilsin diye
  `assets[]` PLACEHOLDER veri-URI'leri taşır (gerçek varlıkla değiştirilir).
- **`templates/rosenshine-di.json`** — `tool-training.json`ın (Pattern A İzle→Uygula→Sıra
  Sende) paket eşlemesi: dosya EŞLENDİ, atılmadı (`_pattern_a_eslemesi` eski-adım→faz
  tablosu). Denetim düzeltmeleri: İzle'nin boş dış-varlık slotu kanıt taşıyan caption'a
  dönüştü (K1 dış-medya şartı); Uygula'nın 20 puanı kaldırıldı (rehberli pratik skorsuz, Z3);
  B3-ihlali salt-onay/salt-ret feedback'i gerekçeli üçlüyle değiştirildi; skorlu soru
  `evidence_screen_ids: [izle, model]`.
- **`templates/merrill-fpi.json`** — `concept-lesson.json`ın (Pattern B) kanıt-bağlı halefi
  (`_pattern_b_eslemesi`): iddia+pasif-tur zinciri (tanım→tabs→flashcards→"*"-kabullü
  fill_blank) görev-merkezli döngüye taşındı — gerçek görev (rıza metni değerlendirme) +
  karşılaştırmalı gösterim (kanıt) + skorsuz destekli deneme + kanıta bağlı skorlu ölçüm +
  skorsuz bütünleştirme.
- **`templates/5e-inquiry.json`** — C3 şablonu, tahminini-kilitle keşif mekaniğiyle BUGÜN
  inşa edilebilir: kesfet = skorsuz mcq (feedback ders anlatmaz, yalnız deney sonucunu açıklar)
  + data_chart deney verisi; skorlu soru üç kanıt ekranına birden çoğul bağlı
  (kesfet×2 + acikla).
- **`templates/4cid.json`** — C4 şablonu `_draft: true`: `worked_example` (F1) ekran tipi
  sunucuda henüz yok; taklit ekran tipiyle sahte build yerine taslak beyanı
  (`_draft_reason` + F1 sonrası yükseltme adımları). build_from_spec taslağı bilinçli reddeder.
- **SKILL.md** — "Templates & examples" bölümü 4 paket şablonuna güncellendi (lint-temiz
  invariantı + eski şablonların halefiyet notu).

### Added — v2.1 İlk dalga yöntem paketleri (Wave 4a: C1–C4)
- **`references/pedagogy/rosenshine-di.md`** (#16) — C1 Doğrudan Öğretim paketi: günlük tekrar →
  küçük adımlar + model/çözümlü örnek (`evidence_phase: sunum_model`) → rehberli pratik (skorsuz,
  yüksek soru yoğunluğu) → bağımsız pratik (skorlu). Uzmanlık-tersinme "ne zaman seçilmemeli"
  bölümü; `conflicts_with: [5e-inquiry, productive-failure]` (aynı kazanımda keşif-önce ↔
  model-önce zıtlığı); Pattern A (İzle→Uygula→Sıra Sende) eşleme beyanı (şablon işi #20'de);
  uçtan uca build_from_spec örneği (pediatrik doz hesabı; skorlu soru `evidence_screen_ids` ile
  kanıt ekranına bağlı — scorm-mcp CONTRACTS §1.3 E1). Kaynak: Rosenshine (2012), American
  Educator 36(1) — doğrulandı.
- **`references/pedagogy/merrill-fpi.md`** (#17) — C2 Merrill İlk İlkeler (görev-merkezli):
  gerçek görev tanıtımı → etkinleştirme (bilinçli olarak kanıt fazı DEĞİL — K2 gerekçesi gövdede)
  → gösterim (`evidence_phase: gosterim` — gösterimsiz kurs yapısal olarak üretilemez) →
  destekli uygulama (skorsuz) → bağımsız uygulama (skorlu) → bütünleştirme (skorsuz yansıtma).
  "Görev tanımlanamıyorsa paket seçilemez" kuralı; 4cid ile ölçek-farkı seçici notu (çakışma
  değil); `conflicts_with: []`. build_from_spec örneği: hata (bug) raporu yazma görevi. Kaynak:
  Merrill (2002), ETR&D 50(3), 43–59 — doğrulandı. Dosya adı seçici kimliğiyle hizalı
  (`merrill-fpi`; şema kuralı: dosya adı == pack).
- **`references/pedagogy/5e-inquiry.md`** (#18) — C3 5E Sorgulama Döngüsü: merak (Engage) →
  kesfet (Explore, skorsuz keşif) → acikla (Explain, keşif çıktısına atıflı kanonik açıklama) →
  derinlestir (Elaborate, skorsuz transfer) → degerlendir (Evaluate, skorlu). ÇOĞUL kanıt beyanı
  `evidence_phases: [kesfet, acikla]`; `requires_platform: [exploration]` (F2 — öğrenen girdisini
  saklayıp geri oynatma; yetenek yoksa seçici paketi ELER, kâğıt-üstü 5E üretilmez). "Ne zaman
  seçilmemeli": yüksek hata maliyeti (sert kısıt dışı), PK<3 (uzmanlık-tersinmenin acemi ucu —
  Kirschner/Sweller/Clark 2006 atfı), dar bütçe; `conflicts_with: [rosenshine-di]`
  (productive-failure bilinçli listede değil — aynı deneme-önce ailesi). build_from_spec örneği:
  yoğunluk kavramı; skorlu soru iki kanıt fazına birden çoğul bağlı. Kaynak: Bybee vd. (2006),
  The BSCS 5E Instructional Model — doğrulandı.
- **`references/pedagogy/4cid.md`** (#19) — C4 4C/ID Karmaşık Beceri Eğitimi: görev sınıfları
  basit→karmaşık TAM görevler; gorev_tam_destek (çözümlü örnek + destekleyici bilgi) →
  gorev_soluklastirma (tamamlama problemleri; `sonraki`/`tekrar_kosulu` döngüsüyle destek 0'a
  inene dek) → gorev_bagimsiz (skorlu). ÇOĞUL kanıt: `evidence_phases: [gorev_tam_destek,
  gorev_soluklastirma]`; `requires_platform: [worked_example]` (F1 — soluklaştırma düzeyleri).
  Dört bileşenin fazlara yerleşim haritası (bileşen ≠ faz); "ne zaman seçilmemeli": tekil
  olgu/kavram, tek-yollu kısa prosedür (rosenshine-di alternatifi — çakışma değil), kısa kurs,
  yüksek PK; `conflicts_with: []`. build_from_spec örneği: SQL yönetici raporu, 3 görev sınıfı;
  skorlu soru iki kanıt fazına çoğul bağlı. Kaynak: van Merriënboer & Kirschner (2018), Ten
  Steps to Complex Learning (3. baskı) — doğrulandı.

### Added — v2.1 Katman 0 seçici + paket şeması (Wave 3: B1–B4)
- **`references/core/method-selector.md`** (#12) — Katman 0 yöntem seçici: 7 kazanım türü + 5 girdi
  (PRIOR_KNOWLEDGE / hata maliyeti / zaman / platform / bağlam) → paket(ler) + kaplama(lar).
  Mekanizma (KARAR ÖNERİSİ, needs-decision): **LLM muhakemesi + deterministik uyumluluk elemesi** —
  paket ön-maddesindeki `outcome_types`/`prior_knowledge`/`error_cost`/`requires_platform` sert
  kısıtları eleyici; sağ-kalanlar arasında gerekçeli seçim; son karar yazarın, gerekçe zorunlu.
  7 örnek eşleme + eksik-girdi varsayılanları + B3-uyumlu YÖNTEM BEYANI çıktı biçimi. Hiçbir paket
  kanonik değil; hiçbiri uymazsa belgeli varsayılan `gagne-9` + zorunlu gerekçe.
- `references/pre-flight.md` — yeni Madde 1b: YÖNTEM BEYANI (paket + kaplamalar + elenenler +
  gerekçe) kaydı zorunlu.
- **`PRIOR_KNOWLEDGE` yöntem kadranı** (#13) — SKILL.md'de 1–10 ölçek + uç değer betimleri;
  sunum kadranlarından AYRI düzlemde (Katman 0 seçici girdisi, "ton ayarı" değil); 3 satırlık
  kadran→seçici etki tablosu (uzmanlık-tersinme: yüksek PK'da çözümlü örnek dozu düşer,
  problem-önce öne geçer) + dört sunum kadranıyla çelişki taraması (çapraz referans bölümü).
- **Eğitim Okuması baskın-mod enum'una `gösterim`** (#13) — keşif | gösterim | uygulama |
  değerlendirme; gösterim-ağırlıklı kurslar artık adlandırılabilir.
- **`references/pedagogy/` paket sözleşmesi** (#14) — `pack-frontmatter.schema.json` (JSON Schema,
  Türkçe alan açıklamalı) + `_SCHEMA.md` sözleşme belgesi: `pack`, `name`, `outcome_types`,
  `prior_knowledge` (aralık), `error_cost`, `requires_platform`, `phases` (amaç + izinli ekran
  tipleri + skorlanabilir; `sonraki`/`tekrar_kosulu` ile döngü-koşul), **`evidence_phase` VEYA
  `evidence_phases` ZORUNLU** (kanıt üreten faz — çoğul serbest, 1:1 dayatması yok; soru-düzeyi
  bağ zaten çoğul: `evidence_screen_ids`, scorm-mcp CONTRACTS §1.3 E1 ile terminoloji-uyumlu),
  `scoring_allowed_from` (Z2'nin paket-düzeyi beyanı), `conflicts_with`. Doğrulama:
  `scripts/validate_packs.py` (şema + bütünlük denetimleri; CI'da çalışır) + 2 çalışan örnek stub
  (`_STUB-dogrusal.md` doğrusal, `_STUB-dongulu.md` döngülü).

- **`references/overlays/_FRAMEWORK.md`** (#15) — Katman 2 kaplama çerçevesi: "sıra dayatan =
  paket, sırasız değiştiren = kaplama" ayracı (mastery-learning sınır örneğiyle); 6 kaplamanın
  (cognitive-load, udl, arcs, expertise-adaptive, assessment-alignment, accessibility) listesi +
  her birinin kapsam SINIRI; kaplama dosya biçimi (`decision_points` beyanı + 8 karar-noktası
  sözlüğü); **paket-bağımsızlık kuralı** (kaplama metninde paket faz adı = 0 — mekanik:
  `scripts/check_overlay_independence.py`, CI'da grep-0 kapısı); çakışma bildirim biçimi
  (`with` + `decision_point` + `rule`) ve productive-failure örneği.

### Changed — v2.1 Katman 0 seçici + paket şeması
- SKILL.md dört mevcut kadranı **"sunum kadranı"** olarak sınıflandırdı (geriye-uyumluluk notu:
  v1 adları ve anlamları sabit); pre-flight Madde 1 PRIOR_KNOWLEDGE beyanını da sorar.

### Added — v2.0 Kanıt Bağlama çekirdeği (Wave 1: A1–A5 + E4)
- **`references/core/` (Katman 1 — yöntemden bağımsız çekirdek kurallar; hiçbir kural bir pedagoji
  paketinin faz adını içermez, sıra dayatmaz):**
  - `evidence-binding.md` (#6) — K1–K3: skorlanan her soru kurs-içi kanıt kaynağına bağlanır
    (≥ 6 geçerli kaynak türü); birebir denetim sorusu ("Bu kursu hiç görmemiş ama alanı bilen biri
    bu soruyu zaten cevaplayabilir mi?") + numaralı "bağla ya da at" prosedürü.
  - `alignment.md` (#7) — H1–H3: hedef→soru→kanıt eşleme tablosu biçimi + "skorlanan ekran >
    hedef + 1" sayısal UYARI eşiği (warn, fail değil) + tam eşleme örneği.
  - `feedback-anatomy.md` (#8) — G1–G3: gerekçeli geri bildirimin 3 zorunlu öğesi (neden doğru /
    neden yanlış / kanıta geri işaret); anti-slop B3 TABAN statüsüne yükseltildi ve fazsız yazıldı.
  - `scoring-timing.md` (#9) — Z1–Z3: formatif/summatif tanımları; "kanıt kaynağı üretilmeden skor
    yok" ilkesi; skorsuz erken-deneme istisnası.
- **`references/eval/blind-test.md`** (#11) — kör test protokolü: kanıt kaynakları çıkarılmış kursta
  skorlanan sorular alan-bilgili okuyucu tarafından cevaplanabiliyor mu? Geçme eşiği **≥ 1/2**;
  sonuç kayıt şablonu; pilot koşu kaydı (amiral gemisi örnek: 1/4 → KALDI). F1/F2 ekran tiplerinin
  kapısı.

### Changed — v2.0 Kanıt Bağlama çekirdeği
- `references/anti-slop.md` (#10) — 17 kuralın tavan/taban sınıflandırma tablosu + yeni **T1–T3
  taban kuralları** (skorlanan soruya kanıt kaynağı VAR; iddiaya mekanizma taşıyıcısı VAR;
  `incorrect_html` kanıta geri işaret) + B3 taban yükseltmesi (fazsız yeniden yazım).
- `references/pre-flight.md` — yeni 9d (tabanlar T1–T3) ve 12b (kanıt bağlama) maddeleri; 12'ye
  hedef→soru→kanıt tablosu + H3 eşiği eklendi.
- `SKILL.md` — referans listesine `core/` ve `eval/` dosyaları eklendi.
- CI D4 drift kapısı `references/` alt dizinlerini de sayacak şekilde `rglob`'a çevrildi; README
  Structure ağacına `core/` ve `eval/` eklendi.

### Added — visual storytelling (W11)
- New `references/visual-storytelling.md` — the anti-ordinariness playbook distilled from the
  "Spot the Phish" showcase rebuild: narrative thread (one scene, opened and closed),
  per-screen visual budget, "find don't read" conversions (simulation/image_compare/timeline),
  realistic artifact mockup-SVG recipe, stat-card pattern, `search_images` → `add_asset` flow.
- `SKILL.md` reference list + `pre-flight.md` new item 9c (visual density & narrative checks,
  aligned with the server's new `text_only_run`/`visual_poverty` lint rules).

## [1.3.1] — 2026-07-23

`references/anti-slop.md` A1/A2/A3/B3 kurallarının artık scorm-mcp'nin `lint_course`'unda mekanik
olarak denetlendiğini belirten notlar (matches scorm-mcp 1.4.0's anti-slop mechanization — pre-flight
bu maddeler için artık modelin dürüstçe saymasına değil, gerçek bir sunucu-taraflı WARN'a dayanıyor).

### Changed
- `references/anti-slop.md` — A1 (`consecutive_content_slides`), A2 (`too_many_list_items`), A3
  (`generic_title`), B3 (`default_feedback`) her birine tek satırlık "artık mekanik denetleniyor" notu.

## [1.3.0] — 2026-06-26

Canva cross-MCP pipeline + SVG diagram pipeline (`svg_to_asset`) + `auto_tts` / `blocks[].width`
authoring guidance (matches scorm-mcp 1.3.0).

### Added
- `references/media.md` — **Canva cross-MCP pipeline** (generate → export → `add_asset` → asset id;
  TTL/signed-URL rules; Turkish-prompt + instructional-image rules).
- `references/mcp-cookbook.md` — `auto_tts` in `build_from_spec`; `content_slide` `blocks[].width`;
  `add_asset` return shape (`{ id, … }`) + "callable directly (may not surface in tool-search)" note;
  Canva/TTL note on `assets[]`.
- `SKILL.md` reference-file descriptions updated.
- **SVG diagrams** — `references/media.md` "SVG diagrams" section, `mcp-cookbook.md` `svg_to_asset`,
  anti-slop **C5** (no raw `<svg>`/`<canvas>`/`<script>` in `body_html`), and a "Known limits" section
  in `SKILL.md` (SVG-as-asset, animations → Lottie/MP4, `render_motion_video` Chromium fallback).

## [1.2.0] — 2026-06-24

Richer media authoring + screen reorder (matches scorm-mcp 1.2.0 / W9).

### Added
- `content_slide` **`blocks[]`** — interleave `paragraph → image → paragraph` in one screen
  (instead of consecutive content slides).
- **Per-item images** — `image_asset_id` on accordion/tabs items and timeline events;
  `front_asset_id` / `back_asset_id` on flashcard faces.
- **Inline assets** — `{{asset:<id>}}` interpolation in any `*_html` (embed a packaged asset in
  flowing text) and inline base64 `data:` URI `<img>`.
- **`reorder_screens`** tool documented (set an explicit screen order; `add_screen` appends).
- `references/mcp-cookbook.md` + `references/screen-types.md` updated for all of the above.

## [1.1.0] — 2026-06-15

Composable game engine + adaptive learning + telemetry guidance (matches scorm-mcp 1.1.0).

### Added
- Decision guides for the **2 new screen types** — `game` (composable serious game: mechanic primitives
  + `when event then action` rules + branching nodes; case_sim / escape_room) and `adaptive_practice`
  (Elo / Bayesian Knowledge Tracing → difficulty calibration). 26 → **28 screen types**.
- `references/interactivity-and-gamification.md` — composable game engine, adaptive practice (Elo vs BKT),
  and optional **xAPI / cmi5** telemetry sections.
- `references/mcp-cookbook.md` — `lint_course` (anti-slop quality gate) and `export_qti` (QTI 2.1 export)
  tools + copy-ready `game` / `adaptive_practice` spec shapes.
- `references/pre-flight.md` — mandatory `lint_course` `clean: true` gate before shipping game/adaptive courses.

## [1.0.0] — 2026-06-11

First stable release.

### Added
- **Anti-slop discipline** — a one-line Training Read (Bölüm 0), parametric dials
  (INTERACTIVITY/COGNITIVE_DENSITY/TONE/VISUAL_RICHNESS), `references/anti-slop.md` (binary bans with
  override paths + before/after JSON), and a mechanical `references/pre-flight.md` gate.
- Decision guides for **all 26 screen types** (games, customized results, visuals) + the MCP cookbook
  shapes, including the gamification HUD (`levels`/`lives_var`) authoring.
- **Topic→theme mapping** in `references/themes.md` — pick a subject-fitting visual identity (editorial,
  playground, clinical-calm…) so the interface differs by topic instead of looking uniform.
- Game-design patterns + scoring guidance (`references/` + the server's `docs/GAME-PATTERNS.md`).

## [Unreleased]

### Added
- Initial public release of the authoring-scorm-courses Claude Agent Skill.
- SKILL.md workflow + quality bar; references for instructional design, screen types, assessment,
  interactivity/gamification, media (cross-MCP + Piper TTS + local helper), programmatic video,
  themes, an authoring decision guide, and an MCP cookbook.
- Copy-and-adapt templates and a complete example course spec.
