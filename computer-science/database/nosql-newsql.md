### NoSQL
NoSQL was originally coined as “No support for SQL” but later on evolved to “Not only SQL” once users realized that NoSQL databases have to coexist alongside the SQL databases rather than replace them entirely.

为了可用性和scalability，牺牲一定的consistency。the queries and access patterns优先，而不像RDBMS的normalized schema

大型网站遇到了RDBMS难以克服的缺陷，即糟糕的海量数据处理能力及僵硬的设计约束，NoSQL应运而生。NoSQL 放弃了RDBMS的两大基础：结构化查询（SQL）和事务一致性（ACID）

These databases were designed using `CAP Theorem` as the backbone. This theorem states that between `Consistency`, `Availability`, and `Partition Tolerance`（分区容错）, only two of the three aspects can be achieved at any given time.

### NewSQL
NewSQL is a class of relational database management systems that seek to provide the scalability of NoSQL systems for online transaction processing (OLTP) workloads while maintaining the ACID guarantees of a traditional database system.

Many enterprise systems that handle high-profile data (e.g., `financial` and `order` processing systems) are too large for conventional relational databases, but have transactional and consistency requirements that are not practical for NoSQL systems. The only options previously available for these organizations were to either purchase more powerful computers or to develop custom middleware that distributes requests over conventional DBMS. Both approaches feature high infrastructure costs and/or development costs. NewSQL systems attempt to reconcile the conflicts.

Most current NewSQL databases are based on Google’s `Spanner` database and the theories in academic papers such as Calvin: `Fast Distributed Transactions for Partitioned Database Systems` from Yale. `TiDB`, `CockroachDB`, `FaunaDB`, `Vitess` are a few of the leading NewSQL databases.

NewSQL databases come in two distinct flavors.
- The first flavor simply provides an automated data sharding layer on top of multiple independent instances of monolithic SQL databases. `Vitess`、`Citus` (aka Azure DB for PostgreSQL – Hyperscale)
- The second flavor includes the likes of `NuoDB`, `VoltDB` and `Clustrix` that built new distributed storage engines with the goal of keeping the single logical SQL database concept intact.

