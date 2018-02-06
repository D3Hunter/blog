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

MySQL converts TIMESTAMP values from the current time zone to UTC for storage, and back from UTC to the current time zone for retrieval. (This does not occur for other types such as DATETIME.)

show procedure status;
show columns in xxx.xxx;

### table size
MyISAM的表可从information_schema.tables获取行数和表大小
    或select count(1), 两者行号都在表的.MYD文件中
InnoDB不行
SHOW TABLE STATUS查看某个表使用的什么数据引擎
    也可以用show create table
    在MyISAM下table_row, data_length, index_length为正确指，在Innodb下为内存索引大小近似
    结果从INFORMATION_SCHEMA TABLES来

### 获取一个月前的timestamp和date时间：
h2
- DATEADD('day', -29, CURRENT_DATE())
- datediff('ms', '1969-12-01', now()) 没有直接获得timestamp的方法
mysql
- DATE_ADD(CURDATE(), INTERVAL -29 DAY)
- 1000 * (UNIX_TIMESTAMP() - 31*24*60*60)

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

`mariadb-10`中的`user`表结构跟mysql的不太一样，注意导出数据时避免`mysql`数据库

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

### Fixed-Point Types (Exact Value) - DECIMAL, NUMERIC
The DECIMAL and NUMERIC types store exact numeric data values. These types are used when it is important to preserve exact precision, for example with monetary data. In MySQL, NUMERIC is implemented as DECIMAL


### functions
`last_insert_ID`: The ID that was generated is maintained in the server on a per-connection basis.

### join
the default is `INNER JOIN` if you just specify `JOIN`.
