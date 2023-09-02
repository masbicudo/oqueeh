---
title: Checking if variable exists in *Namespace* in Python
generated: true
---

<div markdown="1" class="ans">
```python
hasattr(ns, "name")
```
*- or -*
```python
'name' in vars(ns)
```
</div>
