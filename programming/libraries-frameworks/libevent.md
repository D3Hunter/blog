event_base - `eventbuffer`

#### Running the loop
Once you have an event_base with some events registered (see the next section about how to create and register events), you will want Libevent to wait for events and alert you about them.
- `event_base_loop`
- `event_base_dispatch`
#### Stopping the loop
- `event_base_loopexit`
- `event_base_loopbreak`
- `event_base_got_exit`
- `event_base_got_break`

#### http
`evhttp_new`
`evhttp_set_gencb`
`evhttp_bind_socket_with_handle`

#### utils
`evutil_parse_sockaddr_port`

### Event
Constructing event objects: `event_new`, `event_free`
Manually activating an event: `event_active`
Once you have constructed an event, it won’t actually do anything until you have made it pending by adding it. You do this with `event_add`: