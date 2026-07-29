---
# Birincil kaynak (DOĞRULANDI, 2026-07-29 — link.springer.com/article/10.1007/BF02505024):
# Merrill, M. D. (2002). "First Principles of Instruction." Educational Technology Research
# and Development, 50(3), 43–59. — Beş ilke: gerçek dünya problemi merkezde (problem-centered)
# + etkinleştirme (activation) + gösterim (demonstration) + uygulama (application) +
# bütünleştirme (integration).
pack: merrill-fpi
name: "Merrill İlk İlkeler (görev-merkezli)"
version: 1
outcome_types: [kavram, prosedür, ilke, problem çözme]
prior_knowledge: [2, 8]
error_cost: [düşük, orta, yüksek]
requires_platform: []
phases:
  - id: gorev_tanitimi
    amac: "Öğrenenin kurs sonunda yapabileceği GERÇEK dünya görevi bütün haliyle gösterilir — soyut hedef değil, somut görev."
    izinli_ekran_tipleri: [content_slide, video, image_compare, data_chart]
    skorlanabilir: false
  - id: etkinlestirme
    amac: "İlgili ön bilgi/deneyim skorsuz geri çağrılır ve yeni bilginin bağlanacağı yapı kurulur."
    izinli_ekran_tipleri: [poll, flashcards, mcq, true_false, accordion]
    skorlanabilir: false
  - id: gosterim
    amac: "Görevin çözümü gerekçeli çözümlü örnekle GÖSTERİLİR (anlatılmaz) — kursun kanıt kaynağı burada üretilir."
    izinli_ekran_tipleri: [content_slide, video, timeline, tabs, accordion, image_compare]
    skorlanabilir: false
  - id: uygulama_destekli
    amac: "Öğrenen görevi azalan destekle (ipucu/iskele) dener; denemeler skorSUZdur (Z3)."
    izinli_ekran_tipleri: [simulation, mcq, fill_blank, drag_drop, sorting, matching, hotspot, decision_scenario]
    skorlanabilir: false
  - id: uygulama_bagimsiz
    amac: "Destek çekilir; gösterim kanıtına bağlı skorlu görev icrası ölçülür."
    izinli_ekran_tipleri: hepsi
    skorlanabilir: true
  - id: butunlestirme
    amac: "Öğrenen yeni beceriyi KENDİ bağlamına taşır: yansıtma, kişisel uygulama planı, tartışma tohumu."
    izinli_ekran_tipleri: [poll, content_slide, branching]
    skorlanabilir: false
evidence_phase: gosterim
scoring_allowed_from: uygulama_bagimsiz
conflicts_with: []
---

# merrill-fpi — Merrill İlk İlkeler (C2)

**Ne:** Görev-merkezli şemsiye yöntem. Öğretim soyut konu başlıkları etrafında değil, öğrenenin
kurs sonunda yapabileceği **gerçek bir görev** etrafında örgütlenir: görev tanıtılır → ön bilgi
etkinleştirilir → çözüm GÖSTERİLİR → kademeli destekle uygulanır → kendi bağlamına taşınır.
**Ne zaman:** kazanım gerçek bir göreve bağlanabiliyorsa geniş-amaçlı güçlü adaydır (kavram /
prosedür / ilke / problem çözme; PK 2–8). Gösterim ilkesi, "0 yazarlı-gösterim" slop bulgusunun
yapısal cevabıdır: bu pakette gösterimsiz kurs ÜRETİLEMEZ.

**Kanıt beyanı (Katman 1 bağlantısı):** `evidence_phase: gosterim` (tekil). `etkinlestirme`
fazı bilinçli olarak kanıt fazı DEĞİLDİR: geri çağrılan şey öğrenenin kurstan ÖNCE bildiğidir ve
K2 denetimini geçemez ("kursu hiç görmemiş ama alanı bilen biri cevaplayabilir mi?" → evet).
Skorlu sorular `evidence_screen_ids` (ÇOĞUL — scorm-mcp CONTRACTS §1.3 E1) ile `gosterim`
fazının çözümlü-örnek ekran(lar)ına bağlanır.

## Faz rehberi

| Faz | Amaç | İzinli ekran tipleri | Skor? |
|---|---|---|---|
| `gorev_tanitimi` | Gerçek görevi bütün haliyle göster; "neden umursayayım"ı görevle cevapla | content_slide, video, image_compare, data_chart | ✗ |
| `etkinlestirme` | Ön bilgiyi skorsuz geri çağır; yapı kur | poll, flashcards, mcq, true_false, accordion | ✗ |
| `gosterim` | Görev çözümünü gerekçeli GÖSTER — **kanıt üretimi** | content_slide, video, timeline, tabs, accordion, image_compare | ✗ |
| `uygulama_destekli` | Azalan destekle deneme, `points: 0` (Z3) | simulation, mcq, fill_blank, drag_drop, sorting, matching, hotspot, decision_scenario | ✗ |
| `uygulama_bagimsiz` | Desteksiz, skorlu görev icrası | hepsi | ✓ |
| `butunlestirme` | Kendi bağlamına taşıma; yansıtma (skorsuz) | poll, content_slide, branching | ✗ |

