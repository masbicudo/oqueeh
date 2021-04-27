---
generated: true
title: Iterating tags in Jekyll
---

<div markdown="1" class="ans">
{% raw %}
```
{% for tag in page.tags %}
    <span>{{ tag }}</span>
{% endfor %}
```
{% endraw %}
</div>

- for pages, use `page.tags`
- for posts, use `post.tags`
