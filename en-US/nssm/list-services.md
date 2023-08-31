---
title: How to list NSSM services?
generated: true
---

<div markdown="1" class="ans">
```bash
nssm list
```
</div>

*- or -* a more detailed list:

```powershell
Get-WmiObject win32_service | ?{$_.PathName -like '*nssm*'} | select Name, DisplayName, State
```
