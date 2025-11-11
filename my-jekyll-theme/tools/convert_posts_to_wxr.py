#!/usr/bin/env python3
"""
Convert Jekyll _posts/*.markdown files to a minimal WordPress WXR (XML) file.

Usage:
    python convert_posts_to_wxr.py

Output:
    my-jekyll-theme/export/posts.wxr

Notes:
 - Requires PyYAML and markdown (install with `pip install -r requirements.txt`)
 - This is a minimal converter: keeps title, date, content (converted to HTML), categories and tags if present.
"""
import os
import re
import sys
import shutil
import argparse
from datetime import datetime
import email.utils
import hashlib
import requests
from urllib.parse import urljoin, urlparse

try:
    import yaml
    import markdown
except Exception as e:
    print("Missing dependencies. Run: pip install -r requirements.txt")
    raise


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
POSTS_DIR = os.path.join(ROOT, '_posts')
OUT_DIR = os.path.join(ROOT, 'my-jekyll-theme', 'export')
OUT_FILE = os.path.join(OUT_DIR, 'posts.wxr')
UPLOADS_DIR = os.path.join(OUT_DIR, 'uploads')

# Default site URL used to build attachment URLs in the WXR. Can be overridden by --site-url.
DEFAULT_SITE_URL = 'http://example.com'


