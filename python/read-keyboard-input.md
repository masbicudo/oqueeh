---
title: Read keyboard input in Python
tags: [python,keyboard,input]
categories: [Python]
---

<div markdown="1" class="ans">
```python
input()
```
</div>

`input` can be passed a string to show as a prompt.

## With sys

<div markdown="1" class="ans">
```python
import sys
sys.stdin.readline()
```
</div>

`readline` will keep a `'\n'` at the end of the string.
