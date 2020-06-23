`Antlr 4`相比`Antlr 3`中不建议将`action`放到`grammer`中，除了为提高`grammer`的复用性，也是认识到所有的`action`其实就是一个`Visitor`的实现，这样就把`grammer`(语法识别)和`action`(`contex-sensitive analysis`)分离开。去除`AST`构建语法也类似。

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

### best practices
- `parser grammar`和`lexer grammar`要么完全分开，要么合并在一起，不然`parser grammar`还会生成一个单独的`lexer`。如果完全分开，需要在`parser`的`g4`中使用`parser grammar`，否则生成的parser名称会在`g4`名称的基础上在加上一个`Parser`后缀
- `lexer production name`以大写开头，`parser production name`以小写开头

#### lexer和parser完全分开的示例
- `parser.g4`开头指定grammar类型和tokenVocab：
```
parser grammar XXXParser;
options {tokenVocab=XXXLexer;}
```
- lexer.g4开头指定类型和注释channel
```
lexer grammar XXXLexer;
channels{COMMENTS}
```

### antlr maven plugin
```xml
<plugin>
    <groupId>org.antlr</groupId>
    <artifactId>antlr4-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>antlr</id>
            <goals>
                <goal>antlr4</goal>
            </goals>
            <configuration>
                <visitor>true</visitor>
            </configuration>
        </execution>
    </executions>
</plugin>
```

默认输入目录为`${basedir}/src/main/antlr4`，输出目录为`${project.build.directory}/generated-sources/antlr4`

Your input files under antlr4 should be stored in sub directories that reflect the package structure of your java parsers. 此时不需要在g4中指定package，会自动设置

### antlr runtime
- 同一个parser会累积ATNConfig，可以手动清除：ParserATNSimulator.html#clearDFA()

