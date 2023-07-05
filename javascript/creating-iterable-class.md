---
title: Creating an iterable class in JavaScript
generated: true
---

<div markdown="1" class="ans">
```js
class Class {
    *[Symbol.iterator]() {
        yield 1
        yield 2
    }
}
```
</div>

Iterables can be used in `for`..`of` statements, and with spread operator:

```js
for (let x of iterable) console.log(x)
console.log([...iterable])
```

- javascript/iterables-usage.md
