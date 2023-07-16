---
title: Reading embedded resource from *.resx* file
generated: true
---

<div markdown="1" class="ans">
```c#
AssemblyNamespace.FolderStructure.ResourceFileName.resource_name
```
</div>

**Example:**
```c#
AssemblyNamespace.Properties.Resources.foo_txt
```

**Notes:**
- **AssemblyNamespace:** is the default namespace of the assembly containing the embedded resource
- **FolderStructure:** is the relative path to the *.resx* file separated by dots (`"."`)
- **ResourceFileName:** is the name of resource file, without *.resx* extension
- **resource_name:** is the name of the resource item inside the resource file
- can only access from another assembly if resource is *public*

Know more:
- [Adding embedded resource to *Resources.resx* file](/en-US/visual-studio/adding-embedded-resource-to-resources-resx-file)
