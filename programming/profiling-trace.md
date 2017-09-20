`valgrind`如果进程再目录没权限就无法创建结果log，如`php-fpm/nginx/httpd`都会使用单独账户运行
对带有循环调用的函数，不易做profiling

systemtap、dtrace，strace，ptrace为内核trace相关，也可以处理上层应用
`valgrind`为动态程序分析，需要将程序运行于valgrind的VM中，相比于静态程序分析而言

### Linux tracers 以下trace都可以在程序运行中获取数据

- strace系统调用，可以抓正在运行的程序, 使用ptrace接口，需要暂停被trace的进程
- ltrace，可以trace库函数
- ftrace是一个kernel subsystem，类似dtrace
- perf_events
- eBPF
- SystemTap
- LTTng
- ktap
- sysdig

gdb/strace/ltrace都使用ptrace API
应用的kernel技术: kprobes/utrace/uprobes
strace防止参数被truncate，-s strsize。-o outfile