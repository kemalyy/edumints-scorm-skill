# SCORM курстарын жасау — Claude Agent Skill

> ЖИ-клиентке **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)** серверімен
> жоғары сапалы, интерактивті, SCORM-үйлесімді электрондық оқыту курстарын жасауды үйрететін
> **Claude Agent Skill**.

**🌐 Тілдер:** [English](README.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Azərbaycanca](README.az.md) · [Қазақша](README.kk.md) · [Кыргызча](README.ky.md)

Ашық бастапқы код, **[edumints.com](https://edumints.com)** платформасы әзірлеген. Үлес қосуға ашық.

---

## Бұл не

[Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) — ЖИ-клиент қажет
болғанда жүктейтін нұсқаулар қалтасы. Бұл skill модельге *«фишинг туралы 6 минуттық курс жаса»* сияқты
сұранысты сапалы SCORM бумасына айналдыру үшін қажет **оқыту-дизайн пайымдауын** және **дәл құрал
рецепттерін** береді: айқын мақсаттар, әртүрлі экран түрлері, мақсатқа сай бағалау, бренд темалары,
уақытпен көрсетілетін слайд-сахна ойнатқышы, медиа және құрастыру → алдын ала қарау → кері байланыс циклі.

Skill — **автордың нұсқаулығы**; scorm-mcp сервері — **құрастырушы**.

## Құрылым (кезеңмен ашылу)

```
authoring-scorm-courses/
├── SKILL.md                         # кіру нүктесі: жұмыс ағыны + сапа межесі
├── references/
│   ├── authoring-recommendations.md # қашан/қалай/неге шешім нұсқаулығы (алдымен оқы)
│   ├── mcp-cookbook.md              # дәл құрал шақырулары + толық build_from_spec құрылымы
│   ├── course-patterns.md           # дәлелденген курс құрылымдары
│   ├── instructional-design.md      # мақсаттар, микрооқыту, шаблон шаршауына қарсы
│   ├── screen-types.md              # барлық экран түрлеріне арналған шешім нұсқаулығы
│   ├── assessment.md                # сұрақ/кері байланыс/бағалау дизайны
│   ├── interactivity-and-gamification.md
│   ├── media.md                     # MCP-аралық медиа + ендірілген түрік TTS + жергілікті көмекші
│   ├── video-generation.md          # бағдарламалық motion-graphic / деректер видеосы
│   └── themes.md
├── templates/                       # көшіріп-бейімдейтін үлгілер
└── examples/                        # толық, сапалы үлгі курс спецификациясы
```

## Талаптар

- ЖИ-клиентіңіз қол жеткізе алатын **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**
  сервері (өзіңіз хостинг жасаңыз немесе өз орналастыруыңызға бағыттаңыз).
- Agent Skills қолдайтын MCP клиенті (мысалы, Claude).

## Орнату

**claude.ai (Skills):** `authoring-scorm-courses/` қалтасын zip-теп, Settings → Capabilities →
Skills → Create skill бөлімінде жүктеңіз.
```bash
cd authoring-scorm-courses && zip -r ../authoring-scorm-courses.zip . && cd ..
```

**Claude Code / жергілікті:** `authoring-scorm-courses/` қалтасын skills қалтасына көшіріңіз
(мысалы, `~/.claude/skills/authoring-scorm-courses/`).

Содан кейін scorm-mcp серверін қосып, модельден курс құруды сұраңыз — ол осы skill-ді ұстанады.

## Лицензия

**MIT** — [LICENSE](LICENSE) қараңыз. **edumints.com** әзірлеген. Аталған өнім атаулары тиісті
иелерінің сауда белгілері (тек номинативті қолдану).
