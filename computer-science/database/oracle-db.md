### 分区
1. range
- range分区可以在多列上，Interval range分区只能在一列上
- 多列比较时为逐列比较，如果前一列相同再往后比较，比如(1, 2) < (1, 3)
- range_values只能是literal values

2. oracle的list分区只能在一列上，每个partition可在多个值上
- Oracle 12.2 支持在多列上创建list分区。目前基本没遇到过
- 只能是literal value

### misc
- oracle定义subprogram时，如果没有参数，则一定不能有`()`
- `DATE`类型的literal可以使用TO_DATE函数
- `DECLARE`在function/procedure中一定没有，在匿名块中一定有
- `nested subprogram` 必须在`declaration part`的末尾定义，在中间定义报错：`Encountered the symbol "XXX" when expecting one of the following`
- Analytic functions are the last set of operations performed in a query except for the final `ORDER BY` clause. All joins and all `WHERE`, `GROUP BY`, and `HAVING` clauses are completed before the analytic functions are processed. Therefore, analytic functions can appear only in the select list or ORDER BY clause.
- If you omit the `windowing_clause` entirely, then the default is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. `windowing_clause`必须跟order配合使用，如果没有order，则默认的frame是全部的结果行

### multitenant architecture(since 12c)
The `multitenant architecture` enables an Oracle database to function as a multitenant `container database (CDB)`.

A `CDB` includes zero, one, or many customer-created `pluggable databases (PDBs)`. A PDB is a portable collection of schemas, schema objects, and nonschema objects that appears to an Oracle Net client as a `non-CDB`. All Oracle databases before Oracle Database 12c were non-CDBs.

A container is either a PDB or the root. The root container is a collection of schemas, schema objects, and nonschema objects to which all PDBs belong.

Every CDB has the following containers:
- Exactly one root
    - The root container is named CDB$ROOT.
- Exactly one seed PDB
    - a system-supplied template that the CDB can use to create new PDBs. The seed PDB is named PDB$SEED.
- Zero or more user-created PDBs

In multitenant environments there are two types of user.
- Common User : The user is present in all containers (root and all PDBs). 用户名一定以"c##"开头
- Local User : The user is only present in a specific PDB. The same username can be present in multiple PDBs, but they are unrelated.用户名一定**不能**以"c##"开头，在oracle 12c之前都是这种类型的用户
    - 这两个用户链接方式一样，访问具体PDB使用`alter session set container = xxx`

### jdbc url(Database URLs and Database Specifiers)
The complete URL syntax is: `jdbc:oracle:driver_type:[username/password]@database_specifier`
- The supported driver_type values are `thin`, `oci`, and `kprb`.

Supported Database Specifiers
- Thin-style service name: `//host_name:port_number/service_name`
- sid(for thin driver): `host:port:sid`

