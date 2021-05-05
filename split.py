import json
import hashlib
import re
import os

import func_cache as fc
import sys
import datetime as dt
import distutils.util as du



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

    html_ok = False

    meta_content_type = document.find('./head/meta[@http-equiv="Content-type"]')
    if meta_content_type is not None:
        meta_content_type_charset = get_charset_from_content_type(meta_content_type.text)
        try:
            html = bstr.decode(meta_content_type_charset)
            html_ok = True
        except:
            pass

    if not html_ok:
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

_pattern_domain = re.compile(r"(?:((?:[^\.]+\.)*[^\.]+)\.)?([^\.]+)((\.(?:com|net|org|gov|edu|info|biz))(\.[^\.]+)?)")

def get_link(uri):
    if uri[0] == "/":
        return f"{{% link {uri[1:]} %}}"
    try:
        title = get_page_title_cached(uri)
        title = re.sub(r"([|\\])", r"\\\1", title)
        title_lower = title.lower()
        domain = get_domain_from_uri(uri)
        m_domain = _pattern_domain.match(domain)
        if m_domain is not None:
            if m_domain[2] in title_lower:
                return f"[{title}]({uri})"
        return f"[{title} - {domain}]({uri})"
    except Exception as ex:
        return uri

def get_link_cached(uri):
    return get_link(uri)
    # return fc.func_cache_get("get_link", 1, uri, dt.timedelta(30), lambda: get_link(uri))

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

def format_error(source, lnum, message, value):
    text = f"{source}:{lnum + 1} - Error: {message}"
    if value:
        text += f"\n  {value}"
    return text

_pattern_ans_start_tag = re.compile(r'^(\s*)<ans(?:((?:(?!class).)*?)\s*(\s)class=(["\'])((?:(?!\4).)+)\4)?([^>]*?)>\s*$')
_replace_ans_start_tag = lambda line: _pattern_ans_start_tag.sub(r'\1<div markdown="1"\2 class="ans\3\5"\6>', line)

_pattern_ans_close_tag = re.compile(r'^(\s*)</ans>\s*$')
_replace_ans_close_tag = lambda line: _pattern_ans_close_tag.sub(r'\1</div>', line)

_allowed_exts = [".md"]

class ParseException(Exception):
    def __init__(self, message, value=None):
        super().__init__()
        self.message = message
        self.value = value

class FileData(object):
    def __init__(self, name=None):
        super().__init__()
        self.name = name
        self.hash = None
        self.lines = []
        self.title = None
        self.publish = True
        self.options = {}
        self.includes = set()
        self.source_linenumber = -1
        self.source_filename = None
        self.cyclic_dependency = None

    def add_text(self, text):
        data = LineData()
        data.text = text
        self.lines.append(data)
        return data

    def add_directive(self, name, value, prefix):
        data = LineData()
        data.text = prefix
        data.directive = DirectiveInfo(name, value)
        self.lines.append(data)
        return data

    def __repr__(self):
        return self.name

class DirectiveInfo(object):
    def __init__(self, name, value):
        super().__init__()
        if name is None or name == "":
            raise Exception("name of DirectiveInfo class must be a non-empty string")
        self.name = name
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f"#{self.name}={self.value}"
        return f"#{self.name}"

class LineData(object):
    def __init__(self):
        super().__init__()
        self.text = None
        self.directive = None

    def __repr__(self):
        text = self.text if self.text is not None else ""
        directive = repr(self.directive) if self.directive is not None else ""
        return f"{text}{directive}"

def preprocess_files(input_files):
    files = []
    for input_filename in input_files:
        for file in preprocess_file(input_filename):
            files.append(file)
    return files

def preprocess_file(input_filename):
    with open(input_filename, "r") as fs:
        cur_file = None
        for lnum, line in enumerate(fs):
            try:
                line = line.rstrip()
                ret_file, line_data = preprocess_line(cur_file, line)
                if ret_file is not cur_file:
                    cur_file = ret_file
                    cur_file.source_filename = input_filename
                    cur_file.source_linenumber = lnum+1
                    yield cur_file
                if line_data is not None and line_data.directive is not None:
                    directive = line_data.directive
                    if directive.name == "publish":
                        cur_file.publish = (directive.value == True)
                    elif directive.name == "include":
                        cur_file.includes.add(directive.value)
            except ParseException as pex:
                print(format_error(input_filename, lnum, pex.message, pex.value))

