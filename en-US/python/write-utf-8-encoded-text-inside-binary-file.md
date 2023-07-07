---
title: Write UTF-8 encoded text inside binary file in Python
generated: true
---

<div markdown="1" class="ans">
```python
content = "MASBicudo"
bytes_utf8 = content.encode("utf-8")
with open("filename.txt", "wb") as fs:
    fs.write(bytes_utf8)
```
</div>

`str` has the `encode` method, that returns `bytes` with the encoded string.
