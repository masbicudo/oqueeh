---
title: Save object to JSON in Python
---

<div markdown="1" class="ans">
```python
with open(json_filename, "w") as fs:
    json.dump(obj, fs, indent=2, sort_keys=True, separators=(',', ':'))
```
</div>

If `indent` is absent, then all JSON is written in one single line.

The default `separator` puts a space after `:`. In above example, we specify the option `':'` without a space.

## Prerequisite

```python
import json
```
