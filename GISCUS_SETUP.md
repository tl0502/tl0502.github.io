# Giscus 评论系统配置指南

本博客已集成 Giscus 评论系统，这是一个基于 GitHub Discussions 的现代化评论解决方案。

## 🎯 为什么选择 Giscus？

- ✅ **完全免费** - 基于 GitHub Discussions，无需额外费用
- ✅ **数据自有** - 所有评论数据存储在您的 GitHub 仓库中
- ✅ **无广告** - 纯净的评论体验
- ✅ **支持 Markdown** - 评论支持完整的 Markdown 语法
- ✅ **GitHub 登录** - 使用 GitHub 账号登录，对开发者友好
- ✅ **多语言支持** - 支持中文界面
- ✅ **响应式设计** - 完美适配移动端和桌面端

## 📝 配置步骤

### 1️⃣ 启用 GitHub Discussions

1. 打开您的 GitHub 仓库：https://github.com/TVXL520/TVXL520.github.io
2. 点击 **Settings** 选项卡
3. 在 **Features** 部分，勾选 ✅ **Discussions**
4. 点击 **Set up discussions** 创建第一个 Discussion

### 2️⃣ 安装 Giscus App

1. 访问 https://github.com/apps/giscus
2. 点击 **Install** 按钮
3. 选择 **Only select repositories**
4. 选择 `TVXL520/TVXL520.github.io` 仓库
5. 点击 **Install** 完成安装

### 3️⃣ 获取配置参数

1. 访问 https://giscus.app/zh-CN
2. 在 **配置** 部分填写：
   - **仓库**：`TVXL520/TVXL520.github.io`
   - **页面 ↔️ discussion 映射关系**：选择 `pathname` （推荐）
   - **Discussion 分类**：选择 `Announcements` 或 `General`
   - **特性**：
     - ✅ 启用主评论区上方的反应
     - 如果需要，可以启用懒加载
   - **主题**：选择 `preferred_color_scheme` （自动适配浅色/深色模式）
   - **语言**：选择 `简体中文 (zh-CN)`

3. 向下滚动，您会看到生成的脚本，从中复制以下参数：
   ```html
   data-repo-id="..."
   data-category="..."
   data-category-id="..."
   ```

### 4️⃣ 更新配置文件

打开 `_config.yml` 文件，找到 Giscus 配置部分，填入您获取的参数：

```yaml
giscus:
  repo: TVXL520/TVXL520.github.io
  repo-id: R_kgDOxxxxxxx           # 从 giscus.app 复制
  category: Announcements            # 您选择的分类名称
  category-id: DIC_kwDOxxxxxxx      # 从 giscus.app 复制
  mapping: pathname
  reactions-enabled: 1
  emit-metadata: 0
  theme: preferred_color_scheme
  lang: zh-CN
```

### 5️⃣ 测试评论系统

1. 提交并推送更改到 GitHub：
   ```bash
   git add _config.yml
   git commit -m "配置 Giscus 评论系统"
   git push origin main
   ```

2. 等待 GitHub Actions 部署完成（约 1-2 分钟）

3. 访问您的博客任意文章页面，您应该能看到 Giscus 评论框

4. 使用您的 GitHub 账号登录并发布测试评论

## 🎨 主题自定义

Giscus 支持以下主题：

- `light` - 浅色主题
- `dark` - 深色主题
- `dark_dimmed` - 柔和深色主题
- `preferred_color_scheme` - **推荐**：自动跟随系统主题
- `transparent_dark` - 透明深色主题
- 自定义 CSS 主题

修改 `_config.yml` 中的 `theme` 参数即可切换。

## 🔧 高级配置

### 映射方式（mapping）

- `pathname`（推荐）- 使用页面路径作为映射键
- `url` - 使用完整 URL
- `title` - 使用页面标题
- `og:title` - 使用 Open Graph 标题

### 评论反应

设置 `reactions-enabled: 1` 可以让读者对评论添加表情反应（👍 ❤️ 😄 等）。

### 懒加载

Giscus 已配置为懒加载（`data-loading="lazy"`），只有当用户滚动到评论区时才加载，提升页面性能。

## 📚 更多资源

- [Giscus 官方文档](https://github.com/giscus/giscus/blob/main/ADVANCED-USAGE.md)
- [GitHub Discussions 文档](https://docs.github.com/zh/discussions)
- [Giscus 配置工具](https://giscus.app/zh-CN)

## ❓ 常见问题

### Q: 评论框不显示？
A: 检查以下项：
1. GitHub Discussions 是否已启用
2. Giscus App 是否已安装
3. `_config.yml` 中的参数是否正确填写
4. 浏览器控制台是否有错误信息

### Q: 如何管理评论？
A: 所有评论都在您的 GitHub 仓库的 Discussions 中，您可以：
- 在 Discussions 中回复、编辑、删除评论
- 锁定、解锁讨论
- 标记为已解决
- 使用 GitHub 的审核工具

### Q: 可以导入旧评论吗？
A: 可以通过 GitHub API 手动导入，但需要编写脚本。建议从新系统开始使用。

### Q: 如何禁用评论系统？
A: 在 `_config.yml` 中注释或删除 `giscus` 配置块即可。

---

配置完成后，享受现代化的评论体验吧！🎉
