import re
import os

import func_cache as fc

def get_charset_from_content_type(content_type):
    match_charset = re.search(r"charset=\s*([^,]*)\s*", content_type)
    if match_charset is not None:
        return match_charset[1]
    return None

def get_page_html(uri):
    from urllib.request import urlopen
    from lxml.html import document_fromstring

    stream = urlopen(uri)
    if "Content-Type" in stream.headers:
        content_type_charset = get_charset_from_content_type(stream.headers["Content-Type"])

    bstr = stream.read()
    try:
        html = bstr.decode(content_type_charset)
    except Exception as ex:
        try:
            html = bstr.decode("utf-8")
        except Exception as ex:
            html = bstr
    document = document_fromstring(html)

    meta_content_type = document.find('./head/meta[@http-equiv="Content-type"]')
    if meta_content_type is not None:
        meta_content_type_charset = get_charset_from_content_type(meta_content_type.text)
        try:
            html = bstr.decode(meta_content_type_charset)
        except:
            pass

    meta_charset = document.find('./head/meta[@charset]')
    if meta_charset is not None:
        meta_charset_attrib = meta_charset.attrib["charset"]
        try:
            html = bstr.decode(meta_charset_attrib)
        except:
            pass

    document = document_fromstring(html)

    return document

def get_page_html_cached(uri):
    return fc.func_session_get("get_page_html", 1, uri, dt.timedelta(30), lambda: get_page_html(uri))

def get_page_title(uri):
    tree = get_page_html_cached(uri)
    text = tree.find(".//title").text
    return text

def get_page_title_cached(uri):
    return fc.func_cache_get("get_page_title", 1, uri, dt.timedelta(30), lambda: get_page_title(uri))

def get_domain_from_uri(uri):
    from urllib.parse import urlparse
    result = urlparse(uri).netloc
    return result

def get_link(uri):
    if uri[0] == "/":
        return f"{{% link {uri[1:]} %}}"
    try:
        title = get_page_title_cached(uri)
        if " | " in title or " - " in title:
            return f"[{title}]({uri})"
        domain = get_domain_from_uri(uri)
        return f"[{title} - {domain}]({uri})"
    except Exception as ex:
        return uri

def get_link_cached(uri):
    return get_link(uri)
    # return fc.func_cache_get("get_link", 1, uri, dt.timedelta(30), lambda: get_link(uri))

import sys

input_filename = "_split.md"

argn = 0
overwrite = False
for arg in sys.argv[1:]:
    m = re.match(r"^--?[\d\w].*$", arg)
    if m is not None:
        if arg == "--overwrite" or arg == "-o":
            overwrite=True
        else:
            raise Exception(f"Invalid named argument {arg}")
    else:
        if argn == 0:
            input_filename = arg
        elif argn == 1:
            raise Exception(f"Invalid ordinal argument {argn}")
        argn += 1
error_file_name = re.sub(r'(.*)\.md', r'\1.error.md', input_filename)

import datetime as dt
import distutils.util as du
def get_value_from_string(str_value):
    try: return int(str_value)
    except: pass
    try: return float(str_value)
    except: pass
    try: return bool(du.strtobool(str_value))
    except: pass
    try: return dt.datetime.strptime(str_value, '%Y-%m-%d %H:%M:%S.%f')
    except: pass
    try: return dt.datetime.strptime(str_value, '%Y-%m-%d %H:%M:%S')
    except: pass
    try: return dt.datetime.strptime(str_value, '%Y-%m-%d %H:%M')
    except: pass
    try: return dt.datetime.strptime(str_value, '%Y-%m-%d')
    except: pass
    return str_value

def set_front_matter(lines, key, value):
    if lines[0] != "---":
        lines.insert(0, "---")
        lines.insert(0, "---")
    fm = {}
    state = 0
    ok = False
    for lnum, line in enumerate(lines):
        if line.strip() == "---":
            state += 1
        if state == 2: break
        if state == 1:
            m = re.match(r"^([^:]+):\s*(.*)\s*$", line)
            if m is not None:
                if m[1] == key:
                    lines[lnum] = f"{key}: {value}"
                    ok = True
    if not ok:
        lines.insert(1, f"{key}: {value}")
    return lines

with open(input_filename, "r") as fs:
    orig_files = {}
    files = {}
    data = {}
    cur_file = None
    orig_file = None
    for line in fs:
        m = re.match(r"^(\s*)#([^=]*)\s*(?:=\s*(.*)\s*)?", line)
        if m is not None:
            prefix = m[1]
            name = m[2]
            str_value = m[3]
            value = get_value_from_string(str_value)
            data[name] = value
            if data["file"] not in files:
                cur_file = files[data["file"]] = {"lines": [], "title": None, "publish": True}
            if name == "file":
                continue
            if name == "publish":
                cur_file["publish"] = (value == 0)
            if name == "ref" and data["file"] != "":
                line = f"{prefix}- {get_link_cached(value)}"
        m = re.match(r"^(\s*)(#+)\s+(.*)\s*$", line)
        if m is not None:
            if m[2] == "#":
                cur_file["title"] = m[3]
                continue
        if data["file"] != "":
            line = re.sub(r'^(\s*)<ans>\s*$', r'\1<div markdown="1" class="ans">', line)
            line = re.sub(r'^(\s*)</ans>\s*$', r'\1</div>', line)
        cur_file["lines"].append(line.rstrip("\n"))

    with open(error_file_name, "w", encoding="utf-8") as fs_out_split:
        for key, value in files.items():
            file_path = key
            file_data = value
            if file_data["publish"] == False:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                continue
            if file_path != "":
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
            lmin = min(v for v in file_data["lines"] if v.strip() != "")
            lmax = max(v for v in file_data["lines"] if v.strip() != "")
            it = 0
            for a, b in zip(lmin, lmax):
                if a != b or a not in " \t":
                    break
                it += 1
            content_lines = [v[it:] if v.strip() != "" else "" for v in file_data["lines"]]
            set_front_matter(content_lines, "generated", "true")
            if file_data["title"] is not None:
                set_front_matter(content_lines, "title", file_data["title"])
            content = "\n".join(content_lines)
            if content.strip() != "" and file_path != "":
                try:
                    with open(file_path, "w" if overwrite else "x", encoding="utf-8") as fs_out:
                        fs_out.write(content)
                except:
                    fs_out_split.write(f"#error=file exists: {file_path}\n")
            else:
                content = "\n".join(file_data["lines"])
                fs_out_split.write(f"#file={file_path}\n")
                fs_out_split.write(f"{content}\n")
