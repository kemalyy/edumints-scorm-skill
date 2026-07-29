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

## K4 — Gövde kendine-yeterliliği yasağı (kritik olgu kanıt ekranında yaşar)

Skorlanan sorunun **gövdesi** (`prompt_html` + seçenek/bölge metinleri), cevabın türetilmesi için
gereken **kursa-özgü kritik olguyu** (tarih-saat damgası, ölçüm değeri, tutar, ad, madde
numarası…) **İÇEREMEZ**. Kritik olgu yalnız o sorunun `evidence_screen_ids` ekranlarında yaşar;
gövde ona **ATIF yapar** ("zaman çizelgesindeki damgaya göre…"), **değerini kopyalamaz**.

Neden: gövdeye kopyalanan olgu + kamusal alan kuralı = kaynak gereksiz. İlk gerçek E4 koşusunda
coverage 1.0 + strict-temiz bir kurs tam bu mekanizmayla düştü (depo kökünde
`eval/results/2026-07-29-e4-kvkk-rosenshine.md`): kanıt ekranları sökülse bile soru kendi
gövdesinden çözülüyordu.

**İkili denetim (soru başına):**
1. Gövdedeki her kursa-özgü değeri işaretle (tarih-saat, sayı, tutar, özel ad…).
2. Sor: *"işaretli değer + kursu hiç görmemiş uzmanın alan bilgisi cevabı üretir mi?"*
   **Evet → ihlal.** Değeri gövdeden sil, kanıt ekranına taşı (yoksa üret; K1 türlerinden biri),
   gövdeyi atıfla yeniden kur.
3. Yeni-vaka (transfer) gövdesi de aynı denetimden geçer: gövdede tanıtılan vakanın olgusu +
   alan kuralı cevabı üretiyorsa soru kanıta bağlı DEĞİLDİR — vakayı gövdeye değil bir vaka
   artefaktı ekranına (K1 türü 4) koy ve o ekranı `evidence_screen_ids`'e ekle.

Kör testte karşılığı: gövdesindeki verili olguyla çözülen soru **[GÖVDE]** diye sınıflanır ve
**E sayılır** (`references/eval/blind-test.md` adım 4).

