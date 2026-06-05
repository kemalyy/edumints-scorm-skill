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
│   ├── authoring-recommendations.md # ne zaman/nasıl/neden karar rehberi (önce oku)
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
└── examples/                        # tam, kaliteli bir örnek kurs spec'i
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
