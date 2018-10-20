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
