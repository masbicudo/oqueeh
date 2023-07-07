---
generated: true
title: Drop table if it exists in PostgreSQL
---

<div markdown="1" class="ans">
```sql
DROP TABLE IF EXISTS table_name
```
</div>

Multiple table names can be specified.

#### Cascade drop dependent objects

```sql
DROP TABLE IF EXISTS table_name CASCADE
```
