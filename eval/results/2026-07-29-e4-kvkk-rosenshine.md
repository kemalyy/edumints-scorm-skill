# E4 kör test — ilk gerçek koşu (v2-yazımlı kurs)

```
Kurs: e4-run/spec.json (KVKK ihlal bildirimi, eval prompt 06, rosenshine-di, 15 ekran / 4 skorlu)
Tarih: 2026-07-29        Okuyucu: temiz-bağlam LLM (alan: KVKK/uyum)
Çıkarılan kanıt ekranları: vaka_zaman_cizelgesi, model_sinir_hesabi, sizinti_kapsami, iki_kanal, bildirim_anatomisi
Lint durumu (sökülmeden önce): 0 hata / 0 uyarı / coverage 1.0 / strict temiz

| Soru (id) | Tip | Kaynaksız cevaplanabildi mi (E/H) | Dayanak (tek cümle) |
|---|---|---|---|
| q_sinir | mcq | E | 72 saat öğrenme anından işler — Kurul kararı 2019/10; vaka saatleri soru gövdesinde zaten verili. |
| q_gecikme | mcq | E | Kademeli bildirim ilkesi alan bilgisi; ayrıca kapanış özeti cevabı birebir içeriyor. |
| q_dil | mcq | E | İlgili-kişi bildirimi "en kısa sürede + anlaşılır dil" — alan bilgisi; kapanış özeti yine sızdırıyor. |
| q_icerik | hotspot | E | Asgari dört öğe seti (GDPR md.33-34 paraleli) alan bilgisi; üçünün sayılması elemeyi kolaylaştırıyor. |

Oran: 0 / 4   Sonuç: KALDI (< 1/2)
```

## Analiz — neden kaldı (coverage 1.0 ve strict-temiz olmasına rağmen)

Tam da öngörülen ayrım: **coverage hijyendir, kanıt-gereksinimi değildir.** Kurs kanıtları gerçekten
üretti ve sorular onlara dürüstçe bağlandı; ama üç mekanizma soruları yine ön-bilgiyle çözülür kıldı:

1. **Gövde kendine-yeterliliği:** q_sinir'in ihtiyaç duyduğu vaka olgusu (Salı 16:40) soru
   GÖVDESİNDE verili — kural (alan bilgisi) + gövde olgusu = kaynak gereksiz. Kritik olgu kanıt
   ekranında kalmalı, gövdeye kopyalanmamalıydı.
2. **Kapanış sızıntısı:** özet ekranı üç sorunun cevabını tek cümlede yeniden söylüyor; kanıt
   ekranı olmadığı için sökülmedi ama fiilen ikinci bir cevap kanalı.
3. **Kanon-alan etkisi:** mevzuat içeriğinde standart kurallar alanın kamusal kanonudur; uzman
   okuyucu tanımı gereği bunları bilir. Bu tür kurslarda sorular kanonun KENDİSİNİ değil, kanonun
   KURSA-ÖZGÜ artefakta uygulanmasını ölçmeli (ör. "zaman çizelgesindeki hangi damga saati başlatır?"
   — damga yalnız kanıt ekranında yaşarken).

## Kalan işler (K3 + kural revizyonu — kullanıcı direktifi: E4 düşerse kurallar revize edilir,
paketler askıya alınmaz)
- [ ] Yeni taban kuralı: skorlu soru gövdesi, cevabın türetilmesi için gereken kritik olguyu
      İÇEREMEZ — olgu kanıt ekranında yaşamalı (gövde kendine-yeterliliği yasağı).
- [ ] Yeni taban kuralı: kanıt-dışı ekranlar (özellikle summary) skorlu cevapları yeniden ifade edemez.
- [ ] Kanon-alan rehberi: mevzuat/standart içerikte soru tipi "kural hatırlama" değil
      "artefakta uygulama" olmalı (evidence-binding.md'ye ek bölüm).
- [ ] Revizyon sonrası E4 yeniden koşulur. F1/F2 kapısı KAPALI kalır.
