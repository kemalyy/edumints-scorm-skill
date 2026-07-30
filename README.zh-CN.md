# 创作 SCORM 课程 —— 一个 Claude Agent Skill

> 一个 **Claude Agent Skill**，教 AI 客户端用
> **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)** 服务器创作高质量、交互式、
> 符合 SCORM 标准的在线课程。

**🌐 语言：** [English](README.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Azərbaycanca](README.az.md) · [Қазақша](README.kk.md) · [Кыргызча](README.ky.md)

开源，由 **[edumints.com](https://edumints.com)** 平台开发。欢迎贡献。

---

## 这是什么

[Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) 是一个按需加载的
指令文件夹。本技能赋予模型**教学设计判断力**与**精确的工具调用配方**，把诸如*“做一个 6 分钟的钓鱼
邮件课程”*的请求变成精良的 SCORM 包：清晰的目标、多样的屏幕类型、对齐的测评、品牌主题、带定时显示的
幻灯片舞台播放器、媒体，以及“构建 → 预览 → 反馈”的循环。

技能是**作者手册**；scorm-mcp 服务器是**组装器**。

## 结构（渐进式披露）

```
authoring-scorm-courses/
├── SKILL.md                         # 入口：工作流 + 质量标准
├── references/
│   ├── anti-slop.md                 # anti-slop 纪律：训练阅读 + 参数化旋钮（先读）
│   ├── pre-flight.md                # 强制的构建前质量门矩阵
│   ├── core/                        # 第 1 层 —— 与方法无关的核心规则（+ 第 0 层选择器）
│   │   ├── method-selector.md       # 第 0 层 —— 结果类型 + 旋钮 → 方法包 + 叠加层
│   │   ├── evidence-binding.md      # 每道计分题都绑定到课程内的一个证据来源（K1–K6）
│   │   ├── alignment.md             # 目标→题目→证据映射 + 警告阈值（H1–H3）
│   │   ├── feedback-anatomy.md      # 3 个必备反馈要素 —— 底线规则（G1–G3）
│   │   └── scoring-timing.md        # 形成性/终结性 +「证据之前不计分」（Z1–Z3）
│   ├── eval/
│   │   └── blind-test.md            # 盲测协议（≥ 1/2 通过阈值）—— 新屏幕类型的门
│   ├── pedagogy/                    # 第 3 层 —— 方法包（C 系列）
│   │   ├── _SCHEMA.md               # 包 front-matter 契约（evidence_phase(s) 必填）+ 校验命令
│   │   ├── _STUB-dogrusal.md        # 模式校验示例：线性流程（非方法包）
│   │   ├── _STUB-dongulu.md         # 模式校验示例：循环流程（非方法包）
│   │   ├── rosenshine-di.md         # C1 —— 直接教学：先示范，引导→独立练习
│   │   ├── merrill-fpi.md           # C2 —— Merrill 首要原理：以任务为中心的激活→示范→应用→整合
│   │   ├── 5e-inquiry.md            # C3 —— BSCS 5E 探究循环：先探索（需要探索屏幕类型）
│   │   ├── 4cid.md                  # C4 —— 4C/ID 复杂技能训练：整体任务，简单→复杂，逐渐撤除支持
│   │   ├── mastery-learning.md      # C5 —— Bloom 掌握学习：单元 → 形成性阈值 → 补救循环 → 终结性
│   │   ├── productive-failure.md    # C6 —— Kapur 有效失败：不计分的挣扎 → 巩固（需要探索；PK 下限 4）
│   │   ├── pbl-case.md              # C7 —— Barrows 案例/问题式学习：案例文件 = 证据工件族（高 PK）
│   │   ├── kolb-experiential.md     # C8 —— Kolb 经验循环：具体经验 → 反思 → 概念 → 主动实验（态度）
│   │   ├── sim-drill.md             # C9 —— 模拟演练：示范运行 → 不计分试做模式 → 复盘 → 部分任务循环 → 计分情景
│   │   ├── gagne-9.md               # C10 —— Gagné 九大事件（合规/强制培训；有据可依的兜底默认）
│   │   ├── cognitive-apprenticeship.md  # C11 —— Collins/Brown/Newman：专家出声思考示范 → 辅导 → 撤除 → 表述 → 反思 → 探索
│   │   └── retrieval-spaced.md      # C12 —— 提取练习 + 间隔（仅复习；证据 = 再曝光的参考工件）
│   ├── overlays/                    # 第 2 层 —— 与方法正交的叠加层（D 系列）
│   │   ├── _FRAMEWORK.md            # 叠加层文件格式 + 包无关性规则 + 冲突格式
│   │   ├── cognitive-load.md        # D1 —— 认知负荷管理：分段/预训练/通道/连贯/冗余/信号 → 屏幕决策
│   │   ├── udl.md                   # D2 —— UDL（CAST 3.0）：对同一证据来源的多重表征；作答格式选项；诚实的音频/字幕限度
│   │   ├── arcs.md                  # D3 —— Keller ARCS：注意/相关/自信/满足作为结构性决策（非语气）；不做装饰性游戏化
│   │   ├── expertise-adaptive.md    # D4 —— Kalyuga 专长反转：PK → 支持剂量（worked_example 撤除），经 visible_if 的专家路径；「可跳过 = 支持，绝非证据」
│   │   ├── assessment-alignment.md  # D5 —— Bloom 修订版/SOLO 层级 ↔ 题型映射；「回忆题无法测量应用目标」；分值权重分配
│   │   └── accessibility.md         # D6 —— 在平台诚实合规声明之上的 WCAG 2.2 AA 创作期决策（替代文本质量、键盘安全类型、学习者可控计时器）
│   ├── migration-v1-to-v2.md        # v1→v2 迁移指南：破坏性变更 + 配方 + 模式 A→rosenshine-di 映射 + 3-demo 手册
│   ├── source-expansion.md          # 压缩源展开：速查表行 → 机制问题 → 工件 → 绑定题（2 个示范转换）
│   ├── visual-storytelling.md       # 叙事线索 + 每屏视觉预算 + mockup-SVG 配方
│   ├── authoring-recommendations.md # 何时/如何/为何的决策指南（先读）
│   ├── mcp-cookbook.md              # 精确的工具调用 + 完整的 build_from_spec 结构
│   ├── course-patterns.md           # 经过验证的课程结构
│   ├── instructional-design.md      # 目标、微学习、避免模板疲劳
│   ├── screen-types.md              # 所有屏幕类型的选择指南
│   ├── assessment.md                # 题目/反馈/计分设计
│   ├── interactivity-and-gamification.md
│   ├── media.md                     # 跨 MCP 媒体 + 内置土耳其语 TTS + 本地助手
│   ├── video-generation.md          # 程序化动态图形 / 数据可视化视频
│   └── themes.md
├── templates/                       # 复制即用的蓝本
└── examples/                        # 旗舰多包示例（证据绑定，盲测通过）+ 已弃用的 v1 试点
```

## 要求

- 你的 AI 客户端可访问的 **[edumints SCORM MCP](https://github.com/kemalyy/edumints-scorm-mcp)**
  服务器（自托管或指向你自己的部署）。
- 支持 Agent Skills 的 MCP 客户端（如 Claude）。

## 安装

**claude.ai（Skills）：** 将 `authoring-scorm-courses/` 文件夹打包为 zip，并在
Settings → Capabilities → Skills → Create skill 上传。
```bash
cd authoring-scorm-courses && zip -r ../authoring-scorm-courses.zip . && cd ..
```

**Claude Code / 本地：** 将 `authoring-scorm-courses/` 文件夹复制到你的 skills 目录
（例如 `~/.claude/skills/authoring-scorm-courses/`）。

然后连接 scorm-mcp 服务器，让模型构建课程——它会遵循本技能。

## 许可证

**MIT** — 见 [LICENSE](LICENSE)。由 **edumints.com** 开发。提及的产品名称为各自所有者的商标（仅作指称性使用）。
