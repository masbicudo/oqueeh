---
title: Command line arguments in Python
---

<div markdown="1" class="ans">
```python
for arg in sys.argv:
    print(arg)
```
</div>

`sys.argv[0]` is the python script name.

The script name can be **absolute** or **relative** depending on how the script was started:

- `python3 some.py`

    `sys.argv[0]` will be `"some.py"`

- `python3 /home/masbicudo/some.py`

    `sys.argv[0]` will be `"/home/masbicudo/some.py"`

#### Prerequsite

```python
import sys
```
