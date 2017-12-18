an OCI Image, consisting of a manifest, an image index (optional), a set of filesystem layers, and a configuration.

At a high level the image manifest contains metadata about the contents and dependencies of the image including the content-addressable identity of one or more filesystem layer changeset archives that will be unpacked to make up the final runnable filesystem.
The image configuration includes information such as application arguments, environments, etc.
The image index is a higher-level manifest which points to a list of manifests and descriptors. Typically, these manifests may provide different implementations of the image, possibly varying by platform or other attributes.

## Content Descriptors
- An OCI image consists of several different components, arranged in a Merkle Directed Acyclic Graph (DAG).
- References between components in the graph are expressed through Content Descriptors.
- A Content Descriptor (or simply Descriptor) describes the disposition of the targeted content.
- A Content Descriptor includes the type of the content, a content identifier (digest), and the byte-size of the raw content.
- Descriptors SHOULD be embedded in other formats to securely reference external content.
- Other formats SHOULD use descriptors to securely reference external content.

A descriptor consists of a set of `properties` encapsulated in key-value fields. primary properties that constitute a Descriptor:
- mediaType
- digest
- size: specifies the size, in bytes, of the raw content.
- urls
- annotations: arbitrary metadata for this descriptor
