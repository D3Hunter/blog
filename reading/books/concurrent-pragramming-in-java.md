## Concurrent pragramming in java - design principles and pattern
### Chapter 1 - Concurrent Object-Oriented Programming
One can take two complementary views of any OO system, object-centric and activity-centric: `System = Objects + Activities`. These two views give rise to two complementary sets of `correctness` concerns:
- `Safety`. Nothing bad ever happens to an object.
- `Liveness`. Something eventually happens within an activity.

Safety and liveness issues may be further extended to encompass two categories of `quality` concerns:
- `Reusability`. The utility of objects and classes across multiple contexts.
- `Performance`. The extent to which activities execute soon and quickly.

#### Safety
It sometimes takes hard work to nail down exactly what "legal" and "meaningful" mean in a particular class. One path is first to establish conceptual-level `invariants`. An object is `consistent` if all fields obey their `invariants`.

Safe programming techniques rely on clear understanding of required `properties` and `constraints` surrounding object representations.

Broad categories of fields and constraints include the following:
- Direct value representations.
- Cached value representations.
- Logical state representations.
- Execution state variables.
- History variables.
- Version tracking variables.
- References to acquaintances
- References to representation objects.

#### Performance
Meaningful performance requirements are stated in terms of measurable qualities, including the following metrics. Goals may be expressed for central tendencies (e.g., mean, median) of measurements, as well as their variability (e.g., range, standard deviation).
- `Throughput`. The number of operations performed per unit time.
- `Latency`. The time elapsed between issuing a message and servicing it.
- `Capacity`. The number of simultaneous activities that can be supported for a given target minimum throughput or maximum latency.
- `Efficiency`. Throughput divided by the amount of computational resources (for example CPUs, memory, and IO devices) needed to obtain this throughput.
- `Scalability`. The rate at which latency or throughput improves when resources (again, usually CPUs, memory, or devices) are added to a system.
- `Degradation`. The rate at which latency or throughput worsens as more clients, activities, or operations are added without adding resources.

Most multithreaded designs implicitly accept a small trade-off of poorer computational efficiency to obtain better latency and scalability.

#### Reusability
It is usually more productive to proceed with the understanding that some very useful and efficient components are not, and need not be, absolutely safe, and that useful services supported by some components are not absolutely live. Instead, they operate correctly only within certain `restricted usage contexts`. Therefore, establishing, documenting, advertising, and exploiting these contexts become central issues in concurrent software design.

There are two general approaches (and a range of intermediate choices) for dealing with context dependence:
1. Minimize uncertainty by closing off parts of systems
2. Establish policies and protocols that enable components to become or remain open. Many practical design efforts involve some of each.

`Unbounded openness` is usually as unattainable and undesirable as `complete closedness`: If everything can change, then you cannot program anything. But most systems require at least some of this flexibility.

While inducing greater closedness allows you to optimize for performance, inducing greater openness allows you to optimize for future change.

Across these audiences, the first goal is to eliminate the need for extensive documentation by minimizing the unexpected, and thus reducing conceptual complexity via:
- `Standardization`. Using common policies, protocols, and interfaces.
- `Clarity`. Using the simplest, most self-evident code expressions.
- `Auxiliary code`. Supplying code that demonstrates intended usages.

### Chapter 2 - Exclusion
`Exclusion` techniques preserve object invariants and avoid effects that would result from acting upon even momentarily inconsistent state representations. Programming techniques and design patterns achieve exclusion by preventing multiple threads from concurrently modifying or acting upon object representations. All approaches rely on one or more of three basic strategies:
- `Eliminating` the need for some or all exclusion control by ensuring that methods never modify an object's representation, so that the object cannot enter inconsistent states. i.e. `immutability`
- `Dynamically` ensuring that only one thread at a time can access object state, by protecting objects with locks and related constructs. i.e. `synchronization`
- `Structurally` ensuring that only one thread (or only one thread at a time) can ever use a given object, by hiding or restricting access to it. i.e. `confinement`

#### Java Memory Model
Somewhat more precisely, `as-if-serial` (also known as `program order`) semantics can be defined as any execution traversal of the graph formed by ordering only those operations that have value or control dependencies with respect to each other under a language's base expression and statement semantics.

#### Confinement
- Confinement across methods
    - `hand-off` protocol that ensures that, at any given time, at most one actively executing method can access an object. such as tail-call hand-offs
    - Many `hand-off `sequences are structured as `sessions` in which some public entry method constructs objects that will be confined to a sequence of operations comprising a service.
    - Alternative protocols
        - caller copies
        - receiver copies
        - using scalar variables
        - Trust
- Confinement within threads
    - thread per session
    - thread-specific fields: subclassing `Thread` class
    - ThreadLocal
- Confinement within objects
    - Adapters
    - subclassing
- Confinement within groups
    - In some contexts and senses, protocols involving exclusive resources have been termed `tokens`, `batons`, `linear objects`, `capabilities`, and sometimes just `resources`.

#### Structuring and refactoring classes
- splitting synchronization to match functionality
- exporting read-only operations via adapters
- isolating state representations to reduce access costs or improve potential parallelism, and
- grouping objects to use common locks so as to mirror layered designs

- Reducing Synchronization
    - `open calls`: Messages sent without holding locks are also known as open calls.

`Optimistic Locking` is a strategy where you read a record, take note of a version number (other methods to do this involve dates, timestamps or checksums/hashes) and check that the version hasn't changed before you write the record back.

### State dependency
State-dependent concurrency control imposes additional concerns surrounding `preconditions` and `postconditions`.

