A sliding window protocol is a feature of packet-based data transmission protocols. Sliding window protocols are used where `reliable in-order delivery of packets` is required, such as in the data link layer (OSI layer 2) as well as in the Transmission Control Protocol (TCP).
- 使用window限制sequence number大小

TCP provides reliability with a mechanism called `Positive Acknowledgment with Re-transmission (PAR)`. Simply stated, a system using PAR sends the data again, unless it hears from the remote system that the data arrived successfully.

### Serialization
- JSON payload is human readable, easy to implement and debug. In contrary of most binary protocol, JSON payload can be easily extended without breaking backward compatibility.
- Custom text protocol is human readable and easy to debug, but not so easy to implement as it may look at first glance. We have to define a way how to pair request and response, because sequential processing of requests may be a bit tricky on some platforms (yes, now I'm referring Twisted framework which I used for pool implementation). We also have to define how to serialize various data types like lists or even mappings. JSON solve all this transparently for us.
- Custom binary protocol is the most compact form which can saves a lot of bandwith, especially while dealing with binary data involved in bitcoin mining. However writing (de)serializers *properly* may be a bit tricky. I wanted the protocol which is easy to implement. Fiddling with byte order and binary headers is not what I was looking for.
- Protocol buffers by Google is interesting concept which may fit the needs, except that only C++, Python and Java are supported.
- Thrift is another binary protocol which I used some time ago, but it is defitely too heavy for our purposes.

### congestion control algorithms
- slow start
- congestion avoidance
- fast retransmit
- fast recovery.

### socket connect/send/recv timeout
#### system call layer
- connect 默认timeout：linux下该值在/proc/sys/net/ipv4/tcp_syn_retries，配置文件为/etc/sysctl.conf：net.ipv4.tcp_syn_retries
- send/recv操作，底层对应到socket的超时参数为SO_RCVTIMEO and SO_SNDTIMEO，默认为0，即无超时

C socket connect没有TIMEOUT设置，实现超时可通过：
- 设置non-blocking，然后通过select/poll设置超时并选择。（HotSpot实现方式）
- 使用signal来interrupt connect
- linux下在connect前设置SO_SNDTIMEO

- RTT - Round Trip Time
- RTO: round trip timeout

#### java layer
`Socket.connect(addr, timeout)`和`Socket.setSoTimeout`，HotSpot底层（solaris／linux）在`connect`或`read`前`poll`来实现超时

这俩参数影响的是URLConnection及其子类
- sun.net.client.defaultConnectTimeout
- sun.net.client.defaultReadTimeout

#### jdbc layer
Statement.setQueryTimeout 默认无timeout，设置后会启动一个timer，在超时后向DB发送CANCEL命令

PostgreSQL的jdbc参数
- connectTimeout为调用Socket.connect的参数
- socketTimeout就是调用Socket.setSoTimeout

