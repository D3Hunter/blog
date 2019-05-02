#### Background
Apache Calcite is a dynamic data management framework.

It contains many of the pieces that comprise a typical database management system, but omits some key functions:
- storage of data
- algorithms to process data
- a repository for storing metadata.

Calcite intentionally stays out of the business of storing and processing data. mediating between applications and one or more data storage locations and data processing engines. Many projects and products use Apache Calcite for:
- SQL parsing
- query optimization
- data virtualization/federation
- materialized view rewrite.

Calcite can handle any data source and data format, including in-memory objects and JDBC. You can define you own adapters to support you own data source or data format.

Alibaba’s `MaxCompute` big data computing and storage platform uses Calcite for cost-based query optimization.

#### Concepts
`schema adapter`: allows Calcite to read particular kind of data, presenting the data as tables within a schema.

`Relational algebra`:  is at the heart of Calcite. Every query is represented as a tree of relational operators. You can translate from SQL to relational algebra, or you can build the tree directly.

`Execute plans`: represent the steps necessary to execute a query.

Stage of Query execution
- Parse
- Validate
- Optimize
- Execute

#### Components of Calcite
- Catalog: defines metadata and namespaces
- Sql parsing: using a JavaCC generated parser
- Sql validation: against database metadata
- Sql optimization: Logical plans are optimized and converted into physical expressions.
    - optimization operations:
        - prune unused fields
        - merge projections
        - convert subqueries into join
        - reorder joins
        - push down projections
        - push down filters
    - Rule based optimization
    - Cost based optimization
- Sql generator: Converts physical plans to SQL

https://www.slideshare.net/JordanHalterman/introduction-to-apache-calcite
