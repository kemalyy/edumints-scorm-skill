# Sıkıştırılmış kaynak açma prosedürü — kopya kâğıdı satırından kanıta (G3)

**Sorun (başarısızlık-kökeni):** brief bir *sıkıştırılmış referans* olduğunda — kopya kâğıdı,
politika tablosu, mevzuat özeti, terim listesi — girdinin içinde kanıt kaynağı üretecek hammadde
**yoktur**. v1'in refleksi "madde sayısı ≈ ekran sayısı + tablo-ezber quiz'i"ydi (E1 lint'inin
`source_item_parity` kokusu tam bunu yakalar; kör testte bu kurslar düşer — alanı bilen herkes
"72 saat"i bilir). Ama yalnız yasak koymak yazarı çıkmaza sokar: kanıt bağlama (K1–K6) "kanıt
üret" der, sıkıştırılmış kaynak üretecek malzeme vermez. Bu belge açığı kapatan **pozitif
prosedürdür**: bir kaynak satırını kanıta nasıl açarsın.

**Çekirdek fikir:** sıkıştırılmış satır, bir zamanlar yaşanmış (ya da yaşanabilir) olayların
DAMITILMIŞ halidir. Açma = damıtmayı geri sarmak: satırın **dünyada bıraktığı izi** (vaka, kayıt,
ölçüm, sonuç) yeniden kurmak ve skorlu soruyu satıra değil o ize bağlamak.

## Prosedür (satır başına, numaralı)

