import os
import re
from utils import get_category_name

def html(header, items):
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

def md(header, items):
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

generate_file = md

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

def make(header="", path=".", url_path="", ignore_files=False):
    listing = sorted(os.listdir(path), key=path_key)

    items = []
    for name in listing:
        file_path = os.path.join(path, name)
        if os.path.isdir(file_path):
            if not valid_dir(name):
                continue
            title = get_category_name(name)
            items.append({
                "title": title,
                "url": name,
            })
            continue
        if ignore_files:
            continue
        if name in ["index.html", "index.md"]:
            os.remove(os.path.join(path, name))
            continue
        m = re.match(r"^(.*)\.md$", name)
        if m is None:
            continue

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
        page_title = page_title if page_title is not None else ""
        while True:
            tag_match = re.match(r"<(\w+)[^>]*>((?:(?!</\1>).)*)</\1>", page_title)
            if tag_match is None:
                break
            page_title = page_title = re.sub(r"<(\w+)[^>]*>((?:(?!</\1>).)*)</\1>", r"\2", page_title)
        page_title = re.sub(r"\s+", " ", page_title)
        items.append({
            "title": page_title,
            "url": m[1],
        })
    text, ext = generate_file(header, items)
    with open(os.path.join(path, f"index{ext}"), "w") as fs:
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

def main():
    make(ignore_files=True)
    make_children()

if __name__ == '__main__':
    main()
