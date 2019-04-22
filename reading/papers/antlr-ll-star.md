### LL(*): The Foundation of the ANTLR Parser Generator
By statically removing as much speculation as possible, LL(*) provides the expressivity of PEGs while retaining LL’s good error handling and unrestricted grammar actions.

When parsing theory was originally developed, machine resources were scarce, and so parser efficiency was the paramount concern.

In response to this development, researchers have developed more powerful, but more costly, nondeterministic parsing strategies following both the “bottom-up” approach (LR-style parsing) and the “top-down” approach (LL-style parsing).

In the “bottom-up” world, Generalized LR (GLR) [16] parsers parse in linear to cubic time, depending on how closely the grammar conforms to classic LR.

Elkhound is a very efficient GLR implementation that achieves yacc-like parsing speeds when grammars are LALR(1).

In the “top-down” world, Ford introduced Packrat parsers and the associated Parser Expression Grammars (PEGs)

Packrat parsers are linear rather than exponential because they memoize partial results, ensuring input states will never be parsed by the same production more than once. The Rats! PEG-based tool vigorously optimizes away memoization events to improve speed and reduce the memory footprint.

Despite this advantage, neither GLR nor PEG parsers are completely satisfactory, for a number of reasons.
- First, GLR and PEG parsers do not always do what was intended.
- Second, debugging nondeterministic parsers can be very difficult.
- Third, generating high-quality error messages in nondeterministic parsers is difficult but very important to commercial developers.
- Finally, nondeterministic parsing strategies cannot easily support arbitrary, embedded grammar actions, which are useful for manipulating symbol tables, constructing data structures, etc.

The contributions of this paper are
1. the top-down parsing strategy LL(\*)
2. the associated static grammar analysis algorithm that constructs LL(*) parsing decisions from ANTLR grammars.

ANTLR generates top-down, recursive-descent, mostly nonspeculating parsers, which means it supports source-level debugging, produces high-quality error messages, and allows programmers to embed arbitrary actions.

