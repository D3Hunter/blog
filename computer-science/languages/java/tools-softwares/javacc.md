Java Compiler Compiler:
- generates `top-down` parsers, can handle `LL(k)` grammers; by use of `lookahead specifications`, it can also resolve choices requiring unbounded look ahead.
- targeting Java or C/C++ or C#
- don't require a runtime library
- to construct a parse tree, you need JJTree
- more lightweight than ANTLR, and faster
- older than ANTLR(Created in 1996 at SUN)
