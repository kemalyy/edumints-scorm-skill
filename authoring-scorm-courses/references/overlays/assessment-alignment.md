---
# Birincil kaynaklar (DOĞRULANDI, 2026-07-30 — quincycollege.edu "Anderson and Krathwohl
# Bloom's Taxonomy Revised" özeti + ResearchGate künyesi; SOLO: johnbiggsau.com +
# structural-learning.com): Anderson, L. W., & Krathwohl, D. R. (Eds.) (2001). A Taxonomy for
# Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.
# New York: Longman. — Altı düzey FİİL olarak doğrulandı: remember, understand, apply, analyze,
# evaluate, create (değerlendirme 5.'ye indi, yaratma tepeye çıktı). Biggs, J. B., & Collis,
# K. F. (1982). Evaluating the Quality of Learning: The SOLO Taxonomy. New York: Academic
# Press. — Beş düzey doğrulandı: prestructural, unistructural, multistructural, relational,
# extended abstract.
overlay: assessment-alignment
name: "Ölçme Hizası"
version: 1
decision_points: [olcme, ekran_secimi]
conflicts:
  - with: retrieval-spaced
    decision_point: olcme
    rule: "Tazeleme paketinde hatırlama-düzeyi geri getirme maddeleri paketin özüdür ve
           meşrudur; bu kaplamanın düzey-eşitliği itirazı yalnız hedef fiili uygulama ve üstü
           iken işler — hedef geri getirme/akıcılık ise paket beyanı önceliklidir."
---

# assessment-alignment — Ölçme Hizası (D5)

**Ne:** A2 çekirdek kuralı (H1–H3, `core/alignment.md`) hedef→soru eşlemesini zorunlu kılar; bu
kaplama o kuralın **pratiğe dökülmüş karar setidir**: hangi kazanım türü ve hangi biliş düzeyi,
hangi soru biçimiyle ölçülür. Amiral-gemisi bulgusunun panzehiri: hedefe ve içeriğe bağlı olmayan
soruların ödüllendirilmesi yalnız kanıt-bağ (K1–K6) sorunu değil, DÜZEY sorunudur da —
"tanımı hatırladı" verisi "uygulayabilir" iddiasını desteklemez. **Ne zaman:** skorlu ölçüm
içeren her kursta değerlendirilebilir; özellikle uyum/sınav kursları ve çok-hedefli kurslar.

## Kurucu kural — düzey eşitliği

> **Hatırlama düzeyinde soruyla uygulama hedefi ölçülemez.** Skorlu her sorunun biliş düzeyi,
> bağlandığı hedefin FİİLİNİN düzeyine eşit olmalıdır (Anderson & Krathwohl 2001 düzeyleri:
> hatırla → anla → uygula → çözümle → değerlendir → yarat).

- Hedef "uygular / değerlendirir / kurar" diyorsa skorlu soru yeni bir duruma uygulama ister —
  tanım, liste, terim geri getirme maddeleri o hedefe SKORLU olarak bağlanamaz.
- Alt-düzey maddeler yasak değildir: skorsuz (`points: 0`) ısınma/yoklama olarak meşrudur
  (Z1 formatif) — yasak olan, alt-düzey veriyle üst-düzey iddiayı PUANLAMAKTIR.
- Ters yön serbesttir ama beyan ister: hedef "hatırlar" ise uygulama sorusu fazla-ölçümdür;
  hedef fiili mi dar yazılmış, soru mu taşmış — H2 tablosunda görünür kılınıp düzeltilir.
- SOLO (Biggs & Collis 1982) cevap YAPISININ kalite cetvelidir: tek-yönlü (bir olgu) ↔
  çok-yönlü (olgular yan yana, ilişkisiz) ↔ ilişkisel (olgular tek kararda bütünleşir).
  Kullanımı: "uygula" hedefli bir soruda doğru seçenek İLİŞKİSEL olmalı (kararı gerekçesiyle
  kurar), çeldiriciler tipik tek-yönlü/çok-yönlü okumalar olmalı — çeldirici tasarımının cetveli.

## H2 tablosuna düzey sütunu (uygulama biçimi)

H2 eşleme tablosu bu kaplamayla bir sütun kazanır — boş hücre yine ihlaldir:

| Hedef (id + ölçülebilir fiil) | **Düzey (hedef fiili)** | Soru ekranı (id + tip) | **Düzey (soru)** | Kanıt kaynağı |
|---|---|---|---|---|
| O1 — rıza metnindeki kusuru *gösterir* | uygula/çözümle | `q_kusur` (hotspot) | uygula ✓ | artefakt |
| O2 — geçerlilik koşullarını *sayar* | hatırla | `q_kosul` (fill_blank) | hatırla ✓ | referans ekranı |

