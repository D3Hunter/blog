As others pointed out, in order to apply the bitwise operations, we should rethink how integers are represented in computers -- by bits.
遇到需要使用binary操作实现的情况，需要将问题从int等类型简化到bit层来思考，然后再上推到这个int

### 求和进位
求和进位，以3位的数 + 1位举例，x3,x2,x1 + n
x   n  sum carry
0   0  0   0
0   1  1   0
1   0  1   0
1   1  0   1

由以上状态转换图得出1位求和公式：
- `x + n = x ^ n`
- carry为`x & n`
推导得到3位求和为（需要按顺序计算，避免覆盖）
- carry为 `x3 & x2 & x1 & n`
- x3 = x3 ^ (x2 & x1 & n)
- x2 = x2 ^ (x1 & n)
- x1 = x1 ^ n

### 不断递增1，到达某个数X时清零
- 如果X是2^n，那么不去处理最后的carry即可
- 否则，如X = 5，即 `1 0 1`，那么每次递增后每位都&上`~(x3 & ~x2 & x1)`

### 数位表示，横向纵向
加入有一组数需要3位表示，总共32个
1. 横向：使用32个byte/short/int来表示
2. 纵向：使用3个int（假设int为32位），每个int的最低位共同组成第一个数，次末位表示第二个数。。。。。

### 按XOR对数进行分组
如果A != B，那么(A ^ B) != 0，即A^B中至少有一位为1，从右边找到第一处，设为k，那么通过对一组数按第k为的值分组，即可将A和B分到不同的组里。
