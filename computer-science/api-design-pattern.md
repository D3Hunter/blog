### Fluent Interface
Intent: A fluent interface provides an easy-readable, flowing interface, that often mimics a `domain specific language`. Using this pattern results in code that can be read nearly as human language.

Implementation: A fluent interface can be implemented using any of
- Method Chaining - calling a method returns some object on which further methods can be called.
- Static Factory Methods and Imports
- Named parameters - can be simulated in Java using static factory methods.

Applicability: Use the Fluent Interface pattern when
- you provide an API that would benefit from a DSL-like usage
- you have objects that are difficult to configure or use

do something externally then use `DSL`, internally then use `fluent interface`.

