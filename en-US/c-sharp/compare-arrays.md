---
title: Comparing arrays in C#
generated: true
---

<div markdown="1" class="ans">
```c#
Enumerable.SequenceEquals(array1, array2)
```
*-or-*
```c#
array1.AsSpan().SequenceEqual(array2)
```
</div>

**References:**
- https://code-maze.com/csharp-compare-arrays/
