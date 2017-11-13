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

### Boost
`boost::bind` is a generalization of the standard functions std::bind1st and std::bind2nd. It supports arbitrary function objects, functions, function pointers, and member function pointers, and is able to bind any argument to a specific value or route input arguments into arbitrary positions. bind does not place any requirements on the function object; in particular, it does not need the `result_type`, `first_argument_type` and `second_argument_type` standard typedefs.
signal/slot

### STL
`std::move` is used to indicate that an object t may be "moved from", i.e. allowing the efficient transfer of resources from t to another object.
`std::integral_constant` wraps a static constant of specified type.
`std::thread::detach` Separates the thread of execution from the thread object, allowing execution to continue independently. Any allocated resources will be freed once the thread exits.
`std::unique_lock` is a general-purpose mutex ownership wrapper. RAII用法
`std::atomic` is neither copyable nor movable.
`std::condition_variable`.wait_until 可按Predicate等待
`std::remove` does not remove the actual objects, rather, pushes them to the end of the container. Actual deletion and deallocation of memory is done via `erase`.
The `erase–remove` idiom is a common C++ technique to eliminate elements which is faster than `erase` itself.
### traits
Traits classes do not determine the type of the object. Instead, they provide additional information about a type, typically by defining typedefs or constants inside the trait.

### Memory Model
#### Sequential consistency
-  the result of any execution is the same as if the operations of all the processors were executed in some sequential order, 及前一次操作的影响对后面的操作立即可见
- the operations of each individual processor appear in this sequence in the order specified by its program，即单个线程内的执行顺序为程序顺序
#### memory ordering
`Memory ordering` describes the order of accesses to computer memory by a CPU.
- memory ordering generated by the compiler during compile time
- memory ordering generated by a CPU during runtime.
