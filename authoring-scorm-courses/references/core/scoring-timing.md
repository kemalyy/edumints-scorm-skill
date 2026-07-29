# Formatif / summatif ayrımı ve skorlama zamanlaması (Katman 1)

Yöntemden bağımsız zamanlama ilkesi. **"Önce öğret sonra sor" DEĞİL** — kimi yöntemler kasıtlı
olarak denemeyle açılır ve bu meşrudur. Kısıt yalnız şudur: **skorlamadan önce kanıt üret.**

## Z1 — Tanımlar

- **Formatif (skorsuz, deneme-güvenli):** `points: 0` ya da puana yazmayan soru/etkileşim. Amaç
  yoklama ve düşünmeyi görünür kılma; tekrar serbest, ceza yok, `passing_score`'a etkisi yok.
- **Summatif (skorlu):** `points` > 0 ya da `on_correct`/`set_vars` ile puan değişkenine yazan her
  ekran. Ölçtüğü şeyden sorumludur: kanıt bağlama (`core/evidence-binding.md` K1) ve hedef hizası
  (`core/alignment.md` H1) summatif ekranlara uygulanır.

## Z2 — İlke: kanıt kaynağı üretilmeden skor yok

Bir soru **skor kaydettiği anda**, cevabının kanıt kaynağı (K1 türlerinden biri — yazarın koyduğu
bir ekran YA DA öğrenenin o ana dek kendi ürettiği çıktı) kursta **var olmuş olmalı**. Kanıttan önce
gelen skor, öğretimi değil ön bilgiyi (ya da şansı) puanlar. Mekanik denetim: her summatif ekran
için, kanıt-kaynağı ekranının öğrenenin o noktaya gelen yolunda erişilmiş olduğunu doğrula.

## Z3 — İstisna: skorsuz erken deneme serbest

Kasıtlı erken-deneme yöntemleri (öğrenen kanonik çözümü görmeden önce problemle boğuşur) Z2'yi
İHLAL ETMEZ — **şartı: erken denemeler skorSUZdur.** Erken deneme ekranı `points: 0` taşır, puana
yazmaz, deneme-güvenlidir; hatta başarısız deneme sonradan gelen kanonik çözümle birlikte kendisi
bir kanıt kaynağına dönüşür (K1 türü 5). Kanıt üretildikten sonra aynı becerinin **skorlu** sorusu
gelebilir. Yasak olan denemenin kendisi değil, **denemeyi puanlamaktır**.

#### ÖNCE / SONRA
```jsonc
// SLOP — henüz hiçbir kanıt üretilmeden ilk temas skorlu; yanlış = kalıcı puan kaybı
{ "type":"simulation", "title":"Raporlama adımlarını yap", "points":20,
  "steps":[ { "instruction_html":"<p><b>1.</b> Doğru butonu bul ve tıkla</p>", "regions":[…] } ] }
```
```jsonc
// DÜZELTİLMİŞ — aynı etkileşim formatif (deneme-güvenli); skor, kanıt var olduktan sonra
{ "type":"simulation", "title":"Dene: raporlamayı kendi başına çöz", "points":0,
  "prompt_html":"<p>Puan yok — dene, yanıl, gör. Denemenin kendisi birazdan göreceğin çözümün hammaddesi.</p>",
  "steps":[ { "instruction_html":"<p><b>1.</b> Doğru butonu bul ve tıkla</p>", "regions":[…] } ] }
{ "type":"content_slide", "id":"kanonik_cozum", "title":"Kanonik çözüm: adımlar ve nedenleri",
  "body_html":"<p>Az önceki denemenle karşılaştır: <b>Bildir</b> butonu e-postayı güvenlik kuyruğuna düşürür; silmek iz bırakmaz…</p>" }
{ "type":"mcq", "title":"Şimdi skorlu: ilk adım ne?", "points":20,
  "prompt_html":"<p>Yeni bir şüpheli e-posta geldi. İlk adımın ne?</p>",
  "options":[ {"id":"a","text_html":"Bildir butonuyla raporla","correct":true},
              {"id":"b","text_html":"Sil ve devam et"} ],
  "feedback":{ "correct_html":"Doğru — kanonik çözümde gördüğün gibi raporlama güvenlik ekibini uyarır; silmek uyarıyı yutar.",
               "incorrect_html":"Silmek tehdidi yalnız senin kutundan çıkarır. 'Kanonik çözüm' ekranındaki karşılaştırmaya geri dön." } }
```
