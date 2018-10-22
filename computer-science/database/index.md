`primary`: must be unique, is an index, is (likely) the physical index, can be only one per table.

`unique`: as it says. You can't have more than one row with a tuple of this value. Note that since a unique key can be over more than one column, this doesn't necessarily mean that each individual column in the index is unique, but that each combination of values across these columns is unique.

`key`/`index`: if it's not primary or unique, it doesn't constrain values inserted into the table, but it does allow them to be looked up more efficiently.

`fulltext`: a more specialized form of indexing that allows full text search. Think of it as (essentially) creating an "index" for each "word" in the specified column.

