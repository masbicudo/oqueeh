---
title: Execute command in new tab in Windows Terminal
generated: true
---

<div markdown="1" class="ans">
```
wt -w 0 nt cmd /K echo MASBicudo
```
</div>

#### Using a profile

```
wt -w 0 nt -p "Prompt de comando" cmd /K echo MASBicudo
```

The profile name is not culture invariant, so using it in scripts could be a problem.

#### Reference

- [Windows Terminal command line arguments \| Microsoft Docs](https://docs.microsoft.com/en-us/windows/terminal/command-line-arguments?tabs=windows)
