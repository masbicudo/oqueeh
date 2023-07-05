---
title: Get all capture groups from regex match in Python
generated: true
---
<div markdown="1" class="ans">
```python
match.groups()
```
</div>

#### Example

```python
match = re.match(r"(\d+)(\w+)", "123abc")
print(match.groups())
```

Output: `('123', 'abc')`

#### Prerequisite

```python
import re
```

#### Reference

- https://docs.python.org/3/library/re.html#re.Match.groups
