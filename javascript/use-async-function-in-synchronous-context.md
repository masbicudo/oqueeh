---
generated: true
---

<div markdown="1" class="ans">
```js
promise.then(data => proc(data))
```
</div>

#### Alternative

```js
(async () => proc(await promise))()
```
