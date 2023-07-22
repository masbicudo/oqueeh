---
title: Enter and search for new-line character in JSONB column in PostgreSQL
generated: true
---

<div markdown="1" class="ans">
```sql
select distinct on (column1) column1, column2
from sample_table
```
*-or-*
```sql
select column1, max(column2)
from sample_table
group by column1
```
</div>

These examples return one of the values aggregated in *column2*.
While the first example will return the first that it finds,
the second will return the maximum value, which is one of the values.

**References:**
- [postgresql - Aggregate function that returns any value for a group - Stack Overflow - stackoverflow.com](https://stackoverflow.com/questions/42556344/aggregate-function-that-returns-any-value-for-a-group)
