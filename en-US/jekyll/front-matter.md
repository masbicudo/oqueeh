---
generated: true
title: Front matter in Jekyll
---

- http://simpleprimate.com/blog/front-matter

<div markdown="1" class="ans">
{% raw %}
```
---
title: Title of the page or post
---
```
{% endraw %}
</div>

The front matter of a Jekyll page is like a header of the file.

It is used to define variables associated with the file.

These variables are then used in various contexts.

The variables go directly into the `page` or `post` variable.

```
{{ page.title }}
```
