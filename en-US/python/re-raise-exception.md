---
title: Re-raise exception in Python
generated: true
---

<div markdown="1" class="ans">
```python
try: # ...
except ex: # ...
raise ex from None
```
</div>

**Remarks:**

Use `from None` to remove parent exceptions, e.g. when exception is raised while handling another exception.
