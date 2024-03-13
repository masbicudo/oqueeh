---
title: Running `http.server` returning `ERR_ADDRESS_INVALID` in Python
generated: true
---

<div markdown="1" class="ans">
Use a valid IP or hostname to access the server:
- localhost
- 127.0.0.1

You can bind to 0.0.0.0, but not access it.
</div>

**Remarks:**
Binding to 0.0.0.0 means to accept any IP address when connecting.

**Related:**
- [Running `http.server` returning `ERR_EMPTY_RESPONSE` in Python](/en-US/python/running-http-server-returning-empty-response)
- [Running `http.server` returning `ERR_CONNECTION_REFUSED` in Python](/en-US/python/running-http-server-returning-connection-refused)
