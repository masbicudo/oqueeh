# First letters to upper

```
text = "miguel angelo"
re.sub(r"\b\w", lambda x: x[0].upper(), text)
```
