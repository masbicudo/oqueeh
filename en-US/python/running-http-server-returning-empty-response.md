---
title: Running `http.server` returning `ERR_EMPTY_RESPONSE` in Python
generated: true
---

<div markdown="1" class="ans">
Add a binding to localhost when running:
```bash
python -m http.server 8000 --bind localhost
```
</div>

**Related:**
- [Running `http.server` returning `ERR_ADDRESS_INVALID` in Python](/en-US/python/running-http-server-returning-invalid-address)
- [Running `http.server` returning `ERR_CONNECTION_REFUSED` in Python](/en-US/python/running-http-server-returning-connection-refused)
