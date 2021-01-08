### Mongo The Definitive Guide
Scaling a database comes down to the choice between `scaling up` (getting a bigger machine) or `scaling out` (partitioning data across more machines).

A database has its own permissions, and each database is stored in separate files on disk.

The shell is a full-featured JavaScript interpreter, capable of running arbitrary JavaScript programs.

On startup, the shell connects to the `test` database on a MongoDB server and assigns this database connection to the global variable `db`.

Strings do not match dates and vice versa. However, dates in the database are just stored as milliseconds since the epoch

Documents can be used as the value for a key. This is called an `embedded document`.

Another way of getting around invalid properties is to use array-access syntax: in JavaScript, `x.y` is identical to `x['y']`.

One of the basic structure checks is size: all documents must be smaller than `16 MB`.

A common mistake is matching more than one document with the criteria and then creating a duplicate "_id" value with the second parameter. The database will throw an error for this, and no documents will be updated.

Always use `$` operators for modifying individual key/value pairs.

store engine
- WiredTiger Storage Engine (Default since 3.2)
- In-Memory Storage Engine
- MMAPv1 Storage Engine (Default for versions 3.0 and earlier. Deprecated as of MongoDB 4.0)

We can eliminate the race condition and cut down on the amount of code by just sending an `upsert`

`Write concern` is a client setting used to describe how safely a write should be stored before the application continues.

db.runCommand({getLastError:1})

However, MongoDB has no joining facilities, so gathering documents from multiple collections will require multiple queries.

Deciding when to normalize and when to denormalize can be difficult: typically, `normalizing` makes writes faster and `denormalizing` makes reads faster. Thus, you need to find what trade-offs make sense for your application.

`Cardinality` is how many references a collection has to another collection.

Generally, “few” relationships will work better with `embedding`, and “many” relationships will work better as `references`

