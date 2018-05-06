From the start rkt was built as a pod native container engine. This means that the basic unit of execution is a pod, 
## Build from source
`sudo apt install libssl-dev libacl1-dev libtspi-dev libsystemd-dev make autoconf automake gcc g++ libattr1-dev libcap-dev libpixman-1-dev libglib2.0-dev zlib1g-dev pkg-config python bc systemd-container`

### Commands
- list: list pods
- image list: List images in the local store
- enter: attach
- rm: Remove all files and resources associated with an exited pod
- fetch: Fetch image(s) and store them in the local store
rkt 没有docker -d，rkt doesn't have a daemonize option but relies on the `init system` to do that:
- systemd-run rkt run xxx: 会打印unit name
    - `--slice=machine` option to `systemd-run` places the service in `machine.slice` rather than the host's `system.slice`, isolating containers in their own cgroup area.
    - 这样可通过machinectl/journalctl -M来控制对应的容器
- journalctl -u <unit-name>: 显示stdout／err日志
- systemctl stop <unit-name>：关闭
- systemd-cgls
- systemd-cgls –all
`systemd-machined` is a system service that keeps track of virtual machines and containers, and processes belonging to them.
To ensure that rkt is the main process of the service, the pattern `/bin/sh -c "foo ; rkt run ..."` should be avoided, because in that case the main process is `sh`. If shell invocation is unavoidable, use `exec` to ensure rkt replaces the preceding shell process:

rkt supports socket-activated services.

rkt uses `content addressable storage (CAS)` to store an ACI on disk. 

## ACI
The image format defined by appc and used in rkt is the `Application Container Image`, or ACI. An ACI is a simple tarball bundle of a rootfs (containing all the files needed to execute an application) and an Image Manifest, which defines things like default execution parameters and default resource constraints. ACIs can be built with tools like `acbuild`, `actool`, or `goaci`. Docker images can be converted to ACI using `docker2aci`, although rkt will do this automatically.
## Pod
A pod (as in a pod of whales or pea pod) is a group of one or more containers (such as Docker containers), with shared storage/network, and a specification for how to run the containers. A pod’s contents are always co-located and co-scheduled, and run in a shared context. A pod models an application-specific “logical host” - it contains one or more application containers which are relatively tightly coupled — in a pre-container world, they would have executed on the same physical or virtual machine.
## Stages
Execution with rkt is divided into several distinct stages.
1. invoking process -> stage0: The invoking process uses its own mechanism to invoke the rkt binary.
2. stage0 -> stage1: An ordinary `exec(3)` is being used to replace the stage0 process with the stage1 entrypoint.
3. stage1 -> stage2: The stage1 entrypoint uses its mechanism to invoke the stage2 app executables.
### Stage 0
The first stage is the actual rkt binary itself. When running a pod, this binary is responsible for performing a number of initial preparatory tasks
### Stage 1
The next stage is a binary that the user trusts, and has the responsibility of taking the pod filesystem that was created by stage0, create the necessary container isolation, network, and mounts to launch the pod.
Currently there are three flavors implemented:
- systemd/nspawn: a cgroup/namespace based isolation environment using systemd, and systemd-nspawn.
    - The "host", "src", and "coreos" flavors (referenced to as systemd/nspawn flavors) use systemd-nspawn, and systemd to set up the execution chain.
- kvm: a fully isolated kvm environment.
- fly: a simple chroot only environment.
    - The "fly" flavor uses a very simple mechanism being limited to only execute one child app process. After setting up a chroot'ed environment it simply exec's the target app without any further internal supervision:
### Stage 2
The final stage, stage2, is the actual environment in which the applications run, as launched by stage1.
## Immutable vs. mutable pods
rkt supports two kinds of pod runtime environments: an immutable pod runtime environment, and a new, experimental mutable pod runtime environment.
The immutable runtime environment is currently the default
Conversely, the mutable runtime environment allows users to add, remove, start, and stop applications after a pod has been started. Currently this mode is only available in the experimental rkt app family of subcommands;
## Image lifecycle
- Fetch: in the fetch phase rkt retrieves the requested images. The fetching implementation depends on the provided image argument such as an image string/hash/https URL/file (e.g. example.com/app:v1.0).
- Store: in the store phase the fetched images are saved to the local store. The local store is a cache for fetched images and related data.
- Render: in the render phase, a renderer pulls the required images from the store and renders them so they can be easily used as stage2 content.

Both stage1-2 render modes internally uses the aci renderer. Since an ACI may depend on other ones the acirenderer may require other ACIs. The acirenderer only relies on the ACIStore, so all the required ACIs must already be available in the store. Additionally, since appc dependencies can be found only via discovery, a dependency may be updated and so there can be multiple rendered images for the same ACI.
## Logging and attaching
For each application, rkt support separately configuring stdin/stdout/stderr via runtime command-line flags. The following modes are available:
- interactive: application will be run under the TTY of the parent process. A single application is allowed in the pod, which is tied to the lifetime of the parent terminal and cannot be later re-attached.
- TTY: selected I/O streams will be run under a newly allocated TTY, which can be later used for external attaching.
- streaming: selected I/O streams will be supervised by a separate multiplexing process (running in the pod context). They can be later externally attached.
- logging: selected output streams will be supervised by a separate logging process (running in the pod context). Output entries will be handled as log entries, and the application cannot be later re-attached.
- null: selected I/O streams will be closed. Application will not received the file-descriptor for the corresponding stream, and it cannot be later re-attached.
