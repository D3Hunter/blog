### Type Systems
A type system for a typical modern language has four major components:
- a set of base types, or built-in types;
- rules for constructing new types from the existing types;
- a method for determining if two types are equivalent or compatible;
    - name equivalence
    - structural equivalence
- and rules for inferring the type of each source-language expression.

Many languages also include rules for the implicit conversion of values from one type to another based on context.

#### CLASSIFYING TYPE SYSTEMS
- Typed or Untyped
    - strongly typed, untyped, and weakly typed
- Checked versus Unchecked Implementations
    - strongly checked, unchecked, weakly checked
- Compile Time versus Runtime Activity
    - statically typed and statically checked
    - dynamically typed and dynamically checked
    - strongly typed, statically typed language with dynamic checking, such as Java
    - Other combinations

#### Inference Rules
In general, type inference rules specify, for each operator, the mapping between the operand types and the result type.

The relationship between operand types and result types is often specified as a recursive function on the type of the expression tree. The function computes the result type of an operation as a function of the types of its operands. The functions might be specified in tabular form

many programming languages include a “declare before use” rule. With mandatory declarations, each variable has a well defined type.

ways to assign types to constants
- a constant’s form implies a specific type
    - for example, `2` is an integer and `2.0` is a floating-point number
- the compiler infers a constant’s type from its usage—for example
    - `sin(2)` implies that `2` is a floating-point number
    - `x ⟵ 2`, for integer `x`, implies that `2` is an integer.

With declared types for variables, implied types for constants, and a complete set of type-inference rules, the compiler can assign types to any expression over variables and constants. Although function calls complicate the picture

### THE ATTRIBUTE-GRAMMAR FRAMEWORK
One formalism that has been proposed for performing context-sensitive analysis is the `attribute grammar`, or `attributed context-free grammar`. An `attribute grammar` consists of a context-free grammar augmented by a set of rules that specify computations. Each `rule` defines one `value`, or `attribute`, in terms of the values of other attributes. The `rule` associates the attribute with a specific `grammar symbol`; each instance of the `grammar symbol` that occurs in a `parse tree` has a corresponding instance of the `attribute`. The rules are functional; they imply no specific evaluation order and they define each attribute’s value uniquely.

We distinguish between attributes based on the direction of value flow.
- `Synthesized attributes` are defined by bottom-up information flow; a rule that defines an attribute for attribute can draw values from the node itself, its descendants in the parse tree, and constants.
- `Inherited attributes` are defined by top-down and lateral information flow; a rule that defines an attribute for the production’s righthand side creates an inherited attribute.

attribute evaluation methods:
- `Dynamic Methods` These techniques use the structure of a particular attributed parse tree to determine the evaluation order.
    - A related scheme would build the attribute dependence graph, topologically sort it, and use the topological order to evaluate the attributes.
- `Oblivious Methods` In these methods, the order of evaluation is independent of both the attribute grammar and the particular attributed parse tree.
    - Examples of this evaluation style include repeated left-to-right passes (until all attributes have values), repeated right-to-left passes, and alternating left-to-right and right-to-left passes.
- `Rule-Based Methods` Rule-based methods rely on a static analysis of the attribute grammar to construct an evaluation order.

Circularity
- `Avoidance` The compiler writer can restrict the attribute grammar to a class that cannot give rise to circular dependence graphs.
- `Evaluation` The compiler writer can use an evaluation method that assigns a value to every attribute, even those involved in cycles. The evaluator might iterate over the cycle and assign appropriate or default values.

#### Inferring Expression Types
type conversions
- To represent type conversions in the attributed tree, we could add an `attribute` to each node that holds its `converted type`, along with rules to set the attributes appropriately.
    - localizes all of the information needed for a conversion to a single parse-tree node.
- Alternatively, we could rely on the process that generates code from the tree to compare the two types—parent and child—during the traversal and insert the necessary conversion.

#### Problems with the Attribute-Grammar Approach
The attribute-grammar approach has never achieved widespread popularity for a number of mundane reasons.
- Handling Nonlocal Information
- Storage Management: The use of copy rules to move information around the parse tree can multiply the number of attribute instances that evaluation creates.
    - The possible uses of an attribute in later phases of the compiler have the effect of adding dependences from that attribute to uses not specified in the attribute grammar. This bends the functional paradigm and removes one of its strengths: the ability to automatically manage attribute storage.
- Instantiating the Parse Tree
- Locating the Answers

One way to address all of these problems is to add a central repository for attributes. In this scenario, an attribute rule can record information directly into a global table, where other rules can read the information.

### AD HOC SYNTAX-DIRECTED TRANSLATION
The rule-based evaluators for attribute grammars introduce a powerful idea that serves as the basis for the ad hoc techniques used for context-sensitive analysis in many compilers.

In this scheme, the compiler writer provides snippets of code that execute
at parse time. Each snippet, or action, is directly tied to a production in the
grammar. Each time the parser recognizes that it is at a particular place in the
grammar, the corresponding action is invoked to perform its task.

