---
title: Get a list of True values inside a *Namespace* in Python
generated: true
---

<div markdown="1" class="ans">
```python
list_true_keys = [ k for (k, v) in ns.items() if v ]
```
</div>
