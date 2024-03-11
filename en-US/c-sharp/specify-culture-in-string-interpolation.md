---
title: How to specify culture in a C# interpolated string?
generated: true
---

<div markdown="1" class="ans">
Use the conversion to *FormattableString* or *IFormattable*:
```c#
FormattableString message = $"Value is {value}";
message.ToString(specificCulture);
```
</div>

**Know more:**
- [$ - string interpolation - format string output - C# \| Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated)
