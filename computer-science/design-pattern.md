### registry pattern
also called as the Name Service pattern. An object needs to contact other objects for which it knows only the object's name or the service it proovides but not how to contact the object.

### decorator pattern
The decoration pattern is an alternative to subclassing. Subclassing adds behavior at compile time, and the change affects all instances of the orginal class. decorating can provide new behavior at run-time for selected objects.
decorator与delegate同属相同接口，提供额外功能，如`添加try-catch`、`log`，一种模块化cross-cutting-concern的方式

### visitor
Moving operations into visitor classes is beneficial when
- many unrelated operations on an object structure are required,
- the classes that make up the object structure are known and not expected to change,
- new operations need to be added frequently,
- an algorithm involves several classes of the object structure, but it is desired to manage it in one single location,
- an algorithm needs to work across several independent class hierarchies.