Faz notları:

- **Görev tanımlanamıyorsa bu paket SEÇİLEMEZ** — "görev" gerçek dünyada teslim edilebilir bir
  çıktıdır ("e-postayı yaz", "raporu doğrula"), konu başlığı değildir ("e-posta iletişimi").
- `gosterim` ANLATIM değildir: madde listesi yerine görevin bir örneğinin adım adım, gerekçeli
  çözümü ("iyi örnek + neden iyi" / "kötü örnek + neden kötü" karşıtlığı güçlü bir biçimdir).
- `uygulama_destekli` → `uygulama_bagimsiz` geçişi Merrill'in kademeli-destek ilkesidir
  ("issue #17: uygulama ortası geç skorlama"): erken denemeler skorsuz, destek adım adım
  çekilir, skor yalnız desteksiz fazda.
- `butunlestirme` skorSUZdur: yansıtmayı puanlamak onu anket cevabına çevirir. Kısa kursta tek
  `poll` yeter; atlama, görev-merkezliliğin "kendi dünyasına taşı" ayağını koparır.
- Birden çok görev varyantı gerekiyorsa (basitten karmaşığa görev SINIFLARI + destek
  soluklaştırma), bu paketin büyüğü olan `4cid`'i düşün — akrabalık notu aşağıda.

## Bu paket NE ZAMAN seçilmemeli

- **Görevden koparılmış tekil olgular** (tarih/eşik/terim ezberi): görev iskeleti gereksiz
  ağırlıktır; `retrieval-spaced` (ya da olgu+prosedür karışımı uyum eğitiminde `gagne-9`) seç.
- **Görev tanımlanamıyorsa:** yukarıdaki kural — paket yapısal olarak kurulamaz.
- **Karmaşık, uzun-soluklu beceriler** (haftalar süren, çok alt-becerili): tek görev döngüsü
  yetmez; görev sınıfları + soluklaştırma isteyen `4cid` doğru araçtır (çakışma DEĞİL,
  ölçek farkı: merrill-fpi kısa-orta görevler, 4cid karmaşık-uzun — seçici notu).
- **Tutum / psikomotor kazanımlar:** `outcome_types` dışıdır (deneyim döngüsü için
  `kolb-experiential`, tatbikat için `sim-drill`).

## Çakışmalar (`conflicts_with`)

Boş — bilinen kurs-düzeyi çakışma yok. `4cid` ile ilişki çakışma değil ölçek seçimi (yukarıda);
keşif-önce paketlerle ilişki de çakışma sayılmadı çünkü gösterim-önce sıra bu paketin kendi
kazanımı içindeki sözleşmesidir, başka kazanımın paketine hüküm koymaz.

## build_from_spec örneği — tek kazanım, uçtan uca

Kazanım **O1** (tür: prosedür · PK: 4 · hata maliyeti: orta): *"Geliştiriciye yeniden-üretilebilir
bir hata (bug) raporu yazar."* Kitle: destek ekibi; görev gerçek ve teslim edilebilir.

