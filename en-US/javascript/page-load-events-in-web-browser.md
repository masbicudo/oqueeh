---
title: Page load events in web browser JavaScript
generated: true
---

<div markdown="1" class="ans">
1. document.readystate = interactive
2. document.DOMContentLoaded
3. document.readystate = complete
4. window.load
</div>

#### Adding the event listeners

```js
window.addEventListener('load',
    e => console.log('window.load'))
document.addEventListener('readystatechange',
    e => console.log(`document.readystate = ${document.readyState}`))
document.addEventListener('DOMContentLoaded',
    e => console.log('document.DOMContentLoaded'))
```

#### Reference

[Document: DOMContentLoaded event - Web APIs \| MDN - developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event)
