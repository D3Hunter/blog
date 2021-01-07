## predication
In computer science, `predication` is an architectural feature that provides an alternative to conditional transfer of control, implemented by machine instructions such as `conditional branch`, `conditional call`, `conditional return`, and `branch tables`. Predication works by executing instructions from both paths of the branch and only permitting those instructions from the taken path to modify architectural state. The instructions from the taken path are permitted to modify architectural state because they have been associated (predicated) with a predicate, a Boolean value used by the instruction to control whether the instruction is allowed to modify the architectural state or not.

## some concepts
- In computing, a `meta-circular evaluator` (MCE) or `meta-circular interpreter` (MCI) is an interpreter which defines each feature of the interpreted language using a similar facility of the interpreter's host language. A `self-interpreter` is a `meta-circular interpreter` where the interpreted language is nearly identical to the host language; the two terms are often used synonymously.
- `Programming by Coincidence` means that you don't know what you are doing. Your code relies on luck and accidental success.
- `SOA`: service-oriented architecture
- `Distributed computing` is a field of computer science that studies distributed systems.
- `distributed system` is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another.
- `Dark launching`(灰度发布) is a process where software is gradually or stealthily released to consumers in order to get user feedback and test performance.
- `race condition` arises in software when a computer program, to operate properly, depends on the sequence or timing of the program's processes or threads.
- The main difference between `SOA` and `microservices`: `Scope`. The main distinction between the two approaches comes down to scope. To put it simply, `service-oriented architecture (SOA)` has an `enterprise scope`, while the microservices architecture has an `application scope`.
- `Scalability`（伸缩性） is the ability of the system to accommodate larger loads just by adding resources either making hardware stronger (`scale up` or `Scaling Vertically`) or adding additional nodes (`scale out`).
- `Elasticity`（弹性） is the ability to fit the resources needed to cope with loads dynamically usually in relation to scale out. 可增可减
- `Anemic domain model`(贫血模型): Anemic domain model is the use of a software domain model where the domain objects contain little or no business logic (validations, calculations, business rules etc.).
-ssboilerplate code` or just `boilerplate` are sections of code that are repeated in multiple places with little to no variation.....the programmer must write a lot of code(`boilerplate`) to accomplish only minor functionality. 比如`OOP`中的`getter/setter`，`C/C++ header`中的`#ifndef XXX_H`, Most JDBC code is mired in `resource acquisition`, `connection management`, `exception handling`, and `general error checking` that is wholly unrelated to what the code is meant to achieve.
- `Inversion of Control` is a key part of what makes a `framework` different to a `library`.
    - `dependency injection` is an specific styles of `inversion of control`.
- `Simulation`, on the other hand, involves modeling the underlying state of the target. The end result of a good simulation is that the simulation model will emulate the target which it is simulating.
- `Emulation` is the process of mimicking the outwardly observable behavior to match an existing target. The internal state of the emulation mechanism does not have to accurately reflect the internal state of the target which it is emulating.

## Formal Verification
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

## Program Equivalence
The general problem of program equivalence checking is undecidable. Applications include program equivalence:
- translation validation: source-to-source, or unoptimized-optimized code
- program synthesis: determining if the optimized program proposed by the synthesis algorithm is equivalent to the original program specification

- `soundness` is critical, i.e., if the equivalence checker determines the programs to be equivalent, then the programs are guaranteed to have equivalent runtime behaviour.(`robustness`)
- `completeness` may not always be achievable, i.e., it is possible that the equivalence checker is unable to prove the programs equivalent, even if they are actually equivalent.

In computer science, `program synthesis` is the task to construct a program that `provably` satisfies a given `high-level formal specification`.

## cache coherence
`cache coherence` is the uniformity of shared resource data that ends up stored in multiple local caches.
- Write Propagation
    - Changes to the data in any cache must be propagated to other copies (of that cache line) in the peer caches.
- Transaction Serialization
    - Reads/Writes to a single memory location must be seen by all processors in the same order.

The alternative definition of a coherent system is via the definition of `sequential consistency memory model`: "the cache coherent system must appear to execute all threads’ loads and stores to a single memory location in a total order that respects the program order of each thread".[3] Thus, the only difference between the cache coherent system and sequentially consistent system is in the number of address locations the definition talks about (`single memory location for a cache coherent system, and all memory locations for a sequentially consistent system`).

- `Write through` is a storage method in which data is written into the cache and the corresponding main memory location at the same time.
- `Write back` is a storage method in which data is written into the cache every time a change occurs, but is written into the corresponding location in main memory only at specified intervals or under certain conditions.