### concepts
参考：
- [Introduction to Oracle Database](https://docs.oracle.com/database/121/CNCPT/intro.htm#CNCPT001)
- [Connectivity Concepts](https://docs.oracle.com/cd/B19306_01/network.102/b14212/concepts.htm)
- [Help! I can’t connect to my database](https://edstevensdba.wordpress.com/2011/02/09/sqlnet_overview/)
- [ORA-12514: TNS:listener does not currently know of service](https://edstevensdba.wordpress.com/2011/03/19/ora-12514/)

- `schema` and `user`: oracle里`schema`基本等同于user，创建user时自动创建同名schema，oracle还有一个`create schema`语句，但该语句用于批量创建table/view并grant权限，并不创建schema。默认情况下使用用户A连接，默认schema为A，但是用户A可以连接schema B，使用`alter session set current_schema`可更改当前schema
- `Database` : A collection of physical operating system files or disk. It refers to a database system on a server. This is different from the database concept in other database systems.  In other database systems, a database belongs to an instance which is a logical database manager environment
- `database instance` or `Instance`  : An instance is a collection of some process and background process and listeners which is mounted on a database system. An instance can only mount to one database(i.e, belongs to one database). It's different from other database system(DB2 for example) concept where an instance can have many databases under it.  A database can have more than one instance. 此时需要通过`Oracle Real Application Clusters (RAC，译为“实时应用集群”)`来实现
- `instance name`: used to identified an instance. The instance name is specified by the `INSTANCE_NAME` parameter in the initialization parameter file. The instance name defaults to the `Oracle System Identifier (SID)` of the instance.
- `Oracle system identifier (SID)`: A name that identifies a specific instance of a database.
- `service` and `service name`: An Oracle database is represented to clients as a service; that is, the database performs work on behalf of clients. A database can have one or more services associated with it. The service name defaults to the `global database name`. 连接后，默认`SERVICE_NAMES`仅显示当前的service_name，查看所有的可通过`select name from V$SERVICES;`
- `global database name` or `global name`: a name comprising the database name (`DB_NAME` parameter) and domain name (`DB_DOMAIN` parameter).
- `instance` dynamically registers itself to the `listener` and provides the listener with information about the database instances and the `service handler`s available for each instance. A service handler can be a dispatcher or a dedicated server.
- `connect descriptor` that provides the location of the database and the name of the database service.
- `connect string`: A connect string includes a username and password, along with a connect identifier.
- `connect identifier` can be the connect descriptor itself or a name that resolves to a connect descriptor.
- `Transparent Network Substrate (TNS)`, a proprietary Oracle computer-networking technology, supports homogeneous peer-to-peer connectivity on top of other networking technologies such as TCP/IP, SDP and named pipes.

#### 对应关系
- instance <-> database: N to 1
- service <-> database: N to 1
- service <-> instance: N to N
- listener <-> service: 1 to N
- listener <-> instance: 1 to N

但一般安装的单机oracle，`lister - service - instance - database` 基本都是一对一的

#### storage concepts
- A `segment` is a set of extents that contains all the data for `a specific logical storage structure` within a `tablespace`. For example, for each table, Oracle allocates one or more extents to form that `table's data segment`, and for each index, Oracle allocates one or more extents to form its `index segment`. Same to `Lob segment`.

### JDBC
- `resultset`读取时, 有时必须按照列的顺序。否则会报stream closed. 这个估计跟 oracle driver有关
- oracle的`CASE THEN`和`ELSE`部分返回值需要一致，如果有null，jdbc中要用`Types.NULL`，否则可能会报类型不匹配
- SQLException: I/O Exception: Connection reset
    - Oracle 11g JDBC drivers use `java.security.SecureRandom.nextBytes(byte[])` to generate random number during login. Users using Linux have been encountering `SQLException("Io exception: Connection reset")`. The method uses `/dev/random` on Linux and on some machines which lack the random number generating hardware the operation slows down to the extent of bringing the whole login process to a halt. Ultimately the the user encounters `SQLException("Io exception: Connection reset")`.
    - `/dev/random`使用用户操作等噪音生成随机数来提高安全性，但是如果没有什么输入则该文件生成随机数会很慢。解决方法是添加JVM参数：`-Djava.security.egd=file:/dev/./urandom`

### command line tools/utilities
注意运行下列命令前一般需要设置`ORACLE_HOME`和`ORACLE_SID`，否则可能报错
- 未设置`ORACLE_HOME`会报错：SP2-0750: You may need to set ORACLE_HOME to your Oracle software directory
- 未设置`ORACLE_SID`会报错：ORA-12162 TNS:net service name is incorrectly specified

- `oerr ora 12514`查看对应error code的详细描述及解决方案
- `lsnrctl`TNS listener控制工具
       - `lsnrctl status`
- `tnsping`
- `sqlplus`
    - sqlplus执行文件可使用 @xxx.sql, 该sql脚本可添加sqlplus控制命令，比如在xxx.sql文件末尾加上exit就会自动退出
    ```bash
    sqlplus /
    Enter user-name: sys as sysdba
    Enter password:
    ```
    - `sqlplus  user/password`，如果遇到ORA-28001: the password has expired:
        - 按上面的方法登陆，会提示更改密码
        - 取消时间限制：`ALTER PROFILE DEFAULT LIMIT PASSWORD_LIFE_TIME UNLIMITED;`
        - 解锁用户：`alter user 用户名 account unlock;`

### Oracle version
Oracle 12c共两个release
- release 1: 12.1.0.1，12.1.0.2。已经不再支持
- release 2: 12.2.0.1，仍在支持

oracle在`12.2.0.1`没有发布新版本，而是直接发布了`18.1.0`，即`oracle 18c`，为当前最新版本

### SQL/PLSQL symbol table and symbol lookup
确定`a.b.c`代表的符号含义
- 使用符号表/嵌套scope
- 穷举

- 同一个符号，仅保存一份实例
    - 对于`declaration`和`definition`分离的语言，如plsql，也要用同一符号处理，否则一旦分离，会让整个resolve框架很复杂，容易出错，比如同样的名字两处分别找到了不同的符号，在后续处理时会将问题复杂化，很难推理
- Symbol resolve和基于resolve上的应用，比如将AST节点跟symbol关联（标记过程），是两件事情
    - 如果合二为一个TypeResolver，则前面的“仅保存一份实例”不好满足
    - A依赖B，在resolve A时，同时会resolve B，之后在直接resolve B就会重新创建一个符号，把之前的符号冲掉了，这里也可以做判断，但是整体逻辑会复杂的多
    - 可将lazy load／metaOnly部分做的事情抽离出来
- 内置和非内置符号在一起处理，分开处理会导致概念不一致
    - 比如数据库的内置和非内置分离，会导致代码中逻辑上存在两个不相干的DB，导致代码复杂和冗长，对于一些逻辑处理起来很麻烦
    - 对于内置和非内置交叉的部分，比如Oracle的`PUBLIC`下既有内置也有非内置符号，而内置为固定的可以提前处理好，非内置则是不同的库有不同的内容，此时即使复制也要保持概念一致，否则也会出现前面的问题
    - 如果能够不在架构／概念上区分内置和非内置，比如直接连接数据库获取所有对象信息，则问题要简单的多。
- 统一符号搜索接口，符号搜索逻辑跟语言实际情况保持一致
    - PLSQL使用`identifier`唯一标识一个`symbol`，嵌套`scope`的同名`identifier`会覆盖之前定义的符号，注意这里不限制类型，变量跟上层的函数同名同样覆盖上面的函数定义，参考下面的例子。像java语言就不仅通过名称来区分，通过语法结构就能区分是否为函数调用，因此就算跟变量同名也能正确解析。
        ```sql
        create or replace function ff(v int) return number as begin return v; end;
        -- PLS-00222: no function with name 'FF' exists in this scope
        create or replace function f(ff int) return number as begin return ff(1); end;
        -- 由于SQL和PLSQL是两个子系统，下面的SQL语句中的t并没有被函数f的参数t覆盖
        create or replace function f(t int) return number as begin insert into t values(1); return 1; end;
        ```
    - 因此整个嵌套`scope`的resolve对象过程区分函数非函数会导致整个符号搜索流程跟实际流程不符，oracle下是由内而外根据当前信息去搜索，而区分后的流程是，按函数从内而外搜索一次，再按非函数搜索一次，或者是相反的顺序（这是由于plsql语言的模糊性，无参数的subprogram可以带括号也可以不带，数组访问跟函数调用同样都使用括号）
    - Oracle的`SQL`和`PLSQL`是两个子系统，resolve的方式有差异，嵌入到`PLSQL`的SQL（oracle中称为`PL/SQL Static SQL`）被送到SQL子系统处理并resolve，无法resolve的再拿到`PLSQL`子系统resolve，因此列名优先于`PLSQL`内定义的变量或参数
    - oracle的`ADT`的`constructor`不参与符号搜索，即不能使用`type_name.type_name(xxx)`的方式引用构造函数，因此要单独处理
    - `type body`的函数必须在type中定义，不能额外新增
    - `package body`里可以定义package里没有的subprogram，但是是私有的，外部不能访问
    - `trigger`是一个对象，但不参与符号搜索
    - `synonym`是顶层对象，按其实际情况处理可简化符号搜索过程，而非写死的目标符号
    - 自定义类型作为列类型，如要在SQL中引用其`attribute/method`，则需要表带有`alias`，并通过`alias.column.attribute/method`的方式引用
        - 参考`Qualifying References to Attributes and Methods`
    - SQL中的符号搜索也是从内而外，但是如果某个表是qualified，那么在遇到qualified的符号时也会搜索这种情况：
        - 参考`Avoiding Inner Capture in SELECT and DML Statements`中的示例，在从内层query搜索`hr.tab2.a`时，会考虑该符号为owner qualified的情况（因为from表为qualified的），在找不到时才会向上找
    - `create index idx on foo_sym(b)`时一定是表或view，不可能是`synonym`
- `Symbol`通过`scope`串联起来，向上串联，通过define来保证向下查询。两者可以拆分。在即需要保持符号串联，又不希望当前resolve的对象放到符号树时，可仅设置`scope`但不define
- SQL 语言
    - SQL语言跟PLSQL的差别是，SQL仅引用外部符号，只有表列是需要放在query内的，但其本身并不定义符号
    - from clause部分都应该为table reference，以记录真实符号信息（如实际符号为synonym的情况，是否带着schema等）
- collection类型
    - package中定义的collection类型跟本地或外部定义的相同类型并不兼容：A collection type defined in a package specification is incompatible with an identically defined local or standalone collection type

如何确定某个`a.b.c`代表的符号是否为顶层符号
- 判断最外层的`a`代表的符号，是否为owner，如果是则是`fully qualified`对象
- 否则看其scope是否为owner，如果是则确定其为顶层对象且不是`fully qualified`，否则不是顶层对象

相关资料
- PLSQL的`Scope and Visibility of Identifiers`章节和`PL/SQL Name Resolution`章节
- SQL的resolve参考`How Oracle Database Resolves Schema Object References`

### SQL reference
- `ROWNUM`从1开始

#### identifier and quote
带quote的内置函数同名标识符，不搜索内置函数。从下面的UID可看出，不带quote的内置函数同名标识符不搜索列（或优先搜索内置函数）
```sql
select CURRENT_DATE from dual;
select "CURRENT_DATE" from dual; -- 报错
```

UID不能作为列名，但是quote后就可以。而Oracle下不加quote等同于大写，单从这句话来看下面的“报错SQL”不应该报错，所以内部对quote和非quote是做了区分处理的。ROWNUM的结果跟UID一致
```sql
drop table test_tab;
create table test_tab(UID number); -- 报错
create table test_tab("UID" number);
insert into test_tab values(199);
select UID, "UID" from test_tab;
```
查询结果
```
       UID        UID
---------- ----------
         5        199
```

#### data types
- NUMBER(p,s)
    - `p` is the precision, or the total number of significant decimal digits, where the most significant digit is the left-most nonzero digit, and the least significant digit is the right-most known digit.
    - `s` is the scale, or the number of digits from the decimal point to the least significant digit.
        - Positive scale is the number of significant digits to the right of the decimal point to and including the least significant digit.
        - Negative scale is the number of significant digits to the left of the decimal point, to but not including the least significant digit.
        - 注意scale是可以大于precision的，其表示范围仍然可以通过上述定义推论出来

#### pivot/unpivot clause
1. `pivot：rotate` rows into columns, use column value as new column name
- 以pivot列（pivot_clause中没指定的列）为基准，对其他列做行列转换，这部分列一部分参与group by 并生成结果列（pivot_in里的列），另一部分列参与aggregate。结果列的顺序为，pivot列(内部顺序取决于table／subquery)，pivot_in列（内部顺序为指定顺序）。如果又多个aggregate列，则需要跟pivot_in列（在前）做笛卡尔积，形成新的列名
```sql
create table orders(id int, omode varchar(100), paymod varchar(100), val int);
insert into orders values(1, 'online', 'cash', 10);
insert into orders values(2, 'online', 'qcode', 12);
insert into orders values(1, 'offline', 'cash', 20);
insert into orders values(2, 'offline', 'qcode', 22);
insert into orders values(3, 'offline', 'qcode', 23);
insert into orders values(1, 'store', 'cash', 30);
insert into orders values(2, 'store', 'cash', 32);
insert into orders values(3, 'store', 'qcode', 33);
select * from orders b pivot(sum(b.val), count(1) cnt for(omode, paymod) in (('online','cash') on_cash, ('offline', 'qcode') as off_qcode)) a;

        ID    ON_CASH ON_CASH_CNT  OFF_QCODE OFF_QCODE_CNT
---------- ---------- ----------- ---------- -------------
         1         10           1                        0
         2                      0         22             1
         3                      0         23             1
```

2. `unpivot`：rotate columns into rows（descriptor columns and measure columns)
- unpivot_clause给出measure columns
- for_clause给出descriptor columns
- unpivot_in给出measure columns值的来源
    - 给出的列的列名作为descriptor column的值（也可通过as literal给出其他值），列的值为measure列的值
    - 每个in元素列的个数需要跟measure columns一致
    - 每个in元素列的alias个数需要跟descriptor columns一致
```sql
create or replace view orders_pivot as select * from orders b pivot(sum(b.val) for(omode, paymod) in (('online','cash') on_cash, ('offline', 'qcode') as off_qcode)) a;
select * from orders_pivot unpivot include nulls ((sum,tot) for (s, c) in ((on_cash, on_cash_cnt) as ('onelineA', 'cash'), (off_qcode, off_qcode_cnt) as ('offline', 'qcode')));
        ID S        C            SUM        TOT
---------- -------- ----- ---------- ----------
         1 onelineA cash          10          1
         1 offline  qcode                     0
         2 onelineA cash                      0
         2 offline  qcode         22          1
         3 onelineA cash                      0
         3 offline  qcode         23          1
```

#### model clause
The `model_clause` lets you view selected rows as a multidimensional array and randomly access cells within that array.

When using the `model_clause` in a query, the `SELECT` and `ORDER BY` clauses must refer only to those columns defined in the `model_column_clauses`.

The model_column_clauses define and classify the columns of a query into three groups: `partition columns`, `dimension columns`, and `measure columns`.

#### Global Temporary table
- transaction based：`ON COMMIT DELETE ROWS`
- session based：`ON COMMIT PRESERVE ROWS`

#### PUBLIC
`PUBLIC`并不是一个实体的schema，但引用相关对象是可使用`"PUBLIC".synonym_name`的形式，只有`synonym`和`database link`可以是`PUBLIC`的

#### dblink
A database link is a `schema object` in one database that enables you to access objects on another database...If you omit `PUBLIC`, then the database link is private and is available only to you. 创建private database link时不能指定`schema name`.

A database link is a connection from the Oracle database to another remote database. The remote database can be an Oracle Database or any ODBC compliant database such as SQL Server or MySQL.

dblink名称可取的值受`GLOBAL_NAMES`参数影响，如果为`TRUE`则必须跟目标database name一致（后面可跟`domain name`和`connection qualifier`）。Using `connection qualifier`s, you can create multiple database links to the same database. 这个值用来区分不同的instance，不一定要跟instance name一致。

`tnsnames.ora` is located in the directory `/NETWORK/ADMIN/` under `ORACLE_HOME`. 存放在client端，存储配置好的remote信息，每个remote信息可命名为`connect identifier`（可能跟`service name`相同），在连接时可以使用，如`sqlplus scott/tiger@larry`

### package
A package is a schema object that groups logically related PL/SQL types, variables, constants, subprograms, cursors, and exceptions. A package always has a `specification`, which declares the `public items` that can be referenced from outside the package. body中可以有`private items`、`initialization part`和`exception-handling part`.

- 带有`cursor`或`subprogram`的`pacakge`必须有`package body`
- `package body`内不能重复声明`package`中的`public variables`(实际可声明，但是不能在代码中引用，否则会报错，应该是编译系统未检测该情况)，但可以定义`private variables`
- 函数声明和定义需要完全一致：The headings of corresponding subprogram declarations and definitions must match word for word, except for white space.
- public items如变量或cursor可以在package中直接初始化
- 对于非`SERIALLY_REUSABLE`包，package 状态在当前session内都会保持。但对于`SERIALLY_REUSABLE` package, the work unit is a server call. 变量／cursor的值仅在当前work unit有效
- SQL（不在PLSQL内）不能直接访问package里的variable，但可通过package function访问
- When a session references a package item, Oracle Database instantiates the package for that `session`. Every `session` that references a package has its own instantiation of that package.
    - 常量赋值初始值: 常量的值不一定是literal，可能是某个变量
    - 变量赋值初始值
    - 执行initialization part

### PLSQL reference
#### for loop statement
- `FOR index IN [ REVERSE ] lower_bound..upper_bound LOOP`. The index of a `FOR LOOP` statement is **implicitly** declared as a variable of type `PLS_INTEGER` that is local to the loop.
- The `cursor FOR LOOP` statement **implicitly** declares its loop index as a `%ROWTYPE` record variable of the type that its cursor returns. This record is local to the loop and exists only during loop execution.
- `cursor LOOP`时，该cursor由`LOOP`自动打开，并在结束时关闭

#### cursor
oracle cursor fetch 不抛出异常，而是通过%NOTFOUND判断

cursor可用于更新，使用FOR UPDATE，where current of xxx

#### subprogram parameters
parameter mode
- `IN`: passed by reference 但是为只读，不可修改
- `OUT`: 默认passed by value(除非给定NOCOPY，此时可能为reference)
    - 此时subprogram内操作的actual parameter跟传入的参数在不同内存地址，在返回时才拷贝回去
    - 如果是record类型，在subprogram内必须初始化才能使用（无论传入的变量是否初始化过），否则报Reference to uninitialized composite
- `IN OUT`: 同OUT

### commonly used sqls
```sql
-- parameters
SHOW PARAMETER SERVICE_NAME;
select * from GLOBAL_NAME;
SELECT * FROM V$PARAMETER WHERE NAME='global_names';
ALTER SESSION SET NLS_DATE_FORMAT = 'dd/mm/yyyy'
SELECT value FROM NLS_SESSION_PARAMETERS WHERE  PARAMETER = 'NLS_DATE_FORMAT'
SELECT value FROM NLS_DATABASE_PARAMETERS WHERE  PARAMETER = 'NLS_DATE_FORMAT'

-- create user
CREATE USER TEST IDENTIFIED BY TEST;
GRANT CONNECT TO test;
GRANT CREATE SESSION TO test;
GRANT UNLIMITED TABLESPACE TO test;
GRANT ALL PRIVILEGES TO TEST;
```

## transaction and jdbc
- `JDBC`的`connection`默认为`autocommit=true`的，`close`方法没规定如何处理`last transaction`，跟数据库有关，比如
    - MySQL中`autocommit`参数控制`InnoDB`事务行为，默认开启。其JDBC客户端的`autocommit`特性底层也通过该server端参数控制
- 事务启动（参考`sql reference - SET TRANSACTION statement`)。A transaction implicitly begins with any operation that obtains a TX lock:
    - When a statement that modifies data is issued
    - When a `SELECT ... FOR UPDATE` statement is issued
    - When a transaction is explicitly started with a `SET TRANSACTION` statement or the `DBMS_TRANSACTION` package
- 事务提交（参考`SQL reference - COMMIT statement`）。
    - 显示提交
    - Oracle Database issues an implicit `COMMIT` under the following circumstances:
        - Before any syntactically valid data definition language (`DDL`) statement, even if the statement results in an error
        - After any data definition language (`DDL`) statement that completes without an error
    - 正常断开连接时，客户端工具会自动提交，但这个不是oracle db的行为
- oracle db本身没有`autocommit`的概念，只有客户端告诉oracle db什么时候`commit`（除了部分implicit commit）。`autocommit`是客户端的属性，开启后在每条语句执行后执行一个commit语句，比如:
    - sqlplus：使用`set autocommit on/off`、`show autocommit`
    - oracle sql developer：`Perferences -> 数据库 -> 高级 -> 自动提交`
    - `JDBC`：使用Connection的`autocommit`设置
- 关闭JDBC Connection时如何处理`last transaction`（参考`Oracle® Database JDBC Developer’s Guide - Committing Changes`）
    - 关闭连接时Oracle JDBC implicitly calls `commit()`，即使设置了`Connection.autocommit(false)`. If the auto-commit mode is disabled and you close the connection without explicitly committing or rolling back your last changes, then an implicit `COMMIT` operation is run.
- 异常退出连接时，rollback `last transaction`：If you do not explicitly `commit` the transaction and the program terminates abnormally, then Oracle Database `rolls back` the last uncommitted transaction.
- 事务内某个`DML`失败后被`catch`，前面的语句不会被`roll back`，这应该就是`statement-level rollback`（参考`PLSQL reference - Implicit Rollbacks`）
    - Before running an `INSERT`, `UPDATE`, `DELETE`, or `MERGE` statement, the database marks an implicit `savepoint` (unavailable to you). If the statement fails, the database rolls back to the savepoint.
    - 如果没被catch，文档上写的不会做任何`rollback`，但在sql developer中整个事务是被`rollback`的

## query execution order
`FROM` `JOIN` `WHERE` `GROUP BY` ... `SELECT`. When using `group by`, only the fields remaining from the previous step are available. 所以在`group by`是不能使用column alias的
