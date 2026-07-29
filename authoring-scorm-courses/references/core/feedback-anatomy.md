# Gerekçeli geri bildirim anatomisi (Katman 1 TABANI — anti-slop B3'ün yükseltilmiş hali)

Bu bir **taban** kuralıdır: neyin yasak olduğunu değil, her feedback'te neyin **var olmak zorunda**
olduğunu söyler. Cevaplı her ekran tipine uygulanır (`mcq`, `true_false`, `fill_blank`, `matching`,
`sorting`, `simulation`, `hotspot`, `decision_scenario.feedback_html`, …).

## G1 — Üç zorunlu öğe

Her `feedback` üç öğeyi de taşır; biri eksikse ihlal:

1. **Neden doğru:** `correct_html`, doğru cevabın **mekanizmasını** söyler — cevap neyi sağlıyor /
   neyi engelliyor / neden işliyor. Salt onay ("Doğru!", "Harika!") YASAK.
2. **Neden yanlış:** `incorrect_html`, öğrenenin muhtemel **yanılgısını adlandırır ve düzeltir** —
   "hangi akıl yürütme seni buraya getirdi ve nerede kırılıyor". Salt ret ("Tekrar dene.") YASAK.
3. **Kanıta geri işaret:** `incorrect_html`, cevabın türetildiği **kurs-içi kanıt kaynağına**
   (ekran başlığı ya da `id`) geri işaret eder — hangi ekrana dönüp neye bakacağını söyler.
   Kaynak yoksa geri işaret edilemez → sorunun kendisi ihlaldedir: önce
   `references/core/evidence-binding.md` K3 ("bağla ya da at") çalıştırılır.

## G2 — Gerekçe şablonlaşamaz

"Doğru, çünkü bu doğru cevap", "Yanlış, çünkü bu seçenek hatalı" gibi **jenerik gerekçe kalıbı yeni
bir slop türüdür** ve G1'i karşılamaz. Gerekçe, kanıt kaynağının **içeriğine** işaret eder: o ekranda
görülen somut olgu, adım, cümle ya da karşılaştırma. Test: gerekçe cümlesi başka bir kursa
kopyalandığında hâlâ "doğru" duruyorsa gerekçe değildir.

## G3 — Varsayılan / boş feedback = ihlal

`feedback` alanını boş bırakmak şema varsayılanını (`"Doğru!"` / `"Tekrar deneyin."`) devreye sokar;
**boş bırakmak da G1 ihlalidir.** Cevaplı ekranda feedback her zaman elle yazılır.

#### ÖNCE / SONRA
```jsonc
// SLOP — onay + ret; mekanizma yok, yanılgı yok, kanıta işaret yok
{ "type":"simulation", "title":"Raporla", "points":20,
  "feedback":{ "correct_html":"Harika, doğru yaptın!", "incorrect_html":"Tekrar dene." } }
```
```jsonc
// DÜZELTİLMİŞ — üç öğe de var
{ "type":"simulation", "title":"Şüpheli e-postayı raporla", "points":20,
  "feedback":{
    "correct_html":"Doğru — 'Bildir' butonu e-postayı güvenlik ekibinin kuyruğuna düşürür; silmek ya da yanıtlamak iz bırakmaz ve ekibi uyarmaz.",
    "incorrect_html":"Silmek tehdidi ortadan kaldırmaz, yalnız senin kutundan çıkarır — saldırı başkalarında sürer. 'Çözümlü örnek: raporlama adımları' ekranına dön ve 'Bildir' butonunun konumuna bak." } }
```
