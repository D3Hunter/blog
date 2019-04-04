### terminal出现乱码
`terminal`的输出变乱（按回车会打印PS1但并不换行，输入也不显示），是`echo`被关闭导致,可使用`reset`，或`stty echo`打开echo（`stty -echo`用来关闭echo）
bash里`\[\]`用来表示non-printable字符的开始结束，否则针对过长的命令，会导致bash不能正确显示输入
对应到ascii代码为`\001`和`\002`，在不能使用`\[\]`的情况可以使用这两个，如gdb prompt
参考：https://superuser.com/questions/301353/escape-non-printing-characters-in-a-function-for-a-bash-prompt/301355

### job 管理
jobs/disown/fg/bg/跟作业管理相关，disown解除关系（不再在shell接受到HUP时向该进程发送HUP）
使用时jobspec需要加前缀%
先将作业stop（Ctrl-z）然后bg即可将作业放置后台

### 关闭history记录
- 配置中添加`set +o history`
- 删除`.bash_history`

`history -c` clears your history in the current shell.

### misc
- `PROMPT_COMMAND`: If set, the value is executed as a command prior to issuing each primary prompt.

### Redirection
使用`pipe`时，`pipe`是先创建好的（在`fork`前创建`fifo`，`child`直接继承），然后才处理命令行上的`redirect`

the redirect operators for each side are evaluated from left to right, and the current settings are used whenever duplication of the descriptor occurs.

### 只pipe stderr
`foo 2>&1 >/dev/null | bar`
- `pipe`: `foo fd1 -> bar fd0`
- `redirect 2>&1`: `copy foo fd1 to foo fd2`, 意味着这两个都到 `bar fd0`
- `redirect >/dev/null`: `foo fd1 to /dev/null`, 即关闭`foo fd1`

注意该方法在`zsh`都不生效，因为`zsh`默认开启`mult_ios`，上面命令的结果是`foo fd1`即到`bar fd0`也到`/dev/null`，需要改为：
- `foo 2>&1 >&- | bar` 即关闭`foo fd1`

