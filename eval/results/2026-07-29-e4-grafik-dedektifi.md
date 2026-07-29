# E4 kör test — 2. koşu (vitrin kursu, K4/K5 sonrası) — GEÇTİ

```
Kurs: showcase-v2/spec.json (Grafik Dedektifi, 5e-inquiry, 16 ekran / 4 skorlu ekran = 10 skorlu karar)
Tarih: 2026-07-29   Okuyucu: temiz-bağlam LLM (veri-okuryazarlığı uzmanı) — 3 ayrı taze okuyucu, 3 iterasyon
Çıkarılan kanıt ekranları: cs_ajans, q_tahmin, ec_eksen, dc_satis, dc_sikayet, tl_revizyon, cs_reklam, acc_teknikler

SON KOŞU (iterasyon 3, tüm yamalar sonrası):
Oran (muhafazakâr: şans-doğru = E): 5 / 10   Sonuç: GEÇTİ (≥ 1/2)
Oran (öz-beyan + yanlış-cevap = H): 7 / 10
Not: "alan bilgim yeter" diyen uzman i_cift_eksen, i_eksik_test ve i_reklam_kat'ta YANLIŞ cevap verdi —
artefaktsız akıl yürütme özgüvenli ama hatalı; sorular tasarlandığı gibi çalışıyor.
```

## İterasyon geçmişi (kural setine geri beslenen bulgular)
1. **Koşu A (4/10 → KALDI):** özet ekranı oyun kararlarını sıralı ifade ediyordu (K5 ihlali — yazar
   ajan kendi yeni kuralını çiğnedi); tek-şerh oyun mimarisi kendini ele veriyordu; çeldirici
   asimetrileri ([GÖVDE]). → Oyun düğümleri "hangi şerh" teşhis mimarisine çevrildi.
2. **Koşu B (4/10 → KALDI):** YENİ SIZINTI SINIFI: **çapraz-madde kontaminasyonu** — bir sorunun
   gövdesi başka sorunun cevabını öğretiyor (q_eksen gövdesi n_satis teşhisini, i_zirve gövdesi seri
   derinliğini). Ayrıca düzenek hatası: sökülmüş pakete iç seçenek ID'leri (serh_yanlis) basılmıştı.
3. **Koşu C (5-7/10 → GEÇTİ):** çapraz ayrıştırma + simetrik çeldiriciler (aynı-sezon mekanizma
   varyantları; hepsi-daraltma aralıkları; hepsi-modest yüzdeler) + anonim düzenek.

## Kalan bilinen zayıflık (kayıt)
Üç oyun düğümünün teknik-dağılım çıkarımı: 3 slayt × 3 ünlü teknik + diğer maddelerin dolaylı
atıflarıyla uzman eşleme yapabiliyor ([KOPYA] 3 madde). Taban eşiği aşıldı; ideal → 1.0 için
teknik-dağılım çeşitlendirmesi (aynı teknik iki slaytta, bir teknik hiç) sonraki revizyona.

## Karar
Protokol eşiği sağlandı → **F1/F2 yatırım kapısı AÇILABİLİR** (SV#112/#113). Çapraz-madde
kontaminasyonu için K6 kural issue'su açıldı.
