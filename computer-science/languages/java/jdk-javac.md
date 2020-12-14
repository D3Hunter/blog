### javac source code
- Enter/MemberEnter: put symbols into scope
- Context 每次编译一个，其他跟当前Context相关的对象可通过该对象获取
- Env; 传递给 tree visitor，记录重要父节点，及其他信息
- Attr: attibute the AST tree, associate symbol with tree node
- flow: Perform dataflow checks on an attributed parse tree.
- desugar: Prepare attributed parse trees, in conjunction with their attribution contexts, for source or code generation
- generate: Generates the source or class file for a list of classes
- Pool: constant pool
- item: Items are objects that stand for addressable entities in the bytecode. Each item supports a fixed protocol for loading the item on the stack, storing into it, converting it into a jump condition, and several others

compile2: The phases following annotation processing: attribution, desugar, and finally code generation.

### jdk7-b99 source code
- JCTree.Visitor 没处理中间的节点
- 将javac放到mvn中
- PathFileObject JavacPathFileManager javac用到了了nio的一些API，这些API在正式的JDK里没有
    - java.nio.files.attribute.Attributes：正式JDK没有该类
    - Path在jdk源码中为抽象类，在正式jdk中为interface
- 使用IDEA调试，实际运行的是tools.jar中的对应类
- ast 通过一个field绑定symbol，symbol跟scope相互独立，symbol内的子symbol通过一个scope成员存储，而不是一个scoped symbol
- Type跟Symbol相互独立

java compiler phases:
- annotation processing
- attribution
- desugar
- code generation

