## history
- ISO C++98
- ISO C++03
- ISO C++11
- ISO C++14

osx上使用clang/clang++

Each C++ expression (an operator with its operands, a literal, a variable name, etc.) is characterized by two independent properties: a type and a value category. Each expression has some non-reference type, and each expression belongs to exactly one of the three primary value categories: `prvalue`, `xvalue`, `lvalue`
`noexcept` = `noexcept(true)`: means no exception

Declare destructors virtual in polymorphic base classes.
destructors are called automatically in the reverse order of construction.
cv (`const` and `volatile`) type qualifiers

#### Return Value or Return Reference
C++ functions can return by value, by reference (but don't return a local variable by reference), or by pointer (again, don't return a local by pointer).
When returning by value, the compiler can often do optimizations that make it equally as fast as returning by reference, without the problem of dangling references. These optimizations are commonly called "`Return Value Optimization (RVO)`" and/or "`Named Return Value Optimization (NRVO)`".

#### RAII
In `Resource acquisition is initialization(RAII)`, holding a resource is a class invariant, and is tied to object lifetime: resource allocation (or acquisition) is done during object creation (specifically initialization), by the constructor, while resource deallocation (release) is done during object destruction (specifically finalization), by the destructor.
Other names for this idiom include Constructor Acquires, Destructor Releases (CADRe) [7] and one particular style of use is called Scope-based Resource Management (SBRM).

### C++11
#### lvalue, rvalue
An `lvalue` (locator value) represents an object that occupies some identifiable location in memory
`reference` are called "lvalue references"
Constant lvalue references can be assigned rvalues

An lvalue (3.10) of a non-function, non-array type T can be converted to an rvalue. [...] If T is a non-class type, the type of the rvalue is the cv-unqualified version of T. Otherwise, the type of the rvalue is T.
The cv-qualified or cv-unqualified versions of a type are distinct types; however, they shall have the same representation and alignment requirements (3.9)
The `&&` syntax is the new `rvalue reference`. It does exactly what it sounds it does - gives us a reference to an rvalue, which is going to be destroyed after the call.
- Implementing move semantics
- Perfect forwarding
Things that are declared as `rvalue reference` can be `lvalues` or `rvalues`. The distinguishing criterion is: if it has a name, then it is an lvalue. Otherwise, it is an rvalue.
- And here's the rationale behind the design: Allowing move sematics to be applied tacitly to something that has a name, as in
-   X anotherX = x;
-   // x is still in scope!
- would be dangerously confusing and error-prone because the thing from which we just moved, that is, the thing that we just pilfered, is still accessible on subsequent lines of code.
Thus, `std::move` "turns its argument into an rvalue even if it isn't," and it achieves that by "hiding the name."

reference collapsing rules1:
- A& & becomes A&
- A& && becomes A&
- A&& & becomes A&
- A&& && becomes A&&
special template argument deduction rule for function templates that `take an argument by rvalue reference` to a template argument:
- When foo is called on an `lvalue` of type A, then T resolves to `A&`
- When foo is called on an `rvalue` of type A, then T resolves to `A`

Also, you have probably noticed by now that instead of` std::move(x);` you could just as well write `static_cast<X&&>(x);`

A `move constructor` of class T is a non-template constructor whose first parameter is T&&, const T&&, volatile T&&, or const volatile T&&, and either there are no other parameters, or the rest of the parameters all have default values.

