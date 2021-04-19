import os
import re

def html(header, items):
    nl = "\n  "
    return f"""<!DOCTYPE html>
<html>
<body>
<h2>{header}</h2>
<p>
  {nl.join(list(map(lambda i: f'<li><a href="{i["url"]}">{i["title"]}</a></li>', items)))}
</p>
</body>
</html>
"""

EXCLUDED = ['index.html']

def join_url(a, b):
    if a == "":
        return b
    return f"{a}/{b}"

def valid_dir(name):
    if name[0] == ".":
        return False
    return True

def get_title(title):
    title = re.sub(r"-_\.", " ", title)
    title = re.sub(r"\b\w", lambda x: x[0].upper(), title)
    return title

def make(header, path=".", url_path=""):
    items = []
    for name in os.listdir(path):
        file_path = os.path.join(path, name)
        if os.path.isdir(file_path):
            if not valid_dir(name):
                continue
            title = get_title(name)
            items.append({
                "title": title,
                "url": join_url(url_path, name),
            })
            continue
        if name == "index.html":
            continue
        m = re.match(r"^(.*)\.md$", name)
        if m is None:
            continue

        with open(file_path, "r") as fs:
            while True:
                line = fs.readline()
                if not line:
                    break
                title = re.match(r"^#\s*(.*)[\s\n]*$", line)
                if title is not None:
                    title = title[1]
                    break
        title = re.sub(r"\s+", " ", title)
        items.append({
            "title": title,
            "url": join_url(url_path, m[1]),
        })
    with open(os.path.join(path, "index.html"), "w") as fs:
        text = html(header, items)
        fs.write(text)

def make_children(path=".", url_path=""):
    for name in os.listdir(path):
        child_path = os.path.join(path, name)
        if not os.path.isdir(child_path):
            continue
        if not valid_dir(name):
            continue
        child_url_path = join_url(url_path, name)
        title = get_title(name)
        make(title, child_path, child_url_path)
        make_children(child_path, child_url_path)

def main():
    make("oqueeh")
    make_children()

if __name__ == '__main__':
    main()
