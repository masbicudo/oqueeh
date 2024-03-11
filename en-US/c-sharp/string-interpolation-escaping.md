---
title: String interpolation escaping in C#
generated: true
---

<div markdown="1" class="ans">
```c#
$$"{someValue}: {{"{{"}}someValue:0.0}}"
```
*-or-*
```c#
$"{{"{{"}}someValue}}: {someValue:0.0}"
```
</div>

**Notes:**
- Use multiple *$* to denote that braces (*{* and *}*)should be also the same multiple.

**Know more:**
- [$ - string interpolation - format string output - C# \| Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated)
