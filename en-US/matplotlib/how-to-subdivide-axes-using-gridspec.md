---
title: How to subdivide Axes using GridSpec in PyPlot?
generated: true
---
<div markdown="1" class="ans">
```python
import matplotlib.gridspec as gridspec
gs = ax.get_gridspec()
subgs = gridspec.GridSpecFromSubplotSpec(
    2, 2,
    subplot_spec=gs,
    wspace=0.1, hspace=0.1)
for it in range(len(subgs))
    ax = plt.Subplot(fig, inner[it])
    # ax.plot(...)
```
</div>

**Know more:**
- [How to get the GridSpec from Axes in PyPlot?](/en-US/matplotlib/how-to-get-gridspec-from-axes)
