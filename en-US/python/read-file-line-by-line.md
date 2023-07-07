---
title: Read a file line by line in Python
---

<div markdown="1" class="ans">
```python
with open(filename, "r") as fs:
    for line in fs:
        pass
```
</div>

Each `line` might be terminated with a `\n` to indicate that there is another line after itself.

A line that terminates at EOF will not have a `\n`.

#### Remove the new-line character

```python
line = line.rstrip("\n")
```
