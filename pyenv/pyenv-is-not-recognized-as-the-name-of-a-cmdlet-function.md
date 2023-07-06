---
title: 'pyenv' is not recognized as the name of a cmdlet, function
generated: true
---

<div markdown="1" class="ans">
Reinstall PyEnv-Win:
```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```
</div>

See [pyenv for Windows](https://github.com/pyenv-win/pyenv-win)
