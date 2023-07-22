---
title: String concatenation in PosgreSQL
generated: true
---

<div markdown="1" class="ans">
```sql
SELECT 'a' || 'b'
```
*-or-*
```sql
SELECT concat('a', 'b')
```
*-or-*
```sql
SELECT concat_ws(',', 'a', 'b')
```
</div>

*concat_ws* stands for concatenate with separator.

**Know more:**
- [String concatenation aggregation in PostgreSQL](/en-US/postgresql/string-concatenation-aggregation)

**References:**
- https://www.postgresqltutorial.com/postgresql-string-functions/postgresql-concat-function/
