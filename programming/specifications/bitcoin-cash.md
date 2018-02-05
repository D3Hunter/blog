BCH从`Bitcoin ABC version 0.14.2`版本开始分离出来

Bitcoin ABC has published version 0.16.0 which contains an updated Difficulty Adjustment Algorithm (DAA).  

The Bitcoin Cash EDA was, according to its chief scientist, developed to take hash power away from Core in “bursts”. 但结果并不怎么好

当多个币种拥有相同的pow算法时，币种间算力来回切换会导致网络的hashrate的波动，如btc/bch


### EDA
EDA调整难度的时机：
- Median Time Past of the current block and the Median Time Past of 6 blocks before has to be greater than 12 hours.
    - Median Time Past (MTP) is just the median of the last 11 blocks(前11个块（不包括当前块）的中位数)。这是由于后面的block的timestamp可能小于前面的block。
- If so, it gets 20% easier to create proof of work. In other words, miners can find blocks 20% easier.
2017/7/6 于0.14.2版本加入，即分叉后第一个版本

主要避免BCH因BTC的难度而没有人挖矿而死掉（或者向BTC抢hashrate）

这个文章描述的比较清楚https://medium.com/@jimmysong/bitcoin-cash-difficulty-adjustments-2ec589099a8e

### DAA
November 13, 2017开始使用，`0.16.0版本`
从504031块，后续的快都采用DAA

To compute the difficulty, we begin with the three topmost blocks, and choose the one with the median timestamp of the three.  Next, the process is repeated with blocks 144, 145, and 146 (blocks of 144-146 height less than the current) and a median timestamp block is again chosen from those 3.
From these 2 blocks roughly 144 blocks apart, we define W as the amount of work done between the blocks, and T as the elapsed time between the blocks.  A high-low filter is applied so that T has maximum value of 2 days and a minimum value of .5 days.  This prevents difficulty from changing too abruptly. (Normally 144 blocks takes approximately 1 day).We can then compute:
Wn = W * ExpectedBlockTime / T
G = (2^256 / Wn) - 1

G is our difficulty target.
参考https://www.bitcoinabc.org/november