#### nullptr
`nullptr` is always a pointer type.  0 (aka. C's NULL bridged over into C++) could cause ambiguity in overloaded function resolution, among other things:
- f(int);
- f(foo *);

#### const qualifier
`const int *ptr`: pointer to const data
`int * const ptr:` const pointer
- 这种易混淆性可通过"const is read from right to left"来消除，这样就不存在上面的混淆之处了
- 也因为此，最好写成`int const *ptr`, 而不是`const int *ptr`

#### Converting Constructor
A constructor that is not declared with the specifier explicit and `which can be called with a single parameter (until C++11)` is called a converting constructor.

### STL
`std::move` is used to indicate that an object t may be "moved from", i.e. allowing the efficient transfer of resources from t to another object.
`std::integral_constant` wraps a static constant of specified type.
`std::thread::detach` Separates the thread of execution from the thread object, allowing execution to continue independently. Any allocated resources will be freed once the thread exits.
- Threads begin execution immediately upon construction of the associated thread object
`std::unique_lock` is a general-purpose mutex ownership wrapper. RAII用法
`std::atomic` is neither copyable nor movable.
`std::condition_variable`.wait_until 可按Predicate等待
`std::remove` does not remove the actual objects, rather, pushes them to the end of the container. Actual deletion and deallocation of memory is done via `erase`.
The `erase–remove` idiom is a common C++ technique to eliminate elements which is faster than `erase` itself.
`std::memory_order` specifies how regular, non-atomic memory accesses are to be ordered around an atomic operation. The default behavior of all atomic operations in the library provides for `sequentially consistent` ordering (see discussion below).
- `memory_order_relaxed`: Relaxed operation: there are no synchronization or ordering constraints imposed on other reads or writes, only this operation's atomicity is guaranteed.
- `memory_order_consume`: A `load operation` with this memory order performs a `consume operation` on the affected memory location: no reads or writes in the current thread dependent on the value currently loaded can be reordered before this load. Writes to data-dependent variables in other threads that release the same atomic variable are visible in the current thread. On most platforms, this affects compiler optimizations only.
- `memory_order_acquire`: A `load operation` with this memory order performs the `acquire operation` on the affected memory location: no reads or writes in the current thread can be reordered before this load. All writes in other threads that release the `same atomic variable` are visible in the current thread
- `memory_order_release`: A `store operation` with this memory order performs the `release operation`: no reads or writes in the current thread can be reordered after this store. All writes in the current thread are visible in other threads that acquire the `same atomic variable` and writes that carry a dependency into the atomic variable become visible in other threads that consume the `same atomic`
- `memory_order_acq_rel`: A read-modify-write operation with this memory order is both an acquire operation and a release operation. No memory reads or writes in the current thread can be reordered before or after this store. All writes in other threads that release the same atomic variable are visible before the modification and the modification is visible in other threads that acquire the same atomic variable.
- `memory_order_seq_cst`: Any operation with this memory order is both an acquire operation and a release operation, plus a single total order exists in which `all threads` observe all modifications in the same order
### traits
Traits classes do not determine the type of the object. Instead, they provide additional information about a type, typically by defining typedefs or constants inside the trait.

### Memory Model
#### Sequential consistency
-  the result of any execution is the same as if the operations of all the processors were executed in some sequential order, 及前一次操作的影响对后面的操作立即可见
- the operations of each individual processor appear in this sequence in the order specified by its program，即单个线程内的执行顺序为程序顺序
##### 其他定义
Sequential consistency memory model specifies that the system must appear to execute all threads’ loads and stores to `all memory locations` in a `total order` that respects the program order of each thread. Each load gets the value of the most recent store in that total order.
#### (Cache) Coherence
A definition of coherence that is analogous to the definition of Sequential Consistency is that a coherent system must appear to execute all threads’ loads and stores to a `single memory location` in a total order that respects the program order of each thread.
#### difference between coherence and consistency
This definition highlights an important distinction between `coherence` and `consistency`: coherence is specified on a per-memory location basis, whereas consistency is specified with respect to all memory locations.
#### memory ordering
`Memory ordering` describes the order of accesses to computer memory by a CPU.
- memory ordering generated by the compiler during compile time
- memory ordering generated by a CPU during runtime.
#### Modification order
All modifications to any particular atomic variable occur in a `total order` that is specific to this one atomic variable.
The following four requirements are guaranteed for all atomic operations:
- `Write-write coherence`
- `Read-read coherence`
- `Read-write coherence`
- `Write-read coherence`
