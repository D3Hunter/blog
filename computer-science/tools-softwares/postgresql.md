`schema`只能是小写，

更改schema: `set schema 'schema_name';`

使用guid函数需要安装extension: `create extension "uuid-ossp";`

命令行登陆: `psql dbName userName`

获取当前session list: `SELECT pid FROM pg_stat_activity where backend_type='client backend' and pid != pg_backend_pid()`

强制中止session：`SELECT pg_terminate_backend(?) from dual`

