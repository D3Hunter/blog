a Java persistence framework that couples objects with stored procedures or SQL statements using an XML descriptor or annotations.
Unlike ORM frameworks, MyBatis does not map Java objects to database tables but Java methods to SQL statements.
The SqlSession contains absolutely every method needed to execute SQL commands against the database.
SqlSessionFactoryBuilder/SqlSessionFactory/SqlSession/Mapper instances
select count(1) from ${}设置表名

${} string substitution，而#{}类似PreparedStatement中的'?'
    ${}不能直接引用某个变量，String不行，目前的做法是放到Map里引用对应key

ScriptRunner用来执行数据库脚本

提供TableNameHandler，可以通过逻辑表名映射到实际表名

DataSourceContextHolder.setDataSourceSuffix似乎用来设置database名的suffix

MapperScannerConfigurer自动搜索所有的DAO
SqlSessionFactoryBean设定typeAliasesPackage可自动搜索Entity
