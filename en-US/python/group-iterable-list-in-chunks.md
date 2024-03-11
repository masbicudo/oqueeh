---
title: Group iterable sequence in chunks of N elements in Python
generated: true
---

<div markdown="1" class="ans">
```python
import itertools as it
def grouped(chunk_size, sequence):
    iterable = iter(sequence)
    return iter(lambda: (*it.islice(iterable, chunk_size),), ())
```
</div>
