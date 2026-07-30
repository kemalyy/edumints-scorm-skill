---
# Birincil kaynak (DOĞRULANDI, 2026-07-30 — link.springer.com/article/10.1007/s10648-007-9054-3
# + Semantic Scholar künyesi): Kalyuga, S. (2007). "Expertise Reversal Effect and Its
# Implications for Learner-Tailored Instruction." Educational Psychology Review, 19(4),
# 509–539. — 26 çalışmanın taraması: aynı destek biçimi düşük ve yüksek önbilgide ZIT etki
# üretir. Etkinin adlandırıldığı kaynak: Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J.
# (2003). "The Expertise Reversal Effect." Educational Psychologist, 38(1), 23–31. — Acemiye
# yardım eden rehberlik (çözümlü örnek, adım kılavuzu) uzmanda gereksizlik etkisine dönüşür;
# uzman kendi şemasıyla çalışırken dışarıdan gelen destek işlemeyi ÇOĞALTIR.
overlay: expertise-adaptive
name: "Uzmanlığa Uyarlanır Tasarım (Kalyuga)"
version: 1
decision_points: [destek_dozu, gezinme, ekran_secimi]
conflicts:
  - with: gagne-9
    decision_point: gezinme
    rule: "Mevzuat/zorunlu-eğitim bağlamında paketin herkes-aynı-içerik beyanı önceliklidir:
           bu kaplama İÇERİK ATLATAMAZ, yalnız EK (isteğe bağlı) destek ekleyip çıkarabilir;
           atlama-yolu önerileri o bağlamda askıya alınır."
  - with: productive-failure
    decision_point: destek_dozu
    rule: "Deneme-önce paketin kasıtlı düşük-destekli deneme bölümünde bu kaplamanın
           soluklaştırma/destek-ekleme kararları askıya alınır (oradaki desteksizlik yöntem
           beyanıdır); paketin PRIOR_KNOWLEDGE bandı ön-madde sert kısıtından okunur — kaplama
           bandı genişletemez, kendi PK tahmini üretemez."
  - with: rosenshine-di
    decision_point: destek_dozu
    rule: "Model-önce pakette yüksek önbilgide gösterim dozu KISALTILABİLİR (soluklaştırılmış
           örnek, tamamlama biçimi) ama kanıt üreten gösterim ekranı KALDIRILAMAZ — atlanabilen
           destektir, kanıt değil; kanıt ekranının varlığı paket + Katman 1 beyanıdır."
---

# expertise-adaptive — Uzmanlığa Uyarlanır Tasarım (D4)

**Ne:** Uzmanlık-tersinme etkisi (Kalyuga vd. 2003): acemiye öğreten destek — tam çözümlü
örnek, adım kılavuzu, yoğun ipucu — yüksek önbilgide ETKİYİ TERSİNE çevirir: uzman kendi
şemasıyla çalışır, dışarıdan gelen rehberlik gereksiz işleme (yük) üretir ve öğrenmeyi düşürür.
Bu kaplama, `PRIOR_KNOWLEDGE` kadranını (SKILL.md yöntem kadranı — kaplamanın GİRDİSİ; kaplama
kendi PK tahmini üretmez) destek dozu, atlama yolları ve ekran-parametresi kararlarına çevirir.
**Ne zaman:** PK ≥ 7 profillerde (Katman 0 örnek eşlemesi: problem çözme + yüksek önbilgi bu
kaplamayı önerir) ya da kitle PK'sı heterojen olup tek kursta iki profil birden yaşıyorsa.

## KURUCU KURAL — atlanabilen şey DESTEKTİR, KANIT değildir

Bu kaplamanın en sert sınırı: **hiçbir kanıt ekranı atlama yoluna konamaz.** Skorlu herhangi
bir sorunun `evidence_screen_ids`'inde geçen ekran, `visible_if` ile gizlenemez ve atlama
dalıyla geçilemez — kanıt ekranı atlatılırsa o soruların kanıt bağı ÖĞRENENİN YOLUNDA kurulmaz
(K1/T1 boş kalır; Z2 "skor anında kanıt erişilmiş olmalı" ihlal edilir) ve kör test protokolü
fiilen kurs içinde yeniden sahnelenir. Mekanik denetim (kurs başına):

