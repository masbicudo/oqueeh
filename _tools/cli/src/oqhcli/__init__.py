version = "0.1.2"

def get_github_search_uri(search_string):
    import urllib.parse as up
    query_string = up.urlencode({"q": search_string})
    uri = f"https://github.com/masbicudo/oqueeh/search?{query_string}"
    return uri
