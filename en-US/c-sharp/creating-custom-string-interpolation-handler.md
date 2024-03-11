---
title: Creating a custom string interpolation handler in C#
generated: true
---

Create a class with the following:
<div markdown="1" class="ans">
- Attribute *InterpolatedStringHandler* applied to the class
- Constructor with parameters `int literalLength` and `int formatCount`
- Public methods *AppendLiteral* and *AppendFormatted*:
  - `public void AppendLiteral(string s)`
  - `public void AppendFormatted<T>(T t)`
</div>

**Notes:**
- *AppendFormatted* may have additional parameters `int alignment` and `string format`:
  - e.g. when using `$"{value,-15:red}"`
- The methods may return *bool* to stop interpolation at any point.

**Know more:**
- [Passing parameters to a string interpolation handler constructor in C#](/en-US/c-sharp/passing-parameters-to-interpolation-handler-constructor)

**References:**
- [Explore string interpolation handlers - C# \| Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/interpolated-string-handler)