İki düzey sütunu eşit değilse satır kırmızıdır: soruyu yükselt (yeni-durum artefaktına uygula)
ya da hedef fiilini dürüstçe daralt — sessiz geçiş yasak.

## Soru sorabilen tipler × taşıyabildiği düzey (sunucu QUIZ_TYPES kümesi)

Karar tablosu — "bu hedef düzeyi için hangi tip": tip tek başına düzey GARANTİLEMEZ (mcq ile
hem tanım hem karar sorulur); tablo her tipin RAHAT taşıdığı bandı verir.

| Tip | Rahat taşıdığı düzey | Not |
|---|---|---|
| `mcq` | hatırla → değerlendir | Bant en geniş; üst düzey için gövde YENİ durum + gerekçeli seçenekler ister (en-iyi-gerekçe / karşı-örnek biçimi) |
| `true_false` | hatırla, anla | İkilem gerçekse `decision_scenario`'ya terfi ettir; üst düzeyi zorlamaz |
| `fill_blank` | hatırla | Tam terim geri getirme; uygulama hedefine skorlu bağlanamaz |
| `drag_drop` | anla, çözümle | Sınıflama/eşleme; klavye sınırı için `accessibility` kaplamasına bak |
| `matching` | anla, çözümle | Sınıflamanın erişilebilir biçimi |
| `sorting` | uygula | Prosedür sırası — "adımları doğru diz" uygulamanın kendisidir |
| `hotspot` | uygula, çözümle | Kuralı artefakt ÜZERİNDE gösterme ("kusuru işaretle") |
| `labeled_diagram` | hatırla, anla | Konum–terim bağı; uzamsal geri getirme |
| `simulation` | uygula | Adımlı icra; prosedür hedeflerinin birincil ölçüm tipi |
| `decision_scenario` | uygula, değerlendir | Sonuçlu karar + gerekçe; tutum/ilke hedeflerinin davranışsal ölçümü |
| `game` | uygula, değerlendir | Mekanik öğrenmeyi taşıyorsa (içsel bütünleşme) karar dizisi ölçer |
| `escape_room` | hatırla, uygula | Zincirli geri getirme + kural uygulama; düzeyi bulmaca tasarımı belirler |
| `term_match_race` | hatırla | Akıcılık/otomatiklik; YALNIZ akıcılık hedefinde skorlu meşru (süre sınırı için `accessibility` kaplamasına bak) |
| `adaptive_practice` | bankadaki maddelerin düzeyi | Motor düzey üretmez, kalibre eder — banka maddeleri tek tek bu tabloya tabidir |

## Kazanım türü → soru biçimi eşlemesi

| Kazanım türü | Doğru ölçüm biçimi | Skorlu olarak YANLIŞ biçim |
|---|---|---|
| olgu | geri getirme: `fill_blank`, `mcq` (tanıma) | uygulama tiyatrosu (olguyu senaryoya sarıp aynı tanımı sormak) |
| kavram | YENİ örneği sınıflama: `matching`/`drag_drop`, karşı-örnekli `mcq` | tanım metnini geri isteme (tanım ≠ sınıflandırabilme) |
| prosedür | sıra + icra: `sorting`, `simulation` | adım listesini `mcq` ile tanıtma (tanıma ≠ icra) |
| ilke | yeni duruma tahmin/sonuç: `mcq` ("ne olur?"), `decision_scenario` | ilkenin cümlesini ezber sorma |
| problem çözme | strateji + savunma: `decision_scenario`, `game`, vaka kararı | tek-doğrulu kısa cevap |
| tutum | davranış SEÇİMİ senaryoda: `decision_scenario` | "doğru tutum hangisi?" beyan sorusu (sosyal-istenirlik ölçer) |
| psikomotor | akıcı icra: `simulation`; akıcılık eşiği süreli varyantla (a11y şartlı) | yazılı bilgi sorusu (bilgi ≠ kas icrası) |

**Kanon-alan bağı:** kamusal-kanon içerikte (mevzuat, standart) dönüştürme kalıbı
("kural nedir?" → "kanıt ekranındaki ŞU artefakta göre kural neyi gerektirir?" —
`core/evidence-binding.md`) düzeyi de kendiliğinden yükseltir: kanon-hatırlama sorusu hatırla
düzeyindedir, artefakta-uygulama sorusu uygula düzeyine çıkar. İki kural aynı hamlede çözülür.

## Skor ağırlığı dağılımı (`olcme`)

