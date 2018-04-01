### Class File Format
class文件中存储的access权限只有`public`和`default（package-private）`两种，在源码中外部类也只有这两种，内部类可以有`protected`和`private`等，但这部分内容不存储在class文件的access中
- `default` is for package level access and `protected` is for package level plus non-package classes but which extends this class (Point to be noted here is you can extend the class only if it is visible!).
    - protected top-level class would be visible to classes in its package.
    - now making it visible outside the package (subclasses) is bit confusing and tricky. Which classes should be allowed to inherit our protected class?
    - If all the classes are allowed to subclass then it will be similar to public access specifier.
    - If none then it is similar to default.
- Since there is no way to restrict this class being subclassed by only few classes (we cannot restrict class being inherited by only few classes out of all the available classes in a package/outside of a package), there is no use of protected access specifiers for top level classes. Hence it is not allowed.

attributes
- `ConstantValue`属性指针对`static field`，`instance field`的`final`标识的都被合并到了`<init>`中

