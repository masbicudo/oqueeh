import hashlib
import re
import os
import argparse

import oqhlib.func_cache as fc
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
    if str_value is None:
        return None
    str_value = str_value.strip()
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
    if len(lines) == 0 or lines[0] != "---":
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
    text = f"Error: {message}"
    if value:
        text += f"\n  {value} @ {source}:{lnum}"
    else:
        text += f"\n  @ {source}:{lnum}"
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
        self.hash_code = None
        self.lines = []
        self.title = None
        self.publish = True
        self.options = {}
        self.includes = set()
        self.source_linenumber = -1
        self.source_filename = None
        self.cyclic_dependency = None
        self.dependency_count = 0
        self.content_b = None
        self.persisted = False
        self.overwrite = None # tristate variable
        self.delete = False

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
        self.line_number = -1

    def __repr__(self):
        text = self.text if self.text is not None else ""
        directive = repr(self.directive) if self.directive is not None else ""
        return f"{text}{directive}"

def preproc_files(input_files, errors_list):
    files = []
    for input_filename in input_files:
        for file in preproc_file(input_filename, errors_list):
            files.append(file)
    return files

def preproc_file(input_filename, errors_list):
    with _open(input_filename, "r") as fs:
        cur_file = None
        for lnum, line in enumerate(fs):
            try:
                line = line.rstrip()
                ret_file, line_data = preproc_line(cur_file, line)

                # returned object is a file-item
                if ret_file is not cur_file:
                    cur_file = ret_file
                    cur_file.source_filename = input_filename
                    cur_file.source_linenumber = lnum+1
                    yield cur_file
                
                # returned object is a line-item
                if line_data is not None:
                    if cur_file is not None:
                        line_data.line_number = lnum - cur_file.source_linenumber + 1
                    if line_data.directive is not None:
                        directive = line_data.directive
                        if directive.name == "publish":
                            cur_file.publish = (directive.value == True)
                        elif directive.name == "include":
                            cur_file.includes.add(directive.value)
                        elif directive.name == "delete":
                            cur_file.delete = True
                        elif directive.name == "overwrite":
                            cur_file.overwrite = True
                    _ = True # Prevent VSCode debugger bug
            except ParseException as pex:
                errors_list.append(format_error(
                        input_filename,
                        lnum + 1,
                        pex.message,
                        pex.value,
                    ))

def preproc_line(cur_file : FileData, line : str):
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
        if name in ["publish", "include", "ref", "overwrite", "delete"]:
            line_data = cur_file.add_directive(name, value, prefix)
        else:
            raise ParseException(f"unrecognized directive", name)
        return cur_file, line_data
    if cur_file is not None:
        line_data = cur_file.add_text(line)
    return cur_file, line_data

def sort_by_dependency(file : FileData, old_files, new_files):
    if file.name not in new_files:
        for inc in file.includes:
            if inc in old_files:
                inc_file = old_files[inc]
                sort_by_dependency(inc_file, old_files, new_files)
                file.dependency_count += 1 + inc_file.dependency_count
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

def get_files_sorted_by_dependency(
        pre_files : list,
        errors_list : list[str],
    ):
    files = {}
    for file in pre_files:
            if file.name in files:
                files[file.name].append(file)
            else:
                files[file.name] = [file]
    dupes = {k:v for k, v in files.items() if len(v) > 1}
    singles = {k:v[0] for k, v in files.items() if len(v) == 1}
    for i, (k, v) in enumerate(dupes.items()):
        msg = f"Error: found {len(dupes)} duplicated file names\n"
        pex = ParseException(
            f"  duplicate d{i}: {k} len={len(v)}",
            (f'    f{n+1}: {f.source_filename}:{f.source_linenumber}' for n,f in enumerate(v))
            )
        sub_msg = '\n'.join(pex.value)
        msg += f"{pex.message}\n{sub_msg}"
        errors_list.append(msg)

    cycles = set()
    for file in singles.values():
        if file.cyclic_dependency is None:
            cycle = detect_dependency_cycle(file, singles, [])
            if cycle is not None and len(cycle) > 0:
                cycles.add(tuple(cycle))
    if len(cycles) > 0:
        msg = f"Error: found {len(cycles)} dependency cycles\n"
        for num, cycle in enumerate(cycles):
            msg_sub = '\n'.join(
                    (
                        f'    f{n+1}: {x} @ {singles[x].source_filename}:{singles[x].source_linenumber}'
                        for n,x in enumerate(cycle)
                    )
                )
            msg += f"  dependency cycle c{num+1}: len={len(cycle)}\n{msg_sub}"
        errors_list.append(msg)

    sorted_files = {}
    for file in singles.values():
        if file.cyclic_dependency is None:
            sort_by_dependency(file, singles, sorted_files)
    return sorted_files

