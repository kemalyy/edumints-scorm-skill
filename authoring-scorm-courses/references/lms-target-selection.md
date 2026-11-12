# LMS → SCORM hedef seçimi (üretimin ilk kararı)

**Tek kural, iki yerde:** bu dosya Workflow **adım 1** ile pre-flight **Madde 11**'in kullandığı
*aynı* kuraldır. İkisi de buraya işaret eder; kural burada değişir, iki yerde birden değişmez.

> **Paket üretebilmek, hedef LMS'in o sürümü oynatabildiği anlamına gelmez.** Sunucu hangi SCORM
> hedefini isterseniz paketler; paketi **oynatan** taraf LMS'tir. Bu iki şeyi aynı cümlede
> saymak, teslimde "kurs açılmıyor / ilerleme kaydedilmiyor" olarak geri döner.

## Kural

**L0 — Önce LMS'i kaydet, sonra hedefi seç.** Sürüm seçimi brief'in *özellik listesinden* değil,
hedef LMS'in **oynatma yolundan** çıkar. Üç alan, tahmin değil kayıt:

1. **LMS adı + sürümü** ("Moodle 4.5", "şirket LMS'i" değil).
2. **Oynatma yolu:** *yerleşik* modül mü, *ek modül / entegrasyon* mu?
3. **Kanıt:** üreticinin kendi uyumluluk belgesi (bağlantı) **veya** o kurulumda yapılmış bir test
   (kim, ne zaman). Üçüncü el blog yazısı, forum cevabı veya "muhtemelen destekler" kanıt değildir.

**L1 — Hedefi oynatma yolu belirler.**

