## Advanced Message Queuing Protocol (AMQP) 
an open standard application layer protocol for message-oriented middleware. The defining features of AMQP are message orientation, queuing, routing (including point-to-point and publish-and-subscribe), reliability and security
AMQP is a wire-level protocol
The AMQP specification is defined in several layers: (i) a type system, (ii) a symmetric, asynchronous protocol for the transfer of messages from one process to another, (iii) a standard, extensible message format and (iv) a set of standardised but extensible 'messaging capabilities.'

Java Message Service (JMS), is often compared to AMQP. However, `JMS is an API specification` (part of the Java EE specification) that defines how message producers and consumers are implemented. `JMS does not guarantee interoperability between implementations`, and the JMS-compliant messaging system in use may need to be deployed on both client and server. On the other hand, AMQP is a wire-level protocol specification. In theory AMQP provides interoperability as different AMQP-compliant software can be deployed on the client and server sides. Note that, like HTTP and XMPP, AMQP does not have a standard API.

### Comparable specifications
- Streaming Text Oriented Messaging Protocol (STOMP), a text-based protocol developed at Codehaus; uses the JMS-like semantics of 'destination'.
- Extensible Messaging and Presence Protocol (XMPP), the Extensible Messaging and Presence Protocol.
- MQTT, a lightweight publish-subscribe protocol.
- OpenWire as used by ActiveMQ.

## wire protocol
a wire protocol refers to a way of getting data from point to point
A wire-level protocol is a description of the format of the data that is sent across the network as a stream of bytes.
In contrast to `transport protocols` at the transport level (like TCP or UDP), the term "`wire protocol`" is used to describe a common way to represent information at the application level.

Examples of wire protocols include:
- IIOP for CORBA
- RTPS for DDS
- Java Debug Wire Protocol (JDWP) for Java debugging
- JRMP for RMI
- SOAP for Web services
- AMQP for message-oriented middleware

## RabbitMQ
implements the Advanced Message Queuing Protocol (AMQP)
written in the Erlang programming language and is built on the `Open Telecom Platform framework` for clustering and failover. Client libraries to interface with the broker are available for all major programming languages.
## ActiveMQ
written in Java together with a full Java Message Service (JMS) client.
its support for a relatively large number of transport protocols, including OpenWire, STOMP, MQTT, AMQP, REST, and WebSockets.[5]
## RocketMQ
by alibaba
