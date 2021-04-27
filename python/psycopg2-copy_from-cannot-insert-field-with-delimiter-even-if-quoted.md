---
generated: true
title: psycopg2 copy_from cannot insert field with delimiter, even if quoted
---

`copy_from` does not support CSV field quoting. Use `copy_expert` instead:

<div markdown="1" class="ans">
```python
cur.copy_expert(f"""
    COPY {tablename} (col1, col2, ...)
    FROM STDIN
    WITH (FORMAT CSV)
""", csv_file_stream)
```
</div>
