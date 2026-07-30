# Hedef–ölçme hizası (Katman 1)

Soru üretmek kolaydır; hizalamak kuraldır. 30 ekran tipinin 14'ü soru sorabilir (worked_example ve exploration yapısal olarak skorsuzdur — soru soramaz, kanıt taşır) — bu doküman
**hangi sorunun var olmaya hakkı olduğunu** belirler. Yöntemden bağımsızdır: hedefe giden yol
serbesttir, hedefsiz ölçme yasaktır.

## H1 — Her skorlanan soru beyan edilmiş bir hedefe eşlenir

Kursun ölçülebilir hedef(ler)i pre-flight Madde 2'de beyan edilir. **Hiçbir hedefe eşlenemeyen
skorlanan soru YASAK** — beyan edilmemiş bilgiyi ödüllendirmek hizasızlıktır (örn. hiçbir hedefe
ve hiçbir yazarlı içeriğe bağlı olmayan bir eşleştirme cevabı). Eşlenemeyen soru için
`core/evidence-binding.md` K3 prosedürü: bağla (hedefi beyan et + kanıtı kur) ya da at.

## H2 — Hedef→soru eşleme tablosu (zorunlu biçim)

Her skorlanan ekran bir satır. **Boş hücre = ihlal** (kanıt sütunu `evidence-binding.md` K1'den gelir):

| Hedef (id + ölçülebilir fiil) | Soru ekranı (id + tip) | Kanıt kaynağı (id + K1 türü) |
|---|---|---|

## H3 — Sayısal uyarı eşiği

**`skorlanan ekran sayısı > hedef sayısı + 1` → UYARI.** Bu eşik *warn* düzeyidir, fail değil:
summatif sınav kursları meşru olarak hedef başına çok soru içerebilir. Eşiği aşıyorsan pre-flight'a
tek cümle gerekçe yaz ("sınav kursu; hedef başına N paralel soru bilinçli"). Gerekçesiz aşım = ihlal.

### Tam eşleme örneği

Hedefler (2): **O1** "Şüpheli bir e-postayı işaretlerinden tanır" · **O2** "Şüpheli e-postayı doğru
kanaldan raporlar". Skorlanan ekran: 3 → eşik: 3 ≤ 2 + 1 → uyarı yok.

| Hedef (id + ölçülebilir fiil) | Soru ekranı (id + tip) | Kanıt kaynağı (id + K1 türü) |
|---|---|---|
| O1 — işaretlerinden tanır | `q_isaret` (mcq) | `vaka_eposta` (vaka artefaktı: süre-baskısı cümlesi işaretli) |
| O1 — işaretlerinden tanır | `q_eslestir` (matching) | `karsilastirma` (yan-yana gerçek/sahte e-posta karşılaştırması) |
| O2 — doğru kanaldan raporlar | `sim_rapor` (simulation) | `cozumlu_rapor` (çözümlü örnek: raporlama adımları gerekçeli gösterildi) |
