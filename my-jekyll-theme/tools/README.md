Tools for migrating the Jekyll site into the WordPress theme.

- `convert_posts_to_wxr.py`: Convert `_posts/*.markdown` into `my-jekyll-theme/export/posts.wxr` (WordPress WXR XML).
- `copy_assets.py`: Copy `css`, `js`, and `img` from the project root into `my-jekyll-theme/`.
- `requirements.txt`: Python dependencies (PyYAML, Markdown).

Usage examples:

1. Create a virtualenv and install deps:

    python -m venv .venv
    .\.venv\Scripts\pip.exe install -r requirements.txt

2. Copy assets into theme:

    python copy_assets.py

3. Generate WXR:

    python convert_posts_to_wxr.py

After generating `posts.wxr`, use WordPress Admin -> Tools -> Import -> WordPress 导入该 XML 文件。
