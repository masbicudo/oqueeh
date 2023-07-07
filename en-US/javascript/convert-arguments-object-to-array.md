---
title: Convert arguments object to Array in JavaScript
generated: true
---

<div markdown="1" class="ans">
```js
function fn(...args) {
}
```
</div>

Rest parameters are represented by the three dots before the last parameter.
It receives all extra arguments as an Array.

#### Alternative: spread into Array

```js
[...arguments]
```

#### Alternative: Array.from

```js
Array.from(arguments)
```

#### ES5

```js
Array.prototype.slice.call(arguments)
```

- [Convert iterable object to Array in JavaScript](en-US/javascript/convert-iterable-object-to-array.md)
