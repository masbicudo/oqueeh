---
title: Making an object iterable in JavaScript
generated: true
---

```js
obj = {}
obj[Symbol.iterator] = function* () {
    yield 1
    yield 2
}
```

Iterables can be used in `for`..`of` statements, and with spread operator:

```js
for (let x of iterable) console.log(x)
console.log([...iterable])
```

- javascript/iterables-usage.md