def preprocess_line(cur_file : FileData, line : str):
    line_data = None
    m_directive = re.match(r"^(\s*)#(\b[^=]*)\s*(?:=\s*(.*)\s*)?", line)
    if m_directive is not None:
        prefix = m_directive[1]
        name = m_directive[2]
        str_value = m_directive[3]
        value = get_value_from_string(str_value)
        if name == "file":
            cur_file = FileData(name=value)
            if value == "":
                raise ParseException("empty file name", value)
            m_fname = re.match(r"^(.*?)(\.[^\.]*)$", value)
            if m_fname is None:
                raise ParseException("file without extension", value)
            if m_fname[2] not in _allowed_exts:
                raise ParseException(f"allowed extensions are {' '.join(_allowed_exts)}", value)
            return cur_file, line_data
        if name in ["publish", "include", "ref", "overwrite"]:
            line_data = cur_file.add_directive(name, value, prefix)
        else:
            raise ParseException(f"unrecognized directive: {name}")
        return cur_file, line_data
    line_data = cur_file.add_text(line)
    return cur_file, line_data

def sort_by_dependency(file, old_files, new_files):
    for inc in file.includes:
        if inc in old_files:
            inc_file = old_files[inc]
            sort_by_dependency(inc_file, old_files, new_files)
            file.dependency_count += 1 + inc_file.dependency_count
    if file.name not in new_files:
        new_files[file.name] = file

def detect_dependency_cycle(file, files, cycle):
    cycle.append(file.name)
    file.cyclic_dependency = cycle
    for inc in file.includes:
        if inc in files:
            inc_file = files[inc]
            if inc_file.cyclic_dependency is None:
                ret_cycle = detect_dependency_cycle(inc_file, files, cycle)
                file.cyclic_dependency = ret_cycle
                return ret_cycle
            else:
                return inc_file.cyclic_dependency
    cycle.pop()
    file.cyclic_dependency = None
    return None

def get_files_sorted_by_dependency(pre_files : list):
    files = {}
    for file in pre_files:
            if file.name in files:
                files[file.name].append(file)
            else:
                files[file.name] = [file]
    dupes = {k:v for k, v in files.items() if len(v) > 1}
    singles = {k:v[0] for k, v in files.items() if len(v) == 1}
    for i, (k, v) in enumerate(dupes.items()):
        print(f"found {len(dupes)} duplicated files")
        pex = ParseException(
            f"  duplicate d{i}: {k} len={len(v)}",
            (f'    f{n+1}: {f.source_filename}:{f.source_linenumber}' for n,f in enumerate(v))
            )
        print(f"{pex.message}{os.linesep}{os.linesep.join(pex.value)}")

    cycles = set()
    for file in singles.values():
        if file.cyclic_dependency is None:
            cycle = detect_dependency_cycle(file, singles, [])
            if len(cycle) > 0:
                cycles.add(tuple(cycle))
    if len(cycles) > 0:
        print(f"found {len(cycles)} dependency cycles")
        for num, cycle in enumerate(cycles):
            print(f"  dependency cycle c{num+1}: len={len(cycle)}{os.linesep}{os.linesep.join((f'    f{n+1}: {x} @ {singles[x].source_filename}:{singles[x].source_linenumber}' for n,x in enumerate(cycle)))}")

    sorted_files = {}
    for file in singles.values():
        if file.cyclic_dependency is None:
            sort_by_dependency(file, singles, sorted_files)
    return sorted_files

def process_files(pre_files_sorted_dict : dict, file_hashes, args):
    for cur_file in pre_files_sorted_dict.values():
        try:
            adjust_prefix(cur_file)
            file_lines = process_directives(cur_file)
            file_lines = process_content(file_lines)
            file_lines = process_front_matter(file_lines)
            content = "\n".join(file_lines)
            file_hash = file_hashes[cur_file.name] if cur_file.name in file_hashes else None
            save_or_remove_file(cur_file, content, file_hash, args)
        except ParseException as pex:
            print(format_error(cur_file.source_filename, cur_file.source_linenumber, pex.message, pex.value))

_directives_that_allow_text = ["ref"]

def adjust_prefix(file_data):
    for line in file_data.lines:
        if line.directive is not None:
            if line.directive.name not in _directives_that_allow_text:
                if line.text.strip() == "":
                    line.text = None
                else:
                    raise ParseException("text not allowed before directive {}")
        elif line.text is not None:
            line.text = line.text.rstrip()

    try:
        text_min = min(v for v in file_data.lines if v.text != "" and v.text is not None)
        text_max = max(v for v in file_data.lines if v.text != "" and v.text is not None)
    except ValueError as ve:
        return
    skip = 0
    for a, b in zip(text_min, text_max):
        if a != b or a not in " \t":
            break
        skip += 1
    for line in file_data.lines:
        if line.text != "" and line.text is not None:
            line.text = line.text[skip:]

