---
title: Parsing HTML using HtmlAgilityPack
generated: true
---

<div markdown="1" class="ans">
```c#
var parser = new HtmlDocument();
parser.LoadHtml(html);
var linkElements = parser.DocumentNode.SelectNodes("//a[@href]");
```
</div>

**Know more:**
- [Parsing HTML using CSS selectors with HtmlAgilityPack and Fizzler](/en-US/c-sharp/parsing-html-using-fizzler-extensions-for-html-agility-pack)
- [What is HtmlAgilityPack?](/en-US/dot-net/what-is-html-agility-pack)