*Mekanik sayılabilirlik — lint adayı (E1 genişletmesi):* "skorlu soru gövdesi, kursa-özgü
somut değer deseni (tarih-saat / sayı-birim / damga dizgisi) içeriyor mu; içeriyorsa bu değer
kanıt ekranındaki kritik değerin kopyası mı?" — kemalyy/edumints-scorm-mcp E1 lint'ine
(`lint_course` / `evidence_binding_coverage`, #110) aday genişletme; bugün elle denetlenir.

#### ÖNCE / SONRA (E4 koşusundan, `q_sinir`)
```jsonc
// SLOP — vaka olgusu "salı 16:40" GÖVDEDE verili; 72-saat kuralı kamusal kanon
// → kanıt ekranları sökülse de soru çözülür (E4 kör testinde E çıktı)
{ "type":"mcq", "id":"q_sinir", "points":25,
  "evidence_screen_ids":["vaka_zaman_cizelgesi","model_sinir_hesabi"],
  "prompt_html":"<p>Bir sigorta acentesinde sızıntı: veriler pazartesi gecesi kopyalanmış; BT olayı <b>salı 16:40</b>'ta doğrulayıp iç kaydı damgayla açtı; kapsam raporu çarşamba öğlen çıktı. Kurul bildirim sınırı hangi anda dolar?</p>",
  "options":[ {"id":"a","text_html":"Cuma 16:40 — iç kayıt damgasından itibaren 72 saat","correct":true},
              {"id":"b","text_html":"Perşembe gecesi — verinin kopyalandığı andan itibaren 72 saat"},
              {"id":"c","text_html":"Pazartesi 16:40 — araya hafta sonu girerse süre sonraki iş gününe uzar"} ] }
```
```jsonc
// DÜZELTİLMİŞ — damga YALNIZ zaman çizelgesi ekranında yaşar (Perşembe 09:12); gövde atıf yapar,
// değeri kopyalamaz: cevap için çizelgeye dönmek ZORUNLUDUR. Seçenekler çıplak an verir ki
// kuralı bilen ama damgayı görmeyen okuyucu eleme yapamasın.
// (Çizelgedeki "sınır dolar" satırı da kaldırılır: okuyucu damgadan HESAPLAR, satırdan okumaz.)
{ "type":"mcq", "id":"q_sinir", "points":25,
  "evidence_screen_ids":["vaka_zaman_cizelgesi","model_sinir_hesabi"],
  "prompt_html":"<p>Vaka dosyasının zaman çizelgesine dön ve ihlal kayıt defterinin açılış damgasını bul. Bu vakada Kurul bildirim sınırı hangi anda dolar?</p>",
  "options":[ {"id":"a","text_html":"Pazar 09:12","correct":true},
              {"id":"b","text_html":"Cumartesi 22:47"},
              {"id":"c","text_html":"Pazartesi 09:12"} ],
  "feedback":{ "correct_html":"<p>Çizelgedeki damga + 72 saat. Başlangıç, öğrenme anını kanıtlayan iç kayıt damgasıdır; olay anı hesabın dışındadır ve hafta sonu sayacı durdurmaz.</p>",
               "incorrect_html":"<p>Sayaç olay anından işlemez ve takvim saatleri hafta sonunda durmaz. Zaman çizelgesindeki damgalı satıra geri dön ve 72 saati oradan say.</p>" } }
```

## K5 — Cevap sızıntısı yasağı (kanıt-dışı ekranlar cevabı yeniden söyleyemez)

Skorlanan bir sorunun cevabını, o sorunun `evidence_screen_ids`'i **DIŞINDAKİ hiçbir ekran**
açıkça ifade edemez — `summary` dahil. Özet, "ne öğrendik" çerçevesini **kavram düzeyinde**
kurabilir (hangi karar noktalarından geçildi), **cevap cümlesi kuramaz** (o kararların doğru
cevabını yeniden söyleyemez).

Neden: kör test protokolü yalnız kanıt ekranlarını söker (`references/eval/blind-test.md`
adım 2). Cevabı yeniden söyleyen kanıt-dışı ekran sökülmeden kalır ve fiilen **ikinci bir cevap
kanalı** olur. İlk gerçek E4 koşusunda kapanış özeti üç skorlu sorunun cevabını tek cümlede
taşıyordu — kurs bu kanaldan da düştü.

**İkili denetim (soru başına):**
1. Doğru cevabı tek önerme olarak yaz (ör. "sayaç iç kayıt damgasından işler").
2. `evidence_screen_ids` dışındaki TÜM ekran metinlerinde (body / prompt / feedback / narration /
   caption / seçenek metinleri) bu önermeyi açıkça kuran cümle ara.
3. **Bir eşleşme → ihlal.** İki çıkış var, sessiz geçiş YASAK: cümleyi kavram-düzeyi çerçeveye
   indir (cevabı söylemeden karar noktasını adlandır) **ya da** ekranı o sorunun
   `evidence_screen_ids`'ine ekle — o zaman kanıt olur ve kör testte sökülür.

*Mekanik sayılabilirlik — lint adayı (E1 genişletmesi):* "kanıt-dışı herhangi bir ekran metni,
doğru seçenek metnini / cevap önermesini içeriyor mu?" (dizgi ya da yüksek-örtüşme araması) —
kemalyy/edumints-scorm-mcp E1 lint'ine (`lint_course` / `evidence_binding_coverage`, #110) aday
genişletme; bugün elle denetlenir.

#### ÖNCE / SONRA (E4 koşusundan, `kapanis` özeti)
```jsonc
// SLOP — üç skorlu sorunun cevabı tek cümlede ("öğrenme anından say" = q_sinir,
// "yetişmeyeni gerekçele" = q_gecikme, "beklemeden ve onun dilinde" = q_dil).
// summary hiçbir sorunun kanıt ekranı değil → kör testte sökülmez, ikinci cevap kanalı kalır.
{ "type":"summary", "id":"kapanis", "title":"Artık sayacı sen yönetiyorsun",
  "body_html":"<p>Tek cümlelik çıkarım: damgayı vur, 72'yi öğrenme anından say, yetişmeyeni gerekçele; müşteriye ise beklemeden ve onun dilinde yaz.</p>",
  "narration_text":"Bir sonraki ihlalde ilk hareketin kayıt defterini açmak olacak — çünkü o damga, sonraki yetmiş iki saatin tek tartışılmaz tanığıdır." }
```
```jsonc
// DÜZELTİLMİŞ — kavram düzeyi çerçeve: HANGİ kararlardan geçildiğini adlandırır,
// kararların doğru cevabını kurmaz (narration dahil).
{ "type":"summary", "id":"kapanis", "title":"Artık sayacı sen yönetiyorsun",
  "body_html":"<p>Bu vakada dört karar noktasından geçtin: sayacı neyin başlattığı, Kurul ve ilgili-kişi kanallarının nasıl yönetildiği, kapsam netleşmeden süre dolarken izlenecek yol ve bildirim metninin kuruluşu. Bir sonraki ihlalde aynı dört karar yine senin.</p>",
  "narration_text":"Dört karar noktası artık senin: sayaç, kanallar, eksik bilgi, metin. Sıradaki vakada sıra sende." }
```

## K6 — Çapraz-madde kontaminasyonu yasağı (bir madde başka maddenin cevabını sızdıramaz)

Skorlanan bir sorunun **gövdesi/başlığı/şıkları**, **BAŞKA bir skorlu sorunun** cevabını türetmeye
yetecek kursa-özgü olguyu içeremez. K5'ten farkı sızıntı kanalıdır: orada kaynak kanıt-dışı bir
İÇERİK ekranıydı, burada kaynak başka bir SKORLU maddenin kendisi — iki soru birbirini çözer,
kanıt kaynağına hiç ihtiyaç kalmaz.

Neden: E4 2. koşusunda (`eval/results/2026-07-29-e4-grafik-dedektifi.md`, iterasyon B) bir oyun
düğümünün teşhis cevabı ayrı bir skorlu sorunun BAŞLIĞINDA açık yazıyordu — kanıt ekranı sökülse
bile o soru diğerinden okunuyordu.

**İkili denetim (madde çifti başına):**
1. Skorlanan her sorunun doğru cevabını tek önerme olarak yaz.
2. Diğer TÜM skorlanan soruların gövde/başlık/şık metinlerinde bu önermeyi (ya da onu türetmeye
   yetecek kursa-özgü olguyu) açıkça kuran ifade ara.
3. **Bir eşleşme → ihlal.** İki çıkış var, sessiz geçiş YASAK: sızdıran maddeyi, teşhisi/olguyu
   adlandırmadan kanıt ekranına geri yönlendirecek şekilde nötrleştir **ya da** iki maddeyi tek
   skorlu karara birleştir (ikisi zaten aynı olguyu ölçüyorsa).

Kör testte karşılığı: kanıt ekranları sökülse bile cevap **başka bir skorlu maddeden** okunuyorsa
dayanağa **[KOPYA]** yazılır ve **E** sayılır — çapraz-madde alt türü
(`references/eval/blind-test.md` adım 4).

*Mekanik sayılabilirlik — lint adayı (E1 genişletmesi):* "X maddesinin doğru cevap metni, Y
maddesinin gövde/başlık/şık metninde (dizgi ya da yüksek-örtüşme araması) geçiyor mu?" —
kemalyy/edumints-scorm-mcp E1 lint'ine (`lint_course` / `evidence_binding_coverage`, #110) aday
genişletme; bugün elle denetlenir.

#### ÖNCE / SONRA (E4 koşusundan, `q_eksen`)
```jsonc
// SLOP — q_eksen'in başlığı, dc_satis (satış slaydı) kanıt ekranındaki manipülasyon tekniğinin
// ADINI taşıyor; bu ad aynı zamanda n_satis oyun düğümünün teşhis sorusunun DOĞRU CEVABI.
// n_satis'in kanıt ekranı (dc_satis) sökülse de cevap q_eksen'den okunur ([KOPYA] — çapraz-madde).
{ "type":"mcq", "id":"q_eksen", "points":15,
  "evidence_screen_ids":["ec_eksen"],
  "title":"Sayıyı gövdesine geri koy",
  "prompt_html":"<p>Kesik y-eksenini sıfır tabanına oturtursan eğri nasıl değişir?</p>",
  "options":[ {"id":"a","text_html":"Fark abartılı görünmeye devam eder"},
              {"id":"b","text_html":"Fark gözle fark edilmeyecek kadar küçülür","correct":true} ] }
{ "type":"game", "id":"n_satis", "points":20,
  "evidence_screen_ids":["dc_satis"],
  "prompt_html":"<p>Satış slaydındaki grafik hangi manipülasyon tekniğini kullanıyor?</p>",
  "options":[ {"id":"a","text_html":"Kesik eksen — sıfır tabanı gösterilmeden çizilmiş"},
              {"id":"b","text_html":"Sayıyı gövdesine geri koy — sıfır tabanı gizlenmiş kesik eksen","correct":true} ] }
```
```jsonc
// DÜZELTİLMİŞ — q_eksen tekniğin adını değil kanıt ekranına dönüşü kurar; n_satis'in cevabı
// artık yalnız dc_satis'i inceleyerek türetilebilir.
{ "type":"mcq", "id":"q_eksen", "points":15,
  "evidence_screen_ids":["ec_eksen"],
  "title":"Ekseni düzelt, farkı yeniden oku",
  "prompt_html":"<p>Kesik-eksen ekranındaki grafiği sıfır tabanına oturttuğunda eğri nasıl değişir?</p>",
  "options":[ {"id":"a","text_html":"Fark abartılı görünmeye devam eder"},
              {"id":"b","text_html":"Fark gözle fark edilmeyecek kadar küçülür","correct":true} ],
  "feedback":{ "correct_html":"<p>Doğru — sıfır taban eğriyi düzleştirir; bir sonraki slaytta aynı düzeltmeyi kendin uygula.</p>",
               "incorrect_html":"<p>Kesik-eksen ekranına dön ve tabanı sıfıra çektiğinde eğrinin ne kadar düzleştiğine bak.</p>" } }
{ "type":"game", "id":"n_satis", "points":20,
  "evidence_screen_ids":["dc_satis"],
  "prompt_html":"<p>Satış slaydındaki grafik hangi manipülasyon tekniğini kullanıyor?</p>",
  "options":[ {"id":"a","text_html":"Kesik eksen — sıfır tabanı gösterilmeden çizilmiş","correct":true},
              {"id":"b","text_html":"Yanıltıcı renk kodlaması"} ] }
```

## Kanon-alan içerikleri — kanonu değil, kanonun artefakta uygulanmasını ölç

Alanın standart kuralları **kamusal kanonsa** (mevzuat, standartlar, ders kitabı yasaları),
kursu hiç görmemiş uzman okuyucu bu kuralları tanımı gereği bilir — K2 denetim sorusu bu tür
sorularda HER ZAMAN "evet" çıkar. Bu alanlarda skorlu soru kanonun KENDİSİNİ soramaz; kanonun
**kursun ürettiği artefakta uygulanmasını** ölçer: cevabın kritik parçası artefakttan (K1 türü 4)
gelir, kamusal kural yalnız işlem adımıdır. K4 ve K5 bu alanlarda en sert biter: kural zaten
uzmanın kafasındadır, geriye tek savunma **kritik olgunun yalnız kanıt ekranında yaşaması** kalır.

Dönüştürme kalıbı: **"kural nedir?" → "kanıt ekranındaki ŞU artefakta göre kural neyi gerektirir?"**

| Kural-hatırlama (SLOP) | Artefakta-uygulama (DÜZELTİLMİŞ) |
|---|---|
| (E4, `q_gecikme`) "Süre içinde tüm bilgiler netleşmemişse doğru hamle nedir?" — kademeli bildirim ilkesi kanondur, uzman kaynaksız cevaplar | "Kanıt ekranındaki adli-inceleme e-postasına göre (kapsam ancak 80. saatte netleşiyor) bildirim dosyasında hangi bölüm, hangi gerekçe cümlesiyle açık bırakılır?" — karar, e-posta artefaktının saat ve kapsam ayrıntısına bağlanır; e-posta yalnız kanıt ekranında yaşar |
| (E4, `q_dil`) "İlgili-kişi bildirimi hangi süre ölçütüyle ve hangi dille yapılır?" — "en kısa sürede + anlaşılır dil" kanondur | "Kanıt ekranındaki ilgili-kişi taslağının hangi cümlesi dil şartını ihlal ediyor? (hotspot)" — ihlalli cümle yalnız taslak artefaktında yaşar; okuyucu kuralı metne uygular |
| "Parola politikasına göre asgari uzunluk kaçtır?" — politika tablosu kamusal/standart içeriktir | "Denetim ekranında incelediğin üç hesap kaydından hangisi tablodaki politikayı ihlal ediyor?" — kayıtlar yalnız kanıt ekranında yaşar; okuyucu tabloyu kayıtlara uygular |

Bu bölüm rehberdir; zorlayıcı denetim K4 (gövde) ve K5 (sızıntı) ikili kurallarından gelir.