1. **Satırı seç ve türünü adlandır:** eşik değeri mi (72 saat, 14 karakter), yasak mı ("ASLA
   su"), adım dizisi mi (PASS), terim mi, kural metni mi? Tür, hangi açma hamlesinin uyacağını
   belirler (aşağıdaki tablo).
2. **Mekanizma sorusunu sor:** *"Bu satır neden var? İhlal edilirse dünyada ne olur, kim neyi
   kaybeder?"* Cevap satırın kendisinde yoktur — kaynağın gerekçe bölümünde, alan bilgisinde ya
   da SME'de yaşar. **Kaynak-doğrulama uyarısı:** mekanizmayı kaynaktan/alandan doğrulayamıyorsan
   uydurma — `[DOĞRULANACAK]` işaretiyle yaz ve kullanıcı/SME onayına sun. Açma hamleleri
   halüsinasyon davet eder; **açılan her kanıt yazarın (ve gerekirse alan uzmanının) onayından
   geçer.** Vaka KURGUSU serbesttir (tarih, ad, saat uydurulabilir — kursa-özgü olgu zaten budur);
   MEKANİZMA uydurulamaz (suyun yanan tinere ne yaptığı kurgu değildir).
3. **Kazanım türünü belirle ve seçiciyi çalıştır:** satırın öğrenen davranışı karşılığı ne
   (olgu / kavram / prosedür / ilke)? `core/method-selector.md` girdileri buradan çıkar;
   sıkıştırılmış-kaynak briefleri çoğunlukla olgu+prosedür karışımıdır ve yüksek hata maliyeti
   taşır → gösterim-önce paketler öne gelir (E3-05/06 beklentisi).
4. **Artefakt kararını ver:** mekanizma cevabını hangi K1 kanıt türü GÖRÜNÜR kılar? Çözümlü
   örnek mi (hesap/işlem satırları), vaka zaman çizelgesi mi (timeline), veri görseli mi
   (data_chart), denetim kayıtları mı, simülasyon/karar senaryosu mu? Ölçüt: artefakt, satırın
   sonucunu ANLATMAZ — sonucun türetileceği ham olguyu taşır.
5. **Kanıt ekranını yaz — kritik olgu YALNIZ burada yaşar (K4):** artefaktın kursa-özgü
   değerleri (damga saati, ölçüm, alan büyüklüğü, kayıt satırı) başka hiçbir ekranda ve hiçbir
   soru gövdesinde tekrarlanmaz. Artefakt "cevap satırı" da içermez: okuyucu sonucu artefakttan
   HESAPLAR/ÇIKARIR, satırdan okumaz.
6. **Bağlı soruyu yaz — kanonu değil UYGULAMAYI ölç:** alanın kamusal kuralı (mevzuat eşiği,
   standart tablo) sorunun cevabı olamaz — kursu görmemiş uzman onu zaten bilir (K2 her zaman
   "evet" çıkar). Dönüştürme kalıbı (`core/evidence-binding.md` kanon-alan bölümü):
   **"kural nedir?" → "kanıt ekranındaki ŞU artefakta göre kural neyi gerektirir?"**
   Soru `evidence_screen_ids` ile (ÇOĞUL) artefakt + model ekranlarına bağlanır; şıklar çıplak
   an/değer/satır verir ki kuralı bilen ama artefaktı görmeyen okuyucu eleme yapamasın.
7. **Denetle ve beyan et:** K2/K4/K5/K6 ikili denetimleri + kör test (`eval/blind-test.md`);
   spec'e `source_item_count` beyanını yaz (E1 `source_item_parity` kokusuna karşı); madde↔ekran
   birebirliği kurma — maddeleri grupla, dar bütçede kapsamı bilinçli daralt (E3-07 dersi:
   8 maddeyi 5 dakikaya "kapsamak" slop sinyalidir; kalan maddeler için seri öner).

## Kazanım türü → açma hamlesi tablosu

| Satır türü (kazanım türü) | Açma hamlesi | Tipik artefakt/ekran | Bağlı soru ölçer |
|---|---|---|---|
| Eşik değeri / süre sınırı (olgu) | Eşiğin işlediği damgalı bir vaka kur; sınırı OKUTMA, HESAPLAT | `timeline` (damgalı kayıt) + çözümlü hesap modeli | Eşiğin vakaya uygulanması ("bu damgayla sınır ne zaman dolar?") |
| Yasak / "ASLA" satırı (ilke) | Yasağın ihlal edildiği anın kaydını kur; sonucu ölçülebilir yap | `timeline` / `data_chart` (ihlal → büyüyen sonuç) + mekanizma slaytı | İhlalin teşhisi ("kayıttaki hangi hamle sonucu büyüttü?") |
| Adım dizisi (prosedür) | Doğru icrayı gerekçe zinciriyle göster + BOZUK bir icra kaydı ekle | çözümlü örnek (`worked_example`/`content_slide` blokları) + bozuk-icra kaydı | Sıra ihlali teşhisi / adım-referans eşlemesi |
| Terim listesi (kavram) | Her terime kursa-özgü örnek + karşı-örnek türet; sınıflat | `flashcards`/`accordion` (tanım) + vaka örnekleri ekranı | Yeni örneğin sınıflanması ("bu vaka hangi terimin örneği?") |
| Tablo satırı / politika maddesi (olgu+ilke) | Maddeyi ihlal eden ve etmeyen KAYITLAR üret; denetlet | denetim-kayıtları artefaktı (content_slide/accordion) | Maddenin kayıtlara uygulanması ("hangi kayıt ihlal?") |
| Karar ağacı / akış (problem çözme) | Ağacın bir dalının gerçek geçişini senaryolaştır | `decision_scenario` / `simulation` | Yeni durumda dal seçimi + gerekçesi |

Hamle seçilirken K1 listesindeki altı kanıt-kaynağı türü menüdür; tablo en sık işleyen
eşleşmeleri verir, dayatmaz.

## Açma örneği 1 — mevzuat özeti satırı: "Kurula bildirim: en geç 72 saat" (E3-06, E4-kökeni)

İlk gerçek E4 koşusunun düştüğü satır tam buydu (`eval/results/2026-07-29-e4-kvkk-rosenshine.md`):
72-saat kuralı kamusal kanondur, "kaç saat?" sorusunu uzman kaynaksız cevaplar; gövdeye vaka
saati yazılırsa (K4 ihlali) kural+gövde yine kaynaksız çözer. Doğru açılış:

1-2. *Satır türü:* eşik değeri. *Mekanizma:* sayaç neden **öğrenme anından** işler? Çünkü
denetlenebilir tek an odur — olay anı çoğu ihlalde sonradan, tahminle bulunur; iç kayıt damgası
ise tartışılmaz tanıktır. (Mekanizma mevzuat gerekçesinden doğrulanabilir — `[DOĞRULANACAK]`
gerekmez.)
3. *Kazanım:* olgu+prosedür, hata maliyeti yüksek → gösterim-önce paket (koşuda `rosenshine-di`).
4. *Artefakt kararı:* damgalı vaka zaman çizelgesi + sayma işleminin çözümlü modeli.
5. *Kanıt ekranları:* `vaka_zaman_cizelgesi` (timeline — kopyalama anı, damga **Perşembe 09:12**,
kapsam raporu anı; "sınır dolar" satırı YOK: okuyucu hesaplar) + `model_sinir_hesabi` (çözümlü
örnek: BAŞKA bir mini vakada damgadan 72 sayma, hafta sonu durdurmaz gerekçesiyle).
6. *Bağlı soru* (kritik olgu gövdede DEĞİL, şıklar çıplak an — kuralı bilen ama damgayı
görmeyen eleme yapamaz):

```jsonc
{ "type": "mcq", "id": "q_sinir", "points": 25,
  "evidence_screen_ids": ["vaka_zaman_cizelgesi", "model_sinir_hesabi"],
  "prompt_html": "<p>Vaka dosyasının zaman çizelgesine dön ve ihlal kayıt defterinin açılış damgasını bul. Bu vakada Kurul bildirim sınırı hangi anda dolar?</p>",
  "options": [ { "id": "a", "text_html": "Pazar 09:12", "correct": true },
               { "id": "b", "text_html": "Cumartesi 22:47" },
               { "id": "c", "text_html": "Pazartesi 09:12" } ] }
```

7. *Denetim:* K2 → soru artık kanonu değil damganın uygulanmasını ölçüyor; K4 → damga yalnız
çizelgede; kör testte çizelge sökülünce soru düşer (revizyon sonrası E4 koşuları bunu doğruladı).
ÖNCE/SONRA'nın tam JSON'u: `core/evidence-binding.md` K4 bölümü.

## Açma örneği 2 — kopya-kâğıdı TABLOSU satırı: "B sınıfı · ASLA su (yayar!)" (E3-05)

Farklı kaynak biçimi: tablo satırı + tek kelimelik gerekçe. v1 refleksi: tabloyu slayta koy,
"B sınıfında hangi söndürücü kullanılmaz?" diye sor — uzman (ve tabloyu iki dakika görmüş herkes)
kaynaksız cevaplar; tablo-ezber ölçülür, davranış ölçülmez.

1-2. *Satır türü:* yasak (ilke). *Mekanizma:* su neden yayar? Yanan sıvı sudan hafiftir —
üstünde YÜZER; su alta iner, kızgın yüzeyde buharlaşıp sıçratır: alev alanı söner değil BÜYÜR.
(Yakıt-yoğunluğu mekanizması alan-standart bilgidir; vaka kurgusu serbest.)
4. *Artefakt kararı:* ihlalin ölçülebilir sonucunu taşıyan tatbikat kaydı (timeline) — alev
alanı sayıları kursa-özgü kritik olgu olur.
5. *Kanıt ekranları:* `mekanizma_yuzen` (content_slide: yüzen-yakıt mekanizması, katman-kesiti
çizimiyle) + `tatbikat_kaydi` (timeline: **13:02** tezgâhtaki tiner kabı devrildi ve tutuştu,
alan ~0,5 m² · **13:03** çalışan A su kovası boşalttı · **13:03:40** alan ~3 m², sıçrama
kayıtta · **13:05** çalışan B köpük tüpüyle müdahale etti · **13:06** söndü) + `alan_grafigi`
(data_chart: anlara karşı alev alanı m²). "Yanlış müdahale şuydu" satırı kayıtta YOK — teşhis
okuyucunun işi.
6. *Bağlı soru* — şıklar **çıplak saat**: tabloyu ezberleyen ama kaydı görmeyen eleme yapamaz.
(İlk taslakta şıklar mekanizma cümlesi taşıyordu — "su … sıçratır" fiziği bilen uzman, kaydı
görmeden tek doğru mekanizmayı seçebiliyordu; K2 denetimi bunu yakaladı ve mekanizma feedback'e
taşındı. Bu düzeltme, prosedürün 7. adımının niçin atlanamayacağının canlı örneğidir.)

```jsonc
{ "type": "mcq", "id": "q_yayilma", "points": 25,
  "evidence_screen_ids": ["mekanizma_yuzen", "tatbikat_kaydi", "alan_grafigi"],
  "prompt_html": "<p>Tatbikat kaydına ve alan grafiğine dön: alev alanını altı katına çıkaran müdahale hangi ANDAKİ müdahaleydi?</p>",
  "options": [ { "id": "a", "text_html": "13:03", "correct": true },
               { "id": "b", "text_html": "13:05" },
               { "id": "c", "text_html": "13:02" } ],
  "feedback": { "correct_html": "<p>Doğru — grafik o müdahaleden 40 saniye sonra altı-kat büyümeyi gösteriyor; mekanizma slaytı nedenini kurmuştu: su alta iner, buharlaşır, yüzen yanan sıvıyı sıçratır.</p>",
                "incorrect_html": "<p>Hangi müdahaleden SONRA alan büyüdü, hangisinden sonra sıfırlandı? Kaydı ve grafiği yan yana oku, sonra katman kesitine dön.</p>" } }
```

7. *Denetim + beyan:* `source_item_count: 6` (5 sınıf satırı + PASS); tablo 6 maddeyken kurs
6 slayt DEĞİL — B-sınıfı satırı derin açıldı, kalan sınıflar tek gruplanmış özet ekranında
toplandı (E3-05 beklenen sinyali; ilk taslak 6 ekran = 6 madde çıkınca E1 `source_item_parity`
uyarısı verdi, gruplama ekranı + skorsuz transferle giderildi). Bu örneğin uçtan uca
çalıştırılmış hali (mini spec + gerçek sunucu lint çıktısı):
`eval/results/2026-07-30-e3-05-kaynak-acma.md`.

## `retrieval-spaced` — meşru istisnanın sınırı

Sıkıştırılmış kaynağın **açılmadan** kullanılabildiği tek meşru yer, `pedagogy/retrieval-spaced`
paketinin `referans_artefakt` fazıdır: tek-sayfalık özet tablo orada zaten damıtılmış YENİDEN-SUNUM
malzemesidir ve kurstaki tüm skorlu sorular ona bağlanır. Sınır çift taraflıdır:

- **Ön şart:** içerik daha önce öğretilmiş olmalı (PK 7–10) ve önceki eğitim kurs briefine
  yazılmalı — yazılamıyorsa paket seçilemez, satırlar bu prosedürle AÇILIR.
- **İstisna daralması:** istisna yalnız yeniden-sunumu kapsar; retrieval-spaced kursunda bile
  K4 aynen geçerlidir — kritik olgu yalnız artefakt ekranında yaşar, sorular ona atıfla kurulur.
  "Nasılsa önceki kurs öğretti" diye artefaktsız soru sormak paketin belgelenmiş kötüye
  kullanımıdır (paketin dürüstlük notu).

## Sık düşülen üç tuzak

1. **Artefakta cevabı yazmak:** zaman çizelgesine "sınır Pazar 09:12'de dolar" satırı koymak
   hesaplatmayı okumaya çevirir — artefakt ham olgu taşır, sonucu taşımaz (adım 5).
2. **Gövdeye olgu kopyalamak:** vaka saatini soru gövdesine yazmak K4'ü ihlal eder ve kör testte
   [GÖVDE] düşürür — gövde atıf yapar ("kayıttaki damgayı bul"), değer vermez.
3. **Her maddeyi açmaya çalışmak:** açma pahalıdır (ekran + denetim). Dar bütçede 1–2 maddeyi
   derin aç, kalanını grupla ya da seriye ertele — "hepsini kapsadım" iddiası slop sinyalidir.
