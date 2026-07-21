<div align="center">

# 📚 Prompt Library

**经过实战验证的 AI 提示词库** · 不只是几句话，而是完整的工作流程

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

## ⚡ 快速开始

1. 在下方目录中找到你需要的任务
2. 打开提示词文件，复制“可直接使用的提示词”部分
3. 修改开头的参数（如目标路径、软件名称）
4. 发送给 Codex 或其他 AI 智能体，执行后检查结果

---

## 📋 提示词目录

### 🖥️ 系统维护

| 提示词 | 用途 | 安全等级 |
| --- | --- | --- |
| [🧹 macOS 软件缓存与残留清理](prompts/macos-cleanup/macos-cleanup.md) | 审计并清理用户目录中的缓存、日志、临时文件和升级包，保护聊天记录、文档与账号数据 | 🟢 安全 |

### 📚 知识管理

| 提示词 | 用途 | 安全等级 |
| --- | --- | --- |
| [📦 对话自包含归档与恢复](prompts/conversation-archive/conversation-archive.md) | 一键整理当前对话、代码和附件，生成可在新对话中继续工作的独立备份 | 🟢 安全 |

---

## 🏗️ 仓库结构

`
prompt-library/
|-- README.md              <-- 你在这里
|-- CONTRIBUTING.md         <-- 贡献指南
|-- prompts/                <-- 提示词库
|   |-- README.md           <-- 索引
|   |-- macos-cleanup/      <-- macOS 维护
|   |   |-- macos-cleanup.md
|   |   \-- README.md
|   \-- conversation-archive/ <-- 知识管理
|       |-- conversation-archive.md
|       |-- README.md
|       \-- examples/
\-- templates/              <-- 模板
    \-- prompt-template.md
`

> **命名规范**：每个任务目录包含：
> - **\u76ee录名.md\**：可直接复制使用的完整提示词
> - **\README.md\**：适用场景、参数说明、风险边界（GitHub 自动渲染为目录首页）

---

## 📖 设计原则

| 原则 | 说明 |
| --- | --- |
| **结果明确** | 先写清楚希望完成什么，再说明执行步骤 |
| **边界清晰** | 明确哪些可以处理，哪些绝不能碰 |
| **可验证** | 要求执行前后对比，报告实际结果 |
| **可复用** | 变量放参数区，不写死个人路径和帐号 |
| **安全优先** | 涉及删除、覆盖、发布时限定精确目标，保留人工复核点 |

---

## ✨ 贡献

欢迎提交经过实战验证的提示词！

1. Fork 本仓库，创建新分支
2. 从 [\	emplates/prompt-template.md\](templates/prompt-template.md) 开始，在 \prompts/\ 下创建新目录
3. 确保提交前已移除个人信息，并更新索引
4. 发起 PR，等待审查

详细规范请参阅 [\CONTRIBUTING.md\](CONTRIBUTING.md)。

---

## 📄 License

[MIT](LICENSE) · 使用提示词执行具体操作时，请自行确认目标环境、数据备份和操作风险。
