# Secret scanning 安全测试样例

本仓库用于体验 GitHub Secret scanning（凭据扫描）和 Push protection（推送保护）。所有样例都是公开测试数据，不包含真实账号凭据，也不调用外部服务。

## 样例与预期

| 文件 | 内容 | 预期与前提 |
| --- | --- | --- |
| `github-dummy.env` | GitHub 官方专用 dummy token | 用于验证内置检测和提交时的 Push protection |
| `hardcoded-client.py` | 同一 dummy token 的代码硬编码写法 | 用于比较配置文件与源代码中的检测；不发送请求、不打印 token |
| `application-demo.yml` | 虚构数据库密码、内部格式 token | 普通密码需额外的 AI 检测或适当自定义规则；内部 token 需手动发布自定义规则 |
| `environment-only.py` | 只从环境变量读取凭据 | 负例：没有提交凭据值，不应因环境变量名称本身产生凭据泄露告警 |

相同 token 出现在多个文件时，GitHub 可能归并为一个告警，并显示多个位置，因此不应按文件数推算告警数。

## 测试步骤

1. 在仓库 **Settings → Advanced Security** 查看 Secret scanning / Secret Protection 和 Push protection 的可用状态。公开仓库提供基础凭据扫描；具体功能以账号及仓库设置为准。
2. 提交 dummy token 文件。若出现 **GitHub Secret Scanning secret** 的拦截提示，已经成功验证 Push protection；文件可能因此尚未进入仓库，无需关闭保护来证明检测生效。
3. 对已成功提交的样例，在仓库 **Security and quality → Secret scanning** 查看检测结果。扫描异步执行，本样例不承诺告警数量或生成时限。
   如果放行理由选择 **It's used in tests**，GitHub 会自动关闭该测试告警，请同时查看 **Closed**。同一 token 已有告警后，再次提交它可能不再被拦截。
4. `application-demo.yml` 中的内部 token 可使用以下自定义规则：

   ```regex
   antdemo_[0-9a-f]{32}
   ```

   将其填入自定义规则的 **Secret format**，前后边界保留默认值，先 **Save and dry run**，再按需要发布。提交文件不会自动创建或启用任何规则。普通个人仓库可能没有自定义规则或 AI 检测功能；当前官方自定义规则要求组织所属仓库、Team/Enterprise 及 Secret Protection。

不要将这些测试值替换为真实凭据。随机拼接一个看似真实的服务商 token 并不保证命中，不能据此判定扫描失效。

## 官方参考

- [安全提交 dummy token 的官方练习](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#2-committing-a-dummy-token)
- [Secret scanning 的可用范围和检测方式](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)
- [创建自定义检测规则](https://docs.github.com/en/code-security/how-tos/secure-your-secrets/customize-leak-detection/define-custom-patterns)
- [启用推送保护](https://docs.github.com/en/code-security/how-tos/secure-your-secrets/prevent-future-leaks/enable-push-protection)
