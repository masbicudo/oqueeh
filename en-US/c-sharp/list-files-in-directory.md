---
title: List files in directory in C#
generated: true
---

<div markdown="1" class="ans">
```c#
var allfiles = Directory.GetFiles(
        "D:\",
        "*",
        SearchOption.AllDirectories
    );
```
</div>

**Remarks:**

This may fail with *UnauthorizedAccessException* if any path in the structure requires privileges you don't have.

If you need directories too, use `Directory.GetFileSystemEntries`.
