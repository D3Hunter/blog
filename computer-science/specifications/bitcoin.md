`Pubkey hashes` are almost always sent encoded as Bitcoin addresses, which are `base58-encoded` strings containing an address version number, the hash, and an error-detection checksum to catch typos.
She creates a standard P2PKH transaction output containing instructions which allow anyone to spend that output if they can prove they control the private key corresponding to Bob’s hashed public key. These instructions are called the pubkey script or `scriptPubKey`.
Signature scripts are also called `scriptSigs`.
Pay-To-Public-Key-Hash (P2PKH) 
P2PKH Script is a Forth-like stack-based language deliberately designed to be stateless and not Turing complete.
pay-to-script-hash (P2SH) 
The hash of the `redeem script `has the same properties as a pubkey hash—so it can be transformed into the `standard Bitcoin address format` with only one small change to differentiate it from a standard address.
As of Bitcoin Core 0.9, the `standard pubkey script `types are:
- Pay To Public Key Hash (P2PKH)
- Pay To Script Hash (P2SH)
- Multisig
- Pubkey
- Null Data

transaction fees
### Wallet
A Bitcoin wallet can refer to either a wallet program or a wallet file. 
`Wallet programs` create public keys to receive satoshis and use the corresponding private keys to spend those satoshis.
distributing public keys in order to receive satoshis and signing transactions spending those satoshis.
`Wallet programs` also need to interact with the peer-to-peer network to get information from the `block chain` and to broadcast new transactions.
#### Wallet programs
- Full-Service Wallets
- Signing-Only Wallets
    - Offline Wallets
    - Hardware Wallets
- Distributing-Only Wallets
#### Wallet Files
`Private keys` are what are used to unlock satoshis from a particular address. In Bitcoin, a private key in standard format is simply a 256-bit number, between the values:
- Wallet Import Format (WIF)
- Mini Private Key Format
`Bitcoin ECDSA public keys` represent a point on a particular Elliptic Curve (EC) defined in secp256k1.
`Loose-Key wallets`, also called “Just a Bunch Of Keys (JBOK)”, are a deprecated form of wallet that originated from the Bitcoin Core client wallet.

### Payment Processing
- Pricing Orders
- Requesting Payments
    - users paste in or manually enter an address and amount into a payment screen.
    - `bitcoin:` URIs
    - `bitcoin:` URIs encoded in a QR code
    - new payment protocol providing increased security
### Operating Modes
- Full Node
- Simplified Payment Verification (SPV)
    - only downloads the headers of blocks during the initial syncing process and then requests transactions from full nodes as needed.
    - To mitigate the latter issue, `Bloom filters` have been implemented as a method of obfuscation and compression of block data requests.
`Bitcoin Core` as a representative full node and `BitcoinJ` as a representative SPV client.
`Bitcoin Core` can be used as a `spv` when `prune=xxx` is configured

Wallet: Pruning: since 0.12

### P2P Network
The Bitcoin network protocol allows full nodes (peers) to collaboratively maintain a `peer-to-peer network` for block and transaction exchange.
- Full nodes download and verify every block and transaction prior to relaying them to other nodes.
- Archival nodes are full nodes which store the entire blockchain and can serve historical blocks to other nodes.
- Pruned nodes are full nodes which do not store the entire blockchain. Many SPV clients also use the Bitcoin network protocol to connect to full nodes.
#### Peer Discovery
In order to discover some IP addresses, they query one or more DNS names (called `DNS seeds`) hardcoded into Bitcoin Core and BitcoinJ.
- `dig seed.bitcoin.sipa.be`
`DNS seed` results are not authenticated, programs should not rely on DNS seeds exclusively.
Once a program has connected to the network, its `peers` can begin to send it `addr` (address) messages with the IP addresses and port numbers of other peers on the network, providing a fully decentralized method of peer discovery.
`Bitcoin Core` keeps a record of `known peers` in a persistent on-disk database which usually allows it to connect directly to those `peers` on subsequent startups without having to use `DNS seeds`.
- `peers.dat`
#### Connecting To Peers
- `version` -> `verack`, 类似四次挥手
- `getaddr` `addr`
- In order to maintain a connection with a peer, nodes by default will send a message to peers before `30 minutes` of inactivity. If `90 minutes` pass without a message being received by a peer, the client will assume that connection has closed.
#### Initial Block Download
Before a `full node` can validate `unconfirmed transactions` and r`ecently-mined blocks`, it must download and validate all blocks from `block 1` (the block after the `hardcoded genesis block`) to the current tip of the `block chain`. This is the `Initial Block Download (IBD) `or `initial sync`.
- `Bitcoin Core` (up until version 0.9.3) uses a simple initial block download (IBD) method we’ll call `blocks-first`.
    - `getblocks` -> `inv` then `getdata` -> `block`, repeat
    - The primary advantage of blocks-first IBD is its simplicity. The primary disadvantage is that the IBD node relies on a single sync node for all of its downloading. 
        - Speed Limits:
        - Download Restarts:
        - Disk Fill Attacks
        - High Memory Use
