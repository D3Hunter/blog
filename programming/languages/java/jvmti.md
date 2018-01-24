ClassFileLoadHook
The JVM TI interface pointer is called the environment pointer. An environment pointer is a pointer to an environment and has the type jvmtiEnv*. An environment has information about its JVM TI connection. The first value in the environment is a pointer to the function table. The function table is an array of pointers to JVM TI functions. Every function pointer is at a predefined offset inside the array.
JVM TI functions always return an error code via the jvmtiError function return value
References passed to JVM TI functions can be either global or local, but they must be strong references.
All references returned by JVM TI functions are local references--these local references are created during the JVM TI call. Local references are a resource that must be managed
A thread is ensured the ability to create sixteen local references without the need for any explicit management.（PushLocalFrame and PopLocalFrame.）
"Required Functionality" means it is available for use and no capabilities must be added to use it. "Optional Functionality" means the agent must possess the capability before it can be used.
another environment possesses capabilities that can only be possessed by one environment, or the current phase is live, and certain capabilities can only be added during the OnLoad phase.

gdb直接运行JVM会出现SIGSGEV，这是由于java代码中的NullPointerException,可参考下面的bug链接

All libraries loaded into java are assumed to be MT-safe (Multi-thread safe)

VMSTART中调用JNI的FindClass崩溃问题，参考JDK-8078653,VMStart阶段调用没问题

GetSystemProperty/ies只能在Onload和live phase阶段用
Exception/Catch只能在live用

It is the responsibility of the agent to be careful in the callbacks especially in the VMStart event when the VM has not finished the initialization yet.

IterateOverReachableObjects，遍历所有对象，不会改变object状态，可能会导致java程序暂停
FollowReferences获得object关系树

### jvmti
heap遍历reference需要先添加tag，否则无法获取谁是谁
jvmtiHeapReferenceCallback
- 如果referrer object是一个runtime class，那么其referrer_class_tag为java.lang.Class的tag
- 上面的规则类似回调也适用
- 如果某个object的field为null这时不会生成reference

### JVMTI
JVM TI interface pointer is called the environment pointer可以有多个，有各自的设置
Agent_OnLoad
    options仅在该函数域内可用
    非0返回会导致VM退出
VM execute phase
- OnLoad
- primordial
- start
- Live(VMInit后）
- dead
jvmti agent会被作为JNI native搜索对象，在其他的之后，可用NativeMethodBind event捕获
