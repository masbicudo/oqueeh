---
title: Enter and search for new-line character in JSONB column in PostgreSQL
generated: true
---

<div markdown="1" class="ans">
```sql
with sample_table(jsonb_column) as (
    values ('{"data": "line 1\nline 2"}'::jsonb)
)
select *
from sample_table
where jsonb_column->>'data' ~ '^.*\n.*$'
```
</div>

The escaped string '\n' has no special meaning in PostgreSQL,
but it has a meaning inside JSONB column.

If you try to enter a new line character (`chr(10)`) in a JSONB column,
there will be an error stating:
- Character with value 0x0a must be escaped.

**Know more:**
- [Escaping characters in String literal in PostgreSQL](/en-US/postgresql/escaping-characters-in-string-literal)
- [New line character in PostgreSQL](/en-US/postgresql/new-line-character)
