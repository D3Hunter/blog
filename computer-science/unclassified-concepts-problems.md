### predication
In computer science, `predication` is an architectural feature that provides an alternative to conditional transfer of control, implemented by machine instructions such as `conditional branch`, `conditional call`, `conditional return`, and `branch tables`. Predication works by executing instructions from both paths of the branch and only permitting those instructions from the taken path to modify architectural state. The instructions from the taken path are permitted to modify architectural state because they have been associated (predicated) with a predicate, a Boolean value used by the instruction to control whether the instruction is allowed to modify the architectural state or not.

### some concepts
- In computing, a `meta-circular evaluator` (MCE) or `meta-circular interpreter` (MCI) is an interpreter which defines each feature of the interpreted language using a similar facility of the interpreter's host language. A `self-interpreter` is a `meta-circular interpreter` where the interpreted language is nearly identical to the host language; the two terms are often used synonymously.

### Formal Verification
In the context of hardware and software systems, `formal verification` is the act of proving or disproving the correctness of intended algorithms underlying a system with respect to a certain `formal specification` or `property`, using `formal methods of mathematics`.

`Formal verification` can be helpful in proving the correctness of systems such as: `cryptographic protocols`, `combinational circuits`, `digital circuits` with internal memory, and software expressed as `source code`.

The verification of these systems is done by providing a `formal proof` on an `abstract mathematical model` of the system, the correspondence between the mathematical model and the nature of the system being otherwise known by construction. Examples of mathematical objects often used to model systems are:
- finite state machines
- labelled transition systems
- Petri nets
- vector addition systems
- timed automata
- hybrid automata
- process algebra
- formal semantics of programming languages such as:
    - operational semantics
    - denotational semantics
    - axiomatic semantics
    - Hoare logic.

### Program Equivalence
The general problem of program equivalence checking is undecidable. Applications include program equivalence:
- translation validation: source-to-source, or unoptimized-optimized code
- program synthesis: determining if the optimized program proposed by the synthesis algorithm is equivalent to the original program specification

- `soundness` is critical, i.e., if the equivalence checker determines the programs to be equivalent, then the programs are guaranteed to have equivalent runtime behaviour.(`robustness`)
- `completeness` may not always be achievable, i.e., it is possible that the equivalence checker is unable to prove the programs equivalent, even if they are actually equivalent.

In computer science, `program synthesis` is the task to construct a program that `provably` satisfies a given `high-level formal specification`.

