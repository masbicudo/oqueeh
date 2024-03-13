---
title: Get closure variables used by a function in Python
generated: true
---

<div markdown="1" class="ans">
```python
def get_function_closures(fn):
    return (*(
            closure.cell_contents
            for closure
            in fn.__closure__
        ),)
```
</div>

**Related:**
- [Get global context variables used by a function in Python](/en-US/python/get-global-context-variables-used-by-function)
