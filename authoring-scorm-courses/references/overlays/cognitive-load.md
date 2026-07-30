---
# Birincil kaynaklar (DOĞRULANDI, 2026-07-30 — cambridge.org "The Cambridge Handbook of
# Multimedia Learning" 3. baskı tanıtım sayfası + ResearchGate künyesi): Mayer & Fiorella (Eds.)
# (2022), 3. baskı — 30 ilke ÜÇ kategoride: konu-dışı işlemeyi AZALTMA (coherence, signaling,
# redundancy, spatial/temporal contiguity), zorunlu işlemeyi YÖNETME (segmenting, pre-training,
# modality), üretken işlemeyi TEŞVİK. Bu dosyanın kullandığı altı ilke adı (segmenting,
# pre-training, modality, coherence, redundancy, signaling) bu kategorilerden birebir doğrulandı.
# Kuram tabanı: Sweller (1988) Cognitive Science 12(2) 257–285; Sweller, van Merriënboer & Paas
# (1998) Ed. Psych. Review 10(3) 251–296 (içsel/konu-dışı/üretken yük ayrımı). Sınır koşulu
# kaynağı (destek_dozu çakışması): Sinha & Kapur (2021) RER 91(5), 10.3102/00346543211019105.
overlay: cognitive-load
name: "Bilişsel Yük Yönetimi"
version: 1
decision_points: [ekran_secimi, icerik_dozu, medya, destek_dozu]
conflicts:
  - with: productive-failure
    decision_point: destek_dozu
    rule: "Paketin kasıtlı-zorluk deneme bölümlerinde bu kaplamanın destek-artırma önerileri
           askıya alınır; paket beyanı önceliklidir. Deneme sırasında destek dozu düşük tutulur,
           kanonik çözümün kurulduğu bölümde yükselir (Sinha & Kapur 2021 sınır koşulları:
           deneme-önce tasarımın etkisi tam bu asimetriden gelir)."
  - with: pbl-case
    decision_point: icerik_dozu
    rule: "Vaka dosyasının belge zenginliği kasıtlı içsel yüktür (gerçekçilik = öğrenme
           malzemesi); kaplamanın doz-azaltma önerisi vaka artefaktlarını inceltemez. Kaplama
           yalnız vaka-DIŞI sunum ekranlarında (yönerge, çerçeve, geçiş) doz kararı verir."
  - with: arcs
    decision_point: medya
    rule: "Dikkat amaçlı eklenen medya konu-dışı yük adayıdır: yalnız kanıt taşıyan artefakt
           dikkat ögesi olabilir. İki kaplama aynı ekranda çelişirse tutarlılık (coherence)
           ilkesi önceliklidir — süs-aday öge çıkarılır."
---

# cognitive-load — Bilişsel Yük Yönetimi (D1)

**Ne:** Çalışma belleği dar bir boğazdır; kaplama, her karar noktasında bu boğazı üç yük türüne
göre yönetir: **içsel yük** (konunun kendi karmaşıklığı — azaltılmaz, BÖLÜNÜR), **konu-dışı yük**
(sunumun ürettiği gereksiz işleme — acımasızca ayıklanır), **üretken yük** (şema kuran işleme —
korunur ve beslenir; Sweller, van Merriënboer & Paas 1998). **Ne zaman:** her yöntemin altında
çalışabilir; özellikle mekanizma-yoğun içerik (çok adımlı süreç, neden-sonuç zinciri) ve düşük/orta
önbilgi profillerinde seçilir.

**Denetim bulgusunun cevabı (bu kaplamanın varlık nedeni):** azami kesintisiz anlatım bütçesi
(≈ 320–370 kelime/fikir; ekranda ~120–160) iddia + olguyu taşır ama MEKANİZMAYI taşımaz. Yük
yönetimi kelime saymak değildir: **bütçe mekanizma anlatımını kesiyorsa kaplamanın kararı BÖLMEKTİR,
kısaltmak değil** — kısaltma v1'in yüzeysellik sorununu geri getirir. Anti-slop T2 zaten "iddiaya
mekanizma taşıyıcısı" ister; bu kaplama o taşıyıcının NASIL bölüneceğini söyler.

## Karar noktası kuralları

### `icerik_dozu` — bölme (segmenting) ve ön-eğitim (pre-training)

- **Bölme eşiği (ikili kural):** bir ekran birden çok mekanizma adımını *aynı anda* işletmeye
  zorluyorsa (öğrenen bir adımı anlamadan diğeri ekranda duruyorsa) ekran bölünür. Mekanik
  denetim: gövdedeki neden-sonuç zinciri > 2 halka ise → `content_slide` `blocks[]` ile
  paragraf→görsel→paragraf dizisine, > 3 halka ise ayrı ekranlara ya da adım-adım açılan bir
  yapıya (`worked_example` adımları, `reveal: "click"`) taşınır. Öğrenen-hızlı ilerleme
  (`reveal: "click"`, `accordion`) bölmenin ekran çoğaltmayan biçimidir.
