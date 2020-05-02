## Relational algebra
Relational algebra, first created by Edgar F. Codd while at IBM, is a family of algebras with a well-founded semantics used for modelling the data stored in relational databases, and defining queries on it.

The main application of relational algebra is providing a theoretical foundation for relational databases, particularly query languages for such databases, chief among which is SQL.

Five primitive operators of Codd's algebra are
- selection
    - A `generalized selection` is a unary operation written as `σ(φ, R)` where φ is a `propositional formula`... This selection selects all those tuples in `R` for which `φ` holds.
- projection: 对应到SQL就是选择列表
- Cartesian product (also called the cross product or cross join)
- set union
- set difference.
    - For `set union` and `set difference`, the two relations involved must be `union-compatible`--that is, the two relations must have the same set of attributes. Because `set intersection` is defined in terms of set union and set difference, the two relations involved in set intersection must also be union-compatible.

## Boolean algebra
In `mathematics` and `mathematical logic`, `Boolean algebra` is the branch of algebra in which the values of the variables are the truth values true and false, usually denoted 1 and 0 respectively. Instead of `elementary algebra` where the values of the variables are numbers, and the prime operations are addition and multiplication, the main operations of `Boolean algebra` are the `conjunction (and)` denoted as `∧`, the `disjunction (or)` denoted as `∨`, and the `negation (not)` denoted as `¬`. It is thus a formalism for describing logical operations in the same way that `elementary algebra` describes numerical operations.

### Applications in computers
In the early 20th century, several electrical engineers intuitively recognized that `Boolean algebra` was analogous to the behavior of certain types of electrical circuits. `Claude Shannon` formally proved such behavior was logically equivalent to `Boolean algebra` in his 1937 master's thesis, `A Symbolic Analysis of Relay and Switching Circuits`.

Today, all modern general purpose computers perform their functions using `two-value Boolean logic`; that is, their electrical circuits are a physical manifestation of two-value Boolean logic.

## propositional logic
`Propositional logic` is a logical system that is intimately connected to `Boolean algebra`. Many syntactic concepts of `Boolean algebra` carry over to `propositional logic` with only minor changes in notation and terminology, while the semantics of `propositional logic` are defined via `Boolean algebras` in a way that the tautologies (theorems) of `propositional logic` correspond to equational theorems of `Boolean algebra`.

### propositional formula
In `propositional logic`, a `propositional formula` is a type of syntactic formula which is well formed and has a truth value. If the values of all variables in a `propositional formula` are given, it determines a unique truth value. A `propositional formula` may also be called a `propositional expression`, a `sentence`, or a `sentential formula`.

### Relationship between propositional and predicate formulas
The `predicate calculus` goes a step further than the `propositional calculus` to an "analysis of the inner structure of propositions". It breaks a simple sentence down into two parts (i) its subject and (ii) a predicate.

In particular, simple sentences that employ notions of "all", "some", "a few", "one of", etc. are treated by the `predicate calculus`...∀ (For all), and ∃ (There exists ..., At least one of ... exists, etc.).

### Normal forms
An arbitrary `propositional formula` may have a very complicated structure. It is often convenient to work with formulas that have simpler forms, known as `normal forms`. Some common `normal forms` include `conjunctive normal form` and `disjunctive normal form`. Any propositional formula can be reduced to its conjunctive or disjunctive normal form.

#### Conjunctive normal form
In Boolean logic, a formula is in `conjunctive normal form (CNF)` or `clausal normal form` if it is a `conjunction` of one or more clauses, where a clause is a `disjunction of literals`; otherwise put, it is an `AND of ORs`.

As in the `disjunctive normal form (DNF)`, the only propositional connectives a formula in CNF can contain are `and`, `or`, and `not`. The `not` operator can only be used as part of a literal, which means that it can only precede a `propositional variable` or a `predicate symbol`. 因此`¬(A ∨ B)`并不是CNF形式

##### Conversion into CNF
Every `propositional formula` can be converted into an equivalent formula that is in `CNF`. This transformation is based on rules about logical equivalences: `double negation elimination`, `De Morgan's laws`, and `the distributive law`.

all propositional formulae can be converted into an equivalent formula in CNF...However, in some cases this conversion to CNF can lead to an exponential explosion of the formula.

There exist transformations into CNF that avoid an exponential increase in size by preserving `satisfiability` rather than `equivalence`. These transformations are guaranteed to only linearly increase the size of the formula, but introduce new variables.

http://cs.jhu.edu/~jason/tutorials/convert-to-CNF