> `visible_if` taşıyan ya da atlama dalının pas geçtiği ekran id'leri × TÜM soruların
> `evidence_screen_ids` birleşimi → **kesişim boş olmalı; bir eşleşme = ihlal.**

Atlanabilirler yalnız DESTEK ekranlarıdır: ek örnek, hatırlatma, terim tazeleme, ipucu ekranı,
ısınma yoklaması. Uzman yolu kanıtı ATLAMAZ; kanıtla daha az iskeleyle karşılaşır.

## PK → doz tablosu (`destek_dozu`)

| PK | Çözümlü örnek | İpucu/iskele | Pratik biçimi |
|---|---|---|---|
| Düşük (1–3) | `fading: "full"` — adımlar VE gerekçeler açık | Yoğun: `simulation` her adımda ipucu; `game` `hints` dolu | Destekli deneme önce, skorlu ölçüm sonra |
| Orta (4–6) | `fading: "partial"` — adımlar açık, gerekçeyi öğrenen kurar (tamamlama biçimi) | Seçmeli: ipucu var ama istenince | Karışık: yarı-destekli + bağımsız |
| Yüksek (7–10) | `fading: "problem_only"` — problem-önce; adımlar ancak takılınca açılır | Asgari: ipucu yalnız hata sonrası | Problem-önce varyant; destek ekranları atlanabilir |

Doz tek yönlü değildir: kurs İÇİNDE performans sinyali (aşağıdaki tanılama deseni) düşükse
destek geri yükselir — tersinme etkisi statik etiket değil, güncel şema durumunun fonksiyonudur
(Kalyuga 2007'nin "learner-tailored" tezi).

## Taşıyıcılar (`ekran_secimi` + `gezinme`)

- **`worked_example` soluklaştırma dizisi — doğal taşıyıcı:** aynı içerik `fading` parametresiyle
  üç doza iner; paket hangi fazda çözümlü örnek istiyorsa kaplama yalnız `fading` değerini seçer
  (sıraya dokunmaz). Öz-açıklama istemi (`self_explanation_prompt_html`) yüksek PK'da özellikle
  değerlidir: destek azalırken üretken işleme korunur.
- **`visible_if` + değişkenler — uzman yolu:** skorsuz bir tanılama yoklaması `set_vars` ile
  profil değişkeni yazar; DESTEK ekranları `visible_if` ile yalnız ihtiyaç profiline görünür.
  Kanıt ekranlarında `visible_if` YOK (kurucu kural).
- **`adaptive_practice` `bkt` kipi — pratik dozunun motoru:** ustalık kestirimi (Bayesian
  Knowledge Tracing) eşiği aşınca erken durdurur — uzmana fazladan tur dayatmaz, acemiye
  eksik tur bırakmaz. Yayılmış `difficulty` + madde başına `explain_html` şarttır.
- **`branching` ile destek sapağı:** "çözümü adım adım görmek ister misin?" dalı — destek dalı
  ana hatta geri bağlanır; ana hattaki kanıt ekranları iki yolda da yaşar.

## Somut ekran kararları (parametre düzeyinde)

**1) Soluklaştırma dizisi — aynı çözümlü örnek, PK'ya göre tek parametre:**

```jsonc
// PK 2 (acemi): her şey açık
{ "type": "worked_example", "id": "cozum_tam", "fading": "full",
  "steps": [ { "action_html": "…", "rationale_html": "…" }, { "action_html": "…", "rationale_html": "…" } ] }
// PK 5: adımlar açık, gerekçe öğrenen kurar (per-adım açılır)
{ "type": "worked_example", "id": "cozum_yari", "fading": "partial",
  "self_explanation_prompt_html": "<p>2. adımın gerekçesini KENDİ cümlenle yaz, sonra aç ve karşılaştır.</p>", "steps": [ /* aynı adımlar */ ] }
// PK 8 (uzman): problem-önce — adımlar ancak takılınca tek tek açılır
{ "type": "worked_example", "id": "cozum_problem", "fading": "problem_only",
  "intro_html": "<p>Önce kendin kur; takıldığın adımı aç.</p>", "steps": [ /* aynı adımlar */ ] }
```

