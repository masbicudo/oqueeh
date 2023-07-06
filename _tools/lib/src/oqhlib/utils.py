from data import category_names

def get_category_name(cat):
    import re
    if cat in category_names:
        return category_names[cat]
    cat = re.sub(r"[-_\.\s]+", " ", cat)
    cat = re.sub(r"\b\w", lambda x: x[0].upper(), cat)
    return cat

class DictObj:
    def __init__(self, in_dict:dict):
        assert isinstance(in_dict, dict)
        for key, val in in_dict.items():
            if isinstance(val, (list, tuple)):
               setattr(self, key, [DictObj(x) if isinstance(x, dict) else x for x in val])
            else:
               setattr(self, key, DictObj(val) if isinstance(val, dict) else val)
