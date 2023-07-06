---
title: ModuleNotFoundError: No module named 'pdm.core'
generated: true
---


<ans>Remove PDM by hand, then reinstall by hand.</ans>

```
cd ~
curl -sSLO https://pdm.fming.dev/dev/install-pdm.py
python install-pdm.py --remove
python install-pdm.py
rm install-pdm.py
```
