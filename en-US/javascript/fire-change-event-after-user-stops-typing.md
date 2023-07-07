---
generated: true
---

<div markdown="1" class="ans">
```js
text_input.addEventListener("keydown", e => {
    clearTimeout(timer)
    timer = setTimeout(() => output.innerText = e.target.value, 1000)
})
```
</div>

HTML:

```html
<input type="text" id="text_input" />
<div id="output"></div>
```
