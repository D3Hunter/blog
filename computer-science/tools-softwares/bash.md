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
