---
title: Read CSV data file in Jekyll
---

<div markdown="1" class="ans">
{% raw %}
```
{% assign var_name = site.data.data_filename[0].name %}
```
{% endraw %}
</div>

This assumes a CSV data file named `data_filename.csv` in `_data` folder, with content like this:

```csv
name,age
Miguel Angelo,36
```
