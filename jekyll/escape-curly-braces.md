---
title: Escape curly braces in Jekyll
categories: ["Jekyll"]
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

Use this Python program to help escaping these strings [escape-curly-braces.py]({% link /Jekyll/escape-curly-braces.py %})
