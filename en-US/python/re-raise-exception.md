---
title: Re-raise exception in Python
generated: true
---

<div markdown="1" class="ans">
Use `raise` to re-raise exception.
</div>

**Example:**

```python
try: # ...
except: # ...
    print("Error occurred")
    raise
```

**Related:**
- [Re-raise exception without chaining in Python](/en-US/python/re-raise-exception-without-chaining)
- [Raise exception in Python](/en-US/python/raise-exception)

**References:**
- [8. Errors and Exceptions — Python 3.12.2 documentation](https://docs.python.org/3/tutorial/errors.html)
