### row fetching algorithm
https://malisper.me/postgres-bitmap-scans/
- sequential scan
    - a sequential scan is always possible.
    - in some cases a sequential scan is actually faster than the other options available. When reading data from disk, reading data sequentially is usually faster than reading the data in a random order.
- index scan
    - Most of the time when people talk about indexes in Postgres, they are referring to b-tree indexes.
    - the nodes in the b-tree are sorted by the indexed column
    - There are two main types of types of queries that can be sped up by an index scan.
        - The first type are queries that contain a filter that is either a range filter or an equality filter on the indexed column.
        - The other main type of queries sped up are those that sort by the indexed field.
    - Although indexes are useful because they allow Postgres to perform index scans, there are two main reasons why you wouldn’t want to create the index.
        - First of all, they take up additional space.
        - Additionally, indexes increase the amount of I/O that has to be performed in order to insert a row into the table.
    - One major restriction with `regular index scans` is that they can only use a single index.
- bitmap index scan(并非物理存在的索引，而是每次query时单独创建)
    - A bitmap index scan is a way of combining multiple indexes.
        - A bitmap index scan works by using the first index to locate all of the rows that satisfy the first filter
        - then using the second index to locate all indexes that satisfy the second filter
        - then intersecting the results to get the locations of all rows in the table that satisfy both filters.
        - From there Postgres will fetch the rows from the physical table `in the order the rows are in the physical table.`
    - Fetching the rows from the table in the physical order they are in the table has several advantages.
        - 如果结果集较大，bitmap scan类似sequencial scan，在一些情况下比index scan要快，即使只有一个index（磁盘线性IO性能优于随机IO）
    - One downside to fetching rows in order of their physical location in the table is that Postgres loses any information about the sort order.

### join algorithm
- `nested loops` are the most basic way for Postgres to perform a join which is similar to how a sequential scan is the most basic way to retrieve rows from the table.
    - A naive nested loop join is `O(M\*N)`
    - A nested loop is the only join algorithm Postgres has that can be used to process any join!
    - There is a slight variation of a nested loop, sometimes called an `index join`, that is much more efficient, but isn’t as general.
        - This is only `O(M\*log(N))` and is usually much more efficient than the `O(M\*N)` naive nested loop.
- hash join is usually the fastest.
    - The main downside is hash joins only work where the join condition is an `equality condition`.
    - A hash join is only O(M+N) in the size of the inputs to the join.
    - The other major case when a hash join won’t be the preferred join algorithm is when Postgres thinks the hash table needed for the hash join `won’t fit in memory`
- merge join
    - Similar to a hash join, a merge join only works on joins where the join condition is an `equality filter`.
    - Although a merge join is `O(N\*log(N) + M\*log(M))`, due to the need to sort the inputs
    - If one or both of the inputs to the merge join are already sorted by the field being joined on, Postgres can skip the sort step ... under some circumstances, makes the merge join faster than the hash join.

