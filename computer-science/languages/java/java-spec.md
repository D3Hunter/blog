## java
The wildcard `?` in Java is a special type parameter that controls the type safety of the use of generic (parameterized) types. This is a form of use-site `variance` annotation.

### annotation processing
JSR 269: Pluggable Annotation Processing API 从Java SE 6 开始支持

The `javac` command provides direct support for `annotation processing`, superseding the need for the separate annotation processing command, `apt`.

Processors are located by means of service provider-configuration files named `META-INF/services/javax.annotation.processing.Processor` on the search path. Alternatively, processors can be specified explicitly, using the `-processor` option

## concepts
- `subsignature`: 1. same signature, 2. the signature of m1 is the same as the erasure of the signature of m2.
- `override-equivalent` iff either m1 is a subsignature of m2 or m2 is a subsignature of m1. 这样的两个overload函数编译会报错
- `return-type-substitutable`: 都是void、都是相同的primitive type，子类型，R1 = |R2|
- `functional method`(of `functional interface`) is `m`:
    - `m` is a `subsignature` of every method's signature in `M`(the set of `abstract` methods that are members of I that do not have the same signature as any public instance method of the class `Object`.).
    - `m` is `return-type-substitutable` for every method in `M`.

