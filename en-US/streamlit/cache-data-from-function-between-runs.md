---
title: Cache data from a function between runs in StreamLit
generated: true
---

<div markdown="1" class="ans">
```python
import streamlit as st
@st.cache_data
def get_some_data():
    # ... do something here!
    return result
```
</div>

**Know more:**
- [Clear cache of a specific cached function in StreamLit](/en-US/streamlit/clear-cache-for-function)
- [Cache function data in disk using StreamLit](/en-US/streamlit/cache-function-data-in-disk)

**Reference:**
- [st.cache_data - Streamlit Docs - docs.streamlit.io](https://docs.streamlit.io/library/api-reference/performance/st.cache_data)
