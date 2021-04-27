import re
import os

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

def get_page_title(uri):
    tree = get_page_html(uri)
    text = tree.find(".//title").text
    return text

def get_domain_from_uri(uri):
    from urllib.parse import urlparse
    result = urlparse(uri).netloc
    return result

def get_link(uri):
    if uri[0] == "/":
        return f"{{% link {uri[1:]} %}}"
    try:
        title = get_page_title(uri)
        if " | " in title or " - " in title:
            return f"[{title}]({uri})"
        domain = get_domain_from_uri(uri)
        return f"[{title} - {domain}]({uri})"
    except Exception as ex:
        return uri

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

with open(input_filename, "r") as fs:
    orig_files = {}
    files = {}
    data = {}
    cur_file = None
    orig_file = None
    for line in fs:
        m = re.match(r"^(\s*)#\s*([^=]*)\s*(?:=\s*(.*)\s*)?", line)
        if m is not None:
            prefix = m[1]
            name = m[2]
            value = m[3]
            data[name] = value
            if name == "publish" and value == "false":
                files[data["file"]] = False
            if data["file"] not in files:
                cur_file = files[data["file"]] = []
            if name == "ref" and data["file"] != "":
                line = f"{prefix}- {get_link(value)}"
            if name == "file":
                continue
        if data["file"] != "":
            line = re.sub(r'^(\s*)<ans>\s*$', r'\1<div markdown="1" class="ans">', line)
            line = re.sub(r'^(\s*)</ans>\s*$', r'\1</div>', line)
        cur_file.append(line.rstrip("\n"))

    with open(error_file_name, "w", encoding="utf-8") as fs_out_split:
        for key, value in files.items():
            if value == False:
                if os.path.isfile(key):
                    os.remove(key)
                continue
            if key != "":
                os.makedirs(os.path.dirname(key), exist_ok=True)
            lmin = min(v for v in value if v.strip() != "")
            lmax = max(v for v in value if v.strip() != "")
            it = 0
            for a, b in zip(lmin, lmax):
                if a != b or a not in " \t":
                    break
                it += 1
            content_lines = [v[it:] if v.strip() != "" else "" for v in value]
            if content_lines[0] == "---":
                content_lines.insert(1, "generated: true")
            else:
                content_lines.insert(0, "---\ngenerated: true\n---")
            content = "\n".join(content_lines)
            if content.strip() != "" and key != "":
                try:
                    with open(key, "w" if overwrite else "x", encoding="utf-8") as fs_out:
                        fs_out.write(content)
                except:
                    fs_out_split.write(f"#error=file exists: {key}\n")
            else:
                content = "\n".join(value)
                fs_out_split.write(f"#file={key}\n")
                fs_out_split.write(f"{content}\n")
