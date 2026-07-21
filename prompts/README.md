# 📋 Prompts — 提示词模板与使用示例

本目录包含各类场景的提示词（Prompt）模板。每份提示词都经过真实任务验证，可以直接复制使用，也可以作为参考来编写你自己的提示词。

---

## 📂 目录结构

```
prompts/
├── README.md                                 # 本文件
├── academic-research/                        # 学术研究
│   ├── README.md                             # 分类说明
│   ├── academic-tools/                       # 研究工具选择与使用
│   │   ├── README.md                         # 使用场景与注意事项
│   │   └── academic-tools.md                 # 可复制的提示词
│   └── nature-agent/                         # 学术研究工作流
│       ├── README.md                         # 快速使用指南
│       ├── nature-agent.md                   # 主工作流入口
│       ├── academic-search.md                # 文献检索
│       ├── academic-writing.md               # 论文写作
│       ├── academic-polishing.md             # 文本润色
│       └── academic-citation.md              # 引文管理
├── knowledge-management/                     # 知识管理
│   ├── README.md
│   └── conversation-archive/                 # 对话归档与恢复
│       ├── README.md
│       └── conversation-archive.md
├── relationships-and-communication/          # 人际关系与沟通
│   ├── README.md
│   └── interpersonal-boundary-guide/         # 人际边界指南
│       ├── README.md
│       └── interpersonal-boundary-guide.md
├── system-maintenance/                       # 系统维护
│   ├── README.md
│   └── macos-cleanup/                        # macOS 系统清理
│       ├── README.md
│       └── macos-cleanup.md
└── travel-planning/                          # 旅行规划
    └── README.md                             # 模板预留，欢迎贡献
```

---

## 🔍 提示词总览

| 分类 | 提示词包 | 适用场景 | 一句话描述 |
|------|----------|----------|-----------|
| 🎓 academic-research | [academic-tools](academic-research/academic-tools/) | 研究自动化 | 研究工具选择与使用的安全任务规划 |
| 🎓 academic-research | [nature-agent](academic-research/nature-agent/) | 学术写作全流程 | 文献检索 → 论文写作 → 润色 → 引文管理的完整工作流 |
| 📚 knowledge-management | [conversation-archive](knowledge-management/conversation-archive/) | 对话归档 | 保存对话中的需求、决策、代码、验证结果，支持恢复 |
| 💬 relationships-and-communication | [interpersonal-boundary-guide](relationships-and-communication/interpersonal-boundary-guide/) | 人际交往 | 基于尊重与边界的健康人际交往指南 |
| 🖥️ system-maintenance | [macos-cleanup](system-maintenance/macos-cleanup/) | Mac 清理 | 检查并清理 macOS 常用软件产生的缓存和日志 |
| ✈️ travel-planning | — | 旅行规划 | 模板预留，欢迎贡献 |

---

## 🚀 如何使用提示词

### 1. 找到合适的提示词

浏览上方表格，根据你的场景找到对应的提示词包，点击链接进入子目录。

### 2. 阅读使用说明

每个提示词包都有一个 `README.md`，其中包含：
- **适用场景**：什么情况下使用这个提示词
- **能力边界**：能做什么、不能做什么
- **风险和限制**：需要注意的安全和隐私问题
- **前置准备**：使用前需要准备什么

### 3. 复制并替换占位符

打开同目录的 `.md` 文件（如 `academic-tools.md`），将提示词文本完整复制。然后将其中的占位符（用 `<>` 包裹的内容）替换为你的实际需求：

```
- 输入或目标：<输入>          →  输入或目标：./data/paper.pdf
- 输出位置：<输出位置>        →  输出位置：./results/
```

### 4. 在 Codex 中使用

将替换好的提示词粘贴到 Codex 对话框中执行。执行时注意：
- 首次使用建议先用一个小任务测试
- 观察 AI 是否准确理解你的边界条件
- 根据实际效果调整提示词中的参数

---

## ✍️ 编写新提示词

参考根目录的 [`templates/prompt-template.md`](../templates/prompt-template.md) 和 [`CONTRIBUTING.md`](../CONTRIBUTING.md)。

提示词编写核心原则：

1. **目标明确**：一句话说清楚要完成什么
2. **边界清晰**：明确"允许"和"禁止"的操作范围
3. **可验证**：写明完成后的检查标准
4. **可复用**：用占位符表达可变信息，不依赖对话背景
5. **安全优先**：对删除、覆盖、付款等操作设定明确边界

---

## 📄 格式约定

- 文件名：小写英文 + 连字符（如 `macos-cleanup.md`）
- 语言：中文为主，必要时补充英文术语
- 占位符：`<描述>` 格式（如 `<目标路径>`、`<仓库地址>`）
- 验证：提交前运行 `python ../scripts/validate_docs.py`
