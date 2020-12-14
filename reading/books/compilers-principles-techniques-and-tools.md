### Chapter 1 - Intruction
Programming languages are notations for describing computations to people and to machines.

- `compiler` is a program that can read a program in one language - `the source language` - and translate it into an equivalent program in another language - `the target language`.
- `interpreter` is another common kind of language processor. Instead of producing a target program as a translation, an interpreter appears to directly execute the operations specified in the source program on inputs supplied by the user.
- `preprocessor`: collecting the source program, expand macros
- `assembler`: processes assembly language and produces relocatable machine code as its output
- `linker`: resolves external memory addresses, link relocatable machine code with other relocatable object files and library files into the code that actually runs on the machine.
- `loader`: then puts together all of the executable object files into memory for execution

Two parts of compiler: `analysis`(`front end`) and `synthesis`(`back end`).

classification of languages.
- by generation.
- by `imperative` or `declarative`
    - `imperative` for languages in which a program specifies how a computation is to be done
        - In imperative languages there is a notion of program state and statements that change the state.
    - `declarative` for languages in which a program specifies what computation is to be done.
- von Neumann language
- object-oriented language
- Scripting languages

Compiler optimizations must meet the following design ob jectives:
- The optimization must be correct, that is, preserve the meaning of the compiled program,
- The optimization must improve the performance of many programs,
- The compilation time must be kept reasonable, and
- The engineering effort required must be manageable.

Applications of Compiler Technology
- Implementation of High-Level Programming Languages
- Optimizations for Computer Architectures
    - Parallelism
    - Memory Hierarchies
- Design of New Computer Architectures
    - RISC
    - Specialized Architectures
- Program Translations
    - Binary Translation
    - Hardware Synthesis
    - Database Query Interpreters
    - Compiled Simulation
- Software Productivity Tools
    - Type Checking
    - Bounds Checking
    - Memory-Management Tools

A language uses `static scope` or `lexical scope` if it is possible to determine the scope of a declaration by looking only at the program. Otherwise, the language uses `dynamic scope`. With `dynamic scope`, as the program runs, the same use of `x` could refer to any of several different declarations of `x`.(method overriding)

- The `environment` is a mapping from names to locations in the store.
- The `state` is a mapping from locations in store to their values.

In a sense, the `dynamic rule` is to time as the `static rule` is to space.

Parameter Passing Mechanisms
- call-by-value
- call-by-reference

Aliasing: an interesting consequence of call-by-reference parameter passing or its simulation. It is possible that two formal parameters can refer to the same location.

### Chapter 2 - A Simple Syntax-Directed Translator
A context-free grammar has four components:
1. A set of `terminal` symbols
2. A set of `nonterminals`
3. A set of productions
4. A designation of one of the nonterminals as the `start symbol`.

The terminal strings that can be derived from the `start symbol` form the `language` defined by the `grammar`.

`Parsing` is the problem of taking a string of terminals and figuring out how to derive it from the `start symbol` of the `grammar`, and if it cannot be derived from the `start symbol` of the `grammar`, then reporting syntax errors within the string.

A `parse tree` pictorially shows how the `start symbol` of a `grammar` derives a string in the `language`.

From left to right, the leaves of a `parse tree` form the `yield` of the tree, which is the string `generated` or `derived` from the `nonterminal` at the root of the `parse tree`.

The process of finding a `parse tree` for a given string of terminals is called `parsing` that string.

When an operand has operators to its left and right, `associativity` is used to decide which operator applies to that operand.

`Syntax-directed translation` is done by attaching rules or program fragments to productions in a grammar.

Two concepts related to `syntax-directed translation`:
- An `attribute` is any quantity associated with a programming construct(grammar symbols (nonterminals and terminals)).
    - The idea of associating quantities with programming constructs can be expressed in terms of `grammars`.
- A `translation scheme` is a notation for attaching `program fragments` to the productions of a grammar.
    - 注意`syntax-directed definition`是用`semantic rules`计算`attributes`，这里是`program fragments`或`semantic actions`

`Syntax-directed translations` will be used to translate infix expressions into postfix notation, to evaluate expressions, and to build syntax trees for programming constructs.

A `syntax-directed definition` associates
1. With each grammar symbol, a set of `attributes`, and
2. With each production, a set of `semantic rules` for computing the values of the attributes associated with the symbols appearing in the production.

- An `attribute` is said to be `synthesized` if its value at a parse-tree node `N` is determined from attribute values at the children of `N` and at `N` itself.
- Informally, `inherited attributes` have their value at a parse-tree node determined from attribute values at the node itself, its parent, and its siblings in the parse tree.

`FIRST(α)` to be the set of terminals that appear as the first symbols of one or more strings of terminals generated from `α`. If `α` is `ε` or can generate `ε`, then `ε` is also in `FIRST(α)`.

