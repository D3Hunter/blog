连接需要service name或者sid
`ORA-21561: OID generation failed`: `/etc/hosts`中的`127.0.0.1`与`hostname`要关联

sql中双引号用于表示标识符，单引号用来表示字符串，用错会报：`ORA-00984 column not allowed here`
如果需要表示`'`, 需要使用`'`来转义，即使用两个单引号`''`来表示字符串内出现的一个`'`
