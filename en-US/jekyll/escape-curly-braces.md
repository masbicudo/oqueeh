---
title: Escape curly braces in Jekyll
---

## One or more curly braces in sequence

```
{{"{{"}}"{{"{{{"}}"}}
```

#### Output:

{{"{{{"}}

## An entire block of text

```
{{ "{%" }} raw %}
Text {{ "{{" }} example }} here.
{{ "{%" }} endraw %}
```

#### Output:

{% raw %}
Text {{ example }} here.
{% endraw %}

Use this Python program to help escaping these strings [escape-curly-braces.py]({% link /en-US/jekyll/escape-curly-braces.py %})
