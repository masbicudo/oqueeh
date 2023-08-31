---
title: Plotting the distribution from data using SeaBorn and MatPlotLib
generated: true
---

A distribution can be represented by a PDF or a CDF using one of the following functions:

<div markdown="1" class="ans">
```python
import seaborn as sns
sns.kdeplot(data=values, cumulative=True)
sns.histplot(values, bins=15, cumulative=True)
sns.displot(values, kde=True, bins=15, cumulative=False)
```

The *displot* function draws a histogram and a line chart of the distribution.

Parameters:
- **bins:** controls the number of bin for the histogram
- **cumulative:** controls whether to draw PDF or CDF
</div>

References:
- [seaborn.kdeplot — seaborn 0.12.2 documentation - seaborn.pydata.org](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)
