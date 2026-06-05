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
└── examples/                        # 一份完整、高质量的示例课程规范
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
