---
title: Hashing a function object in Python
generated: true
---

<div markdown="1" class="ans">
```python
def get_function_hash(fn):
    return hash((
        inspect.getsource(fn),
        get_function_closures(fn),
        get_function_globals(fn),
    ))
```
See related content for `get_function_closures` and `get_function_globals` implementations.
</div>

**Requirements:**
```python
import inspect
```

**Related:**
- [Get closure variables used by a function in Python](/en-US/python/get-closure-variables-used-by-function)
- [Get global context variables used by a function in Python](/en-US/python/get-global-context-variables-used-by-function)
