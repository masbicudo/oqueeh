---
title: Getting the CDF of a distribution given the PDF using Numpy
generated: true
---

<div markdown="1" class="ans">
```python
dX = 0.01 # X distance between values inside PDF
cdf = np.cumsum(pdf*dX)
```
</div>

References:
- [How to plot cdf in matplotlib in Python? - Stack Overflow - stackoverflow.com](https://stackoverflow.com/a/9379432/195417)
