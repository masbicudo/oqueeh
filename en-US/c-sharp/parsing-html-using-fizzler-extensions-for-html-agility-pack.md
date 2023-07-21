---
title: Parsing HTML using CSS selectors with HtmlAgilityPack and Fizzler
generated: true
---

*Fizzler* is a library that contains extensions for *HtmlAgilityPack*
that allows using CSS selectors instead of XPath.
<div markdown="1" class="ans">
```c#
var parser = new HtmlDocument();
parser.LoadHtml(html);
var linkElements = parser.DocumentNode.QuerySelectorAll("a");
```
</div>

**Know more:**
- [GitHub - atifaziz/Fizzler: .NET CSS Selector Engine](https://github.com/atifaziz/Fizzler)
- [What is HtmlAgilityPack?](/en-US/dot-net/what-is-html-agility-pack)
