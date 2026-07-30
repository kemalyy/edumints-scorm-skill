# E4 kör test — F4 çok-paketli vitrin örneği (3 iterasyon + 3 kör okuyucu)

```
Kurs: authoring-scorm-courses/examples/example-multipack-ergonomics.json
      ("Aynı Sandalye, Üç Kat, Üç Sonuç" — O2 kavram → 5e-inquiry, O1 prosedür → rosenshine-di,
       assessment-alignment kaplaması; 16 ekran / 3 skorlu)
Tarih: 2026-07-30    Okuyucular: 3 ayrı temiz-bağlam LLM oturumu (alan: ofis ergonomisi)
Çıkarılan kanıt ekranları: kesif_tahmin, veri_agri, acikla_notr, model_kurulum, vaka_kayit,
vaka_plan, rehberli_kat3
Lint (son durum, sökülmeden önce): clean=True · 0 hata / 0 uyarı (strict) · coverage 1.0
```

## Son koşu (iterasyon C, okuyucu 3)

| Soru (id) | Tip | Kaynaksız cevaplanabildi mi (E/H) | Dayanak (tek cümle) |
|---|---|---|---|
| q_kavram | mcq (30p) | H | Kat kimlikleri/yerleşimleri yalnız grafik+listede; "aynı sandalye" bilgisi ikili seçmeye yetmiyor (okuyucu tahmini ~%40, şans %33). |
| q_sira | mcq (35p) | H | Alan bilgisi zincirin doğru sırasını verir ama 10:02/10:11 satırlarında HANGİ adımların yazdığını yalnız zaman çizelgesi söyler (~%45). |
| q_selin | mcq (35p) | H | Plan satırlarının içeriği tamamen sökülen ekranda; model zinciri bilinse bile neyi neye karşı okuyacağı elde yok (~%40). |

```
Oran: 3 / 3 kaynak gerektirdi   Sonuç: GEÇTİ (≥ 1/2)
```

## İterasyon geçmişi (dürüst kayıt — her okuyucunun bulduğu kanal ve yapılan düzeltme)

**İterasyon A (okuyucu 1):** oran 3/3 H — ama iki kaçak kanal işaretlendi:
1. `rehberli_kat3` (skorsuz rehberli pratik) feedback'i "önce sandalye/referans" ilkesini açık
   ediyor → q_sira tahmin gücü %33→~%55. *Düzeltme:* ekran, ilkeyi gerçekten ürettiği için
   dürüst yolla q_sira'nın `evidence_screen_ids`'ine EKLENDİ (kör test artık onu da söker).
2. q_sira ↔ eski q_referans (saat↔referans eşleştirme) çifti aynı üç saat damgasını
   paylaşıyor; şık metinleri karşılıklı çıkarsama zinciri kuruyor (K6 sınıfı).

**İterasyon B (okuyucu 2):** q_sira şıklarındaki niteleme cümleleri ("referans henüz
kurulmamıştı" / "masanın ön kenarı") tek başına ayrıştırıcıydı → q_sira "sınırda E" (~%70);
eşleştirme sorusu S2 şıklarından ~%45'e türetilebiliyor ([KOPYA] sınıfı). *Düzeltmeler:*
q_sira şıkları tam simetrik çıplak satır imlemesine indirildi; eşleştirme sorusu K6 kararıyla
KALDIRILDI ve ölçüm AYRI bir ikinci artefakta taşındı (`vaka_plan` — Selin'in henüz
uygulanmamış Kat 3 planı; `q_selin` şıkları çıplak satır numarası).

**İterasyon C (okuyucu 3):** oran 3/3 H → GEÇTİ. S2→S3 türetmesi artık YOK (q_selin kendi
artefaktına gerçekten kilitli). Tek kalan mikro bulgu: q_selin gövdesi "10:26 türü yeniden-ayar
faturası" diyerek 10:26'nın ihlal-sonucu olduğunu önvarsayıp q_sira'nın "rutin ince ayar"
çeldiricisini bedavaya eliyordu → gövde nötrleştirildi ("sonraki bir satır uygulandığında
geçersiz kalıp baştan yapılmak zorunda kalır"); Deniz/10:26 atfı gövdeden çıktı. Düzeltme
sonrası lint yeniden koşuldu: 0/0, coverage 1.0.

## Not — bu koşunun yöntem dersi

Üç iterasyonun üçü de K1 boşluğu değil SIZINTI kanalı buldu (rehberli-feedback, şık nitelemesi,
madde-çifti saat yüzeyi, gövde önvarsayımı): coverage 1.0 + strict-temiz lint yine hijyendir,
kanıt-gereksinimi değildir — K4/K5/K6'nın elle süpürülmesi ve kör testin gerçek okuyucuyla
koşulması vazgeçilmez (ilk E4 koşusunun bulgusuyla tutarlı: `2026-07-29-e4-kvkk-rosenshine.md`).
