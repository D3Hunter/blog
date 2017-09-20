# note on reading Java Servlet Specification 3.0

## Overview
A servlet is a Java™ technology-based Web component, managed by a container,
that generates dynamic content. 
Containers, sometimes called servlet engines, are Web server extensions
that provide servlet functionality. Servlets interact with Web clients via a
request/response paradigm implemented by the servlet container.

A servlet container can be built into a host Web server, or installed as an add-on
component to a Web Server via that server’s native extension API. Servlet containers
can also be built into or possibly installed into Web-enabled application servers.

All servlet containers must support HTTP as a protocol for requests and responses,
but additional request/response-based protocols such as HTTPS (HTTP over SSL)
may be supported.

## Servlet Interface
The basic `Servlet` interface defines a `service` method for handling client requests.
The `HttpServlet` interface defines the `getLastModified` method to support conditional `GET` operations.

For a servlet not hosted in a distributed environment (the default), the servlet
container must use only one instance per servlet declaration. However, for a servlet
implementing the `SingleThreadModel` interface, the servlet container may
instantiate multiple instances to handle a heavy request load and serialize requests
to a particular instance.
`SingleThreadModel` Interface is deprecated in this version of the specification

### Servlet Life Cycle
Loading -> Instantiation -> Initalization -> Service -> Destroy

This life cycle is expressed in the API by the `init`, `service`, and `destroy`
methods of the `javax.servlet.Servlet` interface that all servlets must implement.

The loading and instantiation can occur when the container is started, or delayed until
the container determines the servlet is needed to service a request.

The `destroy` method is not called on initalization Exception.

Requests and responces are represented by objects of type `ServletRequest` and `ServletResponse` respectively.

Servlet 3.0 introduces the ability for asynchronous processing of requests so that the
thread may return to the container and perform other tasks. 
When asynchronous processing begins on the request, another thread or callback may either generate the
response and call `complete` or dispatch the request so that it may run in the context
of the container using the `AsyncContext.dispatch` method.
1. The request is received and passed via normal filters for authentication etc. to the servlet.
2. The servlet processes the request parameters and/or content to determine the
3. nature of the request.
4. The servlet issues requests for resources or data, for example, sends a remote web service request or joins a queue waiting for a JDBC connection.
5. The servlet returns without generating a response.
6. After some time, the requested resource becomes available, the thread handling that event continues processing either in the same thread or by dispatching to a resource in the container using the `AsyncContext`.

Dispatching from a servlet that has `asyncSupported=true` to one where
`asyncSupported` is set to false is allowed. In this case, the response will be
committed when the `service` method of the servlet that does not support async is
exited, and it is the container's responsibility to call `complete` on the `AsyncContext`

## important references
- RFC 1630 Uniform Resource Identifiers (URI)
- RFC 1738 Uniform Resource Locators (URL)
- RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax
- RFC 1808 Relative Uniform Resource Locators
- RFC 1945 Hypertext Transfer Protocol (HTTP/1.0)
- RFC 2045 MIME Part One: Format of Internet Message Bodies
- RFC 2046 MIME Part Two: Media Types
- RFC 2047 MIME Part Three: Message Header Extensions for non-ASCII text
- RFC 2048 MIME Part Four: Registration Procedures
- RFC 2049 MIME Part Five: Conformance Criteria and Examples
- RFC 2109 HTTP State Management Mechanism
- RFC 2145 Use and Interpretation of HTTP Version Numbers
- RFC 2324 Hypertext Coffee Pot Control Protocol (HTCPCP/1.0)1
- RFC 2616 Hypertext Transfer Protocol (HTTP/1.1)
- RFC 2617 HTTP Authentication: Basic and Digest Authentication
- RFC 3986 Uniform Resource Identifier (URI): Generic Syntax