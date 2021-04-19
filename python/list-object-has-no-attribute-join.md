# 'list' object has no attribute 'join'

Correct way:

```python
",".join([1, 2, 3])
```

Wrong way:

```python
[1, 2, 3].join(",")
```
