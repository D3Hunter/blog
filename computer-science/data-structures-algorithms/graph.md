In computer science, in `control flow graphs`, a node `d` dominates a node `n` if every path from the `entry node` to `n` must go through `d`. Notationally, this is written as `d dom n` (or sometimes `d >> n`). **By definition, every node dominates itself.**

Extend the dominance frontier mapping from nodes to sets of nodes: `DF(L) = ∪[DF(X)] X ∈ L`
The `iterated dominance frontier` `DF+(L)` is the limit of the sequence: `DF1 = DF(L)`,`DFi+1 = DF(L ∪ DFi)`

