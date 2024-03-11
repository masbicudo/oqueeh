---
title: urllib2.HTTPError: HTTP Error 403: Forbidden using urlopen in Python
generated: true
---

<div markdown="1" class="ans">
```python
headers = { 'User-Agent': 'Mozilla/5.0' }
request = Request(uri, headers=headers)
stream = urlopen(request)
```
</div>

**Remarks:**

When using a URL string with `urlopen` the header *User-Agent* is not defined,
and this causes the server to return 403 Forbidden.
