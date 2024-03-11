---
title: Passing parameters to a string interpolation handler constructor in C#
generated: true
---

Annotate the argument receiving the interpolated string handler with the attribute *InterpolatedStringHandlerArgument*, for example:

<div markdown="1" class="ans">
```c#
public void PrintMessage(
    string color,
    [InterpolatedStringHandlerArgument("", "color")]
    ColorInterpolatedStringHandler builder
  )
```
</div>

**Remarks:**
- `""` parameter refers to `this` in that context.
- `"color"` parameter refers to the argument named *color*.
  - The constructor of *ColorInterpolatedStringHandler* must receive both parameters:
    e.g. `ctor(int literalLength, int formatCount, MyClass my, string color)`

**Know more:**
- [Creating a custom string interpolation handler in C#](/en-US/c-sharp/creating-custom-string-interpolation-handler)

**References:**
- [Explore string interpolation handlers - C# \| Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/interpolated-string-handler)
