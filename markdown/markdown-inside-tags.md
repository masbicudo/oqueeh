---
title: Markdown inside tags
---

<div markdown="1" class="ans">
```markdown
<div markdown="1">
Something **interesting**.
</div>
```
</div>

Works with GitHub pages. Visual Studio Code won't recognize it though.

Does not work with all tags. What I tested: works with `div` and `pre`.
Does not work with `a`, and custom tags, e.g. `ans`.
