---
title: Will "w+" flag truncate the file in Python
---

<ans>Yes.</ans>

The following code truncates `filename.txt`:

```python
with open("filename.txt", "w+"):
    pass
```
