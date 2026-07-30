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
│   ├── anti-slop.md                 # disciplina anti-slop: lectura de entrenamiento + diales paramétricos (leer PRIMERO)
│   ├── pre-flight.md                # matriz OBLIGATORIA de puertas de calidad previas a la construcción
│   ├── core/                        # Capa 1 — reglas núcleo independientes del método (+ el selector de Capa 0)
│   │   ├── method-selector.md       # Capa 0 — tipo de resultado + diales → pack(s) de método + overlay(s)
│   │   ├── evidence-binding.md      # cada pregunta puntuada se vincula a una fuente de evidencia del curso (K1–K6)
│   │   ├── alignment.md             # mapeo objetivo→pregunta→evidencia + umbral de aviso (H1–H3)
│   │   ├── feedback-anatomy.md      # 3 elementos de retroalimentación obligatorios — regla de piso (G1–G3)
│   │   └── scoring-timing.md        # formativo/sumativo + "sin puntuación antes de la evidencia" (Z1–Z3)
│   ├── eval/
│   │   └── blind-test.md            # protocolo de prueba ciega (umbral ≥ 1/2) — puerta para nuevos tipos de pantalla
│   ├── pedagogy/                    # Capa 3 — packs de método (serie C)
│   │   ├── _SCHEMA.md               # contrato de front-matter del pack (evidence_phase(s) OBLIGATORIO) + comando de validación
│   │   ├── _STUB-dogrusal.md        # ejemplo de validación de esquema: flujo lineal (no es un pack)
│   │   ├── _STUB-dongulu.md         # ejemplo de validación de esquema: flujo cíclico (no es un pack)
│   │   ├── rosenshine-di.md         # C1 — Instrucción Directa: modelo primero, práctica guiada→independiente
│   │   ├── merrill-fpi.md           # C2 — Primeros Principios de Merrill: activación→demostración→aplicación→integración centrada en la tarea
│   │   ├── 5e-inquiry.md            # C3 — ciclo de indagación 5E de BSCS: explorar primero (requiere el tipo de pantalla de exploración)
│   │   ├── 4cid.md                  # C4 — 4C/ID formación en habilidades complejas: tareas completas, simple→complejo, apoyo decreciente
│   │   ├── mastery-learning.md      # C5 — aprendizaje para el dominio de Bloom: unidad → umbral formativo → bucle de correctivos → sumativo
│   │   ├── productive-failure.md    # C6 — fracaso productivo de Kapur: lucha sin puntuar → consolidación (requiere exploración; piso PK 4)
│   │   ├── pbl-case.md              # C7 — aprendizaje basado en casos/problemas de Barrows: archivo de caso = familia de artefactos de evidencia (PK alto)
│   │   ├── kolb-experiential.md     # C8 — ciclo experiencial de Kolb: experiencia concreta → reflexión → conceptos → experimentación activa (actitudes)
│   │   ├── sim-drill.md             # C9 — ejercicio de simulación: ejecución modelo → modo-prueba sin puntuar → debriefing → bucle de tarea-parcial → escenario puntuado
│   │   ├── gagne-9.md               # C10 — los nueve eventos de Gagné (formación de cumplimiento/obligatoria; predeterminado de respaldo documentado)
│   │   ├── cognitive-apprenticeship.md  # C11 — Collins/Brown/Newman: modelo experto en voz alta → coaching → desvanecimiento → articulación → reflexión → exploración
│   │   └── retrieval-spaced.md      # C12 — práctica de recuperación + espaciado (solo-repaso; evidencia = el artefacto de referencia de re-exposición)
│   ├── overlays/                    # Capa 2 — overlays ortogonales al método (serie D)
│   │   ├── _FRAMEWORK.md            # formato de archivo de overlay + regla de independencia del pack + formato de conflicto
│   │   ├── cognitive-load.md        # D1 — gestión de carga cognitiva: segmentación/pre-entrenamiento/modalidad/coherencia/redundancia/señalización → decisiones de pantalla
│   │   ├── udl.md                   # D2 — DUA (CAST 3.0): múltiples representaciones de la MISMA fuente de evidencia; opciones de formato de respuesta; límites honestos de audio/subtítulos
│   │   ├── arcs.md                  # D3 — ARCS de Keller: atención/relevancia/confianza/satisfacción como decisiones ESTRUCTURALES (no de tono); sin gamificación decorativa
│   │   ├── expertise-adaptive.md    # D4 — reversión de la pericia de Kalyuga: PK → dosis de apoyo (desvanecimiento de worked_example), rutas expertas vía visible_if; "saltable = APOYO, nunca EVIDENCIA"
│   │   ├── assessment-alignment.md  # D5 — nivel Bloom-revisado/SOLO ↔ mapeo de tipo de pregunta; "una pregunta de recuerdo no puede medir un objetivo de aplicar"; distribución de peso de puntuación
│   │   └── accessibility.md         # D6 — decisiones WCAG 2.2 AA en tiempo de autoría sobre la declaración honesta de conformidad de la plataforma (calidad de texto alternativo, tipos seguros con teclado, temporizadores controlados por el aprendiz)
│   ├── migration-v1-to-v2.md        # guía de migración v1→v2: cambios disruptivos + recetas + mapeo Patrón A→rosenshine-di + el manual de 3-demos
│   ├── source-expansion.md          # expansión de fuente comprimida: línea de chuleta → pregunta de mecanismo → artefacto → pregunta vinculada (2 conversiones trabajadas)
│   ├── visual-storytelling.md       # hilo narrativo + presupuesto visual por pantalla + recetas de mockup-SVG
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
└── examples/                        # ejemplo insignia multi-pack (vinculado a evidencia, prueba ciega superada) + piloto v1 obsoleto
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
