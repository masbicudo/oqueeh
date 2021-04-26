---
title: Read JSON data file in Jekyll
---

<div markdown="1" class="ans">
{% raw %}
```
{% assign var_name = site.data.data_filename["item_name"] %}
```
{% endraw %}
</div>

This assumes a JSON data file named `data_filename.json` in `_data` folder, with content like this:

```json
{
    "item_name": "Miguel Angelo"
}
```
