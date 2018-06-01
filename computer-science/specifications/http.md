- `Http Polling`(http short polling): Basically AJAX
- `Http Long Polling`: AJAX but the server holds on to the response unless the server has an update
- `Http Streaming`: Similar to long polling but the server responds with a header with "Transfer Encoding: chunked" and hence we do not need to initiate a new request every time the server sends some data
- `Java Applet, Flash, Silverlight`: They provide the ability to connect to socket servers over tcp/ip but since they are plugins, developers don't want to depend on them.
- `WebSockets`: they are the new API which tries to address the short comings of above methods in the following manner:
- server-side routing: server decides, whole page refresh
- client-side routing: client decides, partical refresh, slow initial load

## RFC 6202
In order to improve this situation, several `server-push programming`
   mechanisms have been implemented in recent years.  These mechanisms,
   which are often grouped under the common label "`Comet`" [COMET],
   enable a web server to send updates to clients without waiting for a
   poll request from the client.
The two most common server-push mechanisms are `HTTP long polling` and
   `HTTP streaming`:
   HTTP Long Polling:  The server attempts to "hold open" (not
      immediately reply to) each HTTP request, responding only when
      there are events to deliver.  In this way, there is always a
      pending request to which the server can reply for the purpose of
      delivering events as they occur, thereby minimizing the latency in
      message delivery.

   HTTP Streaming:  The server keeps a request open indefinitely; that
      is, it never terminates the request or closes the connection, even
      after it pushes data to the client.
### Http Long Pooling
The server achieves these efficiencies by responding to a request only when a particular event,status, or timeout has occurred.  Once the server sends a long poll response, typically the client immediately sends a new long poll request.
Life Cycle:
1.  The client makes an initial request and then waits for a response.
2.  The server defers its response until an update is available or until a particular status or timeout has occurred.
3.  When an update is available, the server sends a complete response to the client.
4.  The client typically sends a new long poll request, either immediately upon receiving a response or after a pause to allow an acceptable latency period.

The HTTP long polling mechanism can be applied to either `persistent` or `non-persistent` HTTP connections.  The use of persistent HTTP connections will avoid the additional overhead of establishing a new TCP/IP connection [TCP] for every long poll request.
#### HTTP Long Polling Issues
- Header Overhead
- Maximal Latency: the maximal latency is over three network transits (long poll response, next long poll request, long poll response).
- Connection Establishment:  A common criticism of both short polling and long polling is that these mechanisms frequently open TCP/IP connections and then close them. 当然也可以keep-alive
- Allocated Resources: Operating systems will allocate resources to TCP/IP connections and to HTTP requests outstanding on those connections.
- Graceful Degradation:  A long polling client or server that is under load has a natural tendency to gracefully degrade in performance at a cost of message latency.
- Timeouts:  Long poll requests need to remain pending or "hanging" until the server has something to send to the client.
- Caching:  Caching mechanisms implemented by intermediate entities can interfere with long poll requests.
### HTTP Streaming
The HTTP streaming mechanism keeps a request open indefinitely.  It never terminates the request or closes the connection, even after the server pushes data to the client.
Life Cycle:
1.  The client makes an initial request and then waits for a response.
2.  The server defers the response to a poll request until an update is available, or until a particular status or timeout has occurred.
3.  Whenever an update is available, the server sends it back to the client as a part of the response.
4.  The data sent by the server `does not terminate the request or the connection`.  The server returns to step 3.

An HTTP response content length can be defined using three options:
- Content-Length header:  This indicates the size of the entity body in the message, in bytes.
- Transfer-Encoding header:  The 'chunked' valued in this header indicates the message will break into chunks of known size if needed.
- End of File (EOF):The main issue with EOF is that it is difficult to tell the difference between a connection terminated by a fault and one that is correctly terminated.
An HTTP/1.0 server can use only EOF as a streaming mechanism.  In contrast, both EOF and "chunked transfer" are available to an HTTP/1.1 server.
#### HTTP Streaming Issues
- Network Intermediaries: There is no requirement for an intermediary to immediately forward a partial response, and it is legal for the intermediary to buffer the entire response before sending any data to the client
- Maximal Latency:
- Client Buffering:  There is no requirement in existing HTTP specifications for a client library to make the data from a partial HTTP response available to the client application.
- Framing Techniques:  Using HTTP streaming, several application messages can be sent within a single HTTP response.  The separation of the response stream into application messages needs to be performed at the application level and not at the HTTP level.  In particular, it is not possible to use the HTTP chunks as application message delimiters, since intermediate proxies might "re-chunk" the message stream

### Existing technologies
that implement `HTTP-based server-push mechanisms` to asynchronously deliver messages from the server to the client.
- Bayeux
- BOSH: Bidirectional-streams Over Synchronous HTTP
- Server-Sent Events
