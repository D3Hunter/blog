- `Open Addressing` or `Closed Hasing`:
    - The use of "`closed`" vs. "`open`" reflects whether or not we are locked in to using a certain position or data structure
    - the "open" in "open addressing" tells us the index (aka. address) at which an object will be stored in the hash table is not completely determined by its hash code.
    - The "closed" in "closed hashing" refers to the fact that we never leave the `hash table`; every object is stored directly at an index in the hash table's internal array. 这种方法一般需要使用`Open Addressing`
    - [reference](https://stackoverflow.com/questions/9124331/meaning-of-open-hashing-and-closed-hashing)
- `Closed Addressing` or `Open Hashing` 相对上面的来说的
    - open hashing - in this strategy, none of the objects are actually stored in the `hash table's array`; instead once an object is hashed, it is stored in a list which is separate from the hash table's internal array.

