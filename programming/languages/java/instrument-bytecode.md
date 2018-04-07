### dup相关指令
上面是栈顶

    +--------+----------+----------+---------+-----------+----------+
    |  DUP   |  DUP_X1  |  DUP_X2  |  DUP2   |  DUP2_X1  |  DUP2_X2 |
    +--------+----------+----------+---------+-----------+----------+
    | |A A|  |  |A A|   |  |A  A|  |  |A A|  |   |A A|   |   |A A|  |
    |    A   |  |B B|   |  |B  B|  |  |B B|  |   |B B|   |   |B B|  |
    |        |     A    |  |C  C|  |     A   |   |C C|   |   |C C|  |
    |        |          |      A   |     B   |      A    |   |D D|  |
    |        |          |          |         |      B    |      A   |
    |        |          |          |         |           |      B   |
    +--------+----------+----------+---------+-----------+----------+

### ASM BCI
仅仅在 AdviceAdaptor 的 methodExit 添加代码还不够，因为 RuntimeException 并不会显示抛出
    因此需要添加方法整体的 try-catch，并在在 visitMaxs 添加 methodExit 处理
MethodNode的accept会复现一遍该node
为类添加getter，如果field为父类的private会报错，需要调整其access

#### Instrumentation
三种方式
- Static Instrumentation，不同的classpath
- Load-Time Instrumentation，javaagent/nativeagent
- Dynamic Instrumentation，RetransformClasses->ClassFileLoadHook

native methods can be instrumented since 1.6: `setNativeMethodPrefix`
jdk1.5支持redefine，1.6开始支持retransform
redefineClasses: 需要传入被redefine的Class及新的字节码
- 1.5可以使用redefine重新修改字节码，但局限于能从磁盘拿到字节码的类
- 所有注册的transformer都会执行一边，不像retransform能在注册时配置
retransformClasses：
- starting from the `initial class file bytes`
    - The `initial class file bytes` represent the bytes passed to `ClassLoader.defineClass` or `redefineClasses` (before any transformations were applied),
    - however they might not exactly match them.
    - 验证了下每次的`file bytes`都是不同的对象，内容基本一样（参考javadoc，部分顺序可能存在差别），数据来源可能是提前存储下来的（但这样太耗内存了），或者磁盘读取（对网络读取的字节码无效）。从Class对象反向生成bytecode得到的是transform之后的内容。
- for each transformer that was added with `canRetransform` false, skip it.
- for each transformer that was added with `canRetransform` true, the `transform` method is called in these transformers
- the transformed class file bytes are installed as the new definition of the class

#### ClassFileTransformer
`transform`会使jvm卡住，是不是STW得查下
