---
generated: true
title: Remove item from tuple in Python
---

```python
t1 = (0, 1, 2, 3, 4)
t2 = t1[:2] + t1[3:]
```

This removes item at index 2.
`t2` will contain `(0, 1, 3, 4)`.

Tuples are **immutable**, so the resulting tuple is a new tuple.
The value must be assigned back to the original variable to replace the old tuple.

#### Remove last item from tuple:

```python
t2 = t1[:-1]
```

#### Remove first item from tuple:

```python
t2 = t1[1:]
```
