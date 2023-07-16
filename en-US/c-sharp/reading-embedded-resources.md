---
title: Reading embedded resources in C#
generated: true
---

<div markdown="1" class="ans">
```c#
var assembly = Assembly.GetExecutingAssembly();
var resourceName = "AssemblyNamespace.FolderNamespace.FileName";
using (Stream stream = assembly.GetManifestResourceStream(resourceName))
```
</div>

- **AssemblyNamespace:** the default root namespace of the assembly containing the embedded resource
- **FolderNamespace:** path for the file inside the project with dots (`"."`) separating path items
- **FileName:** name of the file including extension

Know more:
- [Embedding resource files in Visual Studio](/en-US/visual-studio/embedding-resource-files)
- [Listing embedded resources in C#](/en-US/c-sharp/listing-embedded-resources)
