# note on reading Java Servlet Specification 3.0
抽象来看其他的app-server/container／甚至框架结构上都类似，比如servlet-mapping在nginx/apache/django都有类似结构

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
container must use only one instance `per servlet declaration`. However, for a servlet
implementing the `SingleThreadModel` interface, the servlet container may
instantiate multiple instances to handle a heavy request load and serialize requests
to a particular instance. 参考后面的annotation部分
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

## The Request
When the request is an HttpServletRequest object, and conditions set out in ”When Parameters Are Available” on page 22 are met, the
container populates the parameters from the URI query string and POST-ed data. 

Multiple parameter values can exist for any given parameter name. 

Data from the query string and the post body are aggregated into the request parameter set. Query string data is presented before post body data. 

Path parameters that are part of a GET request (as defined by HTTP 1.1) are not
exposed by these APIs. They must be parsed from the String values returned by
the `getRequestURI` method or the `getPathInfo` method.

### When Parameters Are Available
1. The request is an `HTTP` or `HTTPS` request.
2. The HTTP method is `POST`.
3. The content type is `application/x-www-form-urlencoded`.
4. The servlet has made an initial call of any of the `getParameter` family of methods on the request object.

这意味如果用户代码依赖`input stream`, 那么探针不能使用`getParameterXXX`函数获取参数
If the conditions are not met and the post form data is not included in the parameter
set, the post data must still be available to the servlet via the request object’s input
stream. If the conditions are met, post form data will no longer be available for
reading directly from the request object’s input stream.

Attributes may be set by the container to express information that otherwise could not be expressed via the API,
or may be set by a servlet to communicate information to another servlet 
Only one attribute value may be associated with an attribute name. 

There can be multiple headers with the same name, e.g. Cache-Control headers, in an HTTP request. 

