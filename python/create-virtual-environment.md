---
title: Create a Python virtual environment
---

<div markdown="1" class="ans">
```
python -m venv env_path
```
</div>

#### With virtualenv package

```
virtualenv env_path
```

#### With Anaconda

```
conda create -p env_path python=3.8
```

Anaconda has problems creating virtual environments inside paths with spaces.
