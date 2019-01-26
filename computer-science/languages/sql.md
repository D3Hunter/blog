计算`foreign key`和`primary／unique key`的执行顺序，可以从表的依赖图上先序遍历；另一种简单方式时，把所有`foreign key`放后面即可。

the default is `INNER JOIN` if you just specify `JOIN`.

`CARTESIAN JOIN`: The `CARTESIAN JOIN` is also known as `CROSS JOIN`. In a `CARTESIAN JOIN` there is a join for each row of one table to every row of another table.

By the SQL standard, a `foreign key` must reference either the `primary key` or a `unique key` of the parent table. If the primary key has multiple columns, the foreign key must have the same number and order of columns.

Any `primary key` must be `unique` and `non-null`.

If you don't specify an `ORDER BY`, then there is NO ORDER defined.

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

