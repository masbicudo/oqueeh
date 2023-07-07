---
title: Assign the output of a command to a variable
generated: true
---

<div markdown="1" class="ans">
```bat
FOR /F "tokens=*" %%A IN ('dir "."') DO (
    SET var=%%A
)
ECHO %var%
```
</div>
