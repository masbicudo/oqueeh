---
title: Load file as data-URI
generated: true
---

<div markdown="1" class="ans">
#### JavaScript

```javascript
function openFile(event, target_element) {
    const reader = new FileReader()
    reader.onload = () => target_element.innerText = reader.result
    reader.readAsDataURL(event.target.files[0])
}
window.addEventListener('load', e =>
```

#### HTML

```html
<div id='output'></div>
```
</div>
