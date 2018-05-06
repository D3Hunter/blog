- rkt can download, cryptographically verify, and run application container images. It is not designed to run "full system images" but instead individual applications such as web apps, databases, or caches. As rkt does not have a centralized daemon it can be integrated with init systems such as upstart and systemd.
- rkt has no centralized "init" daemon, instead launching containers directly from client commands, making it compatible with init systems such as systemd, upstart, and others.
### vs Docker
The Docker Engine is an application container runtime implemented as a central API daemon.
rkt; however, along with "Docker Images", rkt can also download and run "App Container Images" (ACIs) specified by the App Container Specification (appc).
### vs runC
runC is a low-level container runtime and an implementation of the Open Container Initiative specification. runC exposes and expects a user to understand low-level details of the host operating system and configuration.
### vs containerd
containerd is a daemon to control runC. It has a command-line tool called ctr which is used to interact with the containerd daemon.
Unlike the Docker daemon it has a reduced feature set; not supporting image download, for example.
### vs LXC/LXD
LXC is a system container runtime designed to execute "full system containers", which generally consist of a full operating system image. An LXC process, in most common use cases, will boot a full Linux distribution such as Debian, Fedora, Arch, etc, and a user will interact with it similarly to how they would with a Virtual Machine image.
LXD is similar to LXC but is a REST API on top of liblxc which forks a monitor and container process. This ensures the LXD daemon is not a central point of failure and containers continue running in case of LXD daemon failure. All other details are nearly identical to LXC.
### vs OpenVZ
OpenVZ is a system container runtime designed to execute "full system containers" which are generally a full system image. An OpenVZ process, in most common use cases, will boot a full Linux Distro such as Debian, Fedora, Arch, etc and a user will interact with it similarly to a Virtual Machine image.
### vs systemd-nspawn
systemd-nspawn is a container runtime designed to execute a process inside of a Linux container. systemd-nspawn gets its name from "namespace spawn", which means it only handles process isolation and does not do resource isolation like memory, CPU, etc.
### vs machinectl
machinectl is a system manager that can be used to query and control the state of registered systems on a `systemd` host.
### vs qemu-kvm, lkvm
qemu-kvm and lkvm are userspace tools that execute a full system image inside of a Virtual Machine using the Linux KVM infrastructure. A system image will commonly include a boot loader, kernel, root filesystem and be pre-installed with applications to run on boot.
