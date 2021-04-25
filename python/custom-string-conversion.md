---
title: Custom string conversion in Python
---

<div markdown="1" class="ans">
```python
class Some(object):
    def __str__(self):
        return "Some class"
```
</div>

### Usage example

#### 1.
```python
sm = Some()
print(sm)
```

`print` automatically converts argument to string.

#### 2.
```python
sm = Some()
s = str(sm)
```
