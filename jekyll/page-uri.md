---
title: Page URI in Jekyll
---

<div markdown="1" class="ans">
{% raw %}
```
{{ page.url }}
```
{% endraw %}
</div>

First character of page URI is `"/"`.

This is the URI path, including filename.

#### Example output:

{{ page.url }}

#### See also:

- [Page path in Jekyll]({% link jekyll/page-path.md %})
