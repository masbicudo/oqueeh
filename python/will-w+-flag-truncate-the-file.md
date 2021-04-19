# Will "w+" flag truncate the file in Python

Yes.

The following code truncates `filename.txt`:

```
with open("filename.txt", "w+"):
    pass
```
