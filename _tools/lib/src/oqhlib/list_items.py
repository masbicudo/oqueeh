import argparse
import os
import re

def arguments_setup(parser : argparse.ArgumentParser):
    parser.add_argument("inputs", nargs="*", type=str, default=["_split", "_split.md"])
    parser.add_argument("-o", "--orphaned", action='store_true')

def onerror(oserror):
    pass

def valid_dir(name):
    if name[0] in "._" or name == "assets" or "=" in name:
        return False
    return True

def list_files():
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
            if file == "index.md":
                continue
            yield os.path.join(root, file)

def list_files_orphaned(
            input_filenames,
        ):
    errors_list : list[str] = []
    
    import oqhlib.build as bld
    pre_files = bld.preproc_files(input_filenames, errors_list)

    listed_files = {x.name for x in pre_files if not x.delete}
    site_files = {x.replace("\\", "/")[2:] for x in list_files()}
    generated_site_files = {x for x in site_files if bld.check_generated_flag(x)}

    orphaned_list = generated_site_files.difference(listed_files)
    return orphaned_list
