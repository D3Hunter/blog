### 达梦数据库
- 开发版不需要key文件，安装后不会自动运行
- 使用dminit初始化一个库
- 启动dmserver，附带刚才初始化好的库里面的dm.ini
- 使用disql连接dmserver，初始用户为sysdba/sysdba
- 默认每个用户都有自己的schema，所以默认schema为sysdba
- 当前模式查询：SELECT SYS_CONTEXT ('userenv', 'current_schema') FROM DUAL;
- 一些系统表：dba_tables, all_tables，整体上这些表明跟oracle很像
- 达梦使用一个端口对应一个数据库，因此连接时不需要指定数据库
- 达梦的user、schema基本对应postgres的database、schema，但对于SYS这个用户，是对应的Oracle的SYS用户／schema
- 达梦的jdbc不能一次执行多条DDL，没找到相关的jdbc连接参数