def process_files_contents(sorted_files_dict : dict, errors_list : list[str]):
    include_files_dict = dict(sorted_files_dict)
    for cur_file in sorted_files_dict.values():
        try:
            adjust_prefix(cur_file)
            file_lines = [*process_directives(cur_file, include_files_dict)]
            file_lines = [*process_content(file_lines)]
            file_lines = process_front_matter(cur_file, file_lines)
            cur_file.content_b = '\n'.join(file_lines).encode('utf-8')
            cur_file.hash_code = hashlib.sha256(cur_file.content_b).hexdigest()
        except ParseException as pex:
            errors_list.append(format_error(
                    cur_file.source_filename,
                    cur_file.source_linenumber,
                    pex.message,
                    pex.value,
                ))

_directives_that_allow_text = ["ref"]

def adjust_prefix(file_data):
    for line in file_data.lines:
        if line.directive is not None:
            if line.directive.name not in _directives_that_allow_text:
                if line.text.strip() == "":
                    line.text = None
                else:
                    raise Exception("should be impossible to get to here: all directives must be the first non-space chars at a line")
                    # raise ParseException("text not allowed before directive {}")
        elif line.text is not None:
            new_text = line.text.rstrip()
            line.text = new_text

    try:
        text_min = min((v for v in file_data.lines if v.text != "" and v.text is not None), key=lambda l: l.text)
        text_max = max((v for v in file_data.lines if v.text != "" and v.text is not None), key=lambda l: l.text)
    except ValueError as ve:
        return
    skip = 0
    for a, b in zip(text_min.text, text_max.text):
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

def process_directives(cur_file : FileData, include_files_dict):
    import io
    for line_data in cur_file.lines:
        if line_data.directive is not None:
            filename = line_data.directive.value
            if line_data.directive.name == "ref":
                link_line = f"{line_data.text}- {get_link_cached(filename)}"
                yield link_line
            elif line_data.directive.name == "include":
                if filename not in include_files_dict:
                    with _open(filename, "rb") as fs_inc:
                        file_data = FileData(filename)
                        persisted.persisted = True
                        file_data.content_b = fs_inc.read()
                        files_dict[filename] = file_data
                with io.StringIO(include_files_dict[filename].content_b.decode('utf-8')) as ms:
                    for include_line, include_state in parse_post(ms):
                        if include_state == 2:
                            yield include_line
            _ = True # Prevent VSCode debugger bug
        else:
            yield line_data.text

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
    
    count = 0
    if os.path.isfile("_hash_list/index.txt"):
        with _open("_hash_list/index.txt", "r") as fp:
            count = int(fp.read().strip())

    for idx in range(count):
        filename = f"_hash_list/{idx}.txt"
        if os.path.isfile(filename):
            with _open(filename, "r") as fs_hashes:
                for line in fs_hashes:
                    values = line.rstrip('\n').split(maxsplit=1)
                    if len(values) == 2:
                        result[values[1]] = values[0]

    return result

def get_file_action(
        file_data : FileData,
        prev_file_hash,
        args,
    ):
    file_path = file_data.name

    # remove file if needed
    if file_data.publish == False:
        return "remove:publish=False"
    if file_data.delete == True:
        return "remove"

    # content and hash-code
    if file_data.content_b is None or file_data.content_b == b"":
        raise ParseException("file content is empty", file_path)

    # write or overwrite
    exists = os.path.isfile(file_path)
    wow = args.update != False or not exists
    if wow:
        wow = file_data.hash_code != prev_file_hash
        if wow == False:
            return "skip:hash"
    if file_data.overwrite is not None:
        wow = file_data.overwrite != False
    if wow == True and os.path.isfile(file_path):
        if wow == True and args.check_generated:
            found_generated_flag = False
            with _open(file_path, "r") as fs:
                for ltext, state in parse_post(fs):
                    if state == 1:
                        key_value = ltext.split(":", 1)
                        if len(key_value) == 2:
                            key = key_value[0]
                            value = get_value_from_string(key_value[1])
                            if key == "generated":
                                found_generated_flag = value
                                break
            if not found_generated_flag:
                raise ParseException("cannot replace file without 'generated' marker", file_path)

    # saving file
    if wow and exists:
        return "overwrite"
    elif wow and not exists:
        return "write"
    else:
        raise ParseException("file already exists", file_path)

