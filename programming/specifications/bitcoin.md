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

### commands
`bitcoin-cli stop`
`Bitcoin Coin

### glossary
- Internal Byte Order: The standard order in which hash digests are displayed as strings
- RPC Byte Order: reversed: The rationale for the reversal is unknown, but it likely stems from Bitcoin Core’s use of hashes (which are byte arrays in C++) as integers for the purpose of determining whether the hash is below the network target
- target: The target is the threshold below which a block header hash must be in order for the block to valid, and `nBits` is the encoded form of the t`arget threshold` as it appears in the `block header`.
- Coinbase transaction(Generation transaction): The first transaction in a block. Always created by a miner, it includes a single coinbase.
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

### Mining pool
List of Mining Pools: `https://en.bitcoin.it/wiki/Comparison_of_mining_pools`
`Eligius`, also sometimes referred to as `Éloi` or "`Luke-Jr's pool`", is a mining pool.