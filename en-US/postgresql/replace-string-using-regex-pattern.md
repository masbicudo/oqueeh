---
title: Replace string using regex pattern in PostgreSQL
generated: true
---

<div markdown="1" class="ans">
```sql
regexp_replace(string_value, '(\w)s*=\s*(\d)', '\1', 'g')
```
</div>

The previous example extracts the name of a variable being assigned inside the text of *string_value*.
