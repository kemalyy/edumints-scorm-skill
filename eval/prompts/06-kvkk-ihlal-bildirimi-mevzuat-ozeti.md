---
id: E3-06
girdi_turu: sıkıştırılmış-referans
referans_bicimi: mevzuat özeti (madde listesi)
kazanim_turu: [olgu, prosedür]
prior_knowledge: 3
hata_maliyeti: yüksek
zaman_butcesi_dk: 7
kaynak_madde_sayisi: 5
---

# İstem

Hukuk ekibinin hazırladığı şu özeti veri sorumlusu ekipler için 7 dakikalık zorunlu-uyum
SCORM kursuna çevir:

> **Veri ihlali bildirimi — özet**
> 1. İhlal öğrenildiği anda iç kayıt açılır (tarih-saat damgalı).
> 2. Kurula bildirim: öğrenmeden itibaren en geç **72 saat** içinde.
> 3. 72 saat aşılacaksa gerekçe bildirime eklenir.
> 4. Etkilenen ilgili kişilere "en kısa sürede" ve anlaşılır dille bildirim yapılır.
> 5. Bildirimde asgari içerik: ihlalin niteliği, olası sonuçlar, alınan önlemler, iletişim noktası.

## Beklenen v2 sinyalleri (skorlama notu — isteme dahil edilmez)

- **Başarısızlık-kökeni senaryosu:** v1 kokusu — 5 madde → 5 madde-slaytı + "kaç saat?" ezber
  quiz'i (coverage 0, kör testte "alanı bilen herkes 72'yi bilir"). v2'de `source_item_count: 5`
  beyanı + madde-ekran birebirliği YOK.
- Kanıt üretimi: gerçekçi bir ihlal vakası/zaman çizelgesi artefaktı üretilip skorlu sorular
  (ör. "bu vakada saat kaçta bildirim sınırı dolar?") o artefakta bağlanmalı.
- Zorunlu/uyum bağlamı → seçicide `gagne-9` + `mastery-learning` ya da `rosenshine-di`
  gerekçeli; tam kapsama iddiası varsa hedef→soru eşleme tablosu (H2) dolu.
