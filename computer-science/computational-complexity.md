## P/NP/NP-complete/NP-hard
`Decision problem`: A problem with a yes or no answer.

NP: an abbreviation for "nondeterministic polynomial time"
- `P` is a complexity class that represents the set of all `decision problems` that can be solved in polynomial time.
- `NP` is a complexity class that represents the set of all `decision problems` for which the instances where the answer is "yes" have proofs that can be verified in polynomial time.
- `NP-Complete` is a complexity class which represents the set of all problems `X` in `NP` for which it is possible to reduce any other `NP` problem Y to `X` in polynomial time.
- `NP-hard`: The precise definition here is that a problem `X` is `NP-hard`, if there is an `NP-complete` problem `Y`, such that `Y` is reducible to `X` in polynomial time.
    - `Intuitively`, these are the problems that are at least as hard as the NP-complete problems.
    - Note that `NP-hard` problems do not have to be in `NP`, and they do not have to be `decision problems`.
- P = NP
    - It's clear that P is a subset of NP.
    - The open question is whether or not NP problems have deterministic polynomial time solutions. It is largely believed that they do not.

```
+--------------+----------------------+--------------------+
| Problem Type | Verifiable in P time | Solvable in P time | Increasing Difficulty
+--------------+----------------------+--------------------+           |
| P            |        Yes           |        Yes         |           |
| NP           |        Yes           |     Yes or No *    |           |
| NP-Complete  |        Yes           |      Unknown       |           |
| NP-Hard      |     Yes or No **     |      Unknown ***   |           |
+--------------+----------------------+--------------------+           V

* An NP problem that is also P is solvable in P time.
** An NP-Hard problem that is also NP-Complete is verifiable in P time.
*** NP-Complete problems (all of which form a subset of NP-hard) might be. The rest of NP hard is not.
```