###### Computational complexity
The standard algorithm to transform a general `Well-Formed Formula` to an equivalent `CNF` has an exponential run time, since in the worst case a `n-clauses WFF` is equivalento to a `2^n-clauses CNF`. 当然现实中的case未必这么复杂

The task of converting a formula into a DNF, preserving satisfiability, is NP-hard; dually, converting into CNF, preserving validity, is also NP-hard; hence equivalence-preserving conversion into `DNF` or `CNF` is again `NP-hard`.

#### Disjunctive normal form
In boolean logic, a `disjunctive normal form (DNF)` is a canonical normal form of a logical formula consisting of a disjunction of conjunctions; it can also be described as an `OR of ANDs`.

The `not` operator can only be used as part of a literal, which means that it can only precede a `propositional variable` or a `predicate symbol`. 因此`¬(A ∨ B)`并不是DNF形式

`Conversion to DNF`跟`Computational complexity`参考`CNF`

#### Reduction to normal form
Reduction to normal form is relatively simple once a `truth table` for the formula is prepared...`Karnaugh maps` are very suitable a small number of variables (5 or less).

`Quine–McCluskey algorithm`: a method used for minimization of Boolean functions.

## Logical equivalence
In logic and mathematics, statements `p` and `q` are said to be `logically equivalent`, if they are provable from each other under a set of axioms, or have the same truth value in every model.

## Boolean satisfiability problem
In logic and computer science, the `Boolean satisfiability problem` (sometimes called `propositional satisfiability problem` and abbreviated `SATISFIABILITY` or `SAT`) is the problem of determining if there exists an interpretation that satisfies a given `Boolean formula`. In other words, it asks whether the variables of a given `Boolean formula` can be consistently replaced by the values TRUE or FALSE in such a way that the formula evaluates to TRUE. If this is the case, the formula is called `satisfiable`, otherwise `unsatisfiable`.

`SAT` is the first problem that was proven to be `NP-complete`. Nevertheless, as of 2007, `heuristic SAT-algorithms` are able to solve problem instances involving tens of thousands of variables and formulas consisting of millions of symbols, which is sufficient for many practical SAT problems from, e.g., `artificial intelligence`, `circuit design`, and `automatic theorem proving`.

基于sql的filter生成数据既是该问题的一个具体case。

## satisfiability and validity
In `mathematical logic`, `satisfiability` and `validity` are elementary concepts of semantics. A formula is `satisfiable` if it is possible to find an interpretation (model) that makes the formula true. A formula is `valid` if all interpretations make the formula true. The opposites of these concepts are `unsatisfiability` and `invalidity`

`Satisfiability` of formulas in `DNF` can be checked in linear time: A formula in `DNF` is `satisfiable` iff at least one of its conjunctions is satisfiable. A conjunction is satisfiable iff for every atomic formula A the conjunction does not contain both `A` and `¬A` as literals.

Validity of formulas in CNF can be checked in linear time: A formula in `CNF` is `valid` iff all its disjunctions are valid. A disjunction is valid iff for some atomic formula A the disjunction contains both `A` and `¬A` as literals (or the disjunction is empty.)

Theorem: Satisfiability of formulas in CNF is NP-complete.

Theorem: Validity of formulas in DNF is NP-complete.

## boolean expression
`Boolean expressions` correspond to `propositional formulas` in `logic` and are a special case of `Boolean circuits`.

## First-order logic
`First-order logic` — also known as `predicate logic`, `quantificational logic`, and `first-order predicate calculus` — is a collection of formal systems used in mathematics, philosophy, linguistics, and computer science. `First-order logic` uses quantified variables over non-logical objects and allows the use of sentences that contain variables, so that rather than propositions such as `Socrates is a man` one can have expressions in the form `"there exists x such that x is Socrates and x is a man"` and `there exists` is a `quantifier` while `x` is a `variable`. This distinguishes it from `propositional logic`, which does not use `quantifiers` or `relations`; in this sense, `propositional logic` is the foundation of `first-order logic`.

### predicate
Informally, a `predicate` is a statement that may be true or false depending on the values of its variables. It can be thought of as an operator or function that returns a value that is either true or false.

## automic formula
In `mathematical logic`, an `atomic formula` (also known simply as an `atom`) is a formula with no deeper `propositional` structure, that is, a `formula` that contains no logical connectives or equivalently a formula that has no strict subformulas. `Atoms` are thus the simplest well-formed formulas of the logic. `Compound formulas` are formed by combining the atomic formulas using the logical connectives.

The precise form of `atomic formulas` depends on the logic under consideration; for `propositional logic`, for example, the atomic formulas are the propositional variables. For `predicate logic`, the atoms are predicate symbols together with their arguments, each argument being a term.

