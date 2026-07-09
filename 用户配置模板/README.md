# USER.md 模板

> ⚠️ 此目录是公开包中的安装模板，只说明本地 `USER.md` 应该怎么生成。
> 真实 `USER.md`、账号映射、工作区路径、凭证和私密偏好只能安装后生成到用户本地配置，
> 不进入公开包、不提交到 git。

---

## 用户信息

```yaml
user:
  name: "你的名字"
  role: "公众号运营者"
```

## 工作空间

所有员工的读写范围限定在此目录下。

```yaml
workspace:
  base: "${USER_HOME}/Documents/wechat-writing-workspace"    # 归档根目录
  runtime: "${USER_HOME}/Documents/wechat-writing-workspace/runtime"  # 中间文件目录
```

## 账号配置

每行一个公众号，指向对应的风格卡。

```yaml
accounts:
  - name: "你的公众号名"
    style: "${PACKAGE_ROOT}/共享资源/style.md"         # 指向你的风格卡（可复制模板修改）
    output_dir: "你的公众号名"
```

`共享资源/style.md` 只是包内提供的一份写作风格模板。你可以复制它，改成自己的风格卡，再把 `accounts.style` 指向新文件。

## 员工专属配置

### 素材捕手

```yaml
scout:
  search_engine: "x"                    # x | duckduckgo | google
  source_language: "zh"                 # 源素材语言偏好
  chrome_debug_port: 9222
  chrome_profile: "${USER_PRIVATE_CONFIG}/browser-profile"
```

### 事实核查员

```yaml
fact_checker:
  source_hierarchy:
    - "公司财报/IR/官方公告"
    - "权威媒体（路透、彭博、财新）"
    - "行业媒体"
  conversion_tool: "python3"            # 换算用工具
```

### 写手

```yaml
writer:
  default_word_count:
    min: 700
    max: 1000
```

### 审校

```yaml
editor:
  deai_method: "manual"                 # manual | external_tool
```

### 发布员（可选）

仅当启用发布员时才需填写。配置完成后将 `configured` 设为 `true`。

```yaml
publisher:
  configured: false                     # 完成所有配置后改为 true

  platform:
    name: "wechat"                       # 平台名称
    app_id: ""                           # AppID，只填在本地 USER.md
    app_secret: ""                       # AppSecret，只填在本地 USER.md，不要提交到 git
    api_domain: ""                        # 平台 API 域名，例如 api.example.com
    web_domain: ""                        # 平台后台域名，例如 console.example.com
    request_ip: ""                        # 本机公网出口 IP
    request_ip_checked_at: ""             # 查询时间，可留空
    network_configured: false            # 网络权限是否配置完成

  publish:
    auto_push_on_archive: false         # 归档后是否自动推送
    verify_in_editor: true              # 推送后是否提醒人工检查
    method: "api"                       # api | browser
```

---

## 变量说明

安装脚本或 adapter 在加载时解析以下变量：

| 变量 | 说明 |
|------|------|
| `${USER_HOME}` | 用户主目录 |
| `${USER_WORKSPACE}` | 用户工作区（从 workspace.base 注入） |
| `${PACKAGE_ROOT}` | 本员工包的安装目录 |
