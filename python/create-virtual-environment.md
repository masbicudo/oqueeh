---
title: Create a Python virtual environment
---

<div markdown="1" class="ans">
```
python -m venv env_path
```
</div>

#### With virtualenv package

<div markdown="1" class="ans">
```
virtualenv env_path
```
</div>

#### With Anaconda

<div markdown="1" class="ans">
```
conda create -p env_path python=3.8
```
</div>

Anaconda has problems creating virtual environments inside paths with spaces.
