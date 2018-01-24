### Concepts
- visibility
- mutual exclusion

### volatile and mutex
- `volatile`处理`visibility`问题，如果`write A`在`read A`前，那么这两个操作满足`happens-before`关系，但两个`write`并不是互斥访问的
- 通过mutex操作变量，即处理`visibility`问题，同时满足互斥访问
