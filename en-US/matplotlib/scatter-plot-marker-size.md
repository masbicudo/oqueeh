---
title: How to change marker size in a scatter plot in MatPlotLib?
generated: true
---

<div markdown="1" class="ans">
Use *s* parameter with a single size value or an array of sizes:
```python
import matplotlib.pyplot as plt
plt.scatter(x=xs, y=ys, s=sizes, c=colors)
```
</div>

**Know more:**
- [Creating a scatter plot using MatPlotLib](/en-US/matplotlib/creating-scatter-plot)

**Reference:**
- [matplotlib.pyplot.scatter — Matplotlib 3.7.2 documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
