#!/usr/bin/env python3
"""
Copy static asset folders (css, js, img) from project root into theme directory.

Usage:
    python copy_assets.py

This will copy ./css, ./js, ./img to my-jekyll-theme/css etc. Existing target folders will be overwritten.
"""
import os
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC_DIRS = ['css', 'js', 'img']
DEST_BASE = os.path.join(ROOT, 'my-jekyll-theme')


def copy_dir(name):
    src = os.path.join(ROOT, name)
    dst = os.path.join(DEST_BASE, name)
    if not os.path.isdir(src):
        print('Source not found:', src)
        return
    if os.path.exists(dst):
        print('Removing existing:', dst)
        shutil.rmtree(dst)
    print('Copying', src, '->', dst)
    shutil.copytree(src, dst)


def main():
    for d in SRC_DIRS:
        copy_dir(d)
    print('Assets copied to', DEST_BASE)


if __name__ == '__main__':
    main()