- `Bitcoin Core` 0.10.0 uses an initial block download (IBD) method called `headers-first`
    - `getheaders` -> `headers` and `getdata` -> `block`
    - Bitcoin Core will only request up to 16 blocks at a time from a single peer. Combined with its maximum of 8 outbound connections,
    - Bitcoin Core’s headers-first mode uses a 1,024-block moving download window to maximize download speed.
#### Block Broadcasting
When a miner discovers a `new block`, it broadcasts the new block to its peers
- Unsolicited Block Push: the miner sends a `block` message to each of its full node peers with the new block. 
- Standard Block Relay: the miner, acting as a `standard relay node`, sends an `inv` message to each of its peers (both full node and SPV) with an inventory referring to the new block.
- Direct Headers Announcement: a relay node may skip the round trip overhead of an `inv` message followed by `getheaders` by instead immediately sending a `headers` message containing the full header of the new block. 
    - This protocol for block broadcasting was proposed in BIP 130 and has been implemented in Bitcoin Core since version 0.12.
By default, `Bitcoin Core` broadcasts blocks using `direct headers announcement` to any peers that have signalled with `sendheaders` and uses `standard block relay` for all peers that have not. Bitcoin Core will accept blocks sent using any of the methods described above.

Blocks-first nodes may download orphan blocks—blocks
- Orphan Blocks: whose previous block header hash field refers to a block header this node hasn’t seen yet
- stale blocks: which have known parents but which aren’t part of the best block chain
Headers-first nodes avoid some of this complexity by always requesting block headers
However, `orphan discarding` does mean that headers-first nodes will ignore orphan blocks sent by miners in an `unsolicited block push`.

#### Transaction Broadcasting
In order to send a transaction to a peer, an `inv` message is sent. If a `getdata` response message is received, the transaction is sent using `tx`. The peer receiving this transaction also forwards the transaction in the same manner, given that it is a valid transaction.
Full peers may keep track of unconfirmed transactions which are eligible to be included in the next block.
SPV clients don’t have a memory pool for the same reason they don’t relay transactions. They can’t independently verify that a transaction hasn’t yet been included in a block and that it only spends UTXOs, so they can’t know which transactions are eligible to be included in the next block.

### Mining
Mining adds new blocks to the `block chain`, making transaction history hard to modify
- Solo mining, where the miner attempts to generate new blocks on his own, with a higher variance
    - P2P Network <--> bitcoind <--> Mining Software <--> ASIC(Mining Hardware)
- Pooled mining, where the miner pools resources with other miners to find blocks more often
    - P2P Network <--> bitcoind <--> Mining Pool <--> Mining Software <--> ASIC(Mining Hardware)
    - allows mining pool operators to pay miners based on their share of the work done.
    - In pooled mining, the mining pool sets the `target threshold` a few orders of magnitude higher (less difficult) than the network difficulty.
    - The `block reward` and `transaction fees` that come from mining that block are paid to the mining pool.
    - The mining pool pays out a portion of these proceeds to individual miners based on how many shares they generated.
    - Different mining pools use different reward distribution systems based on this basic share system.
#### Block Prototypes
In both solo and pool mining, the mining software needs to get the information necessary to construct `block headers`.
- `getwork` RPC: a single 4-byte nonce good for about 4 gigahashes. Solo miners may still use getwork on `v0.9.5` or below, but most pools today discourage or disallow its use.
- `getblocktemplate` RPC:  provides the mining software with much more information:
- `Stratum` focuses on giving miners the minimal information they need to construct block headers on their own:
Like all `bitcoind` RPCs, `getblocktemplate` is sent over HTTP. To ensure they get the most recent work, most miners use `HTTP longpoll` to leave a `getblocktemplate` request open at all times. This allows the mining pool to push a new `getblocktemplate` to the miner as soon as any miner on the `peer-to-peer network` publishes a new block or the pool wants to send more transactions to the mining software.
The GPLv3 `BFGMiner` mining software and AGPLv3 `Eloipool` mining pool software are widely-used among miners and pools. The `libblkmaker` C library and `python-blkmaker` library, both MIT licensed, can interpret `GetBlockTemplate` for your programs.