- Ağırlık hedefe orantılı dağılır: bir hedefin toplam puan payı, kursun beyan ettiği önem
  sırasıyla uyumlu olmalı — tek hedefin puanların > %70'ini alması diğer hedefleri fiilen
  ölçümsüz bırakır (H1'e gölge ihlal).
- H3 eşiği aynen geçerli: skorlanan ekran > hedef + 1 ise gerekçe yazılır; bu kaplama eşiği
  değiştirmez, yalnız aşımın DÜZEY dağılımını da gerekçeye ekletir ("3 paralel soru: biri
  hatırla-düzey ısınma [skorsuz], ikisi uygula-düzey ölçüm").
- `tracking.passing_score` ile madde ağırlıkları tutarlı olmalı (anti-slop D2): kritik hedefin
  soruları geçilmeden eşik aşılamıyorsa tasarım doğrudur; tek ucuz soruyla eşik aşılıyorsa yanlış.

## Somut ekran kararları (parametre düzeyinde)

**1) Düzey terfisi — "uygular" hedefine bağlanan tanım sorusu düzeltilir:**

```jsonc
// ÖNCE (ihlal): hedef O1 "yangın söndürücü SINIFINI yeni duruma uygular" — soru tanım istiyor (hatırla)
{ "type": "fill_blank", "id": "q_sinif", "points": 30,
  "prompt_html": "<p>Elektrik yangınlarında kullanılan söndürücü sınıfı ___ sınıfıdır.</p>", "accepted": ["C"] }
```
```jsonc
// SONRA — aynı hedef, uygula düzeyi: YENİ vaka artefaktına sınıf kararı (kanıt bağı çoğul)
{ "type": "mcq", "id": "q_sinif", "points": 30,
  "evidence_screen_ids": ["siniflar_tablosu", "vaka_sunucu_odasi"],
  "prompt_html": "<p>Vaka ekranındaki sunucu odası tutuşmasında hangi söndürücüyü alırsın, hangi gerekçeyle?</p>",
  "options": [
    { "id": "a", "text_html": "C sınıfı — enerji kesilmeden iletken olmayan söndürücü şart", "correct": true },
    { "id": "b", "text_html": "A sınıfı — katı yangını gibi köpükle boğulur" } ] }
// doğru seçenek İLİŞKİSEL (karar + gerekçe — SOLO), çeldirici tek-yönlü okuma
```

**2) Süreli tipin düzey-dürüstlüğü — akıcılık hedefi yoksa süre yok:**

```jsonc
// hedef fiili "terimleri 60 sn içinde eşler" (akıcılık) İSE term_match_race skorlu meşrudur;
// hedef yalnız "terimleri tanır" ise süre baskısı ölçüme gürültü katar → matching seç:
{ "type": "matching", "id": "q_terim", "points": 20, "evidence_screen_ids": ["terim_kartlari"],
  "pairs": [ /* terim ↔ tanım */ ] }
```

**3) Ağırlık dağılımı — iki hedefli kursta puan payı:**

```jsonc
// O1 (uygula, birincil) 70 puan / O2 (hatırla, destekleyici) 30 puan; passing_score: 70
// → O1 soruları geçilmeden eşik aşılAMAZ; tek ucuz hatırlama sorusu kursu geçirtmez (D2 uyumu)
"tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 }
```

## Sınırlar (bu kaplama NE YAPMAZ)

- Yeni ölçme kuralı icat etmez: K1–K6, H1–H3, G1–G3, Z1–Z3 aynen kalır — kaplama Katman 1'in
  eşiklerini ekran-tipi ve düzey kararlarına ÇEVİRİR, genişletmez.
- Mekanik uygunluk denetleyicisinin (sunucu tarafı) kapsamına girmez: bu kaplama yazım-zamanı
  karar rehberidir; hedef-başına ihlal taraması sunucu araçlarının işidir, kaplama onları ikame
  etmez.
- Tazeleme bağlamında hatırlama maddelerine itiraz etmez (ön-madde bildirimi): düzey-eşitliği
  kuralı hedef fiiline bakar, tipe değil.

## Literatür

- **Birincil:** Anderson, L. W., & Krathwohl, D. R. (Eds.) (2001). *A Taxonomy for Learning,
  Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.* New York:
  Longman — altı düzey fiil biçiminde DOĞRULANDI (remember → create); özet: Krathwohl, D. R.
  (2002). *A Revision of Bloom's Taxonomy: An Overview.* Theory Into Practice, 41(4), 212–218.
- Cevap yapısı cetveli: Biggs, J. B., & Collis, K. F. (1982). *Evaluating the Quality of
  Learning: The SOLO Taxonomy.* New York: Academic Press — beş düzey DOĞRULANDI.
