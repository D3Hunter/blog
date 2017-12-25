The WSGI interface has two sides: `the "server" or "gateway" side`, and `the "application" or "framework" side`. The server side invokes a callable object that is provided by the application side.
In addition to ease of implementation for existing and future frameworks and servers, it should also be easy to create `request preprocessors`, `response postprocessors`, and other `WSGI-based "middleware"` components that look like an application to their containing server, while acting as a server for their contained applications.

The application object is simply a callable object that accepts two `positional` arguments. Application objects must be able to be invoked more than once, as virtually all servers/gateways (other than CGI) will make such repeated requests.
The term "object" should not be misconstrued as requiring an actual object instance: a `function`, `method`, `class`, or `instance with a __call__ method` are all acceptable for use as an application object.
- function/method/`instance with a __call__ method`
- class: implement `__iter__` method
simple code:

    def simple_app(environ, start_response):
        """Simplest possible application object"""
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return ['Hello world!\n']


The server or gateway invokes the application callable once for each request it receives from an HTTP client, that is directed at the application.

The `environ` parameter is a dictionary object, containing CGI-style environment variables. This object must be a `builtin Python dictionary` (not a subclass, UserDict or other dictionary emulation), and the application is allowed to modify the dictionary in any way it desires.
The `start_response` parameter is a callable accepting two required positional arguments, and one optional argument. The `start_response` callable must return a `write(body_data)` callable that takes one positional parameter: a string to be written as part of the HTTP response body.
When called by the server, the `application object` must return an iterable yielding zero or more strings.
The `start_response` callable must not actually transmit the response headers.
New WSGI applications and frameworks should not use the `write()` callable if it is possible to avoid doing so. 
