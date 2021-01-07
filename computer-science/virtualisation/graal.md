`Truffle` is a Java library that helps you to write an `abstract syntax tree (AST) interpreter` for a language. An AST interpreter is probably the simplest way to implement a language, because it works directly on the output of the parser and doesn't involve any bytecode or conventional compiler techniques, but it is often slow. We have therefore combined it with a technique called `partial evaluation`, which allows `Truffle` to use `Graal` to automatically provide a `just-in-time compiler` for your language, just based on your AST interpreter.

`GraalVM` enables a very diverse set of new functionality:
- it's a platform on which you can build more powerful languages and tools and put them into more environments.
- It lets you pick the language and modules you want no matter where the program is running or which languages you're using already.

### Top 10 Things To Do With GraalVM
https://github.com/chrisseaton/graalvm-ten-things
1. High-performance modern Java
2. Low-footprint, fast-startup Java
3. Combine JavaScript, Java, Ruby, and R
4. Run native languages on the JVM
5. Tools that work across all languages
6. Extend a JVM-based application
7. Extend a native application
8. Java code as a native library
9. Polyglot in the database
10. Create your own language

### Sulong
Sulong is a high-performance LLVM bitcode interpreter built on the GraalVM by Oracle Labs.

Sulong is written in Java and uses the Truffle language implementation framework and Graal as a dynamic compiler.

With Sulong you can execute C/C++, Fortran, and other programming languages that can be transformed to LLVM bitcode on Graal VM. To execute a program, you have to compile the program to LLVM bitcode by a LLVM front end such as `clang`.

## graalVM
`GraalVM` is a high-performance runtime that provides significant improvements in application performance and efficiency which is ideal for microservices. It is designed for applications written in Java, JavaScript, LLVM-based languages such as C and C++, and other dynamic languages. It `removes the isolation between programming languages` and `enables interoperability in a shared runtime`.

## Truffle Language Implementation Framework
The `Truffle framework` (henceforth “Truffle) is an open-source library for building tools and programming languages implementations as interpreters for self-modifying Abstract Syntax Trees. Together with the open-source `GraalVM` compiler, Truffle represents a significant step forward in programming language implementation technology in the current era of dynamic languages.

实现一个`dynamic language`的`interpreter`，需要自行实现一个`编译器front-end`和`Runtime`。`Runtime`包括执行器（比如AST interpreter，这个在Truffle还是需要自行编写的）、类型系统（Truffle也支持）、对象／内存的管理(如Truffle的OSM)、JIT和其他优化项（如Truffle的Block相关优化）等，使用`Truffle`除执行器外都可复用现有框架。

`truffle-dsl-processor`(`<scope>provided</scope>`，仅编译时用到)里包含了相关的`annotation processor`，处理`GenerateWrapper`标记的类

- `GenerateWrapper`: All non-final and non-private methods starting with `execute` are overridden by the generated wrapper. Every execute method must have `VirtualFrame` as the first declared parameter.
- `Specialization`: Defines a method of a node subclass to represent one specialization of an operation. A specialization must have at least as many parameters as there are `NodeChild` annotations declared for the enclosing operation node. These parameters are declared in the same order as the `NodeChild` annotations (linear execution order). We call such parameters dynamic input parameters.
- `TruffleLanguage.Provider`. Used to register a TruffleLanguage using a `ServiceLoader`. 通过Truffle DSL自动生成
- `BlockNode`: Represents a standard node for guest language blocks. 应该也可以直接用自己写的`BlockNode`(存储内部statements，循环执行），但这样应该就利用不了truffle的优化了
- `RootCallTarget`: Represents the target of a call to a RootNode, i.e., to another tree of nodes.
- `DirectCallNode`: Represents a direct call to a `CallTarget`. Direct calls are calls for which the CallTarget remains the same for each consecutive call.
- `TypeSystem`: Each `Node` has one `TypeSystem` at its root to define the types that can be used throughout the system.
- `CompilerDirectives`: Directives that influence the optimizations of the Truffle compiler.
- `CachedLibrary`: The cached library annotation allows to use `Truffle Libraries` conveniently in `specializations` or `exported messages`. It is designed as the primary way of using libraries.

##  simplelanguage
- 符号表可参考`SLNodeFactory.lexicalScope`。每次assignment都创建一个新的变量，同一函数内的variable是使用同一个FrameDescriptor创建的slot，因此在内层block中对外层变量做assignment是直接修改外层变量。
- 禁止编译native image: `export SL_BUILD_NATIVE=false`
- 一些可能的增强项
    - 只能通过main来运行，main不支持带参数

## An Object Storage Model for the Truffle Language Implementation Framework
Language implementers aiming at `developing new runtimes` have to design all the runtime mechanisms for managing dynamically typed objects from scratch. This not only leads to potential code duplication, but also impacts the actual time needed to develop a fully-fledged runtime. In this paper we address this issue by introducing a common `object storage model (OSM)` for Truffle that can be used by language implementers to develop new runtimes.

Using Truffle, a language runtime can be developed just by implementing an `AST interpreter`. More precisely, `the AST interpreter is the language runtime`.

having the following properties:
- Generality.
- Extensibility.
- High performance.

An `object model` defines the properties of objects in a specific programming language as well as the semantics of operations on them.

As with standard `AST interpreters`, the AST is evaluated by recursively executing its nodes in `post-order traversal`. In contrast to standard AST interpreters, however, Truffle ASTs can `self-optimize`: based on profiling feedback gathered at run time, AST nodes can speculatively replace themselves with specialized variants that can eventually be compiled into highly optimized machine code

The Truffle OSM maps guest-language object instances to storage objects that store its data in the form of properties.

An object consists of two separate parts: the `object storage`, containing perinstance data, and the `shape`, which provides a mapping of member names to locations in the object storage (similar to a Java class).

Every object created using this object storage model is an instance of a so-called `storage class`, a Java class that acts as a container for per-instance data.

Any interaction with Truffle objects—rather than accessing data directly—goes through a set of `operations` defined by the language runtime.

