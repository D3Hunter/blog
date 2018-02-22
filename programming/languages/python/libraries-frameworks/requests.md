### Request and Response Objects
`requests.get`'ll create a `Request` object, send the request to the server and return a `Response` object which can be accessed with `r = requests.get(); r.request`

### Session object
The `Session` object allows you to `persist certain parameters across requests`. It also persists `cookies` across all requests made from the Session instance, and will use `urllib3's connection pooling`. So if you're making several requests to the same host, the underlying TCP connection will be reused, which can result in a significant performance increase.

```python
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
```

Sessions can also be used to provide default data to the request methods. This is done by providing data to the properties on a Session object:
```python
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
```

Note, however, that method-level parameters will not be persisted across requests, even if using a session.

### Prepared Requests
Whenever you receive a `Response` object from an `API` call or a `Session` call, the request attribute is actually the `PreparedRequest` that was used. In some cases you may wish to do some extra work to the body or headers (or anything else really) before sending a request.
```python
from requests import Request, Session

s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = req.prepare()

# 如果要附带`Session`中的信息，调用以下方法
# prepped = s.prepare_request(req)


# do something with prepped.body and headers
prepped.body = 'No, I want exactly this as the body.'

resp = s.send(prepped)
```
When you are using the prepared request flow, keep in mind that it does not take into account the environment. You can get around this behaviour by explicity merging the environment settings into your session:

```python
# Merge environment settings into session
settings = s.merge_environment_settings(prepped.url, None, None, None, None)
resp = s.send(prepped, **settings)
```

### SSL Cert Verification
Requests verifies SSL certificates for HTTPS requests, just like a web browser. By default, SSL verification is enabled, and Requests will throw a SSLError if it's unable to verify the certificate:

### Body Content Workflow
By default, when you make a request, the body of the response is downloaded immediately. You can override this behaviour and defer downloading the response body until you access the Response.content attribute with the `stream=True` parameter:

### Keep-Alive
Excellent news — thanks to urllib3, keep-alive is 100% automatic within a session! Any requests that you make within a session will automatically reuse the appropriate connection!

Note that connections are only released back to the pool for reuse once all body data has been read; be sure to either set stream to False or read the content property of the Response object.

### Streaming Uploads
Requests supports streaming uploads, which allow you to send large streams or files without reading them into memory. To stream and upload, simply provide a file-like object for your body:

### Chunk-Encoded Requests
Requests also supports Chunked transfer encoding for outgoing and incoming requests. To send a chunk-encoded request, simply provide a generator (or any iterator without a length) for your body:

It is strongly recommended that you `open files in binary mode`. This is because Requests may attempt to provide the `Content-Length` header for you, and if it does this value will be set to the number of bytes in the file. Errors may occur if you open the file in text mode.

### POST Multiple Multipart-Encoded Files
You can send multiple files in one request. 

