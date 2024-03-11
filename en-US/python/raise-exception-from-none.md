---
title: Raise exception from None in Python
generated: true
---

<div markdown="1" class="ans">
Remove parent exceptions, e.g. when exception is raised in the except block of another exception.
</div>

**Example:**
```python
try: # ...
except ex1:
    try: # ...
    except ex2:
        # ex1 is parent of ex2
        # use from None to force parent to be None
        raise ex2 from None
```
