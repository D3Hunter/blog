### Greenplum(GPDB)
Pivotal’s Greenplum Database (GPDB) is a massively parallel processing (MPP) analytics database. GPDB adopts a shared-nothing computing architecture with two or more cooperating processors.

### HAWQ
HAWQ is “HAdoop With Query” and is basically a port of Greenplum to store data natively in HDFS.

HAWQ is a Hadoop native SQL query engine that combines the key technological advantages of MPP database with the scalability and convenience of Hadoop. HAWQ reads data from and writes data to HDFS natively.

### Orca
Orca is the new query optimizer for Pivotal data management products, including GPDB and HAWQ. Orca is a modern top-down query optimizer based on the Cascades optimization framework.

### MPP DBMS
`MPP` stands for `Massive Parallel Processing`, this is the approach in `grid computing` when all the separate nodes of your grid are participating in the coordinated computations. `MPP DBMSs` are the database management systems built on top of this approach.
- times faster than in traditional SMP RDBMS systems
- scalability, because you can easily scale the grid by adding new nodes into it.
- the data in these solutions is usually split between nodes (sharded)
- most of the MPP DBMS solutions are shared-nothing and work on DAS(Direct-attached storage) storage or the set of storage shelves shared between small groups of servers. This approach is used by solutions like `Teradata`, `Greenplum`, `Vertica`, `Netezza` and other similar ones.

### SMP DBMS(Symmetrical Multiprocessor)
- SMP can have hundreds of CPUs, they are most commonly configured with 2, 4, 8 or 16. Memory is the primary constraint on SMP databases.
- SMP databases can run on more than one server, though they will share other resources; this is known as a called a clustered configuration.
- `Oracle` and `Sybase` run on SMP databases.

