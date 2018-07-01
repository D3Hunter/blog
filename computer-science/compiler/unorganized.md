a recursive descent parser is a kind of top-down parser built from a set of mutually recursive procedures (or a non-recursive equivalent) where each such procedure usually implements one of the productions of the grammar. Thus the structure of the resulting program closely mirrors that of the grammar it recognizes.

A predictive parser is a recursive descent parser that does not require backtracking. Predictive parsing is possible only for the class of LL(k) grammars, which are the context-free grammars for which there exists some positive integer k that allows a recursive descent parser to decide which production to use by examining only the next k tokens of input. 

Recursive descent with backtracking is a technique that determines which production to use by trying each production in turn. Recursive descent with backtracking is not limited to LL(k) grammars, but is not guaranteed to terminate unless the grammar is LL(k). Even when they terminate, parsers that use recursive descent with backtracking may require exponential time.

Although predictive parsers are widely used, and are frequently chosen if writing a parser by hand, programmers often prefer to use a table-based parser produced by a parser generator, either for an LL(k) language or using an alternative parser, such as LALR or LR. This is particularly the case if a grammar is not in LL(k) form, as transforming the grammar to LL to make it suitable for predictive parsing is involved. Predictive parsers can also be automatically generated, using tools like ANTLR.

Left to right, performing Leftmost derivation

An LL parser is called an LL(k) parser if it uses k tokens of lookahead when parsing a sentence. A grammar is called an LL(k) grammar if an LL(k) parser exists that can parse sentences belonging to the language that the grammar generates without backtracking.
LL parsers are table-based parsers, similar to LR parsers. LL grammars can also be parsed by recursive descent parsers.

an operator precedence parser is a bottom-up parser that interprets an operator-precedence grammar. For example, most calculators use operator precedence parsers to convert from the human-readable infix notation relying on order of operations to a format that is optimized for evaluation such as Reverse Polish notation (RPN)

a formal language is a set of strings of symbols together with a set of rules that are specific to it. A formal language is often defined by means of a formal grammar such as a regular grammar or context-free grammar, also called its formation rule.
