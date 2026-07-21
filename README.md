# 🧠 Codex Skills & Prompts Library

> **198 个 Codex 技能 · 16 大分类 · 5 类提示词模板 · 一站式 AI 效率工具库**

本仓库是一个面向 Codex（OpenAI 的 AI 编程助手）的技能（Skills）与提示词（Prompts）集合。无论你是科研人员、开发者、数据分析师，还是想在日常生活中借助 AI 提升效率，都能在这里找到可直接使用的技能和提示词模板。

---

## 📖 仓库概述

这个仓库包含两大核心内容：

| 内容 | 说明 | 位置 |
|------|------|------|
| **Skills（技能）** | 198 个预配置的 Codex 技能，覆盖生物信息学、数据科学、科学写作等 16 个领域。安装后，Codex 能自动调用对应工具和知识完成专业任务。 | [`skills/`](skills/) |
| **Prompts（提示词）** | 经过真实任务验证的提示词模板，覆盖学术研究、知识管理、系统维护等场景。可直接复制使用，或作为编写新提示词的参考。 | [`prompts/`](prompts/) |

**核心理念**：每个技能和提示词都经过了真实任务验证，优先保证"能够稳定完成任务"，而不是追求提示词的长度或复杂度。

---

## 📂 目录结构

```
prompt-library/
├── README.md                   # 本文件 — 仓库总览
├── CONTRIBUTING.md             # 贡献指南
├── LICENSE                     # MIT 许可证
├── skills/                     # 198 个 Codex 技能（16 大分类）
│   ├── academic-research/      # 学术研究（4 个）
│   ├── ai-automation/          # AI 自动化（8 个）
│   ├── bioinformatics/         # 生物信息学（68 个，9 个子类）
│   ├── cheminformatics-drug-discovery/  # 化学信息学（14 个）
│   ├── chinese-academic/       # 中文学术（5 个）
│   ├── clinical-medical/       # 临床医学（6 个）
│   ├── databases-apis/         # 数据库与 API（12 个）
│   ├── data-science-ml/        # 数据科学与 ML（27 个，8 个子类）
│   ├── documents-presentations/# 文档演示（7 个）
│   ├── geospatial/             # 地理空间（2 个）
│   ├── physics-engineering/    # 物理工程（5 个）
│   ├── quantum-computing/      # 量子计算（4 个）
│   ├── scientific-writing-research/  # 科学写作与研究（26 个，6 个子类）
│   ├── system-tools/           # 系统工具（8 个）
│   ├── travel-planning/        # 旅行规划（1 个）
│   └── ui-design/              # UI 设计（1 个）
├── prompts/                    # 提示词模板（5 大场景）
│   ├── academic-research/      # 学术研究
│   ├── knowledge-management/   # 知识管理
│   ├── relationships-and-communication/  # 人际关系与沟通
│   ├── system-maintenance/     # 系统维护
│   └── travel-planning/        # 旅行规划
├── scripts/                    # 仓库工具脚本
│   └── validate_docs.py        # 文档验证（UTF-8、链接、结构检查）
└── templates/                  # 模板文件
    └── prompt-template.md      # 提示词编写模板
```

---

## 📊 技能总览

| 分类 | 数量 | 子目录 | 典型技能 |
|------|------|--------|----------|
| 🧬 bioinformatics | 68 | genomics, proteomics, single-cell, systems-biology, bio-databases, lab-automation, neuro-imaging, phylo-evo, bio-utils | AlphaFold, Scanpy, Biopython, PySAM, GEO, gnomAD, Uniprot |
| 📊 data-science-ml | 27 | ml-dl, statistics, visualization, data-processing, timeseries, math-symbolic, simulation, other-ml | Scikit-learn, PyTorch Lightning, Seaborn, Plotly, Statsmodels, SHAP, Polars |
| 📝 scientific-writing-research | 26 | writing-core, grants-proposals, papers-review, presentations, tools-utils, special | 文献综述、同行评审、基金申请、LaTeX 海报、学术写作 |
| ⚗️ cheminformatics-drug-discovery | 14 | — | RDKit, DeepChem, Molfeat, DataMol, DiffDock, ZINC |
| 🔗 databases-apis | 12 | — | PubChem, ChEMBL, DrugBank, KEGG, Alpha Vantage, FRED, EDGAR |
| 🤖 ai-automation | 8 | — | Modal, Open Notebook, Denario, Claude Skill Registry |
| 🛠️ system-tools | 8 | schedule, consolidate-memory | Codex 技能安装器、定时任务、记忆整理、图片生成 |
| 📄 documents-presentations | 7 | — | PDF, DOCX, PPTX, XLSX, MarkItDown, 信息图 |
| 🏥 clinical-medical | 6 | — | 临床决策支持、临床报告、治疗方案、ISO 13485 |
| 🔬 physics-engineering | 5 | — | Astropy, FluidSim, PyMatGen, 分子动力学, Rowan |
| 🀄 chinese-academic | 5 | — | NSFC 申请书、NSSFC 申请书、沁言学术工具 |
| 🎓 academic-research | 4 | — | BGPT 论文搜索、Nature 学术搜索/引文/PPT |
| ⚛️ quantum-computing | 4 | — | Qiskit, PennyLane, Cirq, QuTiP |
| 🗺️ geospatial | 2 | — | GeoPandas, GeoMaster |
| 📱 ui-design | 1 | frontend-design | 前端设计指南 |
| 🗺️ travel-planning | 1 | qinggan-loop-planner | 青甘大环线旅游规划 |