Block header format
- Version             4 bytes     Little-endian
- Previous Block ID   32 bytes    Big-endian
- Merkle Root         32 bytes    Big-endian
- Time                4 bytes     Little-endian
- Bits                4 bytes     Little-endian
- Nonce               4 bytes     Little-endian
#### Stratum
- The information necessary to construct a coinbase transaction paying the pool.
- The parts of the merkle tree which need to be re-hashed to create a new merkle root when the coinbase transaction is updated with a new extra nonce. The other parts of the merkle tree, if any, are not sent, effectively limiting the amount of data which needs to be sent to (at most) about a kilobyte at current transaction volume.
- All of the other non-merkle root information necessary to construct a block header for the next block.
- The mining pool’s current target threshold for accepting shares.

Unlike getblocktemplate:
- miners using Stratum cannot inspect or add transactions to the block they’re currently mining.
- uses a two-way TCP socket directly, so miners don’t need to use HTTP longpoll to ensure they receive immediate updates from mining pools when a new block is broadcast to the peer-to-peer network.

具体协议格式参考`slushpool` help center

#### Target/Difficulty
The maximum target used by SHA256 mining devices is: `0x00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF`
Because Bitcoin stores the target as a floating-point type, this is truncated: `0x00000000FFFF0000000000000000000000000000000000000000000000000000`

`difficulty = maxtarget / current_target`
`maxtarget` can be different for various ways to measure difficulty. Traditionally, it represents a hash where the leading 32 bits are zero and the rest are one (this is known as "`pool difficulty`" or "`pdiff`"). The Bitcoin protocol represents targets as a custom floating point type with limited precision; as a result, Bitcoin clients often approximate difficulty based on this (this is known as "`bdiff`").

- `256_max = 2^256 - 1`
- `bitcoin_max = 2 ^ 224 - 1`
- `bitcoin_max_real = 2 ^ 224 - 2 ^ 208`
- `probability = 1 / (hashrate * 600) = target / 256_max`
    - `target = 256_max * probability = 256_max / (hashrate * 600)`
- `bdiff = bitcoin_max_real / target = bitcoin_max_real * (hashrate * 600) / 256_max`
    - `hashrate = (bdiff / 600) * (256_max / bitcoin_max_real)`

#### Transaction
The UTXO of a coinbase transaction has the special condition that it cannot be spent (used as an input) for at least `100` blocks. This temporarily prevents a miner from spending the transaction fees and block reward from a block that may later be determined to be stale (and therefore the coinbase transaction destroyed) after a block chain fork.

`Locktime` sets the eariest time a transaction can be mined in to a block. You can use locktime to make sure that a transaction is locked until a specific `block height`, or `a point in time`.
A `vout`(vector out) is an index number for an output in a transaction.

#### Hashcash
Bitcoin uses the `hashcash Proof_of_work` function as the mining core.
Like many cryptographic algorithms `hashcash` uses a hash function as a building block
`hashcash` can be instantiated with different functions:
- hashcash-SHA1 (original)
- hashcash-SHA256^2 (bitcoin)
- hashcash-Scrypt(iter=1) (litecoin).
##### Adding purpose
If the partial-pre-image `x` from `y=H(x)` is random it is just a `disconnected proof-of-work` to no purpose, everyone can see you did do the work, but they don't know why, so users could reuse the same work for different services. To make the proof-of-work be bound to a service, or purpose, the hash must include `s`, a `service string` so the work becomes to find `H(s,c)/2^(n-k)=0`. The miner varies counter `c` until this is true. The service string could be a web server domain name, a recipients email address, or in bitcoin `a block of the bitcoin blockchain ledger`.
One additional problem is that if multiple people are mining, using the same service string, they must not start with the same `x` or they may end up with the same proof
To avoid risking wasting work in this way, there needs to be a random starting point, and so the work becomes to find `H(s,x,c)/2^(n-k) = 0` where `x` is random, and `c` is the counter being varied, and `s` is the service string.
In fact in bitcoin the `service string is the coinbase` and the coinbase includes the recipients reward address, as well as the transactions to validate in the block. Bitcoin actually does not include a random start point `x`, reusing the reward address as the randomization factor to avoid collisions for this random start point purpose, which saves 16-bytes of space in the coinbase. For privacy bitcoin expect the miner to use a different reward address on each successful block.
But because bitcoin needs more precise and dynamic control of work (to target 10-minute block interval accurately), it changes `k` to be a fractional (floating-point) so the work becomes to find `H(s,x,c) < 2^(n-k)`

Bitcoin also defines a new notion of `(relative) difficulty` which is the work required so that at current network hashrate a block is expected to be found every 10 minutes. It is expressed relative to a `minimum work unit of 2^32 iterations` (approximately, technically minimum work is `0xFFFF0000` due to bitcoin implementation level details). Bitcoin difficulty is simple to approximately convert to log2 cryptographic security: `k=log2(difficulty)+32` (or for high accuracy `log2(difficulty*0xFFFF0000)`). Difficulty is related to the target simply as `difficulty = target / 0xFFFF0000`.
##### Miner privacy
In principle a miner should therefore for privacy use a different reward-address for each block (and reset the counter to 0).
In fact with bitcoin the counter also should be obscured otherwise you would reveal your effort level
Bitcoin does this via the `nonce` and `extra-nonce`. `Nonce` starts at 0, but extra nonce is random. Together these form a randomized counter hiding the amount of effort that went into the proof, so no one can tell if it was a powerful but unlucky miner who worked hard, or a weak miner who was very lucky.
#### Block hashing algorithm
Incrementing the `extraNonce` field entails recomputing the `merkle tree`, as the `coinbase transaction` is the left most leaf node.

### commands
`bitcoin-cli stop`
`Bitcoin Coin

### glossary
- Internal Byte Order: The standard order in which hash digests are displayed as strings
- RPC Byte Order: reversed: The rationale for the reversal is unknown, but it likely stems from Bitcoin Core’s use of hashes (which are byte arrays in C++) as integers for the purpose of determining whether the hash is below the network target
- target: The target is the threshold below which a block header hash must be in order for the block to valid, and `nBits` is the encoded form of the `target threshold` as it appears in the `block header`.
- Coinbase transaction(Generation transaction): The first transaction in a block. Always created by a miner, it includes a single coinbase.
- `coinbase`: A special field used as the sole input for `coinbase transaction`. The coinbase allows claiming the block reward and provides up to 100 bytes for arbitrary data.占了普通事务的sigScript的位置
- `The number of Bitcoins generated per block` starts at 50 and is halved every 210,000 blocks (about four years).
- Hash Rate: The hash rate is the measuring unit of the processing power of the Bitcoin network.
- Bitcoin mining is the process of making computer hardware do mathematical calculations for the Bitcoin network to `confirm transactions and increase security`. As a reward for their services, Bitcoin miners can collect `transaction fees` for the transactions they confirm, along with `newly created bitcoins`.
- A `digital signature` is a mathematical scheme for demonstrating the authenticity of digital messages or documents. A valid digital signature gives a recipient reason to believe that the message was created by a known sender (authentication), that the sender cannot deny having sent the message (non-repudiation), and that the message was not altered in transit (integrity).
    - A key generation algorithm that selects a private key uniformly at random from a set of possible private keys. The algorithm outputs the private key and a corresponding public key.
    - A signing algorithm that, given a message and a private key, produces a signature.
    - A signature verifying algorithm that, given the message, public key and signature, either accepts or rejects the message's claim to authenticity.
- A proof of work is a piece of data which was difficult (costly, time-consuming) to produce so as to satisfy certain requirements. It must be trivial to check whether data satisfies said requirements.
- You get a block ID by hashing the block header through SHA256 twice.
- merkle root: By repeatedly hashing together pairs of Transaction IDs until you end up with a single hash as a result.
- The bits field is a compact way of storing the target in the block header.
    - Exponent: This gives you the size of the target in bytes.
    - Coefficient: This gives you the initial 3 bytes of the target.
- The nonce is a field in the block header. I call it "the mining field".
- Application-specific integrated circuit (ASIC)
- `Tor` is a distributed 'onion' network, that makes it more difficult for an adversary to track any one peer on the network.
- `Onion routing` is a technique for anonymous communication over a computer network. In an onion network, messages are encapsulated in layers of encryption, analogous to layers of an onion. The encrypted data is transmitted through a series of network nodes called onion routers, each of which "peels" away a single layer, uncovering the data's next destination. When the final layer is decrypted, the message arrives at its destination. The sender remains anonymous because each intermediary knows only the location of the immediately preceding and following nodes.
- `Merged mining` is the process of allowing two different crypto currencies based on the same algorithm to be mined simultaneously.
- `midstate`:可加快`double sha256`的计算，通过改变header中nonce，header前64字节的hash可以保存，这样只需要计算剩下来的字节。
### Merged Mining
- Auxiliary Proof-of-Work (POW): This is the way that merged mining can exist; it is the relationship between two blockchains for one to trust the other's work as their own and accept AuxPOW blocks.
- Merged Mining: The act of using work done on one blockchain on more than one chain, using Auxiliary POW.
- Auxiliary Blockchain: The altcoin that is accepting work done on alternate chains as valid on its own chain. Client applications have to be modified to accept Auxiliary POW.
- Parent Blockchain: where the actual mining work is taking place. This chain does not need to be aware of the Auxiliary POW logic, as AuxPOW blocks submitted to this chain are still valid blocks.
- Parent Block: a block that is structured for the parent blockchain. The header of this block is part of the AuxPOW Block in the auxiliary blockchain.
- AuxPOW Block: This is a new type of block that is similar to a standard blockchain block
- 将`AuxPOW Block`的header hash插入到`Parent Block`的scriptSig中
### Mining pool
List of Mining Pools: `https://en.bitcoin.it/wiki/Comparison_of_mining_pools`
`Eligius`, also sometimes referred to as `Éloi` or "`Luke-Jr's pool`", is a mining pool.

