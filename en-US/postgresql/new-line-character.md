---
title: New line character in PostgreSQL
generated: true
---

<div markdown="1" class="ans">
```sql
SELECT 'a' || chr(10) || 'b'
SELECT 'a' || E'\n' || 'b'
```
</div>

**Know more:**
- [Escaping characters in String literal in PostgreSQL](/en-US/postgresql/escaping-characters-in-string-literal)
- [Enter and search for new-line character in JSONB column in PostgreSQL](/en-US/postgresql/enter-and-search-new-line-character-in-jsonb)
