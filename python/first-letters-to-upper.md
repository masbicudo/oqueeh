---
title: First letters to upper in Python
---

<div markdown="1" class="ans">
```python
text = "miguel angelo"
re.sub(r"\b\w", lambda x: x[0].upper(), text)
```
</div>

## Prerequisites

```python
import re
```
