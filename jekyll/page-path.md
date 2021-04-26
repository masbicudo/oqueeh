---
title: Page path in Jekyll
---

<div markdown="1" class="ans">
{% raw %}
```
{{ page.dir }}
```
{% endraw %}
</div>

First and last character of page path is `"/"`.

This is the path into the generated site output.
It corresponds to the URI path, without filename.

`dir` can be overwritten by placing a `permalink` in front matter of page.

#### Example output:

{{ page.dir }}

#### See also:

- [Page URI in Jekyll]({% link jekyll/page-uri.md %})
