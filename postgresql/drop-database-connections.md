---
generated: true
title: Drop database connections in PostgreSQL
---

<div markdown="1" class="ans">
```sql
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'db_name'
```
</div>
