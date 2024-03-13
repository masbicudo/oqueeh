---
title: Running `http.server` returning `ERR_CONNECTION_REFUSED` in Python
generated: true
---

<div markdown="1" class="ans">
You need to use the specific binding IP or hostname to access the server:
Either:
- http://localhost &lt;or&gt;
- http://127.0.0.1
</div>

**Related:**
- [Running `http.server` returning `ERR_EMPTY_RESPONSE` in Python](/en-US/python/running-http-server-returning-empty-response)
- [Running `http.server` returning `ERR_ADDRESS_INVALID` in Python](/en-US/python/running-http-server-returning-invalid-address)
