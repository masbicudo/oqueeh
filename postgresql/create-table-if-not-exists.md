---
generated: true
title: Create table if it does not exist in PostgreSQL
---

<div markdown="1" class="ans">
```sql
CREATE TABLE IF NOT EXISTS table_name
```
</div>

---
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
