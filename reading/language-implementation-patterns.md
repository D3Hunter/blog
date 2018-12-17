### Language Implementation Patterns
The kind of application we’re building dictates the stages of the pipeline and how we hook them together. There are four broad application categories:
- Reader: A reader builds a data structure from one or more input streams. The input streams are usually text but can be binary data as well. Examples include configuration file readers, program analysis tools such as a method cross-reference tool, and class file loaders.
- Generator: A generator walks an internal data structure and emits output. Examples include object-to-relational database mapping tools, object serializers, source code generators, and web page generators.
- Translator or Rewriter: A translator reads text or binary input and emits output conforming to the same or a different language. It is essentially a combined reader and generator. Examples include translators from extinct programming languages to modern lan- guages, wiki to HTML translators, refactorers, profilers that in- strument code, log file report generators, pretty printers, and mac- ro preprocessors. Some translators, such as assemblers and com- pilers, are so common that they warrant their own subcategories.
- Interpreter: An interpreter reads, decodes, and executes instruc- tions. Interpreters range from simple calculators and POP protocol servers all the way up to programming language implementations such as those for Java, Ruby, and Python.

The best way to design a language application is to `start with the end in mind`. First, figure out what information you need in order to generate the output. That tells you what the final stage before the generator computes. Then figure out what that stage needs and so on all the way back to the reader.

Such applications are called `syntax-directed` applications because they can generate output as soon as they recognize a construct. The key characteristic of syntax-directed applications is that they translate input phrase by phrase using a single pass over the input.

Most language applications, however, need to build an `intermediate representation (IR)` or intermediate form.

`Parse trees` record the sequence of rules a parser applies as well as the tokens it matches. Interior parse tree nodes represent rule applications, and leaf nodes represent token matches. `Parse trees` are nice to look at and help us understand how a parser interpreted an input phrase. But, a parser execution trace isn’t really the best IR...The critter that we end up with is called an `abstract syntax tree (AST)`.

To figure out what ASTs should look like, let’s start with a list of design guidelines. An IR tree should be the following:
- Dense: No unnecessary nodes
- Convenient: Easy to walk
- Meaningful: Emphasize operators, operands, and the relationship between them rather than artifacts from the grammar

##### Patterns
1. Mapping grammers to recusive-decent recognizers
2. LL(1) recusive-decent lexer
3. LL(1) recusive-decent parser
4. LL(k) recusive-decent parser
5. Backtracing parser
6. Memorizing parser
7. Predicated parser
8. Parse Tree
9. Homogeneous AST
10. Normalized Heterogeneous AST
11. Irregular Heterogeneous AST
12. Embedded Heterogeneous Tree Walker
13. External Tree Visitor
14. Tree Grammar
15. Tree Pattern Matcher
16. Symbol Table for Monolithic Scope
17. Symbol Table for Nested Scopes
18. Symbol Table for Data Aggregates
19. Symbol Table for Classes
20. Computing Static Expression Types
21. Automatic Type Promotion
22. Enforcing Static Type Safety
23. Enforcing Polymorphic Type Safety
24. Syntax-Directed Interpreter
25. Tree-Based Interpreter
26. Bytecode Assembler
27. Stack-Based Bytecode Interpreter
28. Register-Based Bytecode Interpreter
29. Syntax-Directed Translator
30. Rule-Based Translator
31. Target-Specific Generator Classes(Model-driven translation)
- This pattern describes a class library whose sole purpose is to represent and generate output constructs in a particular language.

A `template processor` (also known as a template engine or template parser) is software designed to combine templates with a data model to produce result documents.

In `theoretical computer science` and `formal language theory`, a `regular tree grammar (RTG)` is a formal grammar that describes a set of directed trees, or terms. A `regular word grammar` can be seen as a special kind of regular tree grammar, describing a set of single-path trees.

The process of matching and rewriting trees is formally called `term rewriting`.

In mathematics, computer science, and logic, `rewriting` covers a wide range of (potentially non-deterministic) methods of replacing subterms of a formula with other terms.

`Term rewriting`(`Rule-Based Translation`) is a surprisingly simple computational paradigm that is based on the repeated application of simplification rules. It is particularly suited for tasks like symbolic computation, program analysis and program transformation. Rule-based systems:
- `Meta-Environment4 (ASF+SDF)`
    - ASF(Algebraic Specification Formalism): a notation for describing rewrite rules
    - SDF(Syntax Definition Formalism): A notation for describing the grammar of programming and application languages.
    - 已停止，开发团队已经转向`Rascal`
- `Stratego/XT`, 转向`Spoofax`
- `Txl`

We distinguish program entities via these three parameters:
- Name
- Catagory
- Type

A reference’s scope stack is the set of scopes on the path to the root of the scope tree. We call this stack the `semantic context`.

An `interpreter` simulates an idealized computer in software. Such “computers” have a `processor`, `code memory`, `data memory`, and (usually) a `stack`.

There are three things to consider when building an interpreter:
- how to store data
- how and when to track symbols
- how to execute instructions

The basic idea behind executing instructions is called the `fetch-decode-execute` cycle.

template engines:
- StringTemplate
- Velocity
- FreeMarker

StringTemplate
- Dynamically typed
- Pure functional
- Dynamic scoping
- Lazy evaluation

retargeting strategy
- altering or swapping in new templates. The template hierarchy stays the same
- changing the template hierarchy. assemble different hierarchies using the templates themselves

#### pretty printing papers
- M Van Den Brand: Generation of Formatters for Context-free Languages
- M De Jonge: Pretty-Printing for Software Reengineering
- M van den Brand: The Asf+Sdf Meta-environment: A Component-Based Language Development Environment
- M De Jonge: A Pretty-Printer for Every Occasion
- M van den Brand: Industrial applications of ASF+SDF

#### DSL papers
- Marjan Mernik: When and how to develop domain-specific languages

### Visitor Pattern
In object-oriented programming and software engineering, the `visitor design pattern` is a way of separating an algorithm from an object structure on which it operates. A practical result of this separation is the ability to add new operations to existent object structures without modifying the structures. It is one way to follow the `open/closed principle`.

The `visitor pattern` requires a programming language that supports `single dispatch`, as common object-oriented languages...Thus, the implementation of the `visit` method is chosen based on both the dynamic type of the element and the dynamic type of the visitor. This effectively implements `double dispatch`.

In software engineering, `double dispatch` is a special form of `multiple dispatch`, and a mechanism that dispatches a function call to different concrete functions depending on the runtime types of two objects involved in the call.


Visitors that directly emit text with print statements work fine as long as the order of input and output constructs is very similar. Otherwise, we could use:
- output driven: “pulls” information from the input model according to the output order.
- input driven: compute information and translate phrases, then emit output

Besides, computing output strings in a general-purpose programming language ain’t exactly pretty. All is not lost, though. We can use `templates`, which are the best of both worlds.

