问题解决的方法／思路
要解决问题不仅要有正确的方法及其应用方法的能力，还需要
- 对问题本身的认识、抽象的程度
- 对问题涉及的知识有充分的的了解（或对资源的拥有和把握）
- 之后才能够狠顺畅的解决问题

不需要拆分的问题多是些需要攻克的细节问题
- 是否能简化或避免该问题？
    - 这类问题可能来源于上层问题不恰当的拆分导致，可考虑从上简化或避免该问题
- 问题域或抽象后的问题域常见解决方法

### 抽象
很多问题用业务语言描述，会慢慢模糊了问题的本质，需要抽象出来、站在更高处来看问题。
抽象看问题带来的另一个好处是能更容易的找到相似的问题，参考相似问题就更容易处理当前问题。
比如调用拓扑图，实际上是一个graph，graph就涉及node和edge的问题；
如通知问题，相当于广播，观察者模式，那么相似的问题是什么呢？什么会用到这种机制呢？群聊天系统。

### 分治：
划分方法：
- 功能
- 重要程度
- 已有、欠缺：哪些是欠缺知识的，抽象来说那些是欠缺资源的；那些是现有资源可以解决的
- 对于又一个数据集的
    - 二分
    - 按格式／功能部分分
    - 逐步递增，即之分出来一个小问题，由这个小问题递增解决大问题（动态规划）

### other
特殊情况在循环外处理，要比在循环内判断然后处理要方便的多，比如pascal三角每行的起始和结尾元素

有时候以图示形式画出来，更有助于思考，甚至能直观显示出解决方法
