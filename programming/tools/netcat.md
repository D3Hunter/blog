`netcat/nc` 可用来做TCP/UDP/Unix-domain相关的事情,连接/发送/监听
以下是一个简单的SSH,但不安全,任何连接过来的用户都可以执行命令
- On ‘server’ side:
    $ rm -f /tmp/f; mkfifo /tmp/f
    $ cat /tmp/f | /bin/sh -i 2>&1 | nc -l 127.0.0.1 1234 > /tmp/f
- On ‘client’ side:
    $ nc host.example.com 1234
    $ (shell prompt from host.example.com)
此外netcat还可用来扫描端口,手动向server发送信息(MAIL/HTTP这类文本协议,telnet也有类似的功能)等.
