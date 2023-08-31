---
title: Cache function data in disk using StreamLit
generated: true
---

<div markdown="1" class="ans">
Use atribute *cache_data* with argument `persist="disk"`.

```python
import streamlit as st
@st.cache_data(persist="disk")
def get_some_data():
    # ... function code!
    return result
```
</div>

**Know more:**
- [Cache data from a function between runs in StreamLit](/en-US/streamlit/cache-data-from-function-between-runs)
- [Clear cache of a specific cached function in StreamLit](/en-US/streamlit/clear-cache-for-function)

**Reference:**
- [st.cache_data - Streamlit Docs - docs.streamlit.io](https://docs.streamlit.io/library/api-reference/performance/st.cache_data)
