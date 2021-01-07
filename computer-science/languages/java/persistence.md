## persistence layer
The layer that separates the `business logic` and the `database code` is the persistence layer, which keeps the application independent of the underlying database technology. The `persistence layer` encapsulates the way in which the data is stored and retrieved from a relational database.

`Object-relational mapping (ORM)` has emerged as a solution to what is sometimes called the `object-relational impedance mismatch`...including Hibernate, MyBatis, JPA

## object-relational impedance mismatch
`object-relational impedance mismatch`: a set of conceptual and technical difficulties that are often encountered when a relational database management system (RDBMS) is being served by an application program (or multiple application programs) written in an object-oriented programming language or style, particularly because objects or class definitions must be mapped to database tables defined by a relational schema.

`Objects` (instances) reference one another and therefore form a `graph` in the mathematical sense (a network including loops and cycles). `Relational schemas` are, in contrast, `tabular` and based on `relational algebra`, which defines linked heterogeneous tuples (groupings of data fields into a "row" with different types for each field).

Mismatches
- Object-oriented concepts
- Data type differences
- Structural and integrity differences
- Manipulative differences
- Transactional differences

Solving impedance mismatch
- Alternative architectures: 用其他数据库，如NoSQL or XML database.
- Minimization: OO language is used to model certain relational aspects at runtime rather than attempt the more static mapping. Frameworks which employ this method will typically have an analogue for a tuple, usually as a "row" in a "dataset" component or as a generic "entity instance" class, as well as an analogue for a relation.
- Compensation: reflection and/or code generation are utilized to provide framework support, automation of data manipulation and presentation patterns

## Database normalization
`Database normalization` is the process of structuring a relational database in accordance with a series of so-called `normal forms` in order to reduce `data redundancy` and improve `data integrity`.