**2) Uzman yolu — tanılama + `visible_if` destek ekranı (kanıt ekranı KOŞULSUZ):**

```jsonc
// skorsuz tanılama: profil değişkenini yazar (Z1 — geçme notuna yazmaz)
{ "type": "mcq", "id": "tanilama", "title": "Isınma (puan yok): birimi çevir", "points": 0,
  "options": [ { "id": "a", "text_html": "Doğru cevap", "correct": true }, { "id": "b", "text_html": "Tipik hata" } ],
  "on_correct": [ { "var": "destek_gerek", "op": "set", "value": 0 } ],
  "on_wrong":   [ { "var": "destek_gerek", "op": "set", "value": 1 } ],
  "feedback": { "correct_html": "…", "incorrect_html": "…birazdan açılacak tazeleme ekranına bak…" } },
// DESTEK ekranı: yalnız ihtiyaç profiline görünür — atlanabilir, çünkü kanıt DEĞİL
{ "type": "content_slide", "id": "destek_tazeleme", "title": "Tazeleme: birim çevriminin iki adımı",
  "visible_if": "destek_gerek == 1", "body_html": "<p>…</p>" },
// KANIT ekranı: visible_if YOK — herkes görür; skorlu soru buna bağlanır
{ "type": "worked_example", "id": "kanit_cozum", "fading": "partial", "steps": [ /* … */ ] },
{ "type": "mcq", "id": "q_skorlu", "points": 30, "evidence_screen_ids": ["kanit_cozum"], /* … */ }
```

**3) Pratik dozu — `bkt` kipiyle erken durdurma:**

```jsonc
{ "type": "adaptive_practice", "id": "pratik", "mode": "bkt",
  "items": [ { "difficulty": -1.0, "explain_html": "…" }, { "difficulty": 0.0, "explain_html": "…" },
             { "difficulty": 0.8, "explain_html": "…" }, { "difficulty": 1.6, "explain_html": "…" } ] }
// ustalık eşiği aşılınca durur: uzman 3 maddede çıkar, acemi bankayı gezer — tersinmenin pratik cevabı
```

## Mevzuat istisnası (C10 bayraklı karar — ön-madde bildirimi)

Mevzuat/zorunlu eğitimde tam kapsama yasal yükümlülüktür: bu bağlamda kaplama **içerik
atlatamaz** — herkes aynı içeriği görür. Meşru kalan tek uyarlama, EK desteğin (isteğe bağlı
tazeleme, ek örnek) profile göre eklenip çıkarılması ve pratik dozunun ayarıdır; atlama-yolu
önerileri askıya alınır. Bildirim karar-noktası düzeyindedir (`gezinme`), hedef-düzeyi çakışma
değildir — kaplama aynı kursta diğer karar noktalarında çalışmaya devam eder.

## Sınırlar (bu kaplama NE YAPMAZ)

- Paket yapısını yeniden sıralamaz; yalnız doz, atlama ve parametre kararı verir.
- PK üretmez: `PRIOR_KNOWLEDGE` kadranını ve kurs-içi tanılama sinyalini OKUR; kadran
  bilinmiyorsa varsayılan (3, beyanlı) yöntem-seçici kuralıdır.
- Kanıt ekranı atlatmaz (kurucu kural); Katman 1'i (K/H/G/Z) gevşetmez.
- Deneme-önce paketlerin kasıtlı düşük-destek bölümüne destek enjekte etmez (ön-madde bildirimi).

## Literatür

- **Birincil:** Kalyuga, S. (2007). *Expertise Reversal Effect and Its Implications for
  Learner-Tailored Instruction.* Educational Psychology Review, 19(4), 509–539.
  https://doi.org/10.1007/s10648-007-9054-3 — 26 çalışmalık tarama; doz-uyarlama tezi DOĞRULANDI.
- Etkinin adlandırılması: Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). *The
  Expertise Reversal Effect.* Educational Psychologist, 38(1), 23–31.
- Acemi ucunun karşı-kutbu (rehbersizlik acemide çalışmaz): Kirschner, P. A., Sweller, J., &
  Clark, R. E. (2006). *Why Minimal Guidance During Instruction Does Not Work.* Educational
  Psychologist, 41(2), 75–86.
