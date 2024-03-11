import os
import re
from oqhlib.utils import get_category_name

# Generates a page in HTML format
def html(header, items):
    """
    Generates a page in HTML format
    """
    
    nl = "\n  "
    ext = ".html"
    text = f"""<!DOCTYPE html>
<html>
<body>
<h2>{header}</h2>
<p>
  {nl.join(map(lambda i: f'<li><a href="{i["url"]}">{i["title"]}</a></li>', items))}
</p>
</body>
</html>
"""
    return text, ext

# Generates a page in MD format
def md(header, items):
    """
    Generates a page in MD format
    """
    
    nl = "\n\n"
    ext = ".md"
    text = f"""---
title: {header}
---

{
    nl.join(  map(lambda i: f'[{i["title"]}]({i["url"]})', items)  )
}
"""
    return text, ext

# There are two option to use with the generate_index_file:
# - md: the md function generates a file in md format
# - html: the html function generates a file in html format
generate_index_file = md

def join_url(a, b):
    if a == "":
        return b
    return f"{a}/{b}"

def valid_dir(name):
    if name[0] in "._" or name == "assets" or "=" in name:
        return False
    return True

def path_key(d):
    key = ""
    if os.path.isdir(d):
        key += "D"
    elif os.path.isfile(d):
        key += "F"
    key += d.lower()
    return key

class MdInfo:
    def __init__(self, page_title) -> None:
        self.page_title = page_title

def get_md_file_info(file_path) -> MdInfo:
    with open(file_path, "r") as fs:
        while True:
            line = fs.readline()
            if not line:
                break
            page_title = re.match(r"^(#+)\s*(.*)[\s\n]*$", line)
            if page_title is not None and len(page_title[1]) == 1:
                page_title = page_title[2]
                break
            page_title = re.match(r"^title:\s*(.*)[\s\n]*$", line)
            if page_title is not None:
                page_title = page_title[1]
                page_title = re.sub(r"^\"([^\"]*)\"$", r"\1", page_title)
                break
    return MdInfo(
        page_title=page_title,
    )

def strip_html_tags(content):
    while True:
        tag_match = re.match(r"<(\w+)[^>]*>((?:(?!</\1>).)*)</\1>", content)
        if tag_match is None:
            break
        content = re.sub(r"<(\w+)[^>]*>((?:(?!</\1>).)*)</\1>", r"\2", content)
    return content

def get_dir_link(path):
    name = os.path.basename(path)

    # ignore invalid directory names
    if not valid_dir(name):
        return None

    # get category title from the directory name
    title = get_category_name(name)

    return {
        "title": title,
        "url": name,
    }

def exponential_backoff(func, max_retries, unit_timedelta):
    import time
    def exp_bo(*args, **kwargs):
        delta = unit_timedelta
        ex = None
        for _ in range(max_retries):
            try:
                return func(*args, **kwargs)
            except ex:
                time.sleep(unit_timedelta.seconds)
                delta *= 2
        raise ex
    return exp_bo

def get_file_link(path):
    import datetime as dt
    name = os.path.basename(path)

    # Remove index file containing the category items.
    # This file will be regenerated again at the end
    # of this method with new content.
    if name in ["index.html", "index.md"]:
        exponential_backoff(os.remove, 4, dt.timedelta(seconds=1))(path)
        return None

    # Skip non *.md files.
    m = re.match(r"^(.*)\.md$", name)
    if m is None:
        return None

    # Get info about *.md files (other than index.md, which will be deleted)
    # - page title: will be used as the label of the incoming links
    md_info = get_md_file_info(path)
    page_title = md_info.page_title
    page_title = page_title if page_title is not None else ""
    page_title = strip_html_tags(page_title)
    page_title = re.sub(r"\s+", " ", page_title)
    return {
        "title": page_title,
        "url": m[1],
    }

def make(header="", path=".", url_path="", ignore_files=False):
    listing = sorted(os.listdir(path), key=path_key)

    items = []
    for name in listing:
        file_path = os.path.join(path, name)
        item = None
        if os.path.isdir(file_path):
            item = get_dir_link(file_path)
        elif not ignore_files:
            item = get_file_link(file_path)

        if item is not None:
            items.append(item)

    # Generating a new index.md with links to child pages.
    text, ext = generate_index_file(header, items)
    with open(os.path.join(path, f"index{ext}"), "w", encoding="utf-8") as fs:
        fs.write(text)

def make_children(path=".", url_path=""):
    for name in os.listdir(path):
        child_path = os.path.join(path, name)
        if not os.path.isdir(child_path):
            continue
        if not valid_dir(name):
            continue
        child_url_path = name
        title = get_category_name(name)
        make(title, child_path, child_url_path)
        make_children(child_path, child_url_path)


def generate_indexes():
    make(ignore_files=True)
    make_children()

def main():
    generate_indexes()

if __name__ == '__main__':
    main()
