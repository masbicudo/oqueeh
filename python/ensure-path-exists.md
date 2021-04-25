---
title: Ensure path exists
---

<div markdown="1" class="ans">
```python
os.makedirs("path/child", exist_ok=True)
```
</div>

If `exist_ok` is not specified or is `False`, and the target path already exists, then `FileExistsError` is raised.
