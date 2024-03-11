---
title: Better performance with compiled regex in Python
generated: true
---
<div markdown="1" class="ans">
```python
pattern = re.compile(r"brown (\w+)")
```
</div>

Available `pattern` functions: `match`, `search`, `fullmatch`, `split`, `sub`, `findall`, `finditer` and `subn`.

Each function has one less parameter for the pattern string.

```python
pattern.sub(r"\1", "The brown fox jumps!")
```


#### Reference

[re — Regular expression operations — Python 3.12.2 documentation](https://docs.python.org/3/library/re.html#regular-expression-objects)