### Protocol
Usually, when a hash is computed within bitcoin, it is computed twice. 
#### Addresses
A bitcoin address is in fact the hash of a ECDSA public key, computed this way:
- Version = 1 byte of 0 (zero); on the test network, this is 1 byte of 111
- Key hash = Version concatenated with RIPEMD-160(SHA-256(public key))
- Checksum = 1st 4 bytes of SHA-256(SHA-256(Key hash))
- Bitcoin Address = Base58Encode(Key hash concatenated with Checksum)

#### version
When a node creates an outgoing connection, it will immediately advertise its version. The remote node will respond with its version. No further communication is possible until both peers have exchanged their version.

### BIP Bitcoin Improvement Proposals
`getmemorypool` was renamed to `getblocktemplate`, the technical specifications can be found in BIP 22 and BIP 23
- check [Getblocktemplate](https://en.bitcoin.it/wiki/Getblocktemplate)

#### BIP 34
解决`coinbase transaction`hash重复问题
- Treat transactions with a version greater than 1 as non-standard
- Add `height` as the first item in the coinbase transaction's `scriptSig`, and increase `block version` to `2`
- 75%和95%规则
#### BIP 9
解决`BIP 34`及后续`BIP 66`和`BIP 65`带来的问题，proposal将以位的形式出现，并有状态转换
高三位为`001`，即`block version`以`0x20`开头
在`getblocktemplate rpc request`添加了`rules`参数
#### BIP 22/23
解决`getwork`导致`bitcoind`负载过高，这部分工作可以交给外部应用
`BIP 23` contains optional extensions on top of BIP 22

### other coin
Bitcoin Cash (BCH)(bittrex decided to take `BCC` for bitcoin cash)
BitConnect (`BCC`)(ponzi)
Siacoin (SC)
Dash (DASH)
Dashcoin (DSH)
Ethereum (ETH)
Ethereum Classic (ETC)
Litecoin (LTC)
Zcash (ZEC)
Rootstock (RSK)

### Estimating fees v0.14
提供费率接口：https://bitcoinfees.earn.com/api
https://github.com/jhoenicke/mempool
https://jochen-hoenicke.de/queue/#all
https://bitcointechtalk.com/an-introduction-to-bitcoin-core-fee-estimation-27920880ad0

从`bitcoins core 0.15.0`开始引入`estimatesmartfee`和`estimaterawfee`

- buckets：group those transaction fee rates into buckets, where each bucket corresponds to a range of fee rates
    - Bitcoin Core wants to be able to make estimates over a very large range of fee rates, so the lowest bucket starts at `1s/B`, then increase 10% to `1.1s/B`, and keep increasing at `10%`
- target:  the number of blocks between a transaction entering the mempool and being accepted in a block.
    - Bitcoin Core keeps track of targets from 1 block up to 25 blocks.
