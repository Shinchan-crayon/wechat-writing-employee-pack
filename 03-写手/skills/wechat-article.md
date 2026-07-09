---
id: wechat-article
name: 主笔
role: 公众号写作工作流 Step 6-7 — 拿核查通过的数据和框架，按模板写 HTML + 调 title-generator 出标题
version: 1.0.0
language: zh-CN
dependencies:
  - content-scout: 素材捕手必须完成 Step 4 交棒（提供框架和素材简报）
  - fact-checker: 事实核查员必须完成 Step 5 交棒（核查表全绿）
  - title-generator: Step 7 标题生成依赖本包内的 title-generator skill
tools_required:
  - read_file
  - write_file
  - terminal
  - patch
---

# 主笔 Skill（Step 6-7）

**适用范围：** 公众号写作工作流的核心写稿环节——把框架和数据变成一篇完整的 HTML 文章。

---

## when_to_use

- 收到 🟡 事实核查员的交棒（核查表全绿 + 素材简报 + 结构框架）
- 前置条件：素材框架已确认、数据核查表全绿

---

## 执行流程

### 前置门禁

**拿到以下三项才能动笔，缺一不可：**
1. 🟢 素材捕手的结构框架（角度 + 分节规划）
2. 🟡 事实核查员的核查表（全绿）
3. 已锁定的账号和 style

**门禁：未收到核查通过的框架和数据核查表 → 不得动笔。**

---

### Step 6 — 写正文

#### 5.1 加载资源

动笔前先读取以下文件：
- HTML 模板：`${PACKAGE_ROOT}/模板/article.html`
- 账号风格卡：`${PACKAGE_ROOT}/共享资源/style.md` 或本地 USER.md 中 `accounts.style` 指向的自定义风格卡
- 共享禁用词：`${PACKAGE_ROOT}/共享资源/banned-words.md`
- 共享排版规则：`${PACKAGE_ROOT}/共享资源/formatting-rules.md`

#### 5.2 写作规则

**模板规则：**
- HTML 必须从 `${PACKAGE_ROOT}/模板/article.html` 骨架复制，替换标题/摘要/正文，**禁止从零手写 HTML**
- 胶囊 CSS 不能丢：`.titlestyle span` 必须含 `padding:6px 24px; border-radius:50px;`

**风格规则（按当前 style 执行）：**
- 标题长度、语气、句式优先遵循 style
- 开头方式遵循 style（情绪切入/问题切入/判断切入）
- 正文段落数、句长、断句节奏以 style 为准
- 禁用词以 `banned-words.md` + style 专属禁用词为准

**通用底线：**
- 首段先进入主题，不要大段背景铺垫
- 每节只讲一个核心点
- 节与节之间必须有逻辑递进
- 关键数据用 `<span class="hl">` 标红
- 陈述句段尾默认不加句号，问句/感叹句保留标点
- 每段 1-2 句，一段不超过 3 句

**默认无配图：**
- 所有文章默认不配图
- 从模板中删除 `<div class="img-wrap">` 等图片容器
- 仅当用户明确说"加图""配图"时才执行配图

**原创 vs 重写模式：**
- 模式 A（有锚重写）：用户给了完整文章需要改写 → 以原文节奏为参考，做角度调整 + 风格适配
- 模式 B（无锚原创）：用户给了大纲/散点/关键词 → 先写极短初稿（2-3 自然段聊天语气）确认方向，再展开

#### 5.3 格式自检

写完正文后，逐项检查：
1. HTML 文件存在？（不在对话框，在磁盘上）
2. 是用模板改的？（不是从零手写）
3. 胶囊 CSS 完整？（`padding:6px 24px; border-radius:50px;`）
4. 从模板中删除了 img-wrap？（默认无配图）

#### 5.4 跑 verify 脚本

```bash
cd ${PACKAGE_ROOT}/03-写手
python3 ${PACKAGE_ROOT}/脚本/verify-article.py {HTML文件路径}
```

**门禁：verify 不通过 → 不准交棒。**

---

### Step 7 — 出标题

正文完成后，调同包内的 `title-generator` skill 生成标题候选。

**执行流程：**
1. 加载 `skills/title-generator.md`
2. 传入正文全文，生成 3-5 个标题候选（悬念型/利益型/观点型各至少 1 个）
3. 选推荐款回填到 HTML 的 `<title>` 和 `<h1 class="title">` 中
4. 发给用户确认标题

**英文字母计数规则：** 标题中每 3 个英文字母折算为 1 个汉字。

**回执格式：**
```
🔵 主笔 — 正文完成

文件路径：${USER_WORKSPACE}/{月.日}/{公众号名}/{标题}.html

标题候选：
1. [推荐] {标题1}
2. {标题2}
3. {标题3}

verify 结果：✅ 通过 / ❌ 未通过

请确认主标题。
```

**门禁：** 标题必须等用户确认 + verify 通过 → 才交棒给 🔴 审校。

---

## 我负责的范围

| 步骤 | 内容 | 交付物 |
|:----|:----|:-----|
| Step 6 | 写正文 | HTML 文件（按模板骨架，verify 通过） |
| Step 7 | 出标题 | 3-5 个标题候选（含推荐款） |

## 我不负责什么

- 不搜索素材（那是素材捕手的事）
- 不核查数据（事实核查员会在 Step 5 和 Step 8 处理）
- 不做事实核查（那是事实核查员 Step 8 的事）
- 不降 AI（那是审校的事）
- 不归档文件（那是审校的事）

---

## 硬规则

1. **没有核查通过的框架 = 不动笔**
2. **HTML 必须从模板改，不从零手写**
3. **胶囊 CSS（padding:6px 24px; border-radius:50px;）不能丢**
4. **写完必须跑 verify，不通过不准交棒**
5. **标题必须等用户确认，不自己定**

---

## references

- HTML 模板：`${PACKAGE_ROOT}/模板/article.html`
- 风格卡：`${PACKAGE_ROOT}/共享资源/style.md` 或本地 USER.md 中 `accounts.style` 指向的自定义风格卡
- 标题公式库：`${PACKAGE_ROOT}/参考资料/标题生成/title-formulas.md`
- 共享写作风格：`${PACKAGE_ROOT}/共享资源/style.md`
- 共享禁用词：`${PACKAGE_ROOT}/共享资源/banned-words.md`
- 共享排版规则：`${PACKAGE_ROOT}/共享资源/formatting-rules.md`

---

## scripts

- `${PACKAGE_ROOT}/脚本/verify-article.py` — 文章自检脚本

---

## assets

无独立 assets。HTML 模板见 references。
