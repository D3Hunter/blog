### ssh
-f可以让ssh在执行命令前进入后台，但这样本地会多出一个ssh进程
`ssh  root@10.128.6.234 'sleep 300&'`会导致本地stuck，因为stdout还与远端的ssh保持连接中，使用nohup同样会保持stdout因此也不行
`ssh  root@10.128.6.234 'sleep 300 2>/dev/null &'`本地也会stuck
`ssh  root@10.128.6.234 'sleep 300 >/dev/null &'`可断开

远程运行locust（python脚本）时必须同时重定向stderr，否则程序起不来，原因未知

互信登陆只需要编写~/.ssh/authorized_keys就可以

On the remote host, there are two relevant processes:
- an instance of the ssh daemon (sshd), which is relaying the input and output of the remote program to the local terminal;
- a shell, which is running that for loop.
关闭本地时同时kill远端，需要分配tty保证信号被正确relay过去

如果不做重定向的话，nohup的stdout/stderr仍然与当前shell连接，如果用ssh执行导致不会退出（lingering）

### 配置项
避免断开
- 在client端`~/.ssh/config`添加`ServerAliveInterval 30`
- 在server端`/etc/ssh/sshd_config`中添加`ClientAliveInterval 60`

ssh支持连接复用，只要一个终端连接上了，后续的窗口可免密码登陆

关闭用户名密码登陆：`PasswordAuthentication no`

#### local/remote forwarding:
ssh user@example.com -L bind_address:9000:some-host:5432 # forward any tcp traffic on 9000 to some-host:5432 through example.com，本地监听9000
ssh user@example.com -L bind_address:9000:localhost:5432 # here localhost means example.com
ssh user@example.com -R bind_address:9000:some-host:3000 # forward any traffic from example:9000 to some-host:3000 through chient，远端监听9000
ssh user@example.com -R bind_address:9000:localhost:3000 # here localhost means ssh client
忽略bind_address时默认绑定地址为loopback
ssh -nNf(-nNT)可以避免打开登陆shell，而仅作端口转发
remote forwarding默认不开启，需要在/etc/ssh/sshd_config中设置GatewayPorts yes
当remote forwarding不可用，但可在example.com上访问client时，可通过在example.com上做-L，来实现-R，即：
    在example.com上执行ssh localhost -L 9000:client:5432

避免输入(yes/no):`ssh -o "StrictHostKeyChecking no" user@host`

#### dynamic forwarding
ssh user@example.com -D 1080 # 本地监听1080作为SOCKS代理，通过example.com转发数据
SOCKS本身并不是安全的，但是dynamic forwarding时SOCKS数据通过ssh发送，则是安全的
而像现在的ShadowSocks，也是本地加密，通过非加密通道传输
