In mathematics, and in particular in group theory, a `cyclic permutation` (or cycle) is a permutation of the elements of some set X which maps the elements of some subset S of X to each other in a cyclic fashion, while fixing (that is, mapping to themselves) all other elements of X. If S has k elements, the cycle is called a `k-cycle`.

### random permutation of a finite sequence
Fisher–Yates shuffle

    for i from n−1 downto 1 do
        j ← random integer such that 0 ≤ j ≤ i
        exchange a[j] and a[i]

Variants: The "inside-out" algorithm: can be proved by induction
we do not know "n", the number of elements in source, in this algorithm

    for i from 0 to n − 1 do
        j ← random integer such that 0 ≤ j ≤ i
        if j ≠ i
            a[i] ← a[j]
        a[j] ← source[i]

有些biased实现并不能保证perfcet shuffle，One way to see that you won't get a perfectly uniform distribution is by divisibility.
参考https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle有关biased的讨论