```jsonc
{
  "title": "Yeniden Üretilebilir Hata Raporu Yazmak",
  "description": "Görev-merkezli mikrokurs — merrill-fpi",
  "scorm_version": "2004",
  "language": "tr",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 },
  "screens": [
    { "type": "title_slide", "title": "Hata Raporu Yazmak", "subtitle": "7 dk · gerçek görev: raporun geliştirici tarafından ilk okumada anlaşılması" },

    // ── FAZ gorev_tanitimi (gerçek görev, bütün haliyle) ──
    { "type": "content_slide", "id": "gorev", "title": "Görevin bu: bu rapor yüzünden düzeltme 3 gün gecikti",
      "body_html": "<p>Destek kuyruğundan gerçek bir kayıt: <i>\"Uygulama çalışmıyor, müşteri kızgın, acil!\"</i> — geliştirici neyi, nerede, nasıl deneyeceğini bilemedi; üç tur yazışma gitti. Kurs sonunda AYNI olayı ilk okumada anlaşılan bir rapora çevireceksin.</p>" },

    // ── FAZ etkinlestirme (ön bilgi, skorsuz — kanıt fazı DEĞİL) ──
    { "type": "poll", "id": "aktive", "title": "Sen nasıl yazıyorsun?",
      "prompt_html": "<p>Bugün bir hata bildirirken ilk hangi bilgiyi yazıyorsun?</p>", "multi": false,
      "options": [
        { "id": "a", "text_html": "Ne olduğunu (belirti)" },
        { "id": "b", "text_html": "Nasıl tekrar üretileceğini (adımlar)" },
        { "id": "c", "text_html": "Müşterinin ne kadar kızgın olduğunu" } ] },

    // ── FAZ gosterim (KANIT KAYNAĞI: kötü→iyi rapor, alan alan gerekçeli) ──
    { "type": "tabs", "id": "gosterim_rapor", "title": "Aynı olay, iki rapor: neden biri işe yarıyor?",
      "tabs": [
        { "label": "Kötü rapor", "body_html": "<p><i>\"Uygulama çalışmıyor, müşteri kızgın, acil!\"</i><br>Neden kötü: <b>belirti yok</b> (ne görüldü?), <b>adım yok</b> (nasıl üretilir?), <b>beklenen davranış yok</b> (doğrusu neydi?), <b>ortam yok</b> (hangi sürüm/cihaz?). Geliştirici tahmine mahkûm.</p>" },
        { "label": "İyi rapor — 4 alan", "body_html": "<p>1) <b>Belirti:</b> \"Ödeme ekranında 'Onayla'ya basınca boş sayfa.\" 2) <b>Adımlar:</b> \"Sepete ürün ekle → Ödeme → kartı gir → Onayla.\" 3) <b>Beklenen:</b> \"Onay sayfası açılmalıydı.\" 4) <b>Ortam:</b> \"v3.2.1, Android 14, Chrome.\" Her alan geliştiricinin BİR sorusunu kapatır — sıralama önem sırası değil, okuma sırasıdır.</p>" } ] },

    // ── FAZ uygulama_destekli (azalan destek, points: 0 — Z3) ──
    { "type": "drag_drop", "id": "destekli_alan", "title": "Destekli deneme: cümleleri alanlara yerleştir", "points": 0,
      "prompt_html": "<p>İpucu: 'Gösterim' sekmesindeki 4 alan sıralaması aynen geçerli. Puan yok.</p>",
      "items": [
        { "id": "i1", "text_html": "\"Kaydet düğmesi gri kalıyor\"", "correct_target_id": "t1" },
        { "id": "i2", "text_html": "\"Profil → Ad alanını boş bırak → Kaydet\"", "correct_target_id": "t2" },
        { "id": "i3", "text_html": "\"Düğme aktif olmalıydı\"", "correct_target_id": "t3" } ],
      "targets": [
        { "id": "t1", "label_html": "Belirti" }, { "id": "t2", "label_html": "Adımlar" }, { "id": "t3", "label_html": "Beklenen" } ] },

    // ── FAZ uygulama_bagimsiz (destek yok, SKORLU; kanıt bağı AÇIK) ──
    { "type": "mcq", "id": "q_rapor_bagimsiz", "title": "Skorlu: yeni olay, raporu sen kur", "points": 50,
      "evidence_screen_ids": ["gosterim_rapor"],      // E1 — kanıt: gosterim fazının karşılaştırmalı çözümlü örneği
      "prompt_html": "<p>Müşteri: \"Fatura PDF'i inmiyor.\" Aşağıdaki rapor taslaklarından hangisi 4 alanı da doğru kapatıyor?</p>",
      "options": [
        { "id": "a", "text_html": "\"PDF inmiyor, acil bakın\" — kısa ve net olduğu için" },
        { "id": "b", "text_html": "\"Belirti: Faturalar → İndir'de sayfa donuyor. Adımlar: Faturalar → Mart → İndir. Beklenen: PDF inmeli. Ortam: v3.2.1, Windows 11, Edge.\"", "correct": true },
        { "id": "c", "text_html": "\"Müşteri 3'üncü kez arıyor, öncelik verin; PDF sorunu galiba sunucudan\"" } ],
      "feedback": {
        "correct_html": "<p>Doğru — dört alan da dolu, okuma sırası gösterimdekiyle aynı: belirti → adımlar → beklenen → ortam.</p>",
        "incorrect_html": "<p>Aciliyet/his bir alan değildir. 'Aynı olay, iki rapor' ekranındaki 4-alan karşılaştırmasına geri dön: hangi alanlar boş kalmış?</p>" } },

    // ── FAZ butunlestirme (kendi bağlamına taşıma, skorsuz) ──
    { "type": "poll", "id": "entegre", "title": "Kendi kuyruğuna taşı",
      "prompt_html": "<p>Bu hafta yazacağın ilk gerçek raporda hangi alanı eklemeye en çok dikkat edeceksin — bugüne dek en sık hangisini atlıyordun?</p>", "multi": false,
      "options": [
        { "id": "a", "text_html": "Adımlar" }, { "id": "b", "text_html": "Beklenen davranış" }, { "id": "c", "text_html": "Ortam" } ] },

    { "type": "summary", "title": "Özet", "show_score": true, "show_completion": true }
  ]
}
```

Denetim izi: skorlu tek ekran (`q_rapor_bagimsiz`) → `evidence_screen_ids: ["gosterim_rapor"]`
→ `gosterim` fazı = `evidence_phase` beyanı. `aktive` ve `entegre` poll'ları skorsuz (Z1);
destekli deneme `points: 0` (Z3).

## Literatür

- **Birincil:** Merrill, M. D. (2002). *First Principles of Instruction.* Educational
  Technology Research and Development, 50(3), 43–59. https://doi.org/10.1007/BF02505024
- Sentez: Merrill, M. D. (2007). *First principles of instruction: a synthesis.* — beş ilkenin
  görev-merkezli döngü (task-centered instructional strategy) olarak işlenişi.
