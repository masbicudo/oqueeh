---
title: Parsing HTML5 using Angle Sharp
generated: true
---

<div markdown="1" class="ans">
```c#
var parser = new HtmlParser();
var document = await parser.ParseDocumentAsync(html);
var linkElements = document.QuerySelectorAll("a");
```
</div>

**Know more:**
- [AngleSharp - Documentation - anglesharp.github.io](https://anglesharp.github.io/)
- [What is AngleSharp?](/en-US/dot-net/what-is-angle-sharp)
