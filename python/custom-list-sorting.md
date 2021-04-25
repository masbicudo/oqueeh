---
title: Custom list sorting in Python
categories: [Python]
---

<div markdown="1" class="ans">
```python
sl = sorted(["The", "lazy", "fox"], key=str.upper)
```
</div>

### Using a lambda
<div markdown="1" class="ans">
```python
sl = sorted(["The", "lazy", "fox"], key=lambda x: x[1])
```
</div>

This will sort by the second letter of each word.
