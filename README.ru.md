# Создание SCORM-курсов — Claude Agent Skill

> **Claude Agent Skill**, обучающий ИИ-клиента создавать интерактивные, качественные и
> SCORM-совместимые курсы электронного обучения с сервером
> **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**.

**🌐 Языки:** [English](README.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Azərbaycanca](README.az.md) · [Қазақша](README.kk.md) · [Кыргызча](README.ky.md)

Открытый исходный код, разработан платформой **[edumints.com](https://edumints.com)**. Открыт для вклада.

---

## Что это

[Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) — это папка с
инструкциями, которую ИИ-клиент загружает по необходимости. Этот skill даёт модели **педагогическое
суждение** и **точные рецепты вызова инструментов**, чтобы превратить запрос вроде *«сделай 6-минутный
курс по фишингу»* в качественный SCORM-пакет: чёткие цели, разнообразные типы экранов, согласованное
оценивание, брендовое оформление, слайд-плеер с таймированным раскрытием, медиа и цикл
сборка → предпросмотр → обратная связь.

Skill — это **руководство автора**; сервер scorm-mcp — **сборщик**.

## Структура (постепенное раскрытие)

```
authoring-scorm-courses/
├── SKILL.md                         # точка входа: процесс + планка качества
├── references/
│   ├── authoring-recommendations.md # руководство решений когда/как/почему (читать первым)
│   ├── mcp-cookbook.md              # точные вызовы + полная форма build_from_spec
│   ├── course-patterns.md           # проверенные структуры курсов
│   ├── instructional-design.md      # цели, микрообучение, против шаблонной усталости
│   ├── screen-types.md              # руководство по выбору типов экранов
│   ├── assessment.md                # дизайн вопросов/обратной связи/оценивания
│   ├── interactivity-and-gamification.md
│   ├── media.md                     # межсерверное медиа + встроенный турецкий TTS + локальный хелпер
│   ├── video-generation.md          # программное видео motion-graphics / данных
│   └── themes.md
├── templates/                       # шаблоны «копируй и адаптируй»
└── examples/                        # полная, качественная спецификация курса
```

## Требования

- Сервер **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**, доступный вашему
  ИИ-клиенту (разместите сами или укажите своё развёртывание).
- MCP-клиент с поддержкой Agent Skills (например, Claude).

## Установка

**claude.ai (Skills):** заархивируйте папку `authoring-scorm-courses/` и загрузите её в
Settings → Capabilities → Skills → Create skill.
```bash
cd authoring-scorm-courses && zip -r ../authoring-scorm-courses.zip . && cd ..
```

**Claude Code / локально:** скопируйте папку `authoring-scorm-courses/` в каталог skills
(например, `~/.claude/skills/authoring-scorm-courses/`).

Затем подключите сервер scorm-mcp и попросите модель создать курс — она будет следовать этому skill.

## Лицензия

**MIT** — см. [LICENSE](LICENSE). Разработано **edumints.com**. Упомянутые названия продуктов являются
товарными знаками их владельцев (только номинативное использование).
