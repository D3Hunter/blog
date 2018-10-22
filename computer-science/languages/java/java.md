class必须放到对应包名的目录下才能由java找到
-Dname=value会将其放到System.properity中

java <class-name>中class-name格式为点分或/分，不包含最后的.class

启动过多线程，会导致很多的cpu花在context switch上

`JSR 223` Scripting for the JavaTM Platform, since `1.6`

### JDK classes
ResourceBundle 国际化
wait notify notifyAll需要获得object的monitor

Pattern && Matcher
- Matcher.find()可以用来查找所有满足条件的子串，`group(0)`是匹配的整个串，内部的group从`1`开始
- `Greedy quantifiers` first matches as much as possible.，如`.*`
- `Reluctant quantifiers` first matches as little as possible. 如`.*?`
- `possessive quantifier` is just like the greedy quantifier, but it doesn't backtrack. So it starts out with .* matching the entire string, leaving nothing unmatched. 如`.*+`

ObjectOutputStream/ObjectInputStream:
- writeObject/readObject会记录已经写／读的对象，以避免多次读取，可能会导致OOM
- writeUnshared／readUnshared不会记录对象，但是仍然往内部数组放null，也可能导致OOM
    - 查看以下调用代码`writeObject0 -> writeClass -> handles.assign -> insert`
- 解决以上问题的方法：
    - 重新创建stream对象
    - 调用`reset()`，该方法会清除掉内部记录的信息

### classloader
- Bootstrap classes(Bootstrap class loader) - Classes that comprise the Java platform,
    - including the classes in rt.jar and several other important jar files.
- Extension classes(Extensions class loader) - Classes that use the Java Extension mechanism.
    - These are bundled as .jar files located in the extensions directory.
- User classes(System class loader/App class loader) - Classes defined by developers and third
    parties that do not take advantage of the extension mechanism. You identify the location
    of these classes using the  -classpath option on the command line (the preferred method)
    or by using the CLASSPATH environment variable. (See Setting the Classpath for Windows or
    Unix.)

除了Java默认提供的三个ClassLoader之外，用户还可以根据需要定义自已的ClassLoader，而这些自定义的ClassLoader都必须继承自java.lang.ClassLoader类，也包括Java提供的另外二个ClassLoader（Extension ClassLoader和App ClassLoader）在内，但是Bootstrap ClassLoader不继承自ClassLoader，因为它不是一个普通的Java类，底层由C++编写，已嵌入到了JVM内核当中，当JVM启动后，Bootstrap ClassLoader也随着启动，负责加载完核心类库后，并构造Extension ClassLoader和App ClassLoader类加载器。

Bootstrap Class path and system class path

Ld: defining loader
Li: initializing loader
每个类D使用的相关类C都是以D的Ld作为C的Li来查找的，如果找不到就会报NoClassDefError.

### Plumbr
内存检测工具，JVMTI写的
https://www.javacodegeeks.com/2014/03/migrating-from-javaagent-to-jvmti-our-experience.html

### java tools & 常用命令
- jstack可以看各个线程当前的stack-trace
- javap -l可以显示debug符号表，查看是否有变量表，但没变量表也能调试
- jhat - Java Heap Analysis Tool
- javap - Java class file disassembler(p in javap means printer)
- jconsole - J2SE Monitoring and Management Console
- jinfo - configuration info
- jstack - 基本上等于kill -3, 可以dump远程进程
- jmap - prints shared object memory maps or heap memory details
- jsadebugd - serviceability agent debug daemon
- jstat - Java Virtual Machine statistics monitoring tool
    - `-gc` 可以查看所有区块内存的使用情况
    - `-gccapacity` 查看使用量和最大最小配置
- jvisualvm - profile and monitor tool
- jcmd
- java -XX:+PrintFlagsFinal -version
- jar cvf program.jar -C path/to/classes .
- JMH - Java Microbenchmark Harness 用来做基准测试
- 控制heap的shrink和expand
    - +XX:MinHeapFreeRatio
    - +XX:MaxHeapFreeRatio

