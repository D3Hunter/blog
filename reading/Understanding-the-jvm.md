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
