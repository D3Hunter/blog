BEP stands for BitTorrent Enhancement Proposal

### BEP Types
- Standards Track BEP describes an extension
- Informational BEP describes a BitTorrent design issue
- Process BEP describes a process surrounding BitTorrent

### actors
- clients,
- trackers
- web servers.

### A BitTorrent file distribution consists of these entities:
- An ordinary web server(方便其他人下载.torrent文件)
- A static 'metainfo' file(.torrent文件)
- A BitTorrent tracker(coordinator)
- An 'original' downloader(The first one Serving files in the .torrent file)
- The end user web browsers(get the .torrent file)
- The end user downloaders(download the files in the .torrent file)

### bencoding
- Strings are length-prefixed base ten followed by a colon and the string.
- Integers are represented by an 'i' followed by the number in base 10 followed by an 'e'.
- Lists are encoded as an 'l' followed by their elements (also bencoded) followed by an 'e'.
- Dictionaries are encoded as a 'd' followed by a list of alternating keys and their corresponding values followed by an 'e'.

### Metainfo files (.torrent files)
Metainfo files are bencoded dictionaries with the following keys:
- `announce`: The URL of the tracker.
- `info`: This maps to a dictionary, with keys described below.
    - `name`: maps to a UTF-8 encoded string which is the suggested name to save the file (or directory) as.
        - In the single file case, the name key is the name of a file, in the muliple file case, it's the name of a directory.
    - piece length maps to the number of bytes in each piece the file is split into.(almost always a power of two)
        - 从`bittorrent`协议看整个`.torrent`代表，这个整块数据按`piece length`拆分，`pieces`用于校验。逻辑上内部可分成多个文件
    - `pieces` maps to a string whose length is a multiple of 20.
        - It is to be subdivided into strings of length 20, each of which is the SHA1 hash of the piece at the corresponding index.
    - `length` maps to the length of the file in bytes.（length和files有且只能有一个）
    - `files` represents a set of files which go in a directory structure.
        - multi-file case is treated as only having a single file by concatenating the files in the order they appear in the files list.
        - 每个file包含下面的key
            - length - The length of the file, in bytes.
            - path - A list of UTF-8 encoded strings corresponding to the file/dir names. 按目录分隔符合并起来成为完整路径

All strings in a .torrent file that contains text must be UTF-8 encoded.

### Tracker
#### GET requests have the following keys:
- `info_hash`: hash of value of `info` key in metainfo file.
- peer_id: Each downloader generates its own id at random
- `ip` An optional parameter giving the IP (or dns name) which this peer is at.
    - Generally used for the origin if it's on the same machine as the tracker.(一般的downloader不需要显示指定，通过socket conn就可获得)
- `port` The port number this peer is listening on.
    - Common listen on port 6881 and if that port is taken try 6882, then 6883, etc. and give up after 6889.
    - 一般一个端口服务一个.torrent，也可以多个
- `uploaded` The total amount uploaded so far, encoded in base ten ascii.
- `downloaded` The total amount downloaded so far, encoded in base ten ascii.
- `left` The number of bytes this peer still has to download, encoded in base ten ascii.
    - Note that this can't be computed from downloaded and the file length since it might be a resume, and there's a chance that some of the downloaded data failed an integrity check and had to be re-downloaded.
- `event` This is an optional key which maps to started, completed, or stopped (or empty, which is the same as not being present).

#### Tracker responses
- `failure reason`, then that maps to a human readable string which explains why the query failed
- `interval`, which maps to the number of seconds the downloader should wait between regular rerequests
- `peers` maps to a list of dictionaries corresponding to peers, each of which contains the keys `peer id`, `ip`, and `port`

### peer protocol
BitTorrent's peer protocol operates over `TCP` or `uTP`(uTorrent Transport Protocol, `uTP` is a transport protocol layered on top of UDP.).

Peer connections are symmetrical. Messages sent in both directions look the same, and data can flow in either direction.

Connections contain two bits of state on either end: `choked` or not, and `interested` or not. `Choking` is a notification that no data will be sent until unchoking happens. Data transfer takes place whenever one side is `interested` and the other side is not `choking`.

When data is being transferred, downloaders should keep several piece requests queued up at once in order to get good TCP performance (this is called 'pipelining'.)

The peer wire protocol consists of a `handshake` followed by a never-ending stream of length-prefixed `messages`.

Messages of length zero are keepalives, and ignored. All non-keepalive messages start with a single byte which gives their type.
- 0 - choke
- 1 - unchoke
- 2 - interested
- 3 - not interested
- 4 - have
- 5 - bitfield
- 6 - request
- 7 - piece
- 8 - cancel

### BEP-9 Extension for Peers to Send Metadata Files
magnet links, a link on a web page only containing enough information to join the swarm (the info hash).

This extension only transfers the info-dictionary part of the .torrent file. This part can be validated by the info-hash. In this document, that part of the .torrent file is referred to as the metadata.

#### Magnet URI format
- v1: `magnet:?xt=urn:btih:<info-hash>&dn=<name>&tr=<tracker-url>&x.pe=<peer-address>`
- v2: `magnet:?xt=urn:btmh:<tagged-info-hash>&dn=<name>&tr=<tracker-url>&x.pe=<peer-address>`
    - <tagged-info-hash> Is the multihash formatted

### BEP-5 DHT Protocol
BitTorrent uses a `"distributed sloppy hash table" (DHT)` for storing peer contact information for "trackerless" torrents. In effect, each peer becomes a tracker. The protocol is based on `Kademila` and is implemented over UDP.

- A "peer" is a client/server listening on a TCP port that implements the BitTorrent protocol.
- A "node" is a client/server listening on a UDP port implementing the distributed hash table protocol.

The DHT is composed of nodes and stores the location of peers. BitTorrent clients include a DHT node, which is used to contact other nodes in the DHT to get the location of peers to download from using the BitTorrent protocol.

