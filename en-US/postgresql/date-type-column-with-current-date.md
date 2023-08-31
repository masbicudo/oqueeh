---
title: Creating a Date type column with current date as default value in PostgreSQL
generated: true
---

<div markdown="1" class="ans">
```sql
CREATE TABLE documents (
    ...
    some-Date DATE DEFAULT CURRENT_DATE
    ...
);
```
</div>
