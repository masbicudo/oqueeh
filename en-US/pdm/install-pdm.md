---
title: How to install PDM
generated: true
---


<div markdown="1" class="ans">
On Windows:

```powershell
(Invoke-WebRequest -Uri https://pdm.fming.dev/install-pdm.py -UseBasicParsing).Content | python -
```

On Linux/Mac:

```bash
curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -
```
</div>

```bash
cd ~
curl -sSLO https://pdm.fming.dev/dev/install-pdm.py
python install-pdm.py --remove
python install-pdm.py
rm install-pdm.py
```
