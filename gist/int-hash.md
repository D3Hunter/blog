32b int hash方法
`hashmap.java`中的方法
```
static int hash(int var0) {
    var0 ^= var0 >>> 20 ^ var0 >>> 12;
    return var0 ^ var0 >>> 7 ^ var0 >>> 4;
}
```