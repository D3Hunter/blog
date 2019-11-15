We are interested in understanding whether such constructions exist, and how they work. They are not intended to be a practical model for computation. Instead, we prefer easy-to-understand but inefficient constructions over complicated but efficient ones. In particular, some of our constructions use timestamps (counter values) to distinguish older values from newer values.

Concurrent Correctness
- A `safety` property states that some “bad thing” never happens.
    - For example, a traffic light never displays green in all directions, even if the power fails.
- A `liveness` property states that a particular good thing will happen.
    - For example, a red traffic light will eventually turn green.

Amdahl’s Law: S = 1 / (1 − p + p / n)
    - p is the fraction of the job that can be executed in parallel.
    - n concurrent processors

In general, however, for a given problem and a ten-processor machine, `Amdahl’s Law` says that even if we manage to parallelize 90% of the solution, but not the remaining 10%, then we end up with a `five-fold` speedup, but not a `ten-fold` speedup. In other words, the remaining `10%` that we did not parallelize cut our utilization of the machine in half.

It seems worthwhile to invest an effort to derive as much parallelism from the remaining `10%` as possible, even if it is difficult. Typically, it is hard because these additional parallel parts involve substantial `communication` and `coordination`.

implications of `Amdahl’s Law`: it is important to minimize the granularity of sequential code

It is particularly important to learn how to reason about subtle `liveness` issues such as `starvation` and `deadlock`.

the properties that a good Lock algorithm should satisfy
- Mutual Exclusion(Safety property or correctness)
    - Critical sections of different threads do not overlap.
- Freedom from Deadlock(Liveness property or progress)
    - If some thread attempts to acquire the lock, then some thread will succeed in acquiring the lock.
    - Note that a program can still deadlock even if each of the locks it uses satisfies the deadlock freedom property.
- Freedom from Starvation
    - Every thread that attempts to acquire the lock eventually succeeds.

about consistency
- `Quiescent consistency` is appropriate for applications that require high performance at the cost of placing relatively weak constraints on object behavior.
- `Sequential consistency` is a stronger condition, often useful for describing low-level systems such as hardware memory interfaces.
- `Linearizability`, even stronger, is useful for describing higherlevel systems composed from `linearizable` components.

#### consistency models
单线程内描述和推理object的行为是很容易的，使用precondition和postcondition，但在并行环境下因为有overlapping的存在则不容易这么描述和推理。所以需要一个一致性模型来完成这个功能

The `consistency model` of a shared-memory multiprocessor provides a formal specification of how the memory system will appear to the programmer, eliminating the gap between the behavior expected by the programmer and the actual behavior supported by a system.

Effectively, the `consistency model` places restrictions on the values that can be returned by a read in a shared-memory program execution.

因为sequencial specification很容易理解，一般一致性模型都会转化成等同的sequencial specification来描述。即：Method calls should appear to happen in a one-at-a-time, sequential order.

一致性模型是一个系统（软件、硬件）的属性. 一致性模型都是在单个对象上定义的，受composability属性影响，在多个对象的情况下对应模型不一定成立，比如sequential consistency

以下模型都满足：Method calls should appear to happen in a one-at-a-time, sequential order.
- strict consistency
    - a write to a variable by any processor needs to be seen instantaneously by all processors.
    - 相当于每个method call on a object是一个点，而不是interval，整个系统等同于实际不存在并发
- sequential consistency
    - Method calls should appear to happen in a one-at-a-time, sequential order.
    - Method calls should appear to take effect in program order.（quiescent consistency不具有的）
    - 不保证real-time order，这导致不具有composibility属性，因为compose后的sequential order可能是not legal
        - A write to a variable does not have to be seen instantaneously, however, writes to variables by different processors have to be seen in the same order by all processors.
    - Sequential consistency is a good way to describe standalone systems, such as hardware memories, where composition is not an issue.
- quiescent consistency
    - Method calls should appear to happen in a one-at-a-time, sequential order.
    - the operations of any processors separated by a period of quiescence should appear to take effect in their real-time order.（sequential consistency不具有的）
    - 但是对于由quiescence分开的每个operation group内部，其顺序是不保证的，这是quiescent consistency比Linearizability弱的地方
- Linearizability(linearizable consistency)
    - Method calls should appear to happen in a one-at-a-time, sequential order.
    - Each method call should appear to 'take effect' instantaneously at some moment(`linearization point`) between its invocation and response.
        - 着隐含着：Method calls should appear to take effect in program order. 因此Linearizability一定是sequential consistency
    - local property: a system is linearizable iff each individual object is linearizable. It gives us composability.
    - non-blocking property: one method is never forced to wait to synchronize with another.
    - This property of occurring instantaneously, or indivisibly, leads to the use of the term `atomic` as an alternative to the longer "`linearizable`"
    - Linearizability, by contrast, is a good way to describe components of large systems, where components must be implemented and verified independently.
- serializability
    - Serializability of a schedule means equivalence to a serial schedule with the same transactions.
- strict serializability
- transactional memory semantics.


any algorithm using `atomic registers` can be implemented on an architecture that supports only `safe registers`.

A register providing compareAndSet() and get() methods has an infinite consensus number.

machines that provide primitive operations like `compareAndSet()` are asynchronous computation’s equivalents of the Turing Machines of sequential computation: any concurrent object that can be implemented, can be implemented in a wait-free manner on such machines.(Some architectures provide a pair of operations similar to get()/compareAndSet() called `loadlinked`/`store-conditional`. In general, the `load-linked` method marks a location as loaded, and the `store-conditional` method fails if another thread modified that location since it was loaded. )

A class is universal in a system of n threads if, and only if it has a consensus number greater than or equal to n.

Like classical computability theory, understanding the universal construction and its implications will allow us to avoid the na¨ıve mistake of trying to solve unsolvable problems.

#### Counting，Sorting，and distributed coordination
useful patterns for distributed coordination: combining, counting, diffraction, and sampling. Some are deterministic, while others use randomization.

two classes of sorting algorithms:
- sorting networks, which typically work well for small in-memory data sets
- sample sorting algorithms, which work well for large data sets in external memory.

#### Chapter 16
Finally, a computation’s `parallelism` is the maximum possible `speedup`.

### 作者常用词
- succinct: briefly and clearly expressed.
- culminate: reach a climax or point of highest development.
- obstruction: the action of obstructing or the state of being obstructed.
- obstruct: block (an opening, path, road, etc.); be or get in the way of.
- innocuous: not harmful or offensive.
- valence: the combining power of an element, especially as measured by the number of hydrogen atoms it can displace or combine with.
- seminal: (of a work, event, moment, or figure) strongly influencing later developments.
- splice: a union of two ropes, pieces of timber, or similar materials spliced together at the ends.
- reconcile: restore friendly relations between.
- rendezvous: a meeting at an agreed time and place, typically between two people.
- to no avail: in vain, for nothing
- Sporting, when used in a way that has nothing to do with sport, means fair and respectful. like `sporting offer`
- omission: someone or something that has been left out or excluded.
- shepherd: a person who tends and rears sheep.
- anecdotal: not necessarily true or reliable, because based on personal accounts rather than facts or research.
- vicinity: The area near or surrounding a particular place.
- ostensible: Stated or appearing to be true, but not necessarily so.
- percolate; (of a liquid or gas) filter gradually through a porous surface or substance.
- porous: (of a rock or other material) having minute spaces or holes through which liquid or air may pass.
- catastrophic: involving or causing sudden great damage or suffering. extremely unfortunate or unsuccessful.

