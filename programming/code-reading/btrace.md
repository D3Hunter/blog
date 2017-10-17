`BTraceRuntime`使用一个ThreadLocal的`BTWrapper`存储
`Command`系统使用`ObjectOutput`做序列化
相关的依赖包都做过shade处理，加载时都扔到bootstrap路径中，保证埋点能够引用到
### Command
InstrumentCommand 包含代码和参数
### Client
FileClient 本地脚本
RemoteClient

`BTraceProbe` 继承自`ClassNode`, 表示一个要注入的脚本
`OnMethod`支持以下类匹配
- `+` subclass of
- `@` annotation
- `/.*/` regular expression
