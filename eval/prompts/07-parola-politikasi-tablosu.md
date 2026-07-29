---
id: E3-07
girdi_turu: sıkıştırılmış-referans
referans_bicimi: politika/guideline tablosu
kazanim_turu: [olgu]
prior_knowledge: 4
hata_maliyeti: orta
zaman_butcesi_dk: 5
kaynak_madde_sayisi: 8
---

# İstem

BT güvenlik ekibimizin parola politikasını tüm personel için 5 dakikalık bir SCORM
farkındalık kursuna çevir:

> **Parola ve erişim politikası (v3)**
> 1. En az 14 karakter; cümle-parola önerilir.
> 2. Parola yöneticisi zorunlu (kurumsal lisans).
> 3. MFA tüm dış erişimlerde zorunlu.
> 4. Parola paylaşımı her koşulda yasak (BT dahil kimse sormaz).
> 5. Tarayıcıya kurumsal parola kaydetmek yasak.
> 6. Şüpheli oturum uyarısı 15 dk içinde bildirilir.
> 7. Ayrılan personelin erişimi aynı gün kapatılır (yönetici sorumluluğu).
> 8. Servis hesap parolaları kasada tutulur, kişiye yazılmaz.

## Beklenen v2 sinyalleri (skorlama notu — isteme dahil edilmez)

- **Başarısızlık-kökeni senaryosu:** 8 madde → 8'e yakın ekran + "politikaya göre asgari kaç
  karakter?" ezber quiz'i v1 desenidir. v2'de `source_item_count: 8` beyanı + gruplama
  (madde ≠ ekran) + `source_item_parity` uyarısı 0.
- 5 dk dar bütçe → çok-fazlı döngü paketleri elenir; dar-kapsamlı tek kazanım seçilip
  gerisinin bilinçli bırakılması (ya da seri önerisi) beklenir — 8 maddenin tamamını
  5 dakikaya "kapsama" iddiası slop sinyalidir.
- Kanıt üretimi: en az bir gerçekçi artefakt (ör. sahte BT araması / phishing tarzı parola
  isteme diyaloğu) üretilip skorlu soru ona bağlanmalı; salt politika-metni ezberi yoklanmaz.
