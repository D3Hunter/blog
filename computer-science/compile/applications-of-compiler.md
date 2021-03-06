### phases and applications
- lexing
- parsing
- symbol table/symbol searching
- IR
    - graphical IRs
        - syntax-related trees
            - parse tree
            - AST
            - Level of Abstraction：编译器会根据使用用途同时使用high-level AST，low-level AST
            - DAG
                - A DAG is an AST with sharing. Identical subtrees are instantiated once, with multiple parents
        - graphs
            - DAG
            - Control-Flow Graph: models the flow of control between the basic Control-flow graph blocks in a program
            - Dependence Graph: encode the flow of values
            - Call Graph: represents the calling relationships among the procedures in a program
    - linear IRs
        - Stack-Machine Code
        - Three-Address Code
        - Representing Linear Codes: a set of quadruples: an operator, two operands, and a destination
    - hybrid IRs
    - IR in actual use
        - GCC: RTL/GIMPLE
        - LLVM: a linear three-address code
    - MAPPING VALUES TO NAMES
        - Static Single-Assignment Form: an IR that has a value-based name system, created by renaming and use of pseudo-operations called φ-functions SSA encodes both control and value flow.
        - Memory Models
            - Register-to-Register Model
            - Memory-to-Memory Model
- analyzing
    - type inferencing
- syntax highlighting
- pretty-print(formating)
- translation（抽象来说interpreter、compiler、decompilers、assemblers and disassemblers都属于translator）
    - A `source-to-source translator`, `source-to-source compiler` (S2S compiler), `transcompiler` or `transpiler`
        - 在github上搜索对应的topic，有很多开源的transpiler实现
        - A `transcompiler pipeline` is what results from `recursive transcompiling`.
        - Examples of transcompiled languages include `Closure Compiler`, `CoffeeScript`, `Dart`, `Haxe`, `TypeScript` and `Emscripten`.
        - `Recursive transpiling`is the process of applying the notion of transpiling recursively, to create a pipeline of transformations
        - Recursive transpiling takes advantage of the fact that transpilers may either **keep translated code as close to the source code as possible** to ease development and debugging of the original source code, or else they may change the structure of the original code so much, that the translated code does not look like the source code.
        - A `language-independent specification` (LIS) is a programming language specification providing a common interface usable for defining semantics applicable toward arbitrary language bindings.
    - 实现方式
        - syntax directed translation：直接基于parse结果处理，不使用context info，可生成AST，以可不生成（边parse边转换输出）
        - 创建AST，利用部分可用的context信息进行translate
        - 按照conventional compiler的实现方式
            - build a good front end for your language, including symbol tables and control and data flow analysis
            - 一种pipeline是转换过程直接输出文本，另一种是将原语言AST转换为目标语言AST，后一种还可以对目标语义进行一些优化等处理
        - tree pattern matching and rewriting
    - 可用的translation library
        - `DMS Software Reengineering Toolkit`.
            - DMS has parsers for many languages, can implement parsers for custom languages, automatically builds ASTs,
            - provides a lot of support for Life After Parsing, e.g., building symbol tables and flow analysis, does AST to AST transformation, and has pretty printers
    - Program transformations are usually semantics- (or "correctness-") preserving [optimization, translation, refinement, refactoring, ...] but can be used to alter the semantics of the a "program" (language instance) [add a parameter to a procedure, adjust all array bounds by one, remove all code related to a function,
- generation: after translation
- optimization
- refactoring: 一些规则可以归类到这里，如保留字变量名替换等
    - rename symbol
    - rename file
    - change signature
    - type migration
    - make static
    - move
    - copy
    - safe delete
    - extract symbols and abstract
    - inline
    - find and replace code duplicates
    - pull/push members up/down
    - replace inheritance with delegation
    - convert anonymous to inner
    - encapsulate fields
    - replace constructor with builder

### products about code translation
- http://www.semanticdesigns.com/
    - Programmer's Productivity Tools
        - These tools include code formatter/prettyprinter/beautifiers, code obfuscators, source code comparison tools, hyperlinked cross-references, and testing tools (branch coverage, profiling).
    - Enterprise Level Productivity Tools
        - The DMS® Software Reengineering Toolkit： This is a set of tools for carrying out custom re-engineering of medium and large scale software systems (documentation extraction, analysis, porting, translation, modification, interface changes, or other massive regular change) and/or domain-specific program generation.
            - 可参考这里：http://www.semanticdesigns.com/Products/DMS/DMSToolkit.html
            - http://www.semanticdesigns.com/Products/DMS/ProgramTransformation.html?Home=DMSToolkit
        - PARLANSE™ (A PARallel LANguage for Symbolic Expression)
- DMS的一个开源实现 http://www.program-transformation.org/
    - 有关program transformation的一些介绍
        - http://www.program-transformation.org/Transform/ProgramTransformation

### Typical Front End Features
- Full lexical analysis, including reading source files in ASCII (ISO8859-1) or UNICODE
    - Conversion of literal values (numbers, escaped strings) into native values to enable easy computation over literal values
    - Literal strings represented internally in UNICODE to support 16-bit characters
    - Preprocessor support for those languages requiring it
- Explicit grammars based directly on standards documents
- Automatic construction of complete abstract syntax tree
    - Capture of comments and formats (shape) of literal values
    - Ability to parse tens of thousands of files and millions of lines into same workspace, enabling interprocedural and cross-file - analysis/transformation
    - Ability to parse different languages into same workspace, enabling cross-language analysis/transformation
- Complete support for manipulating trees
    - Full procedural API to visit/query/update/construct syntax trees
    - Full source regneration by prettyprinting and/or fidelity printing of syntax trees with comments and lexical formats
    - Automatic construction of source-to-source transformation system
    - Ability to define custom attribute-grammar-based analyzers
- Available as source code to enable complete customization
    - Means to manage multiple language dialects with highly shared cores
- Robustness due to careful testing and application across multiple customers

### technologies are needed to realistically process computer language(s):
http://www.semanticdesigns.com/Products/DMS/LifeAfterParsing.html

- `Lexing and Parsing`:, ... of course. But there are some really nasty problems here, including :preprocessors:.
- `Representation Capture`: A way to represent and capture program structure
- `Symbol Tables`: A mapping between identifiers used in the program, and their meaning (and scope).
- `Inference Methods`: A way to understand the meaning and consequences of the written code
    - `Simple Fact Collection`: Inferences that are easy to extract from the program structure.
    - `Control Flow Analysis`: Data about the order in which activities occur in a program.
    - `Data Flow Analysis`: Data about how information flows from one part of the program to another.
    - `Symbolic Reasoning`: Method to compute complex consequences of semantics and various information flows.
- `Pattern Matching and Transformation Capability`: Means to find program points that look like places of interest, as well as means to convert one program representation instance into others, to provide optimizations or translation to another representation
- `Pretty-Printing`: If the representation is modified, one needs to be able to regenerate valid source code from it.
- Multi-module and multi-lingual Integration: Inclusion of other programs in the same or another notation to allow one to process systems of code.
- `Multi-module and multi-lingual Integration`: Real software systems are not coded entirely in one language (Java? What, no SQL or HTML?)

