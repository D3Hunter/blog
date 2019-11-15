#### JIT(Just in time) compilation
In computing, just-in-time (JIT) compilation (also dynamic translation or run-time compilations) is a way of executing computer code that involves compilation during execution of a program – at run time – rather than prior to execution.
1. create machine code at program run-time.
    - this is exactly what a compiler does.
2. execute that machine code, also at program run-time.

#### libjit
The goal of the `libjit` project is to provide an extensive set of routines that takes care of the bulk of the JIT process, without tying the programmer down with language specifics. Where we provide support for common object models, we do so strictly in add-on libraries, not as part of the core code.

Unlike other systems such as the `JVM`, `.NET`, and `Parrot`, `libjit` is not a virtual machine in its own right. It is the foundation upon which a number of different virtual machines, dynamic scripting languages, or customized rendering routines can be built.

The `LLVM` project has some similar characteristics to `libjit` in that its intermediate format is generic across front-end languages. It is written in C++ and provides a large set of compiler development and optimization components; much larger than `libjit` itself provides. According to its author, Chris Lattner, a subset of its capabilities can be used to build JIT’s.

#### Parrot
`Parrot` is a virtual machine designed to efficiently compile and execute bytecode for dynamic languages. Parrot currently hosts a variety of language implementations in various stages of completion, including `Tcl`, `Javascript`, `Ruby`, `Lua`, `Scheme`, `PHP`, `Python`, `Perl 6`, `APL`, and a `.NET bytecode translator`.

#### libgc
The Boehm-Demers-Weiser conservative C/C++ Garbage Collector (libgc, bdwgc, boehm-gc)

This is a garbage collecting storage allocator that is intended to be used as a plug-in replacement for C's malloc.

#### Neko
Neko is a high-level dynamically typed programming language.

You can also write generators from your own language to Neko and then use the Neko Runtime to compile, run, and access existing libraries.

Neko has a compiler and a virtual machine. The Virtual Machine is both very lightweight and well optimized, so it can run very quickly. The VM can be easily embedded into any application and your libraries can be accessed using the C foreign function interface.

#### Haxe
Haxe is an open source high-level strictly-typed programming language with a fast optimizing cross-compiler.

Haxe can build cross-platform applications targeting `JavaScript`, `C++`, `C#`, `Java`, `JVM`, `Python`, `Lua`, `PHP`, `Flash` and allows access to each platform native capabilities. Haxe has its own VMs (`HashLink` and `NekoVM`) but can also run in interpreted mode.

Code written in Haxe can be compiled to any target Haxe supports.

#### HashLink
HashLink is a virtual machine for Haxe

HashLink bytecode can be either run through HL/JIT virtual machine or converted to C with HL/C:

