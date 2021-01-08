## misc
PostgreSQL provides several index types: `B-tree`, `Hash`, `GiST`, `SP-GiST`, `GIN` and `BRIN`.

## public
`public`在pg下是一个真正的schema，可创建任意对象，类似一个公共的schema，无schema的形式访问public对象，需要设置`search_path`:
```sql
set search_path to user_name,public;
```

## 常用SQL
- 设置当前schema／search_path: `SET SCHEMA 'value'` is an alias for `SET search_path TO value`.
- 关键字／保留字／特殊标识符：`select * from pg_get_keywords()`
- 函数oid：`select oid from pg_proc where proname='pg_get_functiondef';`
- 函数定义：`select pg_get_functiondef(1939) from dual;`
- 函数信息：`SELECT * FROM information_schema.routines WHERE routine_schema='pg_catalog' and routine_type='FUNCTION' and routine_name='xxx';`
- 函数定义：
    - `select proname, pg_get_functiondef(oid) from pg_proc where proname like '%describe_columns%';`
- 类型信息:
    - `select * from pg_type where oid=2249`
    - `select oid, t.* from pg_type t where typname like '%json%';`
- 表列类型：`select column_name, data_type from information_schema.columns where table_name='hd_communication_opinion'`
- extension查询
    - `select * from pg_available_extensions where name like '%ascii%';`
- 字符集
    - `show server_encoding;`
    - `show client_encoding;`
    - 临时更改客户端字符集： `SET CLIENT_ENCODING TO 'value';`
    - 更改默认客户端字符集(对psql无效)： `alter role role-name set client_encoding to 'utf8'`
- 当前数据库参数
    - session设置
        - 使用show或set查看或设置
        - 可从pg_settings这个view查看或设置: `select name, setting from pg_settings where name like '%encoding%';`
    - role级别
        - ALTER ROLE或通过pg_roles表设置或查看
- role
    - `SELECT rolname FROM pg_roles;`
- namespace: `select oid from pg_namespace where nspname='pg_catalog';`
- 表达式类型： `SELECT pg_typeof('{}'::text[]);`
- 获取当前session list: `SELECT pid FROM pg_stat_activity where backend_type='client backend' and pid != pg_backend_pid()`
- 强制中止session：`SELECT pg_terminate_backend(?) from dual`

## psql
- 登陆：`psql -U postgres -h xxx`
- 显示所有的表: `\dS`
- 显示表定义\d

## install
1. 默认安装到`/usr/pgVERSION`，`initdb`后的数据目录在`/var/lib/pgsql`。数据目录下有两个重要的配置文件`postgresql.conf`和`pg_hba.conf`，前者为主配置文件，后者为用户认证配置。

2. `initdb`后，默认本地登陆使用`ident`，即需要使用本地用户，登陆方法:
- `su - postgres`
- `psql`

3. 登陆后更改`postgres`用户密码`alter user postgres password 'postgres';`
4. 允许用户通过密码登陆，在`pg_hba.conf`中添加
```
host    all             all             0.0.0.0/0               md5
```
5. 编辑`postgresql.conf`，监听TCP端口
```
listen_addresses = '*'
```
6. 配置更改后需要重启才生效
    - centos下，`systemctl restart postgresql-VERSION.service`

7. 自动启动
- `systemctl list-unit-files`: To list all units installed on the system.
- `systemctl enable xxx`

### 忘记密码
- 更改`pg_hba.conf`，添加`host  all   all  127.0.0.1/32  trust`
- `sudo /etc/init.d/postgresql restart`
- `psql -U postgres`
    - 如果报：`Peer authentication failed for user "postgres"`，则使用`sudo -u postgres psql -U postgres`
- `ALTER USER my_user_name with password 'my_secure_password';`或使用`\password`

### PostgreSQL开启plpgsql调试
- postgresql.conf（一般在data目录下）中设置shared_preload_libraries = '$libdir/plugin_debugger'
- create extension pldbgapi;
- 然后在对应function上，右键菜单debugging

### non-deterministic collation
PG12开始支持，官网给出的例子`locale = 'und-u-ks-level2'`在特定版本的`ICU`下不支持(比如libicui18n.so.50.2)，需要使用下面的语句
```sql
CREATE COLLATION case_insensitive (provider = icu, locale = '@colStrength=secondary', deterministic = false);
```

## function vs procedure
- 返回值: SQL standard appears to take a middle ground, in that a `procedure` by default has a different transaction behavior than a `function`, but this can be adjusted per object.
- You can `commit` and `rollback` transactions inside `stored procedures`, but not in `functions`
- You execute a stored procedure using the `CALL` statement rather than a `SELECT` statement.
- The main difference between `function` and `stored procedure` is that user-defined functions do not execute transactions. This means, inside a given function you cannot open a new transaction, neither can you commit or rollback the current transaction. It is important to note that stored procedures are just functions that can support transactions and were introduced in Postgresql 11.

## plpgsql
- you cannot access to out parameters outside function - because they doesn't exist - postgresql cannot pass parameters by ref. 实际调用时，不能传入`OUT`所在的参数，会报找不到函数
- if function has more `out` parameters, then return type is `record` type.
- when function has `OUT` variables in Postgres, then `RETURN` statement is used only for ending execution - not for returned value specification. 此时不能使用`return expression`的语句。
- PostgreSQL的plpgsql程序不存在编译时依赖，只有运行时依赖，因此可直接创建相互依赖的函数，无需`forward declaration`

