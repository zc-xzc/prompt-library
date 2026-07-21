# Prompt Library

一个持续整理的可复用提示词库，用于 Codex 和其他 AI 智能体。这里保存的不只是几句话，而是经过实际任务验证、带有安全边界和验收标准的完整工作流程。

## 快速使用

1. 在下方目录中选择一个任务。
2. 打开对应的提示词文件，复制“可直接使用的提示词”。
3. 按需修改提示词开头的参数，例如目标路径、软件名称或是否允许退出应用。
4. 将完整内容发送给 Codex，并在执行结束后检查结果摘要。

## 提示词目录

| 分类 | 提示词 | 用途 |
| --- | --- | --- |
| [系统维护](prompts/system-maintenance/README.md) | [清理 macOS 软件缓存与残留](prompts/system-maintenance/macos-cleanup/macos-cleanup.md) | 审计并清理用户目录中的缓存、日志、临时文件和已完成的升级包，同时保护聊天记录、文档与账号数据 |
| [知识管理](prompts/knowledge-management/README.md) | [对话自包含归档与恢复](prompts/knowledge-management/conversation-archive/conversation-archive.md) | 整理当前可见的对话、代码和附件，生成可在新对话中继续工作的独立备份 |
| [人际关系与沟通](prompts/relationships-and-communication/README.md) | [人际交往思考指南：尊重与边界](prompts/relationships-and-communication/interpersonal-boundary-guide/interpersonal-boundary-guide.md) | 分析关系边界与互动节奏，帮助减少过度付出、误读信号与社交内耗 |
| [学术研究](prompts/academic-research/README.md) | [Nature Agent：学术研究工作流](prompts/academic-research/nature-agent/nature-agent.md) | 将文献检索、论文写作、文本润色和引文管理组织为可核验的工作流 |
| [学术研究](prompts/academic-research/README.md) | [Academic Tools：研究工具选择与使用](prompts/academic-research/academic-tools/academic-tools.md) | 选择、运行和核验学术研究中的本地自动化与文本处理工具 |

旅行规划分类已预留，后续可直接加入行程设计、预算、资料整理等提示词包。

## 仓库结构

```text
prompt-library/
|-- README.md
|-- CONTRIBUTING.md
|-- prompts/
|   |-- README.md
|   |-- system-maintenance/
|   |   |-- README.md
|   |   `-- macos-cleanup/
|   |-- knowledge-management/
|   |   `-- conversation-archive/
|   |-- relationships-and-communication/
|   |   `-- interpersonal-boundary-guide/
|   |-- travel-planning/
|   `-- academic-research/
|       |-- README.md
|       |-- nature-agent/
|       `-- academic-tools/
|-- templates/
    |-- prompt-template.md
```

每个大类目录包含一个 README，用于说明适用范围并索引其下的提示词。每个具体提示词目录包含：

- 以目录名命名的 .md 文件（如 conversation-archive.md）：可直接复制使用的完整提示词。
- README.md：适用场景、参数说明、风险边界和维护记录（GitHub 自动渲染为目录首页）。

## 设计原则

- **结果明确**：先写清楚希望完成什么，再说明执行步骤。
- **边界清晰**：明确哪些内容可以处理，哪些内容绝不能碰。
- **可验证**：要求执行前后对比，并报告实际结果。
- **可复用**：把容易变化的信息放在参数区，不把个人路径、账号或隐私写死。
- **安全优先**：涉及删除、覆盖或对外发布时，限定精确目标并保留人工复核点。

如需新增提示词，请从 [通用模板](templates/prompt-template.md) 开始，并参考 [贡献指南](CONTRIBUTING.md)。

## License

本仓库采用 [MIT License](LICENSE)。使用提示词执行具体操作时，仍需自行确认目标环境、数据备份和操作风险。
