---
title: Using asynchronous functions with Array map in JavaScript
generated: true
---

<div markdown="1" class="ans">
```js
fna = async (data) => Promise.resolve(data)
promise_list = [1,2,3,4].map(async (x) => (await fna(x)) + 10)
Promise.all(promise_list).then(all_data => console.log(all_data))
```
</div>

`Promise.all` returns a promise that resolves with the values of all listed promises.