> **合计：198 个技能**，覆盖 16 个领域大类。

---

## 📋 提示词模板

提示词模板按使用场景分为 5 个大类，每类包含一个或多个经过验证的提示词包：

| 分类 | 提示词包 | 说明 |
|------|----------|------|
| 🎓 academic-research | academic-tools, nature-agent | 研究工具选择、学术检索/写作/润色/引文工作流 |
| 📚 knowledge-management | conversation-archive | 对话归档、知识整理与恢复 |
| 💬 relationships-and-communication | interpersonal-boundary-guide | 人际沟通、边界指南 |
| 🖥️ system-maintenance | macos-cleanup | macOS 系统清理与维护 |
| ✈️ travel-planning | — | 旅行规划（模板预留，欢迎贡献） |

> 详细说明见 [`prompts/README.md`](prompts/README.md)

---

## 🚀 快速开始

### 安装技能

所有技能均为标准 Codex 技能格式（包含 `SKILL.md` 和配套文件），可通过以下方式安装：

**方式一：使用 skill-installer 安装单个技能**

```bash
# 如果你已经安装了 skill-installer 技能，直接在 Codex 中对话：
"请从 https://github.com/zc-xzc/prompt-library 安装 <技能名> 技能"
```

**方式二：手动复制到 Codex 技能目录**

```bash
# Windows (PowerShell)
Copy-Item -Recurse skills/<分类>/<技能名> $env:USERPROFILE\.codex\skills\<技能名>

# macOS / Linux
cp -r skills/<分类>/<技能名> ~/.codex/skills/<技能名>
```

**方式三：克隆整个仓库后链接技能**

```bash
git clone https://github.com/zc-xzc/prompt-library.git
# 将需要的技能目录链接或复制到 ~/.codex/skills/
```

### 使用提示词

1. 浏览 [`prompts/`](prompts/) 目录，找到适合你场景的提示词包。
2. 阅读该包的 `README.md` 了解使用场景和注意事项。
3. 打开同目录下的 `.md` 文件，复制提示词文本。
4. 将提示词中的占位符（如 `<任务目标>`、`<输入>`）替换为你的实际内容。
5. 在 Codex 中粘贴使用。

**示例**：

```text
# 复制 prompts/academic-research/academic-tools/academic-tools.md 后，替换占位符：

请完成以下任务：用 Python 分析这篇论文的引用网络。

【本次参数】
- 输入：./paper.pdf
- 输出位置：./analysis/
- 允许执行的操作：读取文件、运行 Python 脚本、生成报告
...
```

### 编写新提示词

参考 [`templates/prompt-template.md`](templates/prompt-template.md) 和 [`CONTRIBUTING.md`](CONTRIBUTING.md)，遵循以下原则：

- 任务目标、输入和交付物必须明确
- 区分只读检查、可逆操作和不可逆操作
- 为删除、覆盖等高影响操作设置边界
- 完成后明确验证方法

---

## 🔧 工具脚本

| 脚本 | 用途 |
|------|------|
| `scripts/validate_docs.py` | 验证所有 Markdown 文件的 UTF-8 编码、内部链接、prompts 目录结构 |

```bash
python scripts/validate_docs.py
```

---

## 🤝 贡献

欢迎贡献经过真实任务验证的技能和提示词！详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

贡献流程：
1. Fork 本仓库
2. 创建分支 (`git checkout -b feat/your-feature`)
3. 添加内容（参考模板和约定）
4. 运行 `python scripts/validate_docs.py` 确认通过
5. 提交并推送 (`git commit -m 'feat: add ...'`)
6. 创建 Pull Request

---

## 📄 许可证

[MIT License](LICENSE) © 2026 Zicheng Xu
