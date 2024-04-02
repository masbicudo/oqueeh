---
title: Creating a range of date-times using NumPy
generated: true
---

<div markdown="1" class="ans">
```python
date_range = np.arange(
        dt.datetime(2024, 1, 1),
        dt.datetime(2025, 1, 1),
        dt.timedelta(days=1),
    )
```
</div>

The element types of the resulting array will be `datetime64`, with dtype `'<M8[us]'`.