def parse_post(file_lines):
    state = 0
    for lnum, ltext in enumerate(file_lines):
        ltext = ltext.rstrip()
        if state < 2 and ltext == "---":
            state += 1
            continue
        if state == 0 and ltext != "":
            state = 2
        yield ltext, state

def process_directives(cur_file : FileData):
    for line_data in cur_file.lines:
        if line_data.directive is not None:
            if line_data.directive.name == "ref":
                link_line = f"{line_data.text}- {get_link_cached(line_data.directive.value)}"
                yield link_line
            if line_data.directive.name == "include":
                with open(line_data.directive.value, "r") as fs_inc:
                    for include_line, include_state in parse_post(fs_inc):
                        if include_state == 2:
                            yield include_line

class LineTypes(object):
    title = 1
    content = 2

def process_content(file_lines):
    for line in file_lines:
        if line is not None:
            m_title = re.match(r"^(\s*)(#+)\s+(.*)\s*$", line)
            if m_title is not None:
                if m_title[2] == "#":
                    yield m_title[3], LineTypes.title
                    continue
            if "ans" in line:
                line = _replace_ans_start_tag(line)
                line = _replace_ans_close_tag(line)
            yield line, LineTypes.content

def process_front_matter(file_data, file_lines):
    content_lines = []
    title = file_data.title
    user_title = False
    for ltext, ltype in file_lines:
        if ltype == LineTypes.title:
            if not user_title:
                title = ltext
                user_title = True
            else:
                raise ParseException("multiple titles found in file", None)
        elif ltype == LineTypes.content:
            content_lines.append(ltext)
    set_front_matter(content_lines, "generated", "true")
    if title is not None:
        set_front_matter(content_lines, "title", title)
    return content_lines

def load_hashes():
    result = {}
    if os.path.isfile("_hash_list.txt"):
        with open("_hash_list.txt", "r") as fs_hashes:
            for line in fs_hashes:
                values = line.split(maxsplit=1)
                if len(values) == 2:
                    result[values[1]] = values[0]
    return result

def save_or_remove_file(file_data, file_text, prev_file_hash, args):
    file_path = file_data.name
    if file_data.publish == False:
        if os.path.isfile(file_path):
            os.remove(file_path)
        return False
    if file_path != "":
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    else:
        raise ParseException("file path is empty")

    file_text_b = file_text.rstrip().encode('utf-8')
    if file_text == "":
        raise ParseException("file has no content")
    try:
        ow = args["overwrite"]
        if "overwrite" in file_data.options:
            ow = True
            if file_data.options["overwrite"] == False:
                ow = False
        if ow == True and os.path.isfile(file_path):
            file_hash = hashlib.sha256(file_text_b).hexdigest()
            ow = file_hash != prev_file_hash
            if ow == True and args["check_generated_flag"]:
                with open(file_path, "r") as fs:
                    for ltext, state in parse_post(fs):
                        if state == 1:
                            key_value = ltext.split(":", 1)
                            if len(key_value) == 2:
                                key = key_value[0]
                                value = get_value_from_string(key_value[1])
                                if key == "generated" and value != False:
                                    raise ParseException("existing target file is not marked as generated", file_data.name)
        if not args["test"]:
            with open(file_path, "wb" if ow else "xb") as fs_out:
                fs_out.write(file_text_b)
    except FileExistsError:
        raise ParseException(f"file already exists", file_path)

def main():

    input_filenames = []

    args = {
        "overwrite": False,
        "check_generated_flag": True,
        "test": False,
    }
    argn = 0
    for arg in sys.argv[1:]:
        m = re.match(r"^--?[\d\w].*$", arg)
        if m is not None:
            if arg == "--overwrite" or arg == "-o":
                args["overwrite"] = True
            elif arg == "--ignore-generated" or arg == "-i":
                args["check_generated_flag"] = False
            elif arg == "--test" or arg == "-t":
                args["test"] = True
            else:
                raise Exception(f"Invalid named argument {arg}")
        else:
            input_filenames.append(arg)
            argn += 1

    if len(input_filenames) == 0:
        if os.path.isfile("_split.md"):
            input_filenames.append("_split.md")
        if os.path.isdir("_split"):
            input_filenames.extend(f for f in os.listdir("_split") if os.path.isfile(os.path.join("_split", f)))
    pre_files = preprocess_files(input_filenames)
    files_dict = get_files_sorted_by_dependency(pre_files)
    file_hashes = load_hashes()
    process_files(files_dict, file_hashes, args)

if __name__ == '__main__':
    main()
