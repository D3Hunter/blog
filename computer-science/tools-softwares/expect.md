一个ssh到host执行mysql-client的示例：
```shell
#!/usr/bin/env expect -f

set host [lindex $argv 0]

# StrictHostKeyChecking no避免yes/no提示
spawn ssh -o "StrictHostKeyChecking no" -t root@$host "mysql -u root"
expect "password:"
send -- "host-password\n"
expect "mysql"
send "mysql-password\n"
interact
```
