---
title: Regex replace with reference to capture group in Python
---

<div markdown="1" class="ans">
```python
s = re.sub(r"(\d+)", r"Number is: \1", text)
```
</div>

Note that it's not possible to use `r"\0"` to reference the whole capture.
`r"\0"` means character code 0, or null character.

## Prerequisite

```python
import re
```
