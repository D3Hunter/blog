## ldap
`LDAP` stands for `Lightweight Directory Access Protocol`. As the name suggests, it is a lightweight client-server protocol for accessing directory services, specifically X. 500-based directory services. 可用于用户认证

The `LDAP` API references an LDAP object by its `distinguished name (DN)`. A `DN` is a sequence of `relative distinguished names (RDN)` connected by commas. An `RDN` is an attribute with an associated value in the form `attribute=value`; normally expressed in a UTF-8 string format.

- CN = Common Name
- OU = Organizational Unit
- DC = Domain Component

### LDAP Data Interchange Format
The LDAP Data Interchange Format (LDIF) is a standard plain text data interchange format for representing `LDAP directory content and update requests`.

LDIF conveys directory content as a set of records, one record for each object (or entry). It also represents update requests, such as Add, Modify, Delete, and Rename, as a set of records, one record for each update request.

Each content record is represented as a group of attributes, with records separated from one another by blank lines. The individual attributes of a record are represented as single logical lines (represented as one or more multiple physical lines via a line-folding mechanism), comprising "name: value" pairs.

