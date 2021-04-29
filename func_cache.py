import json as _json
import os as _os
import datetime as _dt
import atexit as _ax

def _date_hook(json_dict):
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = _dt.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        except:
            pass
    return json_dict

def _date_default(o):
    if isinstance(o, (_dt.date, _dt.datetime)):
        return o.strftime("%Y-%m-%dT%H:%M:%S")

_func_cache = {}
def _func_cache_load():
    global _func_cache
    if _os.path.isfile("_func_cache.json"):
        with open("_func_cache.json", "r") as fs:
            try: _func_cache = _json.load(fs, object_hook=_date_hook)
            except: pass

def _func_cache_save():
    global _func_cache
    with open("_func_cache.json", "w") as fs:
        _json.dump(_func_cache, fs, default=_date_default, indent=2)

def _func_cache_get(fname, version, key, timeout, func, cache):
    if fname in cache:
        my_cache = cache[fname]
    else:
        my_cache = cache[fname] = {}

    now = _dt.datetime.now()
    if key in my_cache and now < my_cache[key]["timeout"] and version == my_cache[key]["version"]:
        return my_cache[key]["data"]

    result = my_cache[key] = {
        "data": func(),
        "timeout": now + timeout,
        "version": version,
    }
    return result["data"]

def func_cache_get(fname, version, key, timeout, func):
    global _func_cache
    return _func_cache_get(fname, version, key, timeout, func, _func_cache)

_func_session = {}
def func_session_get(fname, version, key, timeout, func):
    global _func_session
    return _func_cache_get(fname, version, key, timeout, func, _func_session)

_func_cache_load()
_ax.register(_func_cache_save)
