---
title: Passing parameters to a string interpolation handler in C#
generated: true
---

<div markdown="1" class="ans">
Annotate the argument receiving the interpolated string handler with the attribute *InterpolatedStringHandlerArgument*:
```c#
public void PrintMessage(
        string color,
        [InterpolatedStringHandlerArgument("", "color")]
        ColorInterpolatedStringHandler builder
    )
```
</div>

**Notes:**
- `""` parameter refers to `this` in that context.
- `"color"` parameter refers to the argument named *color*.
  - The constructor of *ColorInterpolatedStringHandler* must receive both parameters after `int literalLength` and `int formatCount`.

**Know more:**
- [Creating a custom string interpolation handler in C#](/en-US/c-sharp/creating-custom-string-interpolation-handler)
- [Explore string interpolation handlers \| Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/interpolated-string-handler)