- **Ön-eğitim:** mekanizma ekranından ÖNCE, o mekanizmada geçen bileşen adları/terimler ayrı ve
  düşük-yüklü bir ekranda tanıtılır (`flashcards` terim↔tanım; `accordion` bileşen listesi).
  Böylece mekanizma ekranında çalışma belleği "bu parça neydi?" sorusuna değil parçalar-arası
  ilişkiye harcanır. Ters yönü de kural: ön-eğitim ekranı mekanizmayı ANLATMAZ (o zaman bölme
  değil tekrar olur) — yalnız adlandırır ve tanır.

### `medya` — kip (modality), gereksizlik (redundancy), tutarlılık (coherence), işaretleme (signaling)

- **Kip:** incelemelik görsel artefakt taşıyan ekranda sözel açıklama yazı duvarı olarak değil
  `narration_text` (ses kanalı) olarak verilir — görsel + yazı aynı (görsel) kanalda yarışır,
  görsel + ses iki kanalı kullanır.
- **Gereksizlik:** anlatımın ekran metnini birebir okuması anti-slop B2 ile zaten yasak; bu
  kaplama gerekçesini verir — aynı cümleyi hem okuyup hem dinlemek iki kanalda ÇİFT işleme
  yüküdür. Anlatım genişletir/örnekler/bağlar, kopyalamaz.
- **Tutarlılık:** öğretmeyen medya (süs görseli, dekoratif animasyon) konu-dışı yükün ta
  kendisidir — anti-slop C1/C4 yasaklarının yük-kuramsal gerekçesi. İkili test: "bu görsel
  çıkarılırsa hangi soru cevaplanamaz olur?" Cevap yoksa görsel çıkar.
- **İşaretleme:** öğrenenin dikkatini kritik ögeye metin aramadan götür: anlotasyonlu ekran
  görüntüsü, `hotspot` bölge etiketi, tek-çıkarım taşıyan başlık (anti-slop A3'ün yük gerekçesi),
  `image_compare` ile farkı GÖSTERME (farkı paragrafla tarif etmek yerine).

### `ekran_secimi` — bölünmüş dikkat (split-attention) temizliği

Birbirine başvuran iki içerik ayrı ekranlara düşerse öğrenen zihinsel gidiş-geliş yapar
(bölünmüş dikkat). Kural: **soru, başvurduğu artefaktla aynı ekranda ya da bir ekran geride
olmalı**; grafik + grafiği okuyan metin tek ekranda (`content_slide` `blocks[]` ya da
`data_chart` + `caption`); yoğun başvuru içeriği `accordion`/`tabs` ile aynı ekranda katmanlanır.

### `destek_dozu` — çözümlü-örnek etkisi ve kasıtlı-zorluk istisnası

Taban kural (worked-example etkisi): düşük önbilgide tam açık çözümlü örnek + yoğun ipucu,
problem-çözdürmeden önce gelir; önbilgi arttıkça doz `expertise-adaptive` kaplamasının alanına
girer (oradaki soluklaştırma tablosu). **İstisna — kasıtlı zorluk:** deneme-önce yöntemlerin
düşük-destekli deneme bölümleri bu kaplamanın gözünde "aşırı yük" gibi görünür ama DEĞİLDİR:
oradaki boğuşma üretken yüktür ve yöntemin beyanıdır. Çözüm kuralı ön-maddedeki çakışma
bildirimindedir: deneme bölümünde destek dozu düşük kalır (kaplama susar), kanonik çözümün
kurulduğu bölümde destek dozu yükselir (kaplama tam açık çözümlü örnek + denemeye atıf ister).

## Somut ekran kararları (parametre düzeyinde)

**1) Bölme — mekanizma zinciri `content_slide`'dan `worked_example`'a:**

```jsonc
// ÖNCE — 5 halkalı mekanizma tek gövdede: bütçe ya mekanizmayı keser ya ekranı şişirir
{ "type": "content_slide", "title": "Fatura onay zinciri neden 5 adım?",
  "body_html": "<p>Talep açılır, bütçe kodu düşülür, limit kontrolü yapılır, ikinci imza alınır, ödeme kilidi açılır… (5 adımın nedenleriyle tek blok)</p>" }
```
```jsonc
// SONRA — bölme: her halka action+rationale çifti; öğrenen hızında açılır (segmenting)
{ "type": "worked_example", "id": "onay_zinciri", "title": "Onay zinciri: her adımın var olma nedeni",
  "fading": "full",
  "steps": [
    { "action_html": "<p><b>1.</b> Bütçe kodu düşülür.</p>",
      "rationale_html": "<p>Kod düşülmeden limit kontrolü NEYE karşı yapılacağını bilemez — sonraki adımın girdisi burada üretilir.</p>" },
    { "action_html": "<p><b>2.</b> Limit kontrolü çalışır.</p>",
      "rationale_html": "<p>Kontrol, kod bazlı kalan bütçeyi okur; aşımda zincir burada durur ve ikinci imzaya hiç gitmez.</p>" }
    // … her halka bir adım; tek ekranda 5 paragraf DEĞİL
  ] }
```

