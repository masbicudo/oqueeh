category_names = {
    "css": "CSS",
    "postgresql": "PostgreSQL",
}

def get_category_name(cat):
    import re
    if cat in category_names:
        return category_names[cat]
    cat = re.sub(r"-_\.", " ", cat)
    cat = re.sub(r"\b\w", lambda x: x[0].upper(), cat)
    return cat
