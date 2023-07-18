---
title: What are __enter__ and __exit__ functions in Python
generated: true
---

<div markdown="1" class="ans">
- Manage the usage of resources which need to be freed.
- `__enter__` allocates the resource
- `__exit__` release the resource
</div>

**Notes:**
- Can be used to create code-blocks in which a context is valid.
