## misc
`Turing completeness` in `declarative SQL` is implemented through `recursive common table expressions`. Unsurprisingly, `procedural extensions to SQL` (`PLSQL`, etc.) are also `Turing-complete`.

## ISO & IEC
`ISO` (the International Organization for Standardization) and `IEC` (the International Electrotechnical Commission) form the specialized system for worldwide standardization. ISO and IEC technical committees collaborate in fields of mutual interest. In the field of `information technology`, ISO and IEC have established a joint technical committee, `ISO/IEC JTC 1`.

### ISO/IEC 9075
Technical Committee : ISO/IEC JTC 1/SC 32 Data management and interchange

ISO/IEC 9075: Information technology - Database languages - SQL

The SQL language was first formally standardized in 1986 by the American National Standards Institute (ANSI) as SQL 1986. Subsequent versions of the SQL standard have been released by ANSI and as International Organization for Standardization (ISO) standards:
- SQL 1986
- SQL 1989
- SQL 1992
- SQL 1999
- SQL 2003
- SQL 2006
- SQL 2008 (current SQL standard)
- SQL:2011
- SQL:2016

SQL标准的文档开源但不免费，需要付费下载，参考：https://webstore.ansi.org/Standards/INCITS/INCITSISOIEC907520112012-1506971

#### SQL Conformance Levels
The SQL standard defined different conformance levels so that vendors can claim conformance to a subset of the standard.

`SQL-92` defines three conformance levels: `entry`, `intermediate` and `full`.

Starting with `SQL:1999` all features are enumerated and either flagged mandatory or optional. As a bare minimum, conforming systems must comply with all mandatory features, which are collectively called `Core SQL`. Beyond Core SQL, vendors can claim conformance on a feature-by-feature basis.

#### Parts
Since `SQL:1999` the standard is divided into several parts numbered from `1` though `14` (as of `SQL:2016`). Some of them were never released (`5-8`, `12`), others never became mainstream. Leaving the meta-part (`part 1`) aside, only `part 2` (the SQL language), `part 11` (Information Schema) and `part 14` (XML) became widely implemented. Part 15 (MDA) was just released so it is too early to see whether it becomes widespread adopted or not.

- Part 1 - Framework
    - A rough overview and some definitions of commonly used terms. The 2011 version of this part is available for free from ISO (look for SQL).
- Part 2 - Foundation
    - Defines most of the SQL language (other parts extend it—e.g., for XML functionality).
- Part 3 - Call-Level Interface (SQL/CLI)
    - Describes C and COBOL APIs to access SQL databases.
- Part 4 - Persisted Stored Modules (SQL/PSM)
    - Defines a language used for server-side programming (“stored procedures”).
- Part 5 - Host Language Bindings (SQL/Bindings)
    - Merged into part 2 with SQL:2003 (withdrawal notice).
- Part 6 - Global Transaction Support (SQL/Transaction)
    - Never released(?)
- Part 7 - Temporal (SQL/Temporal)
    - Never released. Temporal support was eventually added to SQL:2011 part 2.
- Part 8 - Extended Object Support
    - Never released. Content absorbed into other parts (notice).
- Part 9 - Management of External Data (SQL/MED)
    - Defines mechanisms to access data stored outside the database.
- Part 10 - Object Language Bindings (SQL/OLB)
    - Defines how to embed SQL statements into Java programs. This is not JDBC, which treats SQL statements as strings (“dynamic SQL”).
- Part 11 - Information and Definition Schemas (SQL/Schemata)
    - Defines INFORMATION_SCHEMA and DEFINITION_SCHEMA, which were covered in part 2 prior SQL:2003.
- Part 12 - Replication (SQL/Replication)
    - Never released.
- Part 13 - Routines and Types Using the Java Programming Language (SQL/JRT)
    - Defines how to run Java inside the database.
- Part 14 - XML-Related Specifications (SQL/XML)
    - Defines the XML data type and methods to work on XML documents. Appeared with SQL:2003.
- Part 15 - Multi dimensional arrays (SQL/MDA)
    - First appeared in 2019. See ISO.
- Part 16 - Property Graph Query (SQL/PGQ)
    - In progress. Embeds parts of the new GQL-Standard in SQL. Probably released in 2020 or 2021.

#### Resources
- SQL-99 Complete(only covers Core SQL:1999). https://crate.io/docs/sql-99/en/latest/
- SQL:2011 Part 1: https://standards.iso.org/ittf/PubliclyAvailableStandards/c053681_ISO_IEC_9075-1_2011.zip

##### Books
- SQL For Smarties
- Trees and Hierarchies
- Thinking in Sets
- SQL Puzzles and Answers
- SQL Performance Explained

### ISO/IEC TR 19075
ISO/IEC TR 19075: Information technology — Database languages — SQL Technical Reports

Technical Committee: ISO/IEC JTC 1, Information technology, Subcommittee SC 32, Data management and interchange.

#### Parts
- Part 1: XQuery Regular Expression Support in SQL
- Part 2: SQL Support for Time-Related Information
- Part 3: SQL Embedded in Programs using the JavaTM programming language
- Part 4: SQL with Routines and types using the JavaTM programming language
- Part 5: Row Pattern Recognition in SQL
- Part 6: SQL support for JavaScript Object Notation (JSON)
- Part 7: Polymorphic table functions in SQL
- Part 8: Multi-dimensional arrays (SQL/MDA)
- Part 9: SQL TR OLAP

