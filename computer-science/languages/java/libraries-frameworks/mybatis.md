MyBatis is a Java persistence framework that couples objects with stored procedures or SQL statements using an XML descriptor or annotations. Unlike ORM frameworks, MyBatis does not map Java objects to database tables but Java methods to SQL statements. `MyBatis` is a fork from `iBATIS`(currently marked as Inactive)

The `SqlSession` contains absolutely every method needed to execute SQL commands against the database.

- `${}` string substitution，而`#{}`类似PreparedStatement中的'?'. `${}`不能直接引用某个变量，String不行，目前的做法是放到Map里引用对应key

ScriptRunner用来执行数据库脚本

提供TableNameHandler，可以通过逻辑表名映射到实际表名

`DataSourceContextHolder.setDataSourceSuffix`似乎用来设置database名的suffix

- `MapperScannerConfigurer`自动搜索所有的DAO
- `SqlSessionFactoryBean`设定`typeAliasesPackage`可自动搜索Entity

One `SqlSessionFactory` instance per database

There are two `TransactionManager` types (i.e. `type="[JDBC|MANAGED]"`) that are included with MyBatis。However, they are both Type Aliases.

There are three build-in dataSource types (i.e. `type="[UNPOOLED|POOLED|JNDI]"`):

mappers can use classpath relative resource references, fully qualified url references (including file:/// URLs), class names or package names.

The MyBatis `3.5.0` will support `JDK 8+`.

best practices for scopes and lifecycles of objects
- `SqlSessionFactoryBuilder`: method scope
- `SqlSessionFactory`: application scope
- `SqlSession`: request/method scope
- `Mapper`: method scope
