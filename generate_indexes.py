import os
import re

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
    text = f"""# {header}

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
    if name[0] in "._":
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
                "url": name,
            })
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
                title = re.match(r"^#\s*(.*)[\s\n]*$", line)
                if title is not None:
                    title = title[1]
                    break
        title = re.sub(r"\s+", " ", title)
        items.append({
            "title": title,
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
        title = get_title(name)
        make(title, child_path, child_url_path)
        make_children(child_path, child_url_path)

def main():
    make("oqueeh")
    make_children()

if __name__ == '__main__':
    main()