There are two general approaches to the design and implementation of any state-dependent action, that stem from liveness-first versus safety-first design perspectives:
- `Optimistic` try-and-see methods can always be tried when invoked, but do not always succeed, and thus may have to deal with failure.
- `Conservative` check-and-act methods refuse to proceed unless preconditions hold. When preconditions do hold, the actions always succeed.

#### Deal with failure
For exceptions, there are six general responses to such failed actions:
- abrupt termination
- continuation (ignoring failures)
- rollback
    - Provisional action. Before attempting updates, construct a new representation that will, upon success, be swapped in as the current state.
    - Checkpointing. Before attempting updates, record the current state of the object in a history variable.
- rollforward(recovery)
    - push ahead as conservatively as possible to re-establish some guaranteed legal, consistent state that may be different from the one holding upon entry to the method.
- retry
- and delegation to handlers.

Cancellation
- Interruption
- IO and resource revocation
- Asynchronous termination
#### Guarded methods
- Balking. Throwing an exception if the precondition fails.
- Guarded suspension. Suspending the current method invocation (and its associated thread) until the precondition becomes true.
- Time-outs. The range of cases falling between balking and suspension

Entities possessing both `locks` and `wait sets` are generally called `monitors`

`wait`/`notify`

`Semaphores` are useful tools whenever you can conceptualize a design in terms of `permits`. Such as `bounded counters`, `bounded buffers`.

A `latching` variable or condition is one that eventually receives a value from which it never again changes. `Latches` help structure solutions to initialization problems where you do not want a set of activities to proceed until all objects and threads have been completely constructed. Extended forms of `latches` include `countdowns`, which allow acquire to proceed when a fixed number of releases occur, not just one.
- Completion indicators.
- Timing thresholds.
- Event indications.
- Error indications.

#### Joint actions
`joint actions` are atomic guarded methods that involve `conditions` and `actions` among multiple, otherwise independent participant objects.

### Creating Threads
#### Oneway messages
message formats
- command strings
- event/request objects
- runnable objects

- thread-per-message
- worker threads
- Polling and Event-Driven IO

#### Composing Oneway Messages
A `flow network` is a collection of objects that all pass oneway messages transferring information and/or objects to each other along paths from `sources` to `sinks`. Flow patterns may occur in any kind of system or subsystem supporting one or more series of connected steps or `stages`, in which each stage plays the role of a producer and/or consumer.
- Control systems.
- Assembly systems.
- Dataflow systems.
- Workflow systems.
- Event systems.

The development of flow networks entails two main sets of concerns:
- design of the `data` being passed around
- design of the `stages` that do the passing.

`Stages` in well-behaved flow networks all obey sets of constraints that are reminiscent of those seen in electrical circuit design. Here is one conservative set of composition rules that generate a small number of basic kinds of stages:
- Directionality. Flow maintains a single directionality, from sources to sinks.
- Interoperability. Methods and message formats are standardized across components
- Connectivity. Stages maintain fixed connectivity: consumers may receive messages only from known producers, and vice versa.

- `Sources` have no predecessors.
- `Sinks` have no successors.
- `Linear` stages have at most one predecessor and one successor.
- `Routers` send a message to one of their successors.
- `Multicasters` send messages to all their successors.
- `Collectors` accept messages from one of their predecessors at a time.
- `Combiners` require messages from all their predecessors.

#### Services in Threads
Many tasks compute results or provide services that are not immediately used by their clients, but are eventually required by them. In these situations, unlike those involving oneway messages, a client's actions at some point become dependent on completion of the task.

- Completion Callbacks: sometimes structurally identical to `Observer` designs
- Joining Threads
- Futures: package the operations underlying join-based constructions in a more convenient and structured fashion
- Scheduling Services

#### Parallel Decomposition
- Fork/Join
- Computation Trees
- Barriers

#### Active Objects
In the `task-based` frameworks illustrated throughout most of this chapter, `threads` are used to propel conceptually `active messages` sent among conceptually `passive objects`. However, it can be productive to approach some design problems from the opposite perspective — `active objects` sending each other `passive messages`

The `active object` design pattern decouples `method execution` from `method invocation`. The goal is to introduce concurrency, by using `asynchronous method invocation` and a `scheduler` for handling requests

Communicating Sequential Processes (CSP)

### 常用词
- contemplation: the action of looking thoughtfully at something for a long time.
- obligation: an act or course of action to which a person is morally or legally bound; a duty or commitment.
- confine: keep or restrict someone or something within certain limits of (space, scope, quantity, or time).
- detract: reduce or take away the worth or value of.
- apparatus: the technical equipment or machinery needed for a particular activity or purpose.
- tentative: not certain or fixed; provisional.
- resilient: (of a substance or object) able to recoil or spring back into shape after bending, stretching, or being compressed.
- reminiscent: tending to remind one of something.
- balking: hesitate or be unwilling to accept an idea or undertaking.
- provision: the action of providing or supplying something for use. A condition or requirement in a legal document.
- anomaly: something that deviates from what is standard, normal, or expected.
- `All but impossible`: means it's possible, but only barely.
- prudent: acting with or showing care and thought for the future.
- latch: a metal bar with a catch and lever used for fastening a door or gate.
- rendezvous: meet at an agreed time and place.
- remedies: a medicine or treatment for a disease or injury.
- impede: delay or prevent (someone or something) by obstructing them; hinder.
- veto: A constitutional right to reject a decision or proposal made by a lawmaking body.
- culmination: the highest or climactic point of something, especially as attained after a long time.
- propel: drive, push, or cause to move in a particular direction, typically forward.

