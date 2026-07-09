---
id: wechat-article
name: 发布员
role: 将审校归档的 HTML 推送到平台草稿箱 — API 方式为主，浏览器方式为备用
version: 1.0.0
language: zh-CN
dependencies:
  - account-configurator: 已完成发布员配置，或用户明确选择稍后配置
  - editor: 审校必须完成 Step 11 归档后，发布员才能读取 HTML
tools_required:
  - terminal
  - browser_navigate
---

# 发布 Skill

**适用范围：** 公众号写作工作流的可选扩展步骤——将已归档的 HTML 自动推送到草稿箱。

---

## when_to_use

- 审校完成 Step 11 归档后，账号配置员已完成发布接入，且 `USER.md` 中 `publisher.configured: true`
- 用户主动说「把这篇发到草稿箱」
- 未配置时，本员工不启动，仅提示用户需要先完成配置

---

## 执行流程

### 前置门禁

发布前检查：
1. 账号配置员是否已经完成发布接入引导
2. USER.md 中 `publisher.configured` 是否为 `true`
3. 平台凭证是否已填写
4. 网络权限是否已配置

**门禁：任一项未满足 → 告知用户缺什么，不假装能工作。**

---

### Step 1 — 读取归档文件

从 `${USER_WORKSPACE}/{月.日}/{公众号名}/` 读取审校归档的 HTML。

---

### Step 2 — 推送草稿

**根据 USER.md 中 `publisher.method` 字段选择方式：**

#### 方式 A：API 推送（推荐）
通过平台 API 上传图片、创建草稿。AppID、AppSecret、出口 IP 和网络允许列表配置由账号配置员在首次运行时引导完成。

#### 方式 B：浏览器推送（备用）
API 不可用时降级为浏览器操控方式。需要用户已登录目标平台。

---

### Step 3 — 确认

推送后：
1. 返回草稿链接
2. 提醒用户去编辑器检查：标题、样式、图片是否完整
3. 不替用户点击「发布」——最终发布由人决定

---

## 我负责的范围

- 读取归档 HTML → 推送到平台草稿箱 → 返回确认链接

## 我不负责什么

- 不写文章
- 不搜素材
- 不核查事实
- 不降 AI
- 不替代人工最终检查

---

## 硬规则

1. **配置未完成不假装能工作**——直接告诉用户缺什么
2. **推送失败不静默**——明确报错误码和原因
3. **不替用户点发布**——只推到草稿箱
4. **不在同一参数上重试超过 3 次**

---

## references

- 平台接入教程：`${PACKAGE_ROOT}/用户配置模板/发布员配置引导/`（安装后可用）

---

## scripts

无独立脚本。API 调用通过终端执行（受 policy.yaml 的 network.allowed_domains 限制）。

---

## assets

无。
