## java
The wildcard `?` in Java is a special type parameter that controls the type safety of the use of generic (parameterized) types. This is a form of use-site `variance` annotation.

### annotation processing
JSR 269: Pluggable Annotation Processing API 从Java SE 6 开始支持

The `javac` command provides direct support for `annotation processing`, superseding the need for the separate annotation processing command, `apt`.

Processors are located by means of service provider-configuration files named `META-INF/services/javax.annotation.processing.Processor` on the search path. Alternatively, processors can be specified explicitly, using the `-processor` option

