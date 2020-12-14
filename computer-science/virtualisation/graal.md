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

### Truffle Language Implementation Framework
The `Truffle framework` (henceforth “Truffle) is an open-source library for building tools and programming languages implementations as interpreters for self-modifying Abstract Syntax Trees. Together with the open-source `GraalVM` compiler, Truffle represents a significant step forward in programming language implementation technology in the current era of dynamic languages.

`GenerateWrapper`: All non-final and non-private methods starting with `execute` are overridden by the generated wrapper. Every execute method must have `VirtualFrame` as the first declared parameter.

`Specialization`: Defines a method of a node subclass to represent one specialization of an operation. A specialization must have at least as many parameters as there are `NodeChild` annotations declared for the enclosing operation node. These parameters are declared in the same order as the `NodeChild` annotations (linear execution order). We call such parameters dynamic input parameters.

`TruffleLanguage.Provider`. Used to register a TruffleLanguage using a `ServiceLoader`. 通过Truffle DSL自动生成