逆向和代码混淆相关
- jarjar用来重命名类
- jd
- bytecodeviewer
- ZKM(Zelix KlassMaster): java obfuscator
### Logging Frameworks
actual: Log4J, JUL, LogBack(kind of Log4J2.0)
facade: JCL(Spring uses it), SLF4J(Hibernate have changed to)

### Java's ForkJoin Framework(JSR-166)
ForkJoinPool: An instance of this class is used to run all your fork-join tasks
RecursiveTask<V>: You run a subclass of this in a pool and have it return a result
RecursiveAction: just like RecursiveTask except it does not return a result
ForkJoinTask<V>: superclass of RecursiveTask<V> and RecursiveAction.

### FreeMarker
    a template engine: a Java library to generate text output (HTML web pages, e-mails,
    configuration files, source code, etc.) based on templates and changing data.

### Application Server(Java EE Container) VS Servlet Container(Web Container)
A servlet-container supports only the servlet API (including JSP, JSTL).

An application server supports the whole JavaEE - EJB, JMS, CDI, JTA, the servlet API (including JSP, JSTL), etc.

It is possible to run most of the JavaEE technologies on a servlet-container, but you have to install a standalone implementation of the particular technology.

### inversion of control (IoC)
a design principle in which custom-written portions of a computer program receive the flow of control from a generic framework as compared to traditional procedural programming

### concepts
Java Management Extensions (JMX)
Java Message Service（JMS）
JAXB:通过xml标记直接得到某个xml结构的bean
JAX-WS(Java API for XML Web Services): an API for creating web services, particularly SOAP services.

### ServiceLoader
service为对应接口或抽象类
service provider为service的具体实现
在META-INF/services中添加名称为service全名的配置文件，里面包含具体的provider
    可通过该类的load来加载对应service
service需要有无参constructor

### 问题解决
`java世界里编译出的是字节码，有很多技术是会修改字节码的`，比如代码混淆，有时候代码混淆会把字符串一并更改掉，如果这时候出了一个很奇怪的问题，可以看一下字节码：比如`String.startsWith`函数总是得不到正确的结果，而该函数肯定没有问题，可以看一下字节码是不是有部分内容被改掉了

javaagent的premain是可以下断点的，使用jpda，设置suspend=y，并且需要将jpda参数放到javaagent的前面，这样就可以在premain下断点了

高编译低运行只能保证字节码兼容，不保证类库兼容
- 比如：ConcurrentHashMap.keySet()如果再1.8编译会返回KeySetView，该类在1.7上没有
- 因此最好的保持binary兼容的方法仍然是，想支持什么最低版本，就在什么版本上编译

压缩效率/压缩大小
    压缩算法，算法参数
    针对数据量本身的处理，如id--string的转换，使用map存储所有字符串

影响问题复现的原因
    时间
    启动时序
    机器/os
执行jar包时，只能通过manifest指定cp，命令行不起作用

### proxy pattern:
Allows for object level access control by acting as a pass through entity
or a placeholder object.

An access proxy is used to enforce a security policy on access to a service or data-providing object.
A facade is a single interface to multiple underlying objects.
The remote proxy is used to mask or shield the client object from the fact that the underlying object is remote.
A virtual proxy is used to perform lazy or just-in-time instantiation of the real object.

Java proxies are runtime implementations of interfaces. On other cases use CGLib

### GC信息获取：hotspot基本上都是stop-the-world
- GarbageCollectorMXBean获取的汇总信息
- -XX:+PrintGCDetails等debug参数，输出到控制台
- Java7u4后的通知机制
- JVMTI
- GarbageCollectionFinish只在full gc才会通知

### OOM的description
Java heap space
unable to create new native thread
GC overhead limit exceeded
PermGen space（java8里叫MetaData）
Requested array size exceeds VM limit

### java逆向
对于混淆代码，可以先把field等改成长名字，避免跟方法/类混淆，减少理解难度
### class name
- `binary name` use '.'
- `internal form of binary name` use '/'
- `fully qualified class name(FQCN)` also known as `binary names`
- FQCN的定义参考Java Language Specification 6.7
- Canonical Names基本等同于FQCN, 只是有时member class在parent和child中可以用不通的FQCN表示，而其Canonical Names只能使用其定义类表示
- Class.getName返回的是一种特殊的格式，里面有`Lclassname;`的用法，这种用法还用于`Descriptors and Signatures`
- `Descriptors and Signatures`参考Java Virtual Machine Specification 4.3

