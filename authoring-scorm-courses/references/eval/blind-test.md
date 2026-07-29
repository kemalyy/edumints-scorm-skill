# Kör test protokolü — kanıt kaynakları olmadan sorular cevaplanabiliyor mu?

Kanıt bağlamanın (`references/core/evidence-binding.md`) işe yaradığının **tek nesnel testi**.
Alanı bilen bir okuyucu, kanıt kaynakları çıkarılmış kursun skorlanan sorularını yine de
cevaplayabiliyorsa, sorular **öğretimi değil ön bilgiyi** ölçüyordur. Bu belge kalıcıdır: her yeni
paket/şablon dalgasında yeniden koşulur ve yeni ekran tiplerinin (worked_example / exploration —
F1/F2) **kapısıdır**: kör test geçilmeden başlamazlar.

## Protokol

1. **Kopyala:** kursun spec'inin bir kopyasını al (orijinale dokunma).
2. **Kanıt kaynaklarını çıkar:** K1 türlerini taşıyan ekranları kopyadan sil (çözümlü örnek, keşif
   etkileşimi, vaka artefaktı, kanonik çözüm, veri görseli…). Skorlanan soru ekranları kalır.
   *Not:* soru ile kanıt aynı ekrandaysa (örn. artefakt üzerinde çalışan `simulation`) ekran kalır;
   artefaktın kendisi olmadan adımın yapılamayacağı ayrıca not edilir.
3. **Kör okuyucu bul:** kursu **hiç görmemiş** ama **alanı bilen** bir okuyucu — insan uzman ya da
   kurs içeriği verilmemiş temiz-bağlam bir LLM oturumu.
4. **Cevaplat:** okuyucu skorlanan soruları KAYNAKLAR OLMADAN cevaplamayı dener. Soru başına kayıt:
   kaynaksız cevaplanabildi mi (E/H) + tek cümle dayanak.
   *Sınıflama notu:* okuyucu cevabı **sorunun kendi gövdesinde verili olgudan** (+ alan bilgisi)
   türetiyorsa bu, kanıttan kopya değildir — dayanağa **[GÖVDE]** yazılır ve soru **E sayılır**
   (kaynak gerekmedi; `references/core/evidence-binding.md` K4 ihlali).
5. **Oranı hesapla:** `kaynak gerektiren soru sayısı / toplam skorlanan soru sayısı`.

## Geçme eşiği (sayısal)

> **≥ 1/2 — soruların EN AZ YARISI için kaynaklara başvurma ihtiyacı doğmalı.**

Oran < 1/2 → kurs kör testi **GEÇEMEZ**: sorular ağırlıkla ön bilgiyi ölçüyor. Kalan her
"E" sorusuna `evidence-binding.md` K3 ("bağla ya da at") uygulanır; sonra test yeniden koşulur.
(1/2 bir taban eşiğidir, hedef değildir — ideal kurslarda oran 1'e yaklaşır.)

## Sonuç kayıt şablonu

```
Kurs: <spec dosyası / project_id>        Tarih: <YYYY-AA-GG>
Okuyucu: <insan uzman | temiz-bağlam LLM>  Çıkarılan kanıt ekranları: <id listesi>

| Soru (id) | Tip | Kaynaksız cevaplanabildi mi (E/H) | Dayanak (tek cümle) |
|---|---|---|---|

Oran: <kaynak gerektiren> / <toplam skorlanan>   Sonuç: GEÇTİ (≥ 1/2) | KALDI (< 1/2)
Kalan işler: <E-sorularına K3 kararları>
```

## Pilot koşu — `examples/example-cybersecurity-course.json`

```
Kurs: examples/example-cybersecurity-course.json   Tarih: 2026-07-29
Okuyucu: temiz-bağlam LLM (alan: temel siber güvenlik farkındalığı)
Çıkarılan kanıt ekranları: why, concepts, izle (video içeriği spec'ten doğrulanamıyor — kanıt sayılmadı)

| Soru (id) | Tip | Kaynaksız cevaplanabildi mi (E/H) | Dayanak (tek cümle) |
|---|---|---|---|
| q1 | mcq (20p) | E | "Aciliyet baskısı" alan bilgisiyle bilinir; kursun yazarlı metni zaten hiçbir yerde öğretmiyor |
| match | matching (20p) | E | "Parola yöneticisi + MFA" alan-standart eşleşme; parola yöneticisi kursta hiç geçmiyor |
| uygula | simulation (20p) | H | Bölge tıklama + giriş, e-posta artefaktının kendisi olmadan yapılamaz (soru = artefakt istisnası) |
| scenario/c2 | branching (+10) | E | "Başka kanaldan doğrula" alan-standart refleks; kurs bunu önceden gerekçelendirmiyor |

Oran: 1/4 kaynak gerektirdi   Sonuç: KALDI (< 1/2)
Kalan işler: q1 → bağla (süre-baskısı cümlesini üreten vaka artefaktı ekle — evidence-binding.md
ÖNCE/SONRA örneği); match → bağla (parola yöneticisi hiçbir hedefe/içeriğe bağlı değil: içerik ekle
ya da çifti at); scenario/c2 → bağla ya da skorsuz yap (Z3).
```

Pilot, v2.0 denetim bulgusunu doğruluyor: amiral gemisi örnek dahi eşiği geçemiyor — kanıt bağlama
(K1–K3) uygulanmadan üretilen kurslar ön bilgi anketi üretir.
