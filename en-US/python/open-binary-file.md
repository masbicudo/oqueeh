---
title: Open binary file in Python
generated: true
---

<div markdown="1" class="ans">
with open("filename.txt", "rb") as fs:
    for line in fs:
        print(line)
</div>

**Remarks:**
Even though lines are a concept of text files, it works with binary files too.

**Know more:**
- [Open text file in Python](/en-US/python/open-text-file)
