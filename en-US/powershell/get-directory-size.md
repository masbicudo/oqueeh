---
title: Get directory size in PowerShell
generated: true
---

<div markdown="1" class="ans">
Example - measuring Documents folder:
```powershell
ls -r ~/Documents | measure -sum Length
```
</div>

You can do it from CMD:
```bash
powershell -noprofile -command "ls -r ~/Documents | measure -sum Length"
```
