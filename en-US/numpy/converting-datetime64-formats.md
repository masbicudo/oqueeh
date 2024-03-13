---
title: Converting datetime64 formats using NumPy
generated: true
---

<div markdown="1" class="ans">
dt64d.astype("<M8[us]")
dt64ns.astype("<M8[D]")
</div>

**Remarks:**
NumPy can store date and times in multiple formats inside datetime64.
The stored int64, which can be accessed using `value` property may be different even if the represented date is the same.

**Related:**
- [Convert datetime to datetime64 format in NumPy](/en-US/numpy/convert-datetime-to-datetime64)
