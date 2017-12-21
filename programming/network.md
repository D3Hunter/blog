### Serialization
- JSON payload is human readable, easy to implement and debug. In contrary of most binary protocol, JSON payload can be easily extended without breaking backward compatibility.
- Custom text protocol is human readable and easy to debug, but not so easy to implement as it may look at first glance. We have to define a way how to pair request and response, because sequential processing of requests may be a bit tricky on some platforms (yes, now I'm referring Twisted framework which I used for pool implementation). We also have to define how to serialize various data types like lists or even mappings. JSON solve all this transparently for us.
- Custom binary protocol is the most compact form which can saves a lot of bandwith, especially while dealing with binary data involved in bitcoin mining. However writing (de)serializers *properly* may be a bit tricky. I wanted the protocol which is easy to implement. Fiddling with byte order and binary headers is not what I was looking for.
- Protocol buffers by Google is interesting concept which may fit the needs, except that only C++, Python and Java are supported.
- Thrift is another binary protocol which I used some time ago, but it is defitely too heavy for our purposes.