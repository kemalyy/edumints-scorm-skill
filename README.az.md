# SCORM Kurslarının Yaradılması — bir Claude Agent Skill

> Bir süni intellekt müştərisinə **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**
> serveri ilə yüksək keyfiyyətli, interaktiv, SCORM-uyğun e-təhsil kursları yaratmağı öyrədən bir
> **Claude Agent Skill**.

**🌐 Dillər:** [English](README.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Azərbaycanca](README.az.md) · [Қазақша](README.kk.md) · [Кыргызча](README.ky.md)

Açıq mənbə, **[edumints.com](https://edumints.com)** platforması tərəfindən hazırlanıb. Töhfəyə açıqdır.

---

## Bu nədir

[Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) süni intellekt
müştərisinin ehtiyac olduqda yüklədiyi təlimatlar qovluğudur. Bu skill modelə *“fişinq haqqında
6 dəqiqəlik kurs hazırla”* kimi sorğunu cilalı SCORM paketinə çevirmək üçün lazım olan **təhsil-dizayn
mühakiməsini** və **dəqiq alət reseptlərini** verir: aydın məqsədlər, müxtəlif ekran növləri, uyğun
qiymətləndirmə, brend temalar, vaxtlı görünmə ilə slayd-səhnə pleyeri, media və qur → önizlə →
geribildirim dövrü.

Skill **müəllifin əl kitabıdır**; scorm-mcp serveri isə **yığıcıdır**.

## Struktur (mərhələli açılma)

```
authoring-scorm-courses/
├── SKILL.md                         # giriş: iş axını + keyfiyyət meyarı
├── references/
│   ├── anti-slop.md                 # anti-slop nizamı: təlim oxuması + parametrik nizamlayıcılar (İLK oxu)
│   ├── pre-flight.md                # MƏCBURİ qurmadan-öncə keyfiyyət-qapısı matrisi
│   ├── core/                        # Qat 1 — metoddan asılı olmayan nüvə qaydaları (+ Qat-0 seçici)
│   │   ├── method-selector.md       # Qat 0 — nəticə növü + nizamlayıcılar → metod paketi(ləri) + örtük(lər)
│   │   ├── evidence-binding.md      # hər ballı sual kurs-içi bir sübut mənbəyinə bağlanır (K1–K6)
│   │   ├── alignment.md             # məqsəd→sual→sübut uyğunlaşdırması + xəbərdarlıq həddi (H1–H3)
│   │   ├── feedback-anatomy.md      # 3 məcburi geribildirim elementi — minimum qayda (G1–G3)
│   │   └── scoring-timing.md        # formativ/summativ + "sübutdan öncə bal yoxdur" (Z1–Z3)
│   ├── eval/
│   │   └── blind-test.md            # kor-test protokolu (≥ 1/2 keçmə həddi) — yeni ekran növləri üçün qapı
│   ├── pedagogy/                    # Qat 3 — metod paketləri (C seriyası)
│   │   ├── _SCHEMA.md               # paket ön-məlumat müqaviləsi (evidence_phase(s) MƏCBURİ) + doğrulama əmri
│   │   ├── _STUB-dogrusal.md        # sxem-doğrulama nümunəsi: xətti axın (paket deyil)
│   │   ├── _STUB-dongulu.md         # sxem-doğrulama nümunəsi: dövri axın (paket deyil)
│   │   ├── rosenshine-di.md         # C1 — Birbaşa Təlim: əvvəl-model, bələdçili→müstəqil məşq
│   │   ├── merrill-fpi.md           # C2 — Merrill İlk Prinsiplər: tapşırıq-mərkəzli aktivləşdirmə→nümayiş→tətbiq→bütövləşmə
│   │   ├── 5e-inquiry.md            # C3 — BSCS 5E tədqiqat dövrü: əvvəl-kəşf (kəşf ekran növünü tələb edir)
│   │   ├── 4cid.md                  # C4 — 4C/ID mürəkkəb-bacarıq təlimi: bütöv tapşırıqlar, sadə→mürəkkəb, azalan dəstək
│   │   ├── mastery-learning.md      # C5 — Bloom tam mənimsəmə: vahid → formativ hədd → düzəliş dövrü → summativ
│   │   ├── productive-failure.md    # C6 — Kapur məhsuldar uğursuzluq: balsız mübarizə → möhkəmləndirmə (kəşf tələb olunur; PK həddi 4)
│   │   ├── pbl-case.md              # C7 — Barrows keys/problemə-əsaslanan təlim: keys faylı = sübut artefakt ailəsi (yüksək PK)
│   │   ├── kolb-experiential.md     # C8 — Kolb təcrübi dövrü: konkret təcrübə → düşüncə → anlayışlar → aktiv sınaq (münasibətlər)
│   │   ├── sim-drill.md             # C9 — simulyasiya məşqi: model işə salma → balsız sınaq-rejimi → təhlil → hissə-tapşırıq dövrü → ballı ssenari
│   │   ├── gagne-9.md               # C10 — Gagné-nin doqquz hadisəsi (uyğunluq/məcburi təlim; sənədləşdirilmiş ehtiyat susmaqla)
│   │   ├── cognitive-apprenticeship.md  # C11 — Collins/Brown/Newman: ekspert səsli-düşünmə modeli → məşqçilik → azaltma → ifadəetmə → düşünmə → kəşf
│   │   └── retrieval-spaced.md      # C12 — geri-çağırma məşqi + aralama (yalnız-təzələmə; sübut = yenidən-məruzqalma istinad artefaktı)
│   ├── overlays/                    # Qat 2 — metoda-ortoqonal örtüklər (D seriyası)
│   │   ├── _FRAMEWORK.md            # örtük fayl formatı + paket-müstəqilliyi qaydası + konflikt formatı
│   │   ├── cognitive-load.md        # D1 — koqnitiv-yük idarəsi: seqmentləşdirmə/ön-təlim/modallıq/uyğunluq/artıqlıq/işarələmə → ekran qərarları
│   │   ├── udl.md                   # D2 — UDL (CAST 3.0): EYNİ sübut mənbəyinin çoxlu təqdimatları; cavab-format seçimləri; dürüst səs/altyazı hədləri
│   │   ├── arcs.md                  # D3 — Keller ARCS: diqqət/uyğunluq/inam/məmnunluq STRUKTUR qərarlar kimi (ton deyil); dekorativ oyunlaşdırma yox
│   │   ├── expertise-adaptive.md    # D4 — Kalyuga ekspertlik tərsinməsi: PK → dəstək dozası (worked_example azaltma), visible_if ilə ekspert yolları; "keçiləbilən = DƏSTƏK, heç vaxt SÜBUT deyil"
│   │   ├── assessment-alignment.md  # D5 — Bloom-yenilənmiş/SOLO səviyyəsi ↔ sual-növü uyğunlaşdırması; "xatırlama sualı tətbiq məqsədini ölçə bilməz"; bal-çəki paylanması
│   │   └── accessibility.md         # D6 — WCAG 2.2 AA yazım-anı qərarları, platformanın dürüst uyğunluq bəyanatı üzərində (alt-mətn keyfiyyəti, klaviatura-təhlükəsiz növlər, öyrənən-idarəli taymerlər)
│   ├── migration-v1-to-v2.md        # v1→v2 keçid bələdçisi: sındıran dəyişikliklər + reseptlər + Naxış A→rosenshine-di uyğunlaşdırması + 3-demo bələdçisi
│   ├── source-expansion.md          # sıxılmış-mənbə açılması: kopya-vərəqi sətri → mexanizm sualı → artefakt → bağlı sual (2 işlənmiş çevrilmə)
│   ├── visual-storytelling.md       # nəql sapı + ekran-başına vizual büdcə + mockup-SVG reseptləri
│   ├── authoring-recommendations.md # nə vaxt/necə/niyə qərar bələdçisi
│   ├── mcp-cookbook.md              # dəqiq alət çağırışları + tam build_from_spec strukturu
│   ├── course-patterns.md           # sınanmış kurs strukturları
│   ├── instructional-design.md      # məqsədlər, mikrotəhsil, şablon yorğunluğuna qarşı
│   ├── screen-types.md              # bütün ekran növləri üçün qərar bələdçisi
│   ├── assessment.md                # sual/geribildirim/qiymətləndirmə dizaynı
│   ├── interactivity-and-gamification.md
│   ├── media.md                     # MCP-lərarası media + daxili Türk TTS + lokal köməkçi
│   ├── video-generation.md          # proqramatik motion-graphic / data videosu
│   └── themes.md
├── templates/                       # köçür-uyğunlaşdır şablonlar
└── examples/                        # flaqman çox-paketli nümunə (sübut-bağlı, kor-test keçib) + istifadədən çıxmış v1 pilotu
```

## Tələblər

- Süni intellekt müştərinin əlçatan olduğu **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**
  serveri (özün host et və ya öz quraşdırmana yönləndir).
- Agent Skills dəstəkləyən bir MCP müştərisi (məs., Claude).

## Quraşdırma

**claude.ai (Skills):** `authoring-scorm-courses/` qovluğunu zip-lə və Settings → Capabilities →
Skills → Create skill altında yüklə.
```bash
cd authoring-scorm-courses && zip -r ../authoring-scorm-courses.zip . && cd ..
```

**Claude Code / lokal:** `authoring-scorm-courses/` qovluğunu skills qovluğuna köçür
(məs. `~/.claude/skills/authoring-scorm-courses/`).

Sonra scorm-mcp serverini qoş və modeldən kurs qurmasını istə — o, bu skill-i izləyəcək.

## Lisenziya

**MIT** — bax [LICENSE](LICENSE). **edumints.com** tərəfindən hazırlanıb. Qeyd olunan məhsul adları
müvafiq sahiblərinin ticarət nişanlarıdır (yalnız nominativ istifadə).
