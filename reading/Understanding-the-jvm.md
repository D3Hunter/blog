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
