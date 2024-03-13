---
title: Convert datetime to datetime64 format in NumPy
generated: true
---

<div markdown="1" class="ans">
```python
np.datetime64(dt.datetime(2024, 3, 31)) # dtype('<M8[us]')
pd.datetime64(dt.date(2024, 3, 31)) # dtype('<M8[D]')
```
</div>

**Related:**
- [Convert datetime to Timestamp format in Pandas](/en-US/pandas/convert-datetime-to-timestamp)
- [Converting datetime64 formats using NumPy](/en-US/numpy/converting-datetime64-formats)
