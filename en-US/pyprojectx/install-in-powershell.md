---
title: Installing Pyprojectx using PowerShell
generated: true
---

<div markdown="1" class="ans">
```powershell
Invoke-WebRequest https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip -OutFile wrappers.zip; Expand-Archive -Force -Path wrappers.zip -DestinationPath .; Remove-Item -Path wrappers.zip
```
</div>

Then setup files in Git:
```bash
git add pw pw.bat
git update-index --chmod=+x pw
echo .pyprojectx/ >> .gitignore
```

**Know more:**
- [Installing Pyprojectx using Bash](/en-US/pyprojectx/install-in-bash)
- [Initializing a Python project using Pyprojectx](/en-US/pyprojectx/initialize)
