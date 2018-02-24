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

### 代码执行
方法调用在class文件里面都是一个常量池的符号引用，实际执行时需要变成直接引用（解析阶段处理，Resolution），但有些需要动态解析。
- invokestatic
- invokespecial：和前面一种，这两种在类加载阶段就能转换成直接引用。init、private方法、父类方法和final表示的方法
- invokevirtual：根据操作数栈顶确定对象实际类型，再去找对应方法
- invokeinterface
- invokedynamic，前四种分派逻辑在虚拟机，这种的分派逻辑由用户指定

重载方法在编译阶段就确定了，是静态的

### 早期优化
javac基本不做代码优化，Hotspot优化主要集中在JIT
javac使用java编写

C#中的范型通过类型膨胀（真实范型）实现，java使用类型擦除（伪泛型）实现，`List<int>`和`List<String>`是不同的类型，而java中是同一个类型

### 晚期优化
HotSpot同时有解释器和编译器（不是指javac，而是将bytecode编译为本地代码的部分，如JIT），两者各有优势，解释器可以立即开始执行，启动快；随着时间推移，编译器能带来更高的执行效率。解释器的存在，允许编译器进行在大多数时候都能提高效率的激进优化，并在假设不成立时回退到解释执行

Tiered Compilation
- 解释执行
- C1（Client Compiler），简单可靠的优化，必要时加入性能监控逻辑
- C2（Server Compiler），会启用编译好时较长的优化，甚至会根据性能监控信息做一些不可靠的激进优化

被JIT编译的HotSpot code有两类：
- 多次调用的方法：整个方法作为编译对象
- 多次执行的循环体（方法调用次数少，但内部存在多次执行的循环体）：也是整个方法作为编译对象，但是当前方法可能正在执行，会使用OSR（栈上替换）来直接替换

热点探测方法：
- Sample based hot spot detection:定期查看各线程栈顶方法。简单高效，但不准确
- Counter based hot spot detection：为每个方法维护一个计数器
    - Counter Decay／Counter Half Life Time，在GC时完成
    - HotSpot有调用计数器和回边计数器（用来统记循环体执行次数

查看JIT结果(有些参数需要Debug或fastDebug编译的jdk)
- `-XX:+PrintCompilation`
- `-XX:+PrintInlining`
- `-XX:+PrintAssembly`,需要HSDIS插件支持
- `-XX:+PrintOptoAssembly`

优化技术
- 公共子表达式消除，语言无关
- 数组范围检查消除，语言相关
- 方法內联
    - 除了消除了对应的方法调用，还使其他优化手段成为可能，比如有些代码在内联后看实际上是Dead Code
- 逃逸分析，目前并不成熟，因为不能保证进行逃逸分析的性能收益必定高于它的消耗
    - 栈上分配
    - 同步消除，不会被其他线程访问的数据，不需要做同步
    - 标量替换，非逃逸对象，可以把对象展开成一系列标量

### java内存模型
cache coherence
cpu／compiler instruction reordering
java虚拟机规范通过JMM来屏蔽各硬件和操作系统的内存访问差异，以使java达到在各平台上都能有一致的效果
java内存模型的主要模型是定义程序中各个变量的访问规则，即在虚拟机中将变量存储到内存和从内存中取出变量这样的底层细节。

volatile变量对所有线程立即可见，对其write操作都能立即反映在其他线程中，即volatile在各个线程是一致的，但java中运算操作不是原子的（其他语言也一样），导致volatile变量运算也是非原子的

java中volatile
- 用于Concurrent Programming
- Adds visibility to the variable
- 单独的read和write是atomic的，这也意味这assign操作（write）也是atomic的
    - 由于assign操作的atomic属性，以及happens-before属性可以实现：让一个线程检查某个被其他线程修改的变量的值来实现线程间同步
- 如果write操作依赖与当前操作，则不是atomic的，比如arithmetic操作会有一个read-update-write的过程
- 拥有happens-before效果，volatile write前面的其他write，会对happends-before的read都可见
    - `double-locking singleton需要该特性避免成员write被reorder到singleton write之后，保证其他线程看到的是完全初始化后的对象`

c/c++中的volatile
- 用于特定内存访问，比如内存映射I/O
- Disables optimizations on the variable
- 虽然很多时候单独的read/write是atomic，但并不总是成立
    - 就算是atomic，由于没有happens-before属性，仍然不能做线程间同步用，编译器及cpu的reordering会导致逻辑错误
    - atomic依赖于具体的代码的编写、编译器、CPU和BUS位数
    - 在x86和IA32，正确对齐的数据的read和write是atomic的
    - 正确对齐的16bit数据，在8086是atomic，8088不是，因为8086有16bit总线，而8088只有8bit
    - 如果两个变量在同一个对齐的区域內，比如两个short在同一个4字节对齐区域，如果write操作只支持以4字节为单位，也会导致非atomic
- 如果write操作依赖与当前操作，跟前者一样也不是atomic的
- 在线看代码的汇编：https://gcc.godbolt.org/
