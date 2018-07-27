open source messaging and Integration Patterns server.

disable jmx support(thread name starts with rmi): set `useJmx` to false
set `persistent=false` to disable persistent
You can monitor the status of the connection with the broker via the `addTransportListener()` method on the `ActiveMQConnection`.

by default there is one thread allocated by every `session`. This basically means that session will use its ThreadPoolExecutor to execute its tasks.

If you want to consume concurrently from a queue, then you must use a different session for each consumer. This is because you must have a session per thread. The JMS contract is that only 1 session is used by one thread at once - which if you're using consumers means that only 1 consumer can receive messages at once if using the same session. So if you want concurrent consumption of messages, you need to `use different sessions for each consumer`.


### Quick Start
- `activemq start`
- 确认安装： http://127.0.0.1:8161/admin/ admin/admin
- `activemq stop`
- `activemq create xxx-broker-name` 创建一个自己的实例（独立的配置等）
- edit `conf/activemq.xml`
- `./bin/xxx-broker-name start`
- `./bin/xxx-broker-name stop`

### Memory Usage
主要是message占用，使用`MemoryUsage`对象,使用Producer Flow Control（PFC）
- systemUsage memory limit
- per destination memory limit.
The memory in ActiveMQ works in a `tiered` fashion that flows from the `JVM -> Broker -> broker features`. E.g., the total amount of destination memory limits placed cannot exceed the memory limit of the broker.

- Temp Usage: assigned disk storage that has been used up to spool non-persistent messages
    - check: [http://tmielke.blogspot.hk/2011/02/observations-on-activemqs-temp-storage.html]
    - Because of all messages being swapped in one go by a subscription, it may happen that after the swap has finished the temp storage is above 100% usage. This might occur either when 
        1) using a memoryUsage > tempUsage and the subscription holds a large amount of messages, but also 
        2) when configuring a tempUsage limit < 32 MB (see above).
    1. Don't configure a tempUsage limit < default size of the journal file (32 MB).
    2. Swapping out messages to temp storage can be rather slow. If you already using producer flow control with topic messages, the VM cursor might be an alternative. It won't swap messages to disk.
- Store Usage: assigned disk space that has been used up to store persistent messages
- Memory Usage: assigned memory of the broker that has been used up to keep track of destinations, cache messages etc.

### Message Cursors(since 5.0)
- Store based: a hybrid approach, allowing messages to pass from producer to consumer directly (after the messages have been persisted), but switches back to using cursors if the consumer(s) fall behind.
- VM Cursor: is how ActiveMQ 4.x works: references to a message are held in memory, and passed to the dispatch queue when needed.
- File based Cursor: When memory in the broker reaches its limit, it can page messages to temporary files on disk.

Paging for Non-Persistent Messages
`Non-persistent` messages are passed directly to the cursor, so the store based cursor embeds a file based cursor just for these types of messages: 

For Topics there is a dispatch queue and pending cursor for every subscriber.
For Queues there is a single dispatch Queue and pending Queue for every destination.

### Interceptor
ActiveMQ has a sophisticated `interceptor stack` so that you can attach whatever functionality you require into the broker in an easy way without complicating all of the other broker code.

### persistent and non-persistent delivery
As per the JMS specification, the `default delivery mode` is persistent. The persistence flag is set on the MessageProducer for all messages using the setDeliveryMode. It can also be specified on a per message basis using the long form of the send method. Persistence is a property of a an individual message.

### Embedded ActiveMQ Broker
Advantages of embedding the broker
- embedding a broker means you can use the VM transport which avoids the use of sockets and serialization. Instead ActiveMQ can pass around messages by value.
    - the slight exception to this is ObjectMessage; the JMS specification says you must serialize the body of the ObjectMessage whenever you send it. However you can disable this feature if you want really high performance when using VM transport
- its only 1 single deployment unit/JVM rather than 2 coupled processes.

## URL
嵌入式mq，本地client可通过`vm://brokerName?transportOptions`连接
### The Failover Transport
The Failover transport layers reconnect logic on top of any of the other transports. The configuration syntax allows you to specify any number of composite URIs. The Failover transport randomly chooses one of the composite URIs and attempts to establish a connection to it. If it does not succeed, or if it subsequently fails, a new connection is established choosing one of the other URIs randomly from the list.
- `failover:(uri1,...,uriN)?transportOptions&nestedURIOptions`
- `failover:uri1,...,uriN`
