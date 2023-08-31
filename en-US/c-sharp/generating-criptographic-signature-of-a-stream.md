---
title: Generating a criptographic hash of a stream in C#
generated: true
---

<div markdown="1" class="ans">
```c#
using System.Security.Cryptography;
var algorithm = SHA256.Create();
var hash = await algorithm.ComputeHashAsync(stream);
return Convert.ToBase64String(hash);
```
</div>
