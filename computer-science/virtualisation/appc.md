`App Container (appc)` is a well-specified and community developed specification for application containers. appc defines several independent but composable aspects involved in running application containers, including an image format, runtime environment, and discovery mechanism for application containers.

With the formation of the `Open Container Initiative (OCI)`, the industry has come together in a single location to define specifications around applications containers.
It is highly encouraged that parties interested in container specifications join the `OCI` community.
The `App Container Image format (ACI)` maps more or less directly to the `OCI Image Format Specification`, with the exception of signing and dependencies.
The `App Container Executor (ACE)` specification is related conceptually to the `OCI Runtime Specification`, with the notable distinctions that the latter does not support pods and generally operates at a lower level of specification.
`App Container Image Discovery` does not yet have an equivalent specification in the OCI project (although it has been discussed and proposed)