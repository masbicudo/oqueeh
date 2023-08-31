---
title: Installing Pyprojectx using Bash
generated: true
---

<div markdown="1" class="ans">
```bash
curl -LO https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip && unzip -o wrappers.zip && rm -f wrappers.zip
```
</div>

Then setup files in Git:
```bash
git add pw pw.bat
git update-index --chmod=+x pw
echo .pyprojectx/ >> .gitignore
```

**Know more:**
- [Installing Pyprojectx using PowerShell](/en-US/pyprojectx/install-in-powershell)
- [Initializing a Python project using Pyprojectx](/en-US/pyprojectx/initialize)
