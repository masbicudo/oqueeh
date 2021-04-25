import os
import re
import sys
from utils import get_category_name

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

proj_root = os.path.dirname(__file__)

for root, dirs, files in os.walk(".", onerror=onerror):
    if root == '.':
        continue
    categories = re.split(r'[\\/]', root)[1:]
    if any(not valid_dir(c) for c in categories):
        continue
    for file in files:
        cats = categories if file != "index.md" else categories[:-1]
        m = re.match(r'.*\.md$', file)
        if m is None:
            continue
        p = os.path.join(root, file)
        state = 0
        cat_names = list(map(get_category_name, cats))
        cats_line_num = -1
        head_end = -1
        ok = False
        with open(p, "r") as fs:
            for cur_line_num, line in enumerate(fs):
                line = line.rstrip("\n")
                if line == "---":
                    state += 1
                    if state == 2:
                        head_end = cur_line_num
                        break
                    continue
                if state == 1:
                    file_cats = read_categories(line)
                    if file_cats is None:
                        continue
                    cats_line_num = cur_line_num
                    file_cat_names = list(map(get_category_name, file_cats))
                    array_equals = all(map(lambda x: x[0] == x[1], zip(cat_names, file_cat_names)))
                    ok = array_equals
                    break
        if len(cats) == 0:
            ok = head_end != -1

        elif not ok:
            with open(p, "r") as fs:
                all_lines = fs.readlines()
            if cats_line_num != -1:
                if len(cats) == 0:
                    del all_lines[cats_line_num]
                else:
                    all_lines[cats_line_num] = f"categories: [{', '.join(cat_names)}]\n"
            elif head_end != -1:
                all_lines = [*all_lines[0:head_end], f"categories: [{', '.join(cat_names)}]\n", *all_lines[head_end:]]
            with open(p, "w") as fs:
                fs.writelines(all_lines)
