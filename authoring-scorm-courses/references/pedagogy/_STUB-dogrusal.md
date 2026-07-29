---
pack: stub-dogrusal
name: "ŞEMA ÖRNEĞİ — doğrusal akış (paket DEĞİLDİR)"
version: 1
outcome_types: [prosedür]
prior_knowledge: [1, 5]
error_cost: [orta, yüksek]
requires_platform: []
phases:
  - id: goster
    amac: "Beceri gerekçeli, adım adım gösterilir — çözümlü örnek (kanıt) burada üretilir."
    izinli_ekran_tipleri: [content_slide, video, image_compare, timeline]
    skorlanabilir: false
  - id: kilavuzlu_deneme
    amac: "Öğrenen destekle dener; denemeler skorSUZdur (Z3) ve karşılaştırmalı kanıt üretir."
    izinli_ekran_tipleri: [simulation, mcq, fill_blank, hotspot]
    skorlanabilir: false
  - id: bagimsiz_olcum
    amac: "Destek çekilir; üretilen kanıta bağlı beceri skorlu ölçülür."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phases: [goster, kilavuzlu_deneme]
scoring_allowed_from: bagimsiz_olcum
conflicts_with: []
---

# ŞEMA DOĞRULAMA ÖRNEĞİ — doğrusal akış

Bu dosya bir yöntem paketi **değildir**; `pack-frontmatter.schema.json` sözleşmesinin
çalıştırılabilir doğrulama örneğidir (`python3 scripts/validate_packs.py`). Gerçek paketler
C1–C12 kapsamında ayrı dosyalar olarak gelir. Bu örnek şunları gösterir:

- Doğrusal akış: `sonraki` alanı yok → fazlar dizi sırasıyla ilerler.
- Çoğul kanıt beyanı: `evidence_phases` iki fazı birden gösteriyor (1:1 dayatması yok).
- `scoring_allowed_from` öncesi fazlar `skorlanabilir: false` (Z2 paket-düzeyi beyanı).
