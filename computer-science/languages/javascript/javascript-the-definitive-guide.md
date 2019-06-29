### Javascript
var sleep = require('sleep');
sleep.sleep(10); // sleep for ten seconds

Unlike many languages, JavaScript does not make a distinction between `integer` values and `floating-point` values. All numbers in JavaScript are represented as floating-point values. JavaScript represents numbers using the `64-bit floating-point format` defined by the IEEE 754 standard

A string is an immutable ordered sequence of 16-bit values. `string` is a primitive type.

The temporary objects created when you access a property of a string, number, or boolean are known as `wrapper objects`

The typeof operator will also show you the difference between a `primitive value` and its `wrapper object`.

constructors for wrapper objects, When invoked without the new operator, however, they work as conversion functions

`native object`: object in an ECMAScript implementation whose semantics are fully defined by this specification rather than by the host environment.

`host object`: object supplied by the host environment to complete the execution environment of ECMAScript. Any object that is not native is a host object.

#### Objects to primitive conversion
all objects (including arrays and functions) convert to `true`. This is so even for `wrapper objects`: `new Boolean(false)` is an object rather than a primitive value, and so it converts to `true`.

To convert an object to a string, JavaScript uses `toString` or `valueOf`. To convert an object to a number, JavaScript does the same thing, but it tries the `valueOf()` method first. The details of this object-to-number conversion explain why an empty array converts to the number 0 and why an array with a single element may also convert to a number.

The object-to-primitive conversion used by `+` and `==` includes a special case for `Date` objects. The object-to-primitive conversion is basically an `object-to-number conversion (valueof() first)` for all objects that are not `dates`, and an `object-to-string conversion (toString() first)` for `Date` objects. The `Date` class is the only predefined core JavaScript type that defines meaningful conversions to both strings and numbers.

The `<` operator and the other relational operators perform object-to-primitive conversions like == does, but without the special case for Date objects: any object is converted by trying valueOf() first and then toString().

The conversion is not exactly the same as those explained above, however: the primitive value returned by valueOf() or toString() is used directly without being forced to a number or string. 因此`1 + [222]`结果是`'1222'`，而不是 `223`.(使用valueOf结果不是primitive，因此使用toString，其结果是string类型，数字+string结果为string)

`+`, `==`, `!=` and the relational operators are the only ones that perform this special kind of string-to-primitive conversions. Other operators convert more explicitly to a specified type and do not have any special case for `Date` objects.

#### Variable Declaration
there's no `block scope` in JavaScript.

JavaScript code behaves as if all `variable declarations` in a function (but `not` any associated `assignments`) are “hoisted” to the top of the function.

The `bitwise` operators expect integer operands and behave as if those values were represented as `32-bit` integers rather than `64-bit` floating-point values.

#### Expressions and Operators
- 如果一侧不是boolean，`&&`会返回一个`truthy`或`falsy`的值。If the value on the left is `falsy`, the value of the entire expression must also be `falsy`, so `&&` simply returns the value on the left and does not even evaluate the expression on the right. So when the value on the left is truthy, the `&&` operator evaluates and returns the value on the right.
- `||`类似，但在返回上有差别。If the value of this first operand is `truthy`, it returns that truthy value. Otherwise, it evaluates its second operand, the expression on its right, and returns the value of that expression.
    - 如这样的用法，用来简化代码：`var max = max_width || preferences.max_width || 500;`
- eval:
    - The problem with `eval()` is that the code it evaluates is, in general, unanalyzable. Generally speaking, if a function calls `eval()`, the interpreter cannot optimize that function.
    - The key thing about `eval()` (when invoked like this) is that it uses the variable environment of the code that calls it.
    - It is the ability of `eval()` to change local variables that is so problematic to JavaScript optimizers.
    - When invoked by any other name, `eval()` would evaluate the string as if it were top-level global code.
    - ECMAScript 5 deprecates EvalError and standardizes the de facto behavior of `eval()`. A `“direct eval”` is a call to the `eval()` function with an expression that uses the exact, unqualified name “eval” Direct calls to `eval()` use the variable environment of the calling context. Any other call—`an indirect call`—uses the global object as its variable environment and cannot read, write, or define local variables or functions.
- delete 不仅可以删除property，还可删除array element。但有些属性不能删除

The for/in loop does not actually enumerate all properties of an object, only the enumerable properties

"use strict" is a directive introduced in ECMAScript 5. Directives are not statements. It can appear only at the start of a script or at the start of a function body, before any real statements have appeared.  It need not be the very first thing in the script or function, however

In strict mode, functions invoked as functions (rather than as methods) have a this value of undefined. (In non-strict mode, functions invoked as functions are always passed the global object as their this value.)

In addition to its name and value, each property has associated values that we’ll call property attributes:

In addition to its properties, every object has three associated object attributes:

- A native object is an object or class of objects defined by the ECMAScript specification.
- A host object is an object defined by the host environment (such as a web browser) within which the JavaScript interpreter is embedded.
- An own property is a property defined directly on an object
- Inherited property

If the assignment is allowed, however, it always creates or sets a property in the original object and never modifies the prototype chain.

js是object inheritance，不像java是class inheritance

accessor property(getter and setter) and data property. property descriptor to represent the set of four attributes

Every object has associated prototype, class, and extensible attributes

The fact that inheritance occurs when querying properties but not when setting them is a key feature of JavaScript because it allows us to selectively override inherited properties

The instanceof operator does not actually check whether r was initialized by the Range constructor. It checks whether it inherits from Range.prototype. 这意味着如果有两个不同名的constructor使用相同的prototype，则对其中一个创建的实例使用instanceof另一个会返回true

js里类是动态的，prototype的更改会直接体现在每个实例上

bookmarklet: 在书签url中添加`javascript:`开头的代码

fragment identifier为URL后面#后的内容

### Client-side javascript
Web Accessibility Initiative – Accessible Rich Internet Applications (`WAI-ARIA`) is a technical specification published by the World Wide Web Consortium (W3C) that specifies how to increase the accessibility of web pages, in particular, dynamic content, and user interface components developed with Ajax, HTML, JavaScript, and related technologies.

### 作者常用词
- idiomatic: using, containing, or denoting expressions that are natural to a native speaker.
- quirk: a peculiar behavioral habit.
- disseminate: spread or disperse (something, especially information) widely.
- handicap: a condition that markedly restricts a person's ability to function physically, mentally, or socially.
- off-limits: 禁止进入

