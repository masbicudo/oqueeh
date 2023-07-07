---
title: Rest parameters in JavaScript
generated: true
---

```js
function fn(a, b, ...others) {
    console.log(a, b, others)
}
```

Rest parameter is denoted by three dots before last parameter.
It receives all extra parameters passed.

#### Example:

```js
fn(1,2,5,8)
```

Output: `1 2 [ 5, 8 ]`
