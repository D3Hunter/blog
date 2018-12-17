### registry pattern
also called as the Name Service pattern. An object needs to contact other objects for which it knows only the object's name or the service it proovides but not how to contact the object.

### decorator pattern
The decoration pattern is an alternative to subclassing. Subclassing adds behavior at compile time, and the change affects all instances of the orginal class. decorating can provide new behavior at run-time for selected objects.
decorator与delegate同属相同接口，提供额外功能，如`添加try-catch`、`log`，一种模块化cross-cutting-concern的方式

### Visitor Pattern
In object-oriented programming and software engineering, the `visitor design pattern` is a way of separating an algorithm from an object structure on which it operates. A practical result of this separation is the ability to add new operations to existent object structures without modifying the structures. It is one way to follow the `open/closed principle`.

The `visitor pattern` requires a programming language that supports `single dispatch`, as common object-oriented languages...Thus, the implementation of the `visit` method is chosen based on both the dynamic type of the element and the dynamic type of the visitor. This effectively implements `double dispatch`.

In software engineering, `double dispatch` is a special form of `multiple dispatch`, and a mechanism that dispatches a function call to different concrete functions depending on the runtime types of two objects involved in the call.

#### visitor
Moving operations into visitor classes is beneficial when
- many unrelated operations on an object structure are required,
- the classes that make up the object structure are known and not expected to change,
- new operations need to be added frequently,
- an algorithm involves several classes of the object structure, but it is desired to manage it in one single location,
- an algorithm needs to work across several independent class hierarchies.

