---
title: Aligning equations to the left with indent using MathJax
generated: true
---

<div markdown="1" class="ans">
```css
.MathJax {
    margin-left: 2em !important;
}
```

*=or=*

```js
MathJax.Hub.Config({
    jax: ["input/TeX","output/HTML-CSS"],
    displayIndent: "2em"
});
```
</div>