### Request Path
- Context Path: The path prefix associated with the ServletContext that this servlet is a part of. If this context is the “default” context rooted at the base of the Web server’s URL name space, this path will be an empty string. Otherwise, if the context is not rooted at the root of the server’s name space, the path starts with a / character but does not end with a / character.
- Servlet Path: The path section that directly corresponds to the mapping which activated this request. This path starts with a ’/’ character except in the case where the request is matched with the ‘/*’ or ““ pattern, in which case it is an empty string.
- PathInfo: The part of the request path that is not part of the Context Path or the Servlet Path. It is either null if there is no extra path, or is a string with a leading ‘/’.

It is important to note that, except for URL encoding differences between the request
URI and the path parts, the following equation is always true:
`requestURI = contextPath + servletPath + pathInfo`

- ServletContext.getRealPath
- HttpServletRequest.getPathTranslated

The specification also allows for the cookies to be `HttpOnly` cookies. `HttpOnly` cookies indicate to the client that
they should not be exposed to client-side scripting code (It’s not filtered out unless
the client knows to look for this attribute). The use of HttpOnly cookies helps
mitigate certain kinds of `cross-site scripting attacks`.

Currently, many browsers do not send a `char` encoding qualifier with the `ContentType`
header, leaving open the determination of the character encoding for reading
HTTP requests. The default encoding of a request the container uses to create the
request reader and parse `POST data` must be `ISO-8859-1` if none has been specified
by the client request.

`setCharacterEncoding(String enc)` has been added to the `ServletRequest` interface. Developers can override the
character encoding supplied by the container by calling this method. It must be
called prior to parsing any post data or reading any input from the request. 

Containers commonly recycle request objects in order to avoid the performance overhead of request object creation. 

## Servlet Context
The `ServletContext` interface defines a servlet’s view of the Web application within
which the servlet is running. 
There is one instance object of the `ServletContext` interface associated with each
Web application deployed into a container. 
Servlets in a container that were not deployed as part of a Web application are
implicitly part of a “default” Web application and have a default ServletContext. In
a distributed container, the default `ServletContext` is non-distributable and must
only exist in one `JVM`.

`Configuration methods` can only be called during the initialization of the application either
from the `contexInitialized` method of a `ServletContextListener`
implementation or from the `onStartup` method of a `ServletContainerInitializer` implementation.

Servlets can be declared(in `web.xml`) or annotated (with `@WebServlet`) or added (with `addServlet` method).

Programmatically added Listeners must implementate one of:
- javax.servlet.ServletContextAttributeListener
- javax.servlet.ServletRequestListener: invocation order corresponds to the declaration order
- javax.servlet.ServletRequestAttributeListener
- javax.servlet.http.HttpSessionListener: invocation order corresponds to the declaration order
- javax.servlet.http.HttpSessionAttributeListener
- javax.servlet.ServletContextListener : If the `ServletContext` was passed to the `ServletContainerInitializer`’s `onStartup` method

Context attributes are local to the JVM in which they were created, not shared in a `distributed container`.
### Resources
The ServletContext interface provides direct access only to the hierarchy of static
content documents that are part of the Web application, including HTML, GIF, and
JPEG files
The `getResource` and `getResourceAsStream` methods take a String with a leading
“/” as an argument that gives the path of the resource `relative` to the root of the
context or relative to the `META-INF/resources` directory of a JAR file inside the
web application’s `WEB-INF/lib` directory. Search order:
1. root of the web application context
2. JAR files in the WEB-INF/lib directory, order of jars is undefined
The full listing of the resources in the Web application can be accessed using the
`getResourcePaths(String path)` method. 
### Temporary Working Directories
Servlet containers must provide a private temporary directory for each servlet context, and make it available via the `javax.servlet.context.tempdir` context attribute. The objects associated with the attribute must be of type `java.io.File`. 

## The Response
### Headers
- setHeader
- addHeader: a header name can have a set of header values 
headers must be set before the response is committed (when the first byte of http payload is sent to the client).
Servlet programmers are responsible for ensuring that the `Content-Type` header is
appropriately set in the response object for the content the servlet is generating.
It is recommended that containers use the `X-Powered-By` HTTP header to publish its
implementation information.
### Convenience Methods
- sendRedirect: set the appropriate headers and content body to redirect the client to a different URL.
- sendError
These methods will have the side effect of committing the response, if it has not already been committed, and terminating it.
### Internationalization
The `setCharacterEncoding`, `setContentType`, and `setLocale` methods can be called repeatedly to change the character encoding. Calls made after the servlet response’s `getWriter` method has been called or after the response is committed have no effect on the character encoding.
If the servlet does not specify a character encoding before the `getWriter` method of
the `ServletResponse` interface is called or the response is committed, the default
`ISO-8859-1` is used.

## Filtering
A filter is a reusable piece of code that can transform the content of HTTP requests, responses, and header information.
- Authentication filters
- Logging and auditing filters
- Image conversion filters
- Data compression filters
- Encryption filters
- Tokenizing filters
- Filters that trigger resource access events
- XSL/T filters that transform XML content
- MIME-type chain filters
- Caching filters
The container must instantiate exactly one instance of the Java class defining the filter `per filter declaration` in the deployment descriptor. Hence, two instances of the same filter class will be instantiated by the container if the developer makes two filter declarations for the same filter class.
- The invocation of the next entity is effected by calling the `doFilter` method on the `FilterChain` object
- After invocation of the next filter in the chain, the filter may examine response headers.
- When the last filter in the chain has been invoked, the next entity accessed is the target servlet or resource at the end of the chain. 

The order the container uses in building the chain of filters to be applied for a
particular request URI is as follows:
1. First, the `<url-pattern>` matching filter mappings in the same order that these elements appear in the deployment descriptor. 即先按url匹配，后面跟着按servlet-name匹配的
2. Next, the `<servlet-name>` matching filter mappings in the same order that these elements appear in the deployment descriptor

filter的栈式调用结构（先处理request的filter，后处理response）是有其使用调用栈方式调用决定的
另一种实现方式是双接口，分别对应in和out，可以更灵活的调整filter顺序，目前没看到哪个app-server这么做。

### Filters and the RequestDispatcher
New since version 2.4 of the Java Servlet specification is the ability to configure filters to be invoked under request dispatcher `forward()` and `include()` calls.
By using the new `<dispatcher>` element in the deployment descriptor, the developer can indicate for a `filter-mapping `whether he would like the filter to be applied to requests.
- The request comes directly from the client. This is indicated by a `<dispatcher>` element with value REQUEST, or by the absence of any `<dispatcher>` elements.

## Sessions
The Hypertext Transfer Protocol (HTTP) is by design a stateless protocol. To build effective Web applications, it is imperative that requests from a particular client be associated with each other.
### Session Tracking Mechanisms
- Cookies
    - The standard name of the session tracking cookie must be `JSESSIONID` which must be supported by all 3.0 compliant containers.
    - If a web application configures a custom name for its session tracking cookies, the same custom name will also be used as the name of the URI parameter if the session id is encoded in the URL
- SSL Sessions: Secure Sockets Layer, the encryption technology used in the HTTPS protocol, has a built-in mechanism allowing multiple requests from a client to be unambiguously identified as being part of a session. 
- URL Rewriting
    - URL rewriting is the lowest common denominator of session tracking
    -  When a client will not accept a cookie, URL rewriting may be used by the server as the basis for session tracking.
### Session Scope
HttpSession objects must be scoped at the application (or servlet context) level.The underlying mechanism, such as the cookie used to establish the session, can be the same for different contexts, but the object referenced, including the attributes in that object, must never be shared between contexts by the container.
### Binding Attributes into a Session
Any object bound into a session is available to any other servlet that belongs to the same ServletContext and handles a request identified as being a part of the same session. 即线程安全
`HttpSessionBindingListener`
The `valueBound` method must be called before the object is made available via the `getAttribute` method of the `HttpSession` interface. The `valueUnbound` method must be called after the object is no longer available via the `getAttribute` method of the `HttpSession` interface.
### Last Accessed Times
The session is considered to be accessed when a request that is part of the session is first handled by the servlet container.

## Annotations and pluggability
In a web application, classes using annotations will have their annotations processed only if they are located in the `WEB-INF/classes` directory, or if they are packaged in a jar file located in `WEB-INF/lib` within the application. 
The “`metadata-complete`” attribute defines whether the web descriptor is complete, or whether the class files of the jar file should be examined for annotations and web fragments at deployment time. If the `metadata-complete` attribute is not specified or is set to "`false`", the deployment tool must examine the class files of the application for annotations, and scan for web fragments.
- @WebServlet: The annotated servlet MUST specify at least one url pattern to be deployed. If the same servlet class is declared in the deployment descriptor under a different name, a new instance of the servlet MUST be instantiated. 如果通过代码注册servlet，则此标记无效
- @WebFilter
- @WebInitParam This annotation is used to specify any init parameters that must be passed to the `Servlet` or the `Filter`. 
- @WebListener
- @MultipartConfig
### Pluggability
For better pluggability and less configuration for developers, in this version (Servlet 3.0) of the specification we are introducing the notion of `web module deployment descriptor fragments` (web fragment). A `web fragment` is a part or all of the `web.xml` that can be specified and included in a library or framework jar's `META-INF` directory. 
A web fragment is a logical partitioning of the web application in such a way that the frameworks being used within the web application can define all the artifacts without asking developers to edit or add information in the web.xml.
可以控制加载顺序
plugin shared copies of frameworks - including being able to plug-in to the web container things like JAX-WS, JAX-RS and JSF that build on top of the web container, using `ServletContainerInitializer`

## Dispatching Requests
When building a Web application, it is often useful to forward processing of a request to another servlet, or to include the output of another servlet in the response. The `RequestDispatcher` interface provides a mechanism to accomplish this. 
When asynchronous processing is enabled on the request, the `AsyncContext` allows a user to dispatch the request `back to the servlet container`
To use a request dispatcher, a servlet calls either the `include` method or `forward` method of the `RequestDispatcher` interface. 
The Container Provider should ensure that the dispatch of the request to a target servlet occurs in the same thread of the same JVM as the original request.
### Obtaining a RequestDispatcher
`RequestDispatcher` may be obtained from the `ServletContext` via the following methods:
- getRequestDispatcher
- getNamedDispatcher
- getRequestDispatcher method is provided in the `ServletRequest` interface.使用相对路径
### The Include Method
If the default servlet is the target of a `RequestDispatch.include()` and the requested resource does not exist, then the default servlet MUST throw `FileNotFoundException`. If the exception isn't caught and handled, and the response hasn’t been committed, the status code MUST be set to `500`.
### The Forward Method
The `forward` method of the `RequestDispatcher` interface may be called by the calling servlet only when no output has been committed to the client.
The `path` elements of the request object exposed to the target servlet must reflect the path used to obtain the `RequestDispatcher`.
The only exception to this is if the `RequestDispatcher` was obtained via the `getNamedDispatcher` method. In this case, the path elements of the request object must reflect those of the `original request`.
### Async
Once you have an `AsyncContext`, you can use it to either complete the processing of the request via the `complete()` method or use one of the `dispatch` methods
