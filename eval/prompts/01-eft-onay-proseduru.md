---
id: E3-01
girdi_turu: serbest-konu
kazanim_turu: [prosedür]
prior_knowledge: 2
hata_maliyeti: yüksek
zaman_butcesi_dk: 6
---

# İstem

Muhasebe ekibimiz yeni bankacılık panelinde yüksek tutarlı EFT'leri çift onay akışından
geçirmeyi öğrenecek: talimatı gir, ilk onaycıya yönlendir, ikinci onaycı limit kontrolüyle
serbest bırakır. Ekip paneli hiç görmedi; yanlış serbest bırakma geri alınamıyor. 6 dakikalık
bir SCORM mikrokursu üret.

## Beklenen v2 sinyalleri (skorlama notu — isteme dahil edilmez)

- YÖNTEM BEYANI: prosedür · PK düşük · hata maliyeti yüksek → `rosenshine-di` (ya da gerekçeli
  4cid elemesi); gerekçe cümlesi zorunlu.
- Çözümlü örnek / gösterim ekranı ÜRETİLMELİ (kanıt kaynağı); skorlu sorular ona
  `evidence_screen_ids` ile bağlı; rehberli deneme `points: 0`.
- v1 tipik başarısızlığı: panel hiç gösterilmeden "çift onay neden önemlidir?" tarzı
  ön-bilgi MCQ'ları (coverage 0).
