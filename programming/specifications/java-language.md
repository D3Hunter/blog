nested class: class defined within another class.
- 分为两类:`static nested classes`. Non-static nested classes are called `inner classes`.
    - There are two special kinds of `inner classes`: `local classes` and `anonymous classes`.
    - Local classes are classes that are defined in a block, which is a group of zero or more statements between balanced braces. 即在某个方法内
    - anonymous classes are like local classes except that they do not have a name.
- A nested class is a member of its enclosing class

The types that comprise a package are known as the `package members`.
At first, packages appear to be hierarchical, but they are not. 这意味着`package member不是递归包含的`，这对nested class也是适用的，`nested class的package跟其outer class并不一样`
