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

**References:**
- [FileAttributes Enumeração (System.IO) \| Microsoft Learn](https://learn.microsoft.com/pt-br/dotnet/api/system.io.fileattributes?view=net-7.0)
- [File Attribute Constants (WinNT.h) - Win32 apps \| Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants)
