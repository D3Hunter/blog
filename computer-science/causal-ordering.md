http://scattered-thoughts.net/blog/2012/08/16/causal-ordering/

We’ll start with the fundamental property of distributed systems:

Messages sent between machines may arrive zero or more times at any point after they are sent

This is the sole reason that building distributed systems is hard.

We are used to thinking of ordering by time which is a total order - every pair of events can be placed in some order. In contrast, causal ordering is only a partial order - sometimes events happen with no possible causal relationship i.e. not (A -> B or B -> A).

Since we don’t have a single global time this is the only thing that allows us to reason about causality in a distributed system. This is really important so let’s say it again:

Communication bounds causality

###partially ordered set
The word "partial" in the names "partial order" or "partially ordered set" is used as an indication that not every pair of elements need be comparable. 