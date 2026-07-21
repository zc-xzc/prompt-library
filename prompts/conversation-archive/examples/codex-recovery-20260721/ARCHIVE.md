# 对话归档：Codex 对话数据恢复与磁盘迁移

## 1. 归档元数据

| 项目 | 内容 |
|------|------|
| 归档日期 | 2026-07-21 (Asia/Shanghai) |
| 对话主题 | Codex Desktop 对话丢失恢复、数据库修复、C盘到D盘数据迁移 |
| 使用场景 | Codex Desktop 用户发现历史对话消失，需排查恢复 |
| 最终目的 | 恢复全部丢失对话、合并数据库、清理冗余目录、确保后续对话写入正确位置 |
| 覆盖范围 | 2026-07-20 11:49 ~ 2026-07-21 |
| 生成环境 | Codex Desktop on Windows, PowerShell, Python 3 |
| 工作目录 | C:\\Users\\xzc\\Documents\\Codex\\2026-07-20\\wo |
| 归档形态 | 带 artifacts/ 的归档目录 |

## 2. 完整性与缺口

- 已完整收录：全部对话历史、执行的命令、数据库修改记录、最终文件路径和状态
- 已知缺口：无。在当前可见上下文范围内未发现已知缺口
- 对话中未涉及任何凭证或敏感信息

## 3. 对话整体概况

用户发现 Codex Desktop 中的历史对话全部消失，怀疑与 C 盘和 D 盘两个 .codex 目录有关。

### 执行过程

1. **诊断**：对比 C:\\Users\\xzc\\.codex 和 D:\\Documents\\.codex，发现两者结构几乎相同。Codex 当前使用 D: 盘目录。
2. **定位根因**： sessions/ 目录中有 37 个 JSONL 会话文件，但 state_5.sqlite 只注册了 10 个线程——29 个对话文件存在但数据库无记录。
3. **首次恢复**：从 JSONL 文件提取元数据，写入根目录 state_5.sqlite，恢复 29 条记录。
4. **发现问题**：用户重启后仍未看到——Codex 实际读取 sqlite/state_5.sqlite（42 个旧线程），而非根目录的。
5. **合并修复**：将两个数据库合并到 sqlite/state_5.sqlite（69 线程），补齐缺失列，更新所有 rollout_path 从 C: 指向 D:。
6. **清理**：C 盘重复目录重命名为 C:\\Users\\xzc\\.codex.old。

### 最终状态
全部 69 个对话已恢复，所有数据在 D 盘，新对话自动写入 D 盘。

## 4. 用户需求、偏好与硬性约束

| 需求 | 状态 |
|------|------|
| 恢复丢失的对话 | ✅ 已完成 |
| C盘和D盘重复则保留一者 | ✅ 已完成（保留D，C重命名为.old） |
| 新对话继续写入正确位置 | ✅ 已确认 |

## 5. 对话时序与迭代记录

### 阶段 1：诊断 (2026-07-20 11:49)
- 用户提出对话丢了，两个目录重复的话保留一个
- 遍历 C: 和 D: .codex 目录，对比文件结构、sessions 数量、SQLite 数据库
- 发现 D: 有 37 个 session 文件，state_5.sqlite 只注册 10 个线程，缺失 29 个

### 阶段 2：首次恢复 (2026-07-20 11:52)
- 操作：编写 Python 脚本解析 JSONL session 文件的 session_meta 和 user_message 行，提取标题和元数据
- 结果：29 条记录插入根目录 state_5.sqlite（总计 39），更新所有标题

### 阶段 3：路径修复 (2026-07-20 11:56)
- 8 个旧线程的 rollout_path 从 C:\\Users\\xzc\\.codex\\ 更新为 D:\\Documents\\.codex\\
- C:\\Users\\xzc\\.codex 重命名为 .codex.old

### 阶段 4：发现问题 (2026-07-20)
- 用户反馈：重启后仍未看到恢复的对话
- 分析：Codex 实际读取 sqlite/state_5.sqlite（42 线程，截止 6/17），而非根目录的（39 线程，含最新）

### 阶段 5：合并修复 (2026-07-20)
- 备份 sqlite/state_5.sqlite，从根数据库插入 27 个新线程
- 补齐缺失列：recency_at, recency_at_ms, history_mode
- 修正 42 条 C: 路径
- 最终：sqlite/state_5.sqlite 共 69 线程，覆盖 2026-04-20 ~ 2026-07-20

### 阶段 6：验证 (2026-07-21)
- 用户确认：对话已恢复，文件全在 D 盘，新对话写入 D 盘

## 6. 决策与事实库

### 已验证事实
- Codex Desktop 当前数据目录：D:\\Documents\\.codex（记录于 2026-07-20）
- Codex Desktop 和 CLI 版本共用同一数据目录，无独立 CLI 目录
- sessions/ 目录使用层级结构：sessions/YYYY/MM/DD/rollout-*.jsonl
- JSONL 格式：timestamp / type（session_meta, event_msg, response_item）/ payload
- 用户消息类型：event_msg → payload.type = user_message
- 数据库 sqlite/state_5.sqlite 的 threads 表共 32 列

### 关键路径
| 路径 | 用途 |
|------|------|
| D:\\Documents\\.codex | Codex Desktop + CLI 数据根目录 |
| D:\\Documents\\.codex\\sessions\\YYYY\\MM\\DD\\ | 对话 rollout 文件 |
| D:\\Documents\\.codex\\archived_sessions\\ | 已归档对话 |
| D:\\Documents\\.codex\\sqlite\\state_5.sqlite | 线程索引数据库 |
| D:\\Documents\\.codex\\sqlite\\codex-dev.db | 线程目录、自动化 |
| D:\\Documents\\.codex\\config.toml | 配置文件 |
| C:\\Users\\xzc\\.codex.old | 旧 C 盘备份（可删除） |

### 数据库备份
- D:\\Documents\\.codex\\state_5.sqlite.backup-20260720-115606
- D:\\Documents\\.codex\\sqlite\\state_5.sqlite.merge-backup-20260720

## 7. 全部交付物目录

| 交付物 | 类型 | 状态 | 说明 |
|--------|------|------|------|
| 恢复的 69 个对话 | 数据库记录 | ✅ | sqlite/state_5.sqlite |
| 数据库合并脚本 | Python | ✅ | 见 artifacts/restore_sessions.py |
| 路径修正 | 数据库更新 | ✅ | 全部 rollout_path → D: |
| C 盘清理 | 文件操作 | ✅ | 重命名为 .codex.old |

## 8. 最终交付物完整保存区

### 8.1 代码、脚本与命令

核心恢复 Python 脚本见 artifacts/restore_sessions.py，包含：
- JSONL session 文件元数据提取
- state_5.sqlite 线程记录插入
- 双数据库合并逻辑
- rollout_path C: → D: 批量替换

### 8.2 提示词、模板与文案

本归档使用 conversation-archive prompt（来源：https://github.com/zc-xzc/prompt-library/blob/main/prompts/conversation-archive/prompt.md）

### 8.3 方案、流程与研究结果

数据恢复流程：
1. 遍历 sessions/ 目录收集所有 JSONL 文件
2. 解析 session_meta 获取 session_id、cwd、timestamp
3. 解析首个 user_message 获取标题
4. INSERT 到 state_5.sqlite 的 threads 表
5. 合并双数据库：root → sqlite/，补齐列，更新 C: 路径
