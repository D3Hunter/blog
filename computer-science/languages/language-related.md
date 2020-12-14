### programming languages
- `type erasure` is the load-time process by which explicit type annotations are removed from a program, before it is executed at run-time. Operational semantics that do not require programs to be accompanied by types are called `type-erasure semantics`, to be contrasted with `type-passing semantics`.
- A `self-hosting compiler` is one that can compile its own source code.
- `self-hosting` is the use of a program as part of the toolchain or operating system that produces new versions of that same program
- `Variance` refers to how subtyping between more complex types relates to subtyping between their components. For example, how should a list of Cats relate to a list of Animals?
    - `covariant`: the subtyping relation of the simple types are preserved for the complex types.
        - "list of Cat" is a subtype of "list of Animal"
    - `contravariant`: the subtyping relation of the simple types is reversed for the complex types.
        - "function from Animal to String" is a subtype of "function from Cat to String"

