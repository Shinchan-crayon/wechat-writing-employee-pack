# 风格卡字段定义（Style Schema）

本文档定义写作风格卡的标准字段结构。任何风格卡（包括 `style.md` 模板和用户自定义的）都应遵循此结构。

adapter 按此 schema 解析风格卡，将规则注入对应员工的 prompt。

## 字段总览

| 字段 | 类型 | 必填 | 说明 |
|------|------|:---:|------|
| `meta` | object | ✅ | 风格卡元信息 |
| `title` | object | ✅ | 标题规则 |
| `summary` | object | ✅ | 摘要规则 |
| `opening` | object | ✅ | 开头规则 |
| `body` | object | ✅ | 正文结构规则 |
| `language` | object | ✅ | 语言风格规则 |
| `formatting` | object | ✅ | 排版规则 |
| `banned` | object | ✅ | 禁用规则 |
| `checklist` | array | ✅ | 交稿前检查清单 |

---

## meta

```yaml
meta:
  name: "默认犀利风"            # 风格名称
  description: "适合科技/财经类公众号，说话犀利、短句、有网感"  # 一句话描述
  suitable_for:                 # 适用场景
    - "科技行业分析"
    - "财经热点解读"
    - "产品评测"
  unsuitable_for:               # 不适合的场景
    - "学术论文"
    - "官方公告"
```

## title

```yaml
title:
  min_length: 12                # 最短字数（中文=1字，英文每3字母=1字）
  max_length: 20                # 最长字数
  style:                        # 标题风格要求
    - "情绪钩子 + 核心事件"
    - "自带冲突感"
    - "不用纯资讯播报标题"
  banned_patterns:              # 禁止的标题模式
    - "问号结尾但没有悬念"
    - "纯情绪词没有信息增量"
    - "像新闻标题（只陈述事实）"
  examples:                     # 正确示例
    good:
      - "谷歌扬言破解比特币只需要9分钟，CZ急了"
      - "太狠了，这家公司一口气裁了四成人"
    bad:
      - "某公司发布新产品"        # 纯资讯，没钩子
```

## summary

```yaml
summary:
  min_length: 10
  max_length: 15
  rule: "补充标题未说完的信息，给判断或悬念，不重复标题"
```

## opening

```yaml
opening:
  strategies:                   # 可用开头方式（按推荐顺序）
    - "情绪切入"
    - "问题切入"
    - "判断切入"
    - "场景切入"
  goal: "第一段先把人拉进来，再补背景"
  banned_openings:              # 禁止的开头方式
    - "近日……"
    - "随着……"
    - "在当前背景下……"
    - "值得注意的是……"
    - "本文将……"
```

## body

```yaml
body:
  word_count:                   # 字数范围
    min: 700
    max: 1000
  paragraph_rule: "每段1-2句，超过3句检查是否流水账"
  sentence_max: 27              # 单句字数上限
  structure_templates:          # 结构模板（至少提供一种）
    - name: "热点解读型"
      steps:
        - "先把事件扔出来"
        - "讲事情怎么走到这一步"
        - "讲它真正离谱/重要的地方"
        - "讲读者真正该看的变量"
        - "最后给扎心判断或提醒"
    - name: "教程型"
      steps:
        - "1-2段用事件做引子"
        - "按操作步骤展开（每步一个小标题）"
        - "收束升华 + 评论区互动钩子"
  principles:
    - "文章要像'往下讲'，不要像'往下列'"
    - "每篇至少有一条明确主线"
    - "中间要有1-2次结构转折"
    - "结尾必须有收束判断"
```

## language

```yaml
language:
  tone:                          # 语气描述
    - "像聊天，不像总结"
    - "多短句，少长句"
    - "允许反问、轻吐槽、抽象幽默"
  allowed_expressions:           # 允许的语气
    - "这味道不对"
    - "这事离谱就离谱在……"
    - "看到这一步就知道不正常了"
  banned_expressions:            # 禁止的语气
    - "书面汇报腔"
    - "机械教学腔"
    - "假大空判断"
    - "情绪发泄文"
  explanation_rule: "复杂概念必须翻译成人话"
```

## formatting

```yaml
formatting:
  paragraph_spacing: "1.6倍行距"
  font_size: "17px"
  text_color: "#3f3f3f"
  subsection_style:              # 小标题样式
    type: "胶囊式"
    format: "「口语化标题」"
    css:
      background: "#8B2E2E"
      color: "#ffffff"
      padding: "6px 24px"
      border-radius: "50px"
  highlight_rule:                # 标红规则
    css: "color:#a93226; font-weight:bold"
    targets:
      - "核心数字"
      - "关键判断"
      - "产品名/模型名"
    max_per_article: 15
  sentence_ending: "陈述句尾不加句号，问句保留问号，感叹句保留感叹号"
  banned_formatting:
    - "项目符号列表（- 或 1. 2. 3.）"
    - "分隔线（---）"
```

## banned

```yaml
banned:
  words:                          # 禁用词列表（此字段引用 banned-words.md）
    ref: "共享资源/banned-words.md"
  patterns:                       # 禁用句型
    - "不是……而是……"
    - "从来不是……而是……"
    - "看着像……其实是……"
    - "如果……那……"
    - "真正……（如'真正麻烦的地方'）"
  glue_words:                     # 胶水词限用（每篇最多1次）
    - "说白了"
    - "你会发现"
    - "某种程度上"
    - "归根结底"
  filler_phrases:                 # 填充短语（完全禁用）
    - "值得注意的是"
    - "不容忽视的是"
    - "从某种意义上说"
    - "这充分说明了"
  structural_banned:              # 结构禁用
    - "首先/其次/最后"
    - "第一/第二/第三"
    - "背景→事件→原因→影响→结论 线性骨架"
```

## checklist

```yaml
checklist:                        # 交稿前强制逐项检查
  - item: "字数在范围内"
  - item: "小标题是口语化「」胶囊式，不是编号目录式"
  - item: "陈述句尾去掉了句号"
  - item: "没有项目符号列表"
  - item: "没有禁用对照句型"
  - item: "没有禁用词命中"
  - item: "段落密度合理（每段1-2句，不碎不密）"
  - item: "HTML 胶囊 CSS 完整"
  - item: "日期正确（用 date 命令确认）"
```
