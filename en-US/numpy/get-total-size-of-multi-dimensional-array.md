---
title: Get total size/length of multi-dimensional array using NumPy
generated: true
---

<div markdown="1" class="ans">
Use *size* property, instead of *len* function.
```python
a.size
```
</div>

**Remarks:**

Python's `len` function will not give number of elements in NumPy multi-dimensional array.

`size` property is the multiplication of all items in `shape` property.

**References:**
- [numpy.ndarray.size — NumPy v1.26 Manual](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html)
