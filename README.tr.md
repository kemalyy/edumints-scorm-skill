# SCORM Kursu Üretimi — bir Claude Agent Skill

> Bir yapay zekâ istemcisine **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**
> sunucusuyla kaliteli, etkileşimli, SCORM-uyumlu e-öğrenme kursları üretmeyi öğreten bir
> **Claude Agent Skill**.

**🌐 Diller:** [English](README.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Azərbaycanca](README.az.md) · [Қазақша](README.kk.md) · [Кыргызча](README.ky.md)

Açık kaynak; **[edumints.com](https://edumints.com)** platformu tarafından geliştirildi. Katkıya açık.

---

## Bu nedir

[Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills), bir yapay zekâ
istemcisinin ihtiyaç anında yüklediği bir talimatlar klasörüdür. Bu skill, modele *"phishing
hakkında 6 dakikalık bir kurs yap"* gibi bir isteği cilalı bir SCORM paketine çevirmek için gereken
**öğretim-tasarımı muhakemesini** ve **kesin araç reçetelerini** verir: net hedefler, çeşitli ekran
tipleri, hizalı değerlendirme, markaya uygun tema, zamanlanmış akışlı slayt-sahne oynatıcı, medya ve
inşa → önizleme → geri bildirim döngüsü.

Skill **yazarın el kitabı**; scorm-mcp sunucusu **derleyici**.

## Yapı (kademeli açılım)

```
authoring-scorm-courses/
├── SKILL.md                         # giriş: akış + kalite çıtası
├── references/
│   ├── anti-slop.md                 # anti-slop disiplini: eğitim okuması + parametrik ayarlar (İLK oku)
│   ├── pre-flight.md                # ZORUNLU inşa-öncesi kalite-kapısı matrisi
│   ├── core/                        # Katman 1 — yöntemden bağımsız çekirdek kurallar (+ Katman-0 seçici)
│   │   ├── method-selector.md       # Katman 0 — kazanım tipi + ayarlar → yöntem paketi(leri) + kaplama(lar)
│   │   ├── evidence-binding.md      # her puanlı soru kurs-içi bir kanıt kaynağına bağlanır (K1–K6)
│   │   ├── alignment.md             # hedef→soru→kanıt eşlemesi + uyarı eşiği (H1–H3)
│   │   ├── feedback-anatomy.md      # 3 zorunlu geri bildirim öğesi — taban kuralı (G1–G3)
│   │   └── scoring-timing.md        # biçimlendirici/düzey-belirleyici + "kanıttan önce puan yok" (Z1–Z3)
│   ├── eval/
│   │   └── blind-test.md            # kör-test protokolü (≥ 1/2 geçme eşiği) — yeni ekran tipleri için kapı
│   ├── pedagogy/                    # Katman 3 — yöntem paketleri (C serisi)
│   │   ├── _SCHEMA.md               # paket ön-veri sözleşmesi (evidence_phase(s) ZORUNLU) + doğrulama komutu
│   │   ├── _STUB-dogrusal.md        # şema-doğrulama örneği: doğrusal akış (paket değil)
│   │   ├── _STUB-dongulu.md         # şema-doğrulama örneği: döngülü akış (paket değil)
│   │   ├── rosenshine-di.md         # C1 — Doğrudan Öğretim: önce-model, rehberli→bağımsız alıştırma
│   │   ├── merrill-fpi.md           # C2 — Merrill İlk İlkeler: görev-merkezli etkinleştirme→gösterim→uygulama→bütünleşme
│   │   ├── 5e-inquiry.md            # C3 — BSCS 5E sorgulama döngüsü: önce-keşif (keşif ekran tipini gerektirir)
│   │   ├── 4cid.md                  # C4 — 4C/ID karmaşık-beceri eğitimi: bütün görevler, basit→karmaşık, azalan destek
│   │   ├── mastery-learning.md      # C5 — Bloom tam öğrenme: ünite → biçimlendirici eşik → düzeltme döngüsü → düzey-belirleyici
│   │   ├── productive-failure.md    # C6 — Kapur üretken başarısızlık: puansız mücadele → pekiştirme (keşif gerekir; PK tabanı 4)
│   │   ├── pbl-case.md              # C7 — Barrows vaka/probleme-dayalı öğrenme: vaka dosyası = kanıt yapıt ailesi (yüksek PK)
│   │   ├── kolb-experiential.md     # C8 — Kolb deneyimsel döngü: somut deneyim → yansıtma → kavramlar → etkin deneme (tutumlar)
│   │   ├── sim-drill.md             # C9 — simülasyon tatbikatı: model çalıştırma → puansız deneme-modu → çözümleme → parça-görev döngüsü → puanlı senaryo
│   │   ├── gagne-9.md               # C10 — Gagné'nin dokuz olayı (uyum/zorunlu eğitim; belgelenmiş yedek varsayılan)
│   │   ├── cognitive-apprenticeship.md  # C11 — Collins/Brown/Newman: uzman sesli-düşünme modeli → koçluk → azaltma → dile getirme → yansıtma → keşif
│   │   └── retrieval-spaced.md      # C12 — geri-getirme alıştırması + aralama (yalnız-tazeleme; kanıt = yeniden-maruz kalma referans yapıtı)
│   ├── overlays/                    # Katman 2 — yönteme-dik kaplamalar (D serisi)
│   │   ├── _FRAMEWORK.md            # kaplama dosya biçimi + paket-bağımsızlığı kuralı + çakışma biçimi
│   │   ├── cognitive-load.md        # D1 — bilişsel-yük yönetimi: bölümleme/ön-eğitim/kip/tutarlılık/fazlalık/işaretleme → ekran kararları
│   │   ├── udl.md                   # D2 — UDL (CAST 3.0): AYNI kanıt kaynağının çoklu sunumları; yanıt-biçimi seçenekleri; dürüst ses/altyazı sınırları
│   │   ├── arcs.md                  # D3 — Keller ARCS: dikkat/ilgi/güven/doyum YAPISAL kararlar olarak (üslup değil); dekoratif oyunlaştırma yok
│   │   ├── expertise-adaptive.md    # D4 — Kalyuga uzmanlık tersinmesi: PK → destek dozu (worked_example azaltma), visible_if ile uzman yolları; "atlanabilir = DESTEK, asla KANIT değil"
│   │   ├── assessment-alignment.md  # D5 — Bloom-güncel/SOLO düzeyi ↔ soru-tipi eşlemesi; "hatırlama sorusu uygulama hedefini ölçemez"; skor-ağırlık dağılımı
│   │   └── accessibility.md         # D6 — WCAG 2.2 AA yazım-anı kararları, platformun dürüst uyum bildirimi üzerine (alt-metin kalitesi, klavye-güvenli tipler, öğrenci-denetimli zamanlayıcılar)
│   ├── migration-v1-to-v2.md        # v1→v2 geçiş rehberi: kırıcı değişiklikler + reçeteler + Desen A→rosenshine-di eşlemesi + 3-demo el kitabı
│   ├── source-expansion.md          # sıkıştırılmış-kaynak açılımı: kopya-kağıdı satırı → mekanizma sorusu → yapıt → bağlı soru (2 işlenmiş dönüşüm)
│   ├── visual-storytelling.md       # anlatı ipliği + ekran-başına görsel bütçe + mockup-SVG reçeteleri
│   ├── authoring-recommendations.md # ne zaman/nasıl/neden karar rehberi
│   ├── mcp-cookbook.md              # kesin araç çağrıları + tam build_from_spec yapısı
│   ├── course-patterns.md           # kanıtlanmış kurs yapıları
│   ├── instructional-design.md      # hedefler, mikroöğrenme, anti-template-fatigue
│   ├── screen-types.md              # tüm ekran tipleri için karar rehberi
│   ├── assessment.md                # soru/geri bildirim/skor tasarımı
│   ├── interactivity-and-gamification.md
│   ├── media.md                     # çapraz-MCP medya + dahili Türkçe TTS + lokal yardımcı
│   ├── video-generation.md          # programatik motion-graphic / veri-viz video
│   └── themes.md
├── templates/                       # kopyala-uyarla iskeletler
└── examples/                        # amiral çok-paketli örnek (kanıt-bağlı, kör-test geçti) + kullanımdan kalkmış v1 pilotu
```

## Gereksinimler

- Yapay zekâ istemcinin erişebildiği **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**
  sunucusu (kendin host et ya da kendi dağıtımına yönlendir).
- Agent Skills destekleyen bir MCP istemcisi (ör. Claude).

## Kurulum

**claude.ai (Skills):** `authoring-scorm-courses/` klasörünü zip'le ve Settings → Capabilities →
Skills → Create skill altında yükle.
```bash
cd authoring-scorm-courses && zip -r ../authoring-scorm-courses.zip . && cd ..
```

**Claude Code / lokal:** `authoring-scorm-courses/` klasörünü skills dizinine kopyala
(ör. `~/.claude/skills/authoring-scorm-courses/`).

Sonra scorm-mcp sunucusunu bağla ve modelden bir kurs üretmesini iste — bu skill'i izleyecektir.

## Lisans

**MIT** — [LICENSE](LICENSE). **edumints.com** tarafından geliştirildi. Anılan ürün adları ilgili
sahiplerinin ticari markalarıdır (yalnız tanımlayıcı kullanım).
