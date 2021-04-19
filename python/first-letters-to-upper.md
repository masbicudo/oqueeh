# First letters to upper in Python

```
text = "miguel angelo"
re.sub(r"\b\w", lambda x: x[0].upper(), text)
```

## Prerequisites

```
import re
```
