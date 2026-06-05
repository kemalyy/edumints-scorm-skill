# Üretim önerileri — profesyonel SCORM kursları için karar rehberi

Bu dosya *ne yapacağını* değil **ne zaman/nasıl/neden** seçeceğini söyler. Profesyonel e-öğrenme
kalitesine ulaşmanın farkı tekil özelliklerde değil, bu kararların disiplininde.

## 1. Sahne modu & timeline akışı (Faz 9 — varsayılan profesyonel mod)

**Varsayılan `layout_mode:"stage"` kullan.** İçerik sabit 16:9 sahnede ölçeklenir; bloklar
(başlık → paragraf/madde → medya) seslendirmeyle senkron, zamanlanmış belirir. Bu, "tasarlanmış
slayt" hissini verir — `flow` (tam-akış) yalnızca uzun referans/erişilebilirlik metinleri için.

| Durum | Öneri |
|---|---|
| Anlatımlı içerik slaytı | `reveal:"auto"` + `narration_asset_id` + `narration_text` (CC). Bloklar sese senkron akar. |
| Ses üretmiyorsan | `reveal:"auto"` yine çalışır (paced ~2.5sn/blok) **veya** `reveal:"click"` (öğrenci kendi hızında ilerler — daha katılımcı). |
| Quiz / drag / simülasyon | dokunma — varsayılan `reveal:"none"` (içerik hemen görünür). Timeline etkileşimi engellemez. |
| Yoğun-bilişsel adım | `reveal:"click"` seç: her tıklamada tek fikir → bilişsel yük azalır. |
| Önemli onay ekranı | `lock_until_complete:true` — öğrenci anlatımı bitirmeden geçemesin (yalnız kritik ekranlarda; her yerde kullanma, sinir bozar). |

**Blok ritmi:** ekran başına **3–6 reveal bloğu** ideal. 1 blok = timeline'sız, donuk; 10+ blok =
bekleme yorucu. Uzun içeriği iki ekrana böl.

**Animasyon kısıtı:** `animation` varsayılanı `fade-up` — sakin, profesyonel. `zoom`/`slide-left`'i
yalnız vurgu için seyrek kullan. Tüm kursu `zoom` yapmak ucuzlaştırır. `prefers-reduced-motion`
otomatik saygı gösterilir — sen ekstra bir şey yapma.

## 2. Seslendirme (narration) yazımı

- **`narration_text` = altyazı + timeline süre kaynağı.** Her anlatımlı ekrana ekle (erişilebilirlik
  + SEO + sessiz izleme). Ekranda yazan metni **birebir tekrarlama** — anlatım metni ekrandaki
  maddeleri *genişletir/bağlar*, kopyalamaz ("ekranı sesli okuma" en sık şikayet).
- Konuşma dili kullan: kısa cümle, 2. tekil şahıs ("...yapabilirsin"), ekran başına ~15–40 sn.
- Sesi bir TTS MCP'den çek → `add_asset` → `narration_asset_id`. Süreyi runtime ölçer; sen
  saniye hesaplama.

## 3. Pedagojik ritim (anti-template-fatigue)

- **~2 içerik ekranında 1 etkileşim.** 8 ardışık content_slide = terk. Tipleri çeşitlendir:
  accordion/tabs/flashcards keşif için, mcq/matching/sorting yoklama için.
- **İzle → Uygula → Sıra Sizde**: bir beceri öğretirken video (göster) → simulation (rehberli dene)
  → quiz (tek başına). Araç/yazılım eğitiminin altın kalıbı (`course-patterns.md` Pattern A).
- Mikroöğrenme: tek ölçülebilir hedef, 3–8 dk. Daha uzunsa böl.
- Her bölümü bir **özet + tek net çıkarımla** kapat.

## 4. Değerlendirme & geri bildirim

- Soruyu hedefe hizala; "ezber" değil "uygula" sorusu sor (senaryo > tanım).
- **Her quizde hem doğru hem yanlış için anlamlı `feedback`.** Yanlışta *neden* yanlış olduğunu
  söyle ve ilgili İzle bölümüne yönlendir — sadece "Yanlış" deme.
- Oyunlaştırma: `points_var` + `on_correct` ile içsel ilerleme hissi. Rozet/liderlik tablosu
  yerine *ustalaşma* mesajı (kullanıcı tercihi: patronlaştırıcı mekanik yok).

## 5. Tema & erişilebilirlik

- Açık/nötr/yüksek-kontrast standarttır (`modern-light`, `academic`, `high-contrast`). Keyfi
  koyu tema **kullanma**. Marka için yalnız vurgu rengini override et.
- Görsellere `alt`, net dil, yeterli kontrast (temalar halleder). Stage modunda metin ölçeklenir —
  mobilde okunurluk için ekranı aşırı doldurma.

## 6. Teslimden önce kalite çıtası (özet)

- [ ] Ölçülebilir hedef; her ekran ona hizmet ediyor.
- [ ] ~2 içerik ekranında ≥1 etkileşim; tip çeşitliliği var.
- [ ] Anlatımlı ekranlarda `narration_text` + uygun `reveal`; quiz dışı içerik stage modunda akıyor.
- [ ] Ekran başına 3–6 reveal bloğu; animasyon ölçülü.
- [ ] Quizlerde iki yönlü geri bildirim + hizalı sorular.
- [ ] Açık/kontrastlı tema, alt metinleri, sade dil.
- [ ] Önce `preview` → gözden geçir/geri bildirim → düzelt → `build_package`.

Karşılığı olmayan ağır özelliği (video, lottie) sırf "havalı" diye ekleme — bir şey **öğretiyorsa**
ekle. Sadelik = profesyonellik.
