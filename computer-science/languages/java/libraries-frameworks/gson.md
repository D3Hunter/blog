## gson
gson支持序列化任意对象，但对于有继承结构的类，在反序列化时会失败，因为在序列化阶段类型信息没有序列化，支持方法如下：
- 使用gson提供的gson-extras包中的`RuntimeTypeAdapterFactory`
- gson-extras在官方仓库中没有，但`RuntimeTypeAdapterFactory`可以单独使用，可从github上拷贝出来
- 注意初始化`RuntimeTypeAdapterFactory`的基类需要是interface或者abstract class，或者所有被序列化的实例都是子类对象，否则序列化基类对象时会报错

