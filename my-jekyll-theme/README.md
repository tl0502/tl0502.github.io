# my-jekyll-theme

这是从你现有的 Jekyll 站点（Hux blog 主题）快速生成的 WordPress 主题骨架。它并非完整自动转换器，而是一个起点，接下来你可以把资源和文章迁移到 WP。

快速使用说明

1. 将本文件夹 `my-jekyll-theme` 复制到你的 WordPress 安装目录 `wp-content/themes/` 下。
2. 把仓库中的静态资源复制到主题目录：
   - `css/bootstrap.min.css`, `css/hux-blog.min.css`, `css/syntax.css` -> `my-jekyll-theme/css/`
   - `js/jquery.min.js` (WP 自带 jQuery，可不复制), `js/bootstrap.min.js`, `js/hux-blog.min.js` -> `my-jekyll-theme/js/`
   - `img/` -> `my-jekyll-theme/img/`
3. 在 WordPress 后台启用主题（外观 → 主题）。
4. 在外观 → 菜单 中创建主菜单并分配为 "Primary Menu"。
5. 将 Jekyll 的文章导入到 WordPress：推荐把 `_posts/` 下的 Markdown 转成 WXR（WordPress XML）格式并使用 WordPress 的导入工具导入。可以使用第三方脚本（Python / Ruby / Node）来批量转换：保留标题、日期、分类、标签和正文。

注意事项与后续改进建议

- 目前主题模板是基础转换，可能需要调整 CSS 类和 HTML 结构以完全匹配原站样式。
- 建议添加主题选项用于配置社交链接、GA/百度统计 ID 等。
- 可以改进导入脚本以保留代码高亮、图片附件和自定义字段。

如果你希望，我可以：

- 帮你把 `_posts/` 自动转换成 WXR 格式的脚本（Python 或 Node），并生成可导入的 XML 文件；
- 把 `css/`, `js/`, `img/` 自动复制到主题目录并修正模板中的路径；
- 增强主题以支持小工具、侧边栏和主题自定义选项。
