# Pre-flight — teslim öncesi mekanik denetim matrisi

**BU OPSİYONEL DEĞİL.** Her kutuyu *çalıştır* — gözden geçirme değil, **mekanik sayım**. Bir kutu
bile dürüstçe işaretlenemiyorsa kurs teslime hazır **DEĞİL**: düzelt, yeniden denetle, sonra
`validate_package` → `build_package`. Override kullandıysan ilgili kutunun yanına **tek cümle
gerekçe** yaz (gerekçesiz override = ihlal).

Sıra önemli: önce **niyet** (0–2), sonra **anti-slop sayımı** (3–9), sonra **mekanik/teslim** (10–13).

## Niyet & ayar
- [ ] **0. Eğitim Okuması beyan edildi mi?** (SKILL.md Bölüm 0 — kitle / hedef davranış / ton / süre /
  baskın mod tek cümlede). Beyan yoksa dur.
- [ ] **1. Dial değerleri brief'ten gerekçeli mi**, yoksa sessizce baseline mı kullanıldı? Dört dial
  (INTERACTIVITY / COGNITIVE_DENSITY / TONE / VISUAL_RICHNESS) için seçilen değer + tek satır neden.
- [ ] **2. Tek ölçülebilir hedef** (Bloom fiili) var mı ve **her ekran** ona hizmet ediyor mu? Hizmet
  etmeyen ekranı sil.

## Anti-slop sayımı (her madde = `references/anti-slop.md`'deki kural)
- [ ] **3. Ardışık `content_slide` ≤ 2 mi?** (A1 — zinciri mekanik say)
- [ ] **4. Hiçbir ekranda 5+ `<li>` yok mu?** (A2 — `<li>` say) **Jenerik başlık yok mu?** (A3)
- [ ] **5. Her ~2 içerik ekranında ≥ 1 etkileşim var mı?** (toplam etkileşim / içerik ekranı oranı)
- [ ] **6. Açılış relevans ile mi açıyor**, müfredat listesiyle değil mi? (B1)
- [ ] **7. Hiçbir `narration_text` ekran metnini birebir okumuyor mu?** (B2 — **her** anlatımlı ekranı
  tek tek karşılaştır)
- [ ] **8. Her quiz `feedback`'i iki yönlü + gerekçeli + remediation içeriyor mu**, ve şema
  varsayılanı (`"Doğru!"`/`"Tekrar deneyin."`) hiçbir yerde kalmadı mı? (B3) **Filler fiil/sıfat yok
  mu?** (B4) **Jenerik senaryo yok mu?** (B5)
- [ ] **9. Klişe stok görsel yok mu** (C1) · **tek-animasyon ardışık tekrarı ≤ 2 mi** (C2) · **keyfi
  koyu tema yok mu** (C3) · **ağır medya yalnız öğretiyorsa mı** (C4)?
- [ ] **9b. Patronlaştırıcı oyunlaştırma yok mu** (rozet/liderlik/"+10!"/konfeti — D1) · **puan yalnız
  skorlanan değerlendirmede mi** (D2) · **`decision_scenario` gerçek ikilem mi** (bariz-doğru/sahte-
  dallanma/sonuçsuz-feedback/tek-düğüm yok; kötü karar negatif `score_delta` — D3)?

## Mekanik & teslim
- [ ] **10. Sahne ritmi:** anlatımlı ekranlarda `narration_text` + uygun `reveal`; ekran başına
  **3–6 reveal bloğu**; quiz dışı içerik `stage` modunda akıyor. (`authoring-recommendations.md` §1–3)
- [ ] **11. Tema açık/nötr/kontrast**, görsellerde `alt` tam, dil sade, `scorm_version` doğru
  (branching/variables/games → **2004**)?
- [ ] **12. Değerlendirme hizalı:** sorular "uygula" düzeyinde (senaryo > tanım); `passing_score` ile
  `completion_rule` tutarlı?
- [ ] **13. Loop çalıştırıldı:** `preview` → gözden geçir/`list_feedback` → düzelt/`resolve_feedback` →
  `validate_package` yeşil → `build_package`?

---

**Sayım kuralı:** 3, 4, 5, 7, 9 maddeleri *sayı* ister — "sanırım iyi" yetmez. Bir ekranı bile
denetlemeden geçme. Liste uzun göründüyse kurs muhtemelen çok uzundur (mikroöğrenme: 3–8 dk) — böl,
sonra yeniden denetle.
