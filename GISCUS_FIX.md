# Giscus 错误修复指南

## ❌ 错误信息
```
giscus is not installed on this repository
```

## 🔍 问题原因
您的 `_config.yml` 中 Giscus 配置参数未完成填写，导致 Giscus 无法正常工作。

---

## ✅ 完整修复步骤

### 步骤 1：启用 GitHub Discussions ⭐

1. **访问仓库设置页面**
   ```
   https://github.com/TVXL520/TVXL520.github.io/settings
   ```

2. **向下滚动到 "Features" 部分**

3. **勾选 "Discussions" 复选框**
   - 如果已经勾选，说明已启用 ✅
   - 如果未勾选，请勾选它

4. **点击 "Set up discussions" 按钮**（如果是首次启用）
   - 这会自动创建第一个 Discussion
   - 您可以看到一个欢迎讨论帖

5. **确认 Discussions 已启用**
   - 在仓库顶部应该能看到 "Discussions" 选项卡
   - 访问：https://github.com/TVXL520/TVXL520.github.io/discussions

---

### 步骤 2：安装 Giscus App ⭐⭐

1. **访问 Giscus App 安装页面**
   ```
   https://github.com/apps/giscus
   ```

2. **点击绿色的 "Install" 按钮**

3. **选择安装位置**
   - 选项 1：All repositories（所有仓库）
   - **选项 2：Only select repositories**（推荐 ✅）

4. **如果选择"Only select repositories"**
   - 在下拉菜单中选择：`TVXL520/TVXL520.github.io`
   - 勾选该仓库

5. **点击绿色的 "Install" 按钮**

6. **确认安装成功**
   - 您会被重定向到确认页面
   - 可以访问：https://github.com/settings/installations
   - 应该能看到 "giscus" 已安装

---

### 步骤 3：获取配置参数 ⭐⭐⭐

1. **访问 Giscus 配置网站**
   ```
   https://giscus.app/zh-CN
   ```

2. **填写"配置"部分**

   **a. 语言**
   - 在页面顶部选择：`简体中文`

   **b. 仓库**
   - 输入：`TVXL520/TVXL520.github.io`
   - 如果配置正确，会显示 ✅ "成功！此仓库满足所有条件。"
   - 如果显示错误，请检查步骤 1 和 2 是否完成

   **c. 页面 ↔️ discussion 映射关系**
   - 选择：`pathname`
   - 说明：使用页面的路径名作为映射

   **d. Discussion 分类**
   - 推荐选择：`Announcements`
   - 或者选择：`General`
   - **重要**：记下您选择的分类名称！

   **e. 特性**
   - ✅ 启用主评论区上方的反应
   - ✅ 懒加载评论（可选，推荐）

   **f. 主题**
   - 选择：`preferred_color_scheme`
   - 说明：自动跟随系统的浅色/深色模式

3. **向下滚动到"启用 giscus"部分**

   您会看到类似这样的脚本：
   ```html
   <script src="https://giscus.app/client.js"
           data-repo="TVXL520/TVXL520.github.io"
           data-repo-id="R_kgDONMabcd12345"              ← 复制这个！
           data-category="Announcements"                  ← 复制这个！
           data-category-id="DIC_kwDONMabcd12345"        ← 复制这个！
           data-mapping="pathname"
           ...
   </script>
   ```

4. **复制以下三个参数**（非常重要！）
   - `data-repo-id` 的值，例如：`R_kgDONMabcd12345`
   - `data-category` 的值，例如：`Announcements`
   - `data-category-id` 的值，例如：`DIC_kwDONMabcd12345`

---

### 步骤 4：更新 _config.yml ⭐⭐⭐

打开您的 `_config.yml` 文件，找到第 55-64 行的 Giscus 配置：

