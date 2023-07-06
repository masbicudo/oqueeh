---
title: How to check CloudAPI offline status?
generated: true
---

<div markdown="1" class="ans">
```c#
var FILE_ATTRIBUTES_RECALL_ON_DATA_ACCESS = 4194304;
var isNotReady = (File.GetFileInfo(filePath)
    & FILE_ATTRIBUTES_RECALL_ON_DATA_ACCESS) != 0;
```
</div>