### 打开JMX
-Dcom.sun.management.jmxremote.port=8999 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Djava.rmi.server.hostname=10.128.6.238

### java 序列化
transient 的对象不会被序列化
对敏感字段加密
情境：服务器端给客户端发送序列化对象数据，对象中有一些数据是敏感的，比如密码字符串等，希望对该密码字段在序列化时，进行加密，而客户端如果拥有解密的密钥，只有在客户端进行反序列化时，才可以对密码进行读取，这样可以一定程度保证序列化对象的数据安全。
解决：在序列化过程中，虚拟机会试图调用对象类里的 writeObject 和 readObject 方法，进行用户自定义的序列化和反序列化，如果没有这样的方法，则默认调用是 ObjectOutputStream 的 defaultWriteObject 方法以及 ObjectInputStream 的 defaultReadObject 方法。用户自定义的 writeObject 和 readObject 方法可以允许用户控制序列化的过程，比如可以在序列化的过程中动态改变序列化的数值。基于这个原理，可以在实际应用中得到使用，用于敏感字段的加密工作，清单 3 展示了这个过程。

### java线程创建上限
java.lang.OutOfMemoryError: unable to create new native thread
以下结果在64b机器上测试，hotspot 1.7.0_79-b15
- 如果以root运行，jvm会自动调整ulimit，此时通过ulimit限制线程数/内存占用无效
- jvm本身会创建10几个（本机数量）native thread，因此可用数量要减去该部分
- virtual memory/physical memory/max user processes/stack size(本机1M)都会影响实际可创建的线程数量
- -Xms或者当前正在使用的heap大小也会影响，因为heap内存需要pin(lock)到内存中
- 以下内核参数也会影响实际可创建线程数
    - `sys.kernel.threads-max` 全局单进程最大线程数，对应路径/proc/sys/kernel/threads-max。/etc/sysctl.conf做永久修改
    - `sys.kernel.pid_max` tid最大编号
    - `sys.vm.max_map_count` 至少为2倍thread-count，否则会报Attempt to protect stack guard pages failed
### HotSpot GC collectors
HotSpot JVM may use one of 6 combinations of garbage collection algorithms listed below.
`UseParallelOldGC`会自动设置`UseParallelGC`
The throughput collector(UseParallelGC) can use multiple threads to process the old generation as well. That is the default behavior in JDK 7u4 and later releases, and that behavior can be enabled in earlier JDK 7 JVMs by specifying the `-XX:+UseParallelOldGC` flag. 即此时单独设置`UseParallelGC`同时也设置了`UseParallelOldGC`
```
+------------------------------+---------------------------------------+----------------------------------------+
|Young collector               |Old collector                          |JVM option                              |
+------------------------------+---------------------------------------+----------------------------------------+
|Serial (DefNew)               |Serial Mark-Sweep-Compact              |-XX:+UseSerialGC                        |
|Parallel scavenge (PSYoungGen)|Serial Mark-Sweep-Compact (PSOldGen)   |-XX:+UseParallelGC                      |
|Parallel scavenge (PSYoungGen)|Parallel Mark-Sweep-Compact (ParOldGen)|-XX:+UseParallelOldGC                   |
|Serial (DefNew)               |Concurrent Mark Sweep                  |-XX:+UseConcMarkSweepGC -XX:-UseParNewGC|
|Parallel (ParNew)             |Concurrent Mark Sweep                  |-XX:+UseConcMarkSweepGC -XX:+UseParNewGC|
|G1                            |                                       |-XX:+UseG1GC                            |
+------------------------------+---------------------------------------+----------------------------------------+
```

### 字节码保护
- 字节码混淆
- classloader层做字节码加密，但这样无论在java或者jvmti层做都会暴露加密规则
- 服务端动态下发加密代码和密钥，避免暴露代码
- 上述方法的缺点在于，jvm层仍能看到解密后的内容，通过tools.jar也能将运行时的类dump出来
- 动态编译依赖加密后的代码可以将依赖接口化

### java source code parser
- eclipse jdt ASTParser
- JavaParser
