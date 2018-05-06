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
## Image Layout
- The OCI Image Layout is directory structure for OCI content-addressable blobs and location-addressable references (refs).
- This layout MAY be used in a variety of different transport mechanisms: archive formats (e.g. tar, zip), shared filesystem environments (e.g. nfs), or networked file fetching (e.g. http, ftp, rsync).
The image layout is as follows:
- blobs directory
- oci-layout file
- index.json file
## Image Manifest
contains layers
- content-addressable images
- allow multi-architecture images
- translatable to the OCI Runtime Specification.
## Image Index
The image index is a higher-level manifest which points to specific image manifests, ideal for one or more platforms. 

## Whiteouts
A whiteout file is an empty file with a special filename that signifies a path should be deleted.
## Terminology
- Layer
    - Image filesystems are composed of layers.
    - Each layer represents a set of filesystem changes in a tar-based layer format, recording files to be added, changed, or deleted relative to its parent layer.
    - Layers do not have configuration metadata such as environment variables or default arguments - these are properties of the image as a whole rather than any particular layer.
    - Using a layer-based or union filesystem such as AUFS, or by computing the diff from filesystem snapshots, the filesystem changeset can be used to present a series of image layers as if they were one cohesive filesystem.
- Image JSON
    - Each image has an associated JSON structure which describes some basic information about the image such as date created, author, as well as execution/runtime configuration like its entrypoint, default arguments, networking, and volumes.
    - The JSON structure also references a cryptographic hash of each layer used by the image, and provides history information for those layers.
    - This JSON is considered to be immutable, because changing it would change the computed ImageID.
    - Changing it means creating a new derived image, instead of changing the existing image.
- Layer DiffID: the digest over the layer's `uncompressed` tar archive and serialized in the descriptor digest format
    - Do not confuse DiffIDs with `layer digests`, often referenced in the manifest, which are digests over `compressed or uncompressed` content.
- ImageID: Each image's ID is given by the SHA256 hash of its `configuration JSON`
