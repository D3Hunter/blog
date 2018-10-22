`antlr`可生成`visitor`和`listener`两种接口，前者更灵活，后者更简单

`fragment`里的作为逻辑词法结构，不会作为独立的token

### setting up
- `export CLASSPATH=".:/usr/local/lib/antlr-4.0-complete.jar:$CLASSPATH"`
- `alias antlr4='java -jar /usr/local/lib/antlr-4.0-complete.jar'`
- `alias grun='java org.antlr.v4.runtime.misc.TestRig'`

### Sharing Information Among Event Methods
1. Return values of visitors.
2. Simulating Return Values with a Stack. (espicially listener interface)
3. Annotating parse trees, `ParseTreeProperty`可用来annotate parse tree

### notes from The Definitive of ANTLR 4 Reference
`FOLLOW Sets` vs. `Following Sets`

The `following set` for a rule reference is the set of tokens that can match immediately following that reference and without leaving the current rule. So, for example, given alternative assign ';', the following set for rule reference assign is {’;’}.

To resynchronize, it has three choices. It can delete a token, it can conjure one up, or it can punt and throw an exception to engage the basic sync-and-return mechanism.

When faced with truly borked-up input, the current rule can’t continue, so the parser recovers by gobbling up tokens until it thinks that it has resynchronized and then returns to the calling rule. We can call this the `sync-and-return` strategy.

Classifying something as an `island language` often depends on our perspective. If we’re building a C preprocessor, the preprocessor commands form an island language where the C code is the sea. On the other hand, if we’re building a C parser suitable for an IDE, the parser must ignore the sea of preprocessor commands.

Issuing Context-Sensitive Tokens with `Lexical Modes`

The `atn` term means `augmented transition network` and is a state machine that can represent a grammar where edges represent grammar elements.
