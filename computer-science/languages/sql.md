### 计算`create table`,`foreign key`和`primary／unique key`的执行顺序
- 以`table`对象为节点（包含各种约束关系），`foreign key`为边构成依赖图，进行拓扑排序。缺点是无法处理循环外键
- 对上述节点进行细分，仍以`table`对象为节点，但从中去掉`foreign key`，这样所有节点都是独立的，没有依赖关系。`foreign key`统一放后面
- 另一种思考方式是，不以对象为节点，而以原子`sql`语句为节点，这样一个`table`对象,变成一个单纯的`create table`语句，多个`alter table`语句,以此构成依赖图，并进行拓扑排序，就可以发现前一条里说的特点

By the SQL standard, a `foreign key` must reference either the `primary key` or a `unique key` of the parent table. If the primary key has multiple columns, the foreign key must have the same number and order of columns.

Any `primary key` must be `unique` and `non-null`.

If you don't specify an `ORDER BY`, then there is NO ORDER defined.

### Table Join
- `[INNER] JOIN`: returns rows when there is a match in both tables.
- `LEFT [OUTER] JOIN`: returns all rows from the left table, even if there are no matches in the right table.
- `RIGHT [OUTER] JOIN`: returns all rows from the right table, even if there are no matches in the left table.
- `FULL [OUTER] JOIN`: It combines the results of both left and right outer joins.
- `[CARTESIAN] or [CROSS] JOIN`: returns the Cartesian product of the sets of records from the two or more joined tables.
- `NATURAL [LEFT] JOIN`: semantically equivalent to an `INNER JOIN` or a `LEFT JOIN` with a `USING` clause that names all columns that exist in both tables.
k

### JDBC
`CLOB` `NCLOB`是`text`类型需要用`setString`

### `SQL execution` is composed of two parts, the `parse` and the `execute`.
- The `parse` consists of turning the string SQL representation to the database representation.
- The `execute` consists of executing the parsed SQL on the database.

### batch writing
Batch writing has two forms, `dynamic` and `parametrized`. Parametrized is the most common, and normally provides the best benefit, as dynamic can have parsing issues.
- `Dynamic` batch writing involves chaining a bunch of heterogeneous dynamic SQL statements into a single block, and sending the entire block to the database in a single database/network access. It is not compatible with `statement caching`
    - Example dynamic SQL: `INSERT INTO EMPLOYEE (ID, NAME) VALUES (34567, "Bob Smith")......`
    - `Dynamic` batch writing does not provide any benefit, this is because `Oracle's JDBC driver` just emulates `dynamic batch writing` and executes statements one by one, so it has the same performance as dynamic SQL.
- `Parametrized` batch writing involves executing a single DML statement, but with a set of bind parameters for multiple homogenous statements, instead of bind parameters for a single statement. It is also compatible with `statement caching`
    - Example parametrized SQL: `INSERT INTO EMPLOYEE (ID, NAME) VALUES (?, ?)`
    - `MySQL` does have batch processing support though, it just requires different SQL. The `MySQL JDBC driver` does support this, but requires the `rewriteBatchedStatements=true` JDBC connect property to be set.
- 两者在不同的数据库上的性能不同，但`Parametrized batch writing`结果都挺不错

