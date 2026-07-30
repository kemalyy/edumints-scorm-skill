# Kör test — SENARYO HATTI kapanış kapısı (kabul #15) — GEÇTİ

```
Kurs: "Sözleşme Dedektifi" — TAMAMEN senaryo araçlarıyla üretildi (create_scenario →
       upsert_node/page → fill_media_slot → scenario_gaps → scenario_compile), doğrudan spec DEĞİL.
       16 ekran / 4 skorlu / 3 hedef / multipack (5e-inquiry O1 + rosenshine-di O2/O3) / 5 medya yuvası.
Tarih: 2026-07-30   Okuyucu: temiz-bağlam LLM (B2B tedarik sözleşmeleri uzmanı) — 2 taze okuyucu, 2 iterasyon
Derleme: 0 err / 0 warn / coverage 1.0 (normal+strict) · gaps 1 iterasyon · PROVENANCE.json 5 kayıt

İterasyon 1 (2/4 — EŞİKTE, marjinal):
  q_yenileme [TAHMİN] · q_fesih [TAHMİN] · q_fiyat [ALAN, çeldirici asimetrisi] · q_tavan [ALAN, kanon]

İterasyon 2 (4/4 — GEÇTİ, kaynağa dönme tam):
  | Soru | Sınıf | Neden |
  |---|---|---|
  | q_yenileme | TAHMİN | başlangıç+90-gün penceresi yalnız Madde 8 artefaktında |
  | q_fiyat    | TAHMİN | çeldiriciler simetrikleştirildi — dördü de gerçek fiyat-koruma üçlüsü; hangisinin B'de kaldığı yalnız A/B çiftinde |
  | q_tavan    | TAHMİN | spesifik-tutar sorusuna çevrildi — 250.000 TL / %100 tavan yalnız Madde 11'de; dolaylı-zarar kanonundan çözülmez |
  | q_fesih    | TAHMİN | ceza tabanı ("kalan dönem toplam bedeli") yalnız Madde 14'te |

Oran: 4 / 4   Sonuç: GEÇTİ (≥ 1/2, hatta 1'e ulaştı)
```

## Anlamı
Senaryo hattı (yüksek-debili şablon üretim yolu) v1 kalitesini v2 hızında ÜRETMEDİ.
Uçtan uca senaryo araçlarıyla, tek geçişte 0-engelleyici derlenen bir kurs, kör testi geçti.
İki-iterasyonluk güçlendirme (çeldirici simetrisi + kanon→artefakt bağlama), önceki gösterge
kursunun aynı örüntüsünü tekrarladı — kalite kapısı şablon yolunda da çalışıyor.

## Kabul #15 KARŞILANDI → sürüm hattı "tamam" sayılabilir.