**2) Ön-eğitim — terimler mekanizmadan önce, ayrı düşük-yük ekranda:**

```jsonc
{ "type": "flashcards", "id": "on_egitim_terimler", "title": "Önce parçaları tanı: 3 terim",
  "cards": [
    { "front_html": "<b>Bütçe kodu</b>", "back_html": "<p>Harcamanın hangi kaleme yazılacağını söyleyen etiket.</p>" },
    { "front_html": "<b>Ödeme kilidi</b>", "back_html": "<p>Onaysız çıkışı engelleyen sistem durumu.</p>" } ] }
// → mekanizma ekranı ("onay_zinciri") bu ekrandan SONRA gelir ve terimleri tanımlamakla vakit kaybetmez
```

**3) Gereksizlik ayıklama — anlatım kopya değil genişletme (B2 bağı):**

```jsonc
// ÖNCE (ihlal): narration_text, body_html'in kopyası → çift kanal çift yük
{ "type": "content_slide", "title": "Kilit onaysız açılmaz",
  "body_html": "<p>Ödeme kilidi ikinci imza olmadan açılmaz.</p>",
  "narration_text": "Ödeme kilidi ikinci imza olmadan açılmaz." }
// SONRA — anlatım vakayla genişletir; metin kuralı, ses bağlamı taşır
{ "type": "content_slide", "title": "Kilit onaysız açılmaz",
  "body_html": "<p>Ödeme kilidi ikinci imza olmadan açılmaz.</p>",
  "narration_text": "Geçen yılki mükerrer ödeme vakasında zincir tam burada kırılmıştı: kilit, ikinci imzayı beklemeden elle açılmıştı." }
```

**4) Tutarlılık — süs medya çıkarma (C4 bağı):** kapanışa "kutlama" lottie'si eklemek yerine
görsel bütçe, soruların bağlandığı anlotasyonlu artefakta harcanır; öğretmeyen medya bu
kaplamada yalnız estetik tercih değil ölçülebilir yük maliyetidir.

## Sınırlar (bu kaplama NE YAPMAZ)

- Sıra dayatmaz: hangi ekranın önce geleceği paketin işidir; kaplama yalnız ekranın İÇİNİ ve
  dozunu düzenler (ön-eğitim "önce"si bir sıra beyanı değil, aynı fazın içinde yerleşim kararıdır).
- Katman 1'i gevşetmez: kanıt bağlama (K1–K6), hiza (H1–H3), feedback anatomisi (G1–G3) ve
  anti-slop tabanları aynen geçerli — "yük azaltmak için feedback'i kısalttım" geçersizdir
  (G1 üç öğe kalır; kaplama olsa olsa feedback'i iki cümleye BÖLER).
- Yöntemin kasıtlı zorluğunu "yük" diye söndürmez (yukarıdaki `destek_dozu` istisnası ve
  ön-madde çakışma bildirimi).

## Literatür

- Kuram tabanı: Sweller, J. (1988). *Cognitive Load During Problem Solving.* Cognitive Science,
  12(2), 257–285; Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). *Cognitive
  Architecture and Instructional Design.* Educational Psychology Review, 10(3), 251–296
  (güncelleme: aynı yazarlar 2019, EPR 31, 261–292).
- İlke adları ve kategorileri: Mayer, R. E., & Fiorella, L. (Eds.) (2022). *The Cambridge
  Handbook of Multimedia Learning* (3. baskı). Cambridge University Press — konu-dışı işlemeyi
  azaltma (coherence, signaling, redundancy, contiguity) / zorunlu işlemeyi yönetme (segmenting,
  pre-training, modality) kategorileri DOĞRULANDI; ayrıca Mayer, R. E., & Moreno, R. (2003).
  *Nine Ways to Reduce Cognitive Load in Multimedia Learning.* Educational Psychologist, 38(1), 43–52.
- Kasıtlı-zorluk sınırı: Sinha, T., & Kapur, M. (2021). *When Problem Solving Followed by
  Instruction Works.* Review of Educational Research, 91(5), 761–798 — deneme-önce tasarımların
  sınır koşulları (`destek_dozu` çakışma kuralının dayanağı).
