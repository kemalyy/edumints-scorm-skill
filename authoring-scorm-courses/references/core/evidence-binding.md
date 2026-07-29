# Kanıt bağlama — skorlanan her soru kurs-içi kanıta bağlanır (Katman 1)

**Katman 1 = yöntemden bağımsız çekirdek.** Bu kural hiçbir öğretim yöntemine sıra dayatmaz:
kanıt kaynağının kurs akışında *nerede* durduğu yöntemin seçimidir; **var olması pazarlık dışıdır**.

## K1 — Kanıt kaynağı VAR olmalı

**Skorlanan her sorunun** (`points` > 0 ya da `on_correct`/`set_vars` ile puana yazan) cevabı,
**kursun KENDİSİNİN ürettiği** bir kanıt kaynağından türetilebilir olmalı. Geçerli kanıt-kaynağı
türleri (biçim serbest — varlık zorunlu):

1. **Çözümlü örnek** — adım adım gösterilmiş bir çözüm/işlem ve gerekçesi.
2. **Öğrenenin kendi keşfi** — bir etkileşimin (accordion / flashcards / image_compare /
   data_chart / hotspot…) öğrenene *bizzat gösterdiği* olgu ya da desen.
3. **Simülasyon / deneme çıktısı** — `simulation` / `game` etkileşiminin ürettiği gözlemlenebilir sonuç.
4. **Vaka dosyası / artefakt** — incelenen gerçekçi belge, ekran görüntüsü, e-posta, veri seti.
5. **Başarısız deneme + kanonik çözüm** — öğrenenin skorsuz denemesi ile ardından gösterilen
   doğru çözümün karşılaştırması.
6. **Veri görseli / karşılaştırma** — grafiğin ya da yan-yana karşılaştırmanın görünür kıldığı ilişki.

Dış medya (video vb.) kanıt sayılır **yalnız** içeriği spec'ten doğrulanabiliyorsa (caption /
transcript / anlatım metni cevabı gerçekten taşıyor). "Videoda anlatılıyordur" varsayımı kanıt değildir.

## K2 — Denetim sorusu (her skorlanan soruya birebir uygula)

> **"Bu kursu hiç görmemiş ama alanı bilen biri bu soruyu zaten cevaplayabilir mi?"**

**Evet** ise bu öğretim değil ankettir — soru yalnız ön bilgiyi yokluyor. **Bağla ya da at.**
Nesnel doğrulama: `references/eval/blind-test.md` (kör test protokolü).

## K3 — "Bağla ya da at" karar prosedürü

1. **Listele:** skorlanan ekranların tam listesini çıkar (`points` > 0 + puana yazanlar).
2. **Eşle:** her soru için cevabın türetildiği kanıt-kaynağı ekranının `id`'sini yaz
   (tablo biçimi: `references/core/alignment.md` H2).
3. **Denetle:** kaynağı boş kalan her soruya K2 denetim sorusunu uygula.
4. **Karar ver** — üçünden biri, sessiz geçiş YASAK:
   - **Bağla:** cevabı gerçekten üreten bir kanıt kaynağı ekle ya da mevcut ekranı cevabı taşıyacak
     şekilde güçlendir (K1 türlerinden biri).
   - **Skorsuz yap:** soru değerli ama kanıt eklenmeyecekse `points: 0` yap — yoklama olur, ölçme
     olmaz (bkz. `references/core/scoring-timing.md`).
   - **At:** soru hedefe de hizmet etmiyorsa sil.
5. **Beyan et:** eşleme tablosunu pre-flight'ta doldur; boş hücre kaldıysa kurs teslime hazır DEĞİL.

#### ÖNCE / SONRA
```jsonc
// SLOP — cevap ("aciliyet baskısı") kursun hiçbir ekranında üretilmiyor; alan bilgisi yoklanıyor
{ "type":"mcq", "title":"En güçlü işaret hangisi?", "points":20,
  "prompt_html":"<p>En güçlü phishing işareti hangisidir?</p>",
  "options":[ {"id":"a","text_html":"Tanıdık gönderen adı"},
              {"id":"b","text_html":"\"Acil! 2 saat içinde doğrula\" baskısı","correct":true} ] }
```
```jsonc
// DÜZELTİLMİŞ — önce artefakt cevabı ÜRETİYOR (kanıt türü 4), soru ona bağlanıyor
{ "type":"hotspot", "id":"vaka_eposta", "title":"Bu e-postada seni acele ettiren cümle hangisi?",
  "image_asset_id":"mail_sahte",
  "prompt_html":"<p>Gerçek vakadan alınmış e-postayı incele: saldırgan düşünmene fırsat vermemek için <b>süre baskısı</b> kuruyor.</p>",
  "regions":[ {"id":"r1","shape":"rect","coords":[120,300,520,60],"correct":true,
               "label":"\"2 saat içinde doğrulamazsan hesabın kapanır\"" } ] }
{ "type":"mcq", "title":"En güçlü işaret hangisi?", "points":20,
  "prompt_html":"<p>Yeni bir e-postada en güçlü phishing işareti hangisidir?</p>",
  "options":[ {"id":"a","text_html":"Tanıdık gönderen adı"},
              {"id":"b","text_html":"Süre baskısı kuran \"acil\" dili","correct":true} ],
  "feedback":{ "correct_html":"Doğru — vaka e-postasında gördüğün gibi süre baskısı, kurbanın doğrulama adımını atlaması için kurulur.",
               "incorrect_html":"Gönderen adı ve logo kolay taklit edilir. \"Bu e-postada seni acele ettiren cümle\" ekranındaki süre-baskısı cümlesine geri dön." } }
```
