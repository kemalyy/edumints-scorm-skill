# Creación de cursos SCORM — una Claude Agent Skill

> Una **Claude Agent Skill** que enseña a un cliente de IA a crear cursos de e-learning interactivos,
> de alta calidad y compatibles con SCORM usando el servidor
> **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**.

**🌐 Idiomas:** [English](README.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Azərbaycanca](README.az.md) · [Қазақша](README.kk.md) · [Кыргызча](README.ky.md)

Código abierto, desarrollado por la plataforma **[edumints.com](https://edumints.com)**. Abierto a contribuciones.

---

## Qué es

Una [Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) es una carpeta
de instrucciones que un cliente de IA carga bajo demanda. Esta skill aporta al modelo el **criterio de
diseño instruccional** y las **recetas exactas de herramientas** para convertir una petición como
*"haz un curso de 6 minutos sobre phishing"* en un paquete SCORM pulido: objetivos claros, tipos de
pantalla variados, evaluación alineada, temas de marca, un reproductor de escenario con revelado
temporizado, multimedia y el ciclo construir → previsualizar → retroalimentación.

La skill es el **manual del autor**; el servidor scorm-mcp es el **ensamblador**.

## Estructura (divulgación progresiva)

```
authoring-scorm-courses/
├── SKILL.md                         # punto de entrada: flujo + criterio de calidad
├── references/
│   ├── authoring-recommendations.md # guía de decisiones cuándo/cómo/por qué (leer primero)
│   ├── mcp-cookbook.md              # llamadas exactas + forma completa de build_from_spec
│   ├── course-patterns.md           # estructuras de curso probadas
│   ├── instructional-design.md      # objetivos, microaprendizaje, anti-fatiga de plantillas
│   ├── screen-types.md              # guía de decisión para todos los tipos de pantalla
│   ├── assessment.md                # diseño de preguntas/retroalimentación/puntuación
│   ├── interactivity-and-gamification.md
│   ├── media.md                     # multimedia entre-MCP + TTS turco integrado + helper local
│   ├── video-generation.md          # vídeo programático de motion-graphics / datos
│   └── themes.md
├── templates/                       # plantillas para copiar y adaptar
└── examples/                        # una especificación de curso completa y de alta calidad
```

## Requisitos

- El servidor **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**, accesible para tu
  cliente de IA (auto-alójalo o apunta a tu propio despliegue).
- Un cliente MCP compatible con Agent Skills (p. ej., Claude).

## Instalación

**claude.ai (Skills):** comprime la carpeta `authoring-scorm-courses/` y súbela en
Settings → Capabilities → Skills → Create skill.
```bash
cd authoring-scorm-courses && zip -r ../authoring-scorm-courses.zip . && cd ..
```

**Claude Code / local:** copia la carpeta `authoring-scorm-courses/` en tu directorio de skills
(p. ej. `~/.claude/skills/authoring-scorm-courses/`).

Luego conecta el servidor scorm-mcp y pide al modelo que cree un curso — seguirá esta skill.

## Licencia

**MIT** — ver [LICENSE](LICENSE). Desarrollado por **edumints.com**. Los nombres de productos
mencionados son marcas de sus respectivos propietarios (uso nominativo únicamente).
