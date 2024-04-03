import os
import re
from oqhlib.utils import get_category_name
from oqhlib.list_items import list_files

def read_categories(line):
    m = re.match(r'categories:(.*)', line)
    if m is None:
        return None
    result = m[1].strip().strip("[]").split(",")
    return result

def ensure_categories():
    category_names = {}

    for file in list_files():
        file_split = re.split(r'[\\/]', file)
        categories = file_split[1:-1]
        for cat in categories:
            cat_name = get_category_name(cat)
            category_names[cat] = cat_name

    import json
    with open("_data/category_names.json", "w") as fs:
        json.dump(category_names, fs, indent=4)

def main():
    ensure_categories()

if __name__ == '__main__':
    main()
