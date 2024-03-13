---
title: Removing linear tendency (or drift) from data using SciPy
generated: true
---

<div markdown="1" class="ans">
```python
def remove_linear_drift(data):
    x = np.arange(len(data))
    return data - stats.linregress(x, data).slope * x
```
</div>
