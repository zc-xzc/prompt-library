# 🧠 Codex Skills & Prompts Library

> **198 个 Codex 技能 · 19 大分类 · 提示词与技能统一管理**

本仓库是一个 Codex（OpenAI 的 AI 编程助手）技能（Skills）与提示词（Prompts）的统一集合。所有内容按场景分类，技能和提示词放在同一分类目录下——不再需要在两个地方分别查找。

---

## 📖 仓库概述

| 内容类型 | 说明 | 识别方式 |
|----------|------|----------|
| **Skills（技能）** | 可安装的 Codex 技能，包含 `SKILL.md`。安装后 AI 能自动调用对应工具。 | 目录中存在 `SKILL.md` |
| **Prompts（提示词）** | 经过验证的提示词模板，可直接复制到对话中使用。 | 目录中存在 `.md` 提示词文件 |

两种内容按**同一套分类体系**组织，同一领域的技能和提示词在同一个分类目录中。

---

## 📂 目录结构

```
prompt-library/
├── README.md                   # 仓库总览
├── CONTRIBUTING.md             # 贡献指南
├── LICENSE                     # MIT 许可证
├── skills/                     # 所有技能和提示词（19 个分类，统一管理）
│   ├── academic-research/      # 学术研究（4 技能 + 2 提示词）
│   ├── ai-automation/          # AI 自动化（8 技能）
│   ├── bioinformatics/         # 生物信息学（68 技能，9 子类）
│   ├── cheminformatics-drug-discovery/  # 化学信息学（14 技能）
│   ├── chinese-academic/       # 中文学术（5 技能）
│   ├── clinical-medical/       # 临床医学（6 技能）
│   ├── databases-apis/         # 数据库与 API（12 技能）
│   ├── data-science-ml/        # 数据科学与 ML（27 技能，8 子类）
│   ├── documents-presentations/# 文档演示（7 技能）
│   ├── geospatial/             # 地理空间（2 技能）
│   ├── knowledge-management/   # 知识管理（1 提示词）
│   ├── physics-engineering/    # 物理工程（5 技能）
│   ├── quantum-computing/      # 量子计算（4 技能）
│   ├── relationships-and-communication/  # 人际关系（1 提示词）
│   ├── scientific-writing-research/  # 科学写作与研究（26 技能，6 子类）
│   ├── system-maintenance/     # 系统维护（1 提示词）
│   ├── system-tools/           # 系统工具（8 技能）
│   ├── travel-planning/        # 旅行规划（1 技能）
│   └── ui-design/              # UI 设计（1 技能）
├── scripts/                    # 仓库工具脚本
│   └── validate_docs.py        # 文档验证（UTF-8、链接、结构检查）
└── templates/                  # 模板文件
    └── prompt-template.md      # 提示词编写模板
```

---

## 📊 内容总览

| 分类 | 技能 | 提示词 | 典型内容 |
|------|------|--------|----------|
| 🧬 bioinformatics | 68 | — | AlphaFold, Scanpy, Biopython, GEO, gnomAD, Uniprot |
| 📊 data-science-ml | 27 | — | Scikit-learn, PyTorch Lightning, Seaborn, Polars, SHAP |
| 📝 scientific-writing-research | 26 | — | 文献综述、同行评审、基金申请、LaTeX 海报、学术写作 |
| ⚗️ cheminformatics-drug-discovery | 14 | — | RDKit, DeepChem, Molfeat, DiffDock, ZINC |
| 🔗 databases-apis | 12 | — | PubChem, PubMed, FRED, Alpha Vantage, USPTO |
| 🤖 ai-automation | 8 | — | Modal, Open Notebook, Denario |
| 🛠️ system-tools | 8 | — | 技能安装器、定时任务、记忆整理、图片生成 |
| 📄 documents-presentations | 7 | — | PDF, DOCX, PPTX, XLSX, MarkItDown, 信息图 |
| 🏥 clinical-medical | 6 | — | 临床决策支持、临床报告、治疗方案、ISO 13485 |
| 🔬 physics-engineering | 5 | — | Astropy, FluidSim, PyMatGen, 分子动力学 |
| 🀄 chinese-academic | 5 | — | 沁言学术工具（检索/分析/润色/选题/引用） |
| 🎓 academic-research | 4 | 2 | Nature 学术搜索/引文/PPT + 研究工作流提示词 |
| ⚛️ quantum-computing | 4 | — | Qiskit, PennyLane, Cirq, QuTiP |
| 🗺️ geospatial | 2 | — | GeoPandas, GeoMaster |
| 📚 knowledge-management | — | 1 | 对话归档与恢复 |
| 💬 relationships-and-communication | — | 1 | 人际边界指南 |
| 🖥️ system-maintenance | — | 1 | macOS 系统清理 |
| 📱 ui-design | 1 | — | 前端设计指南 |
| 🗺️ travel-planning | 1 | — | 青甘大环线旅游规划 |

> **合计：198 个技能 + 5 个提示词包，19 个分类统一管理。**

---

## 🚀 快速开始

### 安装技能

```bash
# 方式一：手动复制到 Codex 技能目录
# Windows (PowerShell)
Copy-Item -Recurse skills/<分类>/<技能名> $env:USERPROFILE\.codex\skills\<技能名>

# macOS / Linux
cp -r skills/<分类>/<技能名> ~/.codex/skills/<技能名>

# 方式二：使用 skill-installer（在 Codex 中对话）
"请从 https://github.com/zc-xzc/prompt-library 安装 <技能名> 技能"

# 方式三：克隆整个仓库
git clone https://github.com/zc-xzc/prompt-library.git
```

### 使用提示词

提示词和技能放在同一个分类目录下。查找时只需：

1. 进入 `skills/<场景分类>/` 找到对应的提示词目录
2. 阅读 `README.md` 了解使用场景
3. 复制 `.md` 提示词文件的内容
4. 替换占位符后粘贴到 Codex 中使用

**示例**：

```bash
# 查看旅游规划
ls skills/travel-planning/

# 使用学术研究工作流提示词
cat skills/academic-research/nature-agent/nature-agent.md
```

### 编写新内容

参考 [`templates/prompt-template.md`](templates/prompt-template.md) 和 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

---

## 🔧 工具脚本

| 脚本 | 用途 |
|------|------|
| `scripts/validate_docs.py` | 验证所有 Markdown 文件的 UTF-8 编码、内部链接、目录结构 |

```bash
python scripts/validate_docs.py
```

---

## 🤝 贡献

欢迎贡献经过真实任务验证的技能和提示词！详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

贡献流程：
1. Fork 本仓库
2. 创建分支 (`git checkout -b feat/your-feature`)
3. 在 `skills/<分类>/` 下添加内容（技能需含 `SKILL.md`，提示词参照模板）
4. 补充对应分类的 `README.md` 入口
5. 运行 `python scripts/validate_docs.py` 确认通过
6. 提交并创建 Pull Request

---

## 📄 许可证

[MIT License](LICENSE) © 2026 Zicheng Xu
