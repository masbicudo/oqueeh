import os
import re
import sys
from oqhlib.utils import get_category_name

def onerror(oserror):
    pass

def valid_dir(name):
    if name[0] in "._" or name == "assets" or "=" in name:
        return False
    return True

def read_categories(line):
    m = re.match(r'categories:(.*)', line)
    if m is None:
        return None
    result = m[1].strip().strip("[]").split(",")
    return result

def ensure_categories():
    category_names = {}

    for root, dirs, files in os.walk(".", onerror=onerror):
        if root == '.':
            continue
        categories = re.split(r'[\\/]', root)[1:]
        if any(not valid_dir(c) for c in categories):
            continue
        for file in files:
            m = re.match(r'.*\.md$', file)
            if m is None:
                continue
            cats = categories if file != "index.md" else categories[:-1]
            for cat in cats:
                cat_name = get_category_name(cat)
                category_names[cat] = cat_name

    import json
    with open("_data/category_names.json", "w") as fs:
        json.dump(category_names, fs, indent=4)

def main():
    ensure_categories()

if __name__ == '__main__':
    main()
