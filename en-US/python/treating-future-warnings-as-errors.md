---
title: Treating `FutureWarning` as errors in Python
generated: true
---

<div markdown="1" class="ans">
```python
warnings.simplefilter('error', FutureWarning)
```
</div>

**Remarks:**
You can undo the change using:
```python
warnings.simplefilter('default', FutureWarning)
```

**References:**
- [Whats actions are available for `warnings.simplefilter` in Python](/en-US/python/what-actions-are-available-in-warnings-simplefilter)
