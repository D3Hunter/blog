### java 技术体系组成
- java语言
- java虚拟机
- class文件格式
- java api类库
- 三方java类库

### java内存区域
#### 运行时数据
- Program Counter
- Java Virtual Machine Stack:运行java代码用，每个一个stack frame
- Native method stack:运行native方法，实现上可能跟前者使用同一个栈
- Java Heap
- Method Area: HotSpot上使用PermGen／MetaSpace实现
    - Runtime Constant Pool：前者的一部分，1.6及前面的版本的HotSpot会把String.intern()放到该区
- Direct Memory

#### HotSpot对象探秘
`Bump the pointer`（指针碰撞）通过指针向前移动对象大小的方式申请内存。使用mark-（compact／copy）的gc算法可用该方法，如Serial、ParNew
`Free List`：通过空闲列表寻找合适的申请位置。使用mark-sweep的gc算法可用该方法，如CMS。
TLAB：多线程bump指针

对象内存布局
- header：一部分为对象运行时数据，一部分为类型指针
- Instance Data
- padding：HotSpot下对象地址对齐到8

对象访问方式（reference实现方式）
- handle：对象被移动时只需要改变句柄池中的地址，多一次解引用
- 直接指针：访问快，但gc带来的对象移动需要同时修改该地址

java执行栈超过栈深度上限，报StackOverflowError，内存不够报OutOfMemoryError。两者有重叠的情况。

### GC
- reference counting
- Reachability Analysis

对象在finalize函数内可以把自己救活，但只有一次机会，因为finalize只被执行一次

gc方法
- copy：hotspot eden／survivor部分采用的算法
- mark-compact：用在tenured space，
- mark-sweep：用在tenured space，如CMS

safe-point: 暂停线程的方式：
- preemptive suspension
- voluntary suspension
safe-region:针对已经进入wait状态（sleep或blocked）的线程

Hotspot中的gc算法
- Serial
- ParNew，Serial的多线程版本，除和SerialOld外只能和CMS配合
- Parallel Scavenge：与CMS关注响应时间不同，该算法关注throughput
    - 可使用`-XX:+UseAdaptiveSizePolicy`，开启后JVM会自动调整如新生代大小等参数，该调节方式称为GC自适应调节车略`GC Ergonomics`
    - 该算法跟G1都没有使用传统的GC代码框架，而是单独实现
- SerialOld：
- Parallel Old：Parallel Scavenge的老年代版本
- CMS：关注响应时间，分为下面几个阶段
    - initial Mark：需要STW，仅标记gc roots能`直接`关联到的对象，速度很快
    - concurrent Mark
    - remark：需要STW，修正concurrent Mark期间变动的标记，比initial Mark慢，远比concurrent Mark快
    - concurrent Sweep
    ------
    - 无法处理floating garbage（标记后生成的垃圾）
    - 内存碎片，可通过一些参数调节
- G1：面向服务端应用的算法
    - 并行和并发
    - 分代收集
    - 空间整合
    - 可预测的停顿
    ------
    - heap划分成多个大小相等的region
    - 和其他gc算法类似，使用Remembered Set避免全堆扫描
    ------
    - Initial Marking
    - Concurrent Marking
    - Final marking
    - Live Data Counting and Evacuation

内存分配策略
- 对象优先在Eden中分配
- 大对象直接进入老年代
- 长期存活的对象进入老年代
- 动态对象年龄判定
- 空间分配担保

### class文件格式
big-endian存储
两种数据类型：无符号数和表
表由多个无符号数和其他表作为数据项构成的复合数据结构，名称一般以_info结尾。
- 这其实是对数据存储格式的一种抽象，如http协议可以描述为由http头和无格式数据构成的表
magic为0xCAFEBABE(咖啡宝贝)
constant_pool_count比实际数量大1，计数从1开始，0是为了表达长常量索引并不指向任何常量做特殊使用
常量池主要包含literal和symbolic reference
`ACC_SUPER`：是否允许使用`invokespecial`字节码指令的新语义，该指令在JDK1.0.2发生过改变，为了区分，之后的版本编译出来的类都会有该标志
Code属性在方法表的属性集合中（interface和abstract方法没有）
因为指令使用一个字节表示，指令集被估计设计成非正交的，即并非每种数据类型和每种操作都有对应的指令，必要时需要做类型转换来支持。

### 类加载
- 加载
- 链接
    - 验证
    - 准备
    - 解析（有时可以再初始化后开始解析）
- 初始化
- 使用
- 卸载

必须立即初始化类的情况（以下方式称为对类的主动引用）
1. 遇到new/getstatic/putstatic/invokedynamic指令
2. 使用java.lang.reflect包对类反射调用时
3. 初始化类时，如果父类还么初始化，需要先初始化父类
4. 虚拟机启动时，包含`main()`的主类需要先初始化
5. 1.7动态语言支持，如果java.lang.invoke.MethodHandle实例最后解析的REF_getstatic/REF_putstatic/REF_invokeStatic等句柄所在类未初始化时

被动引用（跟JDK有关，有些在1.7某些版本下成立，在1.7其他版本或1.8下就不成立）
- 通过子类引用父类定义的static成员，HotSpot下只会出发父类加载，不会触发子类
- 创建某类的一个数组，会触发一个数组类加载，不会触发引用类

加载
- 通过类的fully qualified name获取其binary stream
    - zip包，如jar、war
    - 网络读取
    - 运行时生成，动态代理等
    - 从其他文件生成，如jsp
    - 从数据库中读取，可能较少见
- binary stream转换成PermGen中的数据结构
- 创建对于的Class对象代表该类
- Parents Delegation Model
- 如果基础类需要调用用户类，如JNDI需要调用SPI代码（这些代码在用户的ClassPath下，基础类所在的Bootstrap加载器找不到），Java团队使用的一个不太优雅的设计，及线程上下文加载器，JNDI使用该加载器去加载SPI实现类，也就是父加载器调用子加载器来加载。java中涉及SPI的加载都是采取这种方式：JNDI、JDBC、JCE、JAXB和JBI等。
    - Thread Context Classloader如果创建线程时未指定，则等于父线程的，如果全局未设置，则等于AppClassloader
- HotSwap和Hot Deployment，java模块化如`OSGi`和`Jigsaw`

验证：确保Class文件格式符合当前虚拟机要求
解析：将常量池中的符号引用替换为直接引用的过程
初始化：
- clinit由源码中的类初始化相关的语句按顺序收集而成，代码只能访问定义在该语句前的变量，定义在之后的变量可以赋值，不能访问
- 由于上面的主动引用，虚拟机会先执行父类的clinit
