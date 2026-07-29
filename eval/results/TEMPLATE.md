# E3 sonuç kaydı — <koşu adı>

> Hatırlatma: **coverage tabandır, hedef değil** — 1.0 yalnız ön koşulun sağlandığını söyler;
> karar verici sonuç kör testtir (`eval/README.md` üst kutusu).

- **Tarih:** <YYYY-AA-GG>
- **Skill sürümü:** <v1 etiketi | v2 dalı/commit>
- **Koşucu:** <insan + LLM oturumu tanımı; temiz oturum mu?>
- **Lint:** kemalyy/edumints-scorm-mcp <commit/sürüm>; in-memory `build_from_spec` →
  `lint_course` (`SCORM_AUTH_ENABLED=0`, geçici `DATA_DIR`)
- **Spec kayıtları:** `eval/runs/<koşu>/<istem-id>.json`

## İstem başına sonuçlar

| İstem | Skorlu ekran (n) | Coverage | error | warn | unbound_scored_question | source_item_parity* | Not |
|---|---|---|---|---|---|---|---|
| E3-01 | | | | | | — | |
| E3-02 | | | | | | — | |
| E3-03 | | | | | | — | |
| E3-04 | | | | | | — | |
| E3-05 | | | | | | | |
| E3-06 | | | | | | | |
| E3-07 | | | | | | | |
| E3-08 | | | | | | — | |
| E3-09 | | | | | | — | |
| E3-10 | | | | | | — | |

\* yalnız sıkıştırılmış-referans istemleri (E3-05/06/07); `source_item_count` beyan edilmediyse
"beyan yok" yaz (bu da bir bulgudur).

Vakum kuralı: skorlu ekran n=0 ise coverage sütununa `1.0 (vakum, n=0)` yaz — başarı sayılmaz.

## v1 ↔ v2 karşılaştırma tablosu

| İstem | v1 coverage | v2 coverage | v1 kör test (kaynak-gereksinim oranı) | v2 kör test | Karar (E4) |
|---|---|---|---|---|---|
| E3-01 | | | | | |
| … | | | | | |

- **Karar sütunu kör testten gelir** (≥ 1/2 eşiği, `references/eval/blind-test.md`):
  coverage farkı yalnız bağlam satırıdır.
- Kör test her koşunun ürettiği spec üzerinde ayrı koşulur (kanıt ekranları çıkarılır,
  temiz-bağlam okuyucu sorulara kaynaksız cevap vermeyi dener).

## Bulgular / kalan işler

- <coverage-kör test tutarsızlıkları özellikle not edilir: coverage 1.0 ama kör test KALDI →
  törensel/ilgisiz bağ şüphesi>
