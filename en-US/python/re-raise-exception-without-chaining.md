---
title: Re-raise exception without chaining in Python
generated: true
---

<div markdown="1" class="ans">
Use `raise exc from None` to remove parent exceptions.
</div>

**Example:**

```python
try: # ...
except Exception ex1: # ...
    try: # ...
    except Exception ex2: # ...
        raise ex1 from None
```

**Related:**
- [Re-raise exception in Python](/en-US/python/re-raise-exception)
- [Raise exception in Python](/en-US/python/raise-exception)

**References:**
- [8. Errors and Exceptions — Python 3.12.2 documentation](https://docs.python.org/3/tutorial/errors.html)
