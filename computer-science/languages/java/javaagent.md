javaAgent是从JDK1.5引入
由底层叫instrument的JVMTIAgent实现（Linux下对应的动态库是libinstrument.so
因为javaagent功能就是它来实现的，另外instrument agent还有个别名叫JPLISAgent
    (Java Programming Language Instrumentation Services Agent)
调试用到的JVMTIAgent：-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=localhost:6134

javaagent需要在META-INF/MAINIFEST.MF添加Premain-Class
-javaagent参数需要放到main所在类前面，否则不会执行
javaagent在instrument收到VMInit后开始执行，即运行在live phase
    如果instrument为attach方式，也是live phase

### premain agentmain
premain
- `premain` method throws an uncaught exception, the JVM will abort.
- 运行在`main`线程，先于`main`函数
agentmain
- `agentmain` method throws an uncaught exception it will be ignored.
- 运行在`Attach Listener`线程内，因此不会卡住整个jvm

### Agent start-up
OnLoad phase calls OnLoad
    Agent_OnLoad,Agent_OnUnload
Live phase calls OnAttach

### javaagent and native agent
Java agents
- premain
- 通过Instrumentation object能做的操作：
- rewrite methods
- reload new class without restarting JVM
- 使用ASM：bytecode->DOM-like structure->modify->save to be bytecode
- 更靠后的agent节点，受限于JVM
- 获取GC信息需要辅助agent
Native agents
- GC, locking, code manipulation, synchronization, thread management, compilation debugging，etc.
- Issues related to: Complex,Portability,Stability
- 不受full gc暂停限制，可继续发送数据
- dynatrace使用该方法
    - Full Insight of all Classes
    - More detailed information
    - Additional information: a crash caused by an Out-of-Memory Error情况下继续运行
    - Less impact on JVM: java agent会占用更多heap
    - Performance: 一些数据的获取需要Java to Native的过程
    - Not attached to JVM: full gc的暂停

References
- http://blog.takipi.com/double-agent-java-vs-native-agents/
- http://apmblog.dynatrace.com/2014/01/15/pros-and-cons-of-using-java-vs-native-agent-for-application-performance-management/
- http://jonbell.net/2015/10/new-blog-series-java-bytecode-and-jvmti-examples/
- https://bugs.openjdk.java.net/browse/JDK-8136586
- http://www.students.ic.unicamp.br/~jugic/PUB/jdk1.5.0/demo/jvmti/
- http://jonbell.net/2015/10/new-blog-series-java-bytecode-and-jvmti-examples/
- https://bugs.openjdk.java.net/browse/JDK-8078653