def parse_post(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', text, re.S)
    if not m:
        # no front matter
        metadata = {}
        body = text
    else:
        fm, body = m.group(1), m.group(2)
        metadata = yaml.safe_load(fm) or {}

    # convert markdown to html
    html = markdown.markdown(body)

    title = metadata.get('title') or os.path.splitext(os.path.basename(path))[0]
    date = metadata.get('date')
    if isinstance(date, datetime):
        dt = date
    elif isinstance(date, str):
        try:
            dt = datetime.fromisoformat(date)
        except Exception:
            # fallback: try parsing date part only
            try:
                dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            except Exception:
                try:
                    dt = datetime.strptime(date, '%Y-%m-%d')
                except Exception:
                    dt = datetime.now()
    else:
        dt = datetime.now()

    categories = metadata.get('categories') or metadata.get('category') or []
    if isinstance(categories, str):
        categories = [categories]
    tags = metadata.get('tags') or []
    if isinstance(tags, str):
        tags = [tags]

    slug = metadata.get('permalink') or os.path.splitext(os.path.basename(path))[0]

    return {
        'title': title,
        'date': dt,
        'content': html,
        'categories': categories,
        'tags': tags,
        'slug': slug,
    }


def make_wxr(items, attachments=None):
    header = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    header += '<rss version="2.0" xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" '
    header += 'xmlns:content="http://purl.org/rss/1.0/modules/content/" '
    header += 'xmlns:wfw="http://wellformedweb.org/CommentAPI/" '
    header += 'xmlns:dc="http://purl.org/dc/elements/1.1/" '
    header += 'xmlns:wp="http://wordpress.org/export/1.2/">\n'
    header += '<channel>\n'
    header += '<title>Converted from Jekyll</title>\n'
    header += '<link>http://example.com/</link>\n'
    header += '<description>Exported by convert_posts_to_wxr.py</description>\n'

    body = ''

    # first render attachment items (so importer can create them before posts)
    if attachments:
        for a in attachments:
            pubDate = email.utils.format_datetime(a['date']) if hasattr(email.utils, 'format_datetime') else a['date'].strftime('%a, %d %b %Y %H:%M:%S +0000')
            title = escape_xml(a['title'])
            url = a['url']
            item = '  <item>\n'
            item += f'    <title>{title}</title>\n'
            item += f'    <link>{url}</link>\n'
            item += f'    <pubDate>{pubDate}</pubDate>\n'
            item += '    <dc:creator><![CDATA[author]]></dc:creator>\n'
            item += f'    <guid isPermaLink="false">{url}</guid>\n'
            item += '    <description></description>\n'
            item += '    <content:encoded><![CDATA[]]></content:encoded>\n'
            item += f'    <wp:post_date>{a["date"].strftime("%Y-%m-%d %H:%M:%S")}</wp:post_date>\n'
            item += '    <wp:post_type>attachment</wp:post_type>\n'
            item += f'    <wp:attachment_url>{url}</wp:attachment_url>\n'
            item += '  </item>\n'
            body += item

    for it in items:
        pubDate = email.utils.format_datetime(it['date']) if hasattr(email.utils, 'format_datetime') else it['date'].strftime('%a, %d %b %Y %H:%M:%S +0000')
        title = escape_xml(it['title'])
        content = it['content']
        slug = escape_xml(it['slug'])

        item = '  <item>\n'
        item += f'    <title>{title}</title>\n'
        item += f'    <link>http://example.com/{slug}</link>\n'
        item += f'    <pubDate>{pubDate}</pubDate>\n'
        item += '    <dc:creator><![CDATA[author]]></dc:creator>\n'
        # categories and tags
        for c in it['categories']:
            item += f'    <category domain="category" nicename="{escape_xml(c)}"><![CDATA[{escape_xml(c)}]]></category>\n'
        for t in it['tags']:
            item += f'    <category domain="post_tag" nicename="{escape_xml(t)}"><![CDATA[{escape_xml(t)}]]></category>\n'
        item += f'    <guid isPermaLink="false">http://example.com/{slug}</guid>\n'
        item += '    <description></description>\n'
        item += f'    <content:encoded><![CDATA[{content}]]></content:encoded>\n'
        item += f'    <wp:post_date>{it["date"].strftime("%Y-%m-%d %H:%M:%S")}</wp:post_date>\n'
        item += '    <wp:post_type>post</wp:post_type>\n'
        item += '  </item>\n'
        body += item

    footer = '</channel>\n</rss>\n'
    return header + body + footer


def find_image_urls(html):
    # find src="..." and src='...'
    urls = []
    for m in re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', html, re.I):
        urls.append(m)
    return urls


def download_image(img_url, post_date, site_url):
    # img_url may be absolute, protocol-relative (//), or root-relative (/img/...), or relative path
    parsed = urlparse(img_url)
    if parsed.scheme in ('http', 'https'):
        full_url = img_url
    elif img_url.startswith('//'):
        full_url = 'http:' + img_url
    elif img_url.startswith('/'):
        # try local file first (project root + path)
        local_candidate = os.path.join(ROOT, img_url.lstrip('/'))
        if os.path.isfile(local_candidate):
            with open(local_candidate, 'rb') as f:
                data = f.read()
            return data, os.path.basename(local_candidate)
        full_url = urljoin(site_url, img_url)
    else:
        # treat as relative to project root
        # e.g., img/in-post/foo.png -> file at ROOT/img/in-post/foo.png
        candidate = os.path.join(ROOT, img_url.lstrip('./'))
        if os.path.isfile(candidate):
            # we'll read from file instead of HTTP
            with open(candidate, 'rb') as f:
                data = f.read()
            return data, os.path.basename(candidate)
        else:
            full_url = urljoin(site_url + '/', img_url)

    try:
        r = requests.get(full_url, timeout=15)
        r.raise_for_status()
        data = r.content
        filename = os.path.basename(urlparse(full_url).path)
        if not filename:
            # fallback to hash
            filename = hashlib.sha1(data).hexdigest()[:10]
        return data, filename
    except Exception:
        return None, None


def enhance_items_with_attachments(items, site_url):
    # For each post, find images, download and create attachment items, and update post content URLs
    attachments = []
    os.makedirs(UPLOADS_DIR, exist_ok=True)

    for it in items:
        imgs = find_image_urls(it['content'])
        for img in imgs:
            data, fn = download_image(img, it['date'], site_url)
            if not data or not fn:
                # failed to download, skip
                continue

            # store under year/month folder
            ym = it['date'].strftime('%Y/%m')
            dest_dir = os.path.join(UPLOADS_DIR, ym)
            os.makedirs(dest_dir, exist_ok=True)
            # avoid name collisions
            dest_name = fn
            dest_path = os.path.join(dest_dir, dest_name)
            # if exists, append hash
            if os.path.exists(dest_path):
                h = hashlib.sha1(data).hexdigest()[:8]
                name, ext = os.path.splitext(dest_name)
                dest_name = f"{name}-{h}{ext}"
                dest_path = os.path.join(dest_dir, dest_name)

            with open(dest_path, 'wb') as f:
                f.write(data)

            # construct attachment URL (assume wp uploads path)
            upload_rel = f"/wp-content/uploads/{ym}/{dest_name}"
            attach_url = site_url.rstrip('/') + upload_rel

            # replace occurrences in content (both absolute and relative forms)
            it['content'] = it['content'].replace(img, attach_url)

            # create attachment item
            attachments.append({
                'title': dest_name,
                'url': attach_url,
                'file': f"{ym}/{dest_name}",
                'date': it['date']
            })

    return attachments


def escape_xml(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;').replace("'", '&apos;'))


def main():
    parser = argparse.ArgumentParser(description='Convert Jekyll posts to WXR')
    parser.add_argument('--site-url', default=DEFAULT_SITE_URL, help='Base site URL used for building attachment URLs')
    args = parser.parse_args()

    if not os.path.isdir(POSTS_DIR):
        print('No _posts directory found at', POSTS_DIR)
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)

    posts = []
    for fname in sorted(os.listdir(POSTS_DIR)):
        if fname.lower().endswith(('.md', '.markdown')):
            path = os.path.join(POSTS_DIR, fname)
            print('Parsing', path)
            posts.append(parse_post(path))

    # download images and generate attachment items
    attachments = enhance_items_with_attachments(posts, args.site_url)

    wxr = make_wxr(posts, attachments=attachments)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(wxr)

    print('WXR written to', OUT_FILE)


if __name__ == '__main__':
    main()
