### hotspot
- CallbackWrapper的析构函数会设置tag的变更，因此FollowReference能够修改tag
    - 类似在函数头创建一个对象，constructor枷锁，deconstructor释放锁，这样分支代码就简洁多了
- "oop", or ordinary object pointer
- Compressed oops
    - enabled by default in Java SE 6u23 and later. In Java SE 7, use of compressed oops is the default for 64-bit JVM processes when -Xmx isn't specified and for values of -Xmx less than 32 gigabytes. For JDK 6 before the 6u23 release, use the -XX:+UseCompressedOops flag with the java command to enable the feature.
    - 倒不是为节约内存，而是节省cache和bus占用，让更多obj命中，提高效率
    - 记录obj-id，最多2^32个，转换公式：base + obj-id * sizeof(char *)
- Zero-Based Compressed Ordinary Object Pointers (oops)：
    - 如果操作系统支持从0 reserve虚存，就不需要base了
    - Solaris, Linux, and Windows 都支持
- Escape Analysis
    - Escape analysis is a technique by which the Java Hotspot Server Compiler can analyze the scope of a new object's uses and decide whether to allocate it on the Java heap.

### Serviceability Agent(sa)
$JAVA_HOME/lib/sa-jdi.jar
sun.jvm.hotspot.tools.jcore.ClassDump包含main可dump所有的类
- `-Dsun.jvm.hotspot.tools.jcore.filter`可指定filter只dump特定的类，filter需要实现ClassFilter接口
