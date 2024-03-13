---
title: Get global context variables used by a function in Python
generated: true
---

<div markdown="1" class="ans">
```python
def get_function_globals(fn):
    return (*(
            fn.__globals__[instruction.argval]
            for instruction
            in dis.Bytecode(fn)
            if instruction.opname == 'LOAD_GLOBAL'
        ),)
```
</div>

**Requirements:**
```python
import dis
```

**Related:**
- [Get closure variables used by a function in Python](/en-US/python/get-closure-variables-used-by-function)
