`schema`只能是小写，

更改schema: `set schema 'schema_name';`

使用guid函数需要安装extension: `create extension "uuid-ossp";`

命令行登陆: `psql dbName userName`

获取当前session list: `SELECT pid FROM pg_stat_activity where backend_type='client backend' and pid != pg_backend_pid()`

强制中止session：`SELECT pg_terminate_backend(?) from dual`

### 忘记密码：
- 更改`pg_hba.conf`，添加`host  all   all  127.0.0.1/32  trust`
- `sudo /etc/init.d/postgresql restart`
- `psql -U postgres`
    - 如果报：`Peer authentication failed for user "postgres"`，则使用`sudo -u postgres psql -U postgres`
- `ALTER USER my_user_name with password 'my_secure_password';`或使用`\password`

### PostgreSQL开启plpgsql调试
- postgresql.conf（一般在data目录下）中设置shared_preload_libraries = '$libdir/plugin_debugger'
- create extension pldbgapi;
- 然后在对应function上，右键菜单debugging

