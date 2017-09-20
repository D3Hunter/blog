命令替换`$(cmd)`和符号``cmd``差不多

### `()`和`{}`都是对一串的命令进行执行，但有所区别：
- ()只是对一串命令重新开一个子shell进行执行
- {}对一串命令在当前shell执行
- ()和{}都是把一串的命令放在括号里面，并且命令之间用;号隔开
- ()最后一个命令可以不用分号
- {}最后一个命令要用分号
- {}的第一个命令和左括号之间必须要有一个空格
- ()里的各命令不必和括号有空格
- ()和{}中括号里面的某个命令的重定向只影响该命令，但括号外的重定向则影响到括号里的所有命令

### `shell`中变量`${var}`,加`{}`以分隔变量名，和`$var`一个意思
- `${var:-string}`: 若变量var为空，展开成`string`否则为`var`
- `${var:=string}`: 基本和上面相同，区别在于`${var:=string}`若`var`为空时，替换的同时把`string`赋给变量`var`
- `${var:+string}`: 与`${var:-string}`相反
- `${var:?string}`: 若变量`var`不为空，则用变量`var`，为空，则把`string`输出到`stderr`中，并从脚本中退出。

### POSIX标准的扩展计算:`$((exp))`
- 这种计算是符合C语言的运算符，也就是说只要符合C的运算符都可用在$((exp))，甚至是三目运算符。
- 注意：这种扩展计算是整数型的计算，不支持浮点型.若是逻辑判断，表达式exp为真则为1,假则为0。

### 四种模式匹配替换结构：`${var%pattern},${var%%pattern},${var#pattern},${var##pattern}`
- %|%%表示从最右边(即结尾)匹配的，#|##从最左边(即开头)匹配的
- #|%  是最短匹配
- ##|%%是最长匹配
- 结构中的pattern支持glob，*表示零个或多个任意字符，?表示零个或一个任意字符，[...]表示匹配中括号里面的字符，[!...]表示不匹配中括号里面的字符。

### 特殊变量
- $$  Shell本身的PID（ProcessID）
- $!  Shell最后运行的后台Process的PID
- $?  最后运行的命令的结束代码（返回值）
- $-  使用Set命令设定的Flag一览
- $*  所有参数列表。如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。
- $@  所有参数列表。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。
- $#  添加到Shell的参数个数
- $0  Shell本身的文件名
- $1～$n 位置变量

### shell引号:
单引号内容表示`literal`意思, 即不能包含单引号, 但可以利用类似C里的"sss" "sss"自动拼接，来添加变量或‘
双引号内容除了$\和反引号外表示`literal`意思,且\能够转义$ ` " \ <newline>,若\跟其他字符\会被当作literal
所以:
- echo "\\n"  dash传给echo的字符串为[\n]    echo再转义则会输出换行
- echo "\\\n" dash传给echo的字符串为[\\n]   echo再转义则会输出\n
- echo '"\n"' dash传给echo的字符串为["\n"]  echo再转义则会输出"<换行>"
`sh(dash)`的`echo`基本等于`bash`的`echo -e`

### for循环
有效：var="aa abb"; for i in $var; do echo "$i"; done
    使用Makefile的变量也不行，需要复制过来
    Makefile里用$$来引用bash变量
无效：for i in "aa abb"; do echo "$i"; done
无效：var="aa abb"; for i in "$var"; do echo "$i"; done

对文件内每一行
cat peptides.txt | while read line
do
    # do something with $line here
done

迭代数组for fname in a.txt b.txt c.txt
for file in *.jtl; do
    wc -l $file |cut -d' ' -f 1 | awk '{print "'${file}'  "  $0/600.0}';
done
`for i in $(seq 1 10); do ...;done`

### misc
`n>&digit-` 将文件描述符`digit`作为`n`并关闭`digit`,不指定`digit`相当于关闭`n`,`n`默认为`stdout`,`n<&digit-`同理

`if [ ]; then...;fi`
`set  a b c` 设置到位置变量中
`set -x` 类似与verbose
bash里的strstr：if [[ ${image_name} == *"apache"* ]];

`cat`多行导入
`cat <<EOF` 读入标准输入直到遇到`EOF`为止，可包含变量。也可不使用终止符,而用`Ctrl-D`

IFS(Internal Field Seprator) 会影响set设置位置变量，及echo是否使用”扩起来，比如$@ $*

: 是no-op,可接受参数
if中用`-a` `-o` 表示 AND OR
`-bash: [: too many arguments`  使用的变量被IFS拆分为多个参数 需要用双引号扩起来
`shell`的实际解释器为`#!`设置的,要注意控制台`shell(bash)`与实际脚本使用`shell(sh或叫做dash)`的不同
