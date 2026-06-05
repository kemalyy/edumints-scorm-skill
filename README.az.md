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
│   ├── authoring-recommendations.md # nə vaxt/necə/niyə qərar bələdçisi (əvvəl oxu)
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
└── examples/                        # tam, keyfiyyətli nümunə kurs spesifikasiyası
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
