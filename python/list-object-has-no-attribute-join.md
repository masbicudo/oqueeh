---
title: "'list' object has no attribute 'join'"
categories: [Python]
---

Correct way:

<div markdown="1" class="ans">
```python
",".join([1, 2, 3])
```
</div>

Wrong way:

```python
[1, 2, 3].join(",")
```
