# 🧠 Codex Skills & Prompts Library

> **198 个技能 + 5 个提示词包 · 5 大领域 · 三层架构**

本仓库是 Codex 技能与提示词的统一集合。采用**领域 → 分类 → 内容**三层架构，从顶层 5 个领域即可快速定位到 200+ 个技能和提示词。

---

## 🏗️ 架构

```
skills/
├── 🧬 life-sciences/        88 items   生物 + 化学 + 临床
│   ├── bioinformatics/                  68 skills, 9 subcategories
│   ├── cheminformatics-drug-discovery/  14 skills
│   └── clinical-medical/                6 skills
│
├── 🤖 data-ai/              47 items   数据 + API + 自动化
│   ├── data-science-ml/                27 skills, 8 subcategories
│   ├── databases-apis/                 12 skills
│   └── ai-automation/                   8 skills
│
├── 🎓 academic/             37 items   学术研究 + 写作 + 中文
│   ├── academic-research/               4 skills + 2 prompts
│   ├── scientific-writing-research/    26 skills, 6 subcategories
│   └── chinese-academic/                5 skills
│
├── 🔬 science-eng/          11 items   物理 + 量子 + 地理
│   ├── physics-engineering/             5 skills
│   ├── quantum-computing/               4 skills
│   └── geospatial/                      2 skills
│
└── 🛠️ productivity/         20 items   文档 + 系统 + 生活
    ├── documents-presentations/         7 skills
    ├── system-tools/                    8 skills
    ├── system-maintenance/              1 prompt
    ├── knowledge-management/            1 prompt
    ├── relationships-and-communication/ 1 prompt
    ├── travel-planning/                 1 skill
    └── ui-design/                       1 skill
```

---

## 📊 内容总览

| 领域 | 分类数 | 技能 | 提示词 | 合计 |
|------|--------|------|--------|------|
| 🧬 life-sciences | 3 | 88 | — | 88 |
| 🤖 data-ai | 3 | 47 | — | 47 |
| 🎓 academic | 3 | 35 | 2 | 37 |
| 🔬 science-eng | 3 | 11 | — | 11 |
| 🛠️ productivity | 7 | 17 | 3 | 20 |
| **合计** | **19** | **198** | **5** | **203** |

### 热门技能速览

| 领域 | 热门技能 |
|------|----------|
| 🧬 life-sciences | AlphaFold, Scanpy, RDKit, Biopython, UniProt, DeepChem |
| 🤖 data-ai | Scikit-learn, PyTorch Lightning, Polars, Seaborn, Modal |
| 🎓 academic | 文献综述、NSFC 申请、Nature 论文写作、沁言学术 |
| 🔬 science-eng | Qiskit, Astropy, GeoPandas, PyMatGen |
| 🛠️ productivity | PDF 处理, PPTX, Codex 技能安装器, 记忆整理 |

---

## 🚀 快速开始

### 安装技能

```bash
# 手动复制（Windows PowerShell）
Copy-Item -Recurse skills/<领域>/<分类>/<技能名> $env:USERPROFILE\.codex\skills\<技能名>

# macOS / Linux
cp -r skills/<领域>/<分类>/<技能名> ~/.codex/skills/<技能名>

# 使用 skill-installer（在 Codex 对话中）
"从 https://github.com/zc-xzc/prompt-library 安装 rdkit 技能"
```

### 使用提示词

```bash
# 提示词与技能放在同一分类下
cat skills/academic/academic-research/nature-agent/nature-agent.md
```

### 导航技巧

```
想找某个技能？→ 确定领域 → 找到分类 → 找到技能目录
不确定领域？  → 看上方架构图，按场景匹配
想浏览所有？  → 进入 skills/ 逐个领域探索
```

---

## 🤝 贡献

见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。验证：`python scripts/validate_docs.py`

---

## 📄 许可证

[MIT License](LICENSE) © 2026 Zicheng Xu
