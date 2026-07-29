# E3 — Değerlendirme seti: kanıta bağlı skorlanan soru oranı (v1 ↔ v2)

> **Coverage tabandır; tek gerçek kapı E4 kör testidir. Metrik var olduğu anda optimize
> edilmeye başlanır — bu dosya coverage'ı hedef değil, ön koşul sayar.**
>
> %100 coverage amiral-gemisi başarısızlık modunu DIŞLAMAZ: gerçek bir artefakta yapılan ama
> soruyla İLGİSİZ bir bağ, her mekanik denetimi geçer. Bu yüzden aşağıdaki hiçbir tablo
> "coverage 1.0 → kurs iyi" diye okunamaz; coverage yalnız hijyen eşiğidir (0'sa kesin
> sorun vardır), karar verici sonuç **kör testtir**
> (`authoring-scorm-courses/references/eval/blind-test.md`).

Bu dizin bir **belge + fikstür setidir**, otomasyon değildir (skill-creator eval üslubu):
istemler elle verilir, üretilen spec gerçek sunucu lint'inden geçirilir, sonuç kayıt
şablonuyla raporlanır.

## Amaç

Denetim bulgusunu nicelleştirmek: v1 skill'in ürettiği kurslarda skorlanan sorular kurs-içi
kanıt kaynağına bağlanmıyor (ön-bilgi anketi üretiliyor); "kaynak-doküman madde sayısı ≈ ekran
sayısı" kokusu en çok **sıkıştırılmış referans-doküman girdilerinde** (kopya kâğıdı, mevzuat
özeti, politika tablosu) ortaya çıkıyor. Set bu girdi türünü özellikle içerir
(≥3 istem `girdi_turu: sıkıştırılmış-referans` etiketli).

## Nicel metrik (taban): kanıta bağlı skorlanan soru oranı

```
oran = geçerli evidence_screen_ids bağı olan skorlu ekran sayısı / toplam skorlu ekran sayısı
```

Mekanik ölçüm **sunucu lint'inden türetilir** — elle sayım yok: `lint_course` çıktısındaki
**`evidence_binding_coverage`** alanı (kemalyy/edumints-scorm-mcp, `core/antislop.py`
`evidence_binding_coverage()`, E1/#110). Tanım ayrıntıları:

- **Skorlu ekran** = `points > 0` YA DA `on_correct` ile puan değişkenine yazan quiz-tipi ekran (Z1).
- **Geçerli bağ** = `evidence_screen_ids` içinde en az bir id çözülüyor, kendisine işaret
  etmiyor ve hedef ekran kanıt-TAŞIYABİLİR (törensel bağ — sarkan id, kanıt-taşıyamaz hedef —
  SAYILMAZ; heuristik aday keşfi de sayılmaz, yalnız açık beyan).
- **Bilinen kör noktalar** (rapora not düşülür):
  1. **Vakum:** skorlu ekran yoksa oran 1.0 döner — hiç ölçüm yapmayan kurs (v1
     `concept-lesson.json` böyleydi) metrikte "temiz" görünür. Skorlu ekran sayısı 0 olan
     koşu tabloda `1.0 (vakum, n=0)` diye yazılır ve karşılaştırmada BAŞARI sayılmaz.
  2. **İlgisizlik:** bağ gerçek ama alakasız olabilir — mekanik denetim bunu göremez;
     karar kör testin işidir (üstteki kutu).
  3. **QUIZ_TYPES dışı puanlama:** `branching` düğümü `on_choose` ile puana yazabilir ama
     quiz tipi olmadığından metriğe girmez (v1 amiral örneğindeki `scenario` böyle).

Yardımcı ikincil sinyaller (aynı lint çıktısından): `error_count`, `warn_count`,
`unbound_scored_question` sayısı; sıkıştırılmış-referans istemlerinde ayrıca
`source_item_count` beyanı + `source_item_parity` uyarısı (madde-sayısı ≈ ekran-sayısı kokusu).

## Karşılaştırma prosedürü (v1 ↔ v2)

1. **v1 koşusu:** temiz bir LLM oturumuna v1 skill'i (v1 sürüm etiketi / release zip'i) yükle;
   `prompts/` altındaki her istemin "İstem" bölümünü AYNEN kullanıcı mesajı olarak ver.
   Üretilen `build_from_spec` spec'ini `runs/v1/<istem-id>.json` olarak kaydet.
2. **Lint:** her spec'i gerçek sunucudan geçir (in-memory: `Client(server.mcp)` →
   `build_from_spec` → `lint_course`; `SCORM_AUTH_ENABLED=0`, geçici `DATA_DIR`) ve
   `evidence_binding_coverage` + issue listesini kaydet.
3. **v2 koşusu:** AYNI istemler, temiz oturum, v2 skill — `runs/v2/<istem-id>.json`; aynı lint.
4. **Rapor:** `results/TEMPLATE.md` biçimini doldur (istem başına bir satır; iki koşu tek tabloda).
5. **Karar (E4):** coverage tabloları yalnız ön koşulu belgeler; nihai karşılaştırma her iki
   koşunun **kör test** sonuçlarıyla verilir (`blind-test.md` protokolü + ≥ 1/2 eşiği):
   v2'nin başarı iddiası "coverage yükseldi" değil, "kaynaklar çıkarılınca sorular
   cevaplanamaz hale geldi" cümlesidir.

Not — istem dosyalarındaki "Beklenen v2 sinyalleri" bölümleri isteme DAHİL EDİLMEZ (skorlama
notudur); istem olarak yalnız "İstem" bölümü verilir.

## Dizin

```
eval/
├── README.md                  # bu dosya: metrik tanımı + prosedür
├── prompts/                   # 10 test istemi (3'ü sıkıştırılmış-referans etiketli)
└── results/
    ├── TEMPLATE.md            # sonuç kayıt + karşılaştırma tablosu şablonu
    └── 2026-07-29-v1-baseline.md  # v1 taban çizgisi (artefakt-vekilli koşu, gerçek lint)
```

## İstem matrisi

| id | girdi türü | kazanım türü | PK | hata maliyeti |
|---|---|---|---|---|
| 01 | serbest-konu | prosedür | 2 | yüksek |
| 02 | serbest-konu | ilke/kavram | 5 | düşük |
| 03 | serbest-konu | problem çözme | 3 | orta |
| 04 | serbest-konu | prosedür (görev) | 4 | orta |
| 05 | **sıkıştırılmış-referans** (kopya kâğıdı) | olgu+prosedür | 2 | yüksek |
| 06 | **sıkıştırılmış-referans** (mevzuat özeti) | olgu+prosedür | 3 | yüksek |
| 07 | **sıkıştırılmış-referans** (politika tablosu) | olgu | 4 | orta |
| 08 | serbest-konu | tutum | 5 | düşük |
| 09 | serbest-konu | olgu (tazeleme) | 8 | orta |
| 10 | serbest-konu | prosedür+tutum (çoklu kazanım) | 3 | yüksek |
