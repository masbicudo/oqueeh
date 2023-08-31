---
title: How to download a file from the Internet using C#?
generated: true
---

<div markdown="1" class="ans">
```c#
using System.Net;
using (WebClient webClient = new WebClient())
    webClient.DownloadFile(remoteUrl, localDestination);
```
*-or-*
```c#
using (HttpClient client = new HttpClient())
{
    var contents = await client.GetStringAsync(url1);
    await File.WriteAllTextAsync(filePath, contents);
}
```
</div>
