---
pack: stub-dongulu
name: "ŞEMA ÖRNEĞİ — döngülü akış (paket DEĞİLDİR)"
version: 1
outcome_types: [olgu, kavram]
prior_knowledge: [2, 8]
error_cost: [düşük, orta]
requires_platform: [adaptive_practice]
phases:
  - id: ogretim_turu
    amac: "Hedeflenen bilgi birimi kanıt üretecek biçimde işlenir (keşif etkileşimi ya da çözümlü örnek)."
    izinli_ekran_tipleri: [content_slide, accordion, flashcards, data_chart]
    skorlanabilir: false
    sonraki: [formatif_yoklama]
  - id: formatif_yoklama
    amac: "Skorsuz yoklama eşiğe karşı ölçer; eşik altı öğretim turuna DÖNDÜRÜR (döngü)."
    izinli_ekran_tipleri: [mcq, true_false, adaptive_practice]
    skorlanabilir: false
    sonraki: [ogretim_turu, skorlu_olcum]
    tekrar_kosulu: "Yoklama başarısı eşik (%80) altındaysa ogretim_turu fazına dön; eşik ve üstünde skorlu_olcum fazına geç."
  - id: skorlu_olcum
    amac: "Eşiği geçen öğrenen, döngüde üretilmiş kanıta bağlı skorlu ölçüme girer."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
evidence_phase: ogretim_turu
scoring_allowed_from: skorlu_olcum
conflicts_with: []
---

# ŞEMA DOĞRULAMA ÖRNEĞİ — döngülü akış

Bu dosya bir yöntem paketi **değildir**; şemanın **doğrusal olmayan** paketleri de taşıyabildiğinin
doğrulama örneğidir (#14 risk notu: "döngü/koşul ifade edebilmeli"). Gösterdikleri:

- Döngü: `formatif_yoklama.sonraki` hem geriye (`ogretim_turu`) hem ileriye (`skorlu_olcum`)
  işaret eder; `tekrar_kosulu` hangi koşulda hangi geçişin alınacağını beyan eder.
- Tekil kanıt beyanı biçimi: `evidence_phase` (çoğul biçim için bkz. `_STUB-dogrusal.md`).
- Platform sert kısıtı: `requires_platform: [adaptive_practice]` — yetenek yoksa Katman 0
  seçicisi bu paketi eler.
