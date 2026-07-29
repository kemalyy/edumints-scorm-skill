# Paket ön-madde sözleşmesi (Katman 3 — `references/pedagogy/`)

12 yöntem paketinin (C1–C12) tak-çıkar olabilmesi tek sözleşmeye bağlıdır: **her paket dosyası
(`references/pedagogy/<pack>.md`) bu dizindeki `pack-frontmatter.schema.json` şemasını geçen bir
YAML ön-maddesiyle açılır.** Katman 0 seçici (`core/method-selector.md`) sert kısıtları bu
ön-maddeden okur; Katman 1 kanıt denetimi (`core/evidence-binding.md` K1/T1 + scorm-mcp #110)
`evidence_phase(s)` beyanını okur. Şemasız paket = seçilemez paket.

Bu dizindeki `_` önekli dosyalar paket DEĞİLDİR: `_SCHEMA.md` bu sözleşme, `_STUB-*.md` şema
doğrulamasının çalıştırılabilir örnekleridir.

## Alanlar (Türkçe açıklama)

| Alan | Zorunlu | Tür | Açıklama |
|---|---|---|---|
| `pack` | ✓ | string (kebab-case) | Paket kimliği; YÖNTEM BEYANI'nda ve `<pack>.md` dosya adında kullanılır. |
| `name` | ✓ | string | İnsan-okur Türkçe ad. |
| `version` | — | int ≥ 1 | Sözleşme sürümü (kırıcı değişiklikte artar). |
| `outcome_types` | ✓ | enum listesi | Uygun kazanım türleri: `olgu, kavram, prosedür, ilke, problem çözme, tutum, psikomotor`. **Seçicide sert kısıt.** |
| `prior_knowledge` | ✓ | `[min, max]` (1–10) | Uygun PRIOR_KNOWLEDGE aralığı. **Sert kısıt.** |
| `error_cost` | ✓ | enum listesi | Uygun hata-maliyeti düzeyleri: `düşük, orta, yüksek`. **Sert kısıt.** |
| `requires_platform` | ✓ | string listesi | Zorunlu platform yetenekleri (örn. `simulation`); boş = şart yok. **Sert kısıt.** |
| `phases` | ✓ | nesne listesi (≥ 2) | Fazlar — sıra dayatan yapı, paket olmanın tanımı (bkz. `overlays/_FRAMEWORK.md` ayracı). Her faz: `id`, `amac`, `izinli_ekran_tipleri` (liste ya da `hepsi`), `skorlanabilir` (bool), isteğe bağlı `sonraki` + `tekrar_kosulu`. |
| `evidence_phase` | ✓* | faz id (tekil) | **Kanıt ÜRETEN faz.** Katman 1 denetiminin okuduğu beyan. |
| `evidence_phases` | ✓* | faz id listesi (çoğul) | Birden çok faz kanıt üretiyorsa çoğul biçim. *`evidence_phase` VEYA `evidence_phases` — en az biri ZORUNLU.* |
| `scoring_allowed_from` | ✓ | faz id | Skorlu ekranın yerleşebileceği İLK faz — Z2'nin paket-düzeyi beyanı; öncesindeki fazlar `skorlanabilir: false`. |
| `conflicts_with` | ✓ | kimlik listesi | Aynı kursta birleştirilemeyen paket/kaplama kimlikleri (boş = bilinen çakışma yok); bildirim biçimi `overlays/_FRAMEWORK.md`. |

## Kanıt beyanı ÇOĞULDUR (1:1 dayatması yok)

- **Faz düzeyi:** `evidence_phase` (tekil) = kanıtı üreten faz; birden çok faz üretim yapıyorsa
  `evidence_phases: [..]`. Şema ikisinden birini zorunlu kılar, tekile zorlamaz.
- **Soru düzeyi:** bir skorlu soru **birden çok kanıt kaynağına** yaslanabilir. Spec'teki bağ
  alanı zaten çoğuldur: `evidence_screen_ids: list[str]` (scorm-mcp **CONTRACTS §1.3 E1** —
  sunucu tarafında yayında). Bu şema o sözleşmeyle terminoloji-uyumludur ve hiçbir yerde soru
  başına tek kanıt dayatmaz.
- **Katman 1 değişmezi:** faz beyanı Katman 3'ün işidir; Katman 1 kuralları (K/H/G/Z) fazlardan
  bağımsız, her pakette aynen geçerlidir.

## Doğrusal olmayan akış (döngü / koşul)

`phases` dizi sırası varsayılan akıştır; `sonraki: [faz_id, ...]` geçişleri override eder ve
**döngüye izin verir** (örn. tam-öğrenme: eşik-altı sonuçta öğretim fazına dönüş). Birden çok
hedef varsa `tekrar_kosulu` hangi koşulda hangisine gidileceğini tek cümleyle söyler. Simülasyon /
tam-öğrenme gibi döngüsel paketler bu iki alanla ifade edilir — şemaya sığmıyorsa şema hatalıdır,
paket değil (bkz. `_STUB-dongulu.md`).

## Doğrulama (komut belgelenmiş — CI'da da çalışır)

```bash
python3 -m pip install --quiet pyyaml jsonschema
python3 scripts/validate_packs.py          # repo kökünden
```

Betik `references/pedagogy/` altındaki `_SCHEMA.md` dışındaki tüm `.md` dosyalarının (paketler +
`_STUB-*` örnekleri) ön-maddesini şemaya karşı doğrular ve ek bütünlük denetimleri yapar:
`prior_knowledge` min ≤ max; `evidence_phase(s)`, `scoring_allowed_from` ve her `sonraki` hedefi
tanımlı faz id'lerine işaret eder; `scoring_allowed_from`'dan önceki fazlar `skorlanabilir: false`;
en az bir faz `skorlanabilir: true`. Çalışan iki örnek: `_STUB-dogrusal.md` (doğrusal akış),
`_STUB-dongulu.md` (döngülü akış).

## Kanoniklik yok

Hiçbir paket varsayılan-dayatmalı değildir; seçici önerir, yazar gerekçeyle seçer. "Uymayan durum"
varsayılanı (`gagne-9` + zorunlu gerekçe) yalnız Katman 0 elemesi boş küme döndürdüğünde geçerlidir
(`core/method-selector.md`).