**替换前：**
```yaml
giscus:
  repo: TVXL520/TVXL520.github.io
  repo-id: # Get from https://giscus.app
  category: # Discussions category name
  category-id: # Get from https://giscus.app
  mapping: pathname
  reactions-enabled: 1
  emit-metadata: 0
  theme: preferred_color_scheme
  lang: zh-CN
```

**替换后：**（使用您从步骤 3 复制的值）
```yaml
giscus:
  repo: TVXL520/TVXL520.github.io
  repo-id: R_kgDONMabcd12345              # ← 粘贴您复制的值
  category: Announcements                  # ← 粘贴您选择的分类
  category-id: DIC_kwDONMabcd12345        # ← 粘贴您复制的值
  mapping: pathname
  reactions-enabled: 1
  emit-metadata: 0
  theme: preferred_color_scheme
  lang: zh-CN
```

**⚠️ 注意：**
- 确保没有多余的空格
- 确保值两边没有引号（除非原本就有）
- 保持缩进一致（2个空格）

---

### 步骤 5：提交并重新部署 ⭐

1. **保存 _config.yml 文件**

2. **提交更改**
   ```bash
   git add _config.yml
   git commit -m "配置 Giscus 评论系统参数"
   git push origin main
   ```

3. **等待 GitHub Actions 部署**
   - 访问：https://github.com/TVXL520/TVXL520.github.io/actions
   - 等待最新的工作流运行完成（通常 1-2 分钟）
   - 确保显示绿色 ✅ 表示成功

4. **测试评论系统**
   - 访问您的博客任意文章页面
   - 向下滚动到评论区
   - 应该能看到 Giscus 评论框
   - 点击 "Sign in with GitHub" 测试发表评论

---

## 🔧 故障排查

### 问题 1：仍然显示 "giscus is not installed"
**可能原因：**
- Giscus App 未正确安装
- 安装时没有选择正确的仓库

**解决方案：**
1. 访问：https://github.com/settings/installations
2. 找到 "giscus"
3. 点击 "Configure"
4. 确保 `TVXL520/TVXL520.github.io` 在允许列表中

---

### 问题 2：配置页面显示错误
**错误信息：** "The repository does not have Discussions enabled"

**解决方案：**
1. 重新检查步骤 1
2. 确保 Discussions 已启用
3. 访问：https://github.com/TVXL520/TVXL520.github.io/discussions
4. 应该能看到 Discussions 页面

---

### 问题 3：找不到分类
**错误信息：** "Discussion category not found"

**解决方案：**
1. 访问：https://github.com/TVXL520/TVXL520.github.io/discussions
2. 点击右侧的 "Categories"
3. 查看可用的分类
4. 确保 _config.yml 中的 `category` 名称与实际分类名称完全一致

---

### 问题 4：参数看起来不对
**检查清单：**
- [ ] `repo-id` 应该以 `R_` 开头
- [ ] `category-id` 应该以 `DIC_` 开头
- [ ] `category` 应该是纯文本（如 `Announcements`）
- [ ] 没有多余的空格或引号

---

## 📞 需要帮助？

如果完成步骤 1-3 后遇到问题，请提供以下信息：

1. **Giscus App 是否已安装？**
   - 访问：https://github.com/settings/installations
   - 截图或确认是否看到 "giscus"

2. **Discussions 是否已启用？**
   - 访问：https://github.com/TVXL520/TVXL520.github.io/discussions
   - 能否正常访问？

3. **Giscus 配置页面显示什么？**
   - 访问：https://giscus.app/zh-CN
   - 输入仓库后显示什么消息？
   - 截图配置页面

---

## ✅ 成功标志

配置成功后，您应该看到：

1. ✅ 博客文章页面底部显示 Giscus 评论框
2. ✅ 可以点击 "Sign in with GitHub" 登录
3. ✅ 发表的评论会自动同步到 GitHub Discussions
4. ✅ 评论框样式与博客主题协调

---

**完成这些步骤后，Giscus 评论系统就能正常工作了！** 🎉
