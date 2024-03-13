---
title: Treating errors in Python
generated: true
---

<div markdown="1" class="ans">
```python
try: # code to try
except Exception as ex: # execute on error
else: # execute only if no errors
finally: # always execute
```
</div>

**Remarks:**
- You can omit exception variable name and type.
- Multiple `except` blocks with different types are allowed.

**Related:**
- [Raising errors in Python](/en-US/python/raising-errors)

**References:**
- [8. Errors and Exceptions — Python 3.12.2 documentation](https://docs.python.org/3/tutorial/errors.html)
