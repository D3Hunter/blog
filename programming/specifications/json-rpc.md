JSON-RPC is a stateless, light-weight remote procedure call (RPC) protocol. Primarily this specification defines several data structures and the rules around their processing.

### Request object
The Request object has the following members:
- jsonrpc: A String specifying the version of the JSON-RPC protocol. MUST be exactly "2.0".
- method: A String containing the name of the method to be invoked. Method names that begin with the word `rpc` followed by a period character (U+002E or ASCII 46) are reserved for rpc-internal methods and extensions and MUST NOT be used for anything else.
- params: A Structured value that holds the parameter values to be used during the invocation of the method. This member MAY be omitted.
- id: An identifier established by the Client that MUST contain a String, Number, or NULL value if included. If it is not included it is assumed to be a notification. The value SHOULD normally not be Null [1] and Numbers SHOULD NOT contain fractional parts. The Server MUST reply with the same value in the Response object if included. This member is used to correlate the context between the two objects.

A `Notification` is a Request object without an "id" member. A Request object that is a Notification signifies the Client's lack of interest in the corresponding Response object, and as such no Response object needs to be returned to the client. 

### Response object
When a rpc call encounters an error, the Response Object MUST contain the error member with a value that is a Object with the following members:
- code
- message
- data

### Batch
To send several Request objects at the same time, the Client MAY send an `Array` filled with Request objects.
The Server should respond with an `Array` containing the corresponding Response objects, after all of the batch Request objects have been processed. A Response object SHOULD exist for each Request object, except that there SHOULD NOT be any Response objects for notifications.

