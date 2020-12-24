There are only two hard things in computer science: `cache invalidation` and `naming things` – Phil Karlton. 还有个版本添加了 `oﬀ-by-one errors`.

### code
数据和算法
代码写在哪儿合适？最简单的是写在有数据的地方，但这样耦合度高，抽象度不够，可读性不好，考虑适当分层

命名问题，底层是概念定义问题，是对问题的理解和总结

通用的代码概念：
- (progress) monitor
- error processing
- engine
- processor
- config
- context
- result
- report
- report/error code
- report code message or extra info
- code description
- description language

非通用概念
- rule
- rule group
- rule manager

鲁棒性，扩展性，易用性、统一性，多语言支持
- multi-thread support
- security
- log

### naming
[How to stop naming Java classes with the "Manager" suffix](https://dev.to/scottshipp/how-to-stop-naming-java-classes-with-the-manager-suffix-48la)

It seems `Helper`, `Manager`, and `Util` are the unavoidable nouns you attach for coordinating classes that contain no state and are generally procedural and static. An alternative is `Coordinator`.

`Attribute` `Base` `Bucket` `Builder` `Collection` `Container` `Context` `Controller` `Converter` `Coordinator` `Designer` `Editor` `Element` `Entit`y` Exception` `Factory` `Handler` `Helper` `Info` `Item` `Job` `Manager` `Node` `Option` `Protocol` `Provider` `Reader` `Service` `Target` `Type` `Utils` `View` `Writer`


### 代码编写相关
- `normalization`由接受方处理（调用方太多，处理较麻烦，另外通过该方式也能保证输入到系统中的数据是准确的，避免调用方遗忘的情况）；对于一个模块，仅在模块入口做`normalization`，内部不再关心
- 在实现的过程中自然而然形成了新的解决方法，原设想需要的内容、难以解决的问题发现并不存在。
- 如果不好处理，不好处理的原因在哪儿？一旦确定了原因，往往就知道了怎么处理
- 对于稍大些的系统，有充足单测和回归测试能极大的减少后续扩展新功能的成本，否则新功能上了，老功能出bug，反复修复，临发版还不能保证功能过了

### code that's easy to reason about
refers to code that is easy to "execute in your head".
- short, clearly written, with good names and minimal mutation of values
    - 相对的是poor names, variables that constantly change value and convoluted branching
- no side effects
    - single-responsibility principle (SRP)
    - Immutability
- Does not rely on or affect external state
    - 会让代码hard to reason about
        - 全局变量或类似state
        - 多线程、共享state
- Given the same argument, it will always return the same corresponding output

SOLID principles, GRASP patterns, or STUPID anti-patterns. KISS principle DRY, Law of Demeter

### What kind of code is good
[What is good code?](https://thoughtbot.com/blog/what-is-good-code)
https://thoughtbot.com/blog/authors/joe-ferris
We often discuss the principles we use to write what we consider good code - test-driven development, object-oriented programming, SOLID, DRY, Law of Demeter - the list goes on. Sometimes it’s useful to remind ourselves of the `fundamentals`.
- Code needs to `work as expected`.
- When code is `easy to understand`: we can change or extend it faster and are less likely to make a mistake in the process. Readability counts.
- When code is `easy to change`, we can iterate on user feedback faster.
- When code is `fun to work with`, we’re happier. Building software is our full time job. If we go home every day feeling wrung dry, something is wrong with our process.

