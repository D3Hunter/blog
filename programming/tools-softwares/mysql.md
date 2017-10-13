查询当前配置变量：`show variables like 'old%';`
`show tables from database;`
建表语句：`show create table tale_name;`
`show databases;`
当前数据库：`select database()`
当前用户：`SELECT USER()`
快速插入大量数据 `insert into user select * from user;`
execution plan also known as the `EXPLAIN` plan： `explain select * from users;`可以得到一系列op
### my.cnf位置
mysql --help可查看my.cnf的位置即读取顺序
/etc/my.cnf /etc/mysql/my.cnf /usr/etc/my.cnf ~/.my.cnf
### mysql bind address
如果mysql当前绑定到127.0.0.1，还需要修改mysql配置bind-address：
/etc/mysql/my.cnf或/etc/mysql/mysql.conf.d/mysqld.cnf
设置成0.0.0.0可以监听所有网卡

### 权限相关
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '111111' WITH GRANT OPTION;
flush privileges;
###忘记mysql密码可按下面的方式：
停掉mysql
mysqld_safe --user=mysql --skip-grant-tables --skip-networking &
免密登陆，修改密码：update user set Password=PASSWORD('root') where User='root';

### import, export
`mysqldump -u$user -p$pass -S $socket --all-databases > db_backup.sql`
`mysqldump -u <db_username> -h <db_host> -p db_name table_name > table_name.sql`
`mysql -u username -p db_name < /path/to/table_name.sql`
`mysql -u root -p'PASSWORD'`
	You must do this if the password has any of the following characters: * ? [ < > & ; ! | $ ( )

### mysql5.0默认old_passwords = 1，高版本的client连接时会报ERROR 2049 (HY000):
Connection using old (pre-4.1.1)，在client中加--skip-secure-auth可使用old
password，但最好的方法是修改密码，让其使用新的加密方式
set old_passwords = 0;
update user set password = password('testpass') where user = 'testuser';
select user,password from user;可看到密码长度变了
flush privileges;


### 本地密码保存
```
密码输入时仍然需要使用单引号转义
mysql_config_editor set --login-path=root --host=localhost --user=root --password
```
### 遇到如下错误,重启mysql
```
	Lost connection to MySQL server at 'reading initial communication packet', system error: 102
```