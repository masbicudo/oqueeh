---
title: Detect offline or not synchronized files
generated: true
---

<div markdown="1" class="ans">
```c#
const FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS
    = (FileAttributes)4194304; // (0x00400000)
var attributes = (File.GetAttributes(filename)
    & FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS) != 0;
```
</div>

**Know more:**
- [FileAttributes Enumeração (System.IO) \| Microsoft Learn](https://learn.microsoft.com/pt-br/dotnet/api/system.io.fileattributes?view=net-7.0)
- [File Attribute Constants (WinNT.h) - Win32 apps \| Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants)
