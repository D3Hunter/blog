The `compiler` takes as input a program written in some language and produces as its output an equivalent program.

The `front end` focuses on understanding the source-language program. The `back end` focuses on mapping programs to the target machine.

`LR`: `left-to-right scan`, `reverse rightmost derivation`

An `LR(K)` parser uses, at most, `k` lookahead symbols. Additional lookahead allows an `LR(2)` parser to recognize a larger `set of grammars` than an `LR(1)` parsing system. Almost paradoxically, however, the added lookahead does not increase `the set of languages` that these parsers can recognize. `LR(1)` parsers accept the same set of languages as `LR(K)` parsers for `k > 1`. The `LR(1)` grammar for a language may be more complex than an `LR(K)` grammar.

`Handle`: a pair,`[A -> β,k]`, such that `β` appears in the frontier with its right end at position `k` and replacing `β` with `A` is the next step in the parse

How can the `LR(1)` parser use a `DFA` to find the `handles`, when we know that the language of parentheses is not a regular language? The `LR(1)` parser relies on a simple observation: `the set of handles is finite`. `The set of handles` is precisely `the set of complete LR(1) items`—those with the placeholder • at the right end of the item’s production. Any language with a finite set of sentences can be recognized by a `DFA`. Since the number of productions and the number of lookahead symbols are both finite, the number of complete items is finite, and the language of `handles` is a regular language.

An `attribute grammar` is a formal way to define `attributes` for the `productions of a formal grammar`, associating these attributes with values. The evaluation occurs in the nodes of the `abstract syntax tree`, when the language is processed by some `parser` or `compiler`.

`ISA`: Instruction set architecture

`AR`: activation record

In computer architecture, a `delay slot` is an instruction slot that gets executed without the effects of a preceding instruction. The most common form is a single arbitrary instruction located immediately after a branch instruction on a RISC or DSP architecture; this instruction will execute even if the preceding branch is taken. 在`pipelined architecture`

`register spilling` - (By analogy with spilling the contents of an overfull container) When a compiler is generating machine code and there are more live variables than the machine has registers and it has to transfer or "`spill`" some variables `from registers to memory.`

`Critical edge`: In a CFG, an edge whose source has multiple successors and whose sink has multiple predecessors is called a criticaledge.

In compiler theory, `peephole optimization` is a kind of optimization performed over a very small set of instructions in a segment of generated code. The set is called a "`peephole`" or a "`window`". It works by recognizing sets of instructions that can be replaced by shorter or faster sets of instructions. 一般是在`Basic Block`上处理。

#### Taxonomy of Machine Indenpendent GLobal Compiler Optimizations
- Redundancy
    - Rudundancy Elimination
    - Partial Redundancy Elimination
    - Consolidation
- Code Motion
    - Loop Invariant Code Motion
    - Consolidation
    - Global Scheduling
    - Constant Propagation
- Useless code
    - Dead Code elimination
    - Partial D.C.E
    - Constant Propagation
    - Algebraic Simplication
- Other Opportunities
    - Re-association
    - Replication
- Specialization
    - Replication
    - Strength Reduction
        - Operator Strength Reduction
        - Linear Function test replacement
    - Constant Propagation
    - Method Caching
    - Heap->Stack Allocation
    - Tail Recusion Elimination

#### Lazy Code Motion
- `DEExpr(b)` contains expresions defined in `b` that survived to the end of `b`. `e ∈ DEExpr(b):` evaluating `e` at the end of `b` produces the same value for `e` as evaluating it in its original position.
- `UEExpr(b)` contains expressions defined in `b` in which all arguments are upward exposed arguments. `e ∈ UEExpr(b):` evaluating `e` at the start of `b` produces the same value for `e` at evaluating it in its original position.
- `KILLExpr(b)` contains those expressions whose arguments are (re)defined in `b`. `e ∈ KILLExpr(b):` evaluating `e` at the start of `b` does not produce the same result as evaluating it at its end. 该集合不要求一定是在`b`中定义，前两个要求是在`b`里（重）定义的。
- `e ∈ AvailOut(b)`: evaluating `e` at end of `b` produces the same result for `e`. `AvailOut` tells the compiler how far forware `e` can move the evaluation of `e`, ignoring any uses of `e`.
- `e ∈ AntIn(b)`: evaluating `e` at start of `b` produces the same value for `e`. AntIn tells the compiler how far backward `e` can move.

#### Code Generation
- Instruction Selection
- Instruction Scheduling
- Register Allocation

#### Instruction Selection
- tree-pattern matching
- peephole optimization

Instruction Scheduler和Register Allocator虽然用到了processor-dependent的内容，但是这部分内容可以参数化，从而做到target-independent。Instruction selector也可以通过给定的spec信息用back-end generator生成。就像parser-generator一样。但为了用到target相关特性、或为了符合target的特殊特征，或多或少也会需要一些特定处理。

#### Instruction Scheduling
Informally, `instruction scheduling` is the process whereby a compiler reorders the operations in the compiled code in an attempt to decrease its running time.

`List scheduling` has been the dominant paradigm that compilers has used to schedule operations for many years.

`Stall`: the delay caused by a hardware interlock that prevents a value from being read until its defining operation completes.

`Interlock`: an interlock is the mechanism that detects the premature issue and creates the actual delay.

`Statically Scheduled`: A processor that relaies on compiler insertion of NOPs for correctness.

`Dynamically Scheduled`: A processor that provide interlocks to ensure correctness.

`Superscalar`: A processor that can issue distinct operations to multiple distinct functional units in a single cycle.

`Software pipelining`: attempt to decrease the total running time of a loop.

#### Register Allocation
- Graph Coloring: `interference graph`, `chromatic number`

#### 作者常用的4个非常用词
- albeit: Though
- merit: Deserve or be worthy of
- myraid: countless
- mitigate: Make (something bad) less severe, serious, or painful.
- dichotomy: a division or contrast between two things that are or are represented as being opposed or entirely different. 二分法
