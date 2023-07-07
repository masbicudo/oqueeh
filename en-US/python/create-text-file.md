---
title: Create a text file in Python
---

<div markdown="1" class="ans">
```python
with open("filename.txt", "w") as fs:
    fs.write("Some text")
```
</div>

This overwrites the file if it exists.
