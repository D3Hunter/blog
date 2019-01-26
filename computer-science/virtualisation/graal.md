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

