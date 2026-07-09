---
id: wechat-article
name: 审校
role: 公众号写作工作流 Step 9-11 — 降 AI 处理、9 项自检、日期核实、归档
version: 1.0.0
language: zh-CN
dependencies:
  - fact-checker: 事实核查员必须完成 Step 8 交棒（核查全绿 + 用户确认）
  - anti-ai: 降 AI 处理依赖本包内的 anti-ai skill
tools_required:
  - read_file
  - write_file
  - terminal
---

# 审校 Skill（Step 9-11）

**适用范围：** 公众号写作工作流的最后一道防线。文章质量从这里出厂。

---

## when_to_use

- 收到 🟡 事实核查员交棒（核查全绿 + 用户确认降 AI）
- 文章写完、事实核查通过后

---

## 执行流程

### 前置门禁

事实核查全绿 + 用户确认降 AI → 才能启动 Step 9。

---

### Step 9 — 降 AI

**加载同包内的 `skills/anti-ai.md`，执行语言层面降 AI。**

**核心纪律：**
- 只在词层面工作：换高频词、拆长句、去 AI 骨架
- HTML 格式不动：胶囊小标题、图片顺序、模板结构全部保留
- 降 AI 是必过门，不是可选项

**详细操作见 `skills/anti-ai.md`。**

**门禁：降 AI 做了才进入 Step 10。**

---

### Step 10 — 9 项自检

逐项核对，**缺任何一项 = 打回**：

| # | 检查项 | 验证方法 |
|:--|:------|:--------|
| 1 | HTML 文件存在？ | `ls` 确认文件路径 |
| 2 | 路径格式正确？ | `${USER_WORKSPACE}/{月.日}/{公众号名}/{标题}.html` |
| 3 | 是用模板改的？ | 检查 DOCTYPE / titlestyle / hl 类是否来自模板 |
| 4 | 胶囊 CSS 完整？ | `.titlestyle span` 必须含 `padding:6px 24px; border-radius:50px;` |
| 5 | 日期正确？ | 跑 `date +%-m.%-d` 确认，不准凭感觉 |
| 6 | verify 通过？ | 跑 `python3 ${PACKAGE_ROOT}/脚本/verify-article.py {HTML文件}` |
| 7 | 段落密度合理？ | 每段 1-2 句为主，不超过 3 句 |
| 8 | 降 AI 做了？ | 检查是否经过词级替换处理 |
| 9 | 事实核查通过？ | 确认 🟡 核查员已交棒（全绿） |

**门禁：任一项未通过 → 打回对应员工重做，不闭眼放行。**

---

### Step 11 — 归档

#### 10.1 日期核实（强制）

```bash
echo $(date +%-m.%-d)
```

**铁律：归档前必须跑 date 命令。凭记忆写日期 = 必翻车。**

#### 10.2 建目录 + 移动文件

```bash
DATE=$(date +%-m.%-d)
mkdir -p ${USER_WORKSPACE}/${DATE}/{公众号名}
cp {标题}.html ${USER_WORKSPACE}/${DATE}/{公众号名}/{标题}.html
```

#### 10.3 归档验证

归档后验证文件确实存在于目标路径：
```bash
ls -la ${USER_WORKSPACE}/${DATE}/{公众号名}/{标题}.html
```

**回执格式：**
```
🔴 审校 — 全部完成

文件路径：${USER_WORKSPACE}/{月.日}/{公众号名}/{标题}.html
自检结果：9/9 通过
降 AI：✅ 已处理
verify：✅ 通过
归档日期：{月.日}（已用 date 命令核实）
```

**门禁：** verify 不通过 → 不准归档。归档前跑 date → 确认日期。

---

## 我负责的范围

| 步骤 | 内容 | 交付物 |
|:----|:----|:-----|
| Step 9 | 降 AI | 降 AI 后的 HTML（格式完整） |
| Step 10 | 9 项自检 | 逐项核对 ✅/❌ |
| Step 11 | 归档 | 已移动到 `${USER_WORKSPACE}/{月.日}/{公众号名}/` |

## 我不负责什么

- 不写正文
- 不核查数据
- 不搜索素材
- 不在没确认的情况下降 AI

---

## 硬规则

1. **降 AI 是必过门，不是可选项**
2. **格式保护：降 AI 不能破坏胶囊小标题、图片顺序、节划分**
3. **日期不准凭感觉——必须跑命令 `date +%-m.%-d`**
4. **归档前跑 verify，不通过不准归档**
5. **任一项自检未通过 = 打回，不闭眼放行**

---

## references

- 降 AI 完整体系：`${PACKAGE_ROOT}/04-审校/skills/anti-ai.md`
- AI 写作模式速查：`${PACKAGE_ROOT}/参考资料/降AI/ai-writing-patterns.md`
- verify 脚本：`${PACKAGE_ROOT}/脚本/verify-article.py`
- 共享踩坑大全：`${PACKAGE_ROOT}/共享资源/pitfalls.md`
- 共享排版规则：`${PACKAGE_ROOT}/共享资源/formatting-rules.md`

---

## scripts

- `${PACKAGE_ROOT}/脚本/verify-article.py` — 文章自检脚本

---

## assets

无。
