## Query Optimizer
SQL is declarative; the user specifies what the query returns, not how it should be executed

#### There are many equivalences in SQL:
- Joins can be applied in any order
- Predicates can be evaluated in any order
- Subselects can be transformed into joins

#### Several different methods of doing the same operation:
- Three core join algorithms (nested loops, hash join, merge join)
- Two aggregation algorithms (hashing, sorting)
- Two scan algorithms (index scan, sequential scan)

For a non-trivial query there are many alternative plans

