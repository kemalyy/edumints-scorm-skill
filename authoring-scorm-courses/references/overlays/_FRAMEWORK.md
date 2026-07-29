# Katman 2 — Kaplama (overlay) çerçevesi (`references/overlays/`)

Bazı kaygılar yönteme **diktir**: bilişsel yük, UDL, motivasyon, uzmanlığa uyarlama, ölçme hizası,
erişilebilirlik. Bunlar paket değil **kaplamadır** — her paketin bunları yeniden icat etmesini (ve
birbiriyle çelişmesini) bu çerçeve engeller.

## Ayraç: paket mi, kaplama mı?

> **Sıra dayatan = paket. Sırasız değiştiren = kaplama.**

Bir yapı ekranların/fazların hangi sırayla geleceğini söylüyorsa pakettir (Katman 3,
`references/pedagogy/`); mevcut sıraya dokunmadan kararları (ekran seçimi, doz, dil, medya,
ölçme biçimi) modüle ediyorsa kaplamadır. Sınır örneği: *tam öğrenme* (`mastery-learning`) eşik
döngüsü **sıra dayattığı** için pakettir, kaplama değil. Bir kaplama taslağı kendini sıra dayatırken
buluyorsa yanlış katmandadır — pakete taşınır.

## 6 kaplama (D1–D6) ve kapsam sınırları

| Kimlik | Kapsamı | Kapsam SINIRI (bunu yapmaz) |
|---|---|---|
| `cognitive-load` | İçsel/dışsal yük yönetimi: bölme, ön-eğitim, gereksizlik ve bölünmüş-dikkat temizliği, doz ayarı | Yöntemin **kasıtlı** zorluğunu (üretken boğuşma, problem-önce) "yük" diye söndürmez; çakışmayı bildirir |
| `udl` | Çoklu temsil / eylem-ifade / katılım seçenekleri sunma | Teknik erişilebilirlik uyumu değil (o `accessibility`); seçenek çeşitliliği ekler, zorunluluk koymaz |
| `arcs` | Dikkat–İlgililik–Güven–Doyum motivasyon dokunuşları (açılış kancası, hedef-değer bağı, başarılabilirlik sinyali) | Oyunlaştırma mekaniği eklemez; anti-slop D1 yasakları (rozet/konfeti) aynen geçerli |
| `expertise-adaptive` | PRIOR_KNOWLEDGE'a göre destek dozu: örnek↔problem dengesi, ipucu yoğunluğu, atlama yolları | Yöntemin yapısını yeniden sıralamaz; PK kadranını okur, kendi PK tahmini üretmez |
| `assessment-alignment` | H1–H3 hizasının uygulama detayı: soru düzeyi (uygula>tanı), eşik–kural tutarlılığı, kanıt-bağ kalitesi | Yeni ölçme biçimi/kuralı icat etmez; Katman 1'i uygular, genişletmez |
| `accessibility` | WCAG AA teknik uyum: alt metin, kontrast, klavye/odak, caption/transcript, hareket azaltma | Pedagojik temsil çeşitliliği değil (o `udl`); tema estetiği kararı değil (`themes.md`) |

## Kaplama dosya biçimi

Her kaplama `references/overlays/<overlay>.md` (D serisi) — YAML ön-maddesi + gövde:

```yaml
---
overlay: cognitive-load            # kimlik (kebab-case, dosya adıyla eşleşir)
name: "Bilişsel Yük Yönetimi"
version: 1
decision_points: [icerik_dozu, medya, destek_dozu]   # hangi karar noktalarına uygulanır (beyan zorunlu)
conflicts: []                       # çakışma bildirimleri (biçim aşağıda)
---
```

**Karar noktaları sözlüğü** (`decision_points` bu adlardan seçer — kaplamanın nereye
uygulandığının beyanı):

| Karar noktası | Karar |
|---|---|
| `ekran_secimi` | Hangi ekran tipi seçilir |
| `icerik_dozu` | Ekran başına bilgi/madde/kelime dozu |
| `medya` | Görsel/ses/video kullanımı ve biçimi |
| `geri_bildirim` | Feedback içeriği ve tonu (G1–G3 üstüne) |
| `olcme` | Soru düzeyi, eşik, kanıt-bağ kalitesi |
| `destek_dozu` | İpucu/iskele/çözümlü-örnek yoğunluğu |
| `gezinme` | Atlama/tekrar yolları, ilerleme serbestliği |
| `dil_ton` | Kayıt, hitap, duygu dokunuşları |

## Paket-bağımsızlık kuralı (mekanik denetlenir)

**Kaplama metni hiçbir paket faz adı içeremez.** Kaplama her paketin altında aynen çalışmalıdır;
faz adına referans onu tek pakete lehimler. Paket **kimliği** yalnız ön-maddedeki `conflicts`
bloğunda geçebilir (çakışma bildirmek için) — gövde metninde o da geçmez.

Mekanik denetim (grep 0 beklenir; CI'da çalışır):

```bash
python3 scripts/check_overlay_independence.py
# pedagogy/*.md ön-maddelerinden tüm faz id'lerini toplar,
# overlays/*.md dosyalarında arar; eşleşme sayısı 0 değilse FAIL.
```

## Çakışma bildirim biçimi

Kaplama, bir paketin (ya da başka kaplamanın) beyanıyla çeliştiği yeri **karar noktası düzeyinde**
bildirir; tek taraflı bildirim yeterlidir (paket tarafındaki karşılığı `conflicts_with` alanıdır,
bkz. `pedagogy/_SCHEMA.md`):

```yaml
conflicts:
  - with: productive-failure        # paket ya da kaplama kimliği
    decision_point: destek_dozu     # yukarıdaki sözlükten
    rule: "Paketin kasıtlı-zorluk bölümlerinde bu kaplamanın destek-artırma önerileri
           askıya alınır; paket beyanı önceliklidir."
```

Zorunlu üç alan: `with` (kimlik), `decision_point` (sözlükten), `rule` (tek-iki cümle çözüm
kuralı — kim önceliklidir, hangi koşulda). Çözüm kuralı yazılmamış çakışma = bildirim değil,
belirsizlik; yasak.

## Uygulama kuralları

- Kaplamalar Katman 0 seçicisinin çıktısında listelenir (`core/method-selector.md` YÖNTEM BEYANI);
  hiçbir kaplama otomatik/zorunlu değildir — seçim gerekçelidir.
- Kaplama, yalnız beyan ettiği `decision_points` üzerinde konuşur; beyan dışı alana taşan
  öneri geçersizdir.
- Kaplamalar Katman 1'i **gevşetemez** (K/H/G/Z ve anti-slop tabanları her kaplamanın altında
  geçerli kalır) ve paket sırasına dokunamaz.
- Birden çok kaplama aynı karar noktasında çelişirse: önce `conflicts` bildirimlerine bak;
  bildirim yoksa yazar gerekçeli seçer ve pre-flight Madde 1b'ye yazar.

Kaplamaların içerikleri D1–D6 kapsamında ayrı dosyalar olarak gelir; bu çerçeve yalnız biçimi ve
sınırları tanımlar.