def do_action(file_data, action : str):
    if action is None or action == "skip" or action.startswith("skip:"):
        return

    file_path = file_data.name

    # remove file if needed
    if (action == "remove" or action.startswith("remove:")):
        if os.path.isfile(file_path):
            os.remove(file_path)
            return

    if action == "overwrite" or action == "write":
        # ensure path exists before saving
        dir_path = os.path.dirname(file_path)
        if file_path != "":
            if dir_path != "":
                os.makedirs(dir_path, exist_ok=True)
        else:
            raise ParseException("file path is empty", file_path)

        # saving file
        ow = (action == "overwrite")
        with _open(file_path, "wb" if ow else "xb") as fs_out:
            fs_out.write(file_data.content_b)
            file_data.persisted = True

_test_mode = False
def _open(filename, access, encoding='utf-8'):
    global _test_mode
    if _test_mode and (not os.path.isfile(filename) or os.path.isfile(f"{filename}.uncommited.test-file")):
        filename = f"{filename}.uncommited.test-file"
        def delete_if_exists():
            try: os.remove(filename)
            except: pass
        import atexit
        atexit.register(delete_if_exists)
    if 'b' in access:
        return open(filename, access)
    return open(filename, access, encoding=encoding)

def update_file_hashes(file_hashes, files):
    for cur_file in files:
        if cur_file.persisted:
            file_hashes[cur_file.name] = cur_file.hash_code

def grouper(n, iterable):
    """
    >>> list(grouper(3, 'ABCDEFG'))
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G']]
    """
    import itertools as IT
    iterable = iter(iterable)
    return iter(lambda: list(IT.islice(iterable, n)), [])

def save_hashes(file_hashes):
    idx = 0
    for g in grouper(100, file_hashes.items()):
        with _open(f"_hash_list/{idx}.txt", "w") as fs_hashes:
            for k, v in g:
                if v is not None:
                    fs_hashes.write(f"{v} {k}\n")
        idx += 1

    with _open("_hash_list/index.txt", "w") as fp:
        fp.write(str(idx))

def arguments_setup(parser : argparse.ArgumentParser):
    parser.add_argument("inputs", nargs="*", type=argparse.FileType("r"), default=["_split", "_split.md"])
    parser.add_argument("-u", "--update", action='store_true')
    parser.add_argument("-c", "--check-generated", action='store_true')
    parser.add_argument("-t", "--test", action='store_true')
    parser.add_argument("-l", "--list", action='store_true')

def get_input_filenames(input_filenames):
    new_input_filename = []
    for input_filename in input_filenames:
        if os.path.isfile(input_filename):
            new_input_filename.append(input_filename)
        if os.path.isdir(input_filename):
            subdir_files = [f for f in os.listdir(input_filename) if os.path.isfile(os.path.join(input_filename, f))]
            new_input_filename.extend(get_input_filenames(subdir_files))
    return new_input_filename

def split_files(
        input_filenames,
        args,
        errors_list : list[str],
    ):
    pre_files = preproc_files(input_filenames, errors_list)

    sorted_files_dict = get_files_sorted_by_dependency(pre_files, errors_list)

    process_files_contents(sorted_files_dict, errors_list)

    file_hashes = load_hashes()
    for cur_file in sorted_files_dict.values():
        file_hash = file_hashes[cur_file.name] if cur_file.name in file_hashes else None
        try:
            action = get_file_action(cur_file, file_hash, args)
            if args.list == False:
                do_action(cur_file, action)
            else:
                print(f"{action} {cur_file.name}")
        except ParseException as pex:
            errors_list.append(format_error(
                    cur_file.source_filename,
                    cur_file.source_linenumber,
                    pex.message,
                    pex.value
                ))

    if args.list == False:
        update_file_hashes(file_hashes, sorted_files_dict.values())
        save_hashes(file_hashes)

def main():
    global _test_mode

    parser = argparse.ArgumentParser(prog='oqh-build')
    arguments_setup(parser)
    args = parser.parse_args()

    input_filenames = args.inputs
    input_filenames = get_input_filenames(input_filenames)

    errors_list = []
    split_files(input_filenames, args, errors_list)
    for err in errors_list:
        print(err)

if __name__ == '__main__':
    main()
