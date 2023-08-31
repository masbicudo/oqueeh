---
title: Clear cache of a specific cached function in StreamLit
generated: true
---

<div markdown="1" class="ans">
Just call clear function on the cached function itself.

```python
get_some_data.clear()
```
</div>

```python
import streamlit as st
@st.cache_data
def get_some_data():
    # ... function code
    return result
```

**Know more:**
- [Cache data from a function between runs in StreamLit](/en-US/streamlit/cache-data-from-function-between-runs)
- [Cache function data in disk using StreamLit](/en-US/streamlit/cache-function-data-in-disk)

**Reference:**
- [st.cache_data - Streamlit Docs - docs.streamlit.io](https://docs.streamlit.io/library/api-reference/performance/st.cache_data)
