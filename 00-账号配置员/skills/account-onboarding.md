---
id: account-onboarding
name: 账号配置引导
role: 公众号写作工作流第一步 — 配置账号、风格卡、私有 USER.md 与可选发布接入
version: 1.0.0
language: zh-CN
dependencies: []
tools_required:
  - terminal
  - browser_navigate
  - read_file
---

# 账号配置 Skill

**适用范围：** Agent 第一次加载本包、用户开始写作前、用户要求启用发布员或草稿推送能力时。

---

## when_to_use

- Agent 加载 `公众号写作员工包` 后的第一步
- 本地私有配置层不存在或 `USER.md` 未生成
- 用户说“配置账号”“启用发布员”“自动发到草稿箱”
- 发布员启动前发现 AppID、AppSecret、网络允许列表缺失

---

## 执行流程

### Step 0 — 说明配置目标

先告诉用户本步骤要完成三件事：

1. 写作账号配置：公众号名、工作区、风格卡
2. 发布能力选择：是否启用发布员
3. 如果启用发布员：准备 AppID、AppSecret、出口 IP 和平台允许列表

**门禁：** 用户确认继续后再进入具体配置。

### Step 1 — 生成本地私有配置

引导用户把 `${PACKAGE_ROOT}/私有配置模板/` 复制为本地私有配置层，并基于模板生成 `USER.md`。

`USER.md` 只存在用户本地，不进入公开包，不提交到 git。

### Step 2 — 配置写作账号和风格卡

要求用户在 `USER.md` 中填写：

- `workspace.base`
- `accounts.name`
- `accounts.style`
- `accounts.output_dir`

默认风格卡是 `${PACKAGE_ROOT}/共享资源/style.md`。它只是一个模板案例，用户后续可以复制并改成自己的自定义 style。

### Step 3 — 询问是否启用发布员

必须显式询问：

```
是否需要启用发布员，把审校后的文章推送到平台草稿箱？
```

- 用户选择否：记录 `publisher.configured: false`，直接交棒给素材捕手
- 用户选择是：进入 Step 4

### Step 4 — 引导获取开发者凭证

引导用户登录微信开发者平台或对应平台开发者后台，进入基础配置页面，获取：

- AppID
- AppSecret

要求用户只把值填入本地 `USER.md`，不要发到聊天窗口。

### Step 5 — 查询本机请求出口 IP

优先运行 `${PACKAGE_ROOT}/脚本/check-outbound-ip.py` 查询公网出口 IP。

如果运行时不允许联网，改为让用户手动打开 IP 查询网站，并把查到的地址填入 `USER.md`。

### Step 6 — 配置平台网络允许列表

引导用户在平台开发者后台把 Step 5 查到的出口 IP 加入允许列表。

完成后在 `USER.md` 中填写：

- `publisher.platform.request_ip`
- `publisher.platform.network_configured: true`

### Step 7 — 完成配置并交棒

如果用户启用发布员，确认以下字段存在：

- `publisher.platform.app_id`
- `publisher.platform.app_secret`
- `publisher.platform.request_ip`
- `publisher.platform.network_configured: true`

确认后交棒给素材捕手。发布员仍然只在审校完成后或用户主动要求“推送草稿”时启动。

---

## 我负责的范围

| 步骤 | 内容 | 交付物 |
|:----|:----|:-----|
| Step 0 | 说明配置目标 | 配置路线确认 |
| Step 1 | 生成本地私有配置 | 本地 `USER.md` |
| Step 2 | 写作账号和风格卡 | 账号/style 配置 |
| Step 3 | 发布能力选择 | 是否启用发布员 |
| Step 4 | 开发者凭证引导 | AppID/AppSecret 填写位置 |
| Step 5 | 出口 IP 查询 | 本机公网出口 IP |
| Step 6 | 网络允许列表 | 平台后台网络权限 |
| Step 7 | 配置检查 | 可进入写作流程 |

## 我不负责什么

- 不写文章
- 不推送草稿
- 不替用户最终发布
- 不读取用户未授权的密钥文件

---

## 硬规则

1. **配置账号必须是工作流第一步**，素材捕手不得绕过本步骤直接开始写作
2. **AppSecret 不进聊天、不进日志、不进公开包**
3. **发布员必须由用户显式启用**
4. **出口 IP 查询失败必须给出手动替代方法**

---

## references

- 私有配置模板：`${PACKAGE_ROOT}/私有配置模板/README.md`
- 发布员配置引导：`${PACKAGE_ROOT}/私有配置模板/发布员配置引导/`
- 默认风格卡：`${PACKAGE_ROOT}/共享资源/style.md`
- 风格卡字段说明：`${PACKAGE_ROOT}/共享资源/style-schema.md`

---

## scripts

- `${PACKAGE_ROOT}/脚本/check-outbound-ip.py` — 查询当前机器的公网出口 IP

---

## assets

本 skill 无独立 assets。