| Hedef LMS / yol | SCORM hedefi | Kanıt notu |
|---|---|---|
| **Moodle — yerleşik SCORM etkinliği** | **1.2** | Moodle'ın kendi belgesi SCORM 2004'ü desteklemediğini söylüyor; SCORM 1.2 ve AICC destekli. Bkz. [Moodle SCORM FAQ](https://docs.moodle.org/en/SCORM_FAQ). Belge, 2004 API'sinin *parçalarının* uygulandığını ve bazı 2004 paketlerinin "çalışıyor gibi görünebileceğini" de söylüyor — bu bir destek beyanı değil, tam tersi bir uyarıdır. |
| **Moodle + ticari SCORM oynatma entegrasyonu** (ör. Rustici'nin SCORM Cloud eklentisi) | 2004 **yalnız** o entegrasyon **o kurulumda** doğrulanmışsa | Ek modül ücretli/harici bir hizmet olabilir; varlığını değil, **kurulumda etkin olduğunu** doğrula. Aynı Moodle FAQ bu yolu adlandırıyor. |
| **Üreticisi SCORM 2004 oynatımını kendi belgesinde yazan LMS** | 2004 uygun | Belgeyi **bağlantıyla** karar kaydına yaz. Hangi edition (3rd / 4th) olduğunu da yaz. |
| **LMS bilinmiyor / "kurumsal LMS" deniyor** | **1.2 tabanı** + "teslim uyumu doğrulanmadı" etiketi | Bilinmeyen LMS'te hiçbir hedef doğrulanmış sayılmaz. Bkz. L2. |

**L2 — Hedef LMS bilinmiyorsa teslim uyumu DOĞRULANMIŞ SAYILMAZ.** Kurs yine üretilir, ama:
`SCORM HEDEF KARARI` kaydına "LMS doğrulanmadı" yazılır, taban olarak 1.2 seçilir (daha geniş
oynatılan taban) ve Bölüm 0'ın **TEK** sorusu buna harcanır: *"Kurs hangi LMS'in hangi sürümüne
yüklenecek ve SCORM oynatması yerleşik mi?"*. Varsayma, "herhangi bir LMS'te çalışır" yazma.

**L3 — Özellik türü tek başına 2004 seçtirmez.** Dallanma (`visible_if`), değişkenler, puan/oyun
mekanikleri kursun **kendi motorunda** koşar; SCORM hedefi bunları *çalıştırmaz*, LMS'in ne
**kaydettiğini** belirler. Dolayısıyla "oyun var → 2004" bir çıkarım değil, atlanmış bir adımdır.
2004'ün gerçekten getirdiği ve 1.2'de **dar** olan iki şey:

- **Durum alanı sayısı.** 2004 `completion_status` ile `success_status`'u ayrı taşır. 1.2'de tek
  `cmi.core.lesson_status` vardır: "tamamladı" ile "geçti" aynı alana sığar. 1.2 seçildiyse bu alanın
  **hangisini** taşıdığı karar kaydına yazılır (`tracking.completion_rule` + `passing_score` ile
  tutarlı olmalı) — rapor okuyan yöneticiye ayrı iki sütun **vaat edilmez**.
- **Askıya alınan durumun boyutu.** Değişkenler/dallanma durumu `suspend_data` içinde sürer
  (`interactivity-and-gamification.md`). SCORM 1.2'de bu alan spesifikasyon gereği dardır
  (4096 karakter); 2004'te belirgin biçimde geniştir. 1.2 hedefinde **ölç, varsayma**: gerçek kursu
  hedef LMS'e yükle, çık–geri dön ve durumun korunduğunu gör. Bu sayıyı brief'e "sorun değil" diye
  yazmak, ölçülmeden yazılmışsa bir iddiadır.

**L4 — Desteklenmeyen hiçbir şey sessizce düşürülmez.** Seçilen hedefin kaydetmediği bir şey varsa
üç seçenekten biri **yazılır**: (a) özellik kurs içinde kalır ama LMS'e raporlanmaz (nereden
görülecek?), (b) özellik tasarımdan çıkar ve brief sahibine *neden* çıktığı söylenir, (c) hedef LMS
tarafında ek modül doğrulanır ve 2004'e geçilir. Sessiz düşürme = ihlal.

## Karar kaydı (kopyala, doldur)

```text
SCORM HEDEF KARARI
- Hedef LMS / sürüm : <ad> <sürüm>            (bilinmiyorsa: "doğrulanmadı")
- Oynatma yolu      : yerleşik modül | ek modül/entegrasyon: <ad>
- Kanıt             : <üretici belgesi bağlantısı> | <kurulumda test: kim, ne zaman>
- SCORM hedefi      : 1.2 | 2004
- Gerekçe           : <tek cümle, LMS'e dayanır — özellik listesine DEĞİL>
- Sınırlamalar      : <hedefin kaydetmediği şeyler + her biri için L4 seçimi>
- Test yolu         : <paket → bu LMS'e yükleme → ölçülecek davranış>
- Doğrulanmayanlar  : <açıkça; "hiçbiri" yazmak için gerçekten hiçbiri olmalı>
```

Bu kaydı **pre-flight Madde 11'de** göstermek zorunludur; kayıt yoksa `scorm_version` "doğru"
işaretlenemez.

## Örnek — dallanmalı + oyunlu Moodle brief'i

**Brief:** "Moodle 4.5 kullanıyoruz (yerleşik SCORM etkinliği). Saha ekibi için dallanmalı bir
vaka: yanlış kararda farklı yola gitsin, puan göstergesi olsun, sonunda geçti/kaldı raporlayalım."

Eski (yanlış) akıl yürütme: *dallanma + oyun var → 2004*. L0 atlandığı için paket Moodle'ın
yerleşik oynatıcısında doğrulanmamış bir hedefle teslim edilirdi.

```text
SCORM HEDEF KARARI
- Hedef LMS / sürüm : Moodle 4.5
- Oynatma yolu      : yerleşik SCORM etkinliği (ek modül yok, yöneticiden teyitli)
- Kanıt             : https://docs.moodle.org/en/SCORM_FAQ — core'da SCORM 2004 desteklenmiyor;
                      1.2 ve AICC destekli
- SCORM hedefi      : 1.2
- Gerekçe           : Hedef oynatıcı yerleşik Moodle modülü; 2004 bu yolda desteklenmiyor.
                      Dallanma ve puan kursun kendi motorunda koşuyor, hedefi onlar seçmiyor (L3).
- Sınırlamalar      :
  * Tek durum alanı: 1.2'de "tamamladı" ve "geçti" aynı alanda. Karar: lesson_status
    GEÇME durumunu taşır (completion_rule = viewed_all_and_passed, passing_score = 70).
    Yöneticiye "ayrı tamamlama ve başarı sütunu" VAAT EDİLMEDİ — brief sahibine söylendi (L4-a).
  * suspend_data darlığı: dallanma + puan durumu buradan sürüyor. Ölçülmeden "yeterli" denmedi;
    test yolunun 3. adımı bunu ölçüyor.
  * Puan göstergesi LMS'e ayrı bir metrik olarak gitmiyor (kurs içi HUD). Düşürülmedi,
    raporlanmadığı yazıldı (L4-a).
- Test yolu         : build_package → Moodle 4.5'te SCORM etkinliği olarak yükle →
                      (1) açılış, (2) iki farklı dalda ilerleme, (3) ortadan çık + geri dön
                      (durum ve puan korunuyor mu), (4) geçti/kaldı raporu gözle.
                      Yöntem olarak açık depodaki SCORM 1.2 kabul senaryosu kullanılır:
                      https://github.com/kemalyy/edumints-scorm-mcp/issues/198
                      (senaryo burada yeniden yazılmaz, referans alınır).
- Doğrulanmayanlar  : Bu karar kaydı yazıldığında gerçek Moodle 4.5 kurulumunda henüz koşulmadı;
                      test yolu tamamlanana kadar teslim uyumu doğrulanmış sayılmaz.
```

## Karşı örnek A — SCORM 2004 oynatımı belgelenmiş LMS

Hedefi **özellik** değil **belge** seçer; burada 2004 doğru cevaptır ve gerekçe LMS'e dayanır:

```text
- Hedef LMS / sürüm : <LMS adı> <sürüm>
- Oynatma yolu      : yerleşik oynatıcı
- Kanıt             : <üreticinin kendi uyumluluk sayfası — bağlantı> ; belgelenen edition: 2004 <3rd|4th>
- SCORM hedefi      : 2004
- Gerekçe           : Üretici bu sürümde 2004 <edition> oynatımını kendi belgesinde yazıyor.
- Sınırlamalar      : Edition farkı: paket <edition> olarak üretilecek; belge başka bir edition
                      diyorsa hedef ona göre daralır.
- Test yolu         : build_package → bu LMS'e yükle → tamamlama ve başarı durumlarının AYRI
                      raporlandığını gözle (2004'ü seçmenin asıl kazancı bu).
- Doğrulanmayanlar  : <varsa>
```

**Burada LMS adı bilinçli olarak boş bırakıldı.** Bu rehber hiçbir LMS'in 2004 desteğini kendi
adına beyan etmez; yazar üreticinin belgesini bağlantıyla koyar. Doğrulanmamış bir uyumluluk
iddiasını rehbere yazmak, teslimde kırılan tam da o iddiadır.

## Karşı örnek B — LMS belirsiz brief

**Brief:** "Yeni işe başlayanlar için 5 dakikalık bir oryantasyon kursu, LMS'imize yükleyeceğiz."

```text
- Hedef LMS / sürüm : doğrulanmadı ("LMS'imiz" — ad ve sürüm yok)
- Oynatma yolu      : bilinmiyor
- Kanıt             : yok
- SCORM hedefi      : 1.2 (taban; daha geniş oynatılan hedef)
- Gerekçe           : Hedef oynatıcı bilinmiyor; bilinmeyen LMS'te hiçbir hedef doğrulanmış
                      sayılmaz, bu yüzden taban seçildi (L2).
- Sınırlamalar      : TESLİM UYUMU DOĞRULANMADI. 1.2'nin tek durum alanı ve dar suspend_data'sı
                      geçerli; LMS netleşince hedef yeniden değerlendirilir.
- Test yolu         : LMS adı/sürümü gelince L1 tablosundan hedefi türet, sonra yükleme testi.
- Doğrulanmayanlar  : her şey — bu kayıt bir karar değil, kararın bekletilme gerekçesidir.
```

Bölüm 0'ın **TEK** sorusu buna harcanır: *"Kurs hangi LMS'in hangi sürümüne yüklenecek, SCORM
oynatması yerleşik mi?"*. Cevap gelmezse kurs yine teslim edilir ama **"herhangi bir LMS'te
çalışır" denmez** — doğrulanmadığı yazılır.

## Dürüstlük sınırı (bu dosyanın kapsamı)

Bu dosya **yazarlık rehberidir**: ne sunucuya yeni bir yetenek atfeder, ne de doğrulanmamış bir
LMS uyumluluğu beyan eder. Tek dış olgu kaynağı LMS üreticisinin kendi belgesidir (yukarıda
Moodle için bağlantılı). Hedef LMS'te gerçek bir yükleme testi yapılmadıysa, hangi sürüm seçilmiş
olursa olsun doğru cümle şudur: **"paket üretildi, hedef LMS'te doğrulanmadı."**
