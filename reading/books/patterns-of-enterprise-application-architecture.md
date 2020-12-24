## Patterns of Enterprise Application Architecture
翻译的不大好，技术名词很费解，句子很生硬

这本书很老了，2002年写的

该书总共18章，从第8章开始主要介绍各种模式

中文版的翻译为`企业级应用`，字面看起来好像是比`普通应用`高一个level的东西，但实际上应该翻译为`企业应用`，就是一种特定的应用类型。

`企业应用`涉及大量复杂数据的展示、操纵和存储以及对这些数据进行处理的业务流程的自动化，典型的例子有预订系统、金融系统、物流补给系统以及其他种种驱动现代商业运作的系统。`企业应用`与嵌入式系统、控制系统、电信系统或桌面应用系统不同，他们有特有的挑战和解决方案。

。。。后端租赁系统，它的业务“逻辑”几乎不能套用任何已有的逻辑模式，因为那些“逻辑”归根到底是商人们为争夺利益而制定的，一些古怪的小改动都可能对赢得某笔交易起关键作用，因此，每次生意上的一点点胜利就意味着系统复杂性的又一次增加。

很多人试图给`架构`下定义，但`架构`的定义很难统一，能统一的主要是以下两点
- 最高层次的系统分解
- 系统中不易改变的决定

`架构`是一种主观上的东西，是专家对系统设计的一些`可共享的理解`，一般的，这种可共享的理解表现为`系统中主要的组成部分`以及`这些组成间的交互关系`。它还包括一些决定，开发者希望这些决定及早做出，因为在开发者看来它们是难以改变的。(Ralph Johnson)

`企业应用`也很难下定义

`企业应用`一般都涉及到大量复杂数据，而且必须处理很多“不合逻辑”的业务规则，虽然有些模式是适合所有软件的，但是大多数都只适合某些特定的领域和分支

`企业应用`一般都涉及到大量数据、持久化数据、很多人同时访问数据、大量操作数据的用户界面、与散布在周围的其他企业应用集成。即使`企业`统一了集成技术，但还是会遇到业务过程中的差异以及数据中`概念的不一致`....成千上万的这类“一次性特殊情况“最终导致了`复杂的业务“非逻辑`，使得商业软件开发那么困难

常见`企业应用`
- B2C网上零售系统：用户多，既要考虑资源利用率又要考虑系统伸缩性
- 租约合同自动处理系统：用户少，但业务逻辑复杂
- 开支跟踪系统

不同的工具擅长不同的方面，要选择合适的工具

不必通读所有有关模式的书，只需要了解这些模式是干什么的，它们解决什么问题、它们是如何解决的，就足够了。一旦遇到对应的问题，再深入了解也不迟。

### Chapter 1 - Layering
- 可将某层视为整体，无需了解其他层
- 替代某层的实现
- 降低层与层之间的依赖
- 分层有利于标准化
- 一层可为多层使用

- 分层不能封装所有东西，有时会带来级联修改
- 过多层影响性能

tier和layer常互用

### Chapter 2 - Organizing Domain Logic
In organizing domain logic I’ve separated it into three primary patterns: `Transaction Script` (110), `Domain Model` (116), and `Table Module` (125)

在领域模型中，不再是由某个过程来控制逻辑，而是由每个对象都承担一部分逻辑。领域逻辑的缺点来自the complexity of using it and the complexity of your data source layer.

`Domain Model` has one instance of contract for each contract in the database whereas a `Table Module` has only one instance. .NET大量使用`Table Module`

### Chapter 3 - Mapping to relational database
separate SQL access from the domain logic and place it in separate classes

- Row Data Gateway: 一行一个对象
- Table Data Gateway：一个表一个对象

数据最好一次性通过一条SQL获取，而不是通过多次SQL

When people talk about object-relational mapping, mostly what they mean is these kinds of structural mapping patterns, which you use when `mapping between in-memory objects and database tables`.

Mapping Relationships
- First there’s a difference in representation, 如对象间reference
- 对象可多值存储

多值的问题既可以用外键关联，也可以用`Serialized LOB`，但一般是不需要按条件查询该值的场景

如何在关系数据库中表示inherience
- one table for all the classes in the hierarchy: `Single Table Inheritance`
    - 方便查询和修改，浪费空间
- one table for each concrete class: `Concrete Table Inheritance`
    - 查询方便，不易更改，更改base需要更改所有子类
- one table per class in the hierarchy: `Class Table Inheritance`
    - 简单，查询复杂

需要支持多个数据源的情况，每个数据源有些小的差异
- The simplest option is to have multiple mapping layers, one for each data source.
- 加一个逻辑层

减少使用`select *`，增删或调整列时会造成影响

### Chapter 4 - Web Presentation
两种模式
- script style，如CGI或java servlet，流式生成页面
- server page style，页面内嵌入代码，PHP，JSP

Model View Controller

View层
- Transform View
- Template View
- Two Step View

### Chapter 5 - Concurrency
并发带来的问题
- Lost updates
- Inconsistent read

两个重要的解决方案
- isolation
- immutability

Optimistic（冲突检测，读锁） and Pessimistic（冲突避免，直接不允许并发，写锁） Concurrency Control。选择的标准是冲突的频率和严重性

事务级别
- `serializable`
- `repeatable read`, which allows `phantoms`（如读的人可能看到新插入的一部分数据）
- `read committed`, which allows `unrepeatable reads`
- `read uncommitted`, which allows `dirty reads`

### Chapter 6 - Session State
- `会话迁移`，做不到`会话亲和`时需要迁移会话状态，保证服务
- `会话亲和`，保证某个用户的请求都有一个用户来处理（如果会话信息存储在server外，如cookie或者专门的session服务器，则不存在该问题）
    - 如果用IP来区分，需要考虑代理问题，此时大量请求都来自同一IP，此时可能压力不均匀

### Chapter 7 - Distribution Strategies
主要讲了下分布式对象（如java的RMI用到了），不推荐使用

分布式对象可封装很多东西，但you can't encapsulate the remote/in-process distinction. 本地调用很快并总是成功执行（抛异常也算，这里是相对于因为远端或网络问题）。

With two modules in the same process, it's best to make many fine-grained calls, but when modules are remote, then favor few corse-grained calls. `microservice`就属于后者。作者还写了[一篇文章说明这件事](https://martinfowler.com/articles/distributed-objects-microservices.html)