Trees growing down to the right(`right recursive`) make it harder to translate expressions containing `left-associative` operators, such as minus.

In an `abstract syntax tree` for an expression, each interior node represents an operator; the children of the node represent the operands of the operator.

A sequence of input characters that comprises a single `token` is called a `lexeme`.

The term `scope` by itself refers to a portion of a program that is the scope of one or more declarations.

The `most-closely nested` rule for blocks is that an identifier `x` is in the scope of the most-closely nested declaration of `x`.

Two Kinds of Intermediate Representations:
- Trees, including `parse trees` and `(abstract) syntax trees`.
- Linear representations, especially "three-address code".

### Chapter 3 - Lexical Analysis
The `token name` infuences parsing decisions, while the `attribute value` infuences translation of tokens after the parse.

- "panic mode" recovery. We delete successive characters from the remaining input, until the lexical analyzer can nd a well-formed token at the beginning of what input is left
- Delete one character from the remaining input.
- Insert a missing character into the remaining input.
- Replace a character by another character.
- Transpose two adjacent characters.

The (Kleene) `closure` of a language `L`, denoted `L*`, is the set of strings you get by concatenating L zero or more times.

Finally, the `positive closure`, denoted `L+`, is the same as the `Kleene closure`, but without the term `L0`. That is, `ε` will not be in `L+` unless it is in `L` itself.

`Transition diagrams` have a collection of nodes or circles, called `states`. Each `state` represents a condition that could occur during the process of scanning the input looking for a lexeme that matches one of several patterns.
- Certain `states` are said to be `accepting`, or `final`.
- In addition, if it is necessary to retract the `forward` pointer one position (i.e., the lexeme does not include the symbol that got us to the accepting state), then we shall additionally place a `*` near that accepting state.
- One `state` is designated the `start state`, or `initial state`; it is indicated by an `edge`, labeled `start`, entering from nowhere.

处理保留字
- Install the reserved words in the symbol table initially.
- 对保留字使用单独的`Transition diagrams`

Both `deterministic` and `nondeterministic` finite automata are capable of recognizing the same languages. In fact these languages are exactly the same languages, called the `regular languages`.

`deterministic nite automaton (DFA)` is a special case of an `NFA`.
1. There are no moves on input `ε`, and
2. For each state `s` and input symbol `a`, there is exactly one edge out of `s` labeled `a`.

Every `regular expression` and every `NFA` can be converted to a `DFA` accepting the same language.

Conversion of an `NFA` to a `DFA`: The general idea behind the `subset construction` is that each state of the constructed `DFA` corresponds to a set of `NFA` states.

`augmented regular expression` `(r)#`

1. constructs a `DFA` directly from a `regular expression`, without constructing an intermediate `NFA`.
    - The resulting `DFA` also may have fewer states than the `DFA` constructed via an `NFA`.
2. minimizes the number of states of any `DFA`, by combining states that have the same future behavior.
3. produces more compact representations of `transition tables` than the standard, two-dimensional table.

It is useful, as we shall see, to present the `regular expression` by its `syntax tree`, where the leaves correspond to operands and the interior nodes correspond to operators. An `interior node` is called a `cat-node`, `or-node`, or `star-node` if it is labeled by the `concatenation operator (dot)`, `union operator |`, or `star operator *`, respectively.

To construct a `DFA` directly from a `regular expression`, we construct its `syntax tree` and then compute four functions: `nullable`, `firstpos`, `lastpos`, and `followpos`.

We can represent the function `followpos` by creating a `directed graph` with a node for each position and an arc from position `i` to position `j` if and only if `j` is in `followpos(i)`.

There is always a unique (up to state names) `minimum state DFA` for any `regular language`.

The intended use of the structure of Fig. 3.66 is to make the `next-check arrays` short by taking advantage of the similarities among states. 压缩`transition table`，参考https://stackoverflow.com/a/29960371/1347716

- Tokens. The lexical analyzer scans the source program and produces as output a sequence of tokens.
- Lexemes. Each time the lexical analyzer returns a token to the parser, it has an associated lexeme - the sequence of input characters that the token represents.
- Patterns. Each token has a pattern that describes which sequences of characters can form the lexemes corresponding to that token.
- Regular Expressions. These expressions are commonly used to describe patterns.
- Regular Definitions. Complex collections of languages, such as the patterns that describe the tokens of a programming language, are often defined by a regular definition, which is a sequence of statements that each define one variable to stand for some regular expression.
- Transition Diagrams. The behavior of a lexical analyzer can often be described by a transition diagram.
- Finite Automata. formalization of transition diagrams. Unlike transition diagrams, finite automata can make transitions on empty input as well as on input characters.
- Deterministic Finite Automata. A DFA is a special kind of finite automaton that has `exactly one transition out of each state for each input symbol`.

