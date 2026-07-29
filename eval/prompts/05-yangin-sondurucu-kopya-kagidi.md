---
id: E3-05
girdi_turu: sıkıştırılmış-referans
referans_bicimi: kopya kâğıdı (cheat-sheet tablosu)
kazanim_turu: [olgu, prosedür]
prior_knowledge: 2
hata_maliyeti: yüksek
zaman_butcesi_dk: 6
kaynak_madde_sayisi: 6
---

# İstem

Elimizdeki özet tabloyu yeni çalışan oryantasyonu için 6 dakikalık bir SCORM kursuna çevir:

> **Yangın söndürücü hızlı referans**
>
> | Sınıf | Yakıt | Doğru söndürücü | ASLA |
> |---|---|---|---|
> | A | Kâğıt, ahşap, kumaş | Su, köpük, kuru kimyevi | — |
> | B | Benzin, tiner, yağ | Köpük, CO₂, kuru kimyevi | Su (yayar!) |
> | C | Elektrik panosu, cihaz | CO₂, kuru kimyevi | Su ve köpük (çarpılma!) |
> | D | Metal talaşı (Mg, Al) | D-tipi toz | Su (patlama!) |
> | F/K | Kızgın yağ (fritöz) | Islak kimyevi | Su (alev topu!) |
>
> Kullanım sırası (PASS): Pimi çek → Alevin dibine nişan al → Sık → Süpür.

## Beklenen v2 sinyalleri (skorlama notu — isteme dahil edilmez)

- **Başarısızlık-kökeni senaryosu:** v1 kokusu "madde sayısı ≈ ekran sayısı" (5 sınıf + PASS →
  6-7 ekranlık birebir aktarım + tablo-ezber quiz'i). v2'de `source_item_count: 6` beyanı
  beklenir; ekran sayısı madde sayısını kopyalamaz (`source_item_parity` uyarısı 0).
- Kanıt üretimi: sınıf→söndürücü ilişkisini GÖSTEREN bir artefakt/karşılaştırma (ör. yanlış
  söndürücü sonucu senaryosu, etiket-okuma hotspot'u) üretilmeli; skorlu sorular tabloyu değil
  o kanıtı yoklar ve `evidence_screen_ids` ile bağlanır.
- Yüksek hata maliyeti → keşif değil gösterim-önce paket beklenir (rosenshine-di / gagne-9
  gerekçeli).
