# SCORM курстарын түзүү — Claude Agent Skill

> ЖИ-кардарга **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)** сервери менен
> жогорку сапаттагы, интерактивдүү, SCORM-шайкеш онлайн окуу курстарын түзүүнү үйрөткөн
> **Claude Agent Skill**.

**🌐 Тилдер:** [English](README.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Azərbaycanca](README.az.md) · [Қазақша](README.kk.md) · [Кыргызча](README.ky.md)

Ачык булак, **[edumints.com](https://edumints.com)** платформасы тарабынан иштелип чыккан. Салымга ачык.

---

## Бул эмне

[Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) — ЖИ-кардар керек
болгондо жүктөгөн нускамалар папкасы. Бул skill моделге *«фишинг жөнүндө 6 мүнөттүк курс жаса»* сыяктуу
суроо-талапты сапаттуу SCORM пакетине айландыруу үчүн керектүү **окутуу-дизайн ой жүгүртүүсүн** жана
**так курал рецепттерин** берет: ачык максаттар, ар түрдүү экран түрлөрү, максатка ылайык баалоо, бренд
темалары, убакыт менен көрсөтүлгөн слайд-сахна ойноткучу, медиа жана куруу → алдын ала көрүү → кайтарым
байланыш цикли.

Skill — **автордун колдонмосу**; scorm-mcp сервери — **чогултуучу**.

## Түзүлүшү (этап менен ачылуу)

```
authoring-scorm-courses/
├── SKILL.md                         # кириш чекит: жумуш агымы + сапат ченеми
├── references/
│   ├── authoring-recommendations.md # качан/кантип/эмне үчүн чечим колдонмосу (алгач оку)
│   ├── mcp-cookbook.md              # так курал чакыруулары + толук build_from_spec түзүлүшү
│   ├── course-patterns.md           # текшерилген курс түзүлүштөрү
│   ├── instructional-design.md      # максаттар, микрооку, шаблон чарчоосуна каршы
│   ├── screen-types.md              # бардык экран түрлөрү үчүн чечим колдонмосу
│   ├── assessment.md                # суроо/кайтарым байланыш/баалоо дизайны
│   ├── interactivity-and-gamification.md
│   ├── media.md                     # MCP-аралык медиа + камтылган түрк TTS + жергиликтүү жардамчы
│   ├── video-generation.md          # программалык motion-graphic / маалымат видеосу
│   └── themes.md
├── templates/                       # көчүрүп-ылайыкташтыруучу үлгүлөр
└── examples/                        # толук, сапаттуу үлгү курс спецификациясы
```

## Талаптар

- ЖИ-кардарыңыз жете ала турган **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**
  сервери (өзүңүз хостинг кылыңыз же өз жайгаштырууңузга багыттаңыз).
- Agent Skills колдогон MCP кардары (мисалы, Claude).

## Орнотуу

**claude.ai (Skills):** `authoring-scorm-courses/` папкасын zip-теп, Settings → Capabilities →
Skills → Create skill бөлүмүнө жүктөңүз.
```bash
cd authoring-scorm-courses && zip -r ../authoring-scorm-courses.zip . && cd ..
```

**Claude Code / жергиликтүү:** `authoring-scorm-courses/` папкасын skills папкасына көчүрүңүз
(мисалы, `~/.claude/skills/authoring-scorm-courses/`).

Андан соң scorm-mcp серверин туташтырып, моделден курс түзүүнү сураңыз — ал ушул skill-ди ээрчийт.

## Лицензия

**MIT** — [LICENSE](LICENSE) караңыз. **edumints.com** тарабынан иштелип чыккан. Аталган продукт аттары
тиешелүү ээлеринин соода белгилери (бир гана номинативдик колдонуу).
