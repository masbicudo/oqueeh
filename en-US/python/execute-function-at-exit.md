---
title: Execute function at exit in Python
generated: true
---

```
atexit.register(fn)
```

This can be used inside a module.

The function will be called in the end of the Python program, even if the program is terminated by pressing <kbd>ctrl+c</kbd>.

#### Prerequisite:

```python
import atexit
```
