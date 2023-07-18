---
title: Redirect output of child process using C#
generated: true
---

```c#
var process = Process.Start(
    new ProcessStartInfo("ping", "google.com") {
        UseShellExecute = false,
        RedirectStandardOutput = true,
        RedirectStandardError = true,
        RedirectStandardInput = true });
Console.WriteLine(process.StandardOutput.ReadToEnd());
```

**Notes:**
- `UseShellExecute` must be false, otherwise reading from `StandardOutput` throws an exception.
- `RedirectStandardInput` may be needed even if you don't need to redirect input stream.

**References:**
- [ProcessStartInfo.RedirectStandardOutput Property (System.Diagnostics) \| Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.redirectstandardoutput?view=net-7.0)
- [Blog \| 7th Zero - 7thzero.com](https://7thzero.com/blog/)
process-startinfo-redirectstandardoutput-not-quite-what-you-d-ex
