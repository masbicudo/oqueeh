---
title: Escaping characters in String literal in PostgreSQL
generated: true
---

<div markdown="1" class="ans">
There is a special escaped string representation in PostgreSQL:
```sql
SELECT 'line1' || E'\n' || 'line2'
SELECT E'lin 1\nline 2'
```
</div>

**Know more:**
- [New line character in PostgreSQL](/en-US/postgresql/new-line-character)
- [Enter and search for new-line character in JSONB column in PostgreSQL](/en-US/postgresql/enter-and-search-new-line-character-in-jsonb)
